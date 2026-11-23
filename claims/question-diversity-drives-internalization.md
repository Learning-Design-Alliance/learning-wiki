---
type: claim
title: Question diversity strongly influences knowledge internalization under Closed-SFT, while response diversity has little influence once sufficient correct responses exist
description: Question diversity strongly influences knowledge internalization under Closed-SFT, while response diversity has little influence once sufficient correct responses exist
id: question-diversity-drives-internalization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: jiarui-yuan-2026
    resource: "https://doi.org/10.48550/arXiv.2602.04811"
    title: "Jiarui Yuan, Tailin Jin, Weize Chen, Zeyuan Liu. (2026). SE-BENCH: Benchmarking Self-Evolution with Knowledge Internalization. Preprint. [doi:10.48550/arXiv.2602.04811](https://doi.org/10.48550/arXiv.2602.04811)"
    author: Jiarui Yuan, Tailin Jin, Weize Chen, Zeyuan Liu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Question diversity strongly influences knowledge internalization under Closed-SFT, while response diversity has little influence once sufficient correct responses exist

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` As the number of distinct training questions decreases, training efficiency and final performance degrade; varying responses per question at fixed question count leaves outcomes largely consistent. [→ Jiarui Yuan 2026](#jiarui-yuan-2026)

## Evidence

### Jiarui Yuan 2026

Jiarui Yuan, Tailin Jin, Weize Chen, Zeyuan Liu. (2026). SE-BENCH: Benchmarking Self-Evolution with Knowledge Internalization. Preprint. [doi:10.48550/arXiv.2602.04811](https://doi.org/10.48550/arXiv.2602.04811)

`q2 · i?` · `causal · r2`

Diversity experiments (Fig. 4) under Closed-SFT varying question count and responses per question separately. The right panel shows response diversity (2/5R to 5/5R) has little effect; the figure caption states "Question diversity has a substantially larger influence on knowledge internalization."

> "As the number of distinct questions decreases, the training efficiency gradually drops and the final performance also degrades, indicating that question diversity plays a crucial role in knowledge internalization."

## Discussion


## Related Claims
- Self-play with SFT enables knowledge internalization from self-generated noisy tasks (Closed-SFT-self 22.5%), while pure-RL self-play (Absolute Zero) fails completely — related
