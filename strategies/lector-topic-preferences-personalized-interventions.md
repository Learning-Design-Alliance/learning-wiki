---
type: strategy
id: lector-topic-preferences-personalized-interventions
title: Use LECTOR-extracted topic preferences to design personalized interventions tailored to individual reading preferences
description: The article proposes using the topic preferences extracted by LECTOR as a basis for personalized student support.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: erwin-daniel-lópez-zapata-2025
    resource: "https://doi.org/10.1007/s40593-025-00478-6"
    title: "Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6"
    author: Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada
---

# Use LECTOR-extracted topic preferences to design personalized interventions tailored to individual reading preferences

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article proposes using the topic preferences extracted by LECTOR as a basis for personalized student support. Because at-risk prediction models built only on activity frequencies "do not specify which content requires review", topic-based features indicate which topics a student engages with relatively more or less, giving instructors actionable, content-level information. The authors "proposed examples showing the potential application of the reading preferences extracted by LECTOR in designing personalized interventions for students".

## Design Implications

### Context
#### Requirements
- LECTOR's matrix M estimated for the course materials, plus students' reading-time logs from the e-book system
#### Constraints
- The article presents application examples as potential rather than tested; the prediction benefit over traditional features was a tendency with significant gains only in some cases

### Target Learners
- university students at risk of low final grades in programming courses

### Target Learning Goals
- identifying which specific content topics require review for each student

## Claims

- [LECTOR achieves the highest keyphrase extraction performance among compared models at @15, Best and Mean evaluations on lecture slides](../claims/lector-highest-keyphrase-f1-lecture-slides.md) [+W]
- [Students rated LECTOR-extracted keyphrases as more relevant than TF-IDF-extracted keyphrases in a human evaluation](../claims/lector-human-evaluation-outperforms-tfidf.md) [+W]
- [Topic-preference features separate grade groups better than Reading Time in all analyzed cases](../claims/topic-preference-fdr-beats-reading-time.md) [+W]
- [Integrating LECTOR topic preferences into at-risk prediction shows a tendency to improve performance, with significant AUC gains only in some cases](../claims/topic-preferences-at-risk-prediction-mixed.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6
