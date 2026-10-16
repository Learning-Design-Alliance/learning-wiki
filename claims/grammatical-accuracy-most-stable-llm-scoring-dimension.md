---
type: claim
title: Grammatical Accuracy is the most stable and objective scoring dimension for LLMs, while Task Response is the most challenging
description: Grammatical Accuracy is the most stable and objective scoring dimension for LLMs, while Task Response is the most challenging
id: grammatical-accuracy-most-stable-llm-scoring-dimension
status: review
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

# Grammatical Accuracy is the most stable and objective scoring dimension for LLMs, while Task Response is the most challenging

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Grammatical Accuracy yielded the highest correlations (r = 0.45-0.63) and lowest MAEs (0.67-0.94), which the authors attribute to grammatical features being more rule-based; Task Response correlations ranged from non-significant (Claude, r = 0.22) to strong (Llama, r = 0.61). [→ Tongxi Liu 2026](#tongxi-liu-2026)

## Evidence

### Tongxi Liu 2026

Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565

`q2 · i?` · `associational · r1`

Dimension-level alignment analysis across five LLMs on 60 essays, reported in Results §4.3. The article prints the correlation and MAE ranges for Grammatical Accuracy and separately reports Task Response as the most challenging criterion.

> "Grammatical Accuracy emerged as the most stable dimension, with correlations of r = 0.45-0.63 and lower MAEs (0.67-0.94; Fig. 3)."

## Discussion


## Related Claims
- [The automated scoring system's agreement with human raters varied widely by dimension, with information fidelity showing a weak, non-significant correlation](yunyi-human-agreement-varies-by-dimension.md) — a broader claim this one bears on
- LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst — related
- [Combining the revised rubric with rationale-first evaluation yields the highest human–machine alignment, with dimension-specific gains](combined-rubric-rationale-highest-alignment.md) — related
- [Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration](llama-strongest-human-llm-alignment-claude-weakest.md) — related
