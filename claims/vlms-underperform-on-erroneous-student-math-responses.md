---
type: claim
title: VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem
description: VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem
id: vlms-underperform-on-erroneous-student-math-responses
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: li-lucy-2026
    resource: "https://arxiv.org/abs/2603.00925"
    title: "Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925"
    author: Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Across 11 VLMs evaluated on DrawEduMath, non-erroneous student responses significantly correspond with higher content-description accuracy after problem fixed effects are applied. [→ Li Lucy 2026](#li-lucy-2026)

## Evidence

### Li Lucy 2026

Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925

`q2 · i?` · `associational · r2`

Ordinary least squares regression with problem fixed effects over DrawEduMath content description QA for 11 VLMs, contrasting erroneous and non-erroneous student responses; the article prints per-model β1 estimates, and reports "all p<1.0 −12" in Table 1, with no standardized effect size.

> "These values show that even after controlling for prob- lem, non-erroneous student responses significantly correspond with higher VLM performance."

## Discussion


## Related Claims
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](binary-correctness-judgments-near-chance.md) — related
- [Gold text descriptions improve VLM correctness-and-error assessment, but performance still lags other question types](captions-improve-correctness-qa-but-lag.md) — related
- [The performance gap between erroneous and non-erroneous student images persists after images are digitally redrawn to remove noise](error-gap-persists-after-image-cleanup.md) — related
