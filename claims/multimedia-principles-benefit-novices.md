---
type: claim
title: Multimedia Principles Benefit Novices
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: multimedia-principles-benefit-novices
evidence_strength: moderate
sources:
  - id: kalyuga-et-al-2003
    resource: "https://doi.org/10.1207/s15326985ep3801_4"
    title: "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/s15326985ep3801_4](https://doi.org/10.1207/s15326985ep3801_4)"
    author: "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J."
    q: 2
    i: "?"
    n: N/A (review; ~10 primary studies cited)
  - id: kalyuga-et-al-1998
    resource: "https://doi.org/10.1518/001872098779480587"
    title: "Kalyuga, S., Chandler, P., & Sweller, J. (1998). Levels of expertise and instructional design. *Human Factors, 40*(1), 1–17. [doi:10.1518/001872098779480587](https://doi.org/10.1518/001872098779480587)"
    author: "Kalyuga, S., Chandler, P., & Sweller, J."
    q: 3
    i: "?"
    n: N/A (abstract only; per-experiment n not stated in the text read)
---

# Multimedia Principles Benefit Novices

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2`–`q3`

Multimedia design principles — presenting words and pictures together, excluding extraneous material, and managing channels and segments — tend to yield larger learning benefits for learners with low prior knowledge than for more experienced learners.

## Subclaims

`q2 i?` A synthesis of cognitive-load studies across split-attention/redundancy, modality, worked-example, isolated-elements and imagination-effect paradigms finds that guidance formats which help novices (integrated text, worked examples, auditory narration, isolated elements, direct study) repeatedly lose their advantage — and in several paradigms reverse to a disadvantage — once learners have acquired domain-specific schemas. [→ Kalyuga et al. 2003](#kalyuga-et-al-2003)

`q3 i?` In three experiments teaching electrical trainees to read circuit diagrams, novice trainees learned better from diagrams with integrated explanatory text, but as trainees gained experience the best format shifted to a diagram with the text eliminated, and the most experienced trainees performed significantly better with text removed than with it present. [→ Kalyuga et al. 1998](#kalyuga-et-al-1998)

## Evidence

### Kalyuga et al. 2003

Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/s15326985ep3801_4](https://doi.org/10.1207/s15326985ep3801_4)

`q2 · narrative review of experimental cognitive-load studies` · `i? · no pooled effect size reported (individual experiments described as producing statistically significant reversals, but no d/F values given in the text)` · `n=N/A (review; ~10 primary studies cited)`

A narrative review by the group that coined the term, synthesizing its own and others' experiments across five separate cognitive-load paradigms — split-attention/redundancy (including the Kalyuga, Chandler, & Sweller (1998) study below), modality/redundancy, worked examples, isolated interacting elements, and the imagination effect. In each paradigm the same instructional design that most helped inexperienced learners either lost its advantage or actively hurt more experienced learners once they held relevant schemas, because processing the extra guidance became redundant cross-referencing that consumes working memory rather than useful support. The review frames this as a consequence of [cognitive load theory](../theories/cognitive-load-theory.md): guidance that substitutes for a missing schema helps a novice, but the same guidance duplicates what an expert's automated schema already provides.

### Kalyuga et al. 1998

Kalyuga, S., Chandler, P., & Sweller, J. (1998). Levels of expertise and instructional design. *Human Factors, 40*(1), 1–17. [doi:10.1518/001872098779480587](https://doi.org/10.1518/001872098779480587)

`q3 · peer-reviewed experiment (three studies)` · `i? · no effect size reported in the read text (differences described as "significantly better," no d/F/p values available in the abstract)` · `n=N/A (abstract only; per-experiment n not stated in the text read)`

Three experiments with trainees learning to read electrical/circuit diagrams compared a diagram with text physically integrated onto it against a diagram-only format with the (redundant) text eliminated. For less experienced trainees, the integrated diagram-plus-text format worked best — a diagram alone was not intelligible to them. As trainees' domain experience increased across the three experiments, the best-performing format shifted, and the most experienced group performed better with the diagram-only format than with the integrated text present, replicating the split-attention benefit for novices with a redundancy-driven reversal for experts. Only the abstract was available for this entry (see provenance); the numeric effect sizes are not asserted here because they were not present in the text read.

## Discussion

**Why novices benefit more.** The theoretical rationale comes from [Cognitive Load Theory](../theories/cognitive-load-theory.md): novices lack the prior-knowledge schemas that let experienced learners compensate for poorly designed materials. Principles such as integrating words and images, signaling essential content, and segmenting animation reduce extraneous processing precisely for learners whose working memory is most easily overwhelmed — see [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and [Chunking reduces working memory load](chunking-reduces-working-memory-load.md).

**Expertise reversal as boundary condition.** The same design features that help novices can hinder advanced learners, who must process redundant explanations or unnecessary graphics they no longer need — the [expertise reversal effect](../theories/expertise-reversal-effect.md). This means "apply all multimedia principles everywhere" is the wrong takeaway; designers should match design density to learner expertise and fade support as competence grows.

**Scope caveat.** The claim is a moderator claim (principles × prior knowledge), not a claim that any single principle works in all conditions. Effects depend on the principle in question, the medium, and the domain; some principles, such as removing irrelevant material, are well supported in their own right — see [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md).

**Design implications.** For novice-facing materials, apply the principles at full strength: pair narration with images rather than on-screen text, segment continuous media into learner-paced parts, use pre-training to introduce key terms before the main explanation, and strip decorative content. As learners gain expertise, progressively relax these constraints — allow learners to skip redundant narration, permit denser integrated materials, and shift toward problem-centered formats such as [worked examples](../elements/demonstration.md) faded into independent practice.

**Open questions.** Evidence entries are still needed to quantify how large the novice advantage is for each individual principle, and whether the moderator pattern holds for newer media (interactive simulations, video) as it does for classic text-and-graphics materials.

## Related Claims

- [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) — one of the core multimedia principles whose benefit is strongest for novices
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — the mechanism the principles are designed to prevent
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — segmenting and pre-training operate through this mechanism
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework underlying the multimedia principles
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the boundary condition limiting how far these principles should be applied
- [Instructional support suited to novices can have negative effects for more expert learners (expertise-reversal effect), so instructional design should be tailored to learner experience](expertise-reversal-effect-redundant-support-harms-experts.md) — a narrower finding that bears on this claim
- [Expertise Reversal Guidance Hurts Experts](expertise-reversal-guidance-hurts-experts.md) — possibly the same claim (merge candidate)
- [Intuitive learners tend to outperform sensing learners in media-based presentations](intuitive-learners-outperform-sensing-learners.md) — related
- [Redundancy Hurts Learning](redundancy-hurts-learning.md) — related