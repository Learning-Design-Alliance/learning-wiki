---
type: claim
title: Segmentation Benefits Shrink With Expertise
status: review
generated:
  by: claude/unspecified
  at: 2026-09-25
id: segmentation-benefits-shrink-with-expertise
aliases: [segmentation-expertise-reversal-dynamic-visualizations]
evidence_strength: emerging
sources:
  - id: spanjers-et-al-2011
    resource: "https://doi.org/10.1016/j.chb.2010.05.011"
    title: "Spanjers, I. A. E., Wouters, P., van Gog, T., & van Merriënboer, J. J. G. (2011). An expertise reversal effect of segmentation in learning from animated worked-out examples. *Computers in Human Behavior, 27*(1), 46–52. [doi:10.1016/j.chb.2010.05.011](https://doi.org/10.1016/j.chb.2010.05.011)"
    author: "Spanjers, I. A. E., Wouters, P., van Gog, T., & van Merriënboer, J. J. G."
    q: 3
    i: "?"
    n: 75 (37 segmented, 38 continuous)
    kind: causal
    rigour: "?"
  - id: spanjers-2010
    resource: "https://doi.org/10.1007/s10648-010-9135-6"
    title: "Spanjers, I. A. E., van Gog, T., & van Merriënboer, J. J. G. (2010). A Theoretical Analysis of How Segmentation of Dynamic Visualizations Optimizes Students' Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-010-9135-6"
    author: "Spanjers, I. A. E., van Gog, T., & van Merriënboer, J. J. G."
    q: 3
    i: "?"
    kind: review
    rigour: 2
---

