---
type: claim
title: Under persona simulation with hidden ground-truth mastery, Adaptive sessions yield lower final-belief mastery MAE (0.12) than Random-topic (0.16) and Frozen (0.20) controls, and belief updates shrink as estimates converge
description: Under persona simulation with hidden ground-truth mastery, Adaptive sessions yield lower final-belief mastery MAE (0.12) than Random-topic (0.16) and Frozen (0.20) controls, and belief updates shrink as estimates conv...
id: collearn-adaptive-mastery-mae-convergence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: kailai-he-2026
    resource: "https://arxiv.org/abs/2609.21154"
    title: "Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154"
    author: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: kailai-he-2026-2
    resource: "https://arxiv.org/abs/2609.21154"
    title: "Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154"
    author: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Under persona simulation with hidden ground-truth mastery, Adaptive sessions yield lower final-belief mastery MAE (0.12) than Random-topic (0.16) and Frozen (0.20) controls, and belief updates shrink as estimates converge

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Final-belief mastery MAE is lowest under Adaptive (0.12 vs 0.16/0.20) in the 6-persona Claude Sonnet 4.5-graded run. [→ Kailai He 2026](#kailai-he-2026)
`q2 i?` Mean update magnitude |Δp| shrinks across the six Adaptive persona sessions (0.14→0.10) but stays flat or drifts upward under both controls. [→ Kailai He 2026 (2)](#kailai-he-2026-2)

## Evidence

### Kailai He 2026

Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154

`q2 · i?` · `design · r2`

Persona-simulation run (6 personas, 132 rounds) driving the live grading and BKT services with hidden ground-truth mastery; the article reports "mastery MAE is lowest underAdaptive( 0.12 vs. 0.16/0.20; Table 2)".

> "belief mastery MAE is lowest underAdaptive( 0.12 vs. 0.16/0.20; Table 2), and the per-learner belief error|ˆp−p∗| falls in step (Figure 3a)."

### Kailai He 2026 (2)

Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154

`q2 · i?` · `design · r2`

Secondary aggregate signal from the same 6-persona simulation: the article reports that "mean|∆p| shrinks across the sixAdaptivepersona sessions ( 0.14→0.10 )" while both controls stay flat or drift upward.

> "mean|∆p| shrinks across the sixAdaptivepersona sessions ( 0.14→0.10 ) but stays flat or drifts upward under both controls (Figure 3b)."

## Discussion


## Related Claims
- [In a preliminary 2×3 controlled lesson study across five backbone LLMs, structured student agents produce more differentiated mastery and misconception traces than a baseline simulator](structured-student-agents-differentiated-mastery-traces.md) — related
- [In LLM-simulated subjects with known skill levels, the Executive LLM yields better skill-level recovery (lower MAE) than Independent Agents](executive-llm-improves-skill-recovery-simulation.md) — related
