---
type: claim
title: Gold text descriptions improve VLM correctness-and-error assessment, but performance still lags other question types
description: Gold text descriptions improve VLM correctness-and-error assessment, but performance still lags other question types
id: captions-improve-correctness-qa-but-lag
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
    rigour: 2
---

# Gold text descriptions improve VLM correctness-and-error assessment, but performance still lags other question types

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Appending gold natural language descriptions improves VLM performance on correctness & errors QA, yet captioned performance remains below captionless performance on all other question categories for the same images. [→ Li Lucy 2026](#li-lucy-2026)

## Evidence

### Li Lucy 2026

Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925

`q2 · i?` · `causal · r2`

Experiment re-evaluating four representative VLMs on correctness & errors QA with gold teacher captions appended, after removing 262 of 2,030 images whose captions contained correctness content; a caption-then-answer setup with model-generated captions approached but did not match gold captions (Figure 7). No effect size printed.

> "Results are in the expected direction, in that VLM performance on correctness & errors QA improves with natural language support (Figure 7). However, this improved performance on correctness & errors QA with captions still lags behind VLMs' captionless performance in all other question categories for the same set of images."

## Discussion


## Related Claims
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](binary-correctness-judgments-near-chance.md) — related
- [The performance gap between erroneous and non-erroneous student images persists after images are digitally redrawn to remove noise](error-gap-persists-after-image-cleanup.md) — related
- [VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem](vlms-underperform-on-erroneous-student-math-responses.md) — related
