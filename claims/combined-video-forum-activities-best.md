---
type: claim
title: Combining forum and video activities yields the best prediction performance, and video-only outperforms forum-only
description: Combining forum and video activities yields the best prediction performance, and video-only outperforms forum-only
id: combined-video-forum-activities-best
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

# Combining forum and video activities yields the best prediction performance, and video-only outperforms forum-only

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Incorporating both forum and video activity results in the best performance in most cases, and video-only models consistently outperform forum-only models. [→ Yun-Wei Chu 2018](#yun-wei-chu-2018)

## Evidence

### Yun-Wei Chu 2018

Yun-Wei Chu, Seyyedali Hosseinalipour, Elizabeth Tenorio, Laura Cruz, Kerrie Douglas, Andrew Lan, Christopher Brinton. (2018). Mitigating Biases in Student Performance Prediction via Attention-Based Personalized Federated Learning. Proceedings of ACM Conference (Conference'22). https://doi.org/10.1145/1122445.1122456

`q2 · i?` · `design · r2`

Input-modality analysis in the results section: forum-only models overfit at roughly 50% AUC, video-only models outperform them, and the combined input is best in most cases across the three edX datasets (Figure 3).

> "However, incorporating both forum activity and video activity results in the best performance in most cases, which shows that forum activities also contain useful information about students’ learning processes and outcomes when incorporated properly."

## Discussion


## Related Claims
- [AttnGRU outperforms GRU and LSTM by average AUC of 2.5% and 3.3% with combined inputs without pre-training](attngru-beats-gru-lstm.md) — related
- [Self-supervised behavioral pre-training improves prediction AUC, raising AttnGRU's AUC by 1.4% with combined inputs](self-supervised-pretraining-auc-gain.md) — related
