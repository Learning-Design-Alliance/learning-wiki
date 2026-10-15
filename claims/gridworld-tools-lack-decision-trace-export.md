---
type: claim
title: Representative gridworld teaching tools lack live Bellman substitution, decision-provenance logging, and full trace export
description: Representative gridworld teaching tools lack live Bellman substitution, decision-provenance logging, and full trace export
id: gridworld-tools-lack-decision-trace-export
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: jueng-2026
    resource: "https://doi.org/10.48550/arxiv.2607.10802"
    title: "Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802 [doi:10.48550/arxiv.2607.10802](https://doi.org/10.48550/arxiv.2607.10802)"
    author: Jueng, Ekkachai
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Representative gridworld teaching tools lack live Bellman substitution, decision-provenance logging, and full trace export

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Among the representative gridworld Q-learning teaching tools reviewed, none simultaneously renders the update equation with live numeric substitution, logs the full pre-decision Q-row with greedy/random provenance, and exports the complete decision trace for learner-side analysis. [→ Jueng 2026](#jueng-2026)

## Evidence

### Jueng 2026

Jueng, Ekkachai. (2026). Q-Learning Lab: Teaching Reinforcement Learning Through Learner-Generated Trace Analysis. https://arxiv.org/abs/2607.10802 [doi:10.48550/arxiv.2607.10802](https://doi.org/10.48550/arxiv.2607.10802)

`q1 · i?` · `design · r2`

Feature comparison against representative tools (CS188 Gridworld, RL Playground, Virtual Labs, tinyrl, gridworld-qlearning), summarized in Table 1 from publicly documented feature sets. The authors report they 'did not find a system that simultaneously' offers the three features.

> "we did not find a system that simultaneously (i) renders the update equation itself with live numeric substitution at every step, (ii) logs the agent’s full pre-decision Q-row together with the greedy/random provenance of each action"

## Discussion


## Related Claims
- [Of 100 human-audited claims, 39 are fully verifiable, 55 partially verifiable, and 6 not verifiable, with main responses showing stronger provenance than follow-ups](human-audit-claim-verifiability.md) — related
