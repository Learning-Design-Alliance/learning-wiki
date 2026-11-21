---
type: claim
title: "Autoencoder preprocessing cuts classification error rates for ASD emotion recognition by 48.0% for Xception and 44.1% for InceptionV3"
description: "Autoencoder preprocessing cuts classification error rates for ASD emotion recognition by 48.0% for Xception and 44.1% for InceptionV3"
id: autoencoder-preprocessing-error-rate-reduction-asd
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: nelaka-kar-2025
    resource: "https://doi.org/10.1109/icac69156.2025.11361475"
    title: "Nelaka K.A.R, Peiris M.K.V, Liyanage R.P.B. (2025). Deep Learning Based Approach to Enhanced Recognition of Emotions and Behavioral Patterns of Autistic Children. arXiv preprint. [doi:10.1109/icac69156.2025.11361475](https://doi.org/10.1109/icac69156.2025.11361475)"
    author: Nelaka K.A.R, Peiris M.K.V, Liyanage R.P.B.
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Autoencoder preprocessing cuts classification error rates for ASD emotion recognition by 48.0% for Xception and 44.1% for InceptionV3

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Xception's error rate fell from 27.7% to 14.4% (a 48.0% reduction) and InceptionV3's from 29.0% to 16.2% (a 44.1% reduction) with autoencoder preprocessing. [→ Nelaka K.A.R 2025](#nelaka-kar-2025)

## Evidence

### Nelaka K.A.R 2025

Nelaka K.A.R, Peiris M.K.V, Liyanage R.P.B. (2025). Deep Learning Based Approach to Enhanced Recognition of Emotions and Behavioral Patterns of Autistic Children. arXiv preprint. [doi:10.1109/icac69156.2025.11361475](https://doi.org/10.1109/icac69156.2025.11361475)

`q2 · i?` · `causal · r1`

Error-rate analysis in the Results section of the computational experiment comparing baseline and autoencoder-enhanced pipelines; the article prints the error reductions as descriptive percentages with no effect size for this measure.

> "The Xception model achieved a 48.0% reduction in error rate (from 27.7% to 14.4%), while InceptionV3 demonstrated a 44.1% reduction (from 29.0% to 16.2%)."

## Discussion


## Related Claims
- [The accuracy benefit of autoencoder preprocessing is consistent across Xception and InceptionV3, with a coefficient of variation of 2.7%, suggesting architecture-independent gains](autoencoder-benefit-architecture-independent-consistency.md) — related
- [Autoencoder preprocessing is computationally efficient for ASD emotion recognition, with a 10–20% overhead yielding an 18% accuracy improvement (a 9:1 efficiency ratio)](autoencoder-preprocessing-computational-efficiency-ratio.md) — related
- [Autoencoder preprocessing raises Xception emotion-recognition accuracy for ASD children's facial images from 72.3% to 85.6%, a 13.3 percentage-point improvement with a very large effect size](autoencoder-preprocessing-xception-accuracy-gain-asd.md) — possibly the same claim (merge candidate)
- [Autoencoder preprocessing raises InceptionV3 emotion-recognition accuracy for ASD children's facial images from 71.0% to 83.8%, a 12.8 percentage-point improvement with a very large effect size](autoencoder-preprocessing-inceptionv3-accuracy-gain-asd.md) — possibly the same claim (merge candidate)
