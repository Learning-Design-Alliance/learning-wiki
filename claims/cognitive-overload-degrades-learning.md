---
type: claim
title: Cognitive Overload Degrades Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: cognitive-overload-degrades-learning
evidence_strength:
sources:
  - id: noetel-et-al-2022
    resource: "https://doi.org/10.3102/00346543211052329"
    title: "Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C. (2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research, 92*(3), 413–454. [doi:10.3102/00346543211052329](https://doi.org/10.3102/00346543211052329)"
    author: "Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C."
    q: 4
    i: 1
    n: 29 reviews (1,189 studies, 78,177 participants)
  - id: sweller-1988
    resource: "https://doi.org/10.1207/s15516709cog1202_4"
    title: "Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)"
    author: Sweller, J.
    q: 3
    i: "?"
    n: unreported (abstract only)
---

# Cognitive Overload Degrades Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i1` small

When the demands of a learning task exceed the capacity of working memory, learning suffers. This claim covers the general mechanism; specific load-reduction techniques are treated in their own pages.

## Subclaims

`q4 i1` Across 29 systematic reviews (1,189 studies, 78,177 participants), multimedia designs that cut extraneous load improved learning on average (g = 0.38), and the benefit was far larger for complex, high-element-interactivity materials (g = 0.70) than simple ones (g = 0.20), consistent with overload hurting learning mainly when total demand is high. [→ Noetel et al. 2022](#noetel-et-al-2022)

`q3 i?` Conventional means–ends problem solving uses so much processing capacity that little is left for schema acquisition, which the author supports with a computational model and experimental evidence; the abstract reports no effect size. [→ Sweller 1988](#sweller-1988)

## Evidence

### Noetel et al. 2022

Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C. (2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research, 92*(3), 413–454. [doi:10.3102/00346543211052329](https://doi.org/10.3102/00346543211052329)

`q4 · overview of systematic reviews with meta-meta-analysis` · `i1 · small-to-moderate average effect, g=0.38 (g=0.70 for complex materials)` · `n=29 reviews (1,189 studies, 78,177 participants)`

An overview of 29 systematic reviews testing how multimedia design affects learning or cognitive load. Pooling the 11 largest reviews (808 effect sizes), load-reducing design principles such as contiguity, signaling, segmenting and removing seductive details improved learning (g = 0.38, 95% CI [0.27, 0.49]). The complexity of the material (element interactivity) moderated these effects: design mattered much more for complex media (g = 0.70) than for simple media (g = 0.20), which the authors read as support for the idea that complex materials are the ones likely to cause cognitive overload without good design. Learner prior knowledge did not significantly moderate effects, so this review offers only weak support for the expertise-reversal part of the account. This is indirect evidence: it tests *reducing* load, not inducing overload.

### Sweller 1988

Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)

`q3 · peer-reviewed experiments with a computational model` · `i? · no effect size in the abstract` · `n=unreported (abstract only)`

The founding cognitive load paper. It argues that conventional problem solving by means–ends analysis takes up a relatively large amount of cognitive processing capacity, leaving that capacity unavailable for schema acquisition, and so it is an ineffective way to learn. A computational model and experimental evidence are offered in support. Only the abstract was read here, so the experiments' samples and effect sizes are not recorded.

## Discussion

**Mechanism.** Working memory can hold and process only a small number of elements at once. When intrinsic element interactivity (complexity of the material), extraneous load (poor presentation, irrelevant material), or both push total demand past that capacity, learners cannot construct or automate schemas, and performance degrades. This is the central prediction of [Cognitive Load Theory](../theories/cognitive-load-theory.md) and the theoretical basis for the related principle that [reducing cognitive load improves learning](cognitive-load-reduction-improves-learning.md).

**Sources of load.** Overload can arise from the material itself (high element interactivity for novices), from instructional design choices — e.g., split attention between diagram and text, redundant on-screen narration, irrelevant graphics — or from learner-generated inefficiencies such as means–ends search during unguided problem-solving. Designers control the second and third sources; see [Cognitive Load Reduction](../principles/cognitive-load-reduction.md) and [Chunking](../principles/chunking.md).

**Moderators.** The point at which load becomes "overload" depends on learner expertise (the [expertise reversal effect](../theories/expertise-reversal-effect.md)): scaffolds that reduce load for novices can add redundant load for experts. It also depends on prior knowledge activation, element interactivity of the domain, and whether load measurement distinguishes productive from unproductive effort. Note that some desirable difficulties — e.g., [generative](active-learning-improves-exam-performance.md) or effortful retrieval — impose load that *supports* learning; the claim applies to load that exceeds capacity, not to effort per se.

**Boundary conditions.** The claim is directional but conditional: it predicts degradation only when total demand genuinely exceeds capacity. Moderate challenge within capacity can be productive — see [Cognitive disequilibrium motivates conceptual change](cognitive-disequilibrium-motivates-conceptual-change.md). Designers should therefore treat load reduction as a means of freeing capacity for [generative processing](cognitive-load-management.md), not as an end in itself; stripping all effort from a task risks disengagement.

**Design implications.** Practical countermeasures follow directly from the mechanism: [chunking](chunking-reduces-working-memory-load.md) complex material into integrated units, removing extraneous elements (coherence), integrating text and diagrams to avoid split attention, and sequencing instruction so that element interactivity rises as schemas are automated. Load reduction is most valuable for novices facing high-element-interactivity material; for advanced learners the same supports can backfire.

**Open questions.** Evidence for this page still needs to be added — including the foundational experimental and meta-analytic work on load effects and load-measurement validity. Until then, treat the claim as well-established theoretically but under-sourced here.

## Related Claims

- [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) — extraneous material is a direct source of overload
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — a primary design countermeasure
- [Worked examples can become redundant or counterproductive for advanced learners](worked-examples-less-effective-with-expertise.md) — expertise moderates when load-reducing scaffolds help
- [Automatic word recognition frees resources for comprehension](automatic-word-recognition-frees-resources-for-comprehension.md) — automaticity lowers load in literacy tasks
- [Cognitive disequilibrium motivates conceptual change](cognitive-disequilibrium-motivates-conceptual-change.md) — moderate challenge can be productive; overload is the failure point beyond it
- [Clear Structure Improves Learning](clear-structure-improves-learning.md) — related
- [Cognitive Load Reduction Improves Learning](cognitive-load-reduction-improves-learning.md) — a narrower finding that bears on this claim
- [Cognitive Load Management](cognitive-load-management.md) — related
- [Multimedia Principles Benefit Novices](multimedia-principles-benefit-novices.md) — related
- [Signaling Improves Learning](signaling-improves-learning.md) — related
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](part-task-practice-reduces-load-for-novices.md) — a narrower finding that bears on this claim
- [Individual user goals, such as avoiding cognitive load, can contradict the objectives of the educational community](user-goals-contradict-educational-objectives.md) — related