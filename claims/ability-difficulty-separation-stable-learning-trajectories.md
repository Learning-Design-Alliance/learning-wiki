---
type: claim
title: Separating ability estimation from correctness prediction yields smoother, more stable learning trajectories than probability-based mastery estimation
description: Separating ability estimation from correctness prediction yields smoother, more stable learning trajectories than probability-based mastery estimation
id: ability-difficulty-separation-stable-learning-trajectories
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: shuyan-huang-2026
    resource: "https://arxiv.org/abs/2605.01097"
    title: "Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan. (2026). Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student Dialogues. arXiv preprint. https://arxiv.org/abs/2605.01097"
    author: Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Separating ability estimation from correctness prediction yields smoother, more stable learning trajectories than probability-based mastery estimation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Unlike LLMKT, whose predicted correctness probability oscillates across KC occurrences, the framework's estimated ability consistently increases with repeated KC occurrences, with correctness fluctuations tracking changes in task difficulty. [→ Shuyan Huang 2026](#shuyan-huang-2026)

## Evidence

### Shuyan Huang 2026

Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Andrew Lan. (2026). Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student Dialogues. arXiv preprint. https://arxiv.org/abs/2605.01097

`q2 · i?` · `design · r2`

Learning-curve analysis on QATD2k for the three most frequent KCs (Figure 4): LLMKT "exhibits noticeable oscillations across KC occurrences," while the framework's ability estimates rise monotonically, which the authors say aligns with cognitive theories of gradual learning. No effect size is printed.

> "our framework separates ability estimation from correctness prediction, resulting in smoother and more stable learning trajectories. The esti- mated student ability consistently increases with re- peated KC occurrences across all three KCs"

## Discussion


## Related Claims
-
