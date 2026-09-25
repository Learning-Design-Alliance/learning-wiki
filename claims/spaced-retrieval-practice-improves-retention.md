---
type: claim
title: Spaced Retrieval Practice Improves Retention
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: spaced-retrieval-practice-improves-retention
evidence_strength:
sources:
  - id: latimier-et-al-2021
    resource: "https://doi.org/10.1007/s10648-020-09572-8"
    title: "Latimier, A., Peyre, H., & Ramus, F. (2021). A Meta-Analytic Review of the Benefit of Spacing out Retrieval Practice Episodes on Retention. *Educational Psychology Review, 33*(3), 959–987. [doi:10.1007/s10648-020-09572-8](https://doi.org/10.1007/s10648-020-09572-8)"
    author: "Latimier, A., Peyre, H., & Ramus, F."
    q: 4
    i: 2
    n: 39 effect sizes (subset 1)
---

# Spaced Retrieval Practice Improves Retention

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=39 effect sizes (subset 1)

Combining spaced repetition (distributing practice over time) with retrieval practice (actively recalling material rather than rereading it) produces durable long-term retention of learned material.

## Subclaims

`q4 i2` A meta-analysis of 29 studies finds that spacing out retrieval-practice episodes produces meaningfully better long-term retention than massing them; spacing retrieval on an expanding rather than uniform schedule made no reliable difference. [→ Latimier et al. 2021](#latimier-et-al-2021)

## Evidence

### Latimier et al. 2021

Latimier, A., Peyre, H., & Ramus, F. (2021). A Meta-Analytic Review of the Benefit of Spacing out Retrieval Practice Episodes on Retention. *Educational Psychology Review, 33*(3), 959–987. [doi:10.1007/s10648-020-09572-8](https://doi.org/10.1007/s10648-020-09572-8)

`q4 · meta-analysis (robust variance estimation over 29 studies)` · `i2 · medium effect, g=0.74` · `n=39 effect sizes (subset 1)`

Meta-analysis of 29 studies on spaced retrieval practice, split into two subsets to answer two questions. Subset 1 (39 aggregated effect sizes) tested whether spaced retrieval practice produces better final-retention memory than massed retrieval practice, and found a benefit for spacing (Hedges' g = 0.74). Subset 2 (54 effect sizes) tested whether an expanding spacing schedule beats a uniform one during retrieval practice and found no reliable difference (g = 0.034); the number of retrieval exposures per item moderated this null result. The comparator in subset 1 is massed retrieval practice, so the meta-analysis shows that spacing matters within retrieval practice; it does not compare spaced retrieval with passive review.

## Discussion

**Why the combination matters.** Spacing and retrieval act through complementary mechanisms: retrieval strengthens memory by making recall effortful (the "desirable difficulty" of successful retrieval), while spacing distributes that effort so each retrieval occurs as the memory is partially decayed, triggering greater reconsolidation benefit than massed practice. Either technique alone shows benefits in the literature; the claim here concerns their combination, which classroom studies suggest is at least additive. Both mechanisms are consistent with [cognitive load theory](../theories/cognitive-load-theory.md) and the broader finding that [active learning improves exam performance](../claims/active-learning-improves-exam-performance.md).

**Boundary conditions.** The benefit depends on retrieval success — testing learners on material they cannot yet recall yields little benefit and can entrench errors if feedback is absent. Spacing intervals must be scaled to the retention interval: gaps that are too long produce failed retrievals, gaps that are too short approximate massed practice. The benefit also diminishes for material that is highly overlearned, and the expertise-reversal pattern seen elsewhere in this wiki ([Expertise reversal effect](../theories/expertise-reversal-effect.md)) suggests advanced learners may need less scaffolding of either schedule or feedback.

**Design implications.** Practical implementations should schedule low-stakes retrieval at expanding intervals, ensure feedback follows retrieval attempts, and avoid formats where learners can infer answers without genuine recall. Because retrieval practice adds demands on working memory relative to rereading, it pairs naturally with [chunking](../claims/chunking-reduces-working-memory-load.md) and other [cognitive load](../theories/cognitive-load-theory.md) management techniques for novices. Low-stakes quizzing also functions as [assessment for learning](../claims/assessment-for-learning-improves-achievement.md), giving learners and instructors feedback on what has actually been retained rather than what was merely studied.

**Open questions.** Most evidence comes from verbal and declarative material; the durability of spaced retrieval for complex skills and transfer tasks is less well established. Optimal spacing schedules in real classrooms (where time is fixed and content interleaves) remain an active research area, and adaptive scheduling systems ([adaptive learning](../claims/adaptive-learning-improves-outcomes.md)) are one promising route to individualizing expanding intervals.

**Evidence status.** No studies have yet been added to this page. Meta-analytic work on the testing effect and on distributed practice, plus classroom experiments combining the two, still need to be sourced and entered before an evidence strength can be assigned.

## Related Claims

- [Chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md) — managing load during effortful retrieval is essential for novice learners
- [Active learning improves exam performance](../claims/active-learning-improves-exam-performance.md) — retrieval practice is a core active-learning mechanism
- [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) — low-stakes spaced quizzes double as formative assessment
- [Adaptive learning improves outcomes](../claims/adaptive-learning-improves-outcomes.md) — adaptive systems can individualize expanding retrieval intervals
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — scaffolds like prompts and feedback may become counterproductive as expertise grows
- [Cognitive load theory](../theories/cognitive-load-theory.md) — frames why retrieval is effortful and when that effort pays off