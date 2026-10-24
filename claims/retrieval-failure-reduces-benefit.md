---
type: claim
title: Retrieval Failure Reduces Benefit
status: review
generated:
  by: claude/unspecified
  at: 2026-09-25
id: retrieval-failure-reduces-benefit
evidence_strength:
newest_evidence: 2014
sources:
  - id: rowland-2014
    resource: "https://doi.org/10.1037/a0037559"
    title: "Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)"
    author: Rowland, C. A.
    q: 4
    i: "?"
    n: 159 effect sizes (61 studies)
    kind: quant-synthesis
    rigour: "?"
---

# Retrieval Failure Reduces Benefit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r?` · `q4` · n=159 effect sizes (61 studies)
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person

When learners attempt retrieval practice but fail to successfully retrieve the target information, the learning benefit of the retrieval attempt is reduced compared with successful retrieval. The claim concerns the *quality* of the retrieval attempt, not the presence of failure per se — see Discussion for boundary conditions.

## Subclaims

`q4 i?` Across the testing-effect literature, the memory benefit of a retrieval attempt scales with how often retrieval succeeds: without corrective feedback, initial recall performance at or below 50% produced no reliable testing effect, while effects grew significantly larger as retrieval success rose toward and beyond 75%. [→ Rowland 2014](#rowland-2014)

## Evidence

### Rowland 2014

Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. [doi:10.1037/a0037559](https://doi.org/10.1037/a0037559)

`q4 · meta-analytic review (random-effects model, 159 effect sizes from 61 studies)` · `i? · effect differs by subgroup: g=0.03 at ≤50% initial recall, g=0.56 at >75%` · `n=159 effect sizes (61 studies)` · `quant-synthesis · r?`

This meta-analysis pooled 159 effect sizes from 61 published and unpublished studies comparing final retention of tested vs. restudied material (Hedges's g, random-effects model). A dedicated "retrievability and reexposure" moderator analysis split the no-feedback studies by how often the initial retrieval attempt succeeded. Where more than half of initial retrieval attempts failed (≤50% correct) and no feedback followed, the testing effect was statistically indistinguishable from zero; as the proportion of successful retrievals rose (51–75%, then >75%), the size of the benefit rose with it, and studies that provided feedback after retrieval (regardless of initial success) showed the largest effects of all. The pattern directly supports [practice](../elements/practice.md) calibrated to a learner's likely success and pairing failed attempts with feedback, as this claim's Discussion recommends.

## Studies bearing on this claim

<!-- synthesis:start -->
*How much should retrieval succeed during practice, and how much support should it get?* This table gathers the studies behind this claim and the 7 narrower claims that bear on it: **5 distinct studies** (2 quant-synthesis, 2 causal, 1 review), `q2`–`q4`, 1 of 5 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Rowland 2014](https://doi.org/10.1037/a0037559) | q4 · quant-synthesis · r? | i? | this claim; [The meta-analysis supports retrieval effort as a contributor to the testing effect](retrieval-effort-support-testing-effect.md) (qualifies) |
| [Karpicke 2017](https://doi.org/10.1016/b978-0-12-809324-5.21055-9) | q2 / q3 · review · r3 | i? | [A review reports that retrieval practice effects grow more robust as initial retrieval suc](retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) (supports); [Initial retrieval conditions that provide less cue support, such as free recall rather tha](less-initial-retrieval-support-produces-better-retention.md) (qualifies); [Inducing learners to recollect the prior study episode during retrieval practice enhances ](recollecting-the-prior-study-episode-during-retrieval-enhances-retention.md) (qualifies) |
| [Steven C. Pan and Timothy C. Rickard 2018](https://doi.org/10.1037/bul0000151) | q4 · quant-synthesis · r3 | i? | [Response congruency, elaborated retrieval practice, and initial test performance strongly ](moderators-congruency-elaborated-retrieval-initial-test-performance.md) (supports) |
| [Ariel 2018](https://doi.org/10.1037/xap0000133) | q3 · causal · r2 | i2; i1 | [Repeated successful retrieval during learning predicted final recall in both experiments](repeated-retrieval-success-predicts-final-recall.md) (supports) |
| Maass 2016 | q3 · causal · r2 | i? | [Unsuccessful retrieval attempts confer a smaller benefit to future performance than succes](unsuccessful-retrieval-smaller-benefit-than-successful.md) (supports) |
<!-- synthesis:end -->

## Discussion

**Why failure matters.** Retrieval practice is among the most robust learning strategies, but its benefit is not automatic. A retrieval attempt appears to produce learning primarily when it succeeds — the act of reconstructing an answer strengthens the memory trace. When learners cannot retrieve the answer at all, the attempt may contribute little, and if learners then immediately see the answer, the failed attempt can function as passive re-exposure rather than active reconstruction. This connects to the broader principle that [cognitive load management](../principles/cognitive-load-management.md) matters: a retrieval task pitched far beyond what the learner can access may consume effort without producing consolidation.

**Moderators and boundary conditions.** The claim should not be read as "failure is always bad." Partial retrieval — recalling fragments, related cues, or the gist — may still confer benefit, and some literature on pretesting and errorful learning suggests that unsuccessful attempts followed by feedback can outperform study alone under certain conditions. The critical variables appear to be (a) whether the learner makes a genuine retrieval attempt rather than giving up immediately, (b) whether feedback follows the attempt, and (c) whether task difficulty is calibrated so that retrieval is challenging but achievable. Designers using [retrieval practice](../elements/practice.md) should therefore ensure learners possess enough prior knowledge to have a realistic chance of success — for example by [activating prior knowledge](activation-improves-learning.md) before quizzing — and should pair difficult retrieval attempts with timely corrective feedback.

**Design implications.** Calibrate question difficulty so most learners can retrieve with effort; scaffold with cues or [chunking](chunking-reduces-working-memory-load.md) when material exceeds what learners can access; and always follow failed attempts with feedback that allows successful restudy. Repeated outright failure should trigger adaptation of difficulty rather than more of the same practice — a principle consistent with [adaptive learning](../principles/adaptive-learning.md) approaches that adjust item difficulty to learner performance.

**Open questions.** The precise threshold at which retrieval difficulty stops helping and starts hurting is unresolved, as is the role of learner motivation: repeated retrieval failure may also carry affective costs that erode engagement and [belonging](../elements/belonging.md), independent of any direct cognitive effect. Whether partial retrieval (gist or fragments) yields benefits proportional to its completeness, and how feedback timing interacts with retrieval success, remain open empirical questions.

**Evidence status.** The meta-analysis recorded above supports the claim through a moderator analysis, not a direct manipulation of retrieval success, so the pattern is correlational across groups of studies. Pretesting and errorful-learning studies, where failed retrieval followed by feedback helps, are a counterpoint recorded on the [pretesting claim page](pretesting-enhances-learning.md).

## Related Claims

- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — organizing material into chunks raises the chance that retrieval attempts succeed
- [Activation improves learning.](activation-improves-learning.md) — activating relevant prior knowledge raises the odds that a retrieval attempt succeeds
- [Adaptive learning improves outcomes.](adaptive-learning-improves-outcomes.md) — adjusting difficulty to the learner helps keep retrieval attempts in the productive, challenging-but-achievable zone
- [Cognitive load management.](../principles/cognitive-load-management.md) — the theoretical framework for calibrating task difficulty to learner capacity
- [Retrieval practice and spaced retrieval improve achievement and retention by medium amounts, while interleaving helps category learning only for some materials and blocking beats it for words](desirable-difficulties-enhance-learning.md) — related
- [Pre-tests reduced adult learners' persistence in a MOOC, though they improved post-test scores among those who completed it](pretesting-can-harm-motivation.md) — related
- [Pretesting enhances learning](pretesting-enhances-learning.md) — related
- [Repeated successful retrieval during learning predicted final recall in both experiments](repeated-retrieval-success-predicts-final-recall.md) — related
- [Retrieval practice improves long-term retention](retrieval-practice-improves-retention.md) — a broader claim this one bears on
- [A review reports that retrieval practice effects grow more robust as initial retrieval success rises, especially above 75%, and separately that giving more retrieval cues yields smaller effects](retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) — possibly the same claim (merge candidate)
- [Unsuccessful retrieval attempts confer a smaller benefit to future performance than successful retrievals, whose advantage grows with item difficulty](unsuccessful-retrieval-smaller-benefit-than-successful.md) — a narrower finding that bears on this claim
- [In eSpark quests requiring three post-quiz attempts, students reached the 80 percent mastery criterion only 14 percent of the time](espark-post-quiz-mastery-failure-rate.md) — related
- [Evidence tracing links 96 of 114 generated claims to source chunks, but three claims with retrieval scores of 0.50 or below show retrieval similarity alone is insufficient](evidence-tracing-114-claims-retrieval-limit.md) — related
- [Recorded natural-language feedback was associated with lower odds of subsequent persistent failure than no feedback in the randomized course subset](natural-language-feedback-lower-persistent-failure-odds.md) — related
- [Error correction supports learning when it requires substantive cognitive work such as explanation and reconstruction](error-correction-effort-supports-learning.md) — related
- [Quizzing outperforms no/filler activity, fewer-question testing and restudying, with a larger advantage over no/filler activity (low reexposure) than over restudying (high reexposure); against other elaborative strategies its advantage is small and not significant.](quizzing-beats-restudying-and-elaborative-controls.md) — related
- [The meta-analysis supports retrieval effort as a contributor to the testing effect](retrieval-effort-support-testing-effect.md) — related
- [Taking a practice test before a final test produces a moderately large, statistically significant benefit for learning overall (g = 0.61 fixed-effects; g = 0.70 random-effects)](practice-testing-overall-meta-analytic-benefit.md) — related
- [Differential scaffold benefits were more salient for the more difficult learning concept](scaffold-benefits-more-salient-for-difficult-concept.md) — related
- [Retrieval practice produces better retention than restudying, with meta-analytic reviews reporting people 2.5 times as likely to remember tested information and medium-to-large classroom effects](retrieval-practice-beats-restudying.md) — related
- [Response congruency, elaborated retrieval practice, and initial test performance strongly influence the likelihood of positive transfer](moderators-congruency-elaborated-retrieval-initial-test-performance.md) — related
- [Higher self-reported confusion predicts a much larger negative effect on future performance when learners answer more questions incorrectly](confusion-amplifies-negative-effect-of-incorrect-trials.md) — related
- [In open-ended constructivist activities, task success or failure is not a reliable indicator of learning, so learner models based only on performance risk misjudging learners](performance-not-indicator-learning-open-ended.md) — related
- [Initial retrieval conditions that provide less cue support, such as free recall rather than recognition or fewer letter cues, tend to produce better retention despite lower initial success](less-initial-retrieval-support-produces-better-retention.md) — related
- [Feedback Enhances Retrieval Practice](feedback-enhances-retrieval-practice.md) — related
- [Feedback likely supported both consolidation and rule induction in the observed retrieval practice benefits](feedback-role-in-retrieval-practice-benefits.md) — related
- [Images that reveal the answer reduce recall compared with images appearing after the retrieval attempt](answer-revealing-images-worse-than-post-retrieval-images.md) — a narrower finding that bears on this claim