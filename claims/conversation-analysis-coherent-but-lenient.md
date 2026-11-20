---
type: claim
title: Conversation-log analysis found the system hosted coherent EMT-based dialogues but was lenient toward partial explanations and sometimes repeated requests
description: Conversation-log analysis found the system hosted coherent EMT-based dialogues but was lenient toward partial explanations and sometimes repeated requests
id: conversation-analysis-coherent-but-lenient
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: robin-schmucker-2024
    resource: "https://doi.org/10.1007/978-3-031-64302-6_6"
    title: "Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell. (2024). Ruffle&Riley: Insights from Designing and Evaluating a Large Language Model-Based Conversational Tutoring System. [doi:10.1007/978-3-031-64302-6_6](https://doi.org/10.1007/978-3-031-64302-6_6)"
    author: Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Conversation-log analysis found the system hosted coherent EMT-based dialogues but was lenient toward partial explanations and sometimes repeated requests

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Analysis of conversation logs verified factual correctness of agent responses and coherent dialogues, but found seven conversations omitted one to two expectations, nine conversations repeated similar requests, and the system was often lenient toward responses covering only part of an expectation. [→ Robin Schmucker 2024](#robin-schmucker-2024)

## Evidence

### Robin Schmucker 2024

Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell. (2024). Ruffle&Riley: Insights from Designing and Evaluating a Large Language Model-Based Conversational Tutoring System. [doi:10.1007/978-3-031-64302-6_6](https://doi.org/10.1007/978-3-031-64302-6_6)

`q2 · i?` · `design · r2`

Conversation-log analysis of the 31 R&R participants in Evaluation 2 who completed the activity. The authors report that "An evaluation of all conversations verified the factual correctness of the GPT-4-based agents' responses" and that R&R facilitates coherent free-form conversational tutoring, while identifying omission, repetition, and leniency issues.

> "While all 31 participants went through all four questions in the tutoring script, we noticed that seven conversations omitted one to two expectations. Further, in nine conversations, the student agent requested similar information at different points in the session, often when users wrote long responses covering multiple expectations at once."

## Discussion


## Related Claims
- [Ruffle&Riley produced a significantly more coherent conversation than the LLM QA chatbot and more enjoyment than both QA chatbots](rr-coherence-enjoyment-advantage.md) — related
- [Log analysis: R&R learners used different teaching strategies, requested little help, and conversational learning took longer than reading](rr-log-analysis-strategies-help-time.md) — related
- [Conversation features correlate with learning performance: words and learning time positively, help and revision requests negatively](conversation-features-correlate-with-learning-performance.md) — related
