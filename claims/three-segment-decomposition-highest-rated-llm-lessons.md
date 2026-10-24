---
type: claim
title: Task decomposition into three segments yields the highest-rated LLM-generated tutor training lessons, while single-step generation yields the lowest
description: Task decomposition into three segments yields the highest-rated LLM-generated tutor training lessons, while single-step generation yields the lowest
id: three-segment-decomposition-highest-rated-llm-lessons
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: jionghao-lin-2025
    resource: "https://doi.org/10.48550/arxiv.2506.17356"
    title: "Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger. (2025). Automatic Large Language Models Creation of Interactive Learning Lessons. arXiv preprint. https://arxiv.org/abs/2506.17356 [doi:10.48550/arxiv.2506.17356](https://doi.org/10.48550/arxiv.2506.17356)"
    author: Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Task decomposition into three segments yields the highest-rated LLM-generated tutor training lessons, while single-step generation yields the lowest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The three-segment prompting approach achieved the highest average human rating (14.67) and the one-segment approach the lowest (10.67) for LLM-generated tutor training lessons. [→ Jionghao Lin 2025](#jionghao-lin-2025)

## Evidence

### Jionghao Lin 2025

Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger. (2025). Automatic Large Language Models Creation of Interactive Learning Lessons. arXiv preprint. https://arxiv.org/abs/2506.17356 [doi:10.48550/arxiv.2506.17356](https://doi.org/10.48550/arxiv.2506.17356)

`q2 · i?` · `design · r2`

Human rating study: two coders rated LLM-generated lessons across five segmentation approaches using a 17-code rubric, with inter-rater reliability Cohen's κ of 0.72. The authors report these findings "indicate that decomposing the lesson generation task into multiple subtasks can enhance the quality of the generated content."

> "The results of the human rating scores (Table 1) demonstrate that the three-segment approach (Three Seg.) achieved the highest average rating (14.67) for lesson generation, while the one-segment approach (One Seg.) received the lowest average rating (10.67)."

## Discussion


## Related Claims
- [Feedback quality in LLM-generated lessons improved with three or more segments compared to one- or two-segment prompting](feedback-improves-three-or-more-segments.md) — related
- [The highest decomposition level (five segments) performed slightly worse than the three-segment approach, suggesting non-monotonic benefits of decomposition](five-segment-decomposition-slightly-worse-than-three.md) — related
- [Problem decomposition, artifact creation, data practices, and testing/debugging appear in all 28 reviewed CT manuscripts, while iterative refinement appears in 17](ct-aspect-coverage-across-ct-literature.md) — related
- [LLM-generated lessons produced inauthentic references even when combined with RAG over verified academic papers](rag-does-not-ensure-citation-authenticity.md) — related
- [Lesson designers identify generic feedback and unclear title-page and instruction sections as key weaknesses of LLM-generated lessons](llm-lesson-weaknesses-generic-feedback-clarity.md) — related
