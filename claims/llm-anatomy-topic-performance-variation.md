---
type: claim
title: "LLM performance on anatomy MCQs varies significantly across anatomical topics, with Head & Neck and Abdomen highest and Upper Limb lowest"
description: "LLM performance on anatomy MCQs varies significantly across anatomical topics, with Head & Neck and Abdomen highest and Upper Limb lowest"
id: llm-anatomy-topic-performance-variation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: bolgova-olena-2025
    resource: "https://doi.org/10.1038/s41598-025-22437-w"
    title: "Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w"
    author: Bolgova Olena, Mavrych Volodymyr
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: bolgova-olena-2025-2
    resource: "https://doi.org/10.1038/s41598-025-22437-w"
    title: "Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w"
    author: Bolgova Olena, Mavrych Volodymyr
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: bolgova-olena-2025-3
    resource: "https://doi.org/10.1038/s41598-025-22437-w"
    title: "Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w"
    author: Bolgova Olena, Mavrych Volodymyr
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM performance on anatomy MCQs varies significantly across anatomical topics, with Head & Neck and Abdomen highest and Upper Limb lowest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all current LLMs, Head & Neck (79.5%) and Abdomen (78.7%) were the best topics and Upper Limb the lowest (72.9%), with statistically significant differences between topics (all p-values < 0.001). [→ Bolgova Olena 2025](#bolgova-olena-2025)
`q2 i?` Chi-square analysis showed all LLMs deviated significantly from uniform performance across topics and models (χ2 = 182.11–518.32, p < 0.001). [→ Bolgova Olena 2025 (2)](#bolgova-olena-2025-2)
`q2 i?` The 2.5% of questions never answered correctly by any LLM were all high-level critical-thinking questions distributed among topics. [→ Bolgova Olena 2025 (3)](#bolgova-olena-2025-3)

## Evidence

### Bolgova Olena 2025

Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w

`q2 · i?` · `associational · r1`

Item analysis of topic-wise accuracy across all four current LLMs on the 325-question benchmark. The article reports "statistically significant differences between different topics' performances across all LLMs (all p-values < 0.001)".

> "General item analysis revealed that Head & Neck and Abdomen were the two best categories, with the average results for these LLMs being 79.5% and 78.7%, respectively. In contrast, the lowest results were recorded for Upper Limb questions − 72.9%."

### Bolgova Olena 2025 (2)

Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w

`q2 · i?` · `design · r2`

Omnibus chi-square analysis of performance across topics and models; the article states the null hypothesis of uniform performance can be rejected. Highest variation was for Upper limb questions (χ2 = 243.88), lowest for Back (χ2 = 109.25).

> "Chi-square analysis revealed that all LLMs showed statistically significant deviation from the expected uniform distribution of correct answers χ2 = 182.11–518.32 (p < 0.001)."

### Bolgova Olena 2025 (3)

Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w

`q2 · i?` · `design · r2`

Descriptive item analysis of the eight questions no current model ever answered correctly across three attempts, characterized by the authors as high-level critical-thinking questions.

> "2.5% (8/325) of the questions were never answered correctly by any LLM. Item analysis revealed that all of them were high-level critical-thinking questions, equally (1–2) distributed among the different topics."

## Discussion


## Related Claims
- [Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o](claude-copilot-gemini-topic-strengths-reliability.md) — related
- [LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference](subject-area-accuracy-variation-dus-llms.md) — a broader claim this one bears on
- [Practical exam scores are higher for anatomical regions with online image support than for unsupported regions within the same intervention groups](intra-group-image-supported-blocks-score-higher.md) — related
