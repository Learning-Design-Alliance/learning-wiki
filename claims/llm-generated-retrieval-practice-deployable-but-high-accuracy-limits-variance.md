---
type: claim
title: "LLM-generated retrieval practice was practical to deploy and well received, but high correctness rates (about 70% of items at p=1.0) restricted score variance"
description: "LLM-generated retrieval practice was practical to deploy and well received, but high correctness rates (about 70% of items at p=1.0) restricted score variance"
id: llm-generated-retrieval-practice-deployable-but-high-accuracy-limits-variance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: yuan-an-2026
    resource: "https://doi.org/10.48550/arxiv.2609.27063"
    title: "Yuan An, Lei Wang. (2026). Student Use of LLMs and the Limits of AI-Generated Question Difficulty in Data Science Courses. https://arxiv.org/abs/2609.27063 [doi:10.48550/arxiv.2609.27063](https://doi.org/10.48550/arxiv.2609.27063)"
    author: Yuan An, Lei Wang
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# LLM-generated retrieval practice was practical to deploy and well received, but high correctness rates (about 70% of items at p=1.0) restricted score variance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` In-class deployment of LLM-generated MCQs succeeded logistically, with approximately 70% of items achieving a 100% correct response rate. [→ Yuan An 2026](#yuan-an-2026)

## Evidence

### Yuan An 2026

Yuan An, Lei Wang. (2026). Student Use of LLMs and the Limits of AI-Generated Question Difficulty in Data Science Courses. https://arxiv.org/abs/2609.27063 [doi:10.48550/arxiv.2609.27063](https://doi.org/10.48550/arxiv.2609.27063)

`q2 · i?` · `associational · r1`

Deployment analysis of 311 in-class MCQs across 52 quizzes (7,888 responses from 54 participants) found "approximately 70% of items achieving a 100% correct response rate (p= 1.0)", limiting variance for item statistics.

> "Student scores were high
overall, with approximately 70% of items achieving a 100% correct response rate (p= 1.0). This performance level
restricts score variance"

## Discussion


## Related Claims
- [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) — related
- [On the live single-node deployment, short-answer rounds take ≈32 s (≈$0.015/round) while multiple-choice rounds are ≈4× faster (≈7.6 s, ≈$0.005/round) because grading is deterministic](collearn-latency-cost-efficiency.md) — related
- [The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text](ai-feedback-response-time-and-authoring-efficiency.md) — related
- ConcepTests with roughly 35% to 70% of students answering correctly before discussion appear to produce the highest engagement and most effective discussions — related
