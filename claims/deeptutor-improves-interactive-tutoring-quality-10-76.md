---
type: claim
title: "DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench"
description: "DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench"
id: deeptutor-improves-interactive-tutoring-quality-10-76
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

# DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On TutorBench's first-person interactive evaluation, DeepTutor improves overall quality by 10.76% relative to the Naive Tutor baseline and leads on nearly all of ten metrics. [→ Bingxi Zhao 2026](#bingxi-zhao-2026)

## Evidence

### Bingxi Zhao 2026

Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962

`q2 · i?` · `design · r2`

LLM-simulated interactive evaluation of DeepTutor versus four baselines (Naive, CoT, Self-Refine, ReAct) sharing the same backbone and RAG, over the full TutorBench release of 270 tasks. The article reports DeepTutor "improves overall quality by 10.76% and leads on nearly all metrics"; relative gain is not a standardized effect size.

> "The four baselines remain tightly clustered, indicating that adding CoT, self-refinement, or ReAct-style tool use to the same backbone and RAG interface is not sufficient to matchDeepTutor's learner-adaptive behavior.DeepTutor improves overall quality by 10.76% and leads on nearly all metrics."

## Discussion


## Related Claims
- [DeepTutor's interactive tutoring gains are stable across five university-level domains, varying only 0.16 points in overall quality](deeptutor-gains-stable-across-five-domains.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
