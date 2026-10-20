---
type: claim
title: High agreement between two LLM screeners indicates consistency among outputs, not accuracy, because models may exhibit correlated failure patterns
description: High agreement between two LLM screeners indicates consistency among outputs, not accuracy, because models may exhibit correlated failure patterns
id: llm-agreement-is-consistency-not-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: eicher-2026
    resource: "https://doi.org/10.48550/arxiv.2609.27939"
    title: "Eicher, J., & da Silva, R. (2026). From Sentiment Classification to Actionable and Responsible Feedback: A Scoping Review and Evidence Map of NLP in Student Evaluation of Teaching, 2015–2026. arXiv. https://arxiv.org/abs/2609.27939 [doi:10.48550/arxiv.2609.27939](https://doi.org/10.48550/arxiv.2609.27939)"
    author: "Eicher, J., & da Silva, R."
    q: 1
    i: "?"
    kind: review
    rigour: 3
---

# High agreement between two LLM screeners indicates consistency among outputs, not accuracy, because models may exhibit correlated failure patterns

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r3` · `q1`

## Subclaims
`q1 i?` Agreement between LLMs should be interpreted primarily as consistency among outputs, not as an independent measure of accuracy, since models may exhibit correlated failure patterns. [→ Eicher 2026](#eicher-2026)

## Evidence

### Eicher 2026

Eicher, J., & da Silva, R. (2026). From Sentiment Classification to Actionable and Responsible Feedback: A Scoping Review and Evidence Map of NLP in Student Evaluation of Teaching, 2015–2026. arXiv. https://arxiv.org/abs/2609.27939 [doi:10.48550/arxiv.2609.27939](https://doi.org/10.48550/arxiv.2609.27939)

`q1 · i?` · `review · r3`

Methodological argument in the review's screening section, citing validation literature on LLM-assisted screening. The review argues two LLMs should not be treated as statistically independent sources of evidence of correctness.

> "Models may exhibit correlated failure patterns. High agreement between LLMs can coexist with substantially lower agreement relative to external human judgments"

## Discussion


## Related Claims
- Among 421 SET-NLP studies, 61.3% demonstrate output or stronger (A2+) but only 11.6% evaluate outputs with intended users or stronger (A3+), a 49.7 percentage-point drop — related
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](llm-as-judge-human-level-agreement-with-validation.md) — a broader claim this one bears on
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
