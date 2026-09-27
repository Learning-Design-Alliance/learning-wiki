---
type: claim
title: Redundancy Hurts Learning
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: redundancy-hurts-learning
evidence_strength: moderate
sources:
  - id: kalyuga-et-al-1999
    resource: "https://doi.org/10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6"
    title: "Kalyuga, S., Chandler, P., & Sweller, J. (1999). Managing split-attention and redundancy in multimedia instruction. *Applied Cognitive Psychology, 13*(4), 351–371. [doi:10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6](https://doi.org/10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6)"
    author: "Kalyuga, S., Chandler, P., & Sweller, J."
    q: 3
    i: "?"
  - id: adesope-nesbit-2012
    resource: "https://doi.org/10.1037/a0026147"
    title: "Adesope, O. O., & Nesbit, J. C. (2012). Verbal redundancy in multimedia learning environments: A meta-analysis. *Journal of Educational Psychology, 104*(1), 250–263. [doi:10.1037/a0026147](https://doi.org/10.1037/a0026147)"
    author: "Adesope, O. O., & Nesbit, J. C."
    q: 4
    i: "?"
---

# Redundancy Hurts Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q4` meta-analysis and experiments · `i1`–`i2` · strongly conditional

Presenting the same information simultaneously in multiple formats — such as on-screen text that duplicates spoken narration, or labels that restate what a diagram already shows — imposes extraneous cognitive load and impairs learning relative to a single well-integrated presentation. This is the redundancy principle of [Cognitive Load Theory](../theories/cognitive-load-theory.md).

## Subclaims

`q3 i?` Removing text that duplicated narration improved learning from a diagram-based multimedia lesson; the duplicate had to be processed and contributed nothing. [→ Kalyuga et al. 1999](#kalyuga-et-al-1999)

`q4 i?` A meta-analysis of 57 studies found verbal redundancy is not uniformly harmful: spoken–written presentations did not differ from written-only ones and outperformed spoken-only ones, an advantage found for low prior knowledge learners, system-paced materials and picture-free materials, with prior knowledge, pacing and the inclusion of animation or diagrams as moderators. [→ Adesope & Nesbit 2012](#adesope-nesbit-2012)

`q4 i?` Displaying key terms extracted from the narration was associated with better learning than verbatim spoken–written text, and accounted for much of the advantage of spoken–written over spoken-only presentations. [→ Adesope & Nesbit 2012](#adesope-nesbit-2012)

<!-- deprecated: `q4 i?` The harmful case is specifically the one where a learner must split attention between two sources presenting the same information while a third source competes for the same channel. (Not reported in Adesope & Nesbit's abstract; removed 2026-09-27 after the load-bearing check.) -->

## Evidence

### Kalyuga et al. 1999

Kalyuga, S., Chandler, P., & Sweller, J. (1999). Managing split-attention and redundancy in multimedia instruction. *Applied Cognitive Psychology, 13*(4), 351–371. [doi:10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6](https://doi.org/10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6)

`q3` · `i? · no source text available to check; the entry prints no effect size`

Experiments in technical training comparing a diagram with integrated narration against the same material with redundant on-screen text. The redundant version produced worse learning, consistent with a working-memory account in which the duplicate consumes capacity without adding information.

### Adesope & Nesbit 2012

Adesope, O. O., & Nesbit, J. C. (2012). Verbal redundancy in multimedia learning environments: A meta-analysis. *Journal of Educational Psychology, 104*(1), 250–263. [doi:10.1037/a0026147](https://doi.org/10.1037/a0026147)

`q4` · `i? · the abstract prints no effect size; the full text may`

A meta-analysis of 57 independent experimental studies, mostly with postsecondary students, comparing spoken-only, written-only and spoken–written (text plus verbatim speech) presentations on retention and transfer. Spoken–written and written-only presentations did not differ, and spoken–written presentations *outperformed* spoken-only ones. That advantage depended on prior knowledge, pacing and the inclusion of animation or diagrams: it was found for low prior knowledge learners, system-paced materials and picture-free materials. Presentations showing key terms extracted from the narration were associated with better outcomes than verbatim spoken–written ones. The abstract does not report verbal redundancy as harmful in any configuration, which is why this study qualifies the claim rather than supporting it and should be cited with a contextual tag.

## Discussion

**What counts as harmful redundancy.** The effect is specific: it concerns *duplicated* information presented in parallel channels. Classic cases include narrated animation with concurrent on-screen text repeating the narration, and graphics where printed text restates information the visual already conveys. Learners must mentally reconcile the two sources, splitting attention and consuming working memory without adding new content — the same overload mechanism described in [Cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) [+M]. Redundant duplication is thus a constraint on multimedia design: under these conditions, adding a second format *reduces* rather than supports learning [-S].

**Redundancy is not the same as complementary modalities.** Two presentations that each carry *non-overlapping* information — a diagram plus a concise verbal explanation of what it does not show — are not redundant and can support learning [+M]. The boundary condition is informational overlap, not the mere presence of two formats. Designers should ask whether each channel could stand alone; if deleting one loses nothing, it is redundant. This distinction parallels the [Coherence principle: irrelevant material hurts learning](../claims/coherence-principle-irrelevant-material-hurts-learning.md): both prescribe deleting material that adds load without adding content.

**Moderators and boundary conditions.**

- *Learner expertise.* The harm from redundancy appears mainly for novices. More knowledgeable learners can bypass the integration cost, and for them redundant text may even serve as a review aid — an instance of the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Redundancy guidelines should therefore be relaxed or reversed as expertise grows.
- *Pacing.* When learners control pacing, they can self-manage the cost of cross-referencing two sources, which weakens the effect [~M]. The effect is strongest under system-paced, transient presentations such as narrated animation, where learners cannot pause to reconcile the channels. Adesope & Nesbit's (2012) meta-analysis points the other way for text plus verbatim speech: its advantage of spoken–written over spoken-only presentations was found for system-paced materials and for low prior knowledge learners, so these two moderators are unsettled.
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
- [Instructional support suited to novices can have negative effects for more expert learners (expertise-reversal effect), so instructional design should be tailored to learner experience](expertise-reversal-effect-redundant-support-harms-experts.md) — related
- [Expertise Reversal Guidance Hurts Experts](expertise-reversal-guidance-hurts-experts.md) — related
- [Presenting words as spoken narration rather than on-screen text alongside graphics improves learning](modality-effect-narration-over-text.md) — related
- [Redundancy Effect Impairs Learning](redundancy-effect-impairs-learning.md) — a broader claim this one bears on
- [Redundant on-screen text impairs learning when it competes with a visualization, though written text duplicating narration alone can help](redundancy-principle.md) — a broader claim this one bears on
- [Multimedia Principles Benefit Novices](multimedia-principles-benefit-novices.md) — related
- [Split Attention Effect Degrades Learning](split-attention-effect-degrades-learning.md) — related