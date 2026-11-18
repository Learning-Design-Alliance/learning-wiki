---
type: claim
title: Model results are robust to varying training fraction and number of trees, but the highest-physics-degree factor is only marginally meaningful
description: Model results are robust to varying training fraction and number of trees, but the highest-physics-degree factor is only marginally meaningful
id: hyperparameter-robustness-variable-importance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: nicholas-t-young-2019
    resource: "https://doi.org/10.1103/physrevphyseducres.15.010114"
    title: "Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)"
    author: Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: nicholas-t-young-2019-2
    resource: "https://doi.org/10.1103/physrevphyseducres.15.010114"
    title: "Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)"
    author: Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Model results are robust to varying training fraction and number of trees, but the highest-physics-degree factor is only marginally meaningful

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 870 forests varying training fraction (0.5–0.9) and forest size (50–1000 trees), accuracy and AUC varied by only 0.03 and 0.02 respectively. [→ Nicholas T. Young 2019](#nicholas-t-young-2019)
`q2 i?` Two factors were selected as meaningful in all 29 varied models and two more in over two-thirds, while highest physics degree offered was selected in only about a third, suggesting it is marginally meaningful. [→ Nicholas T. Young 2019 (2)](#nicholas-t-young-2019-2)

## Evidence

### Nicholas T. Young 2019

Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)

`q2 · i?` · `associational · r2`

Hyperparameter sensitivity analysis: 30 trials per training-fraction/forest-size pair, 870 new forests total; the article reports visual inspection of Figs. 5 and 6 and the printed ranges as a numerical result.

> "the ranges of the accuracy and AUC are 0.03 and 0.02 respectively, which are insigniﬁcant from a practical perspective"

### Nicholas T. Young 2019 (2)

Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)

`q2 · i?` · `associational · r2`

Variable-selection stability analysis across the 29 varied models (Fig. 7); the article adds that none of the other factors appeared in more than 15% of the models.

> "“using computation in research with students” and “I do not personally use computation” were selected as meaningful in all the models while “computation allows me to bring new physics into my course” and “computation allows me to bring new problems into my course” were selected as meaningful in over two-thirds of the models."

## Discussion


## Related Claims
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [The most predictive factors of faculty having experience teaching computation are using computation in research with students, not personally using computation, and beliefs that computation brings new physics and new problems to the classroom](meaningful-factors-faculty-computation-teaching.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [In decision-tree and random-forest models, academic word list count, word count, and Flesch-Kincaid grade level were among the most important features for predicting cognitive engagement in discussion posts; an SVM ranked different features first](awl-count-word-count-feature-importance-engagement.md) — related
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) — related
- [The discourse personalization hint-selection model achieves the highest cross-validated accuracy (86.71%) and F1 (84.81%), significantly above all other models](discourse-personalization-hint-selection-best-cv.md) — related
- [Taking the third-semester modern physics course is the single most important feature in a random forest model predicting whether a declared physics major earns a physics or an engineering degree](modern-physics-course-most-important-predictor-physics-degree.md) — related
