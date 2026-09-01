---
type: claim
title: Comparing contrasting cases improves learning
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: comparing-contrasting-cases-improve-learning
evidence_strength:
---

# Comparing contrasting cases improves learning

> **Claim** · [All claims](index.md)

Learners who compare two or more cases that differ on key features — rather than studying each case in isolation — more readily notice the deep structure that distinguishes the cases and transfer that structure to new problems. The claim concerns side-by-side or immediate sequential comparison of worked cases; it does not cover studying cases one at a time without comparison.

## Subclaims

<!-- TODO -->

## Evidence

<!-- TODO -->

## Discussion

**Mechanism.** Contrasting cases work by making discriminating features visible. When two cases differ on exactly the dimension the designer wants learned, learners' attention is drawn to that dimension in a way that studying a single case cannot achieve [+W]. This aligns with the broader claim that [analogical reasoning improves transfer](analogical-reasoning-improves-transfer.md) [+M]: comparison invites learners to map structure from one case onto another, and the mapping process surfaces the relational schema that supports transfer.

**Relation to multiple-case instruction.** The claim is closely related to [Cognitive Flexibility Theory](../patterns/cognitive-flexibility-theory.md) and its recommendation of multiple representations and cases for ill-structured domains — see [Cognitive flexibility theory: multiple cases support transfer in ill-structured domains.](cognitive-flexibility-theory-multiple-cases.md). It also underpins [case-based learning](../patterns/case-based-learning.md) designs, where [case-based learning improves exam performance](case-based-learning-improves-exam-performance.md) under some conditions [~M].

**Moderators and boundary conditions.** Comparison is not automatically beneficial. If the cases differ on too many dimensions at once, learners may attend to surface features rather than the intended deep structure, and the added processing can contribute to [cognitive overload degrading learning](cognitive-overload-degrades-learning.md) [~M]. Sequencing matters: learners typically need enough prior knowledge to interpret the cases before comparison pays off, and for novices the comparison itself imposes working-memory demands that may need scaffolding — consistent with [cognitive load theory](../theories/cognitive-load-theory.md) [~M]. As expertise grows, the value of guided comparison may decline in line with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M].

**Design implications.** Effective comparisons tend to (a) vary on one or few dimensions at a time, (b) present cases side by side or in immediate succession rather than spaced apart, (c) prompt learners to state what differs and why rather than leaving comparison implicit, and (d) align case surface features so that the intended deep structure is the salient difference. These follow directly from the mechanism above: anything that obscures the discriminating dimension — extra differences, temporal separation, or unprompted comparison — weakens the effect [~W]. Prompts to articulate differences can be treated as a form of [self-explanation](../elements/self-explanation.md) layered onto the comparison itself.

**Open questions.** The evidence base for this claim has not yet been populated on this page; studies still need to be added before an evidence strength can be assigned. Key open questions include how the number of cases, the similarity of the cases, and the amount of guidance during comparison moderate the effect.

## Related Claims

- [Cognitive flexibility theory: multiple cases support transfer in ill-structured domains.](cognitive-flexibility-theory-multiple-cases.md) — multiple cases are the core delivery mechanism for contrast in ill-structured domains
- [Analogical reasoning improves transfer.](analogical-reasoning-improves-transfer.md) — comparison between cases is the engine of analogical transfer
- [Case-based learning improves exam performance.](case-based-learning-improves-exam-performance.md) — case-based designs often embed contrasting cases
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — poorly designed comparisons can overload working memory
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — well-structured cases help learners manage the load comparison imposes