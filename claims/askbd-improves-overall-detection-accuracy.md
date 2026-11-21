---
type: claim
title: Adopting AskBD consistently improves overall error detection accuracy on both conventional and alternative solutions
description: Adopting AskBD consistently improves overall error detection accuracy on both conventional and alternative solutions
id: askbd-improves-overall-detection-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: hang-li-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-long.80"
    title: "Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)"
    author: Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adopting AskBD consistently improves overall error detection accuracy on both conventional and alternative solutions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Comparing AskBD (M2) with the naive baseline (M0), detection accuracy improves consistently on both D and D′. [→ Hang Li 2025](#hang-li-2025)

## Evidence

### Hang Li 2025

Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)

`q2 · i?` · `design · r2`

RQ2 analysis of Table 4, comparing M2 with M0 in the D and D′ columns across 10 LLMs on the 200-example GSM8K-derived dataset; e.g., Gemini-1.5 advanced rises from 65.2/55.6 to 76.0/72.2.

> "The results indicate a con- sistent improvement in error detection accuracy af- ter adopting the AskDB framework. This suggests that AskDB not only helps reduce the performance gap between conventional and alternative solutions but also enhances overall detection performance."

## Discussion


## Related Claims
- [AskBD mitigates conformity bias in advanced LLMs but its benefits are less evident for base models](askbd-mitigates-bias-advanced-models.md) — related
- [LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems](llm-conformity-bias-mwp-error-detection.md) — a broader claim this one bears on
- [Error detection accuracy rises with the likelihood score LLMs assign to a solution, which the authors interpret as the cause of conformity bias](likelihood-score-predicts-detection-accuracy.md) — related
- [Providing a corresponding solution as reference mitigates conformity bias, while uniformly providing the conventional solution as reference amplifies it](reference-solution-choice-mitigates-or-amplifies-bias.md) — related
- [AskBD is highly compatible with chain-of-thought prompting, and the combination achieves the best overall error detection performance](askbd-compatible-with-cot.md) — related
