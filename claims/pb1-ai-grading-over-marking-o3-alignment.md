---
type: claim
title: In PB1 AI grading with a mark scheme, models showed systemic over-marking, with ChatGPT-o3 the only evaluator closely aligned with human marks
description: In PB1 AI grading with a mark scheme, models showed systemic over-marking, with ChatGPT-o3 the only evaluator closely aligned with human marks
id: pb1-ai-grading-over-marking-o3-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jonah-l-donaldson-2026
    resource: "https://doi.org/10.48550/arXiv.2605.23660"
    title: "Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)"
    author: Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# In PB1 AI grading with a mark scheme, models showed systemic over-marking, with ChatGPT-o3 the only evaluator closely aligned with human marks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` ChatGPT-o3 achieved the highest Pearson correlation with human graders (r = 0.8379) and an R² of 0.7022, while the cohort showed high Y-intercepts and shallow gradients indicating grade inflation. [→ Jonah L. Donaldson 2026](#jonah-l-donaldson-2026)

## Evidence

### Jonah L. Donaldson 2026

Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)

`q2 · i3` · `design · r2`

PB1 Stage III regression analysis in which six LLMs graded ChatGPT-4o solutions for 18 Set B questions with the mark scheme provided. The article reports ChatGPT-o3's Pearson correlation r = 0.8379 (R² of 0.7022), the highest in the cohort, versus systemic bias toward grade inflation and compression across the cohort.

> "ChatGPT-o3 emerges as the outlier, showing the highest alignment with human graders. With the highest Pearson correlation (0.8379) and anR 2 of 0.7022, it accounts for over 70% of the variance in human marks."

## Discussion


## Related Claims
- [Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades](mark-scheme-improves-llm-grading.md) — reports the opposite
- [With individualised grading contexts, Generation 5 models aligned strongly with human grading, Gemini 3.0 Pro reaching r = 0.9191 and MAE of 7.62%](gen5-individualised-grading-alignment.md) — related
- [LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans](llm-marking-concordance-with-humans-about-half.md) — related
- [Blind AI essay marking is harsher and more variable than human marking, and adding a marking scheme does not improve rank-order agreement](llm-essay-marking-harsh-low-rank-agreement.md) — related
