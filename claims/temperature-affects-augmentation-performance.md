---
type: claim
title: Higher LLM temperature settings yield the best English augmentation performance, with Llama temperature 2 the top generator overall
description: Higher LLM temperature settings yield the best English augmentation performance, with Llama temperature 2 the top generator overall
id: temperature-affects-augmentation-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: keith-cochran-2025
    resource: "https://doi.org/10.1007/s40593-025-00473-x"
    title: "Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x"
    author: Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: keith-cochran-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00473-x"
    title: "Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x"
    author: Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Higher LLM temperature settings yield the best English augmentation performance, with Llama temperature 2 the top generator overall

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Llama with temperature = 2 was the top performer among the five generator/temperature combinations for the English rainwater concepts. [→ Keith Cochran 2025](#keith-cochran-2025)
`q2 i?` For the multi-class French dataset, a lower Llama temperature of 1.5 produced the highest classifier performance. [→ Keith Cochran 2025 (2)](#keith-cochran-2025-2)

## Evidence

### Keith Cochran 2025

Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x

`q2 · i?` · `causal · r2`

Comparison of maximum micro-F1 per augmentation level across generator/temperature combinations for the English rainwater concepts, reported in Tables 9–13. Llama temperature 2 "was the top performer".

> "Examining the maximum performance at each augmentation level revealed that Llama with temperature = 2 was the top performer among the five generator / temperature combinations used for student response generation."

### Keith Cochran 2025 (2)

Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x

`q2 · i?` · `causal · r2`

Result for the four-label French opinion dataset, where the best configuration (Classla model, 89x, temperature 1.5) reached micro-F1 0.939 in Table 13. The authors state the diversity hypothesis was "only partially supported".

> "However, the lower temperature = 1.5 for Llama produced the highest classifier performance for the French video games data set. For this reason, this hypothesis was only partially supported."

## Discussion


## Related Claims

- [LLM-generated responses outperform self-augmentation when augmenting small educational classification datasets](llm-generated-beats-self-augmentation.md) — related
- [LLM temperature settings significantly affect generated-text length and complexity, with Llama3 producing more complex texts than GPT-3.5](temperature-drives-generated-text-complexity.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — related
- [Hyperparameter setting with maximum token 53 and temperature 1 (Set C) yields the most accurate AGE grading performance](age-hyperparameter-set-c-most-accurate.md)
