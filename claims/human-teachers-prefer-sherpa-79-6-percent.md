---
type: claim
title: "Human high school teachers prefer SHERPA DP responses over the base model in 79.6% of pairwise comparisons, including for preferences unseen during training"
description: "Human high school teachers prefer SHERPA DP responses over the base model in 79.6% of pairwise comparisons, including for preferences unseen during training"
id: human-teachers-prefer-sherpa-79-6-percent
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
    kind: causal
    rigour: "?"
---

# Human high school teachers prefer SHERPA DP responses over the base model in 79.6% of pairwise comparisons, including for preferences unseen during training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a human pairwise comparison with 96 high school teachers, SHERPA DP receives a 79.6% win rate over the base model, with the advantage holding across all four injected preferences (75.6-85.5%). [→ Weixian Xu 2026](#weixian-xu-2026)

## Evidence

### Weixian Xu 2026

Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang, Changyu Chen, Diyi Yang. (2026). SHERPA: TEACHINGLLMS TOTEACHADAPTIVELY. [doi:10.48550/arXiv.2610.08778](https://doi.org/10.48550/arXiv.2610.08778)

`q2 · i?` · `causal · r?`

Human study using 320 dialogue contexts from 80 CoMTA conversations, with four injected student preferences (two in-distribution, two unseen); 96 teachers gave 960 judgments. The article reports "87 of 96 teachers favor SHERPA DP more often" and majority voting prefers it on 270 of 320 pairs.

> "Teachers substantially prefer our model: it receives 728 judgments versus 187 for the base model, corresponding to a 79.6% win rate excluding ties."

## Discussion


## Related Claims
- [Training a teacher LLM with SHERPA on diverse-preference student archetypes raises simulated student test accuracy across all seven archetypes, including unseen ones](sherpa-dp-raises-student-accuracy-all-archetypes.md) — related
- [SHERPA training transfers to the external MathTutorBench benchmark, raising the pedagogy average from 52.5% to 79.2% and beating PedagogicalRL on all four response-generation metrics](sherpa-transfers-mathtutorbench-pedagogy.md) — related
- [SHERPA-style teaching-specific training shows a side effect: mistake-location accuracy declines across all trained teachers, and most regress on Socratic questioning](teaching-training-side-effect-mistake-location-decline.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
