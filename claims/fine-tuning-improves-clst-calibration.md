---
type: claim
title: Fine-tuning on KTLP data improved CLST output calibration, moving predictions closer to the ideal diagonal
description: Fine-tuning on KTLP data improved CLST output calibration, moving predictions closer to the ideal diagonal
id: fine-tuning-improves-clst-calibration
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: heeseok-jung-2025
    resource: "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    title: "Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    author: Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Fine-tuning on KTLP data improved CLST output calibration, moving predictions closer to the ideal diagonal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Calibration plots showed the untuned model exhibited poor output calibration, while calibration improved as fine-tuning data increased from 16 to 64 students. [→ Heeseok Jung 2025](#heeseok-jung-2025)

## Evidence

### Heeseok Jung 2025

Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

`q2 · i?` · `causal · r2`

Calibration plot analysis (Figure 5) comparing the untuned mistral-7b-instruct-v02 backbone with fine-tuned CLST on each dataset, relating binned average predicted values to observed positive-class fractions. The article reports "output calibration significantly improved" from 16 to 64 fine-tuning students.

> "the untuned model exhibited poor output calibration; in contrast, output calibration significantly improved as the number of students in the KTLP dataset used for fine-tuning increased from 16 to 64."

## Discussion


## Related Claims
- [Fine-tuning CLST on KTLP-formatted data improved predictive performance across all datasets, with gains growing with training students](fine-tuning-improves-clst-auc.md) — related
- [In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students](clst-outperforms-baselines-cold-start.md) — related
