---
type: claim
title: "Exception-type confusion was the dominant difficulty pattern in SafeDivide at the University of Houston (90% of incorrect attempts) and persisted across harder problems in both deployments"
description: "Exception-type confusion was the dominant difficulty pattern in SafeDivide at the University of Houston (90% of incorrect attempts) and persisted across harder problems in both deployments"
id: exception-type-confusion-dominant-pattern
status: review
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
  - id: daniel-prol-2026-2
    resource: "https://arxiv.org/abs/2609.15944"
    title: "Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944"
    author: Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Exception-type confusion was the dominant difficulty pattern in SafeDivide at the University of Houston (90% of incorrect attempts) and persisted across harder problems in both deployments

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` At the University of Houston, exception type confusion affected 90% of students with incorrect attempts on P1 and remained present on P2 (48%) and P3 (37%). [→ Daniel Prol 2026](#daniel-prol-2026)
`q2 i?` At Aalto University, 62% of incorrect attempts on safe_integer involved a broad or wrong exception class, and on safe_list (P3) most students with incorrect attempts (89%) selected an incorrect guard condition, reflecting confusion about when to raise. [→ Daniel Prol 2026 (2)](#daniel-prol-2026-2)

## Evidence

### Daniel Prol 2026

Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944 [doi:10.48550/arxiv.2609.15944](https://doi.org/10.48550/arxiv.2609.15944)

`q2 · i?` · `design · r2`

Log analysis of UH deployment attempts across the three Parsons problems. Trace data show "exception type confusion was the dominant pattern in P1, affecting 90% of students with incorrect attempts", with students placing semantically imprecise types where a more specific subtype was required.

> "At the University of Houston, exception type confusion was the dominant pattern in P1, affecting 90% of students with incorrect attempts, and remained present in P2 (48%) and P3 (37%): in each case students placed a semantically imprecise type, such asIllegalStateException, Exception, or RuntimeException, where a more specific subtype was required."

### Daniel Prol 2026 (2)

Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944

`q2 · i?` · `design · r2`

Log analysis of Aalto deployment attempts on the safe_list problem. The trace data show "most students with incorrect attempts (89%) selected an incorrect guard condition", choosing if index < 0 rather than the correct bound, which the authors read as confusion about when rather than which exception to raise.

> "in safe_list (P3), most students with incorrect attempts (89%) selected an incorrect guard condition. The dominant error in P3 was choosing if index < 0 rather than the correct bound if index < -len(items) , which is required to reject out-of-range negative indices."

## Discussion


## Related Claims
- [Control-flow ordering errors appeared across all UH problems (43–52% of incorrect attempts) but were only a secondary pattern at Aalto, with the conceptual barrier apparently shifting with problem structure](control-flow-ordering-errors-context-dependent.md) — related
- [Students across both deployments substituted return statements for exception-raising constructs, treating error conditions as reasons to exit early](return-for-raise-substitution-pattern.md) — related
- [Deploying a trace-capturing Parsons tool in two university courses surfaced recurring difficulty patterns including exception-type misidentification, return-for-throw confusion, and incorrect control-flow ordering](pulla-deployment-surfaced-recurring-difficulty-patterns.md) — a broader claim this one bears on
- [State revisits within solving sessions were rarer in the Pulla deployments (6–12% of UH sessions, 0–3% at Aalto) than the 21–33% previously reported for similar Parsons tasks](state-revisits-rare-in-pulla-deployments.md) — related
- [Students struggle with the 'not' operator and logical operator precedence when evaluating conditional statements](students-struggle-operator-precedence-conditionals.md) — related
