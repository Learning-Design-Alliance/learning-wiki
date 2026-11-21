---
type: claim
title: LLM grading of handwritten physics is reliable for fully correct scripts but substantially less accurate for imperfect scripts requiring partial credit
description: LLM grading of handwritten physics is reliable for fully correct scripts but substantially less accurate for imperfect scripts requiring partial credit
id: handwritten-partial-credit-remains-hard
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jonah-l-donaldson-2026
    resource: "https://doi.org/10.48550/arXiv.2605.23660"
    title: "Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)"
    author: Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM grading of handwritten physics is reliable for fully correct scripts but substantially less accurate for imperfect scripts requiring partial credit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all models in the MM handwritten study, grading accuracy was consistently higher for perfect handwritten solutions than for imperfect ones, with near-zero MAE for perfect scripts. [→ Jonah L. Donaldson 2026](#jonah-l-donaldson-2026)

## Evidence

### Jonah L. Donaldson 2026

Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)

`q2 · i?` · `causal · r1`

MM study Stage III, in which models transcribed and graded deliberately constructed perfect and imperfect handwritten solutions embedding common student misconceptions. The article reports grading accuracy was "consistently higher for perfect handwritten solutions than for imperfect ones", with near-zero MAE deviation from human grading for perfect scripts for all models.

> "Across all models, grading accuracy was consistently higher for perfect handwritten solutions than for imperfect ones."

## Discussion


## Related Claims
- [Across models, higher problem-solving accuracy is associated with lower grading error on imperfect handwritten scripts, more strongly for text-based than diagram-based accuracy](reasoning-accuracy-predicts-grading-reliability.md) — related
- [GPT-4 rubric grades of written physics solutions correlate positively with manual grading, with R² ≈ 0.83 for total scores](gpt4-total-score-correlation-manual-grading.md) — possibly the same claim (merge candidate)
- [Automated grading was substantially less reliable for graphical solutions than mathematical derivations, and showed high precision but low recall in identifying passing exam solutions](ethel-grading-reliability-format-precision-recall.md) — related
