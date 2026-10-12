---
type: claim
title: Causal discovery analysis finds four of five LLMs prioritize lexical features in scoring, while DeepSeek R1 uniquely prioritizes syntactic complexity
description: Causal discovery analysis finds four of five LLMs prioritize lexical features in scoring, while DeepSeek R1 uniquely prioritizes syntactic complexity
id: llm-causal-feature-dependencies-lexical-versus-syntactic
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
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

# Causal discovery analysis finds four of five LLMs prioritize lexical features in scoring, while DeepSeek R1 uniquely prioritizes syntactic complexity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Llama, GPT-4.1, Gemini, and Claude ranked lexical features first in cumulative effect size (0.366-1.194), whereas DeepSeek R1 prioritized syntactic complexity as its most influential domain (0.978). [→ Tongxi Liu 2026](#tongxi-liu-2026)

## Evidence

### Tongxi Liu 2026

Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565

`q2 · i?` · `associational · r1`

Hybrid causal discovery analysis of 17 linguistic features across seven domains for each LLM's scores, reported in Results §4.4 and Tables 4-5 with bootstrap validation (n = 1,000 resamples). The article prints the cumulative lexical effect sizes and DeepSeek's divergent syntactic dominance (0.978).

> "Four of the five systems—Llama, GPT-4.1, Gemini, and Claude—showed a pronounced emphasis on lexical features, which consistently ranked first in cumulative effect size (0.366-1.194)."

## Discussion


## Related Claims
- [GPT-4.1 and Llama 4 Maverick achieve ICC reliability above 0.90 across all IELTS dimensions, while Gemini 2.5 Flash is moderate and Claude Sonnet 4 and DeepSeek R1 fall below 0.70 in most dimensions](llm-essay-scoring-reliability-stratification.md) — related
- [LLM grading patterns cluster into six groups aligned with vendor families, with highest correlations within same-vendor model families](llm-grading-vendor-specific-six-clusters.md) — related
