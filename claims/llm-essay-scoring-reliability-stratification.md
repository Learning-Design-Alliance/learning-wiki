---
type: claim
title: "In one study of repeated LLM scoring of 60 IELTS essays, Gemini 2.5 Flash was moderately reliable (ICC 0.63-0.75) while Claude Sonnet 4 and DeepSeek R1 stayed below 0.70 in most dimensions"
description: In one study of repeated LLM scoring of 60 IELTS essays, Gemini 2.5 Flash was moderately reliable (ICC 0.63-0.75) while Claude Sonnet 4 and DeepSeek R1 stayed below 0.70 in most dimensions
id: llm-essay-scoring-reliability-stratification
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: tongxi-liu-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100565"
    title: "Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565"
    author: Tongxi Liu, Luyao Ye, Wei Yan
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# In one study of repeated LLM scoring of 60 IELTS essays, Gemini 2.5 Flash was moderately reliable (ICC 0.63-0.75) while Claude Sonnet 4 and DeepSeek R1 stayed below 0.70 in most dimensions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

<!-- title before 2026-10-15: GPT-4.1 and Llama 4 Maverick achieve ICC reliability above 0.90 across all IELTS dimensions, while Gemini 2.5 Flash is moderate and Claude Sonnet 4 and DeepSeek R1 fall below 0.70 in most dimensions -->

## Subclaims
`q2 i?` Reliability stratified by model: Gemini 2.5 Flash reached ICC = 0.63-0.75 with slightly compressed scoring ranges, while Claude Sonnet 4 and DeepSeek R1 remained below 0.70 in most dimensions. [→ Tongxi Liu 2026](#tongxi-liu-2026)

## Evidence

### Tongxi Liu 2026

Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565

`q2 · i?` · `associational · r1`

Reliability analysis (ICC(3,1)) of three repeated scoring runs per model on 60 essays, reported in Results §4.2 and Table 3. The article prints the ICC ranges and characterizes the lower-reliability models as showing "reduced reproducibility".

> "Gemini 2.5 Flash achieved moderate reliability (ICC = 0.63-0.75), reflecting stable yet slightly compressed scoring ranges, while Claude Sonnet 4 and DeepSeek R1 remained below 0.70 in most dimensions, indicating reduced reproducibility."

## Discussion


## Related Claims
- [Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration](llama-strongest-human-llm-alignment-claude-weakest.md) — related
- [Causal discovery analysis finds four of five LLMs prioritize lexical features in scoring, while DeepSeek R1 uniquely prioritizes syntactic complexity](llm-causal-feature-dependencies-lexical-versus-syntactic.md) — related
