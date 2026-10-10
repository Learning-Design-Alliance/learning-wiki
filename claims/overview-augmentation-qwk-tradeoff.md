---
type: claim
title: In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off
description: In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off
id: overview-augmentation-qwk-tradeoff
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
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

# In the Overview dimension, augmentation produced a marginal QWK decrease (ΔQWK = −0.006) despite improving macro-F1, the only dimension with this trade-off

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Augmentation lowered Overview QWK from its baseline while raising macro-F1 from 0.325 to 0.352, the only such dimension. [→ Firdausi 2026](#firdausi-2026)

## Evidence

### Firdausi 2026

Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09

`q2 · i?` · `design · r2`

Ablation result for the Overview dimension (Results §4.3.6, best model IB-BiLSTM-F, test QWK 0.474). The article reports the marginal QWK decrease alongside the macro-F1 improvement and attributes it to synthetic samples possibly blurring ordinal transitions.

> "data augmentation produced a marginal decrease in QWK (ΔQWK = −0.006), despite improving macro-F1 from 0.325 to 0.352, the only dimension where this trade -off occurred."

## Discussion


## Related Claims
- [Data augmentation was critical for ordinal discriminability, with QWK dropping to near-zero without it in the Focus dimension and gains up to +0.346 in severely imbalanced dimensions](augmentation-critical-ordinal-qwk-gains.md) — related
- [The best AES models per FRISCO dimension reached strong agreement for Situation (QWK 0.728) and Clarity (QWK 0.763) but only fair agreement for Focus, Reason, and Inference in Indonesian physics essays](aes-frisco-qwk-varies-by-dimension.md) — related
