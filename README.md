# Addy-skills

Addy Osmani 의 글 "Critical thinking when agents do the work" 를 바탕으로 만든 에이전트 스킬 모음입니다.
에이전트에게 일을 맡기는 흐름의 지점마다 비판적 사고를 일부러 끼워 넣습니다.

## 메인 스킬

먼저 [agent-oversight](skills/agent-oversight/SKILL.md) 를 씁니다.
글에서 가장 실행 가능한 네 원칙만 남긴 짧은 스킬입니다.

1. 검증됨을 먼저 정한다. 끝난 뒤에 정하면 어떤 결과든 합리화한다.
2. 요약보다 명령과 출력을 먼저 본다. 에이전트의 자기 보고는 증거가 아니다.
3. 감독할 힘을 지킨다. 감독에 필요한 기술은 감독 대상에게 맡길수록 줄어든다.
4. 요약 말고 원본을 넘긴다. 에이전트끼리 요약만 넘기면 세 번째 에이전트는 원본을 읽지 않는다.

아래 여섯 스킬은 상황별 자세한 절차입니다.

## 스킬과 순서

일이 흘러가는 순서대로 놓았습니다.

| 순서 | 스킬 | 언제 쓰나 | 핵심 |
|---|---|---|---|
| 1 | [clarify-intent-before-work](skills/clarify-intent-before-work/SKILL.md) | 일을 시작하거나 맡기기 전 | 가설, 도움인지 대신인지, 브리프, 흐리면 인터뷰 |
| 2 | [verification-loop](skills/verification-loop/SKILL.md) | 체크를 세울 때와 끝내기 직전 | 검증됨을 먼저 정하기, 스스로 검증할 수단, 증명한 것과 증명하지 않은 것, 놓친 것 재점검, 체크 강화 |
| 3 | [review-agent-output](skills/review-agent-output/SKILL.md) | 다른 에이전트의 결과를 받았을 때 | 증거 먼저, 대신 내린 결정 찾기, 숫자 하나와 원본 하나 확인 |
| 4 | [rebuild-understanding](skills/rebuild-understanding/SKILL.md) | 결과를 내 것으로 이해해야 할 때 | 모르는 곳 찾기, 필요한 조각만 다시 세우기, 변경 보고서와 퀴즈, 연습 점검 |
| 5 | [decision-support](skills/decision-support/SKILL.md) | 사람이 큰 결정을 내릴 때 | 틀리려면 무엇이 참이어야 하나, 반론, 결정 요청 형식 |
| 6 | [capture-misses](skills/capture-misses/SKILL.md) | 같은 지적이나 실수가 반복될 때 | 원인을 테스트, 훅, 스킬, 메모리에 남기기 |

```
1 의도 분명히 하기
   |
2 검증 루프 (에이전트가 스스로 확인하고, 끝낼 때 증명 범위를 보고)
   |
3 받은 결과 검토
   |
4 내 이해 다시 세우기
   |
5 결정 돕기
   |
6 기준 미달 남기기 (어느 단계에서든)
```

## 글의 질문이 어느 스킬에 있나

| 글의 질문 | 스킬 |
|---|---|
| 묻기 전에 가설을 세웠는가 | 1, 5 |
| 생각을 도와달라는 건가, 대신 해달라는 건가 | 1 |
| 명확하지 않으면 에이전트가 나를 인터뷰하게 했는가 | 1 |
| 에이전트가 자기 작업을 검증할 수 있는가 | 2 |
| 검증됨을 미리 정했는가 | 1, 2 |
| 체크가 초록이면 무엇을 증명했고 무엇을 증명하지 않았는가 | 2, 3 |
| 놓친 게 있는지 다시 점검했는가 | 2 |
| 체크를 강화해 내 손이 덜 가게 했는가 | 2, 6 |
| 에이전트가 대신 내린 결정과 가정은 무엇인가 | 2, 3, 4 |
| 필요할 때 이해를 다시 세울 수 있는가 | 4 |
| 나는 무엇을 더 이상 연습하지 않는가 | 4 |
| 이게 틀리려면 무엇이 참이어야 하는가 | 5 |
| 다른 각도의 반론을 들어봤는가 | 5 |
| 유지보수할 사람 앞에서 걸 수 있는가 | 2, 5 |
| 기준에 못 미친 이유를 다시 안 일어나게 남겼는가 | 6 |

## 공통 기준

- 에이전트의 도움을 받아도 결과를 설명할 수 없다면 이미 책임을 넘긴 것입니다.
- 되돌리기 쉬운 일은 가볍게, 다른 사람이 결과를 감당하는 일은 끝까지 점검합니다.
- 모든 스킬은 사람이 읽는 글을 내보냅니다.
  그래서 humanizer 스킬 적용, 가운뎃점과 줄표와 화살표 금지, 낱말을 잇는 하이픈 금지, 문장마다 줄바꿈을 기본으로 넣었습니다.

## 설치

Claude Code 플러그인으로 설치합니다.
스킬 일곱 개와 SessionStart 훅이 함께 들어옵니다.

```
/plugin install addy-skills --marketplace holiday0726/Addy-skills
```

예전 판 Claude Code 에서는 두 줄로 나눠 설치합니다.

```
/plugin marketplace add holiday0726/Addy-skills
/plugin install addy-skills@addy-skills
```

스킬 이름은 `addy-skills:agent-oversight` 처럼 앞에 플러그인 이름이 붙습니다.

## SessionStart 훅

세션을 시작하거나 대화를 비우거나 압축할 때, 언제 어느 스킬을 쓰는지 표를 컨텍스트에 넣습니다.
권유만 하고 막지는 않습니다.
사용자나 프로젝트 지침이 다르게 정하면 그쪽을 따르라고 함께 적었습니다.
표 내용은 [hooks/usage.md](hooks/usage.md) 에 있습니다.

## 출처

- Addy Osmani, "Critical thinking when agents do the work"