# Segmentation Benefits Shrink With Expertise

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r?`, 1 review `r2` · `q3` · n=75 (37 segmented, 38 continuous)

The benefit of segmenting continuous instructional material (e.g., pausing animation or breaking narration into segments) is largest for novices and diminishes as learner expertise increases. In the one experiment recorded here the benefit was in learning efficiency (performance relative to mental effort), and it disappeared at higher prior knowledge rather than reversing.
<!-- deprecated (2026-10-14, "or reverses" is not shown by the recorded study): The learning benefit of segmenting continuous instructional material (e.g., pausing animation or breaking narration into learner-paced segments) is largest for novices and diminishes — or reverses — as learner expertise increases. -->

The claim concerns dynamic, transient media (animation, video, narrated slides) where learners cannot otherwise control the pace of information delivery. It is the segmentation-specific instance of the broader [expertise reversal effect](../theories/expertise-reversal-effect.md).

## Subclaims

`q3 i?` Segmenting animated worked-out examples on probability calculation was more efficient (equal transfer performance, lower mental effort) than continuous animation for lower-prior-knowledge students, but this efficiency advantage disappeared at higher prior-knowledge levels. [→ Spanjers et al. 2011](#spanjers-et-al-2011)

`q3 i?` In a study without learner control, students with lower prior knowledge learned more efficiently from segmented animations, while students with higher prior knowledge learned equally efficiently from both formats. [→ Spanjers 2010](#spanjers-2010)

`q3 i?` In a slideshow study on gearing systems, learner control over slide progression produced larger pretest-to-posttest gains, significant only in the low prior knowledge group. [→ Spanjers 2010 (2)](#spanjers-2010)

## Evidence

### Spanjers et al. 2011

Spanjers, I. A. E., Wouters, P., van Gog, T., & van Merriënboer, J. J. G. (2011). An expertise reversal effect of segmentation in learning from animated worked-out examples. *Computers in Human Behavior, 27*(1), 46–52. [doi:10.1016/j.chb.2010.05.011](https://doi.org/10.1016/j.chb.2010.05.011)

`q3 · peer-reviewed experiment (not pre-registered)` · `i? · effect size not reported (regression β/t/p only)` · `n=75 (37 segmented, 38 continuous)` · `causal · r?`

76 Dutch secondary-education students (one excluded for missing data) were randomly assigned to study eight animated, narrated worked-out examples on probability calculation, presented either as one continuous stream per example or divided into 5–7 segments with 2-second pauses. Regression models with prior knowledge (centered), condition, and their interaction predicted near- and far-transfer efficiency (performance combined with invested mental effort). The prior-knowledge × condition interaction was significant for both near (β = −0.35, p = .04) and far transfer efficiency (β = −0.34, p = .05): at one SD below the mean (lower prior knowledge), segmented examples were significantly more efficient than continuous ones (near β = 0.39, p = .01; far β = 0.33, p = .03), but at one SD above the mean (higher prior knowledge) this difference had disappeared (near β = −0.05, p = .72; far β = −0.10, p = .51), driven mainly by continuous-condition mental effort dropping sharply with rising prior knowledge while segmented-condition effort stayed flat. No significant interaction was found on raw transfer performance alone, only on mental effort and the composite efficiency measure.

### Spanjers 2010

Spanjers, I. A. E., van Gog, T., & van Merriënboer, J. J. G. (2010). A Theoretical Analysis of How Segmentation of Dynamic Visualizations Optimizes Students' Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-010-9135-6

`q3 · i?` · `review · r2`

The review reports Spanjers et al.'s (2010) experiment on probability calculation procedures, in which segmented animations automatically paused after each segment and continued after 2 s, with no learner control; a significant interaction between segmentation and prior knowledge was found. No effect size is printed.

> "Students with lower levels of prior knowledge learned more efficiently from segmented animations than from non- segmented animations, while students with higher levels of prior knowledge learned equally efficiently from non-segmented and segmented ones (i.e., an expertise reversal effect; Kalyuga 2007)."

## Studies bearing on this claim

<!-- synthesis:start -->
*For whom: does the benefit depend on prior knowledge or learner characteristics?* This table gathers the studies behind this claim and the 3 narrower claims that bear on it: **4 distinct studies** (2 causal, 1 review, 1 quant-synthesis), `q3`, 1 of 4 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Spanjers et al. 2011](https://doi.org/10.1016/j.chb.2010.05.011) | q3 · causal · r? | i? | this claim |
| [Spanjers 2010](https://doi.org/10.1007/s10648-010-9135-6) | q3 · review · r2 | i? | this claim |
| [Rey 2019](https://doi.org/10.1007/s10648-018-9456-4) | q3 · quant-synthesis · r? | i? | [Learners with high prior knowledge benefit more from segmenting in retention performance t](prior-knowledge-moderates-segmenting-retention.md) (counts against) |
| [Veronica Pimenova 2026](https://doi.org/10.48550/arxiv.2607.24612) | q3 · causal · r1 | i3; i? | [Segmentation reduces errors and hesitations for participants with and without ADHD, with l](segmentation-benefit-larger-for-adhd-group.md) (qualifies); [ADHD medication status shows no significant interaction with segmentation, though medicate](medication-status-segmentation-interaction-null.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

**What the recorded study shows.** Spanjers et al. (2011) found the benefit of segmentation on instructional efficiency (performance relative to mental effort), not on test performance alone, and found it disappearing at high prior knowledge rather than reversing. A full reversal, continuous animation beating segmented animation for more expert learners, is left by the authors as an open question.

**Expertise reversal as the underlying mechanism.** Segmentation reduces extraneous cognitive load by giving novices control over the pace of information delivery and preventing overload from transient, continuous presentations. As expertise grows, learners no longer need external pacing support; segmenting can then add unnecessary processing — re-integration overhead across segment boundaries — or simply waste time, consistent with the broader [expertise reversal effect](../theories/expertise-reversal-effect.md). The same pattern appears for other load-reducing scaffolds such as [worked examples](../elements/demonstration.md), which also lose and eventually reverse their advantage with expertise.

**Boundary conditions.** The claim applies to transient, learner-uncontrolled presentations (animation, video, narrated slides). For static or already self-paced material, segmentation has little to offer novices either, so the expertise interaction is most visible in dynamic media. Learner-controlled pacing is a key moderator: when learners can pause and replay freely, the added value of designer-imposed segments shrinks for everyone.

**Design implication.** Treat segmentation as a fading scaffold: begin with designer-imposed segments for novices encountering high-element-interactivity material, then progressively hand pacing control to learners — or lengthen segments — as diagnostic evidence of growing expertise accumulates. This mirrors the fading logic used for [worked examples](../elements/demonstration.md) in [cognitive load management](../principles/cognitive-load-management.md) more broadly.

**Constraints.** Imposing segments on advanced learners can impose re-integration costs across boundaries and slow experienced learners who would otherwise move at their own pace. When the medium already supports full learner pacing (pause, scrub, replay), designer-imposed segmentation adds little for any expertise level. Coarse segmentation of low-element-interactivity content may fragment material without any compensating load reduction, making the expertise interaction moot.

**Open questions.** The expertise level at which segmentation benefits disappear likely varies by domain complexity and segment granularity. Fine-grained segmentation may retain value longer than coarse segmentation, but this has not been firmly established. Studies specifically testing segmentation × expertise interactions are scarcer than for worked examples, so confidence in the precise crossover point is limited.

## Learner Variables

- [Prior Knowledge](../learner-variables/prior-knowledge.md) — moderator: an instructional effect differs with it

## Related Claims

- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-less-effective-with-expertise.md) — the same expertise reversal pattern for a closely related load-reducing scaffold
- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — another load-reduction principle whose benefits are strongest for novices
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — segmentation is a dynamic-media application of chunking, with the same novice-dependence
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the overload that segmentation prevents occurs mainly under high element interactivity, typical of novice learning
- [Cognitive Load Management](cognitive-load-management.md) — related
- [Letting learners pace instruction helped on complex material in one experiment, while learner control in general showed almost no effect across 18 studies](learner-paced-beats-system-paced-complex-material.md) — related
- [Segmenting Improves Multimedia Learning](segmenting-improves-multimedia-learning.md) — a broader claim this one bears on
- [Expertise reversal: cognitive load effects for novices decrease, disappear, and can reverse as expertise increases](expertise-reversal-effect-compound.md) — a broader claim this one bears on
- [The effectiveness of instructional techniques and procedures interacts with levels of learner prior knowledge, a pattern known as the expertise reversal effect](expertise-reversal-prior-knowledge-interaction.md) — a broader claim this one bears on
- [Learners with high prior knowledge benefit more from segmenting in retention performance than learners with no or low prior knowledge](prior-knowledge-moderates-segmenting-retention.md) — reports the opposite
- [Segmenting principle: learner-paced segments of narrated animation improve transfer over continuous presentation](segmenting-principle-mayer-2008.md) — related
- [Segmentation reduces overall cognitive load during multimedia learning](segmenting-reduces-cognitive-load.md) — related
- [Design principle effects are larger in system-paced and in complex media, and learner prior knowledge was not a significant moderator (p = 0.14)](design-principle-effects-moderated-by-pacing-and-complexity.md) — reports the opposite
- [In one meta-regression, the PS-I fidelity benefit tended to shrink for interventions spanning only a few hours, a marginal interaction (p = .055)](psi-fidelity-time-span-interaction.md) — related
- Experiment 5 showed superior performance for learners who had previously studied isolated elements followed by interacting elements instruction, supporting expertise as the key factor in the technique's benefits — related
- [Segmenting complex dynamic visualizations into pieces with pauses improves learning outcomes, especially transfer performance, at least for novices, compared with non-segmented presentations](segmentation-improves-learning-dynamic-visualizations.md) — related
- [Video benefits learning only when its interactivity matches or exceeds the comparison condition](video-benefit-depends-on-relative-interactivity.md) — related
- [The expertise reversal effect relies on changes in relative levels of element interactivity due to changes in relative levels of expertise](expertise-reversal-changes-from-expertise-levels.md) — a broader claim this one bears on
- [The relative effectiveness of instructional methods reverses as levels of learner knowledge in a domain change (the expertise reversal effect)](expertise-reversal-effect-definition.md) — a broader claim this one bears on
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](expertise-reversal-effect.md) — a broader claim this one bears on
- [Cognitive load when studying depended on instructional method (highest in the worked-out examples condition), but no prior knowledge or test-phase effects emerged](cognitive-load-method-effect-studying.md) — related
- [Instructional method and prior knowledge interact on conceptual understanding of statistics (expertise reversal effect)](expertise-reversal-conceptual-understanding-statistics.md) — a broader claim this one bears on
- [Model progression benefits learning only in sufficiently complex simulations; in a simple domain it was less efficient than full complexity from the start](model-progression-complexity-boundary.md) — related
- [Prior knowledge moderates scaffolding effectiveness: reflection phases were more effective for higher education levels, examples for lower levels](prior-knowledge-moderates-scaffolding-effectiveness.md) — related
- [The efficiency advantage of prior collaborative experience emerges under high information density but not under low information density](zambrano-2019-efficiency-advantage-only-high-density.md) — related
- [No differences were found on mental effort during instruction or on transfer across illusion-of-control and instruction-method conditions](no-mental-effort-differences.md) — related
- [Prior knowledge, but not interest or estimated prior knowledge, predicts use of learner control options](prior-knowledge-predicts-interactive-behavior.md) — related
- [The segmenting, cognitive-load, and learning-time effects are confirmed for system-paced segmentation](segmenting-effects-confirmed-system-paced.md) — related
- [Lesson variability benefits transfer only in combination with worked-example instruction, as shown by a variability-by-instruction interaction](example-variability-interaction-with-cognitive-load.md) — related
- [High experienced effort-by-complexity is not necessarily indicative of better learning outcomes](high-effort-not-indicative-better-learning.md) — related
- [Successful low-prior-knowledge inquiry learners managed cognitive load by exploring simple circuits first and pausing during learning](cognitive-load-management-in-inquiry-simulation-learning.md) — a narrower finding that bears on this claim
- [Element interactivity and expertise reversal effects: cognitive load effects diminish and may reverse as expertise increases because known elements chunk into single elements](expertise-reversal-effect-element-interactivity.md) — a broader claim this one bears on
- [A tracing strategy combining segmentation and prediction produced more efficient learning than a non-interactive instructional condition](tracing-strategy-segmentation-prediction-efficiency.md) — related
