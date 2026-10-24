---
type: claim
title: AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)
description: AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)
id: ai-total-scores-align-with-ta-grades-chemistry-exam
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: jan-cvengros-and-gerd-kortemeyer-2026
    resource: "https://doi.org/10.1007/s44163-026-01606-4"
    title: "Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4"
    author: Jan Cvengros and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: jan-cvengros-and-gerd-kortemeyer-2026-2
    resource: "https://doi.org/10.1007/s44163-026-01606-4"
    title: "Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4"
    author: Jan Cvengros and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The aggregate AI-assigned total score achieved an R2 of 0.91 against TA-assigned totals, exceeding per-problem agreement because random item-level scoring errors partially cancel in the sum. [→ Jan Cvengros and Gerd Kortemeyer 2026](#jan-cvengros-and-gerd-kortemeyer-2026)
`q2 i?` For the individual six problems, AI-derived scores correlated with human scores at R2 values ranging from 0.61 to 0.85, which the authors judge too low for grading without additional measures. [→ Jan Cvengros and Gerd Kortemeyer 2026 (2)](#jan-cvengros-and-gerd-kortemeyer-2026-2)

## Evidence

### Jan Cvengros and Gerd Kortemeyer 2026

Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4

`q2 · i?` · `design · r2`

Descriptive linear-fit comparison of AI-assigned versus TA-assigned total scores for 296 consenting students in the ETH Zurich general chemistry final exam. The article reports that "the aggregate total score shown in the top-left panel of Fig. 11 achieved an R2 of 0.91", attributing the gain over per-problem fits to partial cancellation of unsystematic item-level misgrading.

> "the aggregate total score shown in the top-left panel of Fig. 11 achieved an R2 of 0.91"

### Jan Cvengros and Gerd Kortemeyer 2026 (2)

Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4

`q2 · i?` · `design · r2`

Per-problem scatterplots and linear regressions of AI-assigned versus TA-assigned points (Fig. 10), one data point per student. The article reports R2 "ranging from 0.61 to 0.85" and states this per-problem reliability "is low and not suitable for grading without additional measures".

> "for the individual six problems, the AI-derived scores correlated with human scores at coefficients of determination ( R2) ranging from 0.61 to 0.85"

## Discussion

## Related Claims

- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — the general claim this finding bears on, with the studies behind it
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [AI total scores correlate strongly with official human scores on handwritten physics assessments (r = 0.91–0.97 in Round I; 0.93–0.96 in Round II)](ai-human-total-score-correlation-handwritten-physics.md) — related
- [Round II raised exact question-part agreement from about 63% to about 70% and cut parts differing by more than one point from about 13% to 7%, while exact partial-credit scoring remained hardest](question-part-agreement-partial-credit-limits.md) — related
- [LLM-based rubric scores agreed with expert ratings at the total-score level and on cognitive-process dimensions, but agreement was low for more subjective dimensions](ai-expert-agreement-cognitive-versus-subjective-dimensions.md) — related
- [A page-by-page, rubric-guided multimodal LLM workflow graded an authentic handwritten exam in about three hours at roughly $100 in token costs, versus about $3,500 in TA time](ai-grading-workflow-feasibility-cost.md) — related
- [The revised Round II grading workflow reduced AI over-awarding and total-score MAD, most clearly for OE1 (7.1% to 4.8%) and QM (9.4% to 3.8%)](revised-workflow-reduces-overawarding-mad.md) — related
- [AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels](ai-grading-failure-modes-graphical-tasks.md) — related
