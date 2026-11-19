---
type: claim
title: "AttnGRU outperforms GRU and LSTM by average AUC of 2.5% and 3.3% with combined inputs without pre-training"
description: "AttnGRU outperforms GRU and LSTM by average AUC of 2.5% and 3.3% with combined inputs without pre-training"
id: attngru-beats-gru-lstm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: yun-wei-chu-2018
    resource: "https://doi.org/10.1145/1122445.1122456"
    title: "Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura Cruz, Kerrie Douglas, Andrew Lan, Christopher Brinton. (2018). Mitigating Biases in Student Performance Prediction via Attention-Based Personalized Federated Learning. Proceedings of ACM Conference (Conference'22). https://doi.org/10.1145/1122445.1122456"
    author: Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura Cruz, Kerrie Douglas, Andrew Lan, Christopher Brinton
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AttnGRU outperforms GRU and LSTM by average AUC of 2.5% and 3.3% with combined inputs without pre-training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using both video and forum activities as input without pre-training, AttnGRU outperforms GRU and LSTM by an average AUC of 2.5% and 3.3%. [→ Yun-Wei Chu 2018](#yun-wei-chu-2018)

## Evidence

### Yun-Wei Chu 2018

Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura Cruz, Kerrie Douglas, Andrew Lan, Christopher Brinton. (2018). Mitigating Biases in Student Performance Prediction via Attention-Based Personalized Federated Learning. Proceedings of ACM Conference (Conference'22). https://doi.org/10.1145/1122445.1122456

`q2 · i?` · `design · r2`

Architecture comparison in the model-structure analysis (Figure 3) across the three edX datasets; the article attributes the advantage to the attention mechanism effectively incorporating activities in the distant past.

> "Using both video and forum activities ([af; vid; av]) as input and without performing self-supervised pre- training, AttnGRU outperforms GRU and LSTM by an average AUC of 2.5% and 3.3%."

## Discussion


## Related Claims
- [Self-supervised behavioral pre-training improves prediction AUC, raising AttnGRU's AUC by 1.4% with combined inputs](self-supervised-pretraining-auc-gain.md) — related
- [Combining forum and video activities yields the best prediction performance, and video-only outperforms forum-only](combined-video-forum-activities-best.md) — related
