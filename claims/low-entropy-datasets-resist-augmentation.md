---
type: claim
title: Datasets with entropy below 0.5 are difficult to augment enough to beat majority-label guessing
description: Datasets with entropy below 0.5 are difficult to augment enough to beat majority-label guessing
id: low-entropy-datasets-resist-augmentation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: keith-cochran-2025
    resource: "https://doi.org/10.1007/s40593-025-00473-x"
    title: "Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x"
    author: Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Datasets with entropy below 0.5 are difficult to augment enough to beat majority-label guessing

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Only one classifier/augmentation combination outperformed blind majority-label guessing on concept C1 (89% majority, entropy 0.485), and the authors conclude datasets with entropy below 0.5 are hard to augment sufficiently. [→ Keith Cochran 2025](#keith-cochran-2025)

## Evidence

### Keith Cochran 2025

Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x

`q2 · i?` · `causal · r2`

Analysis of the severely imbalanced C1 concept (89% majority label, entropy 0.485), where the a priori majority baseline beat augmented classifiers in three of four models. Datasets with "entropy of less than 0.5" resisted augmentation.

> "We concluded from our experimentation that data sets with an entropy of less than 0.5 were challenging to augment sufficiently (i.e., with enough generated data) to create a classifier that would outperform simply guessing the majority label."

## Discussion


## Related Claims
- [LLM-generated responses outperform self-augmentation when augmenting small educational classification datasets](llm-generated-beats-self-augmentation.md) — related
- [Fine-tuning BERT-based classifiers on LLM-augmented student-response data outperforms unaugmented training for all tested concepts](llm-augmentation-beats-unaugmented-small-education-data.md) — related
- [Augmentation levels below 20x produce unreliable classification performance in small educational datasets](low-augmentation-levels-unreliable.md) — related
