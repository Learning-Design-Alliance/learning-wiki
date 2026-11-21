---
type: claim
title: Once trained, the ML models annotate student responses far faster than manual application of the measurement scheme (under 1 minute versus about 5 hours per ~100 responses for one problem)
description: Once trained, the ML models annotate student responses far faster than manual application of the measurement scheme (under 1 minute versus about 5 hours per ~100 responses for one problem)
id: ml-annotation-faster-than-manual-coding
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: gili-2025
    resource: "https://doi.org/10.1103/v6gw-lv4c"
    title: "Gili, Heuton, Shah, Hammer, and Hughes. (2025). Combining physics education and machine learning research to measure evidence of students' mechanistic sensemaking. arXiv. [doi:10.1103/v6gw-lv4c](https://doi.org/10.1103/v6gw-lv4c)"
    author: Gili, Heuton, Shah, Hammer, and Hughes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Once trained, the ML models annotate student responses far faster than manual application of the measurement scheme (under 1 minute versus about 5 hours per ~100 responses for one problem)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Manual annotation took about 5 hours per ~100 responses for one problem, while trained models process the same amount of data in under 1 minute, and training takes under 3 hours. [→ Gili 2025](#gili-2025)

## Evidence

### Gili 2025

Gili, Heuton, Shah, Hammer, and Hughes. (2025). Combining physics education and machine learning research to measure evidence of students' mechanistic sensemaking. arXiv. [doi:10.1103/v6gw-lv4c](https://doi.org/10.1103/v6gw-lv4c)

`q2 · i?` · `design · r2`

Efficiency comparison reported in the utility discussion, contrasting the human annotator's time with trained-model processing time on the same volume of data. The article also states training "a model to perform this task is doable in less than 3 hours."

> "Our annotator required about 5 hours to apply our measurement scheme to∼100 student responses for one problem. In contrast, once trained the processing time for our models to annotate the same amount of data is less than 1 minute."

## Discussion


## Related Claims
- [A page-by-page, rubric-guided multimodal LLM workflow graded an authentic handwritten exam in about three hours at roughly $100 in token costs, versus about $3,500 in TA time](ai-grading-workflow-feasibility-cost.md) — related
- [Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant](hdr-human-scoring-time-burden.md) — related
- [Machine-learning-supported grading with complete manual review of all classifier output reduced total exam grading time by 74% (or 64% under a conservative estimate) compared with fully manual grading](ml-supported-grading-cuts-exam-workload-64-74-percent.md) — a broader claim this one bears on
- [The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text](ai-feedback-response-time-and-authoring-efficiency.md) — related
