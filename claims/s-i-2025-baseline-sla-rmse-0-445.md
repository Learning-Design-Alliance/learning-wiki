---
type: claim
title: "The baseline cascaded BERT text-grader predicts holistic CEFR speaking scores at RMSE 0.445 with Pearson correlation 0.746 on the S&I Dev set"
description: "The baseline cascaded BERT text-grader predicts holistic CEFR speaking scores at RMSE 0.445 with Pearson correlation 0.746 on the S&I Dev set"
id: s-i-2025-baseline-sla-rmse-0-445
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

# The baseline cascaded BERT text-grader predicts holistic CEFR speaking scores at RMSE 0.445 with Pearson correlation 0.746 on the S&I Dev set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The baseline SLA system, cascading ASR transcription into BERT-based text graders, achieves RMSE 0.445, PCC 0.746, SRC 0.750, and 73.3% of predictions within half a grade on the Dev set. [→ Mengjie Qian 2025](#mengjie-qian-2025)

## Evidence

### Mengjie Qian 2025

Mengjie Qian, Kate Knill, Stefano Banno, Siyuan Tang, Penny Karanasou, Mark J.F. Gales, Diane Nicholls. (2025). Speak & Improve Challenge 2025: Tasks and Baseline Systems. [doi:10.21437/slate.2025-9](https://doi.org/10.21437/slate.2025-9)

`q2 · i?` · `design · r2`

Baseline system evaluation: four BERT-based text graders (bert-base-uncased with four multi-head self-attention layers and a regression head), one per test part, are trained on ASR-generated transcriptions; part predictions are averaged for the overall score. Dev-set results: RMSE 0.445 (primary ranking metric), PCC 0.746, SRC 0.750, KRC 0.563, 73.3% within half a grade, 96.6% within one grade.

> "Table 4: Baseline SLA results on Dev set."

## Discussion


## Related Claims
- [Dev and Eval test sets were selected from fully annotated complete test submissions with grade distributions concentrated at B1 to B2](si-dev-eval-selection-grade-distribution.md) — related
- [The baseline Whisper-small ASR system transcribes L2 learner speech at a 10.4% WER on the S&I Dev set](s-i-2025-baseline-asr-wer-10-4.md) — related
