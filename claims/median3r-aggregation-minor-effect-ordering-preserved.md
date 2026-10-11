---
type: claim
title: Median aggregation across three runs produces only minor changes in agreement and does not alter the ordering of prompting strategies
description: Median aggregation across three runs produces only minor changes in agreement and does not alter the ordering of prompting strategies
id: median3r-aggregation-minor-effect-ordering-preserved
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: baicheng-lin-2026
    resource: "https://arxiv.org/abs/2608.01783"
    title: "Baicheng Lin, Lingxi Jin, and Kyung-Seok Min. (2026). Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias. arXiv preprint. https://arxiv.org/abs/2608.01783"
    author: Baicheng Lin, Lingxi Jin, and Kyung-Seok Min
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Median aggregation across three runs produces only minor changes in agreement and does not alter the ordering of prompting strategies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Median3R aggregation left strategy ordering unchanged, with Fs+CoT still best (ICC (2,1) = 0.656, QWK = 0.655) and only slight RMSE changes (2.461 to 2.457 for Fs+CoT). [→ Baicheng Lin 2026](#baicheng-lin-2026)

## Evidence

### Baicheng Lin 2026

Baicheng Lin, Lingxi Jin, and Kyung-Seok Min. (2026). Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias. arXiv preprint. https://arxiv.org/abs/2608.01783

`q2 · i?` · `design · r2`

Results section 4.2 and Table 3 comparing Median3R with Run1 for the same 300 responses. Fs+CoT Pearson r stayed at 0.795 and RMSE moved from 2.461 to 2.457; RAG improved most but retained bias of 1.787.

> "aggregating 3R using the Median3R resulted in only modest changes in agreement with teacher mean scores while preserving the performance pattern observed under single-pass deployment."

## Discussion


## Related Claims
- [Under single-pass deployment, Fs+CoT prompting yields the strongest agreement with teacher mean scores for music-analysis essay scoring (r = 0.795, ICC (2,1) = 0.657)](fscot-strongest-teacher-agreement-run1.md) — related
- [LLM scoring performance is dimension-specific: Reasoning shows the strongest agreement and Terminology the weakest across all three strategies](dimension-specific-scoring-reasoning-strongest-terminology-weakest.md) — related
- [Prompting strategies produce distinct directional bias profiles: Fs+CoT under-scores (bias = -1.730), RAG over-scores (bias = 1.787), and SC shows minimal directional bias (bias = -0.083)](strategy-specific-bias-profiles.md) — related
- [Self-Consistency is the most reproducible strategy across repeated runs yet shows weaker agreement with teacher mean scores (ICC (2,1) = 0.537)](sc-repeatable-but-weaker-agreement.md) — related
