---
type: claim
title: CARES achieved an overall majority-vote faithfulness score of 0.74, with most factual claims supported by retrieved regulatory context
description: CARES achieved an overall majority-vote faithfulness score of 0.74, with most factual claims supported by retrieved regulatory context
id: cares-faithfulness-074
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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

# CARES achieved an overall majority-vote faithfulness score of 0.74, with most factual claims supported by retrieved regulatory context

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a preliminary evaluation with 15 construction management students, CARES responses were mostly supported by retrieved regulatory context, with an overall majority-vote faithfulness score of 0.74. [→ Yang 2026](#yang-2026)

## Evidence

### Yang 2026

Yang, F.; Wu, J.; Tian, Y.; and Zhang, J. (2026). CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education. [doi:10.48550/arXiv.2609.19429](https://doi.org/10.48550/arXiv.2609.19429)

`q2 · i?` · `design · r2`

Pooled LLM-as-a-judge evaluation of 15 CARES reporting sessions; three judges (gpt-4o-mini, Gemini 2.5 Flash, Claude 3 Haiku) scored turn-level claim support. The study reports the "overall majority -vote score was 0.74"; no effect size is printed.

> "For Faithfulness, the overall majority -vote score was 0.74, indicating that most factual claims evaluated during eligible conversational turns were supported by the retrieved regulatory context."

## Discussion


## Related Claims
- [CARES achieved an overall answer relevance score of 1.00, consistently addressing the user's immediately preceding message](cares-answer-relevance-100.md) — related
- [Generated answers sometimes added correct background knowledge not explicitly supported by retrieved evidence, an unsupported-answer behavior the authors flag as requiring faithfulness evaluation](answers-add-unsupported-background-knowledge.md) — related
- [Initial retrieval ranking in CARES was weak, with a pooled Retrieval Precision Proxy@4 of 0.17](cares-retrieval-precision-proxy-017.md) — related
- [Automated faithfulness evaluation was sensitive to the evaluator model, with Gemini 2.5 Flash scoring 0.31 while GPT-4o-mini and Claude 3 Haiku each scored 0.77](llm-judge-faithfulness-sensitivity.md) — related
