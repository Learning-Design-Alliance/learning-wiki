---
type: claim
title: "Autoencoder preprocessing raises Xception emotion-recognition accuracy for ASD children's facial images from 72.3% to 85.6%, a 13.3 percentage-point improvement with a very large effect size"
description: "Autoencoder preprocessing raises Xception emotion-recognition accuracy for ASD children's facial images from 72.3% to 85.6%, a 13.3 percentage-point improvement with a very large effect size"
id: autoencoder-preprocessing-xception-accuracy-gain-asd
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
  - id: nelaka-kar-2025-2
    resource: "https://doi.org/10.1109/icac69156.2025.11361475"
    title: "Nelaka K.A.R, Peiris M.K.V, Liyanage R.P.B. (2025). Deep Learning Based Approach to Enhanced Recognition of Emotions and Behavioral Patterns of Autistic Children. arXiv preprint. [doi:10.1109/icac69156.2025.11361475](https://doi.org/10.1109/icac69156.2025.11361475)"
    author: Nelaka K.A.R, Peiris M.K.V, Liyanage R.P.B.
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Autoencoder preprocessing raises Xception emotion-recognition accuracy for ASD children's facial images from 72.3% to 85.6%, a 13.3 percentage-point improvement with a very large effect size

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Xception with autoencoder preprocessing achieved 85.6% accuracy versus a 72.3% direct-resizing baseline, a 13.3 percentage-point improvement with Cohen's d = 2.66. [→ Nelaka K.A.R 2025](#nelaka-kar-2025)
`q2 i?` McNemar's test on paired baseline-versus-enhanced predictions confirmed statistical significance (χ2 = 98.01, p < 0.001). [→ Nelaka K.A.R 2025 (2)](#nelaka-kar-2025-2)

## Evidence

### Nelaka K.A.R 2025

Nelaka K.A.R, Peiris M.K.V, Liyanage R.P.B. (2025). Deep Learning Based Approach to Enhanced Recognition of Emotions and Behavioral Patterns of Autistic Children. arXiv preprint. [doi:10.1109/icac69156.2025.11361475](https://doi.org/10.1109/icac69156.2025.11361475)

`q2 · i3` · `causal · r1`

Computational experiment comparing baseline direct resizing against autoencoder preprocessing on an ASD children's facial-expression dataset. Xception reached "85.6% accuracy after autoencoder preprocessing" versus 72.3% baseline; Table II reports Cohen's d = 2.66, p < 0.001, CI [10.6%, 16.0%].

> "The Xception model achieved the highest overall performance with 85.6% accuracy after autoencoder preprocessing, representing a 13.3 percentage point improvement over the baseline (72.3%)."

### Nelaka K.A.R 2025 (2)

Nelaka K.A.R, Peiris M.K.V, Liyanage R.P.B. (2025). Deep Learning Based Approach to Enhanced Recognition of Emotions and Behavioral Patterns of Autistic Children. arXiv preprint. [doi:10.1109/icac69156.2025.11361475](https://doi.org/10.1109/icac69156.2025.11361475)

`q2 · i?` · `causal · r1`

Statistical significance analysis in the Results section applying McNemar's test to paired predictions; the article reports "χ2 = 98 .01, p < 0.001" with statistical power exceeding 99.9%. No effect size is attached to this test statistic.

> "The McNemar's test results ( χ2 = 98 .01, p < 0.001) further confirm the statistical significance when comparing the paired predictions of baseline versus enhanced models."

## Discussion


## Related Claims
- [The accuracy benefit of autoencoder preprocessing is consistent across Xception and InceptionV3, with a coefficient of variation of 2.7%, suggesting architecture-independent gains](autoencoder-benefit-architecture-independent-consistency.md) — related
- [Autoencoder preprocessing is computationally efficient for ASD emotion recognition, with a 10–20% overhead yielding an 18% accuracy improvement (a 9:1 efficiency ratio)](autoencoder-preprocessing-computational-efficiency-ratio.md) — related
- [Autoencoder preprocessing cuts classification error rates for ASD emotion recognition by 48.0% for Xception and 44.1% for InceptionV3](autoencoder-preprocessing-error-rate-reduction-asd.md) — possibly the same claim (merge candidate)
- [Autoencoder preprocessing raises InceptionV3 emotion-recognition accuracy for ASD children's facial images from 71.0% to 83.8%, a 12.8 percentage-point improvement with a very large effect size](autoencoder-preprocessing-inceptionv3-accuracy-gain-asd.md) — related
