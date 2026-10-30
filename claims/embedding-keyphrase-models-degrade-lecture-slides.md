---
type: claim
title: State-of-the-art embedding-based keyphrase models degrade on lecture slides while TF-IDF generalizes better to them
description: State-of-the-art embedding-based keyphrase models degrade on lecture slides while TF-IDF generalizes better to them
id: embedding-keyphrase-models-degrade-lecture-slides
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
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: erwin-daniel-lópez-zapata-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00478-6"
    title: "Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6"
    author: Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# State-of-the-art embedding-based keyphrase models degrade on lecture slides while TF-IDF generalizes better to them

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` TF-IDF achieves higher F1-scores on lecture slides than on general documents, indicating robustness across domains. [→ Erwin Daniel López Zapata 2025](#erwin-daniel-lopez-zapata-2025)
`q2 i?` AttentionRank shows a pronounced drop in performance on lecture slides compared with its results on general NLP datasets. [→ Erwin Daniel López Zapata 2025 (2)](#erwin-daniel-lopez-zapata-2025-2)

## Evidence

### Erwin Daniel López Zapata 2025

Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6

`q2 · i?` · `design · r2`

Comparison of F1-scores for keyphrase extraction on benchmark general-document datasets versus the lecture-slides dataset (Table 6); the article attributes TF-IDF's result to "TF-IDF's robustness and generalizability across domains".

> "TF-IDF, despite being a simple statistical model, achieves higher performance on lecture slides than on general documents (Table 6)."

### Erwin Daniel López Zapata 2025 (2)

Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6

`q2 · i?` · `design · r2`

Same benchmark comparison (Table 6): AttentionRank's F1 at @5 falls from 24.02 on general documents to 17.25 on lecture slides; the article concludes that "recent advances in unsupervised keyphrase extraction may not adapt well to educational contexts".

> "This suggests that recent advances in unsupervised keyphrase extraction may not adapt well to educational contexts, especially for extracting key concepts from lecture slides."

## Discussion


## Related Claims
- [LECTOR achieves the highest keyphrase extraction performance among compared models at @15, Best and Mean evaluations on lecture slides](lector-highest-keyphrase-f1-lecture-slides.md) — reports the opposite
- [Students rated LECTOR-extracted keyphrases as more relevant than TF-IDF-extracted keyphrases in a human evaluation](lector-human-evaluation-outperforms-tfidf.md) — related
- [Under the fixed protocol, hosted LLMs produce the largest gain on Spanish thematic classification, with thematic macro F1 rising from 0.46 (TF-IDF) to roughly 0.82-0.86 for the two hosted LLMs](llms-largest-gain-spanish-thematic-macro-f1.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
