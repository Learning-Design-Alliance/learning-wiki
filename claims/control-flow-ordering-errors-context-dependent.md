---
type: claim
title: "Control-flow ordering errors appeared across all UH problems (43–52% of incorrect attempts) but were only a secondary pattern at Aalto, with the conceptual barrier apparently shifting with problem structure"
description: "Control-flow ordering errors appeared across all UH problems (43–52% of incorrect attempts) but were only a secondary pattern at Aalto, with the conceptual barrier apparently shifting with problem structure"
id: control-flow-ordering-errors-context-dependent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
sources:
  - id: daniel-prol-2026
    resource: "https://doi.org/10.48550/arxiv.2609.15944"
    title: "Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944 [doi:10.48550/arxiv.2609.15944](https://doi.org/10.48550/arxiv.2609.15944)"
    author: Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: daniel-prol-2026-2
    resource: "https://arxiv.org/abs/2609.15944"
    title: "Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944"
    author: Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Control-flow ordering errors appeared across all UH problems (43–52% of incorrect attempts) but were only a secondary pattern at Aalto, with the conceptual barrier apparently shifting with problem structure

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` At the University of Houston, control-flow ordering errors appeared across all three problems (43–52% of students with incorrect attempts) without a dominant pattern, suggesting students cycled through difficulty types. [→ Daniel Prol 2026](#daniel-prol-2026)
`q2 i?` At Aalto University, control-flow ordering errors were a secondary pattern (31% on safe_integer, 15% on safe_list), with exception-type confusion and return-for-raise substitution dominant instead. [→ Daniel Prol 2026 (2)](#daniel-prol-2026-2)

## Evidence

### Daniel Prol 2026

Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944 [doi:10.48550/arxiv.2609.15944](https://doi.org/10.48550/arxiv.2609.15944)

`q2 · i?` · `design · r2`

Log analysis of UH deployment attempts across the three Parsons problems. Trace data show ordering errors in "43–52% of students with incorrect attempts" with no dominant pattern, which the authors read as upper-division students cycling through all three difficulty types.

> "Control-flow ordering errors appeared consistently across all three problems at the University of Houston (43–52% of students with incorrect attempts), but without a dominant pattern: in P3, wrong ordering (43%) was roughly co-equal with return-for-raise substitution (47%) and exception type confusion (37%)."

### Daniel Prol 2026 (2)

Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944

`q2 · i?` · `design · r2`

Log analysis of Aalto deployment attempts on safe_integer. Ordering errors were "a secondary pattern in safe_integer (P2), present in 31% of students with incorrect attempts", while exception type confusion (62%) and return-for-raise substitution (50%) dominated.

> "At Aalto University, control-flow ordering errors were a secondary pattern in safe_integer (P2), present in 31% of students with incorrect attempts; the dominant difficulties were exception type confusion (62%) and return-for-raise substitution (50%)."

## Discussion


## Related Claims
- [Deploying a trace-capturing Parsons tool in two university courses surfaced recurring difficulty patterns including exception-type misidentification, return-for-throw confusion, and incorrect control-flow ordering](pulla-deployment-surfaced-recurring-difficulty-patterns.md) — a broader claim this one bears on
- [Exception-type confusion was the dominant difficulty pattern in SafeDivide at the University of Houston (90% of incorrect attempts) and persisted across harder problems in both deployments](exception-type-confusion-dominant-pattern.md) — related
- [Students across both deployments substituted return statements for exception-raising constructs, treating error conditions as reasons to exit early](return-for-raise-substitution-pattern.md) — related
- [State revisits within solving sessions were rarer in the Pulla deployments (6–12% of UH sessions, 0–3% at Aalto) than the 21–33% previously reported for similar Parsons tasks](state-revisits-rare-in-pulla-deployments.md) — related
