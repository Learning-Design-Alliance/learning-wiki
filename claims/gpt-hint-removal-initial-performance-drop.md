---
type: claim
title: When GPT hints were unavailable on harder tasks, the experimental group solved correctly less often in the initial attempts but reached comparable correctness by the seventh attempt
description: When GPT hints were unavailable on harder tasks, the experimental group solved correctly less often in the initial attempts but reached comparable correctness by the seventh attempt
id: gpt-hint-removal-initial-performance-drop
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: maciej-pankiewicz-ryan-s-baker-2023
    resource: "https://doi.org/10.58459/icce.2023.950"
    title: "Maciej Pankiewicz & Ryan S. Baker. (2023). Large Language Models (GPT) for automating feedback on programming assignments. Proceedings of the 31st International Conference on Computers in Education. [doi:10.58459/icce.2023.950](https://doi.org/10.58459/icce.2023.950)"
    author: "Maciej Pankiewicz & Ryan S. Baker"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: maciej-pankiewicz-ryan-s-baker-2023-2
    resource: "https://doi.org/10.58459/icce.2023.950"
    title: "Maciej Pankiewicz & Ryan S. Baker. (2023). Large Language Models (GPT) for automating feedback on programming assignments. Proceedings of the 31st International Conference on Computers in Education. [doi:10.58459/icce.2023.950](https://doi.org/10.58459/icce.2023.950)"
    author: "Maciej Pankiewicz & Ryan S. Baker"
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# When GPT hints were unavailable on harder tasks, the experimental group solved correctly less often in the initial attempts but reached comparable correctness by the seventh attempt

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`–`q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For the initial six attempts on tasks without GPT hints, the control group performed better than the experimental group; starting from the seventh attempt correctness rates were comparable. [→ Maciej Pankiewicz & Ryan S. Baker 2023](#maciej-pankiewicz-ryan-s-baker-2023)
`q3 i?` The group-by-attempt interaction on these tasks was significant (t(13)=7.13, p<0.001), indicating the groups' slopes were significantly different. [→ Maciej Pankiewicz & Ryan S. Baker 2023 (2)](#maciej-pankiewicz-ryan-s-baker-2023-2)

## Evidence

### Maciej Pankiewicz & Ryan S. Baker 2023

Maciej Pankiewicz & Ryan S. Baker. (2023). Large Language Models (GPT) for automating feedback on programming assignments. Proceedings of the 31st International Conference on Computers in Education. [doi:10.58459/icce.2023.950](https://doi.org/10.58459/icce.2023.950)

`q2 · i?` · `causal · r2`

Descriptive comparison of cumulative successful-submission percentages per attempt on the 8 tasks without GPT hints in the randomized experiment; the control group "performed better than the experimental group" in early attempts.

> "For the initial six attempts, the control group performed better than the experimental group; however, starting from the seventh attempt correctness rates were comparable (Figure 4)."

### Maciej Pankiewicz & Ryan S. Baker 2023 (2)

Maciej Pankiewicz & Ryan S. Baker. (2023). Large Language Models (GPT) for automating feedback on programming assignments. Proceedings of the 31st International Conference on Computers in Education. [doi:10.58459/icce.2023.950](https://doi.org/10.58459/icce.2023.950)

`q3 · i?` · `causal · r2`

Linear mixed-effects model (REML) on the same no-GPT tasks; the slopes of the control and experimental groups "were significantly different" with respect to number of attempts.

> "The model revealed a significant interaction effect between group and attempt, t(13)=7.13, p<0.001."

## Discussion


## Related Claims
- [Students with prior GPT hints solved later GPT-free tasks significantly faster, while solution time did not differ significantly on tasks where hints were enabled](gpt-hints-faster-later-task-completion.md) — related
- [On tasks with GPT hints enabled, the experimental group scored higher on successful submissions averaged across attempts, with statistically parallel improvement slopes](gpt-hints-higher-successful-submissions.md) — related
- [Students with GPT hints enabled clicked to view regular platform feedback on failed tests significantly less often than controls on those tasks](gpt-hints-reduce-regular-feedback-use.md) — related
- [Average number of attempts before reaching the correct answer served as the task-difficulty measure, with hints preventing bottleneck tasks in the MOOC](attempt-count-task-difficulty-mooc.md) — related
- [GPT-3.5-generated personalized hints for programming assignments improved task-solving but students showed lower success rates without hints, indicating potential reliance](gpt-hints-programming-reliance.md) — a broader claim this one bears on
