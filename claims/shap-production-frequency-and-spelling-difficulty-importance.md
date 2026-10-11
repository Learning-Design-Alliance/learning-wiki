---
type: claim
title: SHAP analysis of the explainable model identifies production frequency and spelling difficulty as high-impact predictors of KVL difficulty, with spelling difficulty varying strongly by L1
description: SHAP analysis of the explainable model identifies production frequency and spelling difficulty as high-impact predictors of KVL difficulty, with spelling difficulty varying strongly by L1
id: shap-production-frequency-and-spelling-difficulty-importance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: adam-nohejl-2026
    resource: "https://arxiv.org/abs/2605.14257"
    title: "Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257"
    author: Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka
    q: 2
    i: "?"
---

# SHAP analysis of the explainable model identifies production frequency and spelling difficulty as high-impact predictors of KVL difficulty, with spelling difficulty varying strongly by L1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` Production frequency is a consistently high-impact feature across languages, overshadowing reception frequency, which ranks as the least important across L1s. [→ Adam Nohejl 2026](#adam-nohejl-2026)

## Evidence

### Adam Nohejl 2026

Adam Nohejl, Xuanxin Wu, Yusuke Ide, Maria Angelica Riera Machin, Yi-Ning Chang, Hitomi Yanaka. (2026). Sakura at BEA 2026 Shared Task 1: What Makes Vocabulary Difficult? https://arxiv.org/abs/2605.14257

`q2 · i?`

Global SHAP analysis (Section 6.2, Figure 1) of mean absolute SHAP values over the test data for the explainable model. The authors link the feature's importance to the KVL's focus on production, noting its importance "corresponds with the amount ofL1-specific data available."

> "Production frequencyis a consistently high-impactfeatureacrosslanguages. Itsimportanceper language, in fact, corresponds with the amount ofL1-specific data available."

## Discussion


## Related Claims
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [Test item construction, including avoidance of cognate L1 equivalents, often affects KVL difficulty scores beyond the genuine difficulty of the words](test-item-construction-affects-kvl-difficulty-scores.md) — related
