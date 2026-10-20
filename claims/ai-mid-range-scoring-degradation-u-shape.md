---
type: claim
title: "AI scoring shows a quality-conditioned pattern: strong agreement on fully correct and fully incorrect responses but substantial degradation on mid-range responses"
description: "AI scoring shows a quality-conditioned pattern: strong agreement on fully correct and fully incorrect responses but substantial degradation on mid-range responses"
id: ai-mid-range-scoring-degradation-u-shape
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: abigail-victoria-gurin-schleifer-2026
    resource: "https://doi.org/10.48550/arxiv.2605.07647"
    title: "Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647 [doi:10.48550/arxiv.2605.07647](https://doi.org/10.48550/arxiv.2605.07647)"
    author: Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: abigail-victoria-gurin-schleifer-2026-2
    resource: "https://arxiv.org/abs/2605.07647"
    title: "Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647"
    author: Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AI scoring shows a quality-conditioned pattern: strong agreement on fully correct and fully incorrect responses but substantial degradation on mid-range responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The authors summarise AI-model performance on the extremes of the quality spectrum (best and worst responses) as excellent regardless of model type and amount of task-specific data, with exceptions in their own table: two-shot GPT-4o on Item 2 at the low end, and Claude Opus 4.5 on Item 2, which was far off at every score level. [→ Abigail Victoria Gurin Schleifer 2026](#abigail-victoria-gurin-schleifer-2026)
`q2 i?` All few-shot models suffered substantial mid-range degradation, with average distance of more than two categories from the gold label at score levels 4-7 in all but one of 48 GPT-model results. [→ Abigail Victoria Gurin Schleifer 2026 (2)](#abigail-victoria-gurin-schleifer-2026-2)

## Evidence

### Abigail Victoria Gurin Schleifer 2026

Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647 [doi:10.48550/arxiv.2605.07647](https://doi.org/10.48550/arxiv.2605.07647)

`q2 · i?` · `design · r2`

Score-level analysis of test responses (Results, Table 1 and Figure 1): the authors report "excellent AI-model performance on the extremes – best and worst quality responses". Table 1 shows exceptions: on Item 2, two-shot GPT-4o averaged 1.50–2.29 categories from the gold label at score levels 1–2 (the authors name it as the exception at the low end), and Claude Opus 4.5 averaged 5.57, 4.90 and 5.14 categories at score levels 0–2, which the authors describe as erratic (best few-shot model on Item 1, by far the worst on Item 2).

> "Analyzing the results by score level (number of correct categories out of 10), we observe excellent AI-model performance on the extremes – best and worst quality responses – regardless of model-type and amount of task-specific data."

### Abigail Victoria Gurin Schleifer 2026 (2)

Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647

`q2 · i?` · `design · r2`

Score-level analysis of mid-range responses (Results): "all but one of the 6×4×2 = 48 results show average distance of more than two categories from the gold label" across score levels 4-7 and both items.

> "For all six GPT models, for each of the four score levels 4-7, for both items, all but one of the 6×4×2 = 48 results show average distance of more than two categories from the gold label."

## Discussion


## Related Claims
- [Task Specific Adaptation Conditions Mid Range Degradation](task-specific-adaptation-conditions-mid-range-degradation.md)
- The second human expert showed the highest and most stable agreement with the gold-standard rater, with no mid-range degradation across the response quality spectrum — related
- [On fully correct responses, the GPT few-shot models outperformed the fine-tuned models, averaging less than one category distance from the gold score](gpt-outperforms-finetuned-on-fully-correct-responses.md) — a narrower finding that bears on this claim
- [Claude's few-shot scoring behaved erratically across items: best few-shot model on Item 1 but by far the worst model on Item 2](claude-erratic-few-shot-performance-across-items.md) — related
- [MLS-WEPs improved the quality of written explanations, with larger gains in fully correct explanations and reduced blank and concept-irrelevant responses](mls-weps-improved-explanation-quality.md) — related
