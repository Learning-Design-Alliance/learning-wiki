---
type: claim
title: GPT-4 rubric grades of written physics solutions correlate positively with manual grading, with R² ≈ 0.83 for total scores
description: GPT-4 rubric grades of written physics solutions correlate positively with manual grading, with R² ≈ 0.83 for total scores
id: gpt4-total-score-correlation-manual-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
source_checked: 2026-11-20
recheck_by: 2026
sources:
  - id: gerd-kortemeyer-2023
    resource: "https://doi.org/10.48550/arXiv.2304.11221"
    title: "Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course?. [doi:10.48550/arXiv.2304.11221](https://doi.org/10.48550/arXiv.2304.11221)"
    author: Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 rubric grades of written physics solutions correlate positively with manual grading, with R² ≈ 0.83 for total scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Total scores assigned by GPT-4 correlate with the author's manual total scores with R² ≈ 0.83, but fluctuations are higher in partial-credit situations. [→ Gerd Kortemeyer 2023](#gerd-kortemeyer-2023)

## Evidence

### Gerd Kortemeyer 2023

Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course?. [doi:10.48550/arXiv.2304.11221](https://doi.org/10.48550/arXiv.2304.11221)

`q2 · i?` · `design · r2`

Correlation analysis of AI vs. manual total scores for 25 sample solutions (Fig. 11), each AI score averaged over about 15 grading rounds. The study found "R2 ≈ 0.83" for best solutions, with GPT assigning "almost 0.9 points higher" scores on average.

> "The scores for the best solutions agree fairly well with the linear interpolation (R2 ≈ 0.83), but fluctuations are higher in partial credit situations. On the average, GPT assigns total scores that are almost 0.9 points higher than those by the author"

## Discussion


## Related Claims
- [GPT-4 grading shows high score variability across repeated rounds, especially for numerical correctness](gpt4-grading-score-variability.md) — related
- [The revised Round II grading workflow reduced AI over-awarding and total-score MAD, most clearly for OE1 (7.1% to 4.8%) and QM (9.4% to 3.8%)](revised-workflow-reduces-overawarding-mad.md) — related
- [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)](ai-total-scores-align-with-ta-grades-chemistry-exam.md) — related
- [Round II raised exact question-part agreement from about 63% to about 70% and cut parts differing by more than one point from about 13% to 7%, while exact partial-credit scoring remained hardest](question-part-agreement-partial-credit-limits.md) — related
- [AI total scores correlate strongly with official human scores on handwritten physics assessments (r = 0.91–0.97 in Round I; 0.93–0.96 in Round II)](ai-human-total-score-correlation-handwritten-physics.md) — related
- [Focused rubric refinement that made required physics and scoring conditions explicit reduced AI–official disagreements on targeted questions (e.g., Grover item MAD 1.1 to 0.4 marks, r 0.70 to 0.82)](explicit-rubric-conditions-reduce-ai-disagreement.md) — related
- [Rubric-based and parts-based grading workflows outperform problem-based grading, possibly because GPT-4-32k cannot reliably add numbers](wf1-wf2-outperform-wf3-grading.md) — related
