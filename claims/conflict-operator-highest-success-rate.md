---
type: claim
title: CONFLICT operator achieves the highest downstream success rate among Berlyne-inspired curiosity operators, while NOVELTY is selected most frequently with a substantially lower success rate
description: CONFLICT operator achieves the highest downstream success rate among Berlyne-inspired curiosity operators, while NOVELTY is selected most frequently with a substantially lower success rate
id: conflict-operator-highest-success-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: ganganath-2026
    resource: "https://doi.org/10.48550/arxiv.2606.22349"
    title: "Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T. (2026). Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior. https://arxiv.org/abs/2606.22349 [doi:10.48550/arxiv.2606.22349](https://doi.org/10.48550/arxiv.2606.22349)"
    author: "Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# CONFLICT operator achieves the highest downstream success rate among Berlyne-inspired curiosity operators, while NOVELTY is selected most frequently with a substantially lower success rate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Ganganath 2026: no comparison group (read from the study by two models, 2026-10-25)

## Subclaims
`q2 i?` CONFLICT achieves the highest success rate (79.03%, 72 appearances) among the five curiosity operators, whereas NOVELTY appears most frequently (258 appearances) but achieves a substantially lower success rate (61.42%). [→ Ganganath 2026](#ganganath-2026)

## Evidence

### Ganganath 2026

Ganganath, G., Bolonghege, P., Lyu, Q., Varakantham, P., & Kandappu, T. (2026). Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior. https://arxiv.org/abs/2606.22349 [doi:10.48550/arxiv.2606.22349](https://doi.org/10.48550/arxiv.2606.22349)

`q2 · i?` · `causal · r2`

Operator-level analysis (§5.2) of selection frequency and downstream success rates (the proportion of operator applications resulting in a stable or increased curiosity score) from Table 4. UNCERTAINTY shows the lowest success rate (44.44%, 22 appearances). The authors interpret this as consistent with Berlyne's theory that conflict produces stronger epistemic tension.

> "CONFLICTachieves the highest success rate (79.03%) despite relatively infrequent selection (72 appearances), whereas NOVELTYappears most frequently (258 appearances)"

## Discussion


## Related Claims
- [Curiosity gains depend on operator sequencing: how operators are ordered across turns, not only which operator is applied, shapes curiosity induction](operator-sequencing-affects-curiosity-gains.md) — related
- [Curiosity is the primary driver and mistrust of accuracy the primary barrier to LLM adoption for learning](curiosity-driver-mistrust-barrier-llm-learning.md) — related
- [The value-conflict taxonomy is applied to student rating of teaching at the University of Salzburg, surfacing conflicts such as bandwidth vs. fidelity](taxonomy-applied-salzburg-student-ratings.md) — related
