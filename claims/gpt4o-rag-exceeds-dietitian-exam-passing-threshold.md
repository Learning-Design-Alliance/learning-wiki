---
type: claim
title: "All three evaluated LLMs exceeded the 60% passing threshold on the Japanese National Examination for Registered Dietitians, with GPT-4o-RAG numerically highest but not significantly more accurate than GPT-4o"
description: "All three evaluated LLMs exceeded the 60% passing threshold on the Japanese National Examination for Registered Dietitians, with GPT-4o-RAG numerically highest but not significantly more accurate than GPT-4o"
id: gpt4o-rag-exceeds-dietitian-exam-passing-threshold
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
---

# All three evaluated LLMs exceeded the 60% passing threshold on the Japanese National Examination for Registered Dietitians, with GPT-4o-RAG numerically highest but not significantly more accurate than GPT-4o

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4o-mini (70.0% ± 1.4%) scored significantly lower than GPT-4o (82.1% ± 1.0%) and GPT-4o-RAG (83.5% ± 0.3%), while GPT-4o-RAG's accuracy advantage over GPT-4o was not statistically significant (p = 0.12). [→ Ishikawa Yu 2025](#ishikawa-yu-2025)

## Evidence

### Ishikawa Yu 2025

Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro. (2025). Performance of GPT-4o combined with retrieval-augmented generation on nutritionist licensing exam questions. Endocrine Journal. https://doi.org/10.1507/endocrj.EJ25-0201

`q2 · i?` · `design · r2`

Performance evaluation of three LLMs answering 599 publicly available multiple-choice questions from the 2022–2024 Japanese national dietitian examinations, five responses per question per model, scored against official MHLW answers. The article reports GPT-4o-mini was "significantly lower (p < 0.001)" and that between GPT-4o and GPT-4o-RAG "No significant difference was observed" (p = 0.12); equivalence was not tested.

> "GPT-4o-mini achieved an accuracy rate of 70.0% ± 1.4%, which was significantly lower (p < 0.001) than that of both GPT-4o (82.1% ± 1.0%) and GPT-4o-RAG (83.5% ± 0.3%). No significant difference was observed between GPT-4o and GPT-4o-RAG (p = 0.12)."

## Discussion


## Related Claims
- [In a simulated nutrition counseling scenario, GPT-4o-RAG generated fewer but more concise responses than GPT-4o and GPT-4o-mini](gpt4o-rag-concise-counseling-responses.md) — related
- [GPT-4 and GPT-4o accuracy exceeds the NMLE passing threshold and the typical national pass rate](gpt4-gpt4o-exceed-nmle-passing-threshold.md) — related
- [All four LLMs showed a decline in accuracy on the Chinese-language NMLE, with GPT-4, GPT-3.5 and Bard failing to reach the 70% accuracy threshold](llm-accuracy-declines-on-chinese-nmle.md) — related
- [GPT-4o-RAG produced significantly lower response variance and significantly higher response consistency than GPT-4o and GPT-4o-mini](gpt4o-rag-lower-variance-higher-consistency.md) — related
- [TF-IDF analysis associated GPT-4o-RAG's incorrect answers with numerical terms about nutrient and energy intake](tfidf-incorrect-answers-numerical-terms.md) — related
- [GPT-4o-RAG significantly outperformed GPT-4o in Applied Nutrition and Clinical Nutrition categories but was non-significantly lower in the other five categories it trailed in](gpt4o-rag-category-advantage-clinical-nutrition.md) — related
