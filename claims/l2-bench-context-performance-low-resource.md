---
type: claim
title: Models struggle more in pedagogically demanding low-proficiency and low-resource contexts, with smaller models varying more across contexts
description: Models struggle more in pedagogically demanding low-proficiency and low-resource contexts, with smaller models varying more across contexts
id: l2-bench-context-performance-low-resource
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: james-edgell-2026
    resource: "https://doi.org/10.1609/aies.v9i2.43189"
    title: "James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis. (2026). L2-Bench: An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education. [doi:10.1609/aies.v9i2.43189](https://doi.org/10.1609/aies.v9i2.43189)"
    author: James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Models struggle more in pedagogically demanding low-proficiency and low-resource contexts, with smaller models varying more across contexts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models appear to struggle more with pedagogically demanding low-proficiency contexts and low-resource contexts; smaller model performance varied more substantially across contexts than larger models. [→ James Edgell 2026](#james-edgell-2026)
`q2 i?` Lower scores on younger age groups indicate models struggle with age-appropriate pedagogy, with universal criteria applying stronger age-appropriateness weighting for younger learners. [→ James Edgell 2026](#james-edgell-2026)

## Evidence

### James Edgell 2026

James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis. (2026). L2-Bench: An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education. [doi:10.1609/aies.v9i2.43189](https://doi.org/10.1609/aies.v9i2.43189)

`q2 · i?` · `design · r3`

Contextual analysis of model performance across task context factors (geographic, economic, resourcedness, age, role). Table 3 reports performance by combined resource level (e.g., Opus 4.7: 85.7 low, 88.1 mixed, 86.6 high) and Table 4 by age group; among top-tier models only modest overall differences were observed.

> "Models appear to struggle more with pedagogically demanding low-proficiency contexts and in low-resource contexts, which present additional constraints (see Table 3). If models score lower on low-resource tasks, it suggests they default to resource-rich assumptions and struggle to adapt."

## Discussion


## Related Claims
- [LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry](llm-teaching-effectiveness-varies-by-domain.md) — related
- [A larger tutor model (LLaMA-3.3-70B) yields greater student gains than a smaller one, especially for low-resource languages](larger-tutor-model-greater-student-gains.md) — related
- [LLM reliability on instructional moves varies by construct: stronger on explicit, structurally constrained moves and weaker on socially and metacognitively demanding ones](llm-reliability-varies-by-talk-move-construct.md) — related
- [SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets](sag-performance-varies-across-corpora.md) — related
- [Large model performance drops notably on hard L2-Bench tasks, with the top three models all scoring below 80% on 267 tasks](l2-bench-hard-task-performance-drop.md) — related
