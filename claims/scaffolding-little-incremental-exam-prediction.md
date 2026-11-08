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
newest_evidence: 2026
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
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

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
- [Dialogue act features raise regression R² but do not significantly improve outcome prediction over a prior-performance baseline](da-features-not-significant-over-baseline.md) — related
- [Interaction depth is not associated with immediate recall or gains once baseline knowledge is controlled](depth-not-associated-with-immediate-recall.md) — related
- [Static whole-session summaries of AI use add no detectable post-test variance beyond pre-test performance](static-ai-use-features-no-incremental-posttest-variance.md) — related
- [Predictor variables beyond prior achievement and school track add predictive value for next-year math achievement, with the smallest added effects for the final-year outcome](predictors-beyond-prior-achievement-add-predictive-value.md) — related
- [In regression models, prior attainment and background explained most variation, with treatment adding little beyond pupil prior characteristics](future-foundations-regression-treatment-small.md) — related
- [Symbolic-regression models built on previous exam grades account for roughly 70% of exam-score variation, but predict project scores poorly (about 35%)](exam-scores-predictable-project-scores-not.md) — related
- [Attitude, Motivation, and Test Strategies subscales did not predict academic outcomes in this sample](attitude-motivation-test-strategies-no-prediction.md) — related
- [AI-context variables and personality traits add incremental variance to self-directed learning beyond covariates, but personality-trait × AI-dimension interactions add only a substantively small increment](hierarchical-regression-incremental-variance-sdl.md) — related
- [No predictors reached conventional statistical significance for academic referral status in the multivariable logistic regression](no-significant-predictors-referral-status-ghana-nursing.md) — related
- [Written knowledge-test scores explain only a small share of overall OSCE score variability in both groups (11% comparator, 14% intervention)](written-test-score-small-share-osce-variance.md) — related
- [Demographics and study approaches together explain 27.5% of exam grade variance, with learning environment adding little](grade-variance-27-percent-model-ot.md) — related
