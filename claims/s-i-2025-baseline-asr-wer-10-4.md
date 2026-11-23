---
type: claim
title: "The baseline Whisper-small ASR system transcribes L2 learner speech at a 10.4% WER on the S&I Dev set"
description: "The baseline Whisper-small ASR system transcribes L2 learner speech at a 10.4% WER on the S&I Dev set"
id: s-i-2025-baseline-asr-wer-10-4
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mengjie-qian-2025
    resource: "https://doi.org/10.21437/slate.2025-9"
    title: "Mengjie Qian, Kate Knill, Stefano Banno, Siyuan Tang, Penny Karanasou, Mark J.F. Gales, Diane Nicholls. (2025). Speak & Improve Challenge 2025: Tasks and Baseline Systems. [doi:10.21437/slate.2025-9](https://doi.org/10.21437/slate.2025-9)"
    author: Mengjie Qian, Kate Knill, Stefano Banno, Siyuan Tang, Penny Karanasou, Mark J.F. Gales, Diane Nicholls
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The baseline Whisper-small ASR system transcribes L2 learner speech at a 10.4% WER on the S&I Dev set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A Whisper-small baseline achieves 10.4% WER (Sub 4.9, Del 4.0, Ins 1.5) on the S&I Dev set. [→ Mengjie Qian 2025](#mengjie-qian-2025)

## Evidence

### Mengjie Qian 2025

Mengjie Qian, Kate Knill, Stefano Banno, Siyuan Tang, Penny Karanasou, Mark J.F. Gales, Diane Nicholls. (2025). Speak & Improve Challenge 2025: Tasks and Baseline Systems. [doi:10.21437/slate.2025-9](https://doi.org/10.21437/slate.2025-9)

`q2 · i?` · `design · r2`

Baseline system evaluation: the ASR task baseline uses the OpenAI Whisper small model, evaluated with Speech Word Error Rate (SpWER) in which "punctuation and case are removed, numbers are written out in orthographic word form". The Dev-set result is a WER of 10.4, with Sub 4.9, Del 4.0, Ins 1.5 (Table 3).

> "Table 3: Baseline ASR (%)WER results on Dev set."

## Discussion


## Related Claims
- [With the Whisper large-v2 backbone, the end-to-end SGEC model reduces WER by 6.9% relative on LNG and 5.6% on S&I versus the partial-cascaded system, surpassing both pipeline baselines](e2e-whisper-large-v2-sgec-outperforms-pipelines.md) — related
- [Pseudo-labeled training data from over 2,500 hours of unlabeled learner speech improves small-model end-to-end SGEC, but offers limited benefit for large-v2 models once manual annotations are added](pseudo-labeled-data-sgec-model-size-moderates.md) — related
- [The baseline cascaded BERT text-grader predicts holistic CEFR speaking scores at RMSE 0.445 with Pearson correlation 0.746 on the S&I Dev set](s-i-2025-baseline-sla-rmse-0-445.md) — related
