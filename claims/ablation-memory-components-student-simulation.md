---
type: claim
title: Removing past cognitive states or the whole few-shot memory from the agent degrades simulation of all behaviors
description: Removing past cognitive states or the whole few-shot memory from the agent degrades simulation of all behaviors
id: ablation-memory-components-student-simulation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: songlin-xu-2024
    resource: "https://doi.org/10.48550/arXiv.2404.07963"
    title: "Songlin Xu, Xinyu Zhang, Lianhui Qin. (2024). EduAgent: Generative Student Agents in Learning. Preprint. [doi:10.48550/arXiv.2404.07963](https://doi.org/10.48550/arXiv.2404.07963)"
    author: Songlin Xu, Xinyu Zhang, Lianhui Qin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Removing past cognitive states or the whole few-shot memory from the agent degrades simulation of all behaviors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Ablations on EduAgent310 show all behavior simulation drops when past cognitive states are removed from memory, and performance drops significantly for all behaviors when the entire few-shot memory is removed. [→ Songlin Xu 2024](#songlin-xu-2024)

## Evidence

### Songlin Xu 2024

Songlin Xu, Xinyu Zhang, Lianhui Qin. (2024). EduAgent: Generative Student Agents in Learning. Preprint. [doi:10.48550/arXiv.2404.07963](https://doi.org/10.48550/arXiv.2404.07963)

`q2 · i?` · `design · r2`

Ablation study within the Experiment 1 simulation on EduAgent310, removing gaze, motor, cognitive-state, or full few-shot memory components. Removing cognitive states degraded all behaviors; the article reports simulation "drops significantly for all behaviors" when the whole few-shot demonstration memory is removed.

> "we find that all behavior simulation performance drops when we remove past cognitive states from memory, indicating that cognitive states are highly correlated with other behaviors and therefore play an important role in our framework"

## Discussion


## Related Claims
- [In the EduAgent framework, removing past cognitive states from memory significantly reduced simulation performance](eduagent-ablation-contextual-memory-critical.md) — possibly the same claim (merge candidate)
- [Integrating cognitive prior knowledge into LLM prompts improves simulation of student gaze behaviors, cognitive states, and question answering](cognitive-priors-improve-llm-student-simulation.md) — related
