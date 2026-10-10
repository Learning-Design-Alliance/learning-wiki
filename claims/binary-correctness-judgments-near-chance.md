---
type: claim
title: Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models
description: Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models
id: binary-correctness-judgments-near-chance
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
    kind: design
    rigour: 2
---

# Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Some VLMs' binary correctness QA scores hover closely around a 0.5 random baseline, and models variously overreport or overlook errors, with patterns not shared within model families. [→ Li Lucy 2026](#li-lucy-2026)

## Evidence

### Li Lucy 2026

Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925

`q2 · i?` · `design · r2`

Analysis splitting correctness & errors QA into generic (45.0%), binary (50.4%), and other (4.5%) subcategories for four representative VLMs, with GPT-5-mini annotating question type and gold correctness (validated at F1 = 0.975 and F1 = 0.925 on 200-example samples); 59.01% of 2,274 binary QA labeled as student-correct.

> "Figure 8 also indicates that some VLMs' binary QA scores hover closely around a random baseline of 0.5. Overall, assessing student error is incredibly challenging for VLMs, even though a substantial proportion of correctness & error QA in DrawEduMath have high by-chance floor for performance."

## Discussion


## Related Claims
- [Gold text descriptions improve VLM correctness-and-error assessment, but performance still lags other question types](captions-improve-correctness-qa-but-lag.md) — related
- [The performance gap between erroneous and non-erroneous student images persists after images are digitally redrawn to remove noise](error-gap-persists-after-image-cleanup.md) — related
- [VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem](vlms-underperform-on-erroneous-student-math-responses.md) — related
