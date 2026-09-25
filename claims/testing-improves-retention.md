---
type: claim
title: Testing Improves Retention
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: testing-improves-retention
evidence_strength:
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

# Testing Improves Retention

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i2`–`i3`

Retrieving information from memory (being tested) strengthens long-term retention of that information more than restudying it. The claim concerns retrieval practice — low- or no-stakes tests used as learning events — not high-stakes assessment.

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

**Mechanism.** The retrieval-effort account holds that the act of successfully reconstructing knowledge from memory changes its storage — each successful retrieval makes the memory more accessible on future attempts, whereas rereading primarily increases fluency without strengthening retrieval pathways. This is why testing is best understood as a learning event, not merely an assessment event, and why it pairs naturally with [assessment for learning](assessment-for-learning-improves-achievement.md) approaches. The mechanism also connects to broader [active learning](active-learning-improves-exam-performance.md) accounts: retrieval is an active, generative act, in contrast to the passive reception of restudy.

**Boundary conditions.** The benefit depends on successful retrieval: tests that learners largely fail, or that occur before the material has been encoded at all, produce far weaker effects. Feedback after retrieval matters most when initial retrieval fails. The effect also varies with test format — free recall and cued recall tend to produce larger retention benefits than multiple-choice recognition, though recognition-based retrieval can still help. Spacing repeated retrievals over time amplifies the benefit relative to massed testing, consistent with [distributed practice](distributed-practice-improves-retention.md) findings. Retrieval that exceeds working-memory capacity — for example, recalling material that was never [chunked](chunking-reduces-working-memory-load.md) into manageable units — can impose [cognitive overload](cognitive-overload-degrades-learning.md) that undermines the benefit, a concern that falls under [cognitive load management](cognitive-load-management.md).

**Open questions.** How retrieval practice transfers to complex, application-level outcomes (as opposed to retention of discrete facts) remains actively debated, and the optimal scheduling of retrievals relative to forgetting points is not fully settled.

**Note on evidence.** The evidence recorded above supports the claim, with one condition worth stating: in Roediger and Karpicke (2006), restudying was ahead on a test five minutes later, and testing won only at two days and one week. The retrieval-practice literature is large and well-established, so populating this section — ideally with the major meta-analyses and the canonical restudy-comparison experiments — should be a high priority for a future enrichment pass.

## Related Claims

- [Active learning improves exam performance.](active-learning-improves-exam-performance.md) — testing is an active-learning format; both contrast with passive restudy
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — successful retrieval depends on how material is organized in memory
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — overly difficult retrieval can fail to strengthen memory
- [Assessment for learning improves achievement.](assessment-for-learning-improves-achievement.md) — positions testing as a learning tool rather than a measurement endpoint
- [Distributed practice improves retention.](distributed-practice-improves-retention.md) — spaced retrievals amplify the testing effect relative to massed testing