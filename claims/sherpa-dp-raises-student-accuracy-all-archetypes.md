---
type: claim
title: Training a teacher LLM with SHERPA on diverse-preference student archetypes raises simulated student test accuracy across all seven archetypes, including unseen ones
description: Training a teacher LLM with SHERPA on diverse-preference student archetypes raises simulated student test accuracy across all seven archetypes, including unseen ones
id: sherpa-dp-raises-student-accuracy-all-archetypes
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

# Training a teacher LLM with SHERPA on diverse-preference student archetypes raises simulated student test accuracy across all seven archetypes, including unseen ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SHERPA DP achieves 69.0% overall student test accuracy, outperforming the untrained Qwen3-8B backbone, PedagogicalRL, and SHERPA NP on every student archetype, including out-of-distribution ones. [→ Weixian Xu 2026](#weixian-xu-2026)

## Evidence

### Weixian Xu 2026

Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang. (2026). SHERPA: TEACHINGLLMS TOTEACHADAPTIVELY. [doi:10.48550/arXiv.2610.08778](https://doi.org/10.48550/arXiv.2610.08778)

`q2 · i?` · `design · r?`

Simulation-based evaluation on 528 filtered MATH problems with a frozen Qwen3-1.7B student across seven archetypes (four in-distribution, three out-of-distribution). The article reports "an overall test accuracy of 69.0%" for SHERPA DP versus 48.6% for the untrained backbone, with 95% CI [66.8, 71.2].

> "As shown in Table 1, SHERPA DP achieves an overall test accuracy of 69.0%, outperforming the untrained backbone, PedagogicalRL, and SHERPANP on every student archetype."

## Discussion


## Related Claims
- [Gated student archetypes, unlike prompted students, show the selectivity and informativeness needed for outcome-based teacher training: improvement concentrated on matched teacher-student pairs and lower complaint rates](gated-archetypes-selective-informative-vs-prompted.md) — related
- [Human high school teachers prefer SHERPA DP responses over the base model in 79.6% of pairwise comparisons, including for preferences unseen during training](human-teachers-prefer-sherpa-79-6-percent.md) — related
- [SHERPA training transfers to the external MathTutorBench benchmark, raising the pedagogy average from 52.5% to 79.2% and beating PedagogicalRL on all four response-generation metrics](sherpa-transfers-mathtutorbench-pedagogy.md) — related
- [SHERPA-style teaching-specific training shows a side effect: mistake-location accuracy declines across all trained teachers, and most regress on Socratic questioning](teaching-training-side-effect-mistake-location-decline.md) — related
