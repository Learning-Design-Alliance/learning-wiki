---
type: claim
title: "Autoencoder preprocessing raises InceptionV3 emotion-recognition accuracy for ASD children's facial images from 71.0% to 83.8%, a 12.8 percentage-point improvement with a very large effect size"
description: "Autoencoder preprocessing raises InceptionV3 emotion-recognition accuracy for ASD children's facial images from 71.0% to 83.8%, a 12.8 percentage-point improvement with a very large effect size"
id: autoencoder-preprocessing-inceptionv3-accuracy-gain-asd
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
    i: 3
    kind: causal
    rigour: 1
---

# Autoencoder preprocessing raises InceptionV3 emotion-recognition accuracy for ASD children's facial images from 71.0% to 83.8%, a 12.8 percentage-point improvement with a very large effect size

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` InceptionV3 with autoencoder preprocessing reached 83.8% accuracy versus a 71.0% baseline, a 12.8 percentage-point improvement with Cohen's d = 2.56. [→ Nelaka K.A.R 2025](#nelaka-kar-2025)

## Evidence

### Nelaka K.A.R 2025

Nelaka K.A.R, Peiris M.K.V, Liyanage R.P.B. (2025). Deep Learning Based Approach to Enhanced Recognition of Emotions and Behavioral Patterns of Autistic Children. arXiv preprint. [doi:10.1109/icac69156.2025.11361475](https://doi.org/10.1109/icac69156.2025.11361475)

`q2 · i3` · `causal · r1`

Computational experiment on the ASD children's facial-expression dataset comparing direct resizing with autoencoder preprocessing. InceptionV3 improved from 71.0% to 83.8% accuracy; Table II reports Cohen's d = 2.56, p < 0.001, CI [10.1%, 15.5%].

> "Similarly, InceptionV3 demonstrated significant enhancement, reaching 83.8% accuracy compared to the baseline performance of 71.0%, corresponding to a 12.8 percentage point improvement."

## Discussion


## Related Claims
- [The accuracy benefit of autoencoder preprocessing is consistent across Xception and InceptionV3, with a coefficient of variation of 2.7%, suggesting architecture-independent gains](autoencoder-benefit-architecture-independent-consistency.md) — related
- [Autoencoder preprocessing is computationally efficient for ASD emotion recognition, with a 10–20% overhead yielding an 18% accuracy improvement (a 9:1 efficiency ratio)](autoencoder-preprocessing-computational-efficiency-ratio.md) — related
- [Autoencoder preprocessing cuts classification error rates for ASD emotion recognition by 48.0% for Xception and 44.1% for InceptionV3](autoencoder-preprocessing-error-rate-reduction-asd.md) — possibly the same claim (merge candidate)
- [Autoencoder preprocessing raises Xception emotion-recognition accuracy for ASD children's facial images from 72.3% to 85.6%, a 13.3 percentage-point improvement with a very large effect size](autoencoder-preprocessing-xception-accuracy-gain-asd.md) — related
