---
type: claim
title: Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other
description: Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other
id: llm-essay-scoring-weak-human-agreement
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: jerin-george-mathew-2026
    resource: "https://arxiv.org/abs/2603.23714"
    title: "Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714"
    author: Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Across ASAP and DREsS datasets, LLM-human score agreement (QWK below 0.30 on ASAP; at most 0.34 on DREsS) is substantially weaker than human inter-rater agreement (QWK 0.72). [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714

`q2 · i?` · `associational · r2`

Evaluation of six GPT and Llama models prompted out-of-the-box to score essays on ASAP Tasks 1 and 7 and DREsS, compared against human ratings using QWK, Pearson correlation, and normalized MAE. Human raters reached "QW K= 0.72" while all LLMs stayed below 0.30 QWK on ASAP.

> "For the ASAP datasets, the agreement between the two human raters is relatively high (QW K= 0.72), indicating strong inter-rater reliability. In contrast, all LLMs achieve considerably lower agreement with human scores, with QWK values below 0.30 across models and tasks."

## Discussion


## Related Claims
- [Newer LLM generations do not consistently agree better with human essay graders](no-consistent-generational-improvement-llm-grading.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Few-shot prompting modestly improves LLM-human score agreement, inconsistently across datasets and models](few-shot-prompting-inconsistent-grading-gains.md) — related
- [Human inter-rater agreement on the writing rubric is imperfect: no rubric item reaches full agreement and the most discrepant rater generally falls below 80%](human-inter-rater-agreement-imperfect-upper-bound.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](llm-high-consensus-agreement-circularity-risk.md) — related
