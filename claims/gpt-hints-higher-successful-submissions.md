---
type: claim
title: On tasks with GPT hints enabled, the experimental group scored higher on successful submissions averaged across attempts, with statistically parallel improvement slopes
description: On tasks with GPT hints enabled, the experimental group scored higher on successful submissions averaged across attempts, with statistically parallel improvement slopes
id: gpt-hints-higher-successful-submissions
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
    q: 3
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

# On tasks with GPT hints enabled, the experimental group scored higher on successful submissions averaged across attempts, with statistically parallel improvement slopes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Averaged across all consecutive attempts, the experimental group scored higher than the control group on percentage of successful submissions (main effect of group: t(13)=5.38, p<0.001). [→ Maciej Pankiewicz & Ryan S. Baker 2023](#maciej-pankiewicz-ryan-s-baker-2023)
`q3 i?` The group-by-attempt interaction was non-significant (t(13)=-0.172, p=0.866), so the two groups' improvement slopes did not significantly differ. [→ Maciej Pankiewicz & Ryan S. Baker 2023 (2)](#maciej-pankiewicz-ryan-s-baker-2023-2)

## Evidence

### Maciej Pankiewicz & Ryan S. Baker 2023

Maciej Pankiewicz & Ryan S. Baker. (2023). Large Language Models (GPT) for automating feedback on programming assignments. Proceedings of the 31st International Conference on Computers in Education. [doi:10.58459/icce.2023.950](https://doi.org/10.58459/icce.2023.950)

`q3 · i?` · `causal · r2`

Linear mixed-effects model (REML, nlme package) on cumulative percentage of successful submissions per attempt for the 38 GPT-enabled tasks; the authors state that "the experimental group scored higher than the control group on the dependent variable".

> "Nonetheless, the main effects of group and attempt were found to be statistically significant, group: t(13)=5.38, p<0.001; attempt: t(13)=-7.38, p<0.001."

### Maciej Pankiewicz & Ryan S. Baker 2023 (2)

Maciej Pankiewicz & Ryan S. Baker. (2023). Large Language Models (GPT) for automating feedback on programming assignments. Proceedings of the 31st International Conference on Computers in Education. [doi:10.58459/icce.2023.950](https://doi.org/10.58459/icce.2023.950)

`q3 · i?` · `causal · r2`

Same mixed-effects model testing the group-by-attempt interaction on GPT-enabled tasks; the slopes of the control and experimental groups "do not significantly differ", so the group advantage ran parallel across attempts.

> "Our analysis revealed a non-significant interaction effect between group and attempt, t(13)=-0.172, p=0.866."

## Discussion


## Related Claims
- [When GPT hints were unavailable on harder tasks, the experimental group solved correctly less often in the initial attempts but reached comparable correctness by the seventh attempt](gpt-hint-removal-initial-performance-drop.md) — related
- [Students with GPT hints enabled clicked to view regular platform feedback on failed tests significantly less often than controls on those tasks](gpt-hints-reduce-regular-feedback-use.md) — related
- [Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment](chatgpt-hints-significant-gains-versus-control.md) — related
- [Immediate post-feedback improvement is near zero on average and does not differ significantly across feedback conditions](baseline-post-feedback-gains-near-zero-no-condition-differences.md) — related
