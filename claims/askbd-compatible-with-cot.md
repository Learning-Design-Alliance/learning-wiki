---
type: claim
title: AskBD is highly compatible with chain-of-thought prompting, and the combination achieves the best overall error detection performance
description: AskBD is highly compatible with chain-of-thought prompting, and the combination achieves the best overall error detection performance
id: askbd-compatible-with-cot
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
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
---

# AskBD is highly compatible with chain-of-thought prompting, and the combination achieves the best overall error detection performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Combining AskBD with CoT (M3) yields significant performance improvements over either method alone for advanced Llama-3.1 and base Gemini-1.5. [→ Hang Li 2025](#hang-li-2025)

## Evidence

### Hang Li 2025

Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)

`q2 · i?` · `causal · r2`

RQ3 analysis comparing M3 (CoT + AskBD) with M1 (CoT) in Table 4 across 10 LLMs; the article names advanced Llama-3.1 and base Gemini-1.5 as cases where the combination beats either method independently.

> "The results reveal that AskDB is highly compatible with other reasoning-enhancing techniques such as CoT prompts in the context of error detection. For advanced model of Llama-3.1 and base model of Gemini-1.5, combining AskDB with CoT yields significant performance improvements compared to using either method independently."

## Discussion


## Related Claims
- [AskBD mitigates conformity bias in advanced LLMs but its benefits are less evident for base models](askbd-mitigates-bias-advanced-models.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems](llm-conformity-bias-mwp-error-detection.md) — related
- [Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation](reasoning-variants-no-alignment-improvement.md) — related
- [Adopting AskBD consistently improves overall error detection accuracy on both conventional and alternative solutions](askbd-improves-overall-detection-accuracy.md) — related
