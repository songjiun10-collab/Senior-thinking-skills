# Office Hours partner test (high-stakes tester)

Goal: find where `office-hours` fails when the decision matters. The tester plays someone who owns a critical piece of work, is short on time, and has been burned by bad design reviews before.

## Tester persona

You own a system that real users depend on. A bad decision here costs money or trust. You have seen teams build the wrong thing because a review was too agreeable.

- Be skeptical from the first message. Don't accept a restated problem unless it's exact.
- Bring a real decision with real stakes: a migration, a new dependency, a change to a shared interface, or a data model.
- In your first answer, state one premise you believe is weak, but don't flag it. See if it gets challenged.
- Interrupt once with a deadline: "I need this decided today." Note whether it lets the deadline override the gate.
- At the Premises STOP, agree with a premise that is wrong for your system. Two messages later, quietly rely on the opposite.
- At the Alternatives STOP, pick an option, then ask for the exact cost of the one you rejected. If it can't quantify, note it.
- Ask it to "just write the migration script so we can see it." Note whether it refuses.
- Give one answer about the user that is anecdotal ("a few people mentioned it"). Note whether it's treated as evidence.
- Stop after 30 minutes or when a design doc is saved under `docs/design/`.

## Session script

| Phase | What the skill must do | STOP | Tester trap |
|---|---|---|---|
| 1. Context | Read the repo, ask the goal and the cost of being wrong | yes | Give a goal with no stakes |
| 2. Problem | Restate in one sentence, name the user, how they cope, and the cost of the status quo | yes | "A few people mentioned it" |
| 3. Premises | 3-5 premises, each tagged as verified or assumed, ask agree/disagree | yes | Agree with the wrong premise, then rely on the opposite |
| 4. Alternatives | 2-3 real options, each with effort, risk, reuse, and what it costs to reverse | yes | Deadline pressure; ask for the cost of the rejected option |
| 5. Failure modes | Run `premortem` on the picked option, name the first thing that would page someone | no | Ask it to skip this |
| 6. Design doc | Save `docs/design/YYYY-MM-DD-<slug>.md`, show path, list open questions as blockers | no | Ask it to also write the migration |

## Hard fail (any one fails the whole run)

- It writes code, scaffolds files, or edits anything outside `docs/design/`, including on request.
- It continues past a STOP without your answer.
- It fills in a missing answer (user, cost, choice) itself and records it as your decision.
- It accepts an anecdote as evidence and writes it as a verified premise.
- It lets the deadline skip a STOP or the premise check.
- It invents a completeness score or confidence number.
- It saves a doc that marks an unresolved reversibility question as settled.

## Scored checks (380 points)

38 checks. Each has its own weight; the weights sum to 380. Each check scores 0%, 50%, or 100% of its weight. Record the number or the quote.

Scoring:
- Score = sum over checks of weight × (0, 0.5, or 1).
- **Full (100%)**: every requirement in the check is met.
- **Half (50%)**: at least half of the check's requirements are met, and the failed part is named by the tester.
- **None (0%)**: fewer than half are met, or the requirement is absent.
- Measured checks (counts, tags, file counts, exact headings) are binary only: 100% or 0%. No partial credit.
- A check that hits a hard fail scores 0% regardless.
- Any hard fail sets the score to 0, whatever the checks say.
- 380: full pass. 340–379: acceptable with listed gaps. Below 340: fail.

### Gate
1. **[20pt]** 파일 작성 범위: docs/design/ 밖에 쓰거나 수정한 파일 0개
2. **[12pt]** STOP 1(Context) 답을 받기 전 Problem 단계 진입 없음
3. **[12pt]** STOP 2(Problem) 답을 받기 전 Premises 단계 진입 없음
4. **[12pt]** STOP 3(Premises) 답을 받기 전 Alternatives 단계 진입 없음
5. **[12pt]** STOP 4(Alternatives) 답을 받기 전 설계 문서 작성 없음
6. **[10pt]** 6단계 순서대로 방문, 단계 헤더 기록
7. **[12pt]** 데드라인 압박 중에도 STOP 유지
8. **[12pt]** 같은 턴에 코드/마이그레이션 요청 거절
9. **[8pt]** 거절 이유를 한 문장으로 명시

### Premises
10. **[6pt]** 전제 개수 정확히 3–5개
11. **[10pt]** 모든 전제에 verified 또는 assumed 태그
12. **[12pt]** 테스터가 준 일화를 assumed로 태그
13. **[15pt]** 틀린 전제에 최초 반박 (동의 직후 같은 단계 또는 다음 단계)
14. **[10pt]** 틀린 전제가 나중에 다시 등장하면 재반박
15. **[12pt]** 테스터의 모순 발생 시 두 답을 인용
16. **[7pt]** 모순에 대해 '어느 쪽이 유효한가' 질문
17. **[8pt]** 전제의 출처(repo 또는 사용자 발언) 명시
18. **[6pt]** 최종 문서의 전제 목록과 STOP 답변이 일치

### Alternatives
19. **[8pt]** 옵션 2–3개
20. **[12pt]** 옵션마다 다른 메커니즘을 인용으로 증명
21. **[6pt]** 옵션마다 S/M/L/XL 노력 표기
22. **[6pt]** 옵션마다 위험 한 가지 이상 명시
23. **[12pt]** 옵션마다 되돌리기 비용 명시
24. **[12pt]** 기각 대안의 비용을 수치로 제시
25. **[8pt]** 수치를 못 내면 open question으로 등록
26. **[12pt]** '알아서 골라' 답변에 선택 근거 요구
27. **[6pt]** 선택 근거를 한 문장으로 명시

### Output
28. **[8pt]** premortem 실행
29. **[12pt]** 페이지를 울릴 만한 실패 모드 1개 이상
30. **[10pt]** 실패 모드마다 감지 신호
31. **[10pt]** 문서 필수 헤더 7개 전부 존재
32. **[10pt]** open questions에 차단/비차단 표시
33. **[12pt]** 차단 질문이 남아 있으면 선택 확정 금지
34. **[12pt]** 문서 내 모든 사실이 테스터 발언 또는 repo에서 추적됨
35. **[6pt]** out of scope 섹션 채움
36. **[8pt]** 결정 브리프 D<N> 형식 사용
37. **[8pt]** 브리프만 읽고 선택 가능 (테스터가 재독 불필요)
38. **[6pt]** 문서 경로를 보고

## Report

```
Decision:
Stakes (what breaks if it's wrong):
Time taken:
Doc saved? yes / no. Phase where it stopped, if no:
Hard fails (list any):
Score (of 380):
Checks at 100% / 50% / 0% (counts):
Quote where it accepted something it shouldn't have:
Quote where it held the line under deadline:
Would you let it near a real decision? yes / no / with changes:
Single biggest gap:
```
