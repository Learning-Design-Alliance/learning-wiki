---
type: claim
title: A multiple linear regression on normalised video features explains little engagement variance, with duration the most influential feature and word count unexpectedly positive
description: A multiple linear regression on normalised video features explains little engagement variance, with duration the most influential feature and word count unexpectedly positive
id: regression-duration-most-influential-word-count-positive
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: tolba-2025
    resource: "https://doi.org/10.48550/arXiv.2512.16254"
    title: "Tolba, Kendall, Tudball Smith, Gregg, Vo, Wordley. (2025). An Open Workflow Model for Improving Educational Video Design: Tools, Data, and Insights. Proceedings of AAEE 2025, The University of Queensland, Australia. [doi:10.48550/arXiv.2512.16254](https://doi.org/10.48550/arXiv.2512.16254)"
    author: Tolba, Kendall, Tudball Smith, Gregg, Vo, Wordley
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: tolba-2025-2
    resource: "https://doi.org/10.48550/arXiv.2512.16254"
    title: "Tolba, Kendall, Tudball Smith, Gregg, Vo, Wordley. (2025). An Open Workflow Model for Improving Educational Video Design: Tools, Data, and Insights. Proceedings of AAEE 2025, The University of Queensland, Australia. [doi:10.48550/arXiv.2512.16254](https://doi.org/10.48550/arXiv.2512.16254)"
    author: Tolba, Kendall, Tudball Smith, Gregg, Vo, Wordley
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# A multiple linear regression on normalised video features explains little engagement variance, with duration the most influential feature and word count unexpectedly positive

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The trained regression model yielded RMSE 8.6 and R² 0.0853, indicating modest explanatory power. [→ Tolba 2025](#tolba-2025)
`q2 i?` Video duration emerged as the most influential feature with a strong negative association; total number of words exhibited a positive association with engagement, contrary to exploratory trends. [→ Tolba 2025 (2)](#tolba-2025-2)

## Evidence

### Tolba 2025

Tolba, Kendall, Tudball Smith, Gregg, Vo, Wordley. (2025). An Open Workflow Model for Improving Educational Video Design: Tools, Data, and Insights. Proceedings of AAEE 2025, The University of Queensland, Australia. [doi:10.48550/arXiv.2512.16254](https://doi.org/10.48550/arXiv.2512.16254)

`q2 · i?` · `associational · r1`

Multiple linear regression trained on z-score-normalised features from the 144-video case study, selected for simplicity and interpretability. The article reports "an R² value of 0.0853, indicating modest explanatory power"; no standardised effect size is printed for this finding.

> "The trained model yielded a root mean squared error (RMSE) of 8.6 and an R² value of 0.0853, indicating modest explanatory power."

### Tolba 2025 (2)

Tolba, Kendall, Tudball Smith, Gregg, Vo, Wordley. (2025). An Open Workflow Model for Improving Educational Video Design: Tools, Data, and Insights. Proceedings of AAEE 2025, The University of Queensland, Australia. [doi:10.48550/arXiv.2512.16254](https://doi.org/10.48550/arXiv.2512.16254)

`q2 · i?` · `associational · r1`

Insight-extraction stage interpreting the normalised regression weights (duration −21.81, words 20.52, speaking speed −3.04, scenes −1.02, scene change rate 1.15). The article reports the word-count result as "contrary to initial assumptions and exploratory data analysis trends".

> "video duration showed a strong negative association with average percentage viewed and emerged as the most influential feature among those studied. However, contrary to initial assumptions and exploratory data analysis trends, where higher word counts were generally linked to lower retention, the total number of words exhibited a positive association with engagement."

## Discussion


## Related Claims
- [Video duration and word count show the strongest negative linear correlations with viewer engagement in a lecture-video dataset](duration-word-count-negative-correlation-engagement.md) — related
- [LOESS curves reveal non-linear feature–engagement patterns: shorter videos and moderate speaking speed and scene values are associated with higher retention](loess-nonlinear-video-feature-engagement-patterns.md) — related
- [Lecture length features are the most influential predictors of engagement, and the top five features span all quality verticals](shap-length-features-most-influential.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [Speaking speed, scene count and scene change rate show minimal or weak linear correlations with engagement](speaking-speed-scene-features-minimal-correlation.md) — related
