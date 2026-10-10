---
type: claim
title: "DeepTutor's interactive tutoring gains are stable across five university-level domains, varying only 0.16 points in overall quality"
description: "DeepTutor's interactive tutoring gains are stable across five university-level domains, varying only 0.16 points in overall quality"
id: deeptutor-gains-stable-across-five-domains
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
    i: "?"
    kind: design
    rigour: 2
---

# DeepTutor's interactive tutoring gains are stable across five university-level domains, varying only 0.16 points in overall quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Decomposition of DeepTutor's interactive performance by discipline shows overall quality varies by only 0.16 points across the five domains, with Source Faithfulness the most domain-sensitive metric. [→ Bingxi Zhao 2026](#bingxi-zhao-2026)

## Evidence

### Bingxi Zhao 2026

Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962

`q2 · i?` · `design · r2`

Cross-domain decomposition of the first-person interactive simulation (Figure 6) across five disciplines with different discourse structures. The article reports the 0.16-point overall span and a 0.36-point average metric span; these are descriptive scores with no standardized effect size.

> "Overall quality varies by only 0.16 points across the five domains, indicating that the gains are not driven by a single discipline. At the metric level, the average cross-domain span is 0.36 points, with the largest fluctuation appearing inSource Faithfulness"

## Discussion


## Related Claims
- [DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench](deeptutor-improves-interactive-tutoring-quality-10-76.md) — related
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
