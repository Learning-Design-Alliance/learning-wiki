---
type: claim
title: Redundancy Effect Impairs Learning
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: redundancy-effect-impairs-learning
evidence_strength: weak
---

# Redundancy Effect Impairs Learning

> **Claim** · [All claims](index.md)
> **Evidence** · none recorded yet

When the same information is presented simultaneously through multiple channels — such as narrated text duplicating on-screen text, or graphics labeled with both text and redundant audio — learning is impaired relative to presenting the information once, because learners must coordinate and re-process identical material.

## Subclaims

<!-- TODO -->

## Evidence

<!-- TODO -->

## Discussion

The redundancy effect is one of the classic effects predicted by [Cognitive Load Theory](../theories/cognitive-load-theory.md). The proposed mechanism is that when identical information is presented in two formats, working memory resources are consumed holding one representation while the learner maps it onto the other, and the learner may be forced to process both even though one is sufficient [-M]. This is distinct from the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md), where the harm comes from *irrelevant* rather than duplicated material — redundant material is relevant, just unnecessarily repeated. Both effects operate through the same underlying constraint that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) [-M].

The effect is strongly moderated by learner expertise [~S]. For novices, redundant duplication of essential information can impair learning; for more advanced learners, the same duplication may be harmless or even helpful, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~S]. Designers should therefore treat redundancy as a novice-focused constraint and fade redundant support as competence develops — the same fading logic that governs when [worked examples can become counterproductive for advanced learners](worked-examples-expertise-reversal.md).

Boundary conditions worth noting: redundancy in the strict CLT sense refers to *same-information* duplication. Complementary material that adds new information (e.g., a diagram with genuinely explanatory labels, or narration that elaborates rather than reads the text) is not redundant and does not fall under this claim. Similarly, signposting or structural cues that help learners navigate material may look like redundancy but serve a different function — see [clear structure improves learning](clear-structure-improves-learning.md) [+M].

Practical implications for multimedia design: avoid on-screen text that verbatim duplicates narration [-M]; prefer graphics with concise integrated labels over graphics plus redundant audio [-M]; and when accessibility requires captions, consider whether they duplicate or complement the audio track. Where duplication is unavoidable (e.g., regulatory or accessibility requirements), giving learners control over pacing may reduce the coordination cost, though this interaction is not yet well quantified [~W]. Consolidating information so it need not be duplicated at all — for example through [chunking](chunking-reduces-working-memory-load.md) — is a complementary mitigation [+M].

Open questions: the exact magnitude of the effect across domains and media, and how it interacts with learner control (e.g., self-paced versus system-paced multimedia), remain areas where this page needs primary evidence before specific design thresholds can be recommended.

## Related Claims

- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — adjacent CLT effect; harm from extraneous rather than duplicated material
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the working-memory mechanism through which redundancy exerts its cost
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — one mitigation: consolidating information so it need not be duplicated
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — expertise reversal applied to example-based support
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the moderator that makes redundancy harmful for novices but not experts
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the parent theory predicting the effect