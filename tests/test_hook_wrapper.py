#!/usr/bin/env python3
"""git 문구 검사 입구(hooks/git-message-check) 시험: 꺼져 있으면 Python 없이 통과, 켜지면 검사."""
import json
import os
import subprocess
import sys

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'hooks', 'git-message-check')
BAD = json.dumps({'tool_name': 'Bash', 'tool_input': {'command': 'git commit -m "파서를 복구했습니다"'}},
                 ensure_ascii=False).encode('utf-8')
ENV = {k: v for k, v in os.environ.items() if k != 'CLAUDE_PLUGIN_OPTION_GIT_MESSAGE_CHECK'}
PY = sys.executable.replace('\\', '/')


def denied(flag, py, extra=None):
    r = subprocess.run(['bash', HOOK, flag, py], input=BAD, capture_output=True, env=dict(ENV, **(extra or {})))
    assert r.returncode == 0, r.stderr
    return b'"deny"' in r.stdout


CASES = [
    ('꺼짐', False, 'false', PY, None),
    ('치환 안 된 값', False, '${user_config.git_message_check}', '${user_config.python}', None),
    ('꺼져 있으면 Python 이 없어도 통과', False, 'false', '/no/such/python', None),
    ('켜짐', True, 'true', PY, None),
    ('환경 변수로 켜짐', True, '', PY, {'CLAUDE_PLUGIN_OPTION_GIT_MESSAGE_CHECK': 'true'}),
]

fail = 0
for name, want, flag, py, extra in CASES:
    if denied(flag, py, extra) != want:
        fail += 1
        print('FAIL', name)
print('%d 건 실패' % fail if fail else 'ok')
sys.exit(1 if fail else 0)
