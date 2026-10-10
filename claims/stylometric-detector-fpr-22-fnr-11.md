---
type: claim
title: "The stylometric detector misclassified 4 of 18 independently authored documents as GPT-assisted (FPR 22.2%) and 2 of 18 GPT-assisted documents (FNR 11.1%), with wide confidence intervals"
description: "The stylometric detector misclassified 4 of 18 independently authored documents as GPT-assisted (FPR 22.2%) and 2 of 18 GPT-assisted documents (FNR 11.1%), with wide confidence intervals"
id: stylometric-detector-fpr-22-fnr-11
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# The stylometric detector misclassified 4 of 18 independently authored documents as GPT-assisted (FPR 22.2%) and 2 of 18 GPT-assisted documents (FNR 11.1%), with wide confidence intervals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the held-out test set the False Positive Rate was 22.2% (4/18) and the False Negative Rate was 11.1% (2/18), with 95% Wilson confidence intervals of 9.0–45.2% and 3.1–32.8% respectively. [→ Rajesh Kumar 2026](#rajesh-kumar-2026)

## Evidence

### Rajesh Kumar 2026

Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger. (2026). Detecting GPT-Assisted Writing Using Interpretable Stylometric Features. https://arxiv.org/abs/2609.26687

`q2 · i?` · `design · r2`

Confusion-matrix results on the 36 held-out documents using the median window-probability rule. The article reports "a False Positive Rate of4/18 = 22.2%" and a False Negative Rate of 2/18 = 11.1% with Wilson confidence intervals.

> "resulting in a False Positive Rate of4/18 = 22.2%(95% Wilson CI:9.0%–45.2%). Two GPT-assisted documents were incorrectly classified as independently authored, resulting in a False Negative Rate of2/18 = 11.1%(95% Wilson CI:3.1%–32.8%)."

## Discussion


## Related Claims
- [Document length alone carries some signal (word-count classifier ROC-AUC 0.68), but the fixed-word sliding-window design largely prevents stylometric features from capturing length differences](sliding-window-controls-document-length-effects.md) — related
- [Random Forest using nine interpretable stylometric features detects GPT-assisted student writing with held-out ROC-AUC of 0.870 and F1 of 0.842](stylometric-features-detect-gpt-assisted-writing-rf-auc-0870.md) — related
