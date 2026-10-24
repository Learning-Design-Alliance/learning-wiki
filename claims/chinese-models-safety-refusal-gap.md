---
type: claim
title: Chinese-developed models lead the safety module, with the refusal gap concentrated on region-specific normative content (difference-in-differences of 28.9 points)
description: Chinese-developed models lead the safety module, with the refusal gap concentrated on region-specific normative content (difference-in-differences of 28.9 points)
id: chinese-models-safety-refusal-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yilin-jiang-2026
    resource: "https://doi.org/10.48550/arxiv.2608.09548"
    title: "Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548 [doi:10.48550/arxiv.2608.09548](https://doi.org/10.48550/arxiv.2608.09548)"
    author: Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: yilin-jiang-2026-2
    resource: "https://arxiv.org/abs/2608.09548"
    title: "Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548"
    author: Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Chinese-developed models lead the safety module, with the refusal gap concentrated on region-specific normative content (difference-in-differences of 28.9 points)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` U.S.-developed systems decline 39.5–50.4% of refusable requests while three of four Chinese-developed general models decline 94.7–99.0% and the safety-specialized variant declines 99.7%. [→ Yilin Jiang 2026](#yilin-jiang-2026)
`q2 i?` The group refusal gap is much larger on region-specific normative content than universal-harm content, a difference-in-differences of 28.9 points (95% CI [18.8, 38.5]). [→ Yilin Jiang 2026 (2)](#yilin-jiang-2026-2)

## Evidence

### Yilin Jiang 2026

Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548 [doi:10.48550/arxiv.2608.09548](https://doi.org/10.48550/arxiv.2608.09548)

`q2 · i?` · `design · r2`

Safety-module results for the nine-model evaluation, refusal task family (Figure 4 and Appendix B). The printed refusal rates are 39.5–50.4% for U.S.-developed systems versus 94.7–99.0% for three Chinese-developed models, with Doubao-Seed-2.0-Pro an exception at 61.1% and Safe-InnoSpark at 99.7%.

> "The U.S.- developed systems decline39.5to50.4%of requests that shouldberefused,whilethreeofthefourChinese-developed general models decline94.7to99.0%and the safety- specialized variant99.7%(Doubao-Seed-2.0-Pro is an ex- ception at61.1%)."

### Yilin Jiang 2026 (2)

Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548

`q2 · i?` · `associational · r1`

Refusal-category analysis in the results section. The article prints a difference-in-differences of 28.9 points with 95% CI [18.8, 38.5], comparing region-specific normative content against universal-harm content across the two model groups.

> "Splitting refusal into region-specific normative content and universal-harm content, the group gap is much larger on the region-specific subset than on the universal-harm subset, a difference-in-differences of28.9 points (95%CI[18.8,38.5])."

## Discussion


## Related Claims
- Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency — related
- Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items — related
- [Safety-aligned LLM tutors refuse educational requests asymmetrically, with low-resource students facing the highest refusal rates (76.7% vs 62.2%)](differential-refusal-low-tier-llm-tutors.md) — related
- [Deepseek's justification scores vary by student socio-economic profile, with Top Tier students averaging 9.60 versus 6.90 for Low Tier students](elite-hermeneutics-justification-gap.md) — related
- [LLM history tutors reduce marginalized students' access to contested geopolitical framing, with the coup theory appearing in 2.6% of Low Tier responses versus 7.9% for the baseline](epistemic-gatekeeping-coup-gap.md) — related
- [The strict-persona collapse is attributed to the preamble's two credit-withholding policy sentences, not its harsh tone, with S2 alone causing refusal in two models](strict-preamble-policy-sentence-attribution.md) — related
- [The two education-specialized models lead neither education module, and the improvement from education-specific post-training is small relative to differences in general capability](education-specialized-models-lead-neither-education-module.md) — related
