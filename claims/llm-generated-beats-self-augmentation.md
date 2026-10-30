---
type: claim
title: LLM-generated responses outperform self-augmentation when augmenting small educational classification datasets
description: LLM-generated responses outperform self-augmentation when augmenting small educational classification datasets
id: llm-generated-beats-self-augmentation
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

# LLM-generated responses outperform self-augmentation when augmenting small educational classification datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly
> **Design limits** · Keith Cochran 2025: the intervention came bundled with another change (read from the study by two models, 2026-10-27)

## Subclaims
`q2 i?` Maximum classification performance was achieved with LLM-generated responses rather than self-augmentation (data replication) for all seven concepts, and self-augmented training was less stable at high augmentation levels. [→ Keith Cochran 2025](#keith-cochran-2025)

## Evidence

### Keith Cochran 2025

Keith Cochran, Clayton Cohn, Jean-François Rouet, Peter Hastings. (2025). Comparing Text Augmentation by GPT-3.5 and Llama3 for Evaluating Student Responses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00473-x

`q2 · i?` · `causal · r2`

Head-to-head comparison of six augmentation methods (self plus five LLM/temperature combinations) across four BERT-based classifiers on French and English student-response datasets, measured by micro-F1 averaged over ten seeds. Generated texts were "longer and more complicated" than copies.

> "This hypothesis was supported by our results which showed that maximum performance was achieved using generated responses for all seven concepts. LLM-generated responses outperformed self-augmentation because the generated texts were longer and more complicated."

## Discussion


## Related Claims
- [Fine-tuning BERT-based classifiers on LLM-augmented student-response data outperforms unaugmented training for all tested concepts](llm-augmentation-beats-unaugmented-small-education-data.md) — related
- [Augmentation levels below 20x produce unreliable classification performance in small educational datasets](low-augmentation-levels-unreliable.md) — related
- [Higher LLM temperature settings yield the best English augmentation performance, with Llama temperature 2 the top generator overall](temperature-affects-augmentation-performance.md) — related
- [Datasets with entropy below 0.5 are difficult to augment enough to beat majority-label guessing](low-entropy-datasets-resist-augmentation.md) — related
