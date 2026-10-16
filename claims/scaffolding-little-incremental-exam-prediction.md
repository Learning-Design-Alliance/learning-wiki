---
type: claim
title: Scaffolding level provides no consistent additional predictive information about subsequent exam performance beyond prior achievement and observed dialogue behavior
description: Scaffolding level provides no consistent additional predictive information about subsequent exam performance beyond prior achievement and observed dialogue behavior
id: scaffolding-little-incremental-exam-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: suhyeon-lee-2026
    resource: "https://doi.org/10.48550/arxiv.2608.22993"
    title: "Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin. (2026). LLM Pedagogical Behavior in AI Tutoring Interactions. https://arxiv.org/abs/2608.22993 [doi:10.48550/arxiv.2608.22993](https://doi.org/10.48550/arxiv.2608.22993)"
    author: Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: suhyeon-lee-2026-2
    resource: "https://arxiv.org/abs/2608.22993"
    title: "Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin. (2026). LLM Pedagogical Behavior in AI Tutoring Interactions. https://arxiv.org/abs/2608.22993"
    author: Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Scaffolding level provides no consistent additional predictive information about subsequent exam performance beyond prior achievement and observed dialogue behavior

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Adding mean scaffolding level to regression models of exam scores increased explained variance by only 1–2 percentage points, none of the three model comparisons reached conventional statistical significance, and the estimated scaffolding coefficient changed direction for e3. [→ Suhyeon Lee 2026](#suhyeon-lee-2026)
`q2 i?` Alternative specifications using counts of Solving responses or low-assistance responses also reached no conventional statistical significance for any exam. [→ Suhyeon Lee 2026 (2)](#suhyeon-lee-2026-2)

## Evidence

### Suhyeon Lee 2026

Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin. (2026). LLM Pedagogical Behavior in AI Tutoring Interactions. https://arxiv.org/abs/2608.22993 [doi:10.48550/arxiv.2608.22993](https://doi.org/10.48550/arxiv.2608.22993)

`q2 · i?` · `associational · r2`

Regression analysis of exam scores for 147–173 students with assessment data, comparing baseline models (prior performance and dialogue-act counts) with full models adding mean scaffolding level; baseline models explained approximately 12–30% of variance.

> "Adding mean scaffolding increases explained variance by only 1–2 percentage points. None of the three model comparisons reaches conventional statistical significance (Table 4), and the estimated scaffolding coefficient changes direction for e3."

### Suhyeon Lee 2026 (2)

Suhyeon Lee, Juneha Baek, Jaehyeong Park, Donghyuk Shin. (2026). LLM Pedagogical Behavior in AI Tutoring Interactions. https://arxiv.org/abs/2608.22993

`q2 · i?` · `associational · r2`

Appendix C sensitivity analysis replacing mean scaffolding with counts of L4 (Solving) and L0–L2 (low-assistance) responses received before each exam; ΔR² values ranged from +.000 to +.007.

> "Neither alternative scaffolding predictor reaches conventional statistical significance for any exam. Both representations add little explained variance, consistent with the main analysis using mean scaffolding level."

## Discussion

## Related Claims

- [Scaffolding improves learning](scaffolding-improves-learning.md) — the general claim this finding bears on, with the studies behind it
- [A general-purpose LLM used as a tutor without pedagogical prompting overwhelmingly provides high assistance, with more than 95% of responses classified as Explaining or Solving](default-llm-tutoring-high-assistance-concentration.md) — related
- [Explanation-seeking interaction depth is positively associated with task quality beyond baseline knowledge and volume](depth-predicts-task-quality.md) — related
- [The largest OSCE-domain improvement from multi-agent scaffolding was in communication performance](communication-largest-osce-gain.md) — related
- [The largest checklist-item gain from multi-agent scaffolding was in observable empathic expression, with additional gains in selected history-taking items](empathy-checklist-item-largest-gain.md) — related
- [PTA traits show stronger statistical explanatory power than dialogue-act and Bloom's taxonomy coded baselines on StudyChat](pta-traits-beat-dialogue-act-bloom-baselines.md) — related
- [PTA-derived traits significantly improve explained exam-score variance over a prior-outcome baseline in one semester of StudyChat but not the other](pta-traits-explain-studychat-exam-variance-semester-inconsistent.md) — related
