---
type: claim
title: Mixing teaching signals (demonstrations and instructions) is superior to using demonstrations only or instructions only for goal-conditioned agents
description: Mixing teaching signals (demonstrations and instructions) is superior to using demonstrations only or instructions only for goal-conditioned agents
id: mixing-demonstrations-instructions-superior
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: hugo-caselles-dupré-2023
    resource: "https://doi.org/10.48550/arXiv.2308.10842"
    title: "Hugo Caselles-Dupré, Olivier Sigaud, Mohamed Chetouani. (2023). Show and Tell: Enhancing Agent Communication and Learning through Action and Language. arXiv. [doi:10.48550/arXiv.2308.10842](https://doi.org/10.48550/arXiv.2308.10842)"
    author: Hugo Caselles-Dupré, Olivier Sigaud, Mohamed Chetouani
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Mixing teaching signals (demonstrations and instructions) is superior to using demonstrations only or instructions only for goal-conditioned agents

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Teaching with both demonstrations and instructions, regardless of order, yields better training efficiency than teaching with demonstrations only or instructions only. [→ Hugo Caselles-Dupré 2023](#hugo-caselles-dupre-2023)

## Evidence

### Hugo Caselles-Dupré 2023

Hugo Caselles-Dupré, Olivier Sigaud, Mohamed Chetouani. (2023). Show and Tell: Enhancing Agent Communication and Learning through Action and Language. arXiv. [doi:10.48550/arXiv.2308.10842](https://doi.org/10.48550/arXiv.2308.10842)

`q2 · i?` · `causal · r1`

Simulation experiments in the Fetch Block Stacking environment compare mixed-modality teaching (demonstrations then instructions, and instructions then demonstrations, AuC 34.3 and 31.2 for naive/literal) against single-modality teaching (AuC 28.8 and 28.3), as reported in Table 1.

> "Our experiments then reveal that mixing the nature of teaching signals is beneficial to GC-agents. Teaching with demonstrations and instruction, no matter the order in which they are given, is superior to learning with demonstrations only or instructions only."

## Discussion


## Related Claims
- [Adding pedagogy to the teacher and pragmatism to the learner increases learning efficiency of goal-conditioned agents across all tested modalities](pedagogy-pragmatism-increase-gc-agent-efficiency.md) — related
- [Instructed learners outperform all other condition groups in learning simple second language rules](instructed-learners-outperform-others-simple-rules.md) — related
