---
type: claim
title: "LECTOR achieves the highest keyphrase extraction performance among compared models at @15, Best and Mean evaluations on lecture slides"
description: "LECTOR achieves the highest keyphrase extraction performance among compared models at @15, Best and Mean evaluations on lecture slides"
id: lector-highest-keyphrase-f1-lecture-slides
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: erwin-daniel-lópez-zapata-2025
    resource: "https://doi.org/10.1007/s40593-025-00478-6"
    title: "Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6"
    author: Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LECTOR achieves the highest keyphrase extraction performance among compared models at @15, Best and Mean evaluations on lecture slides

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the technical evaluation on 2,255 lecture slides, LECTOR achieved the highest F1-scores at @15, Best and Mean (33.44%, 37.92%, 20.14%), outperforming TF-IDF, Binary score, TextRank and AttentionRank. [→ Erwin Daniel López Zapata 2025](#erwin-daniel-lopez-zapata-2025)

## Evidence

### Erwin Daniel López Zapata 2025

Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6

`q2 · i?` · `design · r2`

Technical evaluation comparing LECTOR against TF-IDF, Binary score, TextRank and AttentionRank on keyphrase extraction from 2,255 lecture slides, with performance measured against syllabus ground-truth keyphrases; LECTOR "achieves the highest performance at @15, “Best” and “Mean”".

> "Specifically, LECTOR achieves the highest performance at @15, “Best” and “Mean” with F1-scores of 33.44%, 37.92%, and 20.14%, respectively."

## Discussion


## Related Claims
- [State-of-the-art embedding-based keyphrase models degrade on lecture slides while TF-IDF generalizes better to them](embedding-keyphrase-models-degrade-lecture-slides.md) — reports the opposite
- [Students rated LECTOR-extracted keyphrases as more relevant than TF-IDF-extracted keyphrases in a human evaluation](lector-human-evaluation-outperforms-tfidf.md) — related
