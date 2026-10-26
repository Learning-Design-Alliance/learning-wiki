---
type: claim
title: "Human evaluators rate the framework's simulated solutions higher than the second-best setting across all model settings"
description: "Human evaluators rate the framework's simulated solutions higher than the second-best setting across all model settings"
id: human-evaluation-prefers-prototype-refine-simulations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: tao-wu-2025
    resource: "https://doi.org/10.48550/arxiv.2505.19997"
    title: "Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997 [doi:10.48550/arxiv.2505.19997](https://doi.org/10.48550/arxiv.2505.19997)"
    author: Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human evaluators rate the framework's simulated solutions higher than the second-best setting across all model settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In human evaluation, the proposed method consistently receives higher 1–5 ratings than the second-best setting for every model. [→ Tao Wu 2025](#tao-wu-2025)

## Evidence

### Tao Wu 2025

Tao Wu, Jingyuan Chen, Wang Lin, Mengze Li, Yumeng Zhu, Ang Li, Kun Kuang, Fei Wu. (2025). Embracing Imperfection: Simulating Students with Diverse Cognitive Levels Using LLM-based Agents. https://arxiv.org/abs/2505.19997 [doi:10.48550/arxiv.2505.19997](https://doi.org/10.48550/arxiv.2505.19997)

`q2 · i?` · `design · r2`

Human evaluation in Section 5.4: 10 undergraduate students with solid Python programming skills rated each simulated solution on a 1–5 scale, each solution rated by two independent evaluators and averaged. Table 4 reports, for example, Prototype Mapping + Refine 3.08 versus Prototype Mapping + IO 2.88 for LLaMA-3.3-70B-Instruct.

> "As shown in Table 4, our method consistently receives higher human evaluation scores than the baseline across all model settings."

## Discussion


## Related Claims
- [Beam search-based self-refinement improves simulated solution alignment with predicted student behavior](beam-search-self-refinement-improves-solution-simulation.md) — related
- [Expert evaluation finds larger, more capable LLM backbones produce higher-quality multi-domain graphs, with GPT-5 pro rated best](llm-backbone-graph-quality-expert-evaluation.md) — related
- [Knowledge-graph prototype mapping outperforms existing behavior-prediction baselines for student simulation](prototype-mapping-outperforms-behavior-prediction-baselines.md) — related
- [LLM simulation, reflection, and refinement elevates the quality of LLM-generated teaching plans above their unenhanced baselines](llm-simulation-reflection-enhances-teaching-plans.md) — related
