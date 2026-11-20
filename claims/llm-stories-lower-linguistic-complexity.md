---
type: claim
title: GPT-4 and GPT-3.5 stories are linguistically simpler than LLaMA 2 stories, and Wikipedia definitions are the most complex texts
description: GPT-4 and GPT-3.5 stories are linguistically simpler than LLaMA 2 stories, and Wikipedia definitions are the most complex texts
id: llm-stories-lower-linguistic-complexity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: hang-jiang-2024
    resource: "https://doi.org/10.18653/v1/2024.acl-long.388"
    title: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. [doi:10.18653/v1/2024.acl-long.388](https://doi.org/10.18653/v1/2024.acl-long.388)"
    author: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 and GPT-3.5 stories are linguistically simpler than LLaMA 2 stories, and Wikipedia definitions are the most complex texts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across automatic complexity measures, stories from GPT-3.5 and GPT-4 use a language of similar complexity that is simpler than LLaMA 2 stories, while the Wikipedia definitions show the most linguistic complexity. [→ Hang Jiang 2024](#hang-jiang-2024)

## Evidence

### Hang Jiang 2024

Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. [doi:10.18653/v1/2024.acl-long.388](https://doi.org/10.18653/v1/2024.acl-long.388)

`q2 · i?` · `design · r2`

Automatic complexity evaluation comparing Wikipedia definitions and LLM-generated stories on the same subset of 20 concepts, using six metrics including LVL occurrences, GPT perplexity, sentence length, and Flesch-Kincaid grade level. The article states "Stories from GPT-3.5 and GPT-4 use a language with similar complexity but simpler than those from LLaMA 2."

> "Stories from GPT-3.5 and GPT-4 use a language with similar complexity but simpler than those from LLaMA 2."

## Discussion


## Related Claims
- [GPT-4 outperforms GPT-3.5 and LLaMA 2 in generating legal stories and educational questions](gpt4-outperforms-story-question-generation.md) — related
- [LLM temperature settings significantly affect generated-text length and complexity, with Llama3 producing more complex texts than GPT-3.5](temperature-drives-generated-text-complexity.md) — related
