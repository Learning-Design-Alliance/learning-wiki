---
type: claim
title: Students across both deployments substituted return statements for exception-raising constructs, treating error conditions as reasons to exit early
description: Students across both deployments substituted return statements for exception-raising constructs, treating error conditions as reasons to exit early
id: return-for-raise-substitution-pattern
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

# Students across both deployments substituted return statements for exception-raising constructs, treating error conditions as reasons to exit early

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` At the University of Houston, 60% of students with incorrect attempts on SafeDivide (P1) placed a return statement rather than throwing an exception, and 47% substituted return for throw on P3. [→ Daniel Prol 2026](#daniel-prol-2026)
`q2 i?` At Aalto University, 50% of students with incorrect attempts on safe_integer (P2) substituted return for raise ValueError, treating a parse failure as a silent exit. [→ Daniel Prol 2026 (2)](#daniel-prol-2026-2)

## Evidence

### Daniel Prol 2026

Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944 [doi:10.48550/arxiv.2609.15944](https://doi.org/10.48550/arxiv.2609.15944)

`q2 · i?` · `design · r2`

Log analysis of UH deployment attempts on the SafeDivide and CheckedVsUnchecked Parsons problems. The trace data show "60% of students with incorrect attempts placed if (b == 0) return 0" instead of throwing, and 47% substituted return for throw on P3.

> "At the University of Houston (𝑛= 68), 60% of students with incorrect attempts placed if (b == 0) return 0 in SafeDivide (P1) rather than throw new ArithmeticException(. . . ) , and 47% substitutedreturn for throw in CheckedVsUnchecked (P3)."

### Daniel Prol 2026 (2)

Daniel Prol, Juho Leinonen, Arto Hellas, Saleh Alkhamees, Amin Alipour. (2026). Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis. arXiv. https://arxiv.org/abs/2609.15944

`q2 · i?` · `design · r2`

Log analysis of the Aalto CS1 deployment on the safe_integer Parsons problem. Among students with incorrect attempts, "50% of students with incorrect attempts substituted return for raise ValueError", which the authors interpret as treating the error as a silent exit rather than an exceptional event.

> "At Aalto University, this pattern was prominent insafe_integer (P2), where 50% of students with incorrect attempts substituted return for raise ValueError , treating a parse failure as a silent exit rather than an exceptional event."

## Discussion


## Related Claims
- [Exception-type confusion was the dominant difficulty pattern in SafeDivide at the University of Houston (90% of incorrect attempts) and persisted across harder problems in both deployments](exception-type-confusion-dominant-pattern.md) — related
- [Deploying a trace-capturing Parsons tool in two university courses surfaced recurring difficulty patterns including exception-type misidentification, return-for-throw confusion, and incorrect control-flow ordering](pulla-deployment-surfaced-recurring-difficulty-patterns.md) — a broader claim this one bears on
- [Control-flow ordering errors appeared across all UH problems (43–52% of incorrect attempts) but were only a secondary pattern at Aalto, with the conceptual barrier apparently shifting with problem structure](control-flow-ordering-errors-context-dependent.md) — related
- [State revisits within solving sessions were rarer in the Pulla deployments (6–12% of UH sessions, 0–3% at Aalto) than the 21–33% previously reported for similar Parsons tasks](state-revisits-rare-in-pulla-deployments.md) — related
- [Student specification comments are predominantly natural language, except Return statements which show a high proportion of Strict-Code expressions](natural-language-except-strict-code-returns.md) — related
