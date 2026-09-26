---
type: claim
title: Split Attention Effect Degrades Learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: split-attention-effect-degrades-learning
aliases: [contiguity-principle-improves-learning, spatial-contiguity-improves-learning, split-attention-effect-impairs-learning, split-attention-effect-integration-improves-learning]
evidence_strength: none
sources:
  - id: schroeder-cenkci-2018
    resource: "https://doi.org/10.1007/s10648-018-9435-9"
    title: "Schroeder, N. L., & Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. *Educational Psychology Review, 30*(3), 679–701. [doi:10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)"
    author: "Schroeder, N. L., & Cenkci, A. T."
    q: 4
    i: 2
    n: 2426 (58 independent comparisons)
---

# Split Attention Effect Degrades Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=2426 (58 independent comparisons)

When learners must mentally integrate information that is physically or temporally separated — such as a diagram and its explanatory text presented apart — working memory resources are consumed by search-and-match processes, degrading learning relative to integrated presentations.

## Subclaims

`q4 i2` A meta-analysis of 58 independent comparisons (n=2426) found that spatially integrating mutually referring text and diagrams produced a medium-to-large learning benefit over spatially separated presentation, g=0.63. [→ Schroeder Cenkci 2018](#schroeder-cenkci-2018)

## Evidence

### Schroeder Cenkci 2018

Schroeder, N. L., & Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. *Educational Psychology Review, 30*(3), 679–701. [doi:10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)

`q4 · random-effects meta-analysis` · `i2 · medium-to-large effect, g=0.63` · `n=2426 (58 independent comparisons)`

A random-effects meta-analysis pooled 58 independent comparisons (total n=2426) drawn from the multimedia-learning literature contrasting spatially integrated designs (text and diagrams placed together) against spatially separated designs requiring learners to search back and forth between sources. Integrated designs produced an overall effect size of g=0.63 (p<0.001), a medium-to-large advantage consistent with the split-attention/spatial-contiguity account: physically co-locating mutually referring information removes the search-and-match burden that separated presentation imposes on working memory. The authors also examined numerous intervention- and context-related moderators and found the benefit held broadly across them, though (per the abstract) more remained to be understood about exactly which conditions maximize the effect.

## Discussion

**Mechanism.** Split attention is a core prediction of [Cognitive Load Theory](../theories/cognitive-load-theory.md): when mutually referring sources of information (e.g., a graph and its caption, an animation and its narration) are separated in space or time, learners must hold one source in working memory while locating the other, imposing extraneous load that does not contribute to schema construction [-M]. Physically integrating the sources — embedding labels in a diagram, placing text adjacent to the relevant graphic — eliminates this search-and-match process. The effect is closely related to the broader claim that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and to the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md), which addresses a different source of extraneous load (irrelevant rather than poorly positioned material).

**Boundary conditions.** Split attention is expected to matter most when the separated sources are *mutually referring and unintelligible in isolation* — a diagram that cannot be understood without its labels. If each source is independently intelligible (e.g., a decorative image beside self-contained text), integration is unnecessary and separating them may even be preferable, since redundancy imposes its own load [-M]. The effect should also be attenuated or reversed for experienced learners, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md): experts have schemas that make integration effortless, so physically integrated formats can become redundant for them [~M].

**Temporal separation.** The same logic applies across time — e.g., instructions presented before a task the learner must then perform from memory. This interacts with [chunking](chunking-reduces-working-memory-load.md): when separation is unavoidable, reducing the amount of material that must be held across the gap mitigates the cost.

**Modality as an alternative.** Separation in space is not always harmful: presenting one source in the auditory channel (e.g., spoken narration accompanying an animation) can substitute for physical integration by using different working-memory channels, though this substitution has its own boundary conditions and is treated separately from spatial integration on this page [~M].

**Design implications.** Practitioners should audit instructional materials for mutually referring elements that require back-and-forth search: legends placed far from figures, key terms defined on a different page from the diagram that uses them, or step-by-step instructions separated from the interface they describe. The remedy is usually cheap — embed labels in the graphic, place captions beside the relevant visual region, or put instructions on screen rather than in a separate manual. Where physical integration is impossible (e.g., lab equipment with a separate handbook), pre-teaching the referents or reducing the material held across the gap via [chunking](chunking-reduces-working-memory-load.md) reduces the cost.

**Constraints.** The split-attention remedy fails or backfires under identifiable conditions. When the two sources are *not* mutually referring — each is intelligible alone — physically integrating them creates redundancy rather than removing search costs, and separated presentation is preferable [-M]. For learners with high prior expertise, integrated formats can impose additional load rather than reduce it, per the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Integration also has limits as a universal fix: embedding text into a complex graphic can itself crowd and fragment the visual display [-W], and when material must be held across a temporal gap, integration is impossible — only [chunking](chunking-reduces-working-memory-load.md) or modality substitution mitigates the cost, and modality substitution carries its own boundary conditions (e.g., it fails when narration is long, technical, or must be re-inspected) [~M].

