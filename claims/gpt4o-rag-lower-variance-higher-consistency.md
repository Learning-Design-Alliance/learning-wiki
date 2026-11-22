---
type: claim
title: GPT-4o-RAG produced significantly lower response variance and significantly higher response consistency than GPT-4o and GPT-4o-mini
description: GPT-4o-RAG produced significantly lower response variance and significantly higher response consistency than GPT-4o and GPT-4o-mini
id: gpt4o-rag-lower-variance-higher-consistency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: ishikawa-yu-2025
    resource: "https://doi.org/10.1507/endocrj.EJ25-0201"
    title: "Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro. (2025). Performance of GPT-4o combined with retrieval-augmented generation on nutritionist licensing exam questions. Endocrine Journal. https://doi.org/10.1507/endocrj.EJ25-0201"
    author: Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ishikawa-yu-2025-2
    resource: "https://doi.org/10.1507/endocrj.EJ25-0201"
    title: "Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro. (2025). Performance of GPT-4o combined with retrieval-augmented generation on nutritionist licensing exam questions. Endocrine Journal. https://doi.org/10.1507/endocrj.EJ25-0201"
    author: Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o-RAG produced significantly lower response variance and significantly higher response consistency than GPT-4o and GPT-4o-mini

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The variance of GPT-4o-RAG accuracy (0.08) was significantly smaller than that of GPT-4o (0.91) and GPT-4o-mini (1.86). [→ Ishikawa Yu 2025](#ishikawa-yu-2025)
`q2 i?` GPT-4o-RAG's mean agreement rate (97.3 ± 8.9%) was significantly higher than GPT-4o's (95.2 ± 11.6%) and GPT-4o-mini's (91.2 ± 14.4%). [→ Ishikawa Yu 2025 (2)](#ishikawa-yu-2025-2)

## Evidence

### Ishikawa Yu 2025

Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro. (2025). Performance of GPT-4o combined with retrieval-augmented generation on nutritionist licensing exam questions. Endocrine Journal. https://doi.org/10.1507/endocrj.EJ25-0201

`q2 · i?` · `design · r2`

F-test comparison of accuracy variance across the five repeated answer runs per model on the 599 exam questions. The article reports GPT-4o-RAG variance of 0.08 versus 0.91 for GPT-4o (p = 0.03) and 1.86 for GPT-4o-mini (p < 0.01); no effect size is printed.

> "The variance of GPT-4o-RAG was 0.08, which was smaller than that of GPT-4o (0.91, F (4, 4) = 0.08, p = 0.03) and GPT-4o-mini (1.86, F (4, 4) = 0.04, p < 0.01)."

### Ishikawa Yu 2025 (2)

Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro. (2025). Performance of GPT-4o combined with retrieval-augmented generation on nutritionist licensing exam questions. Endocrine Journal. https://doi.org/10.1507/endocrj.EJ25-0201

`q2 · i?` · `design · r2`

Consistency was computed as the agreement rate with the mode across five independent responses per question, averaged over all questions. GPT-4o-RAG reached "97.3 ± 8.9%", significantly higher than both comparators (p < 0.001); no standardized effect size is printed.

> "The average response consistency (agreement rate) of GPT-4o-RAG was 97.3 ± 8.9%, which was significantly higher than that of GPT-4o (95.2 ± 11.6%, p < 0.001) and GPT-4o-mini (91.2 ± 14.4%, p < 0.001)."

## Discussion


## Related Claims
- [In a simulated nutrition counseling scenario, GPT-4o-RAG generated fewer but more concise responses than GPT-4o and GPT-4o-mini](gpt4o-rag-concise-counseling-responses.md) — related
- [All three evaluated LLMs exceeded the 60% passing threshold on the Japanese National Examination for Registered Dietitians, with GPT-4o-RAG numerically highest but not significantly more accurate than GPT-4o](gpt4o-rag-exceeds-dietitian-exam-passing-threshold.md) — related
- [GPT-4o-RAG significantly outperformed GPT-4o in Applied Nutrition and Clinical Nutrition categories but was non-significantly lower in the other five categories it trailed in](gpt4o-rag-category-advantage-clinical-nutrition.md) — related
- [TF-IDF analysis associated GPT-4o-RAG's incorrect answers with numerical terms about nutrient and energy intake](tfidf-incorrect-answers-numerical-terms.md) — related
