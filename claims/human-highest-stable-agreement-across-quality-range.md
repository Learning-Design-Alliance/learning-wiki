---
type: claim
title: The second human expert showed the highest and most stable agreement with the gold-standard rater, with no mid-range degradation across the response quality spectrum
description: The second human expert showed the highest and most stable agreement with the gold-standard rater, with no mid-range degradation across the response quality spectrum
id: human-highest-stable-agreement-across-quality-range
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
    kind: associational
    rigour: 2
---

# The second human expert showed the highest and most stable agreement with the gold-standard rater, with no mid-range degradation across the response quality spectrum

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` On average and across score levels, the second human rater agreed most with the expert gold labels, ahead of the fine-tuned BERT models and the few-shot LLMs. [→ Abigail Victoria Gurin Schleifer 2026](#abigail-victoria-gurin-schleifer-2026)
`q2 i?` Human-human agreement showed no clear mid-range degradation, remaining stable across the response quality range unlike the AI raters. [→ Abigail Victoria Gurin Schleifer 2026 (2)](#abigail-victoria-gurin-schleifer-2026-2)

## Evidence

### Abigail Victoria Gurin Schleifer 2026

Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647 [doi:10.48550/arxiv.2605.07647](https://doi.org/10.48550/arxiv.2605.07647)

`q2 · i?` · `design · r2`

Score-level comparison of raters against Rater1 gold labels on two biology items (Results, Table 1): H2 ranked highest — "followed by the fine-tuned BERT-based models, followed by the LLMs in few-shot mode".

> "On average and across score levels, H2 had the highest agreement with the expert, followed by the fine-tuned BERT-based models, followed by the LLMs in few-shot mode."

### Abigail Victoria Gurin Schleifer 2026 (2)

Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647

`q2 · i?` · `associational · r2`

Score-level analysis of the test set (Results): the second human rater "does not show a clear pattern of degradation in agreement with the gold labels in the middle of the score range", unlike all AI models.

> "In contrast, the human rater H2 does not show a clear pattern of degradation in agreement with the gold labels in the middle of the score range."

## Discussion


## Related Claims
- [AI scoring shows a quality-conditioned pattern: strong agreement on fully correct and fully incorrect responses but substantial degradation on mid-range responses](ai-mid-range-scoring-degradation-u-shape.md) — related
- [Claude's few-shot scoring behaved erratically across items: best few-shot model on Item 1 but by far the worst model on Item 2](claude-erratic-few-shot-performance-across-items.md) — related
- [Mid-range degradation is conditioned on task-specific adaptation: it is most severe for few-shot LLMs with few examples, decreases with more task-specific data, and is mildest for the fine-tuned encoder](task-specific-adaptation-conditions-mid-range-degradation.md) — related
