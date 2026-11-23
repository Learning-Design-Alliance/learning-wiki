---
type: claim
title: "Semantic alignment between the reference and the student's work is the most important feature for correct error localization"
description: "Semantic alignment between the reference and the student's work is the most important feature for correct error localization"
id: semantic-recall-most-important-error-localization-feature
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: kv-aditya-srivatsa-2025
    resource: "https://doi.org/10.18653/v1/2025.emnlp-main.553"
    title: "KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)"
    author: KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Semantic alignment between the reference and the student's work is the most important feature for correct error localization

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a Random Forest feature-importance analysis, Semantic Recall ranks highest (17.9%), ahead of error position (13.1%) and error type (7.2%). [→ KV Aditya Srivatsa 2025](#kv-aditya-srivatsa-2025)

## Evidence

### KV Aditya Srivatsa 2025

KV Aditya Srivatsa, Kaushal Kumar Maurya, Ekaterina Kochmar. (2025). LLMs cannot spot math errors, even when allowed to peek into the solution. [doi:10.18653/v1/2025.emnlp-main.553](https://doi.org/10.18653/v1/2025.emnlp-main.553)

`q2 · i?` · `design · r2`

Random Forest classifier trained to predict correct localization, chosen over a Linear Regressor by F1 (0.996 vs 0.572); Figure 3 shows "Semantic Recall is the most important (17.9%)" feature.

> "Semantic Recall is the most important (17.9%), highlighting the role of alignment in successful error localization. The relative position of the error (Rel. Error Step Loc. , 13.1%) and error type ( Error Type , 7.2%) also rank highly."

## Discussion


## Related Claims
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — reports the opposite
- [SHAP analysis identifies Hapax Ratio as the most influential stylometric feature in Random Forest predictions, followed by NSR, Noun Ratio, Adverb Ratio, and TTR](shap-hapax-ratio-most-influential-feature.md) — related
