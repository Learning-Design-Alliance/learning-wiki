---
type: claim
title: Expert evaluation finds larger, more capable LLM backbones produce higher-quality multi-domain graphs, with GPT-5 pro rated best
description: Expert evaluation finds larger, more capable LLM backbones produce higher-quality multi-domain graphs, with GPT-5 pro rated best
id: llm-backbone-graph-quality-expert-evaluation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: haotian-zhang-2026
    resource: "https://doi.org/10.48550/arxiv.2608.24005"
    title: "Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005 [doi:10.48550/arxiv.2608.24005](https://doi.org/10.48550/arxiv.2608.24005)"
    author: Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Expert evaluation finds larger, more capable LLM backbones produce higher-quality multi-domain graphs, with GPT-5 pro rated best

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Twenty experts rated graphs from seven LLM backbones on Educational Rationality and Structural Consistency; GPT-5 pro scored highest on all metrics including Fleiss' κ. [→ Haotian Zhang 2026](#haotian-zhang-2026)

## Evidence

### Haotian Zhang 2026

Haotian Zhang, Shucun Wang, Jinze Wu, Liang Ding, Shuochen Liu, Zhenya Huang, Jing Sha, Shijin Wang, and Qi Liu. (2026). Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing. arXiv:2608.24005. https://arxiv.org/abs/2608.24005 [doi:10.48550/arxiv.2608.24005](https://doi.org/10.48550/arxiv.2608.24005)

`q2 · i?` · `design · r2`

Human evaluation with twenty experts (five students, eight educational data mining researchers, seven teachers) rating graphs from seven LLM backbones on five-point Likert scales; the article reports "larger and more capable models consistently achieve higher ER and SC scores" (Table 4).

> "Among all compared models, GPT-5 achieves the best performance across all metrics, including the highest inter-annotator agreement (Fleiss’𝜅). Overall, larger and more capable models consistently achieve higher ER and SC scores"

## Discussion


## Related Claims
- [BEAGLE generalizes across tasks and LLM backbones: on the out-of-distribution Gradient Descent task it still shrinks DKL by ≥3×, raises error recurrence to ≥79%, and improves all three perceptual scores](beagle-cross-task-cross-backbone-generalization.md) — related
- [In a preliminary 2×3 controlled lesson study across five backbone LLMs, structured student agents produce more differentiated mastery and misconception traces than a baseline simulator](structured-student-agents-differentiated-mastery-traces.md) — related
- [The investigate–solve–write scaffold, with personalization disabled, improves all five backbone model families on general agentic benchmarks, with average relative gains of 25.69%–32.03%](solver-scaffold-transfers-general-agentic-problem-solving.md) — related
- [Human evaluators rate the framework's simulated solutions higher than the second-best setting across all model settings](human-evaluation-prefers-prototype-refine-simulations.md) — related
- [Frontier-model choice affects LecturaAgents performance, with Gemini 3 Pro ranking first at 80.4% AAR](lecturaagents-frontier-model-evaluation-aar.md) — related
- [Teacher-agent comparisons show backbone-dependent patterns consistent with ZPD-informed adaptation](teacher-agent-backbone-dependent-zpd-patterns.md) — related
- [Hierarchical Acceptance Rate aligns with expert acceptance decisions better than single-dimension and holistic LLM judges](har-outperforms-llm-judge-acceptance-alignment.md) — related
