---
type: claim
title: Enabling reasoning in GPT-5.2 resolves physics-error items but not visual-error items, with non-monotonic degradation on visually demanding items
description: Enabling reasoning in GPT-5.2 resolves physics-error items but not visual-error items, with non-monotonic degradation on visually demanding items
id: reasoning-depth-interaction-error-type
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: eugenio-tufino-2026
    resource: "https://doi.org/10.1088/1361-6404/ae8c90"
    title: "Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. [doi:10.1088/1361-6404/ae8c90](https://doi.org/10.1088/1361-6404/ae8c90)"
    author: Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Enabling reasoning in GPT-5.2 resolves physics-error items but not visual-error items, with non-monotonic degradation on visually demanding items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across reasoning_effort levels none/medium/high, items dominated by physics errors improved substantially (e.g. Q17: 60% → 100% → 100%), pure visual-error items were unaffected (Q4 near zero at all settings), and Q16/Q20 peaked at medium and decreased at high. [→ Eugenio Tufino 2026](#eugenio-tufino-2026)

## Evidence

### Eugenio Tufino 2026

Eugenio Tufino, Caterina Giovanzana, Andrea Zamboni, Pasquale Onorato and Stefano Oss. (2026). Performance and failure modes of AI chatbots on a novel concept inventory on relativity in classical mechanics. [doi:10.1088/1361-6404/ae8c90](https://doi.org/10.1088/1361-6404/ae8c90)

`q2 · i?` · `design · r2`

Sensitivity analysis repeating the 30-iteration protocol for GPT-5.2 at reasoning_effort = medium and high (temperature not configurable at these settings); printed trajectories include Q15 improving monotonically 7% → 60% → 90% while Q4 remained near zero.

> "items dominated by physics errors are resolved by moderat e reasoning, items with pure visual errors are unaffected regardless of reasoning level, and items with complex visual demands show non -monotonic behavior where excessive reasoning can degrade performance."

## Discussion


## Related Claims
- [All three models show severe, item-specific failures, with Q16 (fluid on inclined plane with friction) difficult for every model and GPT-5.2 scoring 0% on Q4](item-specific-complete-llm-failures.md) — related
- [AI performance on AP Physics FRQs degrades substantially on tasks requiring visual extraction, spatial inference, or integration across sub-parts, despite strong algebraic performance](llm-physics-errors-cluster-visual-spatial-tasks.md) — a broader claim this one bears on
- [LLM errors on multimodal physics problems fall into four categories, with visual processing errors most prevalent, and error type distribution does not differ significantly across models](four-category-llm-multimodal-error-taxonomy.md) — related
- [The Multimodal Interference Effect: mapping visual representations to physical concepts degrades LLM performance even on non-visual problem aspects](multimodal-interference-effect-llms.md) — related
- [All four multimodal LLMs show a marked decrease in correct response rates on visually-based versus text-only JNEOT questions](llm-visual-question-decline-jneot.md) — related
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — related
