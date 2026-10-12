---
type: claim
title: SHAP analysis shows praise mentions raise LLM-assigned scores while criticism mentions lower them
description: SHAP analysis shows praise mentions raise LLM-assigned scores while criticism mentions lower them
id: shap-praise-raises-criticism-lowers-llm-scores
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
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

# SHAP analysis shows praise mentions raise LLM-assigned scores while criticism mentions lower them

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` In proxy XGBoost models predicting LLM scores from trait-specific praise and criticism counts, praise-related features produce positive SHAP values and criticism-related features negative ones. [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714

`q2 · i?` · `associational · r2`

XGBoost proxy models trained per dataset and LLM on counts of positive and negative trait mentions, with SHAP used to estimate feature contributions (Figure 13 for Llama models on ASAP Task 7). Similar trends were reported for GPT models and other datasets in an appendix.

> "These results suggest that LLM-assigned scores are coherent with the evaluative signals expressed in their feedback: praise-related mentions increase predicted scores, whereas criticism-related mentions decrease them."

## Discussion


## Related Claims
- [LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise](llm-feedback-sentiment-tracks-scores.md) — possibly the same claim (merge candidate)
- [Different LLMs rely on different subsets of rubric traits when assigning essay scores](llms-weight-rubric-traits-differently.md) — related
