---
type: claim
title: The best AES models per FRISCO dimension reached strong agreement for Situation (QWK 0.728) and Clarity (QWK 0.763) but only fair agreement for Focus, Reason, and Inference in Indonesian physics essays
description: The best AES models per FRISCO dimension reached strong agreement for Situation (QWK 0.728) and Clarity (QWK 0.763) but only fair agreement for Focus, Reason, and Inference in Indonesian physics essays
id: aes-frisco-qwk-varies-by-dimension
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

# The best AES models per FRISCO dimension reached strong agreement for Situation (QWK 0.728) and Clarity (QWK 0.763) but only fair agreement for Focus, Reason, and Inference in Indonesian physics essays

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Best-performing models achieved QWK of 0.728 (Situation), 0.763 (Clarity), 0.474 (Overview), 0.374 (Focus), 0.332 (Reason), and 0.227 (Inference) on the held-out test set. [→ Firdausi 2026](#firdausi-2026)

## Evidence

### Firdausi 2026

Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09

`q2 · i?` · `design · r2`

Single hold-out test evaluation (23 students) of the best model per dimension after 5-fold CV selection, reported in Results Table 11. The study reports "Situation (QWK = 0.728)" and "Clarity (QWK = 0.763)" as strong, with Inference weakest at 0.227; no effect size beyond QWK is printed.

> "The strongest performance was observed in Situation (QWK = 0.728) and Clarity (QWK = 0.763), both exceeding the previous results and approaching or reaching the threshold for strong agreement, while the weakest was observed in Inference (QWK = 0.227)."

## Discussion


## Related Claims
- [In the Reason dimension, the IndoBERT–SVM baseline outperformed all BiLSTM variants, achieving QWK 0.332](svm-outperforms-bilstm-reason-dimension.md) — a narrower finding that bears on this claim
- [Data augmentation was critical for ordinal discriminability, with QWK dropping to near-zero without it in the Focus dimension and gains up to +0.346 in severely imbalanced dimensions](augmentation-critical-ordinal-qwk-gains.md) — related
- [Cross-validation-selected hyperparameters generalized to the test set only for Situation and Clarity, with the other four dimensions showing CV–test misalignment](cv-test-misalignment-small-imbalanced-data.md) — related
- [In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off](overview-augmentation-qwk-tradeoff.md) — related