**Open questions.** This page currently has no evidence entries; the claim needs at least one controlled comparison of integrated versus separated formats before its strength can be rated. Key moderators to test in future entries include learner expertise, whether sources are mutually referring, and modality (audio narration can sometimes substitute for spatial integration by offloading visual channels).

*Merged from “Contiguity Principle Improves Learning” (contiguity-principle-improves-learning):* **What the recorded evidence covers.** The meta-analysis above tests spatial contiguity only (integrated against separated text and graphics). Temporal contiguity, narration presented at the same time as the animation it describes, is not tested by anything recorded here.

The contiguity principle is one of the core principles of [Cognitive Load Theory](../theories/cognitive-load-theory.md) and Mayer's multimedia learning research. The proposed mechanism is that when corresponding words and images are separated — a caption on a different page from its diagram, or narration delivered long before or after the animation it describes — learners must hold one representation in working memory while searching for its partner, imposing extraneous load that displaces [schema construction](../principles/cognitive-load-management.md). Integrating them reduces that load, consistent with the broader claim that [cognitive load reduction improves learning](../claims/cognitive-load-reduction-improves-learning.md) [+S].

Two variants are usually distinguished:

- **Spatial contiguity.** Printed words should be placed on or next to the part of the graphic they describe, rather than in a caption box or separate legend. This is closely related to the split-attention effect, where physically integrating multiple sources of information removes the need to mentally integrate them [+M].
- **Temporal contiguity.** Narration and animation should be presented simultaneously rather than successively. Successive presentation forces learners to hold the first representation in memory until the second arrives [+M].

Boundary conditions follow from the same mechanism. Integration benefits are largest for novices and for complex, element-interactive material; for experts, integrated formats can become redundant and even hurt performance, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Spatial integration can also backfire when the graphic is simple enough that separation imposes little search cost, or when on-screen text placement occludes essential parts of a dynamic visual [-W].

**Open questions.** Most supporting evidence comes from short laboratory-style multimedia lessons; effects in longer, authentic curricula and with interactive or learner-paced media are less well established [~W]. The relative contribution of spatial versus temporal contiguity when both are manipulated together also remains underexplored.

**Design implications.** In practice, contiguity is usually cheap to implement: place labels directly on diagram parts instead of numbered legends, keep captions on the same screen as their figures, and synchronize narration with the animation segment it describes rather than playing it before or after. In slide-based and video instruction, this means avoiding "title first, diagram later" layouts and avoiding narration that runs ahead of the visuals. Because the mechanism is load reduction rather than added content, contiguity improvements should not increase lesson duration — a useful sanity check that the change is targeting extraneous, not germane, load.

*Merged from “Spatial Contiguity Improves Learning” (spatial-contiguity-improves-learning):* The spatial contiguity principle is one of the core multimedia design principles in [cognitive load theory](../theories/cognitive-load-theory.md). The proposed mechanism is that when text and the graphic element it describes are far apart, learners must scan the display and hold verbal and visual information in working memory simultaneously to integrate them, imposing extraneous load [+M]. Integrating them spatially reduces that search-and-hold burden — consistent with the broader claim that [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) and that [chunking reduces working memory load](chunking-reduces-working-memory-load.md).

**Design implications.** In practice, spatial integration means placing labels directly on diagram parts rather than in a separate legend, embedding captions beneath or beside the specific figure they describe rather than on a following page, and annotating screenshots at the point of the feature being explained. The same logic applies to slide design, textbook layout, and instructional software interfaces: any design that forces learners to hold a verbal description in mind while searching a visual for its referent is a candidate for spatial integration [+M].

**Boundary conditions.** Integration helps most when learners are novices who lack the knowledge to compensate for poor layout; for highly experienced learners, integrated formats can become redundant and lose their advantage [~M], mirroring the expertise-reversal pattern documented in [expertise reversal effect](../theories/expertise-reversal-effect.md). Integration also presupposes that the text is genuinely tied to parts of the graphic — captions or commentary that are not element-specific may not benefit, and adding any text near a graphic must still respect the [coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) [-M]. Overcrowding a graphic with integrated labels can itself create a cluttered display that imposes its own extraneous load [~M], so integration should be paired with [cognitive load management](cognitive-load-management.md) rather than treated as a license to add text.

**Distinguish from temporal contiguity.** Spatial integration should be distinguished from temporal contiguity (presenting words and images simultaneously rather than successively); the two principles are related but empirically separable, and this page covers only the spatial case.

**Evidence status.** No studies are yet catalogued on this page. The spatial contiguity principle is well established in the multimedia learning literature, but specific experiments and meta-analytic estimates still need to be added before an evidence strength can be assigned.

