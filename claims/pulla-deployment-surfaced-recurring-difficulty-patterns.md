---
type: claim
title: Deploying a trace-capturing Parsons tool in two university courses surfaced recurring difficulty patterns including exception-type misidentification, return-for-throw confusion, and incorrect control-flow ordering
description: Deploying a trace-capturing Parsons tool in two university courses surfaced recurring difficulty patterns including exception-type misidentification, return-for-throw confusion, and incorrect control-flow ordering
id: pulla-deployment-surfaced-recurring-difficulty-patterns
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: daniel-prol-2026
    resource: "https://doi.org/10.48550/arxiv.2609.15944"
    title: "Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944 [doi:10.48550/arxiv.2609.15944](https://doi.org/10.48550/arxiv.2609.15944)"
    author: Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Deploying a trace-capturing Parsons tool in two university courses surfaced recurring difficulty patterns including exception-type misidentification, return-for-throw confusion, and incorrect control-flow ordering

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Analysis of behavioral traces from two university deployments identified common difficulty patterns: misidentifying exception types, confusing return with the throw/raise mechanism, and incorrect control-flow ordering. [→ Daniel Prol 2026](#daniel-prol-2026)

## Evidence

### Daniel Prol 2026

Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944 [doi:10.48550/arxiv.2609.15944](https://doi.org/10.48550/arxiv.2609.15944)

`q2 · i?` · `design · r2`

Classroom deployment study of the Pulla tool in two courses (68 UH students, Spring 2026; 36 Aalto students, Summer 2026) solving three exception-handling Parsons problems. The authors report that "we identified common difficulty patterns, including misidentifying exception types, confusing return with the throw/raise mechanism, and incorrect control-flow ordering."

> "We deployed the tool in two university courses: an upper-division software design course at the University of Houston (United States) and an introductory programming course at Aalto University (Finland). By analyzing the data collected, we identified common difficulty patterns, including misidentifying exception types, confusing return with the throw/raise mechanism, and incorrect control-flow ordering."

## Discussion


## Related Claims
- [Control-flow ordering errors appeared across all UH problems (43–52% of incorrect attempts) but were only a secondary pattern at Aalto, with the conceptual barrier apparently shifting with problem structure](control-flow-ordering-errors-context-dependent.md) — a narrower finding that bears on this claim
- [Exception-type confusion was the dominant difficulty pattern in SafeDivide at the University of Houston (90% of incorrect attempts) and persisted across harder problems in both deployments](exception-type-confusion-dominant-pattern.md) — a narrower finding that bears on this claim
- [Students across both deployments substituted return statements for exception-raising constructs, treating error conditions as reasons to exit early](return-for-raise-substitution-pattern.md) — a narrower finding that bears on this claim
- [State revisits within solving sessions were rarer in the Pulla deployments (6–12% of UH sessions, 0–3% at Aalto) than the 21–33% previously reported for similar Parsons tasks](state-revisits-rare-in-pulla-deployments.md) — a narrower finding that bears on this claim
