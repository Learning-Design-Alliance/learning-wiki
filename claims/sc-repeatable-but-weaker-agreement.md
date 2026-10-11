---
type: claim
title: Self-Consistency is the most reproducible strategy across repeated runs yet shows weaker agreement with teacher mean scores (ICC (2,1) = 0.537)
description: Self-Consistency is the most reproducible strategy across repeated runs yet shows weaker agreement with teacher mean scores (ICC (2,1) = 0.537)
id: sc-repeatable-but-weaker-agreement
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
    kind: causal
    rigour: 2
---

# Self-Consistency is the most reproducible strategy across repeated runs yet shows weaker agreement with teacher mean scores (ICC (2,1) = 0.537)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` SC produced highly stable scores across three runs (total-score intra-LLM ICC (2,1) = 0.990, mean within-response SD = 0.098) while its agreement with teacher mean scores remained weaker (ICC (2,1) = 0.537). [→ Baicheng Lin 2026](#baicheng-lin-2026)

## Evidence

### Baicheng Lin 2026

Baicheng Lin, Lingxi Jin, and Kyung-Seok Min. (2026). Comparative Validation of GPT-4o-mini and Teacher Mean Scores for Automated Scoring of Music Analysis Responses: Single-Pass Deployment, Repeatability, and Strategy-Specific Bias. arXiv preprint. https://arxiv.org/abs/2608.01783

`q2 · i?` · `causal · r2`

Abstract-reported result substantiated in Results Tables 1 and 4: SC total-score intra-LLM ICC (2,1) was 0.990 with mean within-response SD 0.098, yet teacher agreement ICC (2,1) was 0.537. The article states "SC showed weaker agreement with teacher mean scores (ICC (2,1) = 0.537), despite stable scores."

> "SC showed weaker agreement with teacher mean scores (ICC (2,1) = 0.537), despite stable scores."

## Discussion


## Related Claims
- [Under single-pass deployment, Fs+CoT prompting yields the strongest agreement with teacher mean scores for music-analysis essay scoring (r = 0.795, ICC (2,1) = 0.657)](fscot-strongest-teacher-agreement-run1.md) — related
- [Median aggregation across three runs produces only minor changes in agreement and does not alter the ordering of prompting strategies](median3r-aggregation-minor-effect-ordering-preserved.md) — related
