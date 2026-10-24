---
type: claim
title: Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models
description: Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models
id: binary-correctness-judgments-near-chance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: li-lucy-2026
    resource: "https://doi.org/10.48550/arxiv.2603.00925"
    title: "Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925 [doi:10.48550/arxiv.2603.00925](https://doi.org/10.48550/arxiv.2603.00925)"
    author: Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Some VLMs' binary correctness QA scores hover closely around a 0.5 random baseline, and models variously overreport or overlook errors, with patterns not shared within model families. [→ Li Lucy 2026](#li-lucy-2026)

## Evidence

### Li Lucy 2026

Li Lucy, Albert Zhang, Nathan Anderson, Ryan Knight, Kyle Lo. (2026). The Aftermath of DrawEduMath: Vision Language Models Underperform with Struggling Students and Misdiagnose Errors. https://arxiv.org/abs/2603.00925 [doi:10.48550/arxiv.2603.00925](https://doi.org/10.48550/arxiv.2603.00925)

`q2 · i?` · `design · r2`

Analysis splitting correctness & errors QA into generic (45.0%), binary (50.4%), and other (4.5%) subcategories for four representative VLMs, with GPT-5-mini annotating question type and gold correctness (validated at F1 = 0.975 and F1 = 0.925 on 200-example samples); 59.01% of 2,274 binary QA labeled as student-correct.

> "Figure 8 also indicates that some VLMs' binary QA scores hover closely around a random baseline of 0.5. Overall, assessing student error is incredibly challenging for VLMs, even though a substantial proportion of correctness & error QA in DrawEduMath have high by-chance floor for performance."

## Discussion

## Related Claims

- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) — the general claim this finding bears on, with the studies behind it
- [Gold text descriptions improve VLM correctness-and-error assessment, but performance still lags other question types](captions-improve-correctness-qa-but-lag.md) — related
- [The performance gap between erroneous and non-erroneous student images persists after images are digitally redrawn to remove noise](error-gap-persists-after-image-cleanup.md) — related
- [VLMs achieve higher accuracy on non-erroneous than erroneous student math responses even when controlling for the math problem](vlms-underperform-on-erroneous-student-math-responses.md) — related
- [FSM-based evaluation aligns with human judgments of interactivity, functional correctness, and visual quality more strongly than VLM and unit-test baselines on balanced data](fsm-eval-aligns-with-human-interactivity-judgments.md) — related
- [VLMs show a common grounding failure: coarse semantic relevance without precise region-activity binding and entity-evidence alignment](vlm-grounding-failure-region-activity-binding.md) — related
- [VLM performance on artistic educational imagery is highly task-dependent, with no model dominating across capabilities](vlm-performance-task-dependent-muse.md) — a broader claim this one bears on
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) — related
- [GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)](llm-communication-grading-insufficient-alignment-ttx.md) — related
