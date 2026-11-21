---
type: claim
title: Correct LLM annotations are marked by higher density of causal connectors in their reasoning, while syntactic complexity (Differentiation) does not distinguish correct from incorrect reasoning
description: Correct LLM annotations are marked by higher density of causal connectors in their reasoning, while syntactic complexity (Differentiation) does not distinguish correct from incorrect reasoning
id: causal-logic-marks-correct-llm-reasoning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ahtisham-2026
    resource: "https://doi.org/10.48550/arXiv.2602.09832"
    title: "Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F. (2026). LLM Reasoning Predicts When Models Are Right: Evidence from Coding Classroom Discourse. [doi:10.48550/arXiv.2602.09832](https://doi.org/10.48550/arXiv.2602.09832)"
    author: Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: ahtisham-2026-2
    resource: "https://doi.org/10.48550/arXiv.2602.09832"
    title: "Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F. (2026). LLM Reasoning Predicts When Models Are Right: Evidence from Coding Classroom Discourse. [doi:10.48550/arXiv.2602.09832](https://doi.org/10.48550/arXiv.2602.09832)"
    author: Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Correct LLM annotations are marked by higher density of causal connectors in their reasoning, while syntactic complexity (Differentiation) does not distinguish correct from incorrect reasoning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Correct responses showed significantly higher density of Causation markers (p = 0.015): 0.18 causal markers per 100 words versus 0.12 for misclassified responses. [→ Ahtisham 2026](#ahtisham-2026)
`q2 i?` Differentiation marker density showed no significant difference between correct and incorrect reasoning (p = 0.212), indicating incorrect reasoning is often just as syntactically complex; equivalence was not tested beyond this comparison. [→ Ahtisham 2026 (2)](#ahtisham-2026-2)

## Evidence

### Ahtisham 2026

Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F. (2026). LLM Reasoning Predicts When Models Are Right: Evidence from Coding Classroom Discourse. [doi:10.48550/arXiv.2602.09832](https://doi.org/10.48550/arXiv.2602.09832)

`q2 · i?` · `associational · r2`

LIWC analysis of reasoning for correct vs. incorrect annotations (Figure 2). Correct responses had significantly higher Causation density (p = 0.015), with "a mean density of 0.18 causal markers per 100 words" versus 0.12, using markers such as therefore, because, implies, yields.

> "Correct rea- soning contained a mean density of 0.18 causal markers per 100 words, compared to only0.12for misclassified responses."

### Ahtisham 2026 (2)

Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F. (2026). LLM Reasoning Predicts When Models Are Right: Evidence from Coding Classroom Discourse. [doi:10.48550/arXiv.2602.09832](https://doi.org/10.48550/arXiv.2602.09832)

`q2 · i?` · `associational · r2`

LIWC Differentiation analysis (contrastives such as but, however, except) comparing correct and incorrect reasoning densities, yielding "a null result (p= 0.212)" with descriptive means of 1.63 vs. 1.74. The null indicates incorrect reasoning is often just as syntactically complex as valid reasoning.

> "The analysis yielded a null result (p= 0.212), with no signif- icant difference in differentiation density between correct (µ= 1.63) and incorrect (µ= 1.74) reasoning."

## Discussion


## Learner Variables
- [Syntax](../learner-variables/syntax.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Causal discovery analysis finds four of five LLMs prioritize lexical features in scoring, while DeepSeek R1 uniquely prioritizes syntactic complexity](llm-causal-feature-dependencies-lexical-versus-syntactic.md) — related
- [Reasoning for correct annotations is significantly shorter than for incorrect ones for most Talk Moves constructs, with Relating to Others the sole significant exception where correct reasoning is longer](concise-reasoning-predicts-correct-annotations.md) — related
