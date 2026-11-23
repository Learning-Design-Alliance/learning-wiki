---
type: claim
title: Fine-tuning the embedding models improves selective coding performance by ten to twenty percent on Kappa and MCC, though performance remains below the exhaustive task
description: Fine-tuning the embedding models improves selective coding performance by ten to twenty percent on Kappa and MCC, though performance remains below the exhaustive task
id: fine-tuning-improves-selective-coding
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

# Fine-tuning the embedding models improves selective coding performance by ten to twenty percent on Kappa and MCC, though performance remains below the exhaustive task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After fine-tuning six embedding models on 93 labeled texts, Kappa and MCC improved for all models (e.g., Kappa 0.50-0.53), but remained below exhaustive-task levels. [→ Mjaaland 2025](#mjaaland-2025)

## Evidence

### Mjaaland 2025

Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B. (2025). A Framework for Deductive Semantic Content Analysis at Scale in Science Education Using Text Embeddings. Data available at Zenodo; code shared via GitHub. [doi:10.3233/faia251443](https://doi.org/10.3233/faia251443)

`q2 · i?` · `design · r2`

Re-classification of the full dataset using six fine-tuned embedding models, trained on 93 labeled responses (28 Limitations, 15 Principles, 19 Statistics, 31 Other) drawn from the centroid examples plus 34 responses from a related question. The article reports "a substantial improvement, between ten and twenty percent on both Kappa and MCC scores for all models".

> "Results show a substantial improvement, between ten and twenty percent on both Kappa and MCC scores for all models."

## Discussion


## Related Claims
- [DeSCA achieves high agreement with expert human coders on a simulated exhaustive coding task using approximately 1-2% of the dataset as examples](desca-high-agreement-exhaustive-coding.md) — related
- [DeSCA performs substantially worse on a selective coding task that includes an Other category than on the simulated exhaustive task](desca-lower-agreement-selective-coding.md) — related
