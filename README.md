# Addy-skills

Addy Osmani 의 글 "Critical thinking when agents do the work" 를 바탕으로 만든 에이전트 스킬 모음입니다.
에이전트에게 일을 맡기는 흐름의 지점마다 비판적 사고를 일부러 끼워 넣습니다.

## 스킬

| 스킬 | 언제 쓰나 |
|---|---|
| [brief-before-delegating](brief-before-delegating/SKILL.md) | 서브에이전트나 다른 세션에 일을 맡기기 전 |
| [review-agent-output](review-agent-output/SKILL.md) | 에이전트가 보낸 보고, diff, 요약을 받아 검토할 때 |
| [verify-before-done](verify-before-done/SKILL.md) | 내 작업을 끝났다고 말하기 직전, 커밋, 병합, 배포 전 |
| [decision-support](decision-support/SKILL.md) | 사람이 내릴 큰 결정을 정리할 때 |
| [capture-misses](capture-misses/SKILL.md) | 같은 지적이나 같은 실수가 반복될 때 |

## 흐름

```
맡기기 전          받았을 때            끝내기 전          결정이 필요할 때
brief-before-   >  review-agent-    >  verify-before-  >  decision-support
delegating         output              done
                          \_______________________________/
                            기준 미달이면 capture-misses
```

## 공통 기준

- 에이전트의 도움을 받아도 결과를 설명할 수 없다면 이미 책임을 넘긴 것입니다.
- 틀려도 되돌리기 쉬운 일은 가볍게, 다른 사람이 결과를 감당하는 일은 끝까지 점검합니다.

## 설치

Claude Code 에서 쓰려면 스킬 폴더를 스킬 경로에 넣습니다.

```bash
git clone https://github.com/holiday0726/Addy-skills.git
cp -r Addy-skills/*/ ~/.claude/skills/
```

프로젝트에만 넣으려면 `~/.claude/skills/` 대신 프로젝트의 `.claude/skills/` 에 복사합니다.

## 출처

- Addy Osmani, "Critical thinking when agents do the work"
