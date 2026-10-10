---
type: claim
title: "After training, tutors were significantly more likely to encounter pedagogical opportunities (61.1% to 68.9%) and showed higher execution quality within those opportunities (65.5% to 68.1%)"
description: "After training, tutors were significantly more likely to encounter pedagogical opportunities (61.1% to 68.9%) and showed higher execution quality within those opportunities (65.5% to 68.1%)"
id: post-training-opportunity-and-execution-gains
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: thomas-2026
    resource: "https://arxiv.org/abs/2606.18617"
    title: "Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R. (2026). AI-Driven Assessment of Human Tutors: Linking Training Performance to Real-Life Practice. https://arxiv.org/abs/2606.18617"
    author: "Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R."
    q: 3
    i: "?"
    kind: causal
    rigour: 1
  - id: thomas-2026-2
    resource: "https://arxiv.org/abs/2606.18617"
    title: "Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R. (2026). AI-Driven Assessment of Human Tutors: Linking Training Performance to Real-Life Practice. https://arxiv.org/abs/2606.18617"
    author: "Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R."
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# After training, tutors were significantly more likely to encounter pedagogical opportunities (61.1% to 68.9%) and showed higher execution quality within those opportunities (65.5% to 68.1%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q3`

## Subclaims
`q3 i?` The probability of having an opportunity to execute a target tutor move rose from 61.1% pre-training to 68.9% post-training (binomial test, p<.001). [→ Thomas 2026](#thomas-2026)
`q3 i?` Conditional on having an opportunity, tutors' probability of successfully executing the target move increased from 65.5% to 68.1% (p=.003). [→ Thomas 2026 (2)](#thomas-2026-2)

## Evidence

### Thomas 2026

Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R. (2026). AI-Driven Assessment of Human Tutors: Linking Training Performance to Real-Life Practice. https://arxiv.org/abs/2606.18617

`q3 · i?` · `causal · r1`

Pre-post comparison of AI-identified opportunities in real-life tutoring transcripts using a binomial test. The article reports the percentages and p<.001; no standardized effect size is printed.

> "The probability of having an opportunity to execute a target tutoring move was higher post-training than pre-training (post: 68.9% vs. pre: 61.1%), a difference that was statistically significant (binomial test,p<.001)."

### Thomas 2026 (2)

Thomas, D. R., Kamikazi, M. C. A., Brandt, C., Borchers, C., & Koedinger, K. R. (2026). AI-Driven Assessment of Human Tutors: Linking Training Performance to Real-Life Practice. https://arxiv.org/abs/2606.18617

`q3 · i?` · `causal · r1`

Pre-post comparison of execution quality within opportunities, scored by the two-stage LLM transcript pipeline. The article reports 65.5% to 68.1% with p=.003; no effect size is printed.

> "Conditional on having an opportunity, tutors' probability of successfully executing the target move also increased from pre- to post-training (65.5% to 68.1%;p=.003)."

## Discussion


## Related Claims
- [Repeated opportunities to apply tutor moves did not by themselves improve execution: opportunity count, lesson completion, and their interaction showed no significant effects on successful execution](opportunity-count-no-effect-execution.md) — related
- [Interrupted time series analysis found tutor quality improved gradually over time (β=0.01, p=.022) with no immediate level change or slope change at the training intervention](its-gradual-trend-not-intervention-effect.md) — related
- [In a large-scale RCT, real-time LLM-generated pedagogical suggestions for human tutors raised student knowledge-component mastery by 4 percentage points on average, with larger effects for lower-performing or less-experienced tutors](llm-suggestions-human-tutors-mastery-gain.md) — related
