---
type: claim
title: Applied to the full dataset of 936 students, the LLM reproduced the human-observed growth trends, detecting significant growth on Q25 and Q26 but none on Q27
description: Applied to the full dataset of 936 students, the LLM reproduced the human-observed growth trends, detecting significant growth on Q25 and Q26 but none on Q27
id: llm-scales-ct-growth-detection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: sean-savage-2026
    resource: "https://doi.org/10.48550/arxiv.2608.06200"
    title: "Sean Savage, Anand Shanker, Grace Michlitsch, and N. Sanjay Rebello. (2026). Using LLMs to Detect Growth in Computational Thinking in Introductory Physics. arXiv preprint. https://arxiv.org/abs/2608.06200 [doi:10.48550/arxiv.2608.06200](https://doi.org/10.48550/arxiv.2608.06200)"
    author: Sean Savage, Anand Shanker, Grace Michlitsch, and N. Sanjay Rebello
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Applied to the full dataset of 936 students, the LLM reproduced the human-observed growth trends, detecting significant growth on Q25 and Q26 but none on Q27

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across over 2,800 responses from N = 936 students, the LLM detected highly statistically significant growth (p < 0.001) on Q25 and Q26, while Q27 showed no measurable growth on any parameter. [→ Sean Savage 2026](#sean-savage-2026)

## Evidence

### Sean Savage 2026

Sean Savage, Anand Shanker, Grace Michlitsch, and N. Sanjay Rebello. (2026). Using LLMs to Detect Growth in Computational Thinking in Introductory Physics. arXiv preprint. https://arxiv.org/abs/2608.06200 [doi:10.48550/arxiv.2608.06200](https://doi.org/10.48550/arxiv.2608.06200)

`q2 · i?` · `design · r2`

The validated multimodal LLM pipeline was deployed across the full dataset of 936 students, evaluating over 2,800 total responses with majority voting across three runs. The article reports significant growth on Q25 and Q26 and no measurable growth on Q27, including STP and Physics Correctness.

> "When applied to the full dataset ofN= 936students, the LLM analysis confirmed the macroscopic trends observed in the human baseline. By evaluating over 2,800 total re- sponses, the model detected highly statistically significant growth (p <0.001) across Q25 and Q26."

## Discussion


## Related Claims
- [Growth is compartmentalized by question: on the code-tracing prompt students grew in procedural code tracing while physics correctness improved only slightly](compartmentalized-ct-growth-by-question.md) — related
- [Students in a computationally intensive introductory physics course show large-magnitude growth in Data Practices and moderate growth in Computational Problem-Solving and Systems Thinking on written CT assessments](ct-growth-data-practices-intro-physics.md) — related
- [Modeling and Simulation Practices showed no measurable growth, attributed to a ceiling effect from students' high prior knowledge](msp-no-growth-ceiling-effect.md) — related
