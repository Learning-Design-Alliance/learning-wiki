---
type: claim
title: Log analysis reveals novel post-acceptance behaviors (slow tab accept, slow accept then modify) that show suggestion acceptance is a multi-step process
description: Log analysis reveals novel post-acceptance behaviors (slow tab accept, slow accept then modify) that show suggestion acceptance is a multi-step process
id: novel-post-acceptance-behavioral-metrics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: jessica-hutchison-2026
    resource: "https://doi.org/10.1145/3803400.3809394"
    title: "Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394"
    author: Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Log analysis reveals novel post-acceptance behaviors (slow tab accept, slow accept then modify) that show suggestion acceptance is a multi-step process

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Of 71 slow accept events, 10 were slow tab accepts and 53 were slow accept then modify events, together 75% of slow accepts; slow accept then delete was not observed. [→ Jessica Hutchison 2026](#jessica-hutchison-2026)

## Evidence

### Jessica Hutchison 2026

Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394

`q2 · i?` · `associational · r1`

Descriptive log analysis of the 55-student Clover study identified three new behavioral metrics: slow tab accept, slow accept then modify, and slow accept then delete. The counts are descriptive; no effect size or inferential test is printed.

> "Of the 71 SAevents, we observed 10STAevents and 53SMevents.STAand SMaccounted for 75% of ourSA, making it a majority.SDwas not observed in our log data, but logically follows from the possibility ofSM."

## Discussion


## Related Claims
- [Higher tab accept rates are strongly associated with failing attention checks among CS1 students using an AI code completion tool](tab-accept-rate-strongly-associated-failed-attention-checks.md) — related
- [Longer dwell time on AI suggestions is associated with better attention check performance but slightly lower task performance](dwell-time-attention-checks-versus-task-performance.md) — related
- [AI-section students framed the AI as a collaborative partner even when logs showed one-shot imperatives and rapid acceptance (Illusion of Dialogue)](illusion-of-dialogue-partnership-framing.md) — related
