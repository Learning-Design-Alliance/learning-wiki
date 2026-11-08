---
type: research-method
id: exploratory-unsupervised-clustering-methodology-for-identifying-at-risk-student-profiles-f
title: Exploratory unsupervised clustering methodology for identifying at-risk student profiles from pre-admission data
description: The article develops an exploratory, unsupervised methodology that applies clustering to university pre-admission data to find latent structures without predefined labels.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Exploratory unsupervised clustering methodology for identifying at-risk student profiles from pre-admission data

> **Research Method** · [All research methods](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article develops an exploratory, unsupervised methodology that applies clustering to university pre-admission data to find latent structures without predefined labels. "The process involves three main phases (see Fig. 1): Data Preparation, Experimentation and Analysis of the Selected Models." Model selection combines internal validation (Silhouette, Davies-Bouldin, Calinski-Harabasz), association with outcomes (Cramér's V), and cluster quality (purity, entropy) via a composite score. It is positioned as an alternative to deductive, theory-driven and supervised approaches.

## Accounts
<!-- How each source describes or uses the method -->
- **Exploratory unsupervised clustering methodology for identifying at-risk student profiles from pre-admission data**: The article develops an exploratory, unsupervised methodology that applies clustering to university pre-admission data to find latent structures without predefined labels. "The process involves three main phases (see Fig. 1): Data Preparation, Experimentation and Analysis of the Selected Models." Model selection combines internal validation (Silhouette, Davies-Bouldin, Calinski-Harabasz), association with outcomes (Cramér's V), and cluster quality (purity, entropy) via a composite score. It is positioned as an alternative to deductive, theory-driven and supervised approaches. (Fabian Santiago-Muñoz et al. (2025))
- **The student-signature approach to admissions and personalized education**: The article proposes replacing a 'one-size-fits-all' admissions reading of applicants with a data-driven account of "distinct clusters of students" delineated by pattern of achievement. It works by feature-engineering applicant records, K-means clustering to define signatures, and logistic regression using the signature to predict medical school success. The authors present it as an example of how "learning analytics may allow for the personalized education of health professions" and for "the implementation of personalized education for more successful student training". (Baron Tal et al. (2020))

### Claims
- [Pre-admission data (2018–2022) contain sufficient information to identify early patterns of dropout or course failure in first-year engineering mathematics subjects](../claims/pre-admission-data-identify-early-dropout-failure-patterns.md) [+M]
- [The Gaussian Mixture algorithm achieved optimal clustering solutions in four of six scenarios, while no evaluated algorithm yielded satisfactory results in the remaining two](../claims/gaussian-mixture-optimal-four-of-six-scenarios.md) [+M]
- [The choice of normalization technique influences clustering outcomes, so multiple normalization approaches should be tested in cluster analysis](../claims/normalization-choice-influences-clustering-outcomes.md) [~M]
- [K-means clustering of admissions data yields four student signatures distinguished mainly by uGPA level and trajectory](../claims/four-medical-student-signatures-clustering.md) [+M]
- [Adding signature classification as a feature improves success prediction accuracy from 36.8% to 44.2% on the test group](../claims/signature-improves-success-prediction-accuracy.md) [+M]
- [Risers and statics have significantly higher and lower medical school success indices than the overall average, respectively](../claims/risers-higher-statics-lower-success-index.md) [+M]

## Related Research Methods
-

## Key Sources
- Fabian Santiago-Muñoz, Mikel Larrañaga, Jon A. Elorriaga, Ana Arruarte. (2025). Identification of Patterns to Prevent the Failure of Engineering Students. Int J Artif Intell Educ 35:3356–3405. https://doi.org/10.1007/s40593-025-00502-9
- Baron Tal, Grossman Robert I., Abramson Steven B., Pusic Martin V., Rivera Rafael, Triola Marc M., Yanai Itai. (2020). Signatures of medical student applicants and academic success. PLoS ONE. https://doi.org/10.1371/journal.pone.0227108
