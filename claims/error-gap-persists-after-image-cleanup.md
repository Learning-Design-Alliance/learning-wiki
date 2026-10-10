---
type: claim
title: The performance gap between erroneous and non-erroneous student images persists after images are digitally redrawn to remove noise
description: The performance gap between erroneous and non-erroneous student images persists after images are digitally redrawn to remove noise
id: error-gap-persists-after-image-cleanup
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
    kind: causal
    rigour: 1
---

# The performance gap between erroneous and non-erroneous student images persists after images are digitally redrawn to remove noise

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Differences in average content-description scores between erroneous and non-erroneous student images persist after standardized digital redrawing, across four representative VLMs. [→ Li Lucy 2026](#li-lucy-2026)

## Evidence

### Li Lucy 2026

Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925

`q2 · i?` · `causal · r1`

Experiment in which the lead author digitally redrew one erroneous and one correct response per problem, yielding 336 images; Table 2 prints per-model score differences on original versus redrawn images, e.g. Gemini 2.5 Pro -0.089*** to -0.096***, with significance markers but no standardized effect size.

> "Differences in average scores on content description QA between erroneous and non-erroneous student images persist after redrawing. ** p <0.01 , ***p<0.001."

## Discussion


## Related Claims
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](binary-correctness-judgments-near-chance.md) — related
- [Gold text descriptions improve VLM correctness-and-error assessment, but performance still lags other question types](captions-improve-correctness-qa-but-lag.md) — related
- [The LWPA advantage on the End-of-Unit exam persists after removing oral comprehension scores](lwpa-advantage-persists-without-oral-comprehension.md) — related
- [VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem](vlms-underperform-on-erroneous-student-math-responses.md) — related
