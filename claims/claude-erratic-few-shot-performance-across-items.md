---
type: claim
title: "Claude's few-shot scoring behaved erratically across items: best few-shot model on Item 1 but by far the worst model on Item 2"
description: "Claude's few-shot scoring behaved erratically across items: best few-shot model on Item 1 but by far the worst model on Item 2"
id: claude-erratic-few-shot-performance-across-items
status: draft
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
    kind: causal
    rigour: 1
---

# Claude's few-shot scoring behaved erratically across items: best few-shot model on Item 1 but by far the worst model on Item 2

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Claude's performance oscillated dramatically between the two conceptually similar biology items, unlike the consistent item patterns of the human rater, fine-tuned, and GPT-family models. [→ Abigail Victoria Gurin Schleifer 2026](#abigail-victoria-gurin-schleifer-2026)

## Evidence

### Abigail Victoria Gurin Schleifer 2026

Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647 [doi:10.48550/arxiv.2605.07647](https://doi.org/10.48550/arxiv.2605.07647)

`q2 · i?` · `causal · r1`

Cross-item comparison of scoring mechanisms (Results): "Claude’s performance oscillates dramatically – it is the best few-shot model for Item 1 but is by far the worst model for Item 2", while H2, fine-tuned and GPT-family patterns were consistent across items.

> "Claude’s performance oscillates dramatically – it is the best few-shot model for Item 1 but is by far the worst model for Item 2."

## Discussion


## Related Claims
- [AI scoring shows a quality-conditioned pattern: strong agreement on fully correct and fully incorrect responses but substantial degradation on mid-range responses](ai-mid-range-scoring-degradation-u-shape.md) — related
- LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst — related
- [The second human expert showed the highest and most stable agreement with the gold-standard rater, with no mid-range degradation across the response quality spectrum](human-highest-stable-agreement-across-quality-range.md) — related
