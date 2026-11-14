#!/usr/bin/env python3
"""git 문구 검사 입구 시험: hooks.json 의 command 문자열을 그대로 bash -c 로 돌린다.

- 셸 형태 command 에 ${user_config.*} 가 있으면 Claude Code 가 훅을 돌리지 않고 거부한다
- 설정값은 CLAUDE_PLUGIN_OPTION_<KEY> 환경 변수로만 받는다
- 꺼져 있으면 Python 없이 통과, 켜지면 검사
"""
import json
import os
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
HOOKS = json.load(open(os.path.join(ROOT, 'hooks', 'hooks.json'), encoding='utf-8'))['hooks']
BAD = json.dumps({'tool_name': 'Bash', 'tool_input': {'command': 'git commit -m "파서를 복구했습니다"'}},
                 ensure_ascii=False).encode('utf-8')
GOOD = json.dumps({'tool_name': 'Bash', 'tool_input': {'command': 'git commit -m "파서 복구"'}},
                  ensure_ascii=False).encode('utf-8')
OPT = ('CLAUDE_PLUGIN_OPTION_GIT_MESSAGE_CHECK', 'CLAUDE_PLUGIN_OPTION_PYTHON')
ENV = {k: v for k, v in os.environ.items() if k not in OPT}
ENV['CLAUDE_PLUGIN_ROOT'] = ROOT
PY = sys.executable.replace('\\', '/')

fail = 0


def check(name, ok):
    global fail
    if not ok:
        fail += 1
        print('FAIL', name)


# 셸 형태 command 는 ${user_config.*} 를 쓸 수 없다(exec 형태 args 만 치환됨)
for event, groups in HOOKS.items():
    for g in groups:
        for h in g['hooks']:
            if 'args' not in h:
                check('%s 셸 형태 command 에 ${user_config.*}' % event, '${user_config.' not in h['command'])

CMD = HOOKS['PreToolUse'][0]['hooks'][0]['command']


def run(payload, opts):
    r = subprocess.run(['bash', '-c', CMD], input=payload, capture_output=True, env=dict(ENV, **opts))
    return r.returncode, r.stdout, r.stderr


CASES = [
    # 이름, 입력, 환경 변수, 막혀야 하나
    ('설정 없음', BAD, {}, False),
    ('빈 값', BAD, {OPT[0]: ''}, False),
    ('꺼짐', BAD, {OPT[0]: 'false'}, False),
    ('꺼져 있으면 Python 이 없어도 통과', BAD, {OPT[0]: 'false', OPT[1]: '/no/such/python'}, False),
    ('켜짐, Python 설정 없음은 python3', BAD, {OPT[0]: 'true'}, True),
    ('켜짐, Python 빈 값은 python3', BAD, {OPT[0]: 'true', OPT[1]: ''}, True),
    ('켜짐, Python 경로 지정', BAD, {OPT[0]: 'true', OPT[1]: PY}, True),
    ('켜짐, 대문자 TRUE', BAD, {OPT[0]: 'TRUE', OPT[1]: PY}, True),
    ('켜짐, 규칙 지킨 문구는 통과', GOOD, {OPT[0]: 'true', OPT[1]: PY}, False),
]

for name, payload, opts, want in CASES:
    code, out, err = run(payload, opts)
    check(name + ' 종료 코드 0 (stderr: %r)' % err[:200], code == 0)
    check(name + (' 막힘' if want else ' 통과'), (b'"deny"' in out) == want)

print('%d 건 실패' % fail if fail else 'ok')
sys.exit(1 if fail else 0)
