---
type: claim
title: Data augmentation was critical for ordinal discriminability, with QWK dropping to near-zero without it in the Focus dimension and gains up to +0.346 in severely imbalanced dimensions
description: Data augmentation was critical for ordinal discriminability, with QWK dropping to near-zero without it in the Focus dimension and gains up to +0.346 in severely imbalanced dimensions
id: augmentation-critical-ordinal-qwk-gains
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: firdausi-2026
    resource: "https://doi.org/10.22266/ijies2026.0831.09"
    title: "Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09"
    author: Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Data augmentation was critical for ordinal discriminability, with QWK dropping to near-zero without it in the Focus dimension and gains up to +0.346 in severely imbalanced dimensions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In the ablation study, augmentation improved ordinal agreement in five of six dimensions; without augmentation, Focus QWK dropped to 0.028 and Inference QWK was negative (−0.115). [→ Firdausi 2026](#firdausi-2026)

## Evidence

### Firdausi 2026

Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09

`q2 · i?` · `design · r2`

Ablation study (Results §4.3.1 and Table 12) comparing the best model per dimension with and without augmentation on the held-out test set. The Focus dimension's QWK fell to "near-zero (0.028)" without augmentation; the article attributes this to severe class imbalance.

> "The ablation study further highlights the critical role of data augmentation: without it, QWK dropped to near-zero (0.028), confirming that class imbalance severely undermines ordinal discrimination"

## Discussion


## Related Claims
- [The best AES models per FRISCO dimension reached strong agreement for Situation (QWK 0.728) and Clarity (QWK 0.763) but only fair agreement for Focus, Reason, and Inference in Indonesian physics essays](aes-frisco-qwk-varies-by-dimension.md) — related
- [In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off](overview-augmentation-qwk-tradeoff.md) — related
