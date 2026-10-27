---
type: claim
title: Augmentation levels below 20x produce unreliable classification performance in small educational datasets
description: Augmentation levels below 20x produce unreliable classification performance in small educational datasets
id: low-augmentation-levels-unreliable
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
---

# Augmentation levels below 20x produce unreliable classification performance in small educational datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Classification performance was generally unreliable at augmentation levels below 20x for both the French and English datasets across the four BERT models. [→ Keith Cochran 2025](#keith-cochran-2025)

## Evidence

### Keith Cochran 2025

Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x

`q2 · i?` · `causal · r2`

Performance curves across augmentation levels 0x–100x (Fig. 2 for French; Figs. 3–6 for English rainwater concepts) showed that "augmentation levels below 20x resulted in unreliable classifications in the majority of cases".

> "At levels of augmentation less than 20x, classification performance with all of the BERT models was generally unreliable."

## Discussion


## Related Claims
- [LLM-generated responses outperform self-augmentation when augmenting small educational classification datasets](llm-generated-beats-self-augmentation.md) — related
- [Fine-tuning BERT-based classifiers on LLM-augmented student-response data outperforms unaugmented training for all tested concepts](llm-augmentation-beats-unaugmented-small-education-data.md) — related
- [Datasets with entropy below 0.5 are difficult to augment enough to beat majority-label guessing](low-entropy-datasets-resist-augmentation.md) — related
- [Self- and GPT-augmented performance peaks and degrades after 55x–89x augmentation, while Llama-augmented performance keeps rising toward 100x](performance-peak-augmentation-llama-rises.md) — related
