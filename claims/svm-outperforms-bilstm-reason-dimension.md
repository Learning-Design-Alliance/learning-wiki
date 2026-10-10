---
type: claim
title: In the Reason dimension, the IndoBERT–SVM baseline outperformed all BiLSTM variants, achieving QWK 0.332
description: In the Reason dimension, the IndoBERT–SVM baseline outperformed all BiLSTM variants, achieving QWK 0.332
id: svm-outperforms-bilstm-reason-dimension
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

# In the Reason dimension, the IndoBERT–SVM baseline outperformed all BiLSTM variants, achieving QWK 0.332

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` IB-SVM achieved accuracy 0.522, macro-F1 0.394, and QWK 0.332 in Reason, outperforming all BiLSTM variants. [→ Firdausi 2026](#firdausi-2026)

## Evidence

### Firdausi 2026

Firdausi, H.; Wasis; Sholikah, R. W.; Lemantara, J.; Rosyadi, F. D.; Ginardi, R. V. H.; Pradityo, M. H. A.; Hakim, A. R. (2026). Educational Innovation through Automated Essay Scoring: A Multidimensional Framework for Evaluating Critical Thinking in High School Physics Essays. International Journal of Intelligent Engineering and Systems, Vol.19, No.8. https://doi.org/10.22266/ijies2026.0831.09

`q2 · i?` · `design · r2`

Test-set comparison across the three architectures in Results §4.3.2. The article reports the SVM with frozen IndoBERT [CLS] embeddings beat every BiLSTM variant on Reason, consistent with kernel models remaining competitive on small domain-specific datasets.

> "In the Reason dimension, IB -SVM emerged as the best-performing model, with an accuracy of 0.522, a macro -F1 of 0.394, and a QWK of 0.332 (fair agreement), outperforming all BiLSTM variants."

## Discussion


## Related Claims
- [The best AES models per FRISCO dimension reached strong agreement for Situation (QWK 0.728) and Clarity (QWK 0.763) but only fair agreement for Focus, Reason, and Inference in Indonesian physics essays](aes-frisco-qwk-varies-by-dimension.md) — a broader claim this one bears on
