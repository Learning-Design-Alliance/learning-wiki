---
type: claim
title: Neural-network predictions agree with the analytical solution within the training domain and can extrapolate when the wavelength-distance product falls within the support of the training distribution, but fail when it does not
description: Neural-network predictions agree with the analytical solution within the training domain and can extrapolate when the wavelength-distance product falls within the support of the training distribution, but fail when it...
id: nn-extrapolation-lambda-z-support
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: c-finot-and-s-boscolo-2022
    resource: "https://doi.org/10.1088/1361-6404/ac5bec"
    title: "C Finot and S Boscolo (2022). Exploring Fresnel diffraction at a straight edge with a neural network. [doi:10.1088/1361-6404/ac5bec](https://doi.org/10.1088/1361-6404/ac5bec)"
    author: C Finot and S Boscolo
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Neural-network predictions agree with the analytical solution within the training domain and can extrapolate when the wavelength-distance product falls within the support of the training distribution, but fail when it does not

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Within the initial dataset domain, predictions agree very well with the analytical solution, demonstrating universal interpolation capability. [→ C Finot and S Boscolo 2022](#c-finot-and-s-boscolo-2022)
`q2 i?` Extrapolation succeeds for a parameter pair outside the data range but inside the support of the training distribution of the wavelength-distance product, and fails when the product falls outside that support. [→ C Finot and S Boscolo 2022](#c-finot-and-s-boscolo-2022)

## Evidence

### C Finot and S Boscolo 2022

C Finot and S Boscolo (2022). Exploring Fresnel diffraction at a straight edge with a neural network. [doi:10.1088/1361-6404/ac5bec](https://doi.org/10.1088/1361-6404/ac5bec)

`q2 · i?` · `design · r2`

Comparison of network predictions with the analytical solution for various wavelength-distance pairs (Fig. 6). The article notes the failing case falls outside the support of the training distribution of the wavelength-distance product, while the successful extrapolation case falls within it.

> "the predictions made by the neural networks with 12 and 15 neurons per layer remain fully consistent with the analytical solution, thus suggesting that the network model can also succeed at extrapolation. However, when the observation distance is 35 cm (Fig. 6a3), none of the neural networks used can predict a fitting diffraction pattern"

## Discussion


## Related Claims
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — related
- [Students have great difficulty extrapolating three dimensions from one- and two-dimensional astronomical representations](difficulty-extrapolating-3d-from-2d-astronomy-representations.md) — related
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](llm-distractor-prediction-asymmetry.md) — related
