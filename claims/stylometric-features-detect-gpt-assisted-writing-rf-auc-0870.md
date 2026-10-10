---
type: claim
title: Random Forest using nine interpretable stylometric features detects GPT-assisted student writing with held-out ROC-AUC of 0.870 and F1 of 0.842
description: Random Forest using nine interpretable stylometric features detects GPT-assisted student writing with held-out ROC-AUC of 0.870 and F1 of 0.842
id: stylometric-features-detect-gpt-assisted-writing-rf-auc-0870
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

# Random Forest using nine interpretable stylometric features detects GPT-assisted student writing with held-out ROC-AUC of 0.870 and F1 of 0.842

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On 36 held-out documents from 18 unseen participants, Random Forest achieved an ROC-AUC of 0.870 and an F1-score of 0.842 for detecting GPT-assisted writing from stylometric features alone. [→ Rajesh Kumar 2026](#rajesh-kumar-2026)

## Evidence

### Rajesh Kumar 2026

Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger. (2026). Detecting GPT-Assisted Writing Using Interpretable Stylometric Features. https://arxiv.org/abs/2609.26687

`q2 · i?` · `design · r2`

Final evaluation on 36 held-out documents from 18 unseen participants, with all texts from a participant kept in one partition and window probabilities aggregated by median. The article reports "a holdout ROC-AUC of0.870" and F1 of 0.842 with bootstrap confidence intervals.

> "Random Forest achieved a holdout ROC-AUC of0.870 (95% CI:0.747–0.981) and an F1-score of0.842(95% CI:0.737–0.944). Confidence intervals were estimated using participant-level bootstrap resampling."

## Discussion


## Related Claims
- [SHAP analysis identifies Hapax Ratio as the most influential stylometric feature in Random Forest predictions, followed by NSR, Noun Ratio, Adverb Ratio, and TTR](shap-hapax-ratio-most-influential-feature.md) — related
- [Document length alone carries some signal (word-count classifier ROC-AUC 0.68), but the fixed-word sliding-window design largely prevents stylometric features from capturing length differences](sliding-window-controls-document-length-effects.md) — related
- [The stylometric detector misclassified 4 of 18 independently authored documents as GPT-assisted (FPR 22.2%) and 2 of 18 GPT-assisted documents (FNR 11.1%), with wide confidence intervals](stylometric-detector-fpr-22-fnr-11.md) — related
- [GPT-assisted writing shows higher lexical diversity, richness, and noun/non-stopword ratios, while independently authored writing shows higher adverb ratio and sentence-length variability](stylometric-feature-differences-gpt-vs-human.md) — related
