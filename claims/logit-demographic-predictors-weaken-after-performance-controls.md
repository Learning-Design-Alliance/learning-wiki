---
type: claim
title: "In descriptive logit models, demographic variables predict dropout at enrollment (e.g., males have a 60% higher chance of dropping out than females), but most lose significance once first-semester performance data is controlled"
description: "In descriptive logit models, demographic variables predict dropout at enrollment (e.g., males have a 60% higher chance of dropping out than females), but most lose significance once first-semester performance data is..."
id: logit-demographic-predictors-weaken-after-performance-controls
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
sources:
  - id: johannes-berens-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389"
    title: "Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff. (2019). Early Detection of Students at Risk - Predicting Student Dropouts Using Administrative Student Data from German Universities and Machine Learning Methods. Journal of Educational Data Mining, Volume 11, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389"
    author: Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
  - id: johannes-berens-2019-2
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389"
    title: "Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff. (2019). Early Detection of Students at Risk - Predicting Student Dropouts Using Administrative Student Data from German Universities and Machine Learning Methods. Journal of Educational Data Mining, Volume 11, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389"
    author: Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# In descriptive logit models, demographic variables predict dropout at enrollment (e.g., males have a 60% higher chance of dropping out than females), but most lose significance once first-semester performance data is controlled

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` At enrollment, male students, older students, and immigrants show higher dropout odds; first-generation immigrants have a 22% higher rate and second-generation immigrants a 46% higher rate than native students. [→ Johannes Berens 2019](#johannes-berens-2019)
`q2 i?` Most demographic variables lose statistical significance when first-semester performance data is included in the model. [→ Johannes Berens 2019 (2)](#johannes-berens-2019-2)

## Evidence

### Johannes Berens 2019

Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff. (2019). Early Detection of Students at Risk - Predicting Student Dropouts Using Administrative Student Data from German Universities and Machine Learning Methods. Journal of Educational Data Mining, Volume 11, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389

`q2 · i?` · `associational · r?`

Pooled-sample logit models on SU training data (N = 12,728 at enrollment), reporting odds ratios; the models are described as strictly descriptive with no causal interpretation. The quote reports the printed demographic correlates; no standardized effect size is printed.

> "At enrollment, males have a 60% higher chance of dropping out than females. Age at enrollment shares a positive correlation with dropping out. At the time of enrollment, immigrants have a higher dropout risk as compared to native students (baseline category), and first-generation immigrants have a higher dropout risk than second-generation immigrants."

### Johannes Berens 2019 (2)

Johannes Berens, Kerstin Schneider, Simon Görtz, Simon Oster, Julian Burghoff. (2019). Early Detection of Students at Risk - Predicting Student Dropouts Using Administrative Student Data from German Universities and Machine Learning Methods. Journal of Educational Data Mining, Volume 11, No 3. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/389

`q2 · i?` · `associational · r2`

In the same SU logit specifications, adding first-semester performance data (average grade, credit points, exams taken, failed exams) renders most demographic coefficients statistically insignificant, consistent with the AIC falling from 15,658 to 11,988.

> "Most of the demographic variables lose statistical significance when controlling for the performance data available after"

## Discussion


## Related Claims
- [Including demographic variables as predictors can reduce actionability by de-emphasizing correlated actionable risk factors and by discounting intervention effects](demographic-predictors-reduce-actionability.md) — related
- [Early-stage performance data is particularly important for predicting attrition, while demographic data has limited predictive value once performance data is available](performance-data-dominates-demographics-in-dropout-prediction.md) — a broader claim this one bears on
- [Evidence is mixed on whether including demographic variables as predictors improves model performance in educational prediction](mixed-evidence-demographic-predictor-performance.md) — related
- [Using predictive analytics while ignoring teacher knowledge may misidentify students at risk of dropping out and negatively influence teacher views](ignoring-teacher-knowledge-misidentifies-risk-students.md) — related
