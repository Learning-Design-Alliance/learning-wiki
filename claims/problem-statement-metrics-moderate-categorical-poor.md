---
type: claim
title: Core problem-statement metrics show only moderate judge agreement, and multi-class metrics (Bloom level, difficulty) perform poorly
description: Core problem-statement metrics show only moderate judge agreement, and multi-class metrics (Bloom level, difficulty) perform poorly
id: problem-statement-metrics-moderate-categorical-poor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tobias-geisler-and-gerd-kortemeyer-2026
    resource: "https://doi.org/10.1103/9hh9-vt4d"
    title: "Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)"
    author: Tobias Geisler and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: tobias-geisler-and-gerd-kortemeyer-2026-2
    resource: "https://doi.org/10.1103/9hh9-vt4d"
    title: "Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)"
    author: Tobias Geisler and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Core problem-statement metrics show only moderate judge agreement, and multi-class metrics (Bloom level, difficulty) perform poorly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Task-clarity metrics such as task-is-solvable, task-is-clear, and task-is-specific-and-complete cluster around F1 values near 0.57–0.61, missing roughly 40% of edge cases. [→ Tobias Geisler and Gerd Kortemeyer 2026](#tobias-geisler-and-gerd-kortemeyer-2026)
`q2 i?` All five categorical metrics fall below F1 0.50, including bloom-level-of-exercise at 0.40 and exercise-difficulty-level at 0.23. [→ Tobias Geisler and Gerd Kortemeyer 2026 (2)](#tobias-geisler-and-gerd-kortemeyer-2026-2)

## Evidence

### Tobias Geisler and Gerd Kortemeyer 2026

Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)

`q2 · i?` · `associational · r1`

LLM-as-a-judge benchmark against expert ground truth (Results, Table V context). The article reports F1 values "near 0 .57 − 0.61" for the core problem-statement metrics; no effect size is printed.

> "Metrics such as task-is-solvable, task-is-clear, and task-is-specific-and-complete cluster around F1 values near 0 .57 − 0.61, meaning they correctly flag most instances but still miss roughly 40 % of edge cases."

### Tobias Geisler and Gerd Kortemeyer 2026 (2)

Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)

`q2 · i?` · `design · r2`

Same judge benchmark. The article reports bloom-level-of-exercise at 0.40 and exercise-difficulty-level at 0 .23 macro F1, and Figure 7 shows expert and AI difficulty distributions diverge, with the AI defaulting to foundational.

> "Multi-category labels perform even more poorly: all five categorical metrics, including bloom-level-of-exercise at 0.40 and exercise-difficulty-level at 0 .23, fall well below the 0 .50-mark."

## Discussion


## Related Claims
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — a broader claim this one bears on
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [For radio-button problems, cognitive-demand metrics (Bloom level, difficulty, distinct misconceptions) are the strongest random-forest predictors of student choice](radio-choice-predictors-cognitive-demand.md) — related
