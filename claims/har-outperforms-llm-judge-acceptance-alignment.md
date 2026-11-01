---
type: claim
title: Hierarchical Acceptance Rate aligns with expert acceptance decisions better than single-dimension and holistic LLM judges
description: Hierarchical Acceptance Rate aligns with expert acceptance decisions better than single-dimension and holistic LLM judges
id: har-outperforms-llm-judge-acceptance-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: youqing-fang-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23535"
    title: "Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen. (2026). MindCopilot: Towards Formalizing and Evaluating Granular Human-LLM Co-Writing. arXiv preprint. https://arxiv.org/abs/2605.23535 [doi:10.48550/arxiv.2605.23535](https://doi.org/10.48550/arxiv.2605.23535)"
    author: Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Hierarchical Acceptance Rate aligns with expert acceptance decisions better than single-dimension and holistic LLM judges

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across three backbone models, the full hierarchical acceptance design achieves the best alignment with expert acceptance decisions, with alignment rates of 69.3, 81.1, and 82.2 percent for DeepSeek-V3, GPT-5.1, and Gemini-2.5-Pro respectively. [→ Youqing Fang 2026](#youqing-fang-2026)

## Evidence

### Youqing Fang 2026

Youqing Fang, Yinhao Tang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Bin Liu, Weiming Zhang, Kuikun Liu, Wenwei Zhang, Kai Chen. (2026). MindCopilot: Towards Formalizing and Evaluating Granular Human-LLM Co-Writing. arXiv preprint. https://arxiv.org/abs/2605.23535 [doi:10.48550/arxiv.2605.23535](https://doi.org/10.48550/arxiv.2605.23535)

`q2 · i?` · `design · r2`

Evaluation of HAR against LLM-as-a-Judge alternatives on 1.2K expert-annotated instances, each containing a writing context, a model-generated continuation, and a gold reference, with annotators using a checklist-style protocol. HAR Full achieved the printed alignment rates of "69.3/81.1/82.2" across the three backbones.

> "the full hierarchical design (HAR Full) achieves the best performance for all three backbones (e.g., 69.3/81.1/82.2 for DeepSeek-V3/GPT-5.1/Gemini-2.5-Pro), while single-dimension judges vary substantially across model families, indicating limited robustness"

## Discussion


## Related Claims
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items](ca-selective-best-average-agreement-drawings.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](ablation-structural-components-lower-judge-scores.md) — related
- [Expert evaluation finds larger, more capable LLM backbones produce higher-quality multi-domain graphs, with GPT-5 pro rated best](llm-backbone-graph-quality-expert-evaluation.md) — related
- [Mechanical/formula-based selection decisions outperform holistic/clinical (human-judgement) decisions, with an average effect size advantage of +.11 SD across 161 studies](mechanical-outperforms-clinical-selection-esd-011.md) — related
