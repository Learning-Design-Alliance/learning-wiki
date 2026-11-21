---
type: claim
title: Providing a corresponding solution as reference mitigates conformity bias, while uniformly providing the conventional solution as reference amplifies it
description: Providing a corresponding solution as reference mitigates conformity bias, while uniformly providing the conventional solution as reference amplifies it
id: reference-solution-choice-mitigates-or-amplifies-bias
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
    kind: causal
    rigour: 1
---

# Providing a corresponding solution as reference mitigates conformity bias, while uniformly providing the conventional solution as reference amplifies it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Using the conventional solution as reference for alternative solutions sharply degrades performance (e.g., GPT-4o base ∆ −28.0). [→ Hang Li 2025](#hang-li-2025)

## Evidence

### Hang Li 2025

Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)

`q2 · i?` · `causal · r1`

Table 3 (conventional solutions as references) shows sharply enlarged gaps on D′, e.g., −28.0 for base GPT-4o and −32.2 for base Qwen-2.5, versus the corresponding-reference setup.

> "uniformly us- ing conventional solutions tends to amplify it. This contrast highlights the critical importance of select- ing appropriate reference solutions to enhance error detection in alternative scenarios."

## Discussion


## Related Claims
- [LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems](llm-conformity-bias-mwp-error-detection.md) — related
- [AskBD mitigates conformity bias in advanced LLMs but its benefits are less evident for base models](askbd-mitigates-bias-advanced-models.md) — related
- [Adopting AskBD consistently improves overall error detection accuracy on both conventional and alternative solutions](askbd-improves-overall-detection-accuracy.md) — related
- [Error detection accuracy rises with the likelihood score LLMs assign to a solution, which the authors interpret as the cause of conformity bias](likelihood-score-predicts-detection-accuracy.md) — related
