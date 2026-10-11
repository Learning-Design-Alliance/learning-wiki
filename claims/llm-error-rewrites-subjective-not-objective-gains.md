---
type: claim
title: LLM-rewritten Python error messages improved subjective evaluations but did not reliably improve objective debugging performance
description: LLM-rewritten Python error messages improved subjective evaluations but did not reliably improve objective debugging performance
id: llm-error-rewrites-subjective-not-objective-gains
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alexandru-radu-moraru-2026
    resource: "https://arxiv.org/abs/2608.20896"
    title: "Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju. (2026). Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors. https://arxiv.org/abs/2608.20896"
    author: Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM-rewritten Python error messages improved subjective evaluations but did not reliably improve objective debugging performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Participants rated LLM-rewritten messages more favorably than standard interpreter messages, but objective outcomes such as fix rate, time-to-fix, and Fix@k did not provide strong evidence that rewritten messages improved repair performance. [→ Alexandru-Radu Moraru 2026](#alexandru-radu-moraru-2026)

## Evidence

### Alexandru-Radu Moraru 2026

Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju. (2026). Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors. https://arxiv.org/abs/2608.20896

`q2 · i?` · `causal · r2`

Main Prolific experiment with 103 valid participants, each assigned one of four calibrated buggy Python snippets and one of three message styles (35 standard, 35 pragmatic, 33 contingent). The authors report that "objective outcomes such as fix rate, time-to-fix, and Fix@k were more variable" without reliable improvement.

> "In contrast, objective outcomes such as fix rate, time-to-fix, and Fix@k were more variable and did not provide strong evidence that rewritten messages reliably improved repair performance."

## Discussion


## Related Claims
- [Fix rate varied substantially across buggy snippets, with snippet A lowest because the standard interpreter message pointed to the non-offending line](fix-rate-varies-by-snippet-misleading-message.md) — related
- [Scores on the debugging-oriented Python proficiency assessment moderately predict successful code repair](proficiency-assessment-predicts-fix-success.md) — related
- [Descriptive time-to-fix patterns favored pragmatic messages, but statistical tests found no significant effects](time-to-fix-descriptive-favor-llm-not-significant.md) — related
- [Both LLM rewrite styles were rated less authoritative than standard interpreter messages](llm-rewrites-rated-less-authoritative.md) — related
- [Pragmatic and contingent LLM rewrites reduced perceived cognitive load relative to standard interpreter messages](llm-rewrites-lower-perceived-cognitive-load.md) — related
