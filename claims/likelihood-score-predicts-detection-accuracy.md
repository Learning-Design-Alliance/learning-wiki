---
type: claim
title: Error detection accuracy rises with the likelihood score LLMs assign to a solution, which the authors interpret as the cause of conformity bias
description: Error detection accuracy rises with the likelihood score LLMs assign to a solution, which the authors interpret as the cause of conformity bias
id: likelihood-score-predicts-detection-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: hang-li-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-long.80"
    title: "Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)"
    author: Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: hang-li-2025-2
    resource: "https://doi.org/10.18653/v1/2025.acl-long.80"
    title: "Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)"
    author: Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Error detection accuracy rises with the likelihood score LLMs assign to a solution, which the authors interpret as the cause of conformity bias

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Solutions grouped into higher average token log-likelihood quartiles show higher error detection accuracy than lower quartiles. [→ Hang Li 2025](#hang-li-2025)
`q2 i?` The authors interpret conformity bias as caused by LLMs' decreased understanding of alternative solutions, which receive lower likelihood scores. [→ Hang Li 2025 (2)](#hang-li-2025-2)

## Evidence

### Hang Li 2025

Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)

`q2 · i?` · `causal · r2`

Analysis of average error detection accuracy across likelihood-score percentile groups (25th, 50th, 75th) shown in Figure 3a–3b; because closed-source model scores are unavailable, "the average scores of all open-source LLMs" served as a pseudo-indicator.

> "From the figure, we observe that the larger quarter groups with higher indicator values exhibit a clear advantage over those with the smaller quarter ones."

### Hang Li 2025 (2)

Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)

`q2 · i?` · `causal · r2`

Figure 3c compares likelihood score distributions of solutions from D and D′; this is the authors' interpretation based on the plotted distributions, attributing conformity bias to lower likelihood scores for alternative solutions.

> "From these plot, we can draw a clear conclusion that the conformity bias in current LLM to error detection tasks is caused by its decreased understanding to those alternative solution."

## Discussion


## Related Claims
- [Adopting AskBD consistently improves overall error detection accuracy on both conventional and alternative solutions](askbd-improves-overall-detection-accuracy.md) — related
- [LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems](llm-conformity-bias-mwp-error-detection.md) — related
- [Providing a corresponding solution as reference mitigates conformity bias, while uniformly providing the conventional solution as reference amplifies it](reference-solution-choice-mitigates-or-amplifies-bias.md) — related
- [Prompt customization introduces at least three types of prompting bias: majority label, recency, and common token bias](prompting-bias-three-types.md) — related
