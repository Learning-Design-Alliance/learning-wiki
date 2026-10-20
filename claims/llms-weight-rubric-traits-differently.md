---
type: claim
title: Different LLMs rely on different subsets of rubric traits when assigning essay scores
description: Different LLMs rely on different subsets of rubric traits when assigning essay scores
id: llms-weight-rubric-traits-differently
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: jerin-george-mathew-2026
    resource: "https://doi.org/10.48550/arxiv.2603.23714"
    title: "Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)"
    author: Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: jerin-george-mathew-2026-2
    resource: "https://arxiv.org/abs/2603.23714"
    title: "Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714"
    author: Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Different LLMs rely on different subsets of rubric traits when assigning essay scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Trait mentions in LLM feedback are not uniformly distributed, with praise concentrated on a few traits and criticism spread more broadly, varying across models and rubric structures. [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)
`q2 i?` SHAP importance differs by model: GPT-3.5 relied most on negative conventions, style, and organization mentions, while GPT-4 was dominated by positive ideas mentions. [→ Jerin George Mathew 2026 (2)](#jerin-george-mathew-2026-2)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)

`q2 · i?` · `associational · r2`

Distribution of trait-specific praise and criticism mentions across models for ASAP Task 1, ASAP Task 7, and DREsS (Figures 14-16). On ASAP Task 7, GPT-4 focused on ideas around 60% while Llama 2 produced more style praise around 50%.

> "LLMs do not evaluate rubric traits uniformly - praise tends to concentrate on a few traits while criticism is more broadly distributed, with trait emphasis varying across models and rubric structures."

### Jerin George Mathew 2026 (2)

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714

`q2 · i?` · `associational · r2`

Average absolute SHAP values from the proxy XGBoost models for GPT models on ASAP Task 7 (Figure 17), showing differing trait weighting; GPT-5 showed a more balanced pattern combining ideas praise with style and organization criticism.

> "For GPT-3.5, the most influential features correspond to negative mentions ofconventions,style, andorganization, suggestingthatthemodelreliesstronglyoncriticismrelated to writing mechanics and structure. In contrast, GPT-4 shows a highly skewed importance distribution in which positive mentions ofideasdominate the score prediction."

## Discussion

## Related Claims

- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — the general claim this finding bears on, with the studies behind it

- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — the general claim this finding bears on, with the studies behind it
- [LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise](llm-feedback-sentiment-tracks-scores.md) — related
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](prompting-limited-uneven-proficiency-control-writing-simulation.md) — related
