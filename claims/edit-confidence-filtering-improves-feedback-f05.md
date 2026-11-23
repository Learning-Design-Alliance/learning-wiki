---
type: claim
title: "Averaged two-sided edit-confidence filtering combined with Strong reference alignment achieves the best feedback F0.5 (44.73 on LNG, 46.94 on S&I), relative gains of 2.4% and 2.1% over the unfiltered baseline"
description: "Averaged two-sided edit-confidence filtering combined with Strong reference alignment achieves the best feedback F0.5 (44.73 on LNG, 46.94 on S&I), relative gains of 2.4% and 2.1% over the unfiltered baseline"
id: edit-confidence-filtering-improves-feedback-f05
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: mengjie-qian-2026
    resource: "https://doi.org/10.2139/ssrn.6588326"
    title: "Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)"
    author: Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Averaged two-sided edit-confidence filtering combined with Strong reference alignment achieves the best feedback F0.5 (44.73 on LNG, 46.94 on S&I), relative gains of 2.4% and 2.1% over the unfiltered baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Filtering low-confidence edits using combined FLT and GEC word-confidence scores consistently improves F0.5 across all settings, with the best configuration (Whispergec+pt, Strong reference, editavg) reaching F0.5 of 44.73 on LNG and 46.94 on S&I. [→ Mengjie Qian 2026](#mengjie-qian-2026)

## Evidence

### Mengjie Qian 2026

Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)

`q2 · i?` · `design · r2`

Edit-confidence filtering evaluation (Section 5.5, Table 6). Thresholds swept from 0.00 to 1.00 in 0.01 increments maximize F0.5; the best setup achieves "an F0.5 of 44.73" on LNG and "46.94" on S&I, relative improvements of 2.4% and 2.1%.

> "The best-performing configuration on LNG is Whispergec+pt with the Strong GEC reference andeditavg, achieving an F0.5 of 44.73, and the best configuration for S&I is the same setup, achieving an F0.5 of 46.94."

## Discussion


## Related Claims
- [Strong GEC reference alignment yields the highest feedback F0.5 (43.69 on LNG, 45.96 on S&I), a 6.4% and 7.8% relative improvement, and is the first approach enabling an end-to-end SGEC system to surpass the partial-cascaded baseline in feedback quality](reference-alignment-boosts-sgec-feedback-f05.md) — related
- [Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model](prompt-conditioned-sgec-improves-feedback-precision.md) — related
- [The Speak & Improve Challenge 2025 is the first shared task to address spoken GEC and holistic spoken language assessment](first-shared-task-spoken-gec-and-sla.md) — related
- [The baseline SGECF system detects and labels learner error types at an overall ERRANT F0.5 of 0.22, with preposition replacement errors best detected](s-i-2025-baseline-sgecf-f05-0-22.md) — related
