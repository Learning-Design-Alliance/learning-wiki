---
type: claim
title: Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math
description: Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math
id: full-representation-beats-semantic-only-ablation
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

# Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In the SAT Math ablation, the full representation (semantic + process features) consistently achieves the best performance, with semantic-only representations trailing the full model by 7.4–12.1 macro-F1 points. [→ Chenguang Wang 2026](#chenguang-wang-2026)
`q2 i?` Removing any one process feature family (length, episode-distribution, or transition) consistently hurts performance, indicating the three families provide complementary signals. [→ Chenguang Wang 2026](#chenguang-wang-2026)

## Evidence

### Chenguang Wang 2026

Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186 [doi:10.48550/arxiv.2606.28186](https://doi.org/10.48550/arxiv.2606.28186)

`q2 · i?` · `design · r2`

Ablation study on the SAT Math dataset with all other settings fixed, comparing semantic-only, process-only, and full representations across trace sources and aggregation settings (Table 2). The study reports Sem. Only trailing "the full model by 7.4–12.1 macro-F1 points"; no standardized effect size is printed.

> "Using either semantic embeddings alone or process features alone leads to clear drops, with Sem. Only trailing the full model by 7.4–12.1 macro-F1 points. Removing any one process feature family also consistently hurts performance, indicating that length, episode-distribution, and transition features provide complementary signals."

## Discussion


## Related Claims
- [Episode-composition and transition features contribute predictive process evidence beyond semantics, with Epi.+Tran. reaching 0.136 permutation importance versus 0.084 for Sem. in the Both (Role) setting](episode-features-predictive-importance-beyond-semantics.md) — related
- Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets — related
- [Harder SAT Math items are associated with more implementation-centered and iterative episode dynamics — stronger Implement counts and Analyze–Implement transitions — rather than a proportional increase in all reasoning activity](harder-items-implementation-centered-episode-dynamics.md) — related
- [Reasoning-process features are particularly useful when difficulty depends on multi-step problem solving, and the representation also generalizes to text-based assessment items](process-features-strongest-for-multistep-items.md) — related
- [Profile-based aggregation across both trace sources achieves the best SAT Math performance and remains stronger than matched repeated direct-prompt generation under the same rollout budget](profile-aggregation-beats-matched-rollouts.md) — related
- [In the shallow-model ablation, class balancing lowered every metric, oversampling did not improve overall performance, and semantic embeddings raised ROC-AUC but lowered accuracy and F1](shallow-ablation-balancing-embeddings.md) — related
- [LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)](llm-features-add-value-beyond-item-metadata.md) — related
