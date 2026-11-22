---
type: claim
title: "Large model performance drops notably on hard L2-Bench tasks, with the top three models all scoring below 80% on 267 tasks"
description: "Large model performance drops notably on hard L2-Bench tasks, with the top three models all scoring below 80% on 267 tasks"
id: l2-bench-hard-task-performance-drop
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

# Large model performance drops notably on hard L2-Bench tasks, with the top three models all scoring below 80% on 267 tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the hardest tasks, large model performance falls to the 69.9%-73.4% range, indicating room for improvement. [→ James Edgell 2026](#james-edgell-2026)

## Evidence

### James Edgell 2026

James Edgell, Wm. Matthew Kennedy, Ben Knight, Danielle Carvalho, Martin Ku, Isaac Pattis. (2026). L2-Bench: An Evaluation Benchmark for Measuring LLM Capabilities in Second Language Education. [doi:10.1609/aies.v9i2.43189](https://doi.org/10.1609/aies.v9i2.43189)

`q2 · i?` · `design · r3`

Benchmark evaluation of nine models on the full L2-Bench task set; the article identifies a hard-items-only variant of 267 tasks that the top three models all scored below 80% on, and reports the hard-task performance range for large models.

> "On hard tasks, large model performance falls to∈[69.9%, 73.4%], suggesting that there is room for improvement—and good reason to develop more complex evaluation datasets."

## Discussion


## Related Claims
- [LLMs perform competently at comparing item difficulty but fall below random chance on comparing item discrimination](llms-below-chance-item-discrimination.md) — related
- [Current vision-language models struggle on education-oriented Turtle Graphics tasks, with even top models far below reliable performance on real-world tasks for grades 3-6](vlms-struggle-turtleai-real-world-tasks.md) — related
- [Models struggle more in pedagogically demanding low-proficiency and low-resource contexts, with smaller models varying more across contexts](l2-bench-context-performance-low-resource.md) — related
- [All tested LLMs exceeded the NMLE passing threshold yet stayed below 80% accuracy across all units and years](llms-pass-nmle-but-ceiling-below-80-percent.md) — related
- [OmniEdu-27B achieves the best overall curriculum-grounding performance among evaluated models, raising K12-Bench EM from 52.11% to 63.12%](omniedu-27b-best-curriculum-grounding-k12-bench.md) — related
