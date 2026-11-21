---
type: claim
title: LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems
description: LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems
id: llm-conformity-bias-mwp-error-detection
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

# LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 10 LLMs, error detection accuracy is consistently lower on alternative solutions (D′) than on conventional solutions (D), with an average gap of about 7%. [→ Hang Li 2025](#hang-li-2025)

## Evidence

### Hang Li 2025

Hang Li, Tianlong Xu, Kaiqi Yang, Yucheng Chu, Yanling Chen, Yichi Song, Qingsong Wen, Hui Liu. (2025). Ask-Before-Detection: Identifying and Mitigating Conformity Bias in LLM-Powered Error Detector for Math Word Problem Solutions. arXiv. Originally published 2024. [doi:10.18653/v1/2025.acl-long.80](https://doi.org/10.18653/v1/2025.acl-long.80)

`q2 · i?` · `causal · r2`

Evaluation of 10 LLM-powered error detectors on 200 GSM8K question-solution pairs, each with a conventional solution (D) and an LLM-generated alternative solution (D′), with four injected error types per solution (2,000 examples). Table 1 prints gaps such as GPT-4o base D 27.2 vs D′ 18.4 (∆ −8.8); the intro reports an "average 7% detection performance gap between conventional and alternative solutions".

> "The results clearly demonstrate a consistent perfor- mance gap between the two datasets, confirming the presence of conformity bias in LLM-based er- ror detection tasks."

## Discussion


## Related Claims
- [Adopting AskBD consistently improves overall error detection accuracy on both conventional and alternative solutions](askbd-improves-overall-detection-accuracy.md) — a narrower finding that bears on this claim
- [AskBD mitigates conformity bias in advanced LLMs but its benefits are less evident for base models](askbd-mitigates-bias-advanced-models.md) — a narrower finding that bears on this claim
- [Error detection accuracy rises with the likelihood score LLMs assign to a solution, which the authors interpret as the cause of conformity bias](likelihood-score-predicts-detection-accuracy.md) — related
- [Providing a corresponding solution as reference mitigates conformity bias, while uniformly providing the conventional solution as reference amplifies it](reference-solution-choice-mitigates-or-amplifies-bias.md) — related
- [AskBD is highly compatible with chain-of-thought prompting, and the combination achieves the best overall error detection performance](askbd-compatible-with-cot.md) — related
- [No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model](no-consistent-fp-fn-pattern.md) — related
- [Providing official reference solutions consistently reduces LLM marking error on structured physics questions](official-solutions-reduce-llm-marking-error.md) — related
