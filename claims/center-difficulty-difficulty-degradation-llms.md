---
type: claim
title: Across frontier LLMs, Counseling is the easiest educational activity center (average 8.78) while Assessment and Research are hardest (8.42), and performance degrades from Easy to Hard difficulty
description: Across frontier LLMs, Counseling is the easiest educational activity center (average 8.78) while Assessment and Research are hardest (8.42), and performance degrades from Easy to Hard difficulty
id: center-difficulty-difficulty-degradation-llms
status: review
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
  - id: unggi-lee-2026-2
    resource: "https://arxiv.org/abs/2601.13882"
    title: "Unggi Lee, Sookbun Lee, Heungsoo Choi, Jinseo Lee, Haeun Park, Younghoon Jeon, Sungmin Cho, Minju Kang, Junbo Koh, Jiyeong Bae, Minwoo Nam, Juyeon Eun, Yeonji Jung, Yeil Jeong. (2026). OpenLearnLM Benchmark: A Unified Framework for Evaluating Knowledge, Skill, and Attitude in Educational Large Language Models. https://arxiv.org/abs/2601.13882"
    author: Unggi Lee, Sookbun Lee, Heungsoo Choi, Jinseo Lee, Haeun Park, Younghoon Jeon, Sungmin Cho, Minju Kang, Junbo Koh, Jiyeong Bae, Minwoo Nam, Juyeon Eun, Yeonji Jung, Yeil Jeong
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Across frontier LLMs, Counseling is the easiest educational activity center (average 8.78) while Assessment and Research are hardest (8.42), and performance degrades from Easy to Hard difficulty

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Counseling consistently receives the highest scores across all models (average 8.78), while Assessment (8.42) and Research (8.42) present the greatest challenges. [→ Unggi Lee 2026](#unggi-lee-2026)
`q2 i?` Performance degrades from Easy through Medium to Hard difficulty across all centers, with the Research center showing the largest difficulty gap and Counseling the smallest. [→ Unggi Lee 2026 (2)](#unggi-lee-2026-2)

## Evidence

### Unggi Lee 2026

Unggi Lee, Sookbun Lee, Heungsoo Choi, Jinseo Lee, Haeun Park, Younghoon Jeon, Sungmin Cho, Minju Kang, Junbo Koh, Jiyeong Bae, Minwoo Nam, Juyeon Eun, Yeonji Jung, Yeil Jeong. (2026). OpenLearnLM Benchmark: A Unified Framework for Evaluating Knowledge, Skill, and Attitude in Educational Large Language Models. https://arxiv.org/abs/2601.13882 [doi:10.48550/arxiv.2601.13882](https://doi.org/10.48550/arxiv.2601.13882)

`q2 · i?` · `design · r2`

Skills performance broken down by six educational activity centers (Figure 5a) across the seven-model evaluation. GPT-5.2 achieves the highest single-center score in Counseling (9.07); Claude-Opus-4.5 leads in four of six centers.

> "Coun- seling consistently receives the highest scores across all mod- els (average 8.78), while Assessment (8.42) and Research (8.42) present the greatest challenges, indicating that current LLMs struggle most with tasks requiring systematic judg- ment and multi-step analytical reasoning."

### Unggi Lee 2026 (2)

Unggi Lee, Sookbun Lee, Heungsoo Choi, Jinseo Lee, Haeun Park, Younghoon Jeon, Sungmin Cho, Minju Kang, Junbo Koh, Jiyeong Bae, Minwoo Nam, Juyeon Eun, Yeonji Jung, Yeil Jeong. (2026). OpenLearnLM Benchmark: A Unified Framework for Evaluating Knowledge, Skill, and Attitude in Educational Large Language Models. https://arxiv.org/abs/2601.13882

`q2 · i?` · `design · r2`

Difficulty-based analysis of Skills scores averaged across models (Figure 6a), with difficulty defined by Bloom's cognitive and Krathwohl's affective taxonomies. The article states current models struggle most with higher-order thinking tasks requiring evaluation and creation.

> "Analysis by Bloom’s Taxonomy difficulty levels (Figure 6a) reveals expected performance degradation from Easy (Re- membering/Understanding) through Medium (Applying/An- alyzing) to Hard (Evaluating/Creating) tasks."

## Discussion


## Related Claims
- [Theoretical quality of both theory-based and non-theory agents remains stable across Easy, Medium, and Hard scenario difficulty levels](theoretical-quality-stable-across-difficulty.md) — related
- [LLM difficulty labels track structural question features: stem length, option length, and digits in stems rise monotonically across Easy, Medium, and Hard labels](llm-difficulty-labels-track-structural-item-features.md) — related
- [Success rates decrease monotonically from easy to medium to hard difficulty levels across all models](monotonic-difficulty-decline-turtleai.md) — related
- [Model performance varies by task category, with Basic Geometry easiest and Spiral consistently the most challenging category](spiral-hardest-basic-geometry-easiest-categories.md) — related
