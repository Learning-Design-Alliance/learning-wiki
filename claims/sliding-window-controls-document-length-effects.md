---
type: claim
title: Document length alone carries some signal (word-count classifier ROC-AUC 0.68), but the fixed-word sliding-window design largely prevents stylometric features from capturing length differences
description: Document length alone carries some signal (word-count classifier ROC-AUC 0.68), but the fixed-word sliding-window design largely prevents stylometric features from capturing length differences
id: sliding-window-controls-document-length-effects
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: rajesh-kumar-2026
    resource: "https://arxiv.org/abs/2609.26687"
    title: "Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger. (2026). Detecting GPT-Assisted Writing Using Interpretable Stylometric Features. https://arxiv.org/abs/2609.26687"
    author: Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Document length alone carries some signal (word-count classifier ROC-AUC 0.68), but the fixed-word sliding-window design largely prevents stylometric features from capturing length differences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A classifier using only total document word count achieved a cross-validation ROC-AUC of 0.68, showing length contains some information, while the 250-word windowing design largely prevents the stylometric features from directly capturing document-length differences. [→ Rajesh Kumar 2026](#rajesh-kumar-2026)

## Evidence

### Rajesh Kumar 2026

Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger. (2026). Detecting GPT-Assisted Writing Using Interpretable Stylometric Features. https://arxiv.org/abs/2609.26687

`q2 · i?` · `design · r2`

Post-hoc control analysis comparing a word-count-only classifier with the main windowed model. Independently authored documents were longer (paired t(89) = 6.46, p < .001), and replacing TTR and Hapax Ratio with moving-average TTR produced an ROC-AUC close to the full model.

> "a classifier using only the total document word count achieved a cross-validation ROC-AUC of0.68, showing that document length itself contains some information about the writing condition."

## Discussion


## Related Claims
- [SHAP analysis identifies Hapax Ratio as the most influential stylometric feature in Random Forest predictions, followed by NSR, Noun Ratio, Adverb Ratio, and TTR](shap-hapax-ratio-most-influential-feature.md) — related
- [Random Forest using nine interpretable stylometric features detects GPT-assisted student writing with held-out ROC-AUC of 0.870 and F1 of 0.842](stylometric-features-detect-gpt-assisted-writing-rf-auc-0870.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [The stylometric detector misclassified 4 of 18 independently authored documents as GPT-assisted (FPR 22.2%) and 2 of 18 GPT-assisted documents (FNR 11.1%), with wide confidence intervals](stylometric-detector-fpr-22-fnr-11.md) — related
