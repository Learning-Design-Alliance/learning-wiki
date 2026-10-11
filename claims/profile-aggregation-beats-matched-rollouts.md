---
type: claim
title: Profile-based aggregation across both trace sources achieves the best SAT Math performance and remains stronger than matched repeated direct-prompt generation under the same rollout budget
description: Profile-based aggregation across both trace sources achieves the best SAT Math performance and remains stronger than matched repeated direct-prompt generation under the same rollout budget
id: profile-aggregation-beats-matched-rollouts
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: chenguang-wang-2026
    resource: "https://arxiv.org/abs/2606.28186"
    title: "Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186"
    author: Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: chenguang-wang-2026-2
    resource: "https://arxiv.org/abs/2606.28186"
    title: "Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186"
    author: Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Profile-based aggregation across both trace sources achieves the best SAT Math performance and remains stronger than matched repeated direct-prompt generation under the same rollout budget

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` On SAT Math, profile-based aggregation across both trace sources (Both (Role)) reaches 0.730 accuracy and 0.728 macro-F1, compared with 0.707/0.708 for source-level aggregation. [→ Chenguang Wang 2026](#chenguang-wang-2026)
`q2 i?` Under the same rollout budget, profiled aggregation achieves a macro-F1 of 0.728 compared with 0.714 for direct replication, suggesting the gain reflects structured profile diversity rather than additional stochastic samples alone. [→ Chenguang Wang 2026 (2)](#chenguang-wang-2026-2)

## Evidence

### Chenguang Wang 2026

Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186

`q2 · i?` · `design · r2`

SAT Math ablation of aggregation strategy (Table 2), comparing single-source traces, source-level aggregation, and proficiency-conditioned profile aggregation. The study reports Both (Role) "reaching 0.730 accuracy and 0.728 macro-F1, compared with 0.707/0.708 forBoth"; no effect size is printed.

> "In contrast, profile-based aggregation is more beneficial when applied across both sources: Both (Role)achieves the best overall performance, reaching 0.730 accuracy and 0.728 macro-F1, compared with 0.707/0.708 forBoth."

### Chenguang Wang 2026 (2)

Chenguang Wang, Ming Li, Xinyue Zeng, Zhuochun Li, Hong Jiao, Tianyi Zhou, Dawei Zhou. (2026). Cognitive Episodes in LLM Reasoning Traces Enable Interpretable Human Item Difficulty Prediction. https://arxiv.org/abs/2606.28186

`q2 · i?` · `design · r2`

Control comparison in Appendix C.4 addressing the concern that profile-based aggregation benefits simply from more rollouts, matching the number of repeated direct-prompt generations. The study reports profiled aggregation at "a macro-F1 of 0.728 compared with 0.714 for direct replication"; no effect size is printed.

> "Profiled aggregation remains stronger under the same rollout budget, particularly in the combined-source setting, where it achieves a macro-F1 of 0.728 compared with 0.714 for direct replication."

## Discussion


## Related Claims
- [Reasoning-process features are particularly useful when difficulty depends on multi-step problem solving, and the representation also generalizes to text-based assessment items](process-features-strongest-for-multistep-items.md) — related
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — a broader claim this one bears on
- [Episode-composition and transition features contribute predictive process evidence beyond semantics, with Epi.+Tran. reaching 0.136 permutation importance versus 0.084 for Sem. in the Both (Role) setting](episode-features-predictive-importance-beyond-semantics.md) — related
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
