---
type: claim
title: Redundancy Harms Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: redundancy-harms-learning
evidence_strength: moderate
sources:
  - id: trypke-et-al-2023
    resource: "https://doi.org/10.3389/fpsyg.2023.1148035"
    title: "Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)"
    author: "Trypke, M., Stebner, F., & Wirth, J."
    q: 3
    i: "?"
    n: "63 studies (44 in the narration+on-screen-text \"scenario 4\")"
---

# Redundancy Harms Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · n=63 studies (44 in the narration+on-screen-text "scenario 4")

Presenting the same information simultaneously in multiple formats — most commonly narrating on-screen text verbatim — imposes extraneous cognitive load and can impair learning relative to presenting the information once.

## Subclaims

`q3 i?` A literature review of 63 studies finds that adding written text which duplicates narration (verbal/"working-memory-channel" redundancy) most often impairs learning, though the direction reverses for some moderators (older learners, learner-paced delivery, non-identical/abridged text). [→ Trypke et al. 2023](#trypke-et-al-2023)

## Evidence

### Trypke et al. 2023

Trypke, M., Stebner, F., & Wirth, J. (2023). Two types of redundancy in multimedia learning: a literature review. *Frontiers in Psychology, 14*, Article 1148035. [doi:10.3389/fpsyg.2023.1148035](https://doi.org/10.3389/fpsyg.2023.1148035)

`q3 · systematic literature review (63 studies)` · `i? · no pooled effect size reported` · `n=63 studies (44 in the narration+on-screen-text "scenario 4")`

This review classifies redundancy effects across 63 multimedia-learning experiments into "content redundancy" (duplicated information, independent of channel) and "working-memory channel redundancy" (two sources competing for the same processing channel). For the case closest to the classic redundancy principle — narration duplicated by identical on-screen text — the authors report that among the 44 studies adding written text to narrated visualizations, several classic experiments (e.g., [Kalyuga et al. 1999](https://doi.org/10.1002/(SICI)1099-0720(199912)13:4%3C351::AID-ACP589%3E3.0.CO;2-6), Mayer et al. 2001, Yue et al. 2013) found that "the animation, narration, and identical written text group performed worse on retention and transfer tests," and note the finding "aligns with the findings of the meta-analysis on the verbal redundancy effect, which shows that narrations accompanied by identical written text impaired learning (e.g., Adesope and Nesbit, 2012)." The review also identifies moderators — degree of overlap (abridged/keyword text is less harmful than verbatim duplication), learner age, prior knowledge, and pacing — that shift or reverse the direction of the effect, which is why the overall pattern is reported as heterogeneous rather than as one pooled effect.

## Discussion

**Mechanism.** Under [cognitive load theory](../theories/cognitive-load-theory.md), redundancy is one of the classic sources of extraneous load: when identical content is duplicated across channels, learners must reconcile the copies, consuming working-memory resources that could otherwise go to schema construction [~M]. The most-studied case is simultaneous narration of identical on-screen text, which forces visual attention and auditory processing onto the same words rather than letting visuals carry the diagram and narration carry the explanation. This is a core multimedia-design principle: duplication across channels degrades learning relative to narration-plus-graphics [~M].

**Boundary conditions.** The redundancy effect is not universal. It is primarily a *novice* phenomenon; as expertise grows, redundant formats can become helpful rather than harmful — the same expertise-reversal pattern documented for [worked examples](worked-examples-expertise-reversal.md) and formalized in the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Redundant on-screen text may also help when learners cannot process audio (hearing impairment, noisy environments, non-native listeners), when text serves as a navigational or reference aid rather than a duplicate of narration, or when pacing is fully learner-controlled [~W]. The effect applies to *identical* duplication; complementary information across channels (e.g., narration plus a non-redundant diagram) is beneficial, not harmful — see the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md) for the related harm from irrelevant material.

**Design implication.** Prefer a single well-chosen presentation of each idea. When using narration with visuals, keep on-screen text minimal and non-duplicative rather than a verbatim transcript. Where accessibility or environment demands captions or transcripts, treat them as an accommodation (see [Accommodations](../elements/accommodations.md)) rather than a default for all learners. This pairs naturally with [cognitive load management](../principles/cognitive-load-management.md) and [chunking](chunking-reduces-working-memory-load.md) as part of a broader extraneous-load audit of instructional materials.

**Open questions.** The one review recorded above reports no pooled effect size, and finds the effect moderated by text overlap, learner age and pacing. The interaction between redundancy and learner-controlled pacing, and the threshold of expertise at which redundancy flips from harmful to helpful, remain under-specified.

## Related Claims

- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — a sibling extraneous-load effect from adding non-essential material
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the underlying mechanism redundancy exploits
- [Chunking reduces working-memory load.](chunking-reduces-working-memory-load.md) — a complementary load-management strategy
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — expertise reversal, the key moderator of redundancy effects
- [Cognitive load reduction improves learning.](cognitive-load-reduction-improves-learning.md) — the general principle this claim instantiates
- [Clear structure improves learning.](clear-structure-improves-learning.md) — a positive-design counterpart: one well-organized presentation instead of duplicated ones