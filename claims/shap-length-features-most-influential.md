---
type: claim
title: Lecture length features are the most influential predictors of engagement, and the top five features span all quality verticals
description: Lecture length features are the most influential predictors of engagement, and the top five features span all quality verticals
id: shap-length-features-most-influential
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: sahan-bulathwela-2020
    resource: "https://doi.org/10.48550/arXiv.2006.00592"
    title: "Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)"
    author: Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: sahan-bulathwela-2020-2
    resource: "https://doi.org/10.48550/arXiv.2006.00592"
    title: "Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)"
    author: Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Lecture length features are the most influential predictors of engagement, and the top five features span all quality verticals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SHAP analysis of the best RF model shows lecture duration and word count are the most relevant features, with long videos generally presenting lower engagement. [→ Sahan Bulathwela 2020](#sahan-bulathwela-2020)
`q2 i?` The five most influential content features represent all identified quality verticals: topic coverage, understandability, freshness and presentation. [→ Sahan Bulathwela 2020 (2)](#sahan-bulathwela-2020-2)

## Evidence

### Sahan Bulathwela 2020

Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)

`q2 · i?` · `associational · r2`

SHAP feature-importance analysis of the best performing RF model on the 30% test set (Figures 6 and 7, Table 4). Word Count has the highest Mean Absolute SHAP (.250, 36.6%), followed by Published Date (.107); the authors note prior studies confirm the length observation.

> "long videos generally present lower engagement and vice versa, with lecture duration and word count being the most relevant features."

### Sahan Bulathwela 2020 (2)

Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)

`q2 · i?` · `associational · r2`

Quantitative MAS ranking in Table 4 maps top features to quality verticals from the authors' prior quality-assurance work; the authors say this supports considering all verticals when predicting context-agnostic engagement.

> "By looking at the ﬁve most inﬂuential features, we observe that all identiﬁed quality ver- ticals (topic coverage, understandability, freshness and pre- sentation) are represented."

## Discussion


## Related Claims
- [In decision-tree and random-forest models, academic word list count, word count, and Flesch-Kincaid grade level were among the most important features for predicting cognitive engagement in discussion posts; an SVM ranked different features first](awl-count-word-count-feature-importance-engagement.md) — related
- [Document length alone carries some signal (word-count classifier ROC-AUC 0.68), but the fixed-word sliding-window design largely prevents stylometric features from capturing length differences](sliding-window-controls-document-length-effects.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — reports the opposite
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [A multiple linear regression on normalised video features explains little engagement variance, with duration the most influential feature and word count unexpectedly positive](regression-duration-most-influential-word-count-positive.md) — related
