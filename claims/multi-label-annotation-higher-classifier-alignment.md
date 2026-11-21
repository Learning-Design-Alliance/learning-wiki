---
type: claim
title: Multi-label annotation of toxic text yields higher alignment with external ML classifiers than forced single-label consensus, though not always higher inter-annotator agreement
description: Multi-label annotation of toxic text yields higher alignment with external ML classifiers than forced single-label consensus, though not always higher inter-annotator agreement
id: multi-label-annotation-higher-classifier-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: danielle-r-thomas-2025
    resource: "https://doi.org/10.48550/arXiv.2508.00143"
    title: "Danielle R. Thomas, Conrad Borchers, Kenneth R. Koedinger. (2025). Beyond Agreement: Rethinking Ground Truth in Educational AI. [doi:10.48550/arXiv.2508.00143](https://doi.org/10.48550/arXiv.2508.00143)"
    author: Danielle R. Thomas, Conrad Borchers, Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# Multi-label annotation of toxic text yields higher alignment with external ML classifiers than forced single-label consensus, though not always higher inter-annotator agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Re-annotating three toxic text datasets with strict, relaxed, and inferred group labels produced annotations with higher alignment to external classifiers (Detoxify, Perspective API) while not always improving inter-annotator agreement. [→ Danielle R. Thomas 2025](#danielle-r-thomas-2025)

## Evidence

### Danielle R. Thomas 2025

Danielle R. Thomas, Conrad Borchers, Kenneth R. Koedinger. (2025). Beyond Agreement: Rethinking Ground Truth in Educational AI. [doi:10.48550/arXiv.2508.00143](https://doi.org/10.48550/arXiv.2508.00143)

`q2 · i?` · `theoretical · r2`

The paper reports, citing Arhin et al. (2021), a re-annotation of three toxic text datasets using three context-based label types; the review states the multi-label scheme offered "enhanced dataset quality and potential model generalizability". No effect sizes are printed.

> "While the approach did not always improve inter-annotator agreement, it pro- duced annotations with higher alignment to exter- nal machine-learning classifiers (e.g., Detoxify and Perspective API), thus offering enhanced dataset quality and potential model generalizability."

## Discussion


## Related Claims
- [Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus](moderate-kappa-versus-perceived-consensus-gap.md) — related
- [The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain](judge-calibration-labels-strong-severity-uneven.md) — related
- [ML scoring models for scientific argumentation items achieved good to almost perfect agreement with human consensus scores (mean Cohen's kappa = 0.60)](ml-scoring-argumentation-mean-kappa-060.md) — related
- [Adjusting the lo_threshold parameter aligns the model's credit decisions with either lenient or strict human annotators](lo-threshold-tuning-matches-annotator-leniency.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — related
