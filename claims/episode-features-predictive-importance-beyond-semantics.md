---
type: claim
title: Episode-composition and transition features contribute predictive process evidence beyond semantics, with Epi.+Tran. reaching 0.136 permutation importance versus 0.084 for Sem. in the Both (Role) setting
description: Episode-composition and transition features contribute predictive process evidence beyond semantics, with Epi.+Tran.
id: episode-features-predictive-importance-beyond-semantics
status: draft
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

# Episode-composition and transition features contribute predictive process evidence beyond semantics, with Epi.+Tran. reaching 0.136 permutation importance versus 0.084 for Sem. in the Both (Role) setting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Feature-importance analysis in the profile-aggregated Both (Role) setting shows the combined episode-structural group (Epi.+Tran.) reaches 0.136 in permutation importance, exceeding Sem. at 0.084 and Len. at 0.042, while semantic features remain an important anchor under SHAP importance. [→ Chenguang Wang 2026](#chenguang-wang-2026)

## Evidence

### Chenguang Wang 2026

Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186 [doi:10.48550/arxiv.2606.28186](https://doi.org/10.48550/arxiv.2606.28186)

`q2 · i?` · `design · r2`

Feature-group importance analysis of the fitted SAT Math difficulty predictor in the Both (Role) setting, using permutation and SHAP importance (Appendix C.2, Table 5). The analysis reports Epi.+Tran. at "0.136 in permutation importance, exceedingSem.at 0.084 andLen.at 0.042"; these are importance values, not standardized effect sizes.

> "In theBoth (Role)setting,Epi.+Tran.reaches 0.136 in permutation importance, exceedingSem.at 0.084 andLen.at 0.042."

## Discussion


## Related Claims
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
- [Harder SAT Math items are associated with more implementation-centered and iterative episode dynamics — stronger Implement counts and Analyze–Implement transitions — rather than a proportional increase in all reasoning activity](harder-items-implementation-centered-episode-dynamics.md) — related
- [Profile-based aggregation across both trace sources achieves the best SAT Math performance and remains stronger than matched repeated direct-prompt generation under the same rollout budget](profile-aggregation-beats-matched-rollouts.md) — related
- [LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)](llm-features-add-value-beyond-item-metadata.md) — related
