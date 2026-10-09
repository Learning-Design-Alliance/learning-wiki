---
type: claim
title: Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none
description: Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none
id: human-llm-agreement-low-construct-varying
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: ober-2026
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ober-2026-2
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ober-2026-3
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Human-LLM alignment remained low across all constructs and configurations, with κ ranging from 0.000 to 0.419. [→ Ober 2026](#ober-2026)
`q2 i?` Every human-LLM comparison for Prior KSAs yielded κ = 0 despite percent agreement of 52.22% to 83.96%, reflecting different evidence standards for prior knowledge. [→ Ober 2026 (2)](#ober-2026-2)
`q2 i?` Self-efficacy demonstrated the best human-LLM alignment (κ = 0.138 to 0.418), and non-mini models consistently outperformed mini models in human alignment for self-efficacy. [→ Ober 2026 (3)](#ober-2026-3)

## Evidence

### Ober 2026

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Human-LLM agreement analysis comparing LLM outputs against codes from two trained human coders with over five years of assessment development experience. The article reports human-LLM alignment "remained low (κ ranging from 0.000 to 0.419)."

> "In contrast, while LLMs achieved high inter-model agreement for certain configurations, human-LLM alignment remained low (κ ranging from 0.000 to 0.419)"

### Ober 2026 (2)

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Human-LLM comparisons for Prior KSAs across all configurations. LLMs coded explicit knowledge statements such as answers to questions, while human coders relied on subtle indicators like domain-specific vocabulary or references to past experiences, which were largely absent in the dataset.

> "The most striking finding was the lack of alignment in identifying Prior KSA s, where every human -LLM comparison yielded κ = 0 despite agreement ranging from 52.22% to 83.96%"

### Ober 2026 (3)

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Human-LLM agreement for self-efficacy across configurations. Non-mini models outperformed mini models: human2 vs. ChatGPT4o/temperature=0 achieved κ = 0.418, while human2 vs. ChatGPT4o-mini/temperature=0 reached only κ = 0.192. Even the best alignment was poor to fair by conventional standards.

> "Self-efficacy demonstrated the best human-LLM alignment among all constructs, with κ values ranging from 0.138 to 0.418. However, this “best” performance still represents poor to fair agreement by conventional standards"

## Discussion


## Related Claims
- [Constructs with higher operational clarity show higher overall coder agreement, and low clarity harms human coder agreement more than LLM agreement](construct-clarity-predicts-coding-agreement.md) — related
- [Human-human agreement (average κ = 0.644) was lower than the best LLM-LLM agreement (average κ = 0.856) across constructs](human-human-agreement-lower-than-llm-llm.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — reports the opposite
- [LLM-based transcript classifications agreed highly with human judgment for explicit questions (κ = .778) and math talk (κ = .722), but only moderately for need for help (κ = .562) and confusion (κ = .531)](llm-classification-agreement-varies-by-construct.md) — reports the opposite
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers](llm-inductive-coding-risks-require-human-oversight.md) — related
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](llm-as-judge-human-level-agreement-with-validation.md) — reports the opposite
- [LLMs align better with human coding on concise theories with discrete concepts than on more complex ones](theory-complexity-affects-llm-coding-agreement.md) — related
