---
type: claim
title: "In offline validation, the HMM timing model detected children's attention moments more accurately than fixed-interval and dwell-time triggers"
description: "In offline validation, the HMM timing model detected children's attention moments more accurately than fixed-interval and dwell-time triggers"
id: hmm-timing-outperforms-fixed-and-dwell-triggers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zekun-wu-2026
    resource: "https://doi.org/10.48550/arxiv.2607.00445"
    title: "Zekun Wu, Man Su, Huiyong Li, Tomohiro Nagashima, and Anna Maria Feit. (2026). Gaze-Informed Proactive AI Assistance for Children Exploring Picture Books. https://arxiv.org/abs/2607.00445 [doi:10.48550/arxiv.2607.00445](https://doi.org/10.48550/arxiv.2607.00445)"
    author: Zekun Wu, Man Su, Huiyong Li, Tomohiro Nagashima, and Anna Maria Feit
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In offline validation, the HMM timing model detected children's attention moments more accurately than fixed-interval and dwell-time triggers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across both proxy-labeling approaches (expert-annotated and future-gaze), the HMM achieved the highest F1 score, mainly due to substantially higher recall than the fixed 3s and 3s dwell baselines. [→ Zekun Wu 2026](#zekun-wu-2026)

## Evidence

### Zekun Wu 2026

Zekun Wu, Man Su, Huiyong Li, Tomohiro Nagashima, and Anna Maria Feit. (2026). Gaze-Informed Proactive AI Assistance for Children Exploring Picture Books. https://arxiv.org/abs/2607.00445 [doi:10.48550/arxiv.2607.00445](https://doi.org/10.48550/arxiv.2607.00445)

`q2 · i?` · `causal · r2`

Offline validation on free-exploration gaze data from four children across nine images, replayed as 500 ms candidate intervals against two proxy labels (669/285 expert-annotated attention/no-attention intervals; 711/606 future-gaze instances). The HMM reached F1 0.784 (expert) and 0.651 (future-gaze); no effect size printed.

> "Across both proxy-labeling approaches, the HMM achieved the highest F1 score, mainly due to substantially higher recall than the two baselines."

## Discussion


## Related Claims

- [In offline validation, combined relevance-based secondary-AOI selection matched children's next attended AOI more often than random or single-distance selection](combined-relevance-selection-aligns-with-next-attention.md) — related
- [Longer dwell time on AI suggestions is associated with better attention check performance but slightly lower task performance](dwell-time-attention-checks-versus-task-performance.md)
- [Speech detection showed preliminary success but remained challenging in noisy settings, particularly for speaker differentiation, children's voices, and diverse dialects](speech-detection-preliminary-success-noisy-settings.md)
- [LLM performance drops from offline to real-time proxy evaluation when clues arrive incrementally](performance-drops-realtime-proxy-nsmq.md) — related
