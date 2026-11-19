---
type: claim
title: Instructor-present video lectures improved self-reported attention among honest students relative to instructor-absent lectures
description: Instructor-present video lectures improved self-reported attention among honest students relative to instructor-absent lectures
id: instructor-present-videos-improved-attention
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: manjusha-kancharla-and-hyunseung-kang-2021
    resource: "https://doi.org/10.48550/arXiv.2112.02452"
    title: "Manjusha Kancharla and Hyunseung Kang. (2021). A Robust, Differentially Private Randomized Experiment for Evaluating Online Educational Programs With Sensitive Student Data. [doi:10.48550/arXiv.2112.02452](https://doi.org/10.48550/arXiv.2112.02452)"
    author: Manjusha Kancharla and Hyunseung Kang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Instructor-present video lectures improved self-reported attention among honest students relative to instructor-absent lectures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Among honest (non-cheater) students, instructor-present (IP) video lectures led to easier self-reported attention than instructor-absent (IA) lectures (covariate-adjusted estimate -0.316, 95% CI [-0.621, -0.011]). [→ Manjusha Kancharla and Hyunseung Kang 2021](#manjusha-kancharla-and-hyunseung-kang-2021)

## Evidence

### Manjusha Kancharla and Hyunseung Kang 2021

Manjusha Kancharla and Hyunseung Kang. (2021). A Robust, Differentially Private Randomized Experiment for Evaluating Online Educational Programs With Sensitive Student Data. [doi:10.48550/arXiv.2112.02452](https://doi.org/10.48550/arXiv.2112.02452)

`q3 · i?` · `causal · r2`

RP-RCT experiment with n = 72 students in introductory statistics at UW-Madison, Spring 2021, randomized to 13-minute IP or IA lecture videos on RCTs; outcomes were yes/no questions privatized by FRR with epsilon = 2. The attention effect "ˆτH,Cov =−0.316" had a 95% CI excluding zero; no standardized effect size is printed.

> "Honest students indicated that it was easier to pay attention to instructor-present (IP) video lectures compared to instructor-absent (IA) video lectures (ˆτH,Cov =−0.316, 95% CI: [−0.621,−0.011])."

## Discussion


## Learner Variables
- [Attention](../learner-variables/attention.md) — outcome: measured as an outcome of the instruction studied

## Related Claims
- [Retention of concepts was higher among honest students randomized to instructor-absent video lectures](instructor-absent-videos-higher-retention.md) — related
- [No significant difference between IP and IA lectures in judgement of learning or comprehension](no-ip-ia-difference-jol-comprehension.md) — related
- [The RP-RCT identifies the ATE among non-cheaters and the proportion of cheaters from privatized outcomes](rp-rct-identifies-ate-among-non-cheaters.md) — a broader claim this one bears on
- [Instructor visuals do not reduce mind wandering during video lectures](instructor-visuals-no-mind-wandering-reduction.md) — related
