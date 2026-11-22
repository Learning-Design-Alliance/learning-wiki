---
type: claim
title: "SHERPA-style teaching-specific training shows a side effect: mistake-location accuracy declines across all trained teachers, and most regress on Socratic questioning"
description: "SHERPA-style teaching-specific training shows a side effect: mistake-location accuracy declines across all trained teachers, and most regress on Socratic questioning"
id: teaching-training-side-effect-mistake-location-decline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: weixian-xu-2026
    resource: "https://doi.org/10.48550/arXiv.2610.08778"
    title: "Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang. (2026). SHERPA: TEACHINGLLMS TOTEACHADAPTIVELY. [doi:10.48550/arXiv.2610.08778](https://doi.org/10.48550/arXiv.2610.08778)"
    author: Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# SHERPA-style teaching-specific training shows a side effect: mistake-location accuracy declines across all trained teachers, and most regress on Socratic questioning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Mistake-location accuracy declines across all trained teachers and most also regress on Socratic questioning, which the authors attribute to a side effect of specific training for teaching. [→ Weixian Xu 2026](#weixian-xu-2026)

## Evidence

### Weixian Xu 2026

Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang. (2026). SHERPA: TEACHINGLLMS TOTEACHADAPTIVELY. [doi:10.48550/arXiv.2610.08778](https://doi.org/10.48550/arXiv.2610.08778)

`q2 · i?` · `design · r?`

MathTutorBench student-understanding results (Table 2) show the decline for trained teachers. The article notes SHERPA DP "retains higher mistake-location accuracy than PedagogicalRL (30.3% versus 18.7%)", so the size of the regression varies by method.

> "Meanwhile, mistake-location accuracy declines across all trained teachers, and most also regress on Socratic questioning, suggesting a side effect of specific training for teaching."

## Discussion


## Related Claims
- [Training a teacher LLM with SHERPA on diverse-preference student archetypes raises simulated student test accuracy across all seven archetypes, including unseen ones](sherpa-dp-raises-student-accuracy-all-archetypes.md) — related
- [GRPO alignment collapses Mathematical-Knowledge-for-Teaching utterances and surges Socratic-style Exploratory questions in tutor output](alignment-shifts-mkt-collapse-exploratory-surge.md) — related
- [Human high school teachers prefer SHERPA DP responses over the base model in 79.6% of pairwise comparisons, including for preferences unseen during training](human-teachers-prefer-sherpa-79-6-percent.md) — related
- [SHERPA training transfers to the external MathTutorBench benchmark, raising the pedagogy average from 52.5% to 79.2% and beating PedagogicalRL on all four response-generation metrics](sherpa-transfers-mathtutorbench-pedagogy.md) — related