*Merged from “Split attention between mutually referring sources of information impairs learning” (split-attention-effect-impairs-learning):* **Mechanism.** Split attention is a core prediction of [Cognitive Load Theory](../theories/cognitive-load-theory.md): when related sources of information are separated in space or time, learners must hold one source in working memory while searching for the other, imposing extraneous load that does not contribute to schema construction [~M]. Physically integrating the sources — placing text labels directly on a diagram, or narrating over the relevant part of an animation — removes the search-and-match process, and is one of the primary levers in [cognitive load reduction](../principles/cognitive-load-reduction.md) [+M].

**Boundary conditions.** The effect is strongest for low-knowledge learners processing complex, interdependent materials [~M]. For simple materials or highly knowledgeable learners, integration may add little or may even become redundant, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Temporal separation (e.g., a lecture slide shown long after the relevant diagram) produces the same integration burden as spatial separation [~M].

**Design implication.** Designers should integrate mutually referring sources of information on-screen or on-page rather than relying on learners to hold one in mind while locating the other [+M]. This is closely related to, but distinct from, the coherence principle: split attention concerns the *placement* of necessary information, while [irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) concerns the removal of unnecessary information. Both operate through the same working-memory bottleneck described in [cognitive overload degrades learning](cognitive-overload-degrades-learning.md).

**Open questions.** Most evidence comes from laboratory studies with diagram–text materials; the magnitude of the effect in authentic digital learning environments, and its interaction with learner-controlled pacing, remains less well established [~W]. Learner-controlled pacing may partially mitigate split attention by allowing learners to alternate between separated sources rather than holding one in memory, but this moderation has not been firmly established [~W].

*Merged from “Split Attention Effect Integration Improves Learning” (split-attention-effect-integration-improves-learning):* **Mechanism.** Split attention is a core extraneous-load effect within [Cognitive Load Theory](../theories/cognitive-load-theory.md). When two mutually referring sources of information (such as a diagram and a caption, or a graphic and narrated text) are separated in space or time, learners must hold one source in working memory while searching for the other, consuming working-memory resources that would otherwise support schema construction. Physically integrating the sources — embedding labels in a diagram, placing text adjacent to the relevant graphic element — or temporally synchronizing them removes the need for this search-and-hold process [~M].

**Boundary conditions.** Integration is only beneficial when the separated sources are *mutually indispensable*: each is unintelligible without the other. When one source is redundant (e.g., a caption that fully restates what the diagram shows), integrating or presenting both can impose unnecessary load, and removing the redundant source is preferable — see [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) [~M]. Integration may also lose its benefit, or reverse, as expertise develops, because experts can self-integrate separated sources and may find integrated formats redundant — consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Integration also does not help when sources can be understood sequentially and independently; in that case separation imposes little or no integration cost.

**Open questions.** Most supporting work comes from controlled laboratory-style experiments with novices in technical domains (geometry, statistics, electrical circuits). Generalization to long-form digital learning environments, mobile layouts, and learner-controlled integration (e.g., allowing learners to toggle between split and integrated views) remains under-researched [~W].

**Design implications.** For novice audiences, designers should place explanatory text directly at the point of reference on a graphic, embed labels within diagrams rather than in legends, and temporally synchronize narration with the animation segment it describes. Before integrating, check whether each source is indispensable; if not, cut the redundant one rather than merging it. These recommendations pair naturally with [Cognitive Load Management](../principles/cognitive-load-management.md) and [Chunking](../principles/chunking.md) when structuring complex multimedia materials.

## Related Claims

- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — split attention is one mechanism by which extraneous load produces overload
- [Coherence principle: irrelevant material hurts learning.](coherence-principle-irrelevant-material-hurts-learning.md) — a parallel source of extraneous load from unnecessary rather than poorly placed material
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — a mitigation strategy when temporal separation of information is unavoidable
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework from which the split attention effect is derived
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — predicts the split-attention cost shrinks or reverses as learner expertise grows
- [Cognitive load reduction improves learning.](cognitive-load-reduction-improves-learning.md) — the broader claim that reducing extraneous load, including via integration, improves outcomes
- [Pure contiguity fails to explain cognitive learning: repeated contiguity between cognitions does not make one evoke the other](contiguity-alone-fails-in-cognitive-learning.md) — related
- [Concept mapping improves learning](concept-mapping-improves-learning.md) — related
- [Multimedia Principle Improves Learning](multimedia-principle-improves-learning.md) — related
- [Expertise Reversal Guidance Hurts Experts](expertise-reversal-guidance-hurts-experts.md) — related
- [Redundancy Hurts Learning](redundancy-hurts-learning.md) — related
- [A majority of surveyed teachers report presenting words and corresponding graphics simultaneously, consistent with the modality effect](teachers-report-simultaneous-words-graphics-presentation.md) — related
