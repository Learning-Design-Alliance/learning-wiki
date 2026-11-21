---
type: claim
title: Automated grading was substantially less reliable for graphical solutions than mathematical derivations, and showed high precision but low recall in identifying passing exam solutions
description: Automated grading was substantially less reliable for graphical solutions than mathematical derivations, and showed high precision but low recall in identifying passing exam solutions
id: ethel-grading-reliability-format-precision-recall
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
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
  - id: kortemeyer-2024-2
    resource: "https://doi.org/10.1119/5.0231187"
    title: "Kortemeyer, G. (2024). Ethel: A Virtual Teaching Assistant. arXiv. [doi:10.1119/5.0231187](https://doi.org/10.1119/5.0231187)"
    author: Kortemeyer, G.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Automated grading was substantially less reliable for graphical solutions than mathematical derivations, and showed high precision but low recall in identifying passing exam solutions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Grading graphical solutions like process diagrams was substantially less reliable than grading mathematical derivations, with inaccuracies often due to extraneous visual elements in freehand drawings. [→ Kortemeyer 2024](#kortemeyer-2024)
`q2 i?` The grading system showed high precision in identifying passing exam solutions but low recall, missing about half of the other passing solutions. [→ Kortemeyer 2024 (2)](#kortemeyer-2024-2)

## Evidence

### Kortemeyer 2024

Kortemeyer, G. (2024). Ethel: A Virtual Teaching Assistant. arXiv. [doi:10.1119/5.0231187](https://doi.org/10.1119/5.0231187)

`q2 · i?` · `design · r2`

Grading-reliability analysis from the thermodynamics exam study: "Grading graphical solu- tions, like process diagrams, was substantially less reli- able than grading mathematical derivations," with inaccuracies often due to extraneous visual elements in freehand drawings.

> "Grading graphical solu- tions, like process diagrams, was substantially less reli- able than grading mathematical derivations, with inaccu- racies often due to extraneous visual elements in freehand drawings."

### Kortemeyer 2024 (2)

Kortemeyer, G. (2024). Ethel: A Virtual Teaching Assistant. arXiv. [doi:10.1119/5.0231187](https://doi.org/10.1119/5.0231187)

`q2 · i?` · `design · r2`

Overall performance of the grading system on the same exam: "high pre- cision in identifying passing exam solutions but had low recall, missing about half of the other passing solutions."

> "Overall, the grading system showed high pre- cision in identifying passing exam solutions but had low recall, missing about half of the other passing solutions."

## Discussion


## Related Claims
- [AI-assisted grading achieves high precision for identifying passing exams but low recall, meaning failing grades still require human grading](high-precision-low-recall-ai-pass-fail.md) — possibly the same claim (merge candidate)
- [AI grading of hand-drawn graphics shows no correlation with TA grades, unlike mathematical derivation parts](hand-drawn-graphics-ai-grading-unreliable.md) — possibly the same claim (merge candidate)
- [LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes](llm-fast-mode-limited-thinking-mode-better-agreement.md) — related
- [Students rated Ethel's handwritten-homework feedback helpful and correct in 3/4th of cases, but the system tended to underestimate solution correctness, mostly due to handwriting recognition](ethel-homework-feedback-ratings.md) — related
- [LLM handwriting recognition of scanned physics solutions is decent but not sufficiently reliable for grading real exam papers](llm-handwriting-recognition-unreliable-for-grading.md) — related
- [Graphical GenAI systems failed to produce reliable scientific illustrations for college-level content, with error rates approaching 100%](image-genai-error-rates-approaching-100-percent.md) — related
- [LLM grading of handwritten physics is reliable for fully correct scripts but substantially less accurate for imperfect scripts requiring partial credit](handwritten-partial-credit-remains-hard.md) — related
