---
type: claim
title: The highest decomposition level (five segments) performed slightly worse than the three-segment approach, suggesting non-monotonic benefits of decomposition
description: The highest decomposition level (five segments) performed slightly worse than the three-segment approach, suggesting non-monotonic benefits of decomposition
id: five-segment-decomposition-slightly-worse-than-three
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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

# The highest decomposition level (five segments) performed slightly worse than the three-segment approach, suggesting non-monotonic benefits of decomposition

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The five-segment approach, the highest level of task decomposition, performed slightly worse than the three-segment approach in human ratings. [→ Jionghao Lin 2025](#jionghao-lin-2025)

## Evidence

### Jionghao Lin 2025

Jionghao Lin, Jiarui Rao, Sandy Yiyang Zhao, Yuting Wang, Ashish Gurung, Amanda Barany, Jaclyn Ocumpaugh, Ryan S. Baker, and Kenneth R. Koedinger. (2025). Automatic Large Language Models Creation of Interactive Learning Lessons. arXiv preprint. https://arxiv.org/abs/2506.17356 [doi:10.48550/arxiv.2506.17356](https://doi.org/10.48550/arxiv.2506.17356)

`q2 · i?` · `design · r2`

Human rating study of LLM-generated lessons across segmentation levels (Table 1 average ratings: three segments 14.67, five segments 13.33). The authors state the five-segment approach "performed slightly worse than the three-segment approach."

> "Interestingly, the five-segment approach (Five Seg.), which represents the highest level of task decomposition, performed slightly worse than the three-segment approach."

## Discussion


## Related Claims
- [Task decomposition into three segments yields the highest-rated LLM-generated tutor training lessons, while single-step generation yields the lowest](three-segment-decomposition-highest-rated-llm-lessons.md) — related
- [Feedback quality in LLM-generated lessons improved with three or more segments compared to one- or two-segment prompting](feedback-improves-three-or-more-segments.md) — related
- [Model-level judge quality is non-monotonic in dataset size: the 13,882-pair v1.1 yields the best model (6.39), while both expansion to ~20,000 pairs (6.33) and aggressive curation to 7,130 pairs (6.12) reduce quality](non-monotonic-quality-volume-iks-instruct.md) — a narrower finding that bears on this claim
