---
type: claim
title: Redundancy Hurts Learning
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: redundancy-hurts-learning
evidence_strength: moderate
---

# Redundancy Hurts Learning

> **Claim** · [All claims](index.md)

Presenting the same information simultaneously in multiple formats — such as on-screen text that duplicates spoken narration, or labels that restate what a diagram already shows — imposes extraneous cognitive load and impairs learning relative to a single well-integrated presentation. This is the redundancy principle of [Cognitive Load Theory](../theories/cognitive-load-theory.md).

## Subclaims

<!-- TODO -->

## Evidence

<!-- TODO -->

## Discussion

**What counts as harmful redundancy.** The effect is specific: it concerns *duplicated* information presented in parallel channels. Classic cases include narrated animation with concurrent on-screen text repeating the narration, and graphics where printed text restates information the visual already conveys. Learners must mentally reconcile the two sources, splitting attention and consuming working memory without adding new content — the same overload mechanism described in [Cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) [+M]. Redundant duplication is thus a constraint on multimedia design: under these conditions, adding a second format *reduces* rather than supports learning [-S].

**Redundancy is not the same as complementary modalities.** Two presentations that each carry *non-overlapping* information — a diagram plus a concise verbal explanation of what it does not show — are not redundant and can support learning [+M]. The boundary condition is informational overlap, not the mere presence of two formats. Designers should ask whether each channel could stand alone; if deleting one loses nothing, it is redundant. This distinction parallels the [Coherence principle: irrelevant material hurts learning](../claims/coherence-principle-irrelevant-material-hurts-learning.md): both prescribe deleting material that adds load without adding content.

**Moderators and boundary conditions.**

- *Learner expertise.* The harm from redundancy appears mainly for novices. More knowledgeable learners can bypass the integration cost, and for them redundant text may even serve as a review aid — an instance of the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Redundancy guidelines should therefore be relaxed or reversed as expertise grows.
- *Pacing.* When learners control pacing, they can self-manage the cost of cross-referencing two sources, which weakens the effect [~M]. The effect is strongest under system-paced, transient presentations such as narrated animation, where learners cannot pause to reconcile the channels.
- *Necessity of text.* When text is needed for reasons the medium cannot serve — accessibility, technical constraints, searchability — designers should minimize overlap (e.g., condensed on-screen summaries rather than verbatim transcripts) rather than simply delete it [~W].

**Design implications.** Audit multimedia lessons for verbatim duplication: remove on-screen text that repeats narration word-for-word, replace redundant labels with brief captions that add information, and integrate explanatory text into the graphic it describes rather than placing it beside a duplicate. Where duplication is unavoidable (e.g., captioning requirements), reduce the overlap by condensing one channel. More broadly, redundancy is one of several extraneous-load sources that [cognitive load management](../claims/cognitive-load-management.md) [+M] techniques are designed to eliminate.

**Open questions.** Most of the supporting literature comes from short, lab-style multimedia lessons in well-structured domains; how strongly redundancy harms learning in long-form or ill-structured learning environments is less settled. Quantified effect sizes and replications across domains still need to be added to the Evidence section of this page.

## Related Claims

- [Coherence principle: irrelevant material hurts learning](../claims/coherence-principle-irrelevant-material-hurts-learning.md) — sibling extraneous-load effect; both prescribe deleting material that adds load without adding content.
- [Cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) — the working-memory mechanism through which redundancy exerts its negative effect.
- [Cognitive load reduction improves learning](../claims/cognitive-load-reduction-improves-learning.md) — the general claim that cutting extraneous load, of which redundancy is one source, improves outcomes.
- [Chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md) — the complementary strategy when multiple information sources must be retained.
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework in which the redundancy principle is defined.
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — explains why redundant formats can stop hurting, or even help, as learner expertise increases.