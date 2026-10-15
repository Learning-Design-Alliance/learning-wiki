---
type: claim
title: "State revisits within solving sessions were rarer in the Pulla deployments (6–12% of UH sessions, 0–3% at Aalto) than the 21–33% previously reported for similar Parsons tasks"
description: "State revisits within solving sessions were rarer in the Pulla deployments (6–12% of UH sessions, 0–3% at Aalto) than the 21–33% previously reported for similar Parsons tasks"
id: state-revisits-rare-in-pulla-deployments
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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

# State revisits within solving sessions were rarer in the Pulla deployments (6–12% of UH sessions, 0–3% at Aalto) than the 21–33% previously reported for similar Parsons tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Between 6% and 12% of University of Houston solving sessions contained at least one state revisit, below the 21–33% reported by Helminen et al. for similar Parsons tasks; at Aalto, revisits were rare (0–3%) and absent in P3. [→ Daniel Prol 2026](#daniel-prol-2026)

## Evidence

### Daniel Prol 2026

Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944 [doi:10.48550/arxiv.2609.15944](https://doi.org/10.48550/arxiv.2609.15944)

`q2 · i?` · `design · r2`

Log analysis of solving-session traces across both deployments, illustrated by a state-transition graph of one UH student's 12-attempt sequence on P3 showing four regressions and two unproductive resubmissions. Sessions with "at least one state revisit" were 6–12% at UH and 0–3% at Aalto.

> "Across the University of Houston, between 6% and 12% of solving sessions contained at least one state revisit, below the 21–33% reported by Helminen et al. [7] for similar Parsons tasks; at Aalto University, revisits were rare (0–3% across problems) and absent in P3, the problem from which Figure 3 is drawn."

## Discussion


## Related Claims
- [Deploying a trace-capturing Parsons tool in two university courses surfaced recurring difficulty patterns including exception-type misidentification, return-for-throw confusion, and incorrect control-flow ordering](pulla-deployment-surfaced-recurring-difficulty-patterns.md) — a broader claim this one bears on
- [Control-flow ordering errors appeared across all UH problems (43–52% of incorrect attempts) but were only a secondary pattern at Aalto, with the conceptual barrier apparently shifting with problem structure](control-flow-ordering-errors-context-dependent.md) — related
- [Students across both deployments substituted return statements for exception-raising constructs, treating error conditions as reasons to exit early](return-for-raise-substitution-pattern.md) — related
- [Exception-type confusion was the dominant difficulty pattern in SafeDivide at the University of Houston (90% of incorrect attempts) and persisted across harder problems in both deployments](exception-type-confusion-dominant-pattern.md) — related
