---
type: claim
title: Multiagent framework demonstrated stable cross-specialty scalability with lower variability than single-LLM baseline
description: Multiagent framework demonstrated stable cross-specialty scalability with lower variability than single-LLM baseline
id: multiagent-stable-cross-specialty-scalability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: qu-yufei-2026
    resource: "https://doi.org/10.2196/84747"
    title: "Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong. (2026). A Large Language Model–Powered Multiagent Framework Emulating Standardized Patients in Clinical Communication Skills Training: Development and Evaluation Study. Journal of Medical Internet Research. https://doi.org/10.2196/84747"
    author: Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: qu-yufei-2026-2
    resource: "https://doi.org/10.2196/84747"
    title: "Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong. (2026). A Large Language Model–Powered Multiagent Framework Emulating Standardized Patients in Clinical Communication Skills Training: Development and Evaluation Study. Journal of Medical Internet Research. https://doi.org/10.2196/84747"
    author: Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multiagent framework demonstrated stable cross-specialty scalability with lower variability than single-LLM baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The multiagent framework maintained factual consistency scores within 0.7 to 0.85 across 4 of 5 departments except pediatrics, and showed lower coefficient of variation than the single-LLM baseline, indicating improved stability. [→ Qu Yufei 2026](#qu-yufei-2026)

## Evidence

### Qu Yufei 2026

Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong. (2026). A Large Language Model–Powered Multiagent Framework Emulating Standardized Patients in Clinical Communication Skills Training: Development and Evaluation Study. Journal of Medical Internet Research. https://doi.org/10.2196/84747

`q2 · i?` · `design · r2`

Scalability was preliminarily evaluated using LLM-as-judge assessments of factual consistency and role-playing across case reports from 5 clinical departments. The method showed "stable fluctuations within a high-scoring interval (0.7‐0.85)" across 4 departments, with pediatrics notably lower.

> "The other 4 departments exhibited similar scoring ranges, with our method demonstrating stable fluctuations within a high-scoring interval (0.7‐0.85), suggesting good generalizability and broad applicability across diverse case reports"

### Qu Yufei 2026 (2)

Qu Yufei, Xu Xiaowei, Long Yunzi, Wang Yijie, Li Jiao, Lu Xudong. (2026). A Large Language Model–Powered Multiagent Framework Emulating Standardized Patients in Clinical Communication Skills Training: Development and Evaluation Study. Journal of Medical Internet Research. https://doi.org/10.2196/84747

`q2 · i?` · `design · r2`

Coefficient of variation analysis compared stability across departments. The "GPT-4o–based framework (CV=4.7%) exhibited the highest stability", while the "single-LLM Qwen3-32B framework (CV=8.7%) showed slightly greater variability" than the multiagent frameworks (Qwen3-32B–based CV=7.1%, DeepSeek-V3–based CV=5.7%).

> "Analysis of the CV revealed that the GPT-4o–based framework (CV=4.7%) exhibited the highest stability, while single-LLM Qwen3-32B framework (CV=8.7%) showed slightly greater variability"

## Discussion


## Related Claims
- [All methods achieved accuracy rates exceeding 94 percent on dental case dialogues](all-methods-accuracy-exceeding-94-percent.md) — related
- [DeepSeek-V3 and Qwen3-32B multiagent frameworks received full perceived educational utility scores from physicians](full-perceived-educational-utility-scores.md) — related
- [GPT-4o–based multiagent framework achieved the highest factual consistency score of 0.769](gpt4o-highest-factual-consistency-0-769.md) — related
- [Multiagent framework showed limited discriminative power against leading questions in low-quality inquiry analysis](limited-discriminative-power-leading-questions.md) — related
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — a broader claim this one bears on
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](llm-ebhs-inter-run-reliability-high-kappa-0821.md) — related
- [Qwen3-32B–based framework achieved the highest role-playing competency score of 39.67](qwen3-32b-highest-role-playing-score-39-67.md) — related
