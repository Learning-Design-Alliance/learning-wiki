---
type: claim
title: Reasoning-process features are particularly useful when difficulty depends on multi-step problem solving, and the representation also generalizes to text-based assessment items
description: Reasoning-process features are particularly useful when difficulty depends on multi-step problem solving, and the representation also generalizes to text-based assessment items
id: process-features-strongest-for-multistep-items
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: chenguang-wang-2026
    resource: "https://doi.org/10.48550/arxiv.2606.28186"
    title: "Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186 [doi:10.48550/arxiv.2606.28186](https://doi.org/10.48550/arxiv.2606.28186)"
    author: Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Reasoning-process features are particularly useful when difficulty depends on multi-step problem solving, and the representation also generalizes to text-based assessment items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Gains are especially clear on SAT Math, suggesting reasoning-process features help most when difficulty depends on multi-step problem solving, while improvements on SAT Reading & Writing indicate generalization to text-based items. [→ Chenguang Wang 2026](#chenguang-wang-2026)

## Evidence

### Chenguang Wang 2026

Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186 [doi:10.48550/arxiv.2606.28186](https://doi.org/10.48550/arxiv.2606.28186)

`q2 · i?` · `design · r2`

Results-section interpretation of the main benchmark comparison, contrasting the especially clear SAT Math gains with the smaller SAT Reading & Writing improvement. The authors state process features are "particularly useful when difficulty depends on multi-step problem solving"; no effect size is printed.

> "This suggests that reasoning-process features are particularly useful when difficulty depends on multi-step problem solving, while the improvement on SAT Reading & Writing indicates that the proposed representation also generalizes to text-based assessment items."

## Discussion


## Related Claims
- [Harder SAT Math items are associated with more implementation-centered and iterative episode dynamics — stronger Implement counts and Analyze–Implement transitions — rather than a proportional increase in all reasoning activity](harder-items-implementation-centered-episode-dynamics.md) — related
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
- [Profile-based aggregation across both trace sources achieves the best SAT Math performance and remains stronger than matched repeated direct-prompt generation under the same rollout budget](profile-aggregation-beats-matched-rollouts.md) — related
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — related
