---
type: claim
title: "Five general instruction-following evaluators could not reach deployable activation rates (best BMK 2.23%–20.72%) because fixed rubrics cannot enumerate long per-conversation instruction sets"
description: "Five general instruction-following evaluators could not reach deployable activation rates (best BMK 2.23%–20.72%) because fixed rubrics cannot enumerate long per-conversation instruction sets"
id: instruction-following-evaluators-structural-carve-out
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: chris-rohlfs-2026
    resource: "https://doi.org/10.48550/arxiv.2609.28478"
    title: "Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell. (2026). When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI. https://arxiv.org/abs/2609.28478 [doi:10.48550/arxiv.2609.28478](https://doi.org/10.48550/arxiv.2609.28478)"
    author: "Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell"
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Five general instruction-following evaluators could not reach deployable activation rates (best BMK 2.23%–20.72%) because fixed rubrics cannot enumerate long per-conversation instruction sets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Five instruction-following evaluators did not reach deployable activation rates under the configurations tested, with best candidate BMK values from 2.23% to 20.72%, well above the deployed median of 0.04%. [→ Chris Rohlfs 2026](#chris-rohlfs-2026)

## Evidence

### Chris Rohlfs 2026

Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell. (2026). When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI. https://arxiv.org/abs/2609.28478 [doi:10.48550/arxiv.2609.28478](https://doi.org/10.48550/arxiv.2609.28478)

`q2 · i?` · `design · r3`

Best candidate configurations for the five carved-out Instruction-Following evaluators (All, Critical, System, Task, Tool instruction), reported in Table 3 with EGR% from 75.4% to 100%. The article attributes the failure to a structural mismatch: a fixed rubric cannot enumerate long, per-conversation instruction sets.

> "Five instruction-following evaluators did not reach deployable activation rates under the configurations tested (best candidate BMK values from 2.23% to 20.72%, well above the deployed median of 0.04%)."

## Discussion


## Related Claims
- [Post-calibration evaluators captured 100% of synthetic egregious failures across all 21 deployed evaluators, up from a pre-calibration range of 73.3–100%](egregious-capture-100-percent-after-calibration.md) — related
- [A deployed reflection agent followed its prompt's countable rules but broke its dispositional rules about manner](agent-followed-countable-not-dispositional-rules.md) — related
