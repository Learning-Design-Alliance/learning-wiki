---
type: claim
title: Testing Effect Improves Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: testing-effect-improves-learning
evidence_strength: strong
sources:
  - id: rowland-2014
    resource: "https://doi.org/10.1037/a0037559"
    title: "Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)"
    author: Rowland, C. A.
    q: 4
    i: 2
    n: 159 effect sizes from 61 studies
  - id: roediger-and-karpicke-2006
    resource: "https://doi.org/10.1111/j.1467-9280.2006.01693.x"
    title: "Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)"
    author: "Roediger, H. L., & Karpicke, J. D."
    q: 3
    i: 3
    n: 300 undergraduates (120 + 180)
---

# Testing Effect Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i2`–`i3`

Retrieving information from memory (being tested) strengthens long-term retention more than restudying the same material for the same amount of time.

## Subclaims

`q4 i2` Across 159 effect sizes from 61 studies, taking a practice test produced better retention than restudying the same material. The benefit was larger after delays of one day or more, and when the initial test used recall or gave feedback. With no feedback and initial test performance of 50% or below, the benefit was about zero. [→ Rowland 2014](#rowland-2014)

`q3 i3` With prose passages, students who recalled the material outperformed students who restudied it on tests two days and one week later. On a test five minutes later, restudying was ahead. [→ Roediger and Karpicke 2006](#roediger-and-karpicke-2006)

## Evidence

### Rowland 2014

Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)

`q4 · meta-analysis` · `i2 · medium effect, g=0.50` · `n=159 effect sizes from 61 studies`

This random-effects meta-analysis covers 159 effect sizes from 61 studies reported between 1975 and 2013. Each effect compares information that learners were tested on with information they restudied. The mean weighted effect was g = 0.50 (95% CI 0.42 to 0.58), and heterogeneity was high. The effect was larger at retention intervals of at least one day (g = 0.69) than below one day (g = 0.41). It was also larger when the initial test gave [feedback](../elements/feedback.md) (g = 0.73 against 0.39 without) and when the initial test was cued recall rather than recognition (0.61 against 0.29). With no feedback and initial test performance of 50% or below, the effect was about zero (g = 0.03, CI −0.21 to 0.27). Published studies showed larger effects than unpublished ones (0.58 against 0.25), so the author advises caution about publication bias.

### Roediger and Karpicke 2006

Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)

`q3 · peer-reviewed experiment (two experiments)` · `i3 · large effect, d=0.83 at 1 week (Exp. 1)` · `n=300 undergraduates (120 + 180)`

Undergraduates at Washington University read short science passages. In Experiment 1 (120 students), they either restudied a passage or took a free-recall test on it, without feedback. At five minutes, restudying did better (81% against 75% recalled). At two days, testing did better (68% against 54%, d = 0.95), and at one week also (56% against 42%, d = 0.83). In Experiment 2 (180 students), one study period followed by three recall tests beat four study periods on the one-week test (61% against 40%, d = 1.26). Repeated study scored best at five minutes and made students more confident they would remember, but it did worst at one week.

## Discussion

**Mechanism.** The dominant explanation is that successful retrieval modifies the underlying memory trace, making it more accessible later, and that the effortful, error-prone character of retrieval — unlike passive rereading — is what drives the benefit. Retrieval also functions as a diagnostic: it exposes gaps that restudying conceals, which supports subsequent study decisions and connects to [Assessment for Learning](../principles/assessment-for-learning.md).

**Boundary conditions.** The benefit depends on retrieval success and feedback. Tests that learners largely fail, or that provide no corrective feedback, can entrench errors rather than strengthen correct knowledge [-M]. The effect is strongest when retrieval is effortful but successful — the "desirable difficulty" framing — and diminishes when the task is so hard that retrieval fails entirely [~M]. The benefit also grows over retention intervals: much of the advantage appears at delayed test rather than immediately, which means immediate post-tests can understate the effect [~M].

**Design implications.** Low-stakes quizzing, free recall prompts, and flashcard-style practice are the standard delivery vehicles; the key design variable is requiring actual retrieval rather than recognition or rereading. Feedback after retrieval attempts preserves the diagnostic function and prevents error entrenchment. Spacing retrieval attempts across time compounds the benefit, linking this claim to spacing and [Chunking](../principles/chunking.md) considerations about how much material a single retrieval attempt can reasonably cover. Because retrieval practice is effortful, it pairs poorly with designs that simultaneously impose heavy extraneous load — see [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md). Learners' preference for rereading over testing makes explicit use of low-stakes retrieval important; without it, learners default to less effective study strategies [~M].

**Open questions.** How retrieval practice transfers beyond the exact retrieved items (e.g., to inference and application) is less settled than its effect on verbatim retention, and optimal spacing of retrieval attempts remains an active design question. Evidence entries establishing the core finding still need to be added.

## Related Claims

- [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) — tests used formatively leverage the same retrieval and diagnostic mechanisms.
- [Active learning improves exam performance](active-learning-improves-exam-performance.md) — retrieval practice is a low-cost, structured form of active learning.
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — successful retrieval depends on material fitting within working-memory limits.
- [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — retrieval benefits emerge only when the test itself does not overwhelm working memory.