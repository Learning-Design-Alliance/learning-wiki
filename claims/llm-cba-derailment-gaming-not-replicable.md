---
type: claim
title: LLM assessment conversations can be derailed off-topic by gaming attempts, and one successful prompt revision was not demonstrated to be replicable
description: LLM assessment conversations can be derailed off-topic by gaming attempts, and one successful prompt revision was not demonstrated to be replicable
id: llm-cba-derailment-gaming-not-replicable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: diego-zapata-rivera-2024
    resource: "https://ceur-ws.org"
    title: "Diego Zapata-Rivera, Carol Forsyth, Edith Aurora Graf and Yang Jiang. (2024). Designing and Evaluating Evidence-Centered Design based Conversations for Assessment with LLMs. Leveraging Large Language Models for Next Generation Educational Technologies, CEUR Workshop Proceedings. https://ceur-ws.org"
    author: Diego Zapata-Rivera, Carol Forsyth, Edith Aurora Graf and Yang Jiang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM assessment conversations can be derailed off-topic by gaming attempts, and one successful prompt revision was not demonstrated to be replicable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In initial attempts, users could derail the LLM from the assessed construct (volcano prediction shifted to mathematics and then to a non-volcano context); a revised prompt resisted topic changes in one example, but the authors state this does not demonstrate success or replicability. [→ Diego Zapata-Rivera 2024](#diego-zapata-rivera-2024)

## Evidence

### Diego Zapata-Rivera 2024

Diego Zapata-Rivera, Carol Forsyth, Edith Aurora Graf and Yang Jiang. (2024). Designing and Evaluating Evidence-Centered Design based Conversations for Assessment with LLMs. Leveraging Large Language Models for Next Generation Educational Technologies, CEUR Workshop Proceedings. https://ceur-ws.org

`q2 · i?` · `design · r2`

Gaming-probe investigation within the case study: a user claiming prior knowledge asked to discuss math, and the LLM eventually posed a rate question about cars, changing both construct and context. After prompt revision the LLM replied humorously to a topic-change attempt, but the authors caution the result "is replicable" only with testing across many conversations.

> "we acknowledge that there are numerous ways that a student could change the topic, and this one example does not demonstrate that we were successful in changing the LLMs behavior or that the result is replicable—that would require testing with many conversations."

## Discussion


## Related Claims
- [In a case study, LLM-generated assessment conversations handled common student speech acts more naturalistically than RegExp/LSA conversations](llm-cba-more-naturalistic-than-regexp-lsa.md) — related
- [Prompting alone could not keep the gpt-3.5-turbo model on-topic, while the text-davinci-002 engine stayed on-topic in the deployed chatbot](gpt35-turbo-off-topic-prompting-insufficient.md) — related
- [LLM participant agents clarify stage goals, keep discussions on topic, and prompt deeper ethical reflection](llm-participants-stage-goal-clarification.md) — related
- [ChatGPT sustains coherent, human-like multi-topic conversation and produces convincing creative content, as shown by the authors' own prompting test](chatgpt-interactive-conversational-capability.md) — reports the opposite
