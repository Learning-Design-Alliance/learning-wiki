---
type: claim
title: Descriptive time-to-fix patterns favored pragmatic messages, but statistical tests found no significant effects
description: Descriptive time-to-fix patterns favored pragmatic messages, but statistical tests found no significant effects
id: time-to-fix-descriptive-favor-llm-not-significant
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: alexandru-radu-moraru-2026
    resource: "https://doi.org/10.48550/arxiv.2608.20896"
    title: "Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju. (2026). Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors. https://arxiv.org/abs/2608.20896 [doi:10.48550/arxiv.2608.20896](https://doi.org/10.48550/arxiv.2608.20896)"
    author: Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Descriptive time-to-fix patterns favored pragmatic messages, but statistical tests found no significant effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Averaged across skill levels, participants fixed errors fastest with pragmatic messages, and both LLM styles tended to speed fixes versus standard, but statistical tests found no significant effects. [→ Alexandru-Radu Moraru 2026](#alexandru-radu-moraru-2026)

## Evidence

### Alexandru-Radu Moraru 2026

Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju. (2026). Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors. https://arxiv.org/abs/2608.20896 [doi:10.48550/arxiv.2608.20896](https://doi.org/10.48550/arxiv.2608.20896)

`q2 · i?` · `causal · r2`

Time-to-fix analysis of the main Prolific experiment, split by skill level; Figure 4 reports descriptive means (Standard M=415.69, Pragmatic M=324.56, Contingent M=423.85 seconds), but "statistical tests found no significant effects".

> "With few novice successes (standard𝑛=6, pragmatic𝑛=7, contingent𝑛=5), statistical tests found no significant effects, though the current pattern seems to favor LLM explanations."

## Discussion


## Related Claims
- [LLM-rewritten Python error messages improved subjective evaluations but did not reliably improve objective debugging performance](llm-error-rewrites-subjective-not-objective-gains.md) — related
- [Pragmatic and contingent LLM rewrites reduced perceived cognitive load relative to standard interpreter messages](llm-rewrites-lower-perceived-cognitive-load.md) — related
- [Both LLM rewrite styles were rated less authoritative than standard interpreter messages](llm-rewrites-rated-less-authoritative.md) — related
- Delayed final-exam differences favored Guided-LLM descriptively but were not statistically confirmatory, with confidence intervals including zero — related
- [Fix rate varied substantially across buggy snippets, with snippet A lowest because the standard interpreter message pointed to the non-offending line](fix-rate-varies-by-snippet-misleading-message.md) — related
- [Scores on the debugging-oriented Python proficiency assessment moderately predict successful code repair](proficiency-assessment-predicts-fix-success.md) — related
