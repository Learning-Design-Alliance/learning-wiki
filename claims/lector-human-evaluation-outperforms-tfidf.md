---
type: claim
title: Students rated LECTOR-extracted keyphrases as more relevant than TF-IDF-extracted keyphrases in a human evaluation
description: Students rated LECTOR-extracted keyphrases as more relevant than TF-IDF-extracted keyphrases in a human evaluation
id: lector-human-evaluation-outperforms-tfidf
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: erwin-daniel-lópez-zapata-2025
    resource: "https://doi.org/10.1007/s40593-025-00478-6"
    title: "Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6"
    author: Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: erwin-daniel-lópez-zapata-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00478-6"
    title: "Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6"
    author: Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Students rated LECTOR-extracted keyphrases as more relevant than TF-IDF-extracted keyphrases in a human evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` In a human evaluation with 28 students, LECTOR consistently outperformed TF-IDF, with the difference validated by a T-test; LECTOR achieved an average F-score of 61.8% at Slide-Level versus TF-IDF's 37.7%. [→ Erwin Daniel López Zapata 2025](#erwin-daniel-lopez-zapata-2025)

## Evidence

### Erwin Daniel López Zapata 2025

Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6

`q3 · i?` · `design · r2`

Human evaluation in which 28 students who completed course A-2023 selected up to 5 keyphrases per slide from candidates extracted by LECTOR and TF-IDF; the article reports "LECTOR consistently outperformed the TF-IDF model" with T-test validation.

> "LECTOR consistently outperformed the TF-IDF model, with a difference validated by a T-test (390 samples in SL, 2760 samples in ST-1, and 2301 samples in ST-2)."

### Erwin Daniel López Zapata 2025 (2)

Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6

`q3 · i?` · `design · r2`

Slide-Level ground-truth condition of the same human evaluation: LECTOR's average F-score of 61.8% across 390 slides, compared in Table 7 with TF-IDF's 37.7 ±20.6 (p-value 4.7E-53).

> "In the Slide-Level evaluation, LECTOR achieved an average F-score of 61.8% across 390 slides (on average 3 of the 5 empirical keyphrases were correctly extracted)."

## Discussion


## Related Claims
- [State-of-the-art embedding-based keyphrase models degrade on lecture slides while TF-IDF generalizes better to them](embedding-keyphrase-models-degrade-lecture-slides.md) — related
- [LECTOR achieves the highest keyphrase extraction performance among compared models at @15, Best and Mean evaluations on lecture slides](lector-highest-keyphrase-f1-lecture-slides.md) — related
