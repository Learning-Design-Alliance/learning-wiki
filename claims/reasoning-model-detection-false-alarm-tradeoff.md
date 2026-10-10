---
type: claim
title: "A reasoning-capable open-weight model detects 84% of hidden misconceptions but at realistic prevalence false alarms outnumber genuine detections roughly 8 to 1"
description: "A reasoning-capable open-weight model detects 84% of hidden misconceptions but at realistic prevalence false alarms outnumber genuine detections roughly 8 to 1"
id: reasoning-model-detection-false-alarm-tradeoff
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: moiz-imran-2026
    resource: "https://orcid.org/0000-0002-5878-2143"
    title: "Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143"
    author: Moiz Imran, Sahan Bulathwela
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A reasoning-capable open-weight model detects 84% of hidden misconceptions but at realistic prevalence false alarms outnumber genuine detections roughly 8 to 1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Gemma 4 26B with the graduated rubric detects 83.6% of TM cases and flags a further 11.5% for clarification, but at 1.6% prevalence achieves only 10.9% positive predictive value. [→ Moiz Imran 2026](#moiz-imran-2026)

## Evidence

### Moiz Imran 2026

Moiz Imran, Sahan Bulathwela. (2026). The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden Misconceptions. PEAF 2026: Workshop on Pedagogical Evaluation of Automated Feedback. https://orcid.org/0000-0002-5878-2143

`q2 · i?` · `design · r2`

Results evaluation of Gemma 4 26B on the 3,702-response test set. Table 1 prints TM detection 83.6 [72.1, 91.4] and TC false positive rate 62.4; the quoted sentence reports the "10.9% positive predictive value" at 1.6% prevalence.

> "However, at 1.6% prevalence, even 84% detection with 18% false positive rate yields only 10.9% positive predictive value (roughly 8 false alarms per genuine detection)."

## Discussion


## Related Claims
- [Validator false-negative cases reveal structural reasoning weaknesses, including answer-schema misinterpretation and internal inconsistency](code-gen-validator-fn-reasoning-weaknesses.md) — related
- [At natural TM prevalence (1.6%), even the best model generates roughly 4.3 false alarms per genuine detection, making fully automated stand-alone screening not viable on its own](false-alarms-make-standalone-screening-impractical.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [Including a mark scheme in the prompt does not change misconception detection but significantly reduces false positives against correct-reasoning students](mark-scheme-reduces-false-positives.md) — related
- [Fine-tuned classifiers detect only about 57% of correct-answer misconceptions despite near-perfect wrong-answer classification](fine-tuned-classifiers-miss-correct-answer-misconceptions.md) — related
