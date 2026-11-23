---
type: claim
title: "DeSCA achieves high agreement with expert human coders on a simulated exhaustive coding task using approximately 1-2% of the dataset as examples"
description: "DeSCA achieves high agreement with expert human coders on a simulated exhaustive coding task using approximately 1-2% of the dataset as examples"
id: desca-high-agreement-exhaustive-coding
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

# DeSCA achieves high agreement with expert human coders on a simulated exhaustive coding task using approximately 1-2% of the dataset as examples

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across ten embedding models and 100 resampled-centroid runs per model, mean Cohen's Kappa against human codes ranged from 0.74 to 0.83 (mean approximately 0.78, SD about 0.03) on 2,489 responses coded L, P, or S. [→ Mjaaland 2025](#mjaaland-2025)

## Evidence

### Mjaaland 2025

Mjaaland, J. T., Kreutzer, M. F., Tyseng, H., Fussell, R. K., Passante, G., Holmes, N. G., Malthe-Sørenssen, A., & Odden, T. O. B. (2025). A Framework for Deductive Semantic Content Analysis at Scale in Science Education Using Text Embeddings. Data available at Zenodo; code shared via GitHub. [doi:10.3233/faia251443](https://doi.org/10.3233/faia251443)

`q2 · i?` · `design · r2`

Computational benchmark of the DeSCA framework on a physics education survey, simulating exhaustive coding by dropping the 410 responses human-coded as Other (leaving 2,489). The article reports "mean Cohen's Kappa score across all runs and models was approximately 0.78" using 28 example responses per run, about 1% of the dataset.

> "The mean Cohen's Kappa score across all runs and models was approximately 0.78, and the standard deviation across the different resampling runs hovers around 0.03, placing this performance within one standard deviation of the commonly-accepted threshold of 0.8 for almost perfect agreement."

## Discussion


## Related Claims
- [DeSCA performs substantially worse on a selective coding task that includes an Other category than on the simulated exhaustive task](desca-lower-agreement-selective-coding.md) — related
- [Fine-tuning the embedding models improves selective coding performance by ten to twenty percent on Kappa and MCC, though performance remains below the exhaustive task](fine-tuning-improves-selective-coding.md) — related
