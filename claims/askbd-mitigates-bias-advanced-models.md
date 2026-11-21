---
type: claim
title: AskBD mitigates conformity bias in advanced LLMs but its benefits are less evident for base models
description: AskBD mitigates conformity bias in advanced LLMs but its benefits are less evident for base models
id: askbd-mitigates-bias-advanced-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: mixed
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

# AskBD mitigates conformity bias in advanced LLMs but its benefits are less evident for base models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` With AskBD, advanced versions of the five LLM families show reduced D–D′ gaps compared with the naive prompt baseline. [→ Hang Li 2025](#hang-li-2025)
`q2 i?` For base LLMs, naive AskBD does not consistently narrow the gap; only Gemini shows a reduced gap, which the authors attribute to weaker reasoning capability. [→ Hang Li 2025 (2)](#hang-li-2025-2)

## Evidence

### Hang Li 2025

Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)

`q2 · i?` · `causal · r2`

Comparison of baselines (M0 naive, M1 CoT) with AskBD (M2, M3) on D and D′ in Table 4, mean accuracy over three random seeds; ∆ columns between M2 and M0 address RQ1.

> "The table clearly demonstrates that AskDB is effective in mitigating conformity bias in error detection results for advanced versions of LLMs. However, for base LLMs, the benefits of naively applying AskDB are less evident."

### Hang Li 2025 (2)

Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)

`q2 · i?` · `causal · r2`

Table 4 base-model rows show naive AskBD (M2) failing to narrow the gap for most base models; the authors' stated interpretation is that base models "fail to fully leverage the valuable information provided by the reference solutions".

> "Among the five LLM frameworks, only Gemini exhibits a reduced performance gap between D and D′. We attribute this to the relatively weaker reasoning capabilities of base models."

## Discussion


## Related Claims
- [AskBD is highly compatible with chain-of-thought prompting, and the combination achieves the best overall error detection performance](askbd-compatible-with-cot.md) — related
- [Adopting AskBD consistently improves overall error detection accuracy on both conventional and alternative solutions](askbd-improves-overall-detection-accuracy.md) — related
- [LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems](llm-conformity-bias-mwp-error-detection.md) — a broader claim this one bears on
- [More complex prompts tend to elicit superior results with advanced LLM versions (authors' observation)](complex-prompts-elicit-better-llm-results.md) — related
- [Providing a corresponding solution as reference mitigates conformity bias, while uniformly providing the conventional solution as reference amplifies it](reference-solution-choice-mitigates-or-amplifies-bias.md) — related
