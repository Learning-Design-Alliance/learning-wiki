---
type: claim
title: Retrieval Practice Improves Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: retrieval-practice-improves-learning
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

# Retrieval Practice Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i2`–`i3`

Actively recalling information from memory (rather than rereading or reviewing it) strengthens long-term retention and transfer of that information — the "testing effect."

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

**Mechanism.** Retrieval practice is generally explained as a memory-modification effect: the act of successfully reconstructing information from memory changes that memory's accessibility, making it easier to retrieve again later. This distinguishes it from restudying, which re-exposes learners to material but does not exercise the retrieval route itself. It also explains why retrieval works best when embedded in [practice](../elements/practice.md) rather than passive review.

**Moderators to expect.** The size of the benefit typically depends on retrieval success (learners must actually retrieve, not fail repeatedly), feedback availability after retrieval, the interval between learning and test, and the match between retrieval format and the criterion task. Designers should treat these as open design parameters rather than assuming a uniform effect across all implementations. Spacing repeated retrieval attempts over time, consistent with [spaced practice](../principles/spaced-practice.md), generally amplifies the effect; massed retrieval yields smaller durable gains.

**Boundary conditions.** Retrieval practice is not a substitute for initial encoding: if learners have not formed a retrievable memory in the first place, retrieval attempts can be unproductive or discouraging. The claim should be scoped to material that has been at least minimally learned. Where retrieval demands exceed working-memory capacity, [chunking](../claims/chunking-reduces-working-memory-load.md) the target material first improves the odds of successful retrieval.

**Open questions.** How retrieval practice effects scale from laboratory materials to complex, higher-order learning outcomes in authentic classrooms remains an active area of investigation, as does the optimal scheduling of repeated retrieval attempts. Low-stakes quizzing in real courses offers a natural bridge between the laboratory finding and [assessment for learning](../claims/assessment-for-learning-improves-achievement.md).

## Related Claims

- [Active learning improves exam performance.](active-learning-improves-exam-performance.md) — retrieval is a core active-learning mechanism
- [Assessment for learning improves achievement.](assessment-for-learning-improves-achievement.md) — low-stakes quizzing doubles as formative assessment
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — well-chunked material is easier to retrieve successfully
- [Activation improves learning.](activation-improves-learning.md) — prior-knowledge activation supports the initial encoding retrieval builds on
- [Cognitive load management.](cognitive-load-management.md) — retrieval demands must fit within working-memory limits