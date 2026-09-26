---
type: claim
title: Retrieval Failure Reduces Benefit
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: retrieval-failure-reduces-benefit
evidence_strength:
sources:
  - id: rowland-2014
    resource: "https://doi.org/10.1037/a0037559"
    title: "Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)"
    author: Rowland, C. A.
    q: 4
    i: "?"
    n: 159 effect sizes (61 studies)
---

# Retrieval Failure Reduces Benefit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · n=159 effect sizes (61 studies)

When learners attempt retrieval practice but fail to successfully retrieve the target information, the learning benefit of the retrieval attempt is reduced compared with successful retrieval. The claim concerns the *quality* of the retrieval attempt, not the presence of failure per se — see Discussion for boundary conditions.

## Subclaims

`q4 i?` Across the testing-effect literature, the memory benefit of a retrieval attempt scales with how often retrieval succeeds: without corrective feedback, initial recall performance at or below 50% produced no reliable testing effect, while effects grew significantly larger as retrieval success rose toward and beyond 75%. [→ Rowland 2014](#rowland-2014)

## Evidence

### Rowland 2014

Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)

`q4 · meta-analytic review (random-effects model, 159 effect sizes from 61 studies)` · `i? · effect differs by subgroup: g=0.03 at ≤50% initial recall, g=0.56 at >75%` · `n=159 effect sizes (61 studies)`

This meta-analysis pooled 159 effect sizes from 61 published and unpublished studies comparing final retention of tested vs. restudied material (Hedges's g, random-effects model). A dedicated "retrievability and reexposure" moderator analysis split the no-feedback studies by how often the initial retrieval attempt succeeded. Where more than half of initial retrieval attempts failed (≤50% correct) and no feedback followed, the testing effect was statistically indistinguishable from zero; as the proportion of successful retrievals rose (51–75%, then >75%), the size of the benefit rose with it, and studies that provided feedback after retrieval (regardless of initial success) showed the largest effects of all. The pattern directly supports [practice](../elements/practice.md) calibrated to a learner's likely success and pairing failed attempts with feedback, as this claim's Discussion recommends.

## Discussion

**Why failure matters.** Retrieval practice is among the most robust learning strategies, but its benefit is not automatic. A retrieval attempt appears to produce learning primarily when it succeeds — the act of reconstructing an answer strengthens the memory trace. When learners cannot retrieve the answer at all, the attempt may contribute little, and if learners then immediately see the answer, the failed attempt can function as passive re-exposure rather than active reconstruction. This connects to the broader principle that [cognitive load management](../principles/cognitive-load-management.md) matters: a retrieval task pitched far beyond what the learner can access may consume effort without producing consolidation.

**Moderators and boundary conditions.** The claim should not be read as "failure is always bad." Partial retrieval — recalling fragments, related cues, or the gist — may still confer benefit, and some literature on pretesting and errorful learning suggests that unsuccessful attempts followed by feedback can outperform study alone under certain conditions. The critical variables appear to be (a) whether the learner makes a genuine retrieval attempt rather than giving up immediately, (b) whether feedback follows the attempt, and (c) whether task difficulty is calibrated so that retrieval is challenging but achievable. Designers using [retrieval practice](../elements/practice.md) should therefore ensure learners possess enough prior knowledge to have a realistic chance of success — for example by [activating prior knowledge](activation-improves-learning.md) before quizzing — and should pair difficult retrieval attempts with timely corrective feedback.

**Design implications.** Calibrate question difficulty so most learners can retrieve with effort; scaffold with cues or [chunking](chunking-reduces-working-memory-load.md) when material exceeds what learners can access; and always follow failed attempts with feedback that allows successful restudy. Repeated outright failure should trigger adaptation of difficulty rather than more of the same practice — a principle consistent with [adaptive learning](../patterns/adaptive-learning.md) approaches that adjust item difficulty to learner performance.

**Open questions.** The precise threshold at which retrieval difficulty stops helping and starts hurting is unresolved, as is the role of learner motivation: repeated retrieval failure may also carry affective costs that erode engagement and [belonging](../elements/belonging.md), independent of any direct cognitive effect. Whether partial retrieval (gist or fragments) yields benefits proportional to its completeness, and how feedback timing interacts with retrieval success, remain open empirical questions.

**Evidence status.** The meta-analysis recorded above supports the claim through a moderator analysis, not a direct manipulation of retrieval success, so the pattern is correlational across groups of studies. Pretesting and errorful-learning studies, where failed retrieval followed by feedback helps, are a counterpoint recorded on the [pretesting claim page](pretesting-enhances-learning.md).

## Related Claims

- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — organizing material into chunks raises the chance that retrieval attempts succeed
- [Activation improves learning.](activation-improves-learning.md) — activating relevant prior knowledge raises the odds that a retrieval attempt succeeds
- [Adaptive learning improves outcomes.](adaptive-learning-improves-outcomes.md) — adjusting difficulty to the learner helps keep retrieval attempts in the productive, challenging-but-achievable zone
- [Cognitive load management.](../principles/cognitive-load-management.md) — the theoretical framework for calibrating task difficulty to learner capacity
- [Desirable Difficulties Enhance Learning](desirable-difficulties-enhance-learning.md) — related
- [Pretesting Can Harm Motivation](pretesting-can-harm-motivation.md) — related
- [Pretesting enhances learning](pretesting-enhances-learning.md) — related
- [Repeated successful retrieval during learning predicted final recall in both experiments](repeated-retrieval-success-predicts-final-recall.md) — related
- [Retrieval Fails Without Encoding](retrieval-fails-without-encoding.md) — related
- [Retrieval practice improves long-term retention](retrieval-practice-improves-retention.md) — a broader claim this one bears on
- [Retrieval practice effects become more robust as initial retrieval success increases, especially above 75%, while retrieval made too easy yields smaller effects](retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) — possibly the same claim (merge candidate)