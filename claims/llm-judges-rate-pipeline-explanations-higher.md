---
type: claim
title: LLM judges rate pipeline-generated explanations higher than direct prompting and hand-crafted templates across USML domains
description: LLM judges rate pipeline-generated explanations higher than direct prompting and hand-crafted templates across USML domains
id: llm-judges-rate-pipeline-explanations-higher
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: lun-ai-2025
    resource: "https://doi.org/10.48550/arXiv.2509.00961"
    title: "Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)"
    author: Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
  - id: lun-ai-2025-2
    resource: "https://doi.org/10.48550/arXiv.2509.00961"
    title: "Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)"
    author: Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: lun-ai-2025-3
    resource: "https://doi.org/10.48550/arXiv.2509.00961"
    title: "Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)"
    author: Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM judges rate pipeline-generated explanations higher than direct prompting and hand-crafted templates across USML domains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Coding LLMs help reasoning LLMs generate higher-rated explanations, particularly when programs have less meaningful names. [→ Lun Ai 2025](#lun-ai-2025)
`q2 i?` Multiple coding models and multiple responses improve explanation rating over a single coding LLM. [→ Lun Ai 2025 (2)](#lun-ai-2025-2)
`q2 i?` The explanation pipeline provides higher-rated explanations than hand-crafted templates, including in game playing and algorithm discovery domains (p < 0.001). [→ Lun Ai 2025 (3)](#lun-ai-2025-3)

## Evidence

### Lun Ai 2025

Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)

`q2 · i?` · `causal · r?`

Pipeline validation experiment: explanations generated across 14 conditions with three repetitions, scored three times per judge (3024 circuit scores), analyzed with one-way ANOVA and post-hoc Tukey's HSD. Ratings are LLM-judge scores, not human outcomes.

> "Results.InFigure4a,LLMjudgesconsiderthepipelinewithnamedoranonymised ILP-learned programs superior to direct prompting of a reasoning LLM with anonymised programs."

### Lun Ai 2025 (2)

Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)

`q2 · i?` · `causal · r2`

Consensus comparison in the pipeline validation (Figure 4c); the authors note this aligns with past work where consensus between multiple LLMs results in higher-quality responses. LLM-judged scores only.

> "In Figure 4c, LLM judges consider that using multiple coding LLMs produces better explanations than using just a single coding LLM."

### Lun Ai 2025 (3)

Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)

`q2 · i?` · `causal · r2`

Appendix B evaluation applying the pipeline to game playing and algorithm discovery USML tasks; the article reports statistically significant differences (p <0.001) in LLM-judged scores favoring the pipeline over hand-crafted templates. The article's text contains broken spacing in this passage.

> "Across both domains, pipeline-generated explanations consistently receive higher LLM-judged scores than hand-crafted templatesfrompriorwork(Figure6aandFigure6b),withstatisticallysignificant differences (p <0.001)"

## Discussion


## Related Claims
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Pipeline-generated LLM explanations of an ILP-learned active learning strategy do not improve human task performance over self-learning in any of three domains](llm-pipeline-explanations-no-advantage-over-self-learning.md) — related
- [LLM quality metrics do not predict human learning outcomes from explanations](llm-quality-metrics-do-not-predict-human-learning.md) — related
