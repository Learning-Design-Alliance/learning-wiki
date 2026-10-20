---
type: claim
title: Prompting alone could not keep the gpt-3.5-turbo model on-topic, while the text-davinci-002 engine stayed on-topic in the deployed chatbot
description: Prompting alone could not keep the gpt-3.5-turbo model on-topic, while the text-davinci-002 engine stayed on-topic in the deployed chatbot
id: gpt35-turbo-off-topic-prompting-insufficient
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: saniya-vahedian-movahed-and-fred-martin-2025
    resource: "https://doi.org/10.48550/arxiv.2502.14217"
    title: "Saniya Vahedian Movahed and Fred Martin. (2025). Ask Me Anything: Exploring children's attitudes toward an age-tailored AI-powered chatbot. arXiv. https://arxiv.org/abs/2502.14217 [doi:10.48550/arxiv.2502.14217](https://doi.org/10.48550/arxiv.2502.14217)"
    author: Saniya Vahedian Movahed and Fred Martin
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Prompting alone could not keep the gpt-3.5-turbo model on-topic, while the text-davinci-002 engine stayed on-topic in the deployed chatbot

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Despite prompt instructions to refuse off-topic questions, gpt-3.5-turbo answered off-topic questions after repeated attempts, so the authors switched to text-davinci-002. [→ Saniya Vahedian Movahed and Fred Martin 2025](#saniya-vahedian-movahed-and-fred-martin-2025)

## Evidence

### Saniya Vahedian Movahed and Fred Martin 2025

Saniya Vahedian Movahed and Fred Martin. (2025). Ask Me Anything: Exploring children's attitudes toward an age-tailored AI-powered chatbot. arXiv. https://arxiv.org/abs/2502.14217 [doi:10.48550/arxiv.2502.14217](https://doi.org/10.48550/arxiv.2502.14217)

`q1 · i?` · `design · r2`

Design-phase experiments with the ChatGPT API, including varied prompt language, temperature values of 0.2, 0.5, and 0.7, and token settings, showed that "the gpt-3.5-turbo model would answer off-topic questions after repeated attempts"; text-davinci-002 stayed on-topic and was used in the deployed system.

> "We discovered that despite our multiple statements to stay on-topic, the gpt-3.5-turbo model would answer off-topic questions after repeated attempts."

## Discussion


## Related Claims
- [Student-AI conversations under teacher-authored prompts largely stay on the intended task (71% fully on-track; fewer than 1% substantially off-track)](teacher-prompts-keep-conversations-on-track.md) — related
- [Preference explanations favoring LearnLM more often cite staying on topic, challenging the learner, and not giving away answers](learnlm-preference-explanation-themes.md) — related
- [LLM assessment conversations can be derailed off-topic by gaming attempts, and one successful prompt revision was not demonstrated to be replicable](llm-cba-derailment-gaming-not-replicable.md) — related
- [FSM-based evaluation discriminates interactive quality across models, with GPT-5 Mini scoring highest and most tiers significantly separated](fsm-eval-discriminates-model-quality.md) — related
