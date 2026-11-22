---
type: claim
title: GPT-4o-RAG significantly outperformed GPT-4o in Applied Nutrition and Clinical Nutrition categories but was non-significantly lower in the other five categories it trailed in
description: GPT-4o-RAG significantly outperformed GPT-4o in Applied Nutrition and Clinical Nutrition categories but was non-significantly lower in the other five categories it trailed in
id: gpt4o-rag-category-advantage-clinical-nutrition
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: mixed
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

# GPT-4o-RAG significantly outperformed GPT-4o in Applied Nutrition and Clinical Nutrition categories but was non-significantly lower in the other five categories it trailed in

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In Applied Nutrition, GPT-4o-RAG scored 92.9% ± 2.4% versus GPT-4o's 82.5% ± 1.9% (p < 0.001); in Clinical Nutrition, 85.4% ± 1.1% versus 81.2% ± 1.9% (p = 0.03). [→ Ishikawa Yu 2025](#ishikawa-yu-2025)
`q2 i?` GPT-4o-RAG showed lower accuracy than GPT-4o in the remaining five categories, with none of those differences reaching statistical significance, and no significant variance differences in any of the 10 categories. [→ Ishikawa Yu 2025 (2)](#ishikawa-yu-2025-2)

## Evidence

### Ishikawa Yu 2025

Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro. (2025). Performance of GPT-4o combined with retrieval-augmented generation on nutritionist licensing exam questions. Endocrine Journal. https://doi.org/10.1507/endocrj.EJ25-0201

`q2 · i?` · `design · r2`

Category-level comparison of average accuracy across the 10 examination domains (Fig. 4). The article reports significant advantages for GPT-4o-RAG over GPT-4o in Applied Nutrition (p < 0.001) and Clinical Nutrition (p = 0.03); no effect sizes are printed.

> "the differences in Applied Nutrition (GPT-4o-RAG: 92.9% ± 2.4% vs. GPT-4o: 82.5% ± 1.9%, p < 0.001) and Clinical Nutrition (GPT-4o-RAG: 85.4% ± 1.1% vs. GPT-4o: 81.2% ± 1.9%, p = 0.03) were significant."

### Ishikawa Yu 2025 (2)

Ishikawa Yu, Higashi Akitaka, Arai Nozomu, Ozo Daisuke, Hasegawa Wataru, Imamura Tetsuya, Matsumoto Zenbei, Nambo Hidetaka, Karashima Shigehiro. (2025). Performance of GPT-4o combined with retrieval-augmented generation on nutritionist licensing exam questions. Endocrine Journal. https://doi.org/10.1507/endocrj.EJ25-0201

`q2 · i?` · `design · r2`

Same category-level analysis: in the five categories where GPT-4o-RAG trailed GPT-4o, differences were not statistically significant, and the article reports no significant variance differences between the two models in any of the 10 categories.

> "Conversely, GPT-4o-RAG showed lower accuracy than GPT-4o in the remaining five categories, but none of these differences reached statistical significance."

## Discussion


## Related Claims
- [In a simulated nutrition counseling scenario, GPT-4o-RAG generated fewer but more concise responses than GPT-4o and GPT-4o-mini](gpt4o-rag-concise-counseling-responses.md) — related
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
- [GPT-4o-RAG produced significantly lower response variance and significantly higher response consistency than GPT-4o and GPT-4o-mini](gpt4o-rag-lower-variance-higher-consistency.md) — related
- [All three evaluated LLMs exceeded the 60% passing threshold on the Japanese National Examination for Registered Dietitians, with GPT-4o-RAG numerically highest but not significantly more accurate than GPT-4o](gpt4o-rag-exceeds-dietitian-exam-passing-threshold.md) — related
