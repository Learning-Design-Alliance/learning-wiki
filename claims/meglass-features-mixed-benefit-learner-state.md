---
type: claim
title: Eyeglass-detection (MeGlass) features slightly improved non-mind-wandering detection but not mind-wandering detection
description: Eyeglass-detection (MeGlass) features slightly improved non-mind-wandering detection but not mind-wandering detection
id: meglass-features-mixed-benefit-learner-state
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: bodonhelyi-2026
    resource: "https://doi.org/10.48550/arXiv.2602.09904"
    title: "Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. [doi:10.48550/arXiv.2602.09904](https://doi.org/10.48550/arXiv.2602.09904)"
    author: Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Eyeglass-detection (MeGlass) features slightly improved non-mind-wandering detection but not mind-wandering detection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding MeGlass glass-detection features slightly improved performance on non-mind-wandering datasets, but on mind-wandering datasets the baseline bi-LSTM performed comparably or better. [→ Bodonhelyi 2026](#bodonhelyi-2026)

## Evidence

### Bodonhelyi 2026

Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. [doi:10.48550/arXiv.2602.09904](https://doi.org/10.48550/arXiv.2602.09904)

`q2 · i?` · `design · r2`

Centralized comparison of baseline bi-LSTM versus MeGlass-augmented bi-LSTM across four datasets (Table 2): MeGlass features gave "a slight improvement in model performance" on non-mind-wandering datasets, while the baseline "either outperformed the models enhanced with MeGlass features or achieved comparable results" on mind-wandering datasets.

> "for the non-mind-wandering datasets, the inclusion of MeGlass features led to a slight improvement in model performance. In contrast, for the mind-wandering datasets, the baseline bi-LSTM either outperformed the models enhanced with MeGlass features or achieved comparable results."

## Discussion


## Related Claims
- [Latent transfer-learned features yield better overall mind wandering detection than explicit OpenFace features, and temporal models add a small improvement, especially cross-dataset](latent-features-beat-explicit-features-overall.md) — related
- [LIME analysis shows the latent features mainly encode information from eye and mouth areas of the face](lime-eye-mouth-areas-in-latent-features.md) — related
