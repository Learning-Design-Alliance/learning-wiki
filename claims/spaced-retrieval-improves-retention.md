---
type: claim
title: Spaced Retrieval Improves Retention
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: spaced-retrieval-improves-retention
aliases: [spaced-retrieval-practice-improves-retention]
evidence_strength: moderate
sources:
  - id: latimier-et-al-2021
    resource: "https://doi.org/10.1007/s10648-020-09572-8"
    title: "Latimier, A., Peyre, H., & Ramus, F. (2021). A Meta-Analytic Review of the Benefit of Spacing out Retrieval Practice Episodes on Retention. *Educational Psychology Review, 33*(3), 959–987. [doi:10.1007/s10648-020-09572-8](https://doi.org/10.1007/s10648-020-09572-8)"
    author: "Latimier, A., Peyre, H., & Ramus, F."
    q: 4
    i: 2
    n: 39 effect sizes (subset 1)
---

# Spaced Retrieval Improves Retention

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=39 effect sizes (subset 1)

Combining spaced repetition (distributing practice over time) with retrieval practice (actively recalling material rather than rereading it) produces stronger long-term retention than massed study or passive review. The two mechanisms are complementary: retrieval makes recall effortful, and spacing ensures that recall occurs after partial forgetting, when reconstruction is most beneficial.

## Subclaims

`q4 i2` A meta-analysis of 29 studies finds that spacing out retrieval-practice episodes produces meaningfully better long-term retention than massing them; spacing retrieval on an expanding rather than uniform schedule made no reliable difference. [→ Latimier et al. 2021](#latimier-et-al-2021)

## Evidence

### Latimier et al. 2021

Latimier, A., Peyre, H., & Ramus, F. (2021). A Meta-Analytic Review of the Benefit of Spacing out Retrieval Practice Episodes on Retention. *Educational Psychology Review, 33*(3), 959–987. [doi:10.1007/s10648-020-09572-8](https://doi.org/10.1007/s10648-020-09572-8)

`q4 · meta-analysis (robust variance estimation over 29 studies)` · `i2 · medium effect, g=0.74` · `n=39 effect sizes (subset 1)`

Meta-analysis of 29 studies on spaced retrieval practice, split into two subsets to answer two questions. Subset 1 (39 aggregated effect sizes) tested whether spaced retrieval practice produces better final-retention memory than massed retrieval practice, and found a benefit for spacing (Hedges' g = 0.74). Subset 2 (54 effect sizes) tested whether an expanding spacing schedule beats a uniform one during retrieval practice and found no reliable difference (g = 0.034); the number of retrieval exposures per item moderated this null result. The comparator in subset 1 is massed retrieval practice, so the meta-analysis shows that spacing matters within retrieval practice; it does not compare spaced retrieval with passive review.

## Discussion

**Why the combination matters.** Spacing and retrieval are two of the most robust effects in memory research, and they operate through complementary mechanisms: retrieval strengthens memory traces by making recall effortful (a desirable difficulty), while spacing forces retrieval to occur after partial forgetting, when reconstruction is most beneficial. Either technique alone helps — see [Testing effect: retrieval practice improves retention](retrieval-practice-improves-retention.md) and [Distributed practice improves retention](distributed-practice-improves-retention.md) — but combining them, recalling material at increasing intervals, is the configuration most classroom applications target.

**Boundary conditions.** The benefit depends on successful retrieval: attempts that fail entirely and are never followed by feedback may yield little gain, and very long intervals before the first retrieval can leave learners without enough consolidated structure to retrieve from. Spacing also trades against short-term performance — massed study often *feels* more effective to learners and can produce better immediate test performance, which is why learners frequently misjudge it as superior. Designers should therefore schedule retrieval after a delay, not immediately after initial study, and expect learner resistance based on perceived difficulty.

**Open questions.** Optimal interval lengths appear to scale with the retention interval, but exact scheduling rules (e.g., expanding versus equal intervals) remain contested across domains and materials. Most evidence comes from verbal, fact-heavy material; generalization to complex skill learning is less well established.

**Design implications.** Practical implementations range from simple (end each session with a short recall quiz on material from previous sessions) to algorithmic (spaced-repetition software such as [Anki](https://apps.ankiweb.net/) or [Duolingo](https://www.duolingo.com/) that schedules individualized review). Whatever the mechanism, the key design decisions are the same: require retrieval rather than recognition, delay the first retrieval beyond immediate recall, and provide feedback after unsuccessful attempts. Because learners systematically misjudge spacing as inferior to massing, designers should also brief learners on the effect — learner misjudgment of effective study strategies is a well-documented calibration problem in the metacognition literature.

*Merged from “Spaced Retrieval Practice Improves Retention” (spaced-retrieval-practice-improves-retention):* **Why the combination matters.** Spacing and retrieval act through complementary mechanisms: retrieval strengthens memory by making recall effortful (the "desirable difficulty" of successful retrieval), while spacing distributes that effort so each retrieval occurs as the memory is partially decayed, triggering greater reconsolidation benefit than massed practice. Either technique alone shows benefits in the literature; the claim here concerns their combination, which classroom studies suggest is at least additive. Both mechanisms are consistent with [cognitive load theory](../theories/cognitive-load-theory.md) and the broader finding that [active learning improves exam performance](../claims/active-learning-improves-exam-performance.md).

**Boundary conditions.** The benefit depends on retrieval success — testing learners on material they cannot yet recall yields little benefit and can entrench errors if feedback is absent. Spacing intervals must be scaled to the retention interval: gaps that are too long produce failed retrievals, gaps that are too short approximate massed practice. The benefit also diminishes for material that is highly overlearned, and the expertise-reversal pattern seen elsewhere in this wiki ([Expertise reversal effect](../theories/expertise-reversal-effect.md)) suggests advanced learners may need less scaffolding of either schedule or feedback.

**Design implications.** Practical implementations should schedule low-stakes retrieval at expanding intervals, ensure feedback follows retrieval attempts, and avoid formats where learners can infer answers without genuine recall. Because retrieval practice adds demands on working memory relative to rereading, it pairs naturally with [chunking](../claims/chunking-reduces-working-memory-load.md) and other [cognitive load](../theories/cognitive-load-theory.md) management techniques for novices. Low-stakes quizzing also functions as [assessment for learning](../claims/assessment-for-learning-improves-achievement.md), giving learners and instructors feedback on what has actually been retained rather than what was merely studied.

**Open questions.** Most evidence comes from verbal and declarative material; the durability of spaced retrieval for complex skills and transfer tasks is less well established. Optimal spacing schedules in real classrooms (where time is fixed and content interleaves) remain an active research area, and adaptive scheduling systems ([adaptive learning](../claims/adaptive-learning-improves-outcomes.md)) are one promising route to individualizing expanding intervals.

**Evidence status.** No studies have yet been added to this page. Meta-analytic work on the testing effect and on distributed practice, plus classroom experiments combining the two, still need to be sourced and entered before an evidence strength can be assigned.

## Related Claims

- [Testing effect: retrieval practice improves retention](retrieval-practice-improves-retention.md) — the retrieval half of this claim, established independently
- [Distributed practice improves retention](distributed-practice-improves-retention.md) — the spacing half of this claim, established independently
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — chunking reduces the load of what must be retrieved, making spaced retrieval more efficient
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — overloaded learners cannot consolidate, undermining the benefit of spaced retrieval
- [Active learning improves exam performance](active-learning-improves-exam-performance.md) — retrieval is a core active-learning operation
- [Adaptive learning improves outcomes](adaptive-learning-improves-outcomes.md) — adaptive platforms operationalize spaced retrieval by scheduling review at individualized intervals
- [Chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md) — managing load during effortful retrieval is essential for novice learners
- [Active learning improves exam performance](../claims/active-learning-improves-exam-performance.md) — retrieval practice is a core active-learning mechanism
- [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) — low-stakes spaced quizzes double as formative assessment
- [Adaptive learning improves outcomes](../claims/adaptive-learning-improves-outcomes.md) — adaptive systems can individualize expanding retrieval intervals
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — scaffolds like prompts and feedback may become counterproductive as expertise grows
- [Cognitive load theory](../theories/cognitive-load-theory.md) — frames why retrieval is effortful and when that effort pays off
- [Expanding retrieval schedules have not shown consistent advantages over equally spaced or contracting schedules matched on total spacing](expanding-retrieval-schedules-are-not-superior-to-equal-or-contracting-schedules.md) — related
- [Learners Misjudge Spacing Benefits](learners-misjudge-spacing-benefits.md) — related
- [Faster rate of learning may be negatively related to long-term retention (efficiency-effectiveness trade-off)](learning-rate-retention-tradeoff.md) — related
- [Spaced Practice Improves Retention](spaced-practice-improves-retention.md) — related
- [Spaced Repetition Improves Retention](spaced-repetition-improves-retention.md) — related
- [Spaced Retrieval Outperforms Restudy](spaced-retrieval-outperforms-restudy.md) — related
- [Desirable Difficulties Enhance Learning](desirable-difficulties-enhance-learning.md) — related
- [Structured CAI with spaced practice and spaced review produced better recall and retention than unstructured CAI](structured-cai-spacing-improves-recall-and-retention.md) — a narrower finding that bears on this claim
- [Most middle and high school students surveyed after classroom retrieval practice programs viewed them positively and said frequent retrieval practice helped them feel less nervous about exams](students-report-classroom-retrieval-practice-helps-learning-and-reduces-exam-nervousness.md) — related
