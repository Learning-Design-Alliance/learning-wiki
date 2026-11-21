---
type: claim
title: Earlier LLM generations failed spatial-geometry steps in Electromagnetism, such as deducing induced-current direction with the right-hand rule
description: Earlier LLM generations failed spatial-geometry steps in Electromagnetism, such as deducing induced-current direction with the right-hand rule
id: llm-spatial-geometry-em-bottleneck
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jonah-l-donaldson-2026
    resource: "https://doi.org/10.48550/arXiv.2605.23660"
    title: "Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)"
    author: Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Earlier LLM generations failed spatial-geometry steps in Electromagnetism, such as deducing induced-current direction with the right-hand rule

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In PB1, almost every model across Generations 1–3 scored exactly 90.9% with zero variance on EM Q4, failing the right-hand-rule step while succeeding at flux calculations. [→ Jonah L. Donaldson 2026](#jonah-l-donaldson-2026)

## Evidence

### Jonah L. Donaldson 2026

Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)

`q2 · i?` · `design · r2`

PB1 human-evaluation results for Electromagnetism question EM Q4, scored against the UCL rubric. The article reports models "failed the final qualitative step required to deduce the direction of the induced current using the right-hand rule", attributing this to lack of three-dimensional spatial grounding in text tokens.

> "Across Generations 1 through 3, almost every model scored exactly 90.9% with zero variance. The models successfully performed the overarching flux calculations but failed the final qualitative step required to deduce the direction of the induced current using the right-hand rule."

## Discussion


## Related Claims
- [AI performance on AP Physics FRQs degrades substantially on tasks requiring visual extraction, spatial inference, or integration across sub-parts, despite strong algebraic performance](llm-physics-errors-cluster-visual-spatial-tasks.md) — a broader claim this one bears on
- [Right-hand-rule tasks are especially difficult for ChatGPT-4o, which states the rule correctly but applies it incorrectly in most cases](right-hand-rule-application-failure-chatgpt-4o.md) — related
- [Native multimodal Generation 5 models resolved the diagram-based spatial reasoning bottleneck, with Gemini 3.0 Pro scoring 100% in Classical Mechanics and Electromagnetism](multimodal-gen5-resolve-spatial-bottleneck.md) — reports the opposite
- [ChatGPT-4o's BEMA errors fall into three difficulty types, with spatial coordination of representations and rules the most prevalent](three-chatbot-difficulty-types-bema.md) — related
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — related
- [LLM factual errors during collaborative circuit debugging occurred almost exclusively after image inputs, attributed to limited 3D spatial reasoning from breadboard or PCB photos](llm-factual-errors-after-image-inputs-3d-reasoning.md) — related
- [A role-engineered Gem guides students through conceptual and spatial reasoning in electromagnetic induction using pre-trained knowledge without instructor-provided Knowledge files](gem-socratic-electromagnetic-induction-reasoning.md) — related
