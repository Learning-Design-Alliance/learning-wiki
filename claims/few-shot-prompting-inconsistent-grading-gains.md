---
type: claim
title: Few-shot prompting modestly improves LLM-human score agreement, inconsistently across datasets and models
description: Few-shot prompting modestly improves LLM-human score agreement, inconsistently across datasets and models
id: few-shot-prompting-inconsistent-grading-gains
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: jerin-george-mathew-2026
    resource: "https://doi.org/10.48550/arxiv.2603.23714"
    title: "Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)"
    author: Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Few-shot prompting modestly improves LLM-human score agreement, inconsistently across datasets and models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Prompt variants including a student-grade variant and a few-shot variant with two example essays produced modest, inconsistent improvements in agreement with human scores. [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)

`q2 · i?` · `causal · r1`

Evaluation of two prompt variants beyond the base template: one specifying the student's grade level and one including two example essays with human-assigned scores. Improvements appeared across QWK, Pearson correlation, and MAE in some cases, particularly for few-shot, but not consistently.

> "Prompt variants such as few-shot prompting can modestly improve LLM-human score agreement, but these gains are not consistent across datasets or models."

## Discussion


## Related Claims
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [Newer LLM generations do not consistently agree better with human essay graders](no-consistent-generational-improvement-llm-grading.md) — related
