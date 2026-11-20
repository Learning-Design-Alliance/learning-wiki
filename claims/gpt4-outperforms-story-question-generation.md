---
type: claim
title: GPT-4 outperforms GPT-3.5 and LLaMA 2 in generating legal stories and educational questions
description: GPT-4 outperforms GPT-3.5 and LLaMA 2 in generating legal stories and educational questions
id: gpt4-outperforms-story-question-generation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: hang-jiang-2024
    resource: "https://doi.org/10.18653/v1/2024.acl-long.388"
    title: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. [doi:10.18653/v1/2024.acl-long.388](https://doi.org/10.18653/v1/2024.acl-long.388)"
    author: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: hang-jiang-2024-2
    resource: "https://doi.org/10.18653/v1/2024.acl-long.388"
    title: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. [doi:10.18653/v1/2024.acl-long.388](https://doi.org/10.18653/v1/2024.acl-long.388)"
    author: "Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GPT-4 outperforms GPT-3.5 and LLaMA 2 in generating legal stories and educational questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 outperforms GPT-3.5 and LLaMA 2 in almost all story quality metrics except redundancy, and outperforms other LLMs across all three types of questions. [→ Hang Jiang 2024](#hang-jiang-2024)
`q2 i?` GPT-4 generated questions with no issues at 83%, 75%, and 80% for concept, prediction, and limitation questions respectively, outperforming other LLMs. [→ Hang Jiang 2024 (2)](#hang-jiang-2024-2)

## Evidence

### Hang Jiang 2024

Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. [doi:10.18653/v1/2024.acl-long.388](https://doi.org/10.18653/v1/2024.acl-long.388)

`q2 · i?` · `causal · r2`

Human evaluation by three raters with law education backgrounds on Prolific using 5-item Likert scales across nine metrics on 20 sampled concepts. GPT-4 stories scored ≥4.5 on readability, cohesiveness, relevance, completeness, and factuality.

> "First, GPT-4 outperforms GPT-3.5 and LLaMA 2 in almost all the metrics except for redundancy. LLaMA 2 performs slightly better than GPT-3.5 in most metrics."

### Hang Jiang 2024 (2)

Hang Jiang, Xiajie Zhang, Robert Mahari, Daniel Kessler, Eric Ma, Tal August, Irene Li, Alex 'Sandy' Pentland, Yoon Kim, Deb Roy, Jad Kabbara. (2024). Leveraging Large Language Models for Learning Complex Legal Concepts through Storytelling. [doi:10.18653/v1/2024.acl-long.388](https://doi.org/10.18653/v1/2024.acl-long.388)

`q2 · i?` · `causal · r2`

Error analysis from human evaluation of LLM-generated questions for 20 sampled concepts, computing percentage of questions with versus without issues per model and question type.

> "GPT-4 outperforms other LLMs in generation questions with no issues at 83%, 75%, and 80% for concept, prediction, and limitation questions, respectively."

## Discussion


## Related Claims
- [GPT-4 and GPT-3.5 stories are linguistically simpler than LLaMA 2 stories, and Wikipedia definitions are the most complex texts](llm-stories-lower-linguistic-complexity.md) — related
- [The IRead question generation model, fine-tuned on in-text OpenStax questions, matched reference questions in human ratings and outperformed zero-shot GPT-4 on automatic metrics](iread-qg-model-evaluation-performance.md) — related
