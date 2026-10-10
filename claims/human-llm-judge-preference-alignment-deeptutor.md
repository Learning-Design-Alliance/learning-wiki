---
type: claim
title: "Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)"
description: "Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)"
id: human-llm-judge-preference-alignment-deeptutor
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: bingxi-zhao-2026
    resource: "https://arxiv.org/abs/2604.26962"
    title: "Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962"
    author: Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` In a blind pairwise study on 45 TutorBench sessions, human and LLM DeepTutor win rates are strongly correlated across the ten metric-level win-rate pairs (Pearson r = 0.82; Spearman ρ = 0.83). [→ Bingxi Zhao 2026](#bingxi-zhao-2026)

## Evidence

### Bingxi Zhao 2026

Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962

`q2 · i3` · `design · r2`

Blind pairwise human study on a domain-stratified subset of 45 TutorBench sessions (nine per domain), comparing anonymized DeepTutor and Naive Tutor outputs under identical profiles and tasks. The printed correlations r = 0.82 and ρ = 0.83 indicate strong human–judge alignment.

> "human and LLMDeepTutorwin rates are strongly correlated across the ten metric-level win-rate pairs (Pearson𝑟= 0.82, 𝑝= 0.0038; Spearman𝜌= 0.83, 𝑝= 0.0027). This agreement suggests that the LLM judge is not merely favoringDeepTutorglobally"

## Discussion


## Related Claims
- [DeepTutor's interactive tutoring gains are stable across five university-level domains, varying only 0.16 points in overall quality](deeptutor-gains-stable-across-five-domains.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [The automated scoring system's agreement with human raters varied widely by dimension, with information fidelity showing a weak, non-significant correlation](yunyi-human-agreement-varies-by-dimension.md) — related
- [DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench](deeptutor-improves-interactive-tutoring-quality-10-76.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [A substantial part of the LLM rating advantage appears attributable to comment length, as length-adjusted scores converge on every dimension except tone](length-explains-llm-rating-advantage.md) — related
- [LLM alignment with expert teaching ratings does not predict, and is often negatively associated with, alignment with student learning gains](proxy-alignment-not-impact-alignment-llm-classroom.md) — reports the opposite
