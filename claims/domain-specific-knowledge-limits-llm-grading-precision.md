---
type: claim
title: Domain-specific knowledge, rather than model complexity or general abilities, limits the precision of LLM criterion-based grading
description: Domain-specific knowledge, rather than model complexity or general abilities, limits the precision of LLM criterion-based grading
id: domain-specific-knowledge-limits-llm-grading-precision
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: da-wei-zhang-2024
    resource: "https://doi.org/10.1038/s41539-024-00291-1"
    title: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1"
    author: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia"
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# Domain-specific knowledge, rather than model complexity or general abilities, limits the precision of LLM criterion-based grading

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The authors argue the most accurate grading came from the prompt with the most domain-specific knowledge, while more advanced models did not improve grading, suggesting domain-specific knowledge is the limiting factor. [→ Da-Wei Zhang 2024](#da-wei-zhang-2024)

## Evidence

### Da-Wei Zhang 2024

Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1

`q1 · i?` · `causal · r1`

Authors' interpretation in the discussion, not a directly tested hypothesis: the most accurate grading came from the prompt embedding detailed marking criteria, and advanced models (ChatGPT 4.0, Claude 3.0) with "more superior domain-general knowledge and general abilities" did not improve grading. The authors explicitly label this a speculation.

> "We speculate that the suboptimal agreement may result from a lack of domain-speciﬁc knowledge rather than the models’ complexity or general knowledge /abilities."

## Discussion


## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [More advanced LLMs (ChatGPT 4.0, Claude 3.0 Haiku) did not improve criterion-based grading over ChatGPT 3.5 with the same prompt](advanced-llms-no-grading-improvement.md) — a narrower finding that bears on this claim
- [More complex prompts tend to elicit superior results with advanced LLM versions (authors' observation)](complex-prompts-elicit-better-llm-results.md) — reports the opposite
- [Switching from reference-based to contextual evaluation prompts improved GenAI grading accuracy](contextual-evaluation-prompt-improvement.md) — related
