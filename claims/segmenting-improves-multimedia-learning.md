---
type: claim
title: Segmenting Improves Multimedia Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: segmenting-improves-multimedia-learning
aliases: [segmenting-principle-improves-multimedia-learning]
evidence_strength:
sources:
  - id: rey-et-al-2019
    resource: "https://doi.org/10.1007/s10648-018-9456-4"
    title: "Rey, G. D., Beege, M., Nebel, S., Wirzberger, M., Schmitt, T. H., & Schneider, S. (2019). A Meta-analysis of the Segmenting Effect. *Educational Psychology Review, 31*(2), 389–419. [doi:10.1007/s10648-018-9456-4](https://doi.org/10.1007/s10648-018-9456-4)"
    author: "Rey, G. D., Beege, M., Nebel, S., Wirzberger, M., Schmitt, T. H., & Schneider, S."
    q: 4
    i: "?"
    n: 56 studies / 88 pairwise comparisons
---

# Segmenting Improves Multimedia Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · n=56 studies / 88 pairwise comparisons

Presenting continuous multimedia material (e.g., a narrated animation) in learner-paced segments rather than as a continuous unit reduces cognitive overload and improves learning.

## Subclaims

`q4 i?` A meta-analysis of 56 studies (88 pairwise comparisons) finds a significant segmenting effect — learner- or system-paced segmentation of multimedia instruction improves retention and transfer versus continuous presentation, with reported effects described as small to medium. [→ Rey et al. 2019](#rey-et-al-2019)

## Evidence

### Rey et al. 2019

Rey, G. D., Beege, M., Nebel, S., Wirzberger, M., Schmitt, T. H., & Schneider, S. (2019). A Meta-analysis of the Segmenting Effect. *Educational Psychology Review, 31*(2), 389–419. [doi:10.1007/s10648-018-9456-4](https://doi.org/10.1007/s10648-018-9456-4)

`q4 · well-powered meta-analysis (56 studies, 88 comparisons)` · `i? · effect size not stated in what was read (abstract describes "small to medium" without a pooled value)` · `n=56 studies / 88 pairwise comparisons`

A meta-analysis of 56 investigations (88 pairwise comparisons) testing whether presenting multimedia instruction in learner-paced segments, rather than as a continuous unit, improves learning. It finds a significant segmenting effect with small-to-medium effects on both retention and transfer performance, and reports that segmentation also reduces overall cognitive load and increases learning time; these four effects held specifically for system-paced segmentation. Moderator analyses indicated learners with high prior knowledge benefited more from segmenting than learners with no or low prior knowledge, on retention performance.

## Discussion

**Mechanism.** Segmenting is grounded in cognitive load theory (see [Cognitive Load Theory](../theories/cognitive-load-theory.md)): continuous narrated animations are transient — each element disappears before the learner has fully processed it, forcing simultaneous processing of essential and still-unintegrated material. Segmenting gives learners time to complete one processing cycle before the next begins, and is one of the standard multimedia design principles alongside coherence and signaling. It is the temporal analogue of [chunking](../claims/chunking-reduces-working-memory-load.md): where chunking groups content spatially or structurally, segmenting breaks it into digestible time slices.

**Boundary conditions.** The benefit is expected primarily for novice learners processing complex, high-element-interactivity material; for simple content or more expert learners, segmenting may add unnecessary interruptions with little gain — a likely instance of the expertise reversal pattern (see [Expertise Reversal Effect](../theories/expertise-reversal-effect.md)). Whether segmentation is system-controlled or learner-controlled matters: learner pacing is generally assumed to be the more effective form, but this raises questions about whether weaker self-regulators actually pause at meaningful boundaries — an open question the current evidence base does not yet resolve. Segment boundaries should fall at conceptual breaks (e.g., between causal steps in a process animation), not at arbitrary time intervals; poorly placed breaks may fragment an integrated causal model rather than support its construction.

**Design implications.** In practice, segmenting pairs naturally with other load-management moves: adding [advance organizers](../elements/advance-organizers.md) before each segment orients learners to what is coming, and brief summaries or [check-ins](../elements/check-in.md) between segments can consolidate each processing cycle. Video platforms that expose chapter markers and playback-speed control (e.g., YouTube chapters, Khan Academy's lesson-split videos, Coursera's segmented lecture units) operationalize learner-paced segmenting at scale. Designers should resist the temptation to equate "segmented" with "short" — a segment that ends mid-causal-chain can be worse than a longer continuous presentation, because it forces re-activation of incomplete models at each restart.

**Status.** This page currently has no evidence entries. Studies still need to be added before the claim can be rated; the strength field is intentionally left blank.

*Merged from “Segmenting Principle Improves Multimedia Learning” (segmenting-principle-improves-multimedia-learning):* **Mechanism.** Segmenting is grounded in cognitive load theory: continuous animations with narration impose extraneous load because essential processing of one element may be interrupted by the arrival of the next. Segmenting — often operationalized as "continue" buttons after each segment — gives learners time to complete essential processing before moving on. It is closely related to [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) and to pre-training, which achieves a similar effect by front-loading component names and characteristics. Both segmenting and pre-training address the same underlying problem described in [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md): essential processing exceeding working memory capacity.

**Moderators and boundary conditions.** The benefit is expected mainly for novice learners and for complex, fast-paced, continuous material; simple or already-familiar content may not need segmenting, and excessive fragmentation could disrupt the formation of a coherent causal model. Learner control over pacing is a related but distinct design variable — segmenting with system-imposed pauses can outperform simple learner control when learners pause at non-optimal points. These boundary conditions should be confirmed against the evidence once entries are added.

**Design implications.** Practical implementations segment at meaningful boundaries — steps in a process, stages in a causal chain — rather than at arbitrary time intervals. Each segment should be small enough that its essential processing fits within working memory, but large enough to preserve the causal or procedural relations between elements. Pairing segmenting with other load-reduction techniques from [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) (e.g., removing decorative material per the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md)) is likely to be complementary, since both reduce extraneous processing without removing essential content.

**Open questions.** Optimal segment size, whether learner-paced or system-paced segmentation is superior, and how segmenting interacts with the coherence principle remain active design questions. It is also unresolved whether segmenting effects persist for learners with higher prior knowledge, where an expertise-reversal pattern (see [Expertise reversal effect](../theories/expertise-reversal-effect.md)) could attenuate or reverse the benefit.

**Evidence status.** This page currently has no verified evidence entries. The segmenting principle is one of the best-established multimedia learning principles in the literature, but per wiki policy, specific studies must be added through a verified evidence pass before any strength rating is assigned.

## Related Claims

- [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) — the overload mechanism segmenting is designed to prevent
- [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) — segmenting is the temporal analogue of chunking
- [Coherence principle: irrelevant material hurts learning.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) — companion multimedia principle for reducing extraneous load
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework from which the segmenting principle derives
- [Expertise Reversal Effect](../theories/expertise-reversal-effect.md) — explains why segmenting benefits may shrink or reverse for advanced learners
- [Advance organizers improve learning.](../claims/advance-organizers-improve-learning.md) — organizers before each segment can orient processing at boundaries
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — segmenting is the temporal, multimedia-specific form of chunking
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — the load mechanism segmenting is designed to prevent
- [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) — companion multimedia principle reducing extraneous load
- [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — the broader family of extraneous-load reductions segmenting belongs to
- [Cognitive Load Management](cognitive-load-management.md) — possibly the same claim (merge candidate)
- [Learner Paced Beats System Paced Complex Material](learner-paced-beats-system-paced-complex-material.md) — a narrower finding that bears on this claim
- [Segmentation Benefits Shrink With Expertise](segmentation-benefits-shrink-with-expertise.md) — a narrower finding that bears on this claim
- [Clear Structure Improves Learning](clear-structure-improves-learning.md) — related
