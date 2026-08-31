---
type: claim
title: Split attention between mutually referring sources of information impairs learning
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: split-attention-effect-impairs-learning
evidence_strength: moderate
---

# Split attention between mutually referring sources of information impairs learning

> **Claim** · [All claims](index.md)

When learners must mentally integrate information that is physically or temporally separated (e.g., a diagram with its explanatory text placed apart from it), working memory resources are consumed by the integration process itself, impairing learning.

## Subclaims

<!-- TODO -->

## Evidence

<!-- TODO -->

## Discussion

**Mechanism.** Split attention is a core prediction of [Cognitive Load Theory](../theories/cognitive-load-theory.md): when related sources of information are separated in space or time, learners must hold one source in working memory while searching for the other, imposing extraneous load that does not contribute to schema construction [~M]. Physically integrating the sources — placing text labels directly on a diagram, or narrating over the relevant part of an animation — removes the search-and-match process, and is one of the primary levers in [cognitive load reduction](../principles/cognitive-load-reduction.md) [+M].

**Boundary conditions.** The effect is strongest for low-knowledge learners processing complex, interdependent materials [~M]. For simple materials or highly knowledgeable learners, integration may add little or may even become redundant, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Temporal separation (e.g., a lecture slide shown long after the relevant diagram) produces the same integration burden as spatial separation [~M].

**Design implication.** Designers should integrate mutually referring sources of information on-screen or on-page rather than relying on learners to hold one in mind while locating the other [+M]. This is closely related to, but distinct from, the coherence principle: split attention concerns the *placement* of necessary information, while [irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) concerns the removal of unnecessary information. Both operate through the same working-memory bottleneck described in [cognitive overload degrades learning](cognitive-overload-degrades-learning.md).

**Open questions.** Most evidence comes from laboratory studies with diagram–text materials; the magnitude of the effect in authentic digital learning environments, and its interaction with learner-controlled pacing, remains less well established [~W]. Learner-controlled pacing may partially mitigate split attention by allowing learners to alternate between separated sources rather than holding one in memory, but this moderation has not been firmly established [~W].

## Related Claims

- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the working-memory mechanism through which split attention impairs learning
- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — companion principle about removing extraneous material rather than integrating necessary material
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — a complementary strategy for managing working-memory demands
- [Cognitive load reduction improves learning.](cognitive-load-reduction-improves-learning.md) — the broader claim that reducing extraneous load, including via integration, improves outcomes
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework from which the split-attention effect derives
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the boundary condition under which integration benefits shrink or reverse for advanced learners