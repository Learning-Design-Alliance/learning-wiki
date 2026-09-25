---
type: claim
title: Spaced Retrieval Improves Retention
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: spaced-retrieval-improves-retention
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

**Why the combination matters.** Spacing and retrieval are two of the most robust effects in memory research, and they operate through complementary mechanisms: retrieval strengthens memory traces by making recall effortful (a desirable difficulty), while spacing forces retrieval to occur after partial forgetting, when reconstruction is most beneficial. Either technique alone helps — see [Testing effect: retrieval practice improves retention](testing-effect-retrieval-practice-improves-retention.md) and [Distributed practice improves retention](distributed-practice-improves-retention.md) — but combining them, recalling material at increasing intervals, is the configuration most classroom applications target.

**Boundary conditions.** The benefit depends on successful retrieval: attempts that fail entirely and are never followed by feedback may yield little gain, and very long intervals before the first retrieval can leave learners without enough consolidated structure to retrieve from. Spacing also trades against short-term performance — massed study often *feels* more effective to learners and can produce better immediate test performance, which is why learners frequently misjudge it as superior. Designers should therefore schedule retrieval after a delay, not immediately after initial study, and expect learner resistance based on perceived difficulty.

**Open questions.** Optimal interval lengths appear to scale with the retention interval, but exact scheduling rules (e.g., expanding versus equal intervals) remain contested across domains and materials. Most evidence comes from verbal, fact-heavy material; generalization to complex skill learning is less well established.

**Design implications.** Practical implementations range from simple (end each session with a short recall quiz on material from previous sessions) to algorithmic (spaced-repetition software such as [Anki](https://apps.ankiweb.net/) or [Duolingo](https://www.duolingo.com/) that schedules individualized review). Whatever the mechanism, the key design decisions are the same: require retrieval rather than recognition, delay the first retrieval beyond immediate recall, and provide feedback after unsuccessful attempts. Because learners systematically misjudge spacing as inferior to massing, designers should also brief learners on the effect — learner misjudgment of effective study strategies is a well-documented calibration problem in the metacognition literature.

## Related Claims

- [Testing effect: retrieval practice improves retention](testing-effect-retrieval-practice-improves-retention.md) — the retrieval half of this claim, established independently
- [Distributed practice improves retention](distributed-practice-improves-retention.md) — the spacing half of this claim, established independently
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — chunking reduces the load of what must be retrieved, making spaced retrieval more efficient
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — overloaded learners cannot consolidate, undermining the benefit of spaced retrieval
- [Active learning improves exam performance](active-learning-improves-exam-performance.md) — retrieval is a core active-learning operation
- [Adaptive learning improves outcomes](adaptive-learning-improves-outcomes.md) — adaptive platforms operationalize spaced retrieval by scheduling review at individualized intervals