---
type: claim
title: Automated faithfulness evaluation was sensitive to the evaluator model, with Gemini 2.5 Flash scoring 0.31 while GPT-4o-mini and Claude 3 Haiku each scored 0.77
description: Automated faithfulness evaluation was sensitive to the evaluator model, with Gemini 2.5 Flash scoring 0.31 while GPT-4o-mini and Claude 3 Haiku each scored 0.77
id: llm-judge-faithfulness-sensitivity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yang-2026
    resource: "https://doi.org/10.48550/arXiv.2609.19429"
    title: "Yang, F.; Wu, J.; Tian, Y.; and Zhang, J. (2026). CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education. [doi:10.48550/arXiv.2609.19429](https://doi.org/10.48550/arXiv.2609.19429)"
    author: Yang, F.; Wu, J.; Tian, Y.; and Zhang, J.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Automated faithfulness evaluation was sensitive to the evaluator model, with Gemini 2.5 Flash scoring 0.31 while GPT-4o-mini and Claude 3 Haiku each scored 0.77

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Faithfulness scores differed substantially across the three LLM judges evaluating the same sessions, indicating sensitivity to the evaluator model. [→ Yang 2026](#yang-2026)

## Evidence

### Yang 2026

Yang, F.; Wu, J.; Tian, Y.; and Zhang, J. (2026). CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education. [doi:10.48550/arXiv.2609.19429](https://doi.org/10.48550/arXiv.2609.19429)

`q2 · i?` · `design · r2`

Secondary analysis of judge agreement in the pooled evaluation of 15 sessions: two judges agreed at 0.77 while Gemini 2.5 Flash scored 0.31 on the same data. The article prints these scores; no effect size is reported.

> "GPT-4o-mini and Claude 3 Haiku produced identical scores of 0 .77, whereas Gemini 2.5 Flash produced a lower score of 0.31. The variation across judges indicates that automated faithfulness evaluation is sensitive to the evaluator model."

## Discussion


## Related Claims
- [Gemini Flash 2.0 was selected for production over GPT-4o-mini and Llama 3.1 for its superior faithfulness and speed-to-cost ratio](gemini-flash-2-selected-for-faithfulness-and-cost.md) — related
- [CARES achieved an overall majority-vote faithfulness score of 0.74, with most factual claims supported by retrieved regulatory context](cares-faithfulness-074.md) — related
- [FATE benchmarks rank Gemini 2.5 Flash highest among commercial AI tutors, with actionability weakest for all models](fate-benchmark-commercial-ai-tutors.md) — related
- [Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models](cross-model-rpla-degradation-consistent.md) — related
