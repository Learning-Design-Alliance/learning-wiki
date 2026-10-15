---
type: claim
title: "Practical educational skill does not follow from knowledge scores: Claude-Opus-4.5 achieves the highest Skills average (8.82) despite the lowest Content Knowledge"
description: "Practical educational skill does not follow from knowledge scores: Claude-Opus-4.5 achieves the highest Skills average (8.82) despite the lowest Content Knowledge"
id: skills-independent-of-knowledge-scores-llms
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: unggi-lee-2026
    resource: "https://doi.org/10.48550/arxiv.2601.13882"
    title: "Unggi Lee, Sookbun Lee, Heungsoo Choi, Jinseo Lee, Haeun Park, Younghoon Jeon, Sungmin Cho, Minju Kang, Junbo Koh, Jiyeong Bae, Minwoo Nam, Juyeon Eun, Yeonji Jung, Yeil Jeong. (2026). OpenLearnLM Benchmark: A Unified Framework for Evaluating Knowledge, Skill, and Attitude in Educational Large Language Models. https://arxiv.org/abs/2601.13882 [doi:10.48550/arxiv.2601.13882](https://doi.org/10.48550/arxiv.2601.13882)"
    author: Unggi Lee, Sookbun Lee, Heungsoo Choi, Jinseo Lee, Haeun Park, Younghoon Jeon, Sungmin Cho, Minju Kang, Junbo Koh, Jiyeong Bae, Minwoo Nam, Juyeon Eun, Yeonji Jung, Yeil Jeong
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Practical educational skill does not follow from knowledge scores: Claude-Opus-4.5 achieves the highest Skills average (8.82) despite the lowest Content Knowledge

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Claude-Opus-4.5 achieves the highest overall Skills average (8.82 on a 10-point scale) despite having the lowest Content Knowledge among the seven models evaluated. [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Sookbun Lee, Heungsoo Choi, Jinseo Lee, Haeun Park, Younghoon Jeon, Sungmin Cho, Minju Kang, Junbo Koh, Jiyeong Bae, Minwoo Nam, Juyeon Eun, Yeonji Jung, Yeil Jeong. (2026). OpenLearnLM Benchmark: A Unified Framework for Evaluating Knowledge, Skill, and Attitude in Educational Large Language Models. https://arxiv.org/abs/2601.13882 [doi:10.48550/arxiv.2601.13882](https://doi.org/10.48550/arxiv.2601.13882)

`q2 · i?` · `design · r2`

Skills-domain results from evaluating seven frontier LLMs on 6,281 items (171 MCQ and 6,110 long-answer items scored on a 10-point LLM-as-Judge scale). The Skills spread between highest (Claude-Opus-4.5, 8.82) and lowest (GLM-4.7, 8.24) models spans 0.58 points.

> "Claude-Opus-4.5 achieves the highest overall Skills average (8.82) despite having the lowest Content Knowledge, demonstrating that knowing facts and applying them in educational contexts are distinct competencies."

## Discussion


## Related Claims
- [Content knowledge and pedagogical knowledge dissociate in frontier LLMs; Claude-Opus-4.5 shows a 19.8 percentage point gap (66.3% content vs. 86.1% pedagogical)](content-pedagogical-knowledge-dissociation-llms.md) — related
- [Knowledge, Skills, and Attitude scores are largely independent across frontier LLMs, with Knowledge–Skills correlation r=−0.51 and Knowledge–Attitude r=−0.63](ksa-dimensions-weakly-negative-correlated-llms.md) — related
- [Across 17 frontier models, Stage 1 pedagogical-judgment scores are high (mean 0.893) while rank correlations with Stage 2 (ρ=0.24) and Stage 3 (ρ=0.21) are weak, with workflow scores topping out at 0.704](teacharena-stage-rank-reshuffling.md) — a broader claim this one bears on
