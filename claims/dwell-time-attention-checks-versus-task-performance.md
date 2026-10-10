---
type: claim
title: Longer dwell time on AI suggestions is associated with better attention check performance but slightly lower task performance
description: Longer dwell time on AI suggestions is associated with better attention check performance but slightly lower task performance
id: dwell-time-attention-checks-versus-task-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: jessica-hutchison-2026
    resource: "https://doi.org/10.1145/3803400.3809394"
    title: "Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394"
    author: Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil
    q: 2
    i: 2
    kind: associational
    rigour: 1
---

# Longer dwell time on AI suggestions is associated with better attention check performance but slightly lower task performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2` · `i2` medium

## Subclaims
`q2 i2` Average dwell time negatively correlated with failed attention check rate (rho = -0.26), meaning more time on a suggestion was associated with passing more attention checks. [→ Jessica Hutchison 2026](#jessica-hutchison-2026)

## Evidence

### Jessica Hutchison 2026

Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394

`q2 · i2` · `associational · r1`

Spearman correlation of session-level aggregates from the 55-student Clover lab study. Average dwell time (mean 12.2 seconds, SD 8.1) negatively correlated with failed attention check rate with effect size rho = -0.26; the article interprets that students who "spent more time looking at a suggestion passed more attention checks."

> "ADTnegatively correlated ( 𝜌=− 0.26) withFCR, which could mean the less time students spend on a suggestion, the more likely they are to have highFCR."

## Discussion


## Learner Variables
- [Attention](../learner-variables/attention.md) — predictor: learners who differ on it differ in outcomes
- [Time and Continuity](../learner-variables/time-and-continuity.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Behavioral interaction metrics are weakly or inconsistently correlated with task performance in AI-assisted programming](interaction-metrics-weakly-correlated-task-performance.md) — related
- [Higher tab accept rates are strongly associated with failing attention checks among CS1 students using an AI code completion tool](tab-accept-rate-strongly-associated-failed-attention-checks.md) — related
