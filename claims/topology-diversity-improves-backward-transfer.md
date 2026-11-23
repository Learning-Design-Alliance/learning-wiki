---
type: claim
title: Varying topology count markedly improves backward transfer to the first distribution, whereas layout and object-assignment counts do not visibly affect it
description: Varying topology count markedly improves backward transfer to the first distribution, whereas layout and object-assignment counts do not visibly affect it
id: topology-diversity-improves-backward-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: purab-seth-2026
    resource: "https://doi.org/10.48550/arXiv.2606.00880"
    title: "Purab Seth, Neil Shah, Ishaan Sinha, Kunal Jha, Samuel J. Gershman, Max Kleiman-Weiner, Wilka Carvalho. (2026). Task diversity produces systematic transfer but inhibits continual reinforcement learning. arXiv preprint. [doi:10.48550/arXiv.2606.00880](https://doi.org/10.48550/arXiv.2606.00880)"
    author: Purab Seth, Neil Shah, Ishaan Sinha, Kunal Jha, Samuel J. Gershman, Max Kleiman-Weiner, Wilka Carvalho
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Varying topology count markedly improves backward transfer to the first distribution, whereas layout and object-assignment counts do not visibly affect it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Varying topology count |T| leads to markedly better backward transfer to d1 after training on d2, across both PPO and PQN. [→ Purab Seth 2026](#purab-seth-2026)
`q2 i?` Neither layout count nor object assignment count visibly affects backward transfer across PPO and PQN. [→ Purab Seth 2026](#purab-seth-2026)

## Evidence

### Purab Seth 2026

Purab Seth, Neil Shah, Ishaan Sinha, Kunal Jha, Samuel J. Gershman, Max Kleiman-Weiner, Wilka Carvalho. (2026). Task diversity produces systematic transfer but inhibits continual reinforcement learning. arXiv preprint. [doi:10.48550/arXiv.2606.00880](https://doi.org/10.48550/arXiv.2606.00880)

`q2 · i?` · `causal · r2`

Single-shift backward-transfer analysis in Banyan after agents trained on d1 then d2, evaluated for PPO and PQN across the three diversity axes. The article reports topology count "leads to markedly better backward transfer" while the other axes show no visible effect.

> "Neither layout count|L|nor object assignment count|O|visibly affects backward transfer across PPO and PQN. However, varying topology count|T|leads to markedly better backward transfer across both PPO and PQN (Figure 3; Figure 11)."

## Discussion


## Related Claims
- Across ten task distributions, increasing task diversity improves backward transfer to the first distribution — related
- Across ten task distributions, high task diversity inhibits continued improvement on new distributions: the final success rate declines monotonically as diversity grows past n=16 — related
- In the continuous-control PointMass domain, increasing object-assignment diversity improves forward transfer (Δ2 rising from about −0.95 to about −0.5) and backward transfer (B(2,1) rising from about −0.8 to about 0) — reports the opposite
