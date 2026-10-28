---
type: claim
title: LLM temperature settings significantly affect generated-text length and complexity, with Llama3 producing more complex texts than GPT-3.5
description: LLM temperature settings significantly affect generated-text length and complexity, with Llama3 producing more complex texts than GPT-3.5
id: temperature-drives-generated-text-complexity
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
    rigour: 1
  - id: keith-cochran-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00473-x"
    title: "Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x"
    author: Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM temperature settings significantly affect generated-text length and complexity, with Llama3 producing more complex texts than GPT-3.5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Higher temperature settings produced longer, more complex generated sentences, with Llama temperature 2 texts averaging 44.4 words versus 25.7 for GPT temperature 0.1. [→ Keith Cochran 2025](#keith-cochran-2025)
`q2 i?` One-sided t-tests on Gunning fog readability confirmed higher-temperature generators produced significantly more readable-complex texts for the French question. [→ Keith Cochran 2025 (2)](#keith-cochran-2025-2)

## Evidence

### Keith Cochran 2025

Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x

`q2 · i?` · `causal · r1`

Numerical comparison of average word counts per generator/temperature (Fig. 1): 44.4 words for Llama temperature 2 versus 25.7 for GPT temperature 0.1, against a 15.8-word average student response. Temperature "had a significant effect" on length and complexity.

> "The different temperature settings for the models had a significant effect on the length and complexity of the generated sentences."

### Keith Cochran 2025 (2)

Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x

`q2 · i?` · `causal · r1`

Two-sample one-sided t-tests on 1000 randomly sampled texts per generator/temperature for the French question, comparing Gunning fog readability. Differences were "highly significant ( p < .0001)" except GPT 0.9 vs GPT 0.5 (p < .05).

> "All the differences were highly significant ( p < .0001) with the exception that texts from GPT 3.5 with a temperature of 0.9 had a mean readability of 13.9 ( SD = 3.8)"

## Discussion


## Related Claims

- [Higher LLM temperature settings yield the best English augmentation performance, with Llama temperature 2 the top generator overall](temperature-affects-augmentation-performance.md) — related
- [The three fine-tuned LLMs differ significantly in response length, readability, and similarity to posts](llm-response-length-readability-differences.md) — related
- [Prompt-based personalization of an LLM/RAG teaching assistant produces measurable variation in response expression, length, and complexity across personalization conditions](prompt-personalization-measurable-response-variation.md) — related
- [Hyperparameter setting with maximum token 53 and temperature 1 (Set C) yields the most accurate AGE grading performance](age-hyperparameter-set-c-most-accurate.md)
