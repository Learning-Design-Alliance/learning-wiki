---
type: claim
title: AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)
description: AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)
id: ai-grading-run-to-run-reliability-icc
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` On total scores per student, the AI showed high run-to-run consistency: ICC(A,1) = 0.967 for a single run and ICC(A,5) = 0.993 if five runs were averaged, with a 95% repeatability coefficient of 5.33 points. [→ Jan Cvengros and Gerd Kortemeyer 2026](#jan-cvengros-and-gerd-kortemeyer-2026)
`q2 i?` At the item×student level (rubric cells), agreement was lower yet still strong: ICC(A,1) = 0.836 and ICC(A,5) = 0.962, with Sw = 0.25 points and RC = 0.68 points per cell. [→ Jan Cvengros and Gerd Kortemeyer 2026 (2)](#jan-cvengros-and-gerd-kortemeyer-2026-2)

## Evidence

### Jan Cvengros and Gerd Kortemeyer 2026

Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4

`q2 · i?` · `design · r2`

Inter-run reliability analysis treating five independent AI grading runs as five raters, using two-way random-effects absolute-agreement ICC on raw total scores. The article also reports Sw = 1.92 points and a 95% repeatability coefficient RC = 5.33 points, with Kendall's W = 0.959 for rank stability.

> "ICC(A,1)=0 .967 for a single run and ICC(A,5) =0 .993 if one were to average five runs"

### Jan Cvengros and Gerd Kortemeyer 2026 (2)

Jan Cvengros and Gerd Kortemeyer. (2026). Assisting the grading of a handwritten general chemistry exam with artificial intelligence. Discover Artificial Intelligence. https://doi.org/10.1007/s44163-026-01606-4

`q2 · i?` · `design · r2`

Same five-run reliability analysis computed at the rubric-cell (item×student) level. The article notes cell-level jitter is small, explaining why summed totals are very stable, and cautions that with about one third of ground-truth scores at zero the ICC would be inflated.

> "At the item×student level (rubric cells), agreement was lower (as expected for finer granularity), yet still strong: ICC(A,1) =0 .836 and ICC(A,5) =0 .962, with Sw =0 .25 points and RC =0 .68 points per cell"

## Discussion


## Related Claims
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
- [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)](ai-total-scores-align-with-ta-grades-chemistry-exam.md) — related
- [Three independent expert instructors reached exceptionally high inter-rater reliability when grading 1200 bash exam responses, establishing a reliable human reference standard](expert-triad-high-inter-rater-reliability-bash-grading.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Spanish Math and Reading scores show high marginal reliability and moderate-to-strong test-retest stability, lowest for fall–spring and kindergarten](spanish-reliability-marginal-test-retest.md) — related
- [Multimodal LLMs grading handwritten student work achieved κ = 0.90 on arithmetic but κ ≈ 0.47 on interpreting student illustrations](multimodal-llm-grading-kappa-arithmetic-illustrations.md) — related
