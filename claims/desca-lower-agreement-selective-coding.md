---
type: claim
title: DeSCA performs substantially worse on a selective coding task that includes an Other category than on the simulated exhaustive task
description: DeSCA performs substantially worse on a selective coding task that includes an Other category than on the simulated exhaustive task
id: desca-lower-agreement-selective-coding
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mjaaland-2025
    resource: "https://doi.org/10.3233/faia251443"
    title: "Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B. (2025). A Framework for Deductive Semantic Content Analysis at Scale in Science Education Using Text Embeddings. Data available at Zenodo; code shared via GitHub. [doi:10.3233/faia251443](https://doi.org/10.3233/faia251443)"
    author: "Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DeSCA performs substantially worse on a selective coding task that includes an Other category than on the simulated exhaustive task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the full 2,899-response dataset with selective coding, Kappa values dropped to 0.38-0.46, interpreted as fair to moderate agreement. [→ Mjaaland 2025](#mjaaland-2025)

## Evidence

### Mjaaland 2025

Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B. (2025). A Framework for Deductive Semantic Content Analysis at Scale in Science Education Using Text Embeddings. Data available at Zenodo; code shared via GitHub. [doi:10.3233/faia251443](https://doi.org/10.3233/faia251443)

`q2 · i?` · `design · r2`

Classification of the entire dataset including responses human-coded as Other, benchmarked against human codes across ten embedding models and 100 runs each. The article reports "Kappa values of 0.38-0.46", far below the exhaustive-task range.

> "As shown, performance was significantly lower on this task than on the simulated exhaustive coding task, with Kappa values of 0.38-0.46, a range that is typically interpreted as fair to moderate agreement"

## Discussion


## Related Claims
- [DeSCA achieves high agreement with expert human coders on a simulated exhaustive coding task using approximately 1-2% of the dataset as examples](desca-high-agreement-exhaustive-coding.md) — related
- [Fine-tuning the embedding models improves selective coding performance by ten to twenty percent on Kappa and MCC, though performance remains below the exhaustive task](fine-tuning-improves-selective-coding.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — related
