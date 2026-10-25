---
type: claim
title: Student specification comments are predominantly natural language, except Return statements which show a high proportion of Strict-Code expressions
description: Student specification comments are predominantly natural language, except Return statements which show a high proportion of Strict-Code expressions
id: natural-language-except-strict-code-returns
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: rq1-expr
    title: rq1-expr
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Student specification comments are predominantly natural language, except Return statements which show a high proportion of Strict-Code expressions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Comments were predominantly expressed in natural language across constructs, with Return statements the exception showing a fairly high proportion of Strict-Code expressions. [→ rq1-expr](#rq1-expr)

## Evidence

### rq1-expr

Nasser Giacaman, Valerio Terragni, Paul Denny, and Viraj Kumar. 2026. Commenting with Copilot: A Taxonomy and Multi-Year Analysis of Student Code-Generation Specifications. Proceedings of the 2nd ACM Virtual Global Computing Education Conference (SIGCSE Virtual 2026). https://doi.org/10.48550/arXiv.2607.10674

`q2 · i?` · `associational · r2`

Aggregate expression-level analysis of classified comments from the four-year Copilot activity (Table 1). Overall, 90.6% of comments were Natural-Language, 5.6% Strict-Code, and 2.2% Code-Like; for Return constructs 36.7% were Strict-Code. No effect size is printed.

> "Comments were predominantly expressed in natural language, except forReturnstatements, which showed a fairly high proportion ofStrict-Codeexpressions."

## Discussion


## Related Claims
- [Students shift toward How comments for procedural constructs: 94.3% of Multi-Step-Block and 57.3% of Loop-Iteration comments were How comments](how-comments-procedural-constructs-shift.md) — related
- [Students across both deployments substituted return statements for exception-raising constructs, treating error conditions as reasons to exit early](return-for-raise-substitution-pattern.md) — related
- [Deploying a trace-capturing Parsons tool in two university courses surfaced recurring difficulty patterns including exception-type misidentification, return-for-throw confusion, and incorrect control-flow ordering](pulla-deployment-surfaced-recurring-difficulty-patterns.md) — related
