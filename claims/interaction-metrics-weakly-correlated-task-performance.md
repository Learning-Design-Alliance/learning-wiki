---
type: claim
title: Behavioral interaction metrics are weakly or inconsistently correlated with task performance in AI-assisted programming
description: Behavioral interaction metrics are weakly or inconsistently correlated with task performance in AI-assisted programming
id: interaction-metrics-weakly-correlated-task-performance
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
  - id: jessica-hutchison-2026-2
    resource: "https://doi.org/10.1145/3803400.3809394"
    title: "Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394"
    author: Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil
    q: 2
    i: 1
    kind: associational
    rigour: 1
---

# Behavioral interaction metrics are weakly or inconsistently correlated with task performance in AI-assisted programming

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2` · `i1`–`i2`

## Subclaims
`q2 i2` Number of runs showed the strongest positive correlation with task performance (rho = 0.26), though the relationship was modest. [→ Jessica Hutchison 2026](#jessica-hutchison-2026)
`q2 i1` Failed attention check rate had only a weak negative correlation with task performance (rho = -0.17), so passing attention checks did not necessarily mean better task performance. [→ Jessica Hutchison 2026 (2)](#jessica-hutchison-2026-2)

## Evidence

### Jessica Hutchison 2026

Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394

`q2 · i2` · `associational · r1`

Spearman correlation analysis of session-level metrics from the 55-student lab study. Number of runs (mean 15.5, SD 12.6) was the strongest positive correlate of task performance (mean 10.4 of 26 tests, SD 12.9) with effect size rho = 0.26; the article notes this "aligns with previous studies" linking running code to higher performance.

> "Among the examined metrics,NRshowed the strongest positive correlation withTP (𝜌= 0.26), although the relationship was modest."

### Jessica Hutchison 2026 (2)

Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394

`q2 · i1` · `associational · r1`

In the same correlation analysis, failed attention check rate and task performance were weakly negatively correlated with effect size rho = -0.17. The authors conclude that failed attention checks "does not represent critical engagement, but it does suggest potential misuse."

> "FCRand TPhad a weak negative correlation ( 𝜌=− 0.17). This suggests that students who passed attention checks did not necessarily perform better on the task."

## Discussion


## Related Claims
- [Longer dwell time on AI suggestions is associated with better attention check performance but slightly lower task performance](dwell-time-attention-checks-versus-task-performance.md) — related
- [AI assistance reduces subjective mental effort across all tasks even when it does not reduce completion time, dissociating time and effort](ai-effort-reduction-time-effort-dissociation.md) — related
- [Higher tab accept rates are strongly associated with failing attention checks among CS1 students using an AI code completion tool](tab-accept-rate-strongly-associated-failed-attention-checks.md) — related
