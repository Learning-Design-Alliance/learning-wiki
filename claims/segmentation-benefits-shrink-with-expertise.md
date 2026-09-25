---
type: claim
title: Segmentation Benefits Shrink With Expertise
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: segmentation-benefits-shrink-with-expertise
evidence_strength: emerging
sources:
  - id: spanjers-et-al-2011
    resource: "https://doi.org/10.1016/j.chb.2010.05.011"
    title: "Spanjers, I. A. E., Wouters, P., van Gog, T., & van Merriënboer, J. J. G. (2011). An expertise reversal effect of segmentation in learning from animated worked-out examples. *Computers in Human Behavior, 27*(1), 46–52. [doi:10.1016/j.chb.2010.05.011](https://doi.org/10.1016/j.chb.2010.05.011)"
    author: "Spanjers, I. A. E., Wouters, P., van Gog, T., & van Merriënboer, J. J. G."
    q: 3
    i: "?"
    n: 75 (37 segmented, 38 continuous)
---

# Segmentation Benefits Shrink With Expertise

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · n=75 (37 segmented, 38 continuous)

The learning benefit of segmenting continuous instructional material (e.g., pausing animation or breaking narration into learner-paced segments) is largest for novices and diminishes — or reverses — as learner expertise increases.

The claim concerns dynamic, transient media (animation, video, narrated slides) where learners cannot otherwise control the pace of information delivery. It is the segmentation-specific instance of the broader [expertise reversal effect](../theories/expertise-reversal-effect.md).

## Subclaims

`q3 i?` Segmenting animated worked-out examples on probability calculation was more efficient (equal transfer performance, lower mental effort) than continuous animation for lower-prior-knowledge students, but this efficiency advantage disappeared at higher prior-knowledge levels. [→ Spanjers et al. 2011](#spanjers-et-al-2011)

## Evidence

### Spanjers et al. 2011

Spanjers, I. A. E., Wouters, P., van Gog, T., & van Merriënboer, J. J. G. (2011). An expertise reversal effect of segmentation in learning from animated worked-out examples. *Computers in Human Behavior, 27*(1), 46–52. [doi:10.1016/j.chb.2010.05.011](https://doi.org/10.1016/j.chb.2010.05.011)

`q3 · peer-reviewed experiment (not pre-registered)` · `i? · effect size not reported (regression β/t/p only)` · `n=75 (37 segmented, 38 continuous)`

76 Dutch secondary-education students (one excluded for missing data) were randomly assigned to study eight animated, narrated worked-out examples on probability calculation, presented either as one continuous stream per example or divided into 5–7 segments with 2-second pauses. Regression models with prior knowledge (centered), condition, and their interaction predicted near- and far-transfer efficiency (performance combined with invested mental effort). The prior-knowledge × condition interaction was significant for both near (β = −0.35, p = .04) and far transfer efficiency (β = −0.34, p = .05): at one SD below the mean (lower prior knowledge), segmented examples were significantly more efficient than continuous ones (near β = 0.39, p = .01; far β = 0.33, p = .03), but at one SD above the mean (higher prior knowledge) this difference had disappeared (near β = −0.05, p = .72; far β = −0.10, p = .51), driven mainly by continuous-condition mental effort dropping sharply with rising prior knowledge while segmented-condition effort stayed flat. No significant interaction was found on raw transfer performance alone, only on mental effort and the composite efficiency measure.

## Discussion

**What the recorded study shows.** Spanjers et al. (2011) found the benefit of segmentation on instructional efficiency (performance relative to mental effort), not on test performance alone, and found it disappearing at high prior knowledge rather than reversing. A full reversal, continuous animation beating segmented animation for more expert learners, is left by the authors as an open question.

**Expertise reversal as the underlying mechanism.** Segmentation reduces extraneous cognitive load by giving novices control over the pace of information delivery and preventing overload from transient, continuous presentations. As expertise grows, learners no longer need external pacing support; segmenting can then add unnecessary processing — re-integration overhead across segment boundaries — or simply waste time, consistent with the broader [expertise reversal effect](../theories/expertise-reversal-effect.md). The same pattern appears for other load-reducing scaffolds such as [worked examples](../elements/demonstration.md), which also lose and eventually reverse their advantage with expertise.

**Boundary conditions.** The claim applies to transient, learner-uncontrolled presentations (animation, video, narrated slides). For static or already self-paced material, segmentation has little to offer novices either, so the expertise interaction is most visible in dynamic media. Learner-controlled pacing is a key moderator: when learners can pause and replay freely, the added value of designer-imposed segments shrinks for everyone.

**Design implication.** Treat segmentation as a fading scaffold: begin with designer-imposed segments for novices encountering high-element-interactivity material, then progressively hand pacing control to learners — or lengthen segments — as diagnostic evidence of growing expertise accumulates. This mirrors the fading logic used for [worked examples](../elements/demonstration.md) in [cognitive load management](../principles/cognitive-load-management.md) more broadly.

**Constraints.** Imposing segments on advanced learners can impose re-integration costs across boundaries and slow experienced learners who would otherwise move at their own pace [-M]. When the medium already supports full learner pacing (pause, scrub, replay), designer-imposed segmentation adds little for any expertise level [~M]. Coarse segmentation of low-element-interactivity content may fragment material without any compensating load reduction, making the expertise interaction moot [~W].

**Open questions.** The expertise level at which segmentation benefits disappear likely varies by domain complexity and segment granularity. Fine-grained segmentation may retain value longer than coarse segmentation, but this has not been firmly established. Studies specifically testing segmentation × expertise interactions are scarcer than for worked examples, so confidence in the precise crossover point is limited.

## Related Claims

- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — the same expertise reversal pattern for a closely related load-reducing scaffold
- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — another load-reduction principle whose benefits are strongest for novices
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — segmentation is a dynamic-media application of chunking, with the same novice-dependence
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the overload that segmentation prevents occurs mainly under high element interactivity, typical of novice learning