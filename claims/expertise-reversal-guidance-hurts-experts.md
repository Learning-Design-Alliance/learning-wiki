---
type: claim
title: Expertise Reversal Guidance Hurts Experts
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: expertise-reversal-guidance-hurts-experts
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

# Expertise Reversal Guidance Hurts Experts

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2`–`q3`

Instructional guidance that benefits novices — worked examples, prompts, explanations — can become redundant or actively counterproductive for more advanced learners, who must reconcile it with knowledge they already possess. [-M]

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

The expertise reversal effect is the dynamic counterpart to guidance benefits for novices. Under [cognitive load theory](../theories/cognitive-load-theory.md), guidance reduces the search burden that overwhelms novices; but once learners have automated domain schemas, that same guidance duplicates information they can generate internally, imposing extraneous load and interfering with schema construction. The effect is therefore inherently conditional: the *same* instructional treatment produces opposite effects at different levels of expertise, and no fixed level of guidance is optimal across a learning trajectory.

Practical consequences follow. Guidance should be faded as competence grows rather than held constant — see [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md). Adaptive designs that tailor guidance to measured learner expertise outperform one-size-fits-all sequences. Assessment of prior knowledge is thus a prerequisite for applying any guidance-heavy pattern such as [worked examples](../elements/demonstration.md) or [scaffolding](../elements/scaffolding.md), and supports [adaptive difficulty](../elements/adaptive-difficulty.md) designs that adjust support to current competence.

Boundary conditions matter. The effect is documented primarily for guidance that duplicates what experts can already derive — full worked steps, redundant explanations, high-support scaffolds. Guidance that adds genuinely new information (e.g., feedback on errors, novel problem constraints) does not automatically reverse; the mechanism is redundancy, not the mere presence of support. Expertise is also domain-specific: a learner expert in one topic of a course may still be a novice in the next, so reversal must be assessed per topic, not per student.

Open questions include how finely expertise must be measured (domain-specific vs. general ability) and how quickly guidance should be faded within a single lesson versus across a curriculum. Because this page currently has no catalogued evidence entries, effect sizes and boundary conditions still need to be sourced before the claim can be rated.

## Related Claims

- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — the best-documented instance of expertise reversal
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the theoretical account in cognitive load theory
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the load mechanism by which redundant guidance harms experts
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — experts' chunked schemas are what make guidance redundant for them