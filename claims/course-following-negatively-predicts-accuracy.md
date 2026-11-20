---
type: claim
title: Logistic regression over question-specific video segments finds peer attention and valid focus positively predict accuracy while course following negatively predicts it
description: Logistic regression over question-specific video segments finds peer attention and valid focus positively predict accuracy while course following negatively predicts it
id: course-following-negatively-predicts-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: songlin-xu-2023
    resource: "https://doi.org/10.48550/arXiv.2312.02358"
    title: "Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang. (2023). Peer attention enhances student learning. arXiv preprint. [doi:10.48550/arXiv.2312.02358](https://doi.org/10.48550/arXiv.2312.02358)"
    author: Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: songlin-xu-2023-2
    resource: "https://doi.org/10.48550/arXiv.2312.02358"
    title: "Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang. (2023). Peer attention enhances student learning. arXiv preprint. [doi:10.48550/arXiv.2312.02358](https://doi.org/10.48550/arXiv.2312.02358)"
    author: Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Logistic regression over question-specific video segments finds peer attention and valid focus positively predict accuracy while course following negatively predicts it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Peer attention (β = 0.84) and valid focus (β = 0.11) positively predicted question accuracy in logistic regressions over question-matched video durations. [→ Songlin Xu 2023](#songlin-xu-2023)
`q2 i?` Course following negatively correlated with question accuracy (β = −0.18), suggesting pace-adherence alone does not guarantee learning. [→ Songlin Xu 2023 (2)](#songlin-xu-2023-2)

## Evidence

### Songlin Xu 2023

Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang. (2023). Peer attention enhances student learning. arXiv preprint. [doi:10.48550/arXiv.2312.02358](https://doi.org/10.48550/arXiv.2312.02358)

`q2 · i?` · `causal · r2`

Granular analysis (Fig. 4) matched each post-test question to its related course-video duration and ran logistic regression on binary accuracy with concurrent experience metrics. Peer attention coefficient β = 0.84 (P < 0.001) and valid focus β = 0.11 (P = 0.009); unstandardised-style coefficients, no standardized effect size printed.

> "Peer attention (coefficient β = 0.84,P < 0.001) and valid focus (coefficient β = 0.11,P = 0.009 < 0.01) positively predicted accuracy."

### Songlin Xu 2023 (2)

Songlin Xu, Dongyin Hu, Ru Wang, and Xinyu Zhang. (2023). Peer attention enhances student learning. arXiv preprint. [doi:10.48550/arXiv.2312.02358](https://doi.org/10.48550/arXiv.2312.02358)

`q2 · i?` · `causal · r2`

Same question-level logistic regression analysis found course following negatively correlated with accuracy (β = −0.18, P < 0.001). The authors suggest students pausing to think deeply may show valid focus without strict pace-alignment yet still understand content; no standardized effect size printed.

> "However, course following negatively correlated with accuracy (coefficientβ = −0.18,P < 0.001)."

## Discussion


## Related Claims
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [Trained logistic-regression coefficients align with the human coding scheme's inclusion and exclusion criteria](model-coefficients-align-with-coding-scheme-criteria.md) — related
