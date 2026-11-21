---
type: claim
title: "Students rated Ethel's handwritten-homework feedback helpful and correct in 3/4th of cases, but the system tended to underestimate solution correctness, mostly due to handwriting recognition"
description: "Students rated Ethel's handwritten-homework feedback helpful and correct in 3/4th of cases, but the system tended to underestimate solution correctness, mostly due to handwriting recognition"
id: ethel-homework-feedback-ratings
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: kortemeyer-2024
    resource: "https://doi.org/10.1119/5.0231187"
    title: "Kortemeyer, G. (2024). Ethel: A Virtual Teaching Assistant. arXiv. [doi:10.1119/5.0231187](https://doi.org/10.1119/5.0231187)"
    author: Kortemeyer, G.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Students rated Ethel's handwritten-homework feedback helpful and correct in 3/4th of cases, but the system tended to underestimate solution correctness, mostly due to handwriting recognition

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Students rated the homework feedback to be helpful and correct in 3/4th of the cases, while Ethel tended to underestimate the correctness of students' solutions, with the issue mostly being handwriting recognition. [→ Kortemeyer 2024](#kortemeyer-2024)

## Evidence

### Kortemeyer 2024

Kortemeyer, G. (2024). Ethel: A Virtual Teaching Assistant. arXiv. [doi:10.1119/5.0231187](https://doi.org/10.1119/5.0231187)

`q2 · i?` · `design · r2`

Deployment of the homework-feedback component on scanned handwritten solutions converted to LaTeX with Mathpix and GPT-4V: "Students rated the feedback to be helpful and correct in 3/4th of the cases," with underestimation of correctness traced mostly to handwriting recognition.

> "Students rated the feedback to be helpful and correct in 3/4th of the cases. Ethel tended to underestimate the correctness of the students' solutions, where the issue was mostly handwriting recognition"

## Discussion


## Related Claims
- [Automated grading was substantially less reliable for graphical solutions than mathematical derivations, and showed high precision but low recall in identifying passing exam solutions](ethel-grading-reliability-format-precision-recall.md) — related
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) — related
- [AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels](ai-grading-failure-modes-graphical-tasks.md) — related
- [MathPix with GPT-4V support produces more reliable and reproducible OCR than using GPT-4V alone for handwritten exam solutions](mathpix-gpt4v-ocr-more-reliable-than-gpt4v-alone.md) — related
- [LLM handwriting recognition of scanned physics solutions is decent but not sufficiently reliable for grading real exam papers](llm-handwriting-recognition-unreliable-for-grading.md) — related
