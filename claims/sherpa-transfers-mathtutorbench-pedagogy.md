---
type: claim
title: "SHERPA training transfers to the external MathTutorBench benchmark, raising the pedagogy average from 52.5% to 79.2% and beating PedagogicalRL on all four response-generation metrics"
description: "SHERPA training transfers to the external MathTutorBench benchmark, raising the pedagogy average from 52.5% to 79.2% and beating PedagogicalRL on all four response-generation metrics"
id: sherpa-transfers-mathtutorbench-pedagogy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# SHERPA training transfers to the external MathTutorBench benchmark, raising the pedagogy average from 52.5% to 79.2% and beating PedagogicalRL on all four response-generation metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On MathTutorBench, SHERPA DP achieves the highest Pedagogy Average (79.2%) among evaluated models and improves on all four teacher response generation metrics. [→ Weixian Xu 2026](#weixian-xu-2026)

## Evidence

### Weixian Xu 2026

Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang. (2026). SHERPA: TEACHINGLLMS TOTEACHADAPTIVELY. [doi:10.48550/arXiv.2610.08778](https://doi.org/10.48550/arXiv.2610.08778)

`q2 · i?` · `design · r?`

Benchmark evaluation of the trained teacher on MathTutorBench's teacher response generation tasks (Scaffolding, Instruction Following, and harder variants), scored by Ped-RM win rates. The article reports instruction-following win rates rising "from 74.0% to 90.3%" standard and "from 70.6% to 87.2%" hard.

> "SHERPA DP achieves the highest Pedagogy Average among the evaluated models, at 79.2%, compared with 52.5% for the untrained backbone and 63.2% for PedagogicalRL, and improves on all four constituent metrics."

## Discussion


## Related Claims
- [Human high school teachers prefer SHERPA DP responses over the base model in 79.6% of pairwise comparisons, including for preferences unseen during training](human-teachers-prefer-sherpa-79-6-percent.md) — related
- [Training a teacher LLM with SHERPA on diverse-preference student archetypes raises simulated student test accuracy across all seven archetypes, including unseen ones](sherpa-dp-raises-student-accuracy-all-archetypes.md) — related
- [Adding gate-failure penalties based on predefined pedagogical criteria harms teaching performance and generalization, while training on student improvement alone allows broader capabilities to emerge](gate-penalties-harm-generalization-student-improvement-reward.md) — related
- [EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens](eduardo-27b-highest-mathtutorbench-pedagogy-win-rate.md) — related
- [SHERPA-style teaching-specific training shows a side effect: mistake-location accuracy declines across all trained teachers, and most regress on Socratic questioning](teaching-training-side-effect-mistake-location-decline.md) — related
- [The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters](llm-judge-pipeline-validated-against-human-raters.md) — related
