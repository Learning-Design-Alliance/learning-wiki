---
type: claim
title: "Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement"
description: "Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement"
id: federated-aggregation-primary-performance-driver
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yagna-manasa-boyapati-2026
    resource: "https://doi.org/10.48550/arxiv.2609.02947"
    title: "Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)"
    author: Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Removing federation causes the largest degradation in the ablation, with improvements dropping by an average of 11.99%. [→ Yagna Manasa Boyapati 2026](#yagna-manasa-boyapati-2026)

## Evidence

### Yagna Manasa Boyapati 2026

Yagna Manasa Boyapati, Chong Yu, Tianyu Jiang, Justin Zhan. (2026). Privacy-Preserving Heterogeneous Multi-LLM Federated Inference for Cognitive Diagnosis. arXiv preprint. https://arxiv.org/abs/2609.02947 [doi:10.48550/arxiv.2609.02947](https://doi.org/10.48550/arxiv.2609.02947)

`q2 · i?` · `design · r2`

Ablation study (Table 4) across three datasets; a simple three-model ensemble also confirms model diversity contributes meaningful gains, but the full system outperforms it across all datasets while providing formal (ε,0)-DP guarantees.

> "Removing federation causes the largest degradation, with improvements dropping by an average of 11.99%, confirming federated aggregation is the primary driver of performance gains."

## Discussion


## Related Claims
- [Taxonomy quality drives CLARA performance: degraded taxonomies reduce alignment, and removing SEL causes the largest degradation](clara-taxonomy-quality-ablation.md) — related
- [Residual correction is essential: removing it while retaining LDP yields MAE worse than the single-LLM baseline across all datasets](residual-correction-essential-heterogeneous-aggregation.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism](beagle-ablation-semi-markov-and-decoupling.md) — related
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
- [Removing the DPO objective reduces examination accuracy by 1.11 percentage points and degrades annotated pedagogical quality](dpo-training-contributes-accuracy-and-pedagogical-tone.md) — related
- [Heterogeneous multi-LLM federated inference improves cognitive diagnosis MAE over single-LLM baselines across three educational benchmarks with minimal privacy cost](multi-llm-federated-cognitive-diagnosis-improvement.md) — possibly the same claim (merge candidate)
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
- [In the EduAgent framework, removing past cognitive states from memory significantly reduced simulation performance](eduagent-ablation-contextual-memory-critical.md) — related
- [Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%](ablation-trust-module-largest-contribution.md) — related
- [CLARA's gains come from the interaction of structured representation, constrained annotation, and aggregation, not prompt engineering alone](clara-contribution-decomposition.md) — a broader claim this one bears on
- [Omitting the teacher's communication strategy causes the greatest drop in classifier accuracy, marking communication choice as the most impactful feature category.](communication-strategy-most-impactful-ablation.md) — related
