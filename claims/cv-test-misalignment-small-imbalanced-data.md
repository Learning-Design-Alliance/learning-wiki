---
type: claim
title: Cross-validation-selected hyperparameters generalized to the test set only for Situation and Clarity, with the other four dimensions showing CV–test misalignment
description: Cross-validation-selected hyperparameters generalized to the test set only for Situation and Clarity, with the other four dimensions showing CV–test misalignment
id: cv-test-misalignment-small-imbalanced-data
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

# Cross-validation-selected hyperparameters generalized to the test set only for Situation and Clarity, with the other four dimensions showing CV–test misalignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` CV-selected configurations matched best test performance only for Situation and Clarity; remaining dimensions showed misalignment attributed to severe class imbalance and limited training samples. [→ Firdausi 2026](#firdausi-2026)

## Evidence

### Firdausi 2026

Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09

`q2 · i?` · `design · r2`

Comparison of stratified 5-fold CV results (Table 9) with held-out test results (Table 10) across six dimensions in Results §4.3. The article reports CV QWK varied widely, e.g., Inference 0.118 ± 0.185 with high variance.

> "Notably, Situation and Clarity were the only two dimensions in which the CV-selected hyperparameters generalized consistently to the test set, whereas the remaining dimensions exhibited misalignment between CV estimates and test performance, likely attributable to severe class imbalance and limited training samples"

## Discussion


## Related Claims
- [The best AES models per FRISCO dimension reached strong agreement for Situation (QWK 0.728) and Clarity (QWK 0.763) but only fair agreement for Focus, Reason, and Inference in Indonesian physics essays](aes-frisco-qwk-varies-by-dimension.md) — related
