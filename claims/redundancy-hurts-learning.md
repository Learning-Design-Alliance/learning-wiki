---
type: claim
title: On-screen text that duplicates the narration of a diagram can hurt learning, but spoken–written redundancy is not harmful on average and helps over spoken-only presentation in some conditions
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: redundancy-hurts-learning
evidence_strength: moderate
newest_evidence: 2012
sources:
  - id: kalyuga-et-al-1999
    resource: "https://doi.org/10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6"
    title: "Kalyuga, S., Chandler, P., & Sweller, J. (1999). Managing split-attention and redundancy in multimedia instruction. *Applied Cognitive Psychology, 13*(4), 351–371. [doi:10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6](https://doi.org/10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6)"
    author: "Kalyuga, S., Chandler, P., & Sweller, J."
    q: 3
    i: "?"
    kind: causal
    rigour: "?"
  - id: adesope-nesbit-2012
    resource: "https://doi.org/10.1037/a0026147"
    title: "Adesope, O. O., & Nesbit, J. C. (2012). Verbal redundancy in multimedia learning environments: A meta-analysis. *Journal of Educational Psychology, 104*(1), 250–263. [doi:10.1037/a0026147](https://doi.org/10.1037/a0026147)"
    author: "Adesope, O. O., & Nesbit, J. C."
    q: 4
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# On-screen text that duplicates the narration of a diagram can hurt learning, but spoken–written redundancy is not harmful on average and helps over spoken-only presentation in some conditions

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r?`, 1 quant-synthesis `r2` · `q3`–`q4`
> **Currency** · newest study 2012 · not yet checked against its sources · not reviewed by a person

<!-- title before 2026-10-14: Redundancy Hurts Learning -->

Presenting the same information simultaneously in multiple formats — such as on-screen text that duplicates spoken narration, or labels that restate what a diagram already shows — can impose extraneous cognitive load and impair learning relative to a single well-integrated presentation, though the recorded meta-analysis finds spoken–written redundancy not harmful on average and helpful over spoken-only presentation in some conditions. The harmful case is the redundancy principle of [Cognitive Load Theory](../theories/cognitive-load-theory.md).

## Subclaims

`q3 i?` Removing text that duplicated narration improved learning from a diagram-based multimedia lesson; the duplicate had to be processed and contributed nothing. [→ Kalyuga et al. 1999](#kalyuga-et-al-1999)

`q4 i?` A meta-analysis of 57 independent effect sizes from 33 reports found verbal redundancy is not uniformly harmful: spoken–written presentations did not differ from written-only ones and outperformed spoken-only ones, an advantage found for low prior knowledge learners, system-paced materials and picture-free materials, with prior knowledge, pacing and the inclusion of animation or diagrams as moderators. [→ Adesope & Nesbit 2012](#adesope-nesbit-2012)

`q4 i?` Displaying key terms extracted from the narration was associated with better learning than verbatim spoken–written text, and accounted for much of the advantage of spoken–written over spoken-only presentations. [→ Adesope & Nesbit 2012](#adesope-nesbit-2012)

<!-- deprecated: `q4 i?` The harmful case is specifically the one where a learner must split attention between two sources presenting the same information while a third source competes for the same channel. (Not reported in Adesope & Nesbit's abstract; removed 2026-09-27 after the load-bearing check.) -->

## Evidence

### Kalyuga et al. 1999

Kalyuga, S., Chandler, P., & Sweller, J. (1999). Managing split-attention and redundancy in multimedia instruction. *Applied Cognitive Psychology, 13*(4), 351–371. [doi:10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6](https://doi.org/10.1002/(SICI)1099-0720(199908)13:4<351::AID-ACP589>3.0.CO;2-6)

`q3` · `i? · no source text available to check; the entry prints no effect size` · `causal · r?`

Experiments in technical training comparing a diagram with integrated narration against the same material with redundant on-screen text. The redundant version produced worse learning, consistent with a working-memory account in which the duplicate consumes capacity without adding information.

### Adesope & Nesbit 2012

Adesope, O. O., & Nesbit, J. C. (2012). Verbal redundancy in multimedia learning environments: A meta-analysis. *Journal of Educational Psychology, 104*(1), 250–263. [doi:10.1037/a0026147](https://doi.org/10.1037/a0026147)

`q4` · `i? · the abstract prints no effect size; the full text may` · `quant-synthesis · r2`

A meta-analysis of 57 independent effect sizes from 33 experimental reports, mostly with postsecondary students, comparing spoken-only, written-only and spoken–written (text plus verbatim speech) presentations on retention and transfer. Spoken–written and written-only presentations did not differ, and spoken–written presentations *outperformed* spoken-only ones. That advantage depended on prior knowledge, pacing and the inclusion of animation or diagrams: it was found for low prior knowledge learners, system-paced materials and picture-free materials. Presentations showing key terms extracted from the narration were associated with better outcomes than verbatim spoken–written ones. The abstract does not report verbal redundancy as harmful in any configuration, which is why this study qualifies the claim rather than supporting it and should be cited with a contextual tag.

## Studies bearing on this claim

<!-- synthesis:start -->
*Without a competing picture, do the same words spoken and written help or hurt, and for whom?* This table gathers the studies behind this claim and the 13 narrower claims that bear on it: **8 distinct studies** (3 causal, 2 quant-synthesis, 2 review, 1 theoretical), `q1`–`q4`, 3 of 8 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Kalyuga et al. 1999](<https://doi.org/10.1002/(sici)1099-0720(199908)13:4<351::aid-acp589>) | q3 · causal · r? | i? | this claim |
| [Adesope & Nesbit 2012](https://doi.org/10.1037/a0026147) | q3 / q4 · quant-synthesis · r2 | i?; i0; i1; i3; i2 | this claim; [Verbal redundancy (spoken–written presentation) yields a small overall learning benefit wi](verbal-redundancy-small-overall-effect.md) (counts against); [Spoken–written presentations do not outperform written-only presentations but do outperfor](spoken-written-beats-spoken-only-not-written-only.md) (qualifies); [Spoken–written advantages are larger for second-language and nonfluent first-language read](reader-fluency-prior-knowledge-moderate-redundancy.md) (qualifies); [The spoken–written advantage over spoken-only presentation appears for system-paced but no](system-paced-moderates-verbal-redundancy.md) (qualifies); [Nonsegmented spoken–written presentations show a larger advantage over spoken-only present](segmentation-moderates-verbal-redundancy.md) (qualifies); [Spoken–written advantages are larger for retention outcomes and multiple-choice test forma](outcome-constructs-test-formats-moderate-redundancy.md) (qualifies); [Verbal redundancy does not facilitate learning when materials include images or animation](images-animation-eliminate-redundancy-benefit.md) (qualifies) |
| [Noetel 2022](https://doi.org/10.3102/00346543211052329) | q3 · quant-synthesis · r3 | i3 | [Captioning second-language videos produces large benefits for comprehension and vocabulary](captioning-second-language-videos-large-benefits.md) (qualifies) |
| [Trypke et al. 2023](https://doi.org/10.3389/fpsyg.2023.1148035) | q3 · review · r? | i? | [Redundant on-screen text impairs learning when it competes with a visualization, though wr](redundancy-principle.md) (supports) |
| Kutbay 2020 | q2 · causal · r2 | i? | [In one middle-school quasi-experiment, adding written text to spoken narration makes no si](redundancy-effect-not-significant-middle-school.md) (qualifies) |
| [Clinton 2016](https://doi.org/10.1080/00220973.2015.1048847) | q3 · causal · r2 | i? | [Redundant text in the diagram did not affect posttest accuracy or difficulty ratings](redundant-text-no-effect-posterior-probability-lesson.md) (qualifies) |
| [Richard E. Mayer 2008](https://doi.org/10.1037/0003-066x.63.8.760) | q3 · review · r2 | i2 | [Redundancy principle: animation plus narration beats animation, narration, and on-screen t](redundancy-principle-mayer-2008.md) (supports) |
| [Darcy 2018](https://doi.org/10.5070/b5.35963) | q1 · theoretical · r3 | i? | [Bimodal captioned input improved L2 listening skills, generalizing to unfamiliar sentences](bimodal-captioned-input-improves-segmentation.md) (supports) |
<!-- synthesis:end -->

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
- [Instructional support suited to novices can have negative effects for more expert learners (expertise-reversal effect), so instructional design should be tailored to learner experience](expertise-reversal-effect.md) — related
- [Presenting words as spoken narration rather than on-screen text alongside graphics improves learning](modality-effect-narration-over-text.md) — related
- [Redundancy Effect Impairs Learning](redundancy-principle.md) — a broader claim this one bears on
- [Split Attention Effect Degrades Learning](split-attention-effect-degrades-learning.md) — related
- [A practice article reports that the studies it cites found better post-test outcomes from words with relevant pictures than from words alone, especially with spoken words](multimedia-principle-words-and-pictures-outcomes.md) — related
- [In one middle-school quasi-experiment, adding written text to spoken narration makes no significant difference to achievement with either abstract or concrete animation](redundancy-effect-not-significant-middle-school.md) — a narrower finding that bears on this claim
- [A narrative review cites one study in which simultaneous notes, worked example and explanation aided understanding, and another in which temporally contiguous instruction lowered perceived cognitive load](temporal-contiguity-lower-cognitive-load.md) — related
- [Avoiding double load on the visual channel improves visual knowledge (channel-overload effect)](voice-media-outperform-picture-text-overall.md) — related
- [Modality principle: graphics with spoken text beat graphics with printed text for transfer](modality-principle-mayer-2008.md) — related
- [Redundancy principle: animation plus narration beats animation, narration, and on-screen text for transfer](redundancy-principle-mayer-2008.md) — a narrower finding that bears on this claim
- [Verbal redundancy does not facilitate learning when materials include images or animation](images-animation-eliminate-redundancy-benefit.md) — reports the opposite
- [Verbal redundancy (spoken–written presentation) yields a small overall learning benefit with large between-study heterogeneity](verbal-redundancy-small-overall-effect.md) — reports the opposite
- [Multimedia design interventions yield small average improvements in cognitive load management (g = 0.22), with personalisation and modality showing the largest effects](design-principles-improve-cognitive-load-management.md) — related
- [The animation advantage is largest when instruction includes no accompanying text](animation-advantage-largest-without-accompanying-text.md) — related
- [Matching modality by conveying complementary information through auditory and visual channels increases retention, transfer, and engagement](modality-matching-complementary-channels-video.md) — related
- [Working memory is limited in capacity and includes partially independent subcomponents for auditory/verbal and visual/2- or 3-dimensional information](working-memory-partially-independent-modality-subcomponents.md) — related
- [APA presentations tend to overload the visual channel, especially with high element interactivity content](apa-visual-channel-overload.md) — related
- [Redundant speech-gesture cooperation improves recall and social perception more than complementarity](speech-gesture-redundancy-better.md) — related
- [The spoken–written advantage over spoken-only presentation appears for system-paced but not learner-paced materials](system-paced-moderates-verbal-redundancy.md) — related
- [Redundant text in the diagram did not affect posttest accuracy or difficulty ratings](redundant-text-no-effect-posterior-probability-lesson.md) — reports the opposite
- [Weeding extraneous information such as music and complex backgrounds improves retention and transfer from video](weeding-extraneous-content-improves-video-learning.md) — related
- [Spoken–written presentations do not outperform written-only presentations but do outperform spoken-only presentations](spoken-written-beats-spoken-only-not-written-only.md) — related
- [Congruent pictures paired with text facilitate reading comprehension better than text alone or pictures alone](congruent-pictures-with-text-facilitate-comprehension.md) — related
- [Redundancy effect: when one source of information is intelligible in isolation, physically integrating it with another source fails to help and eliminating the redundant source facilitates learning](redundancy-effect-elimination-of-redundant-text.md) — related
- [Synced auditory and visual information in narrated presentations produces better learning than single-channel or out-of-sync presentation](synced-audio-visual-presentation-better-learning.md) — related
- [Observing gestures embedded in instruction aids learning, especially when gestures convey a different strategy than speech](observing-gestures-in-instruction-aids-learning.md) — related
- [Mayer published seven pieces in Educational Psychology Review, including the Select–Organize–Integrate model of learning and a research-based analysis of animation as an aid to multimedia learning.](mayer-seven-epr-pieces-soi-animation.md) — related
- [Embodied action can harm learning when it adds motor demands, redundant cues, or irrelevant activity without improving understanding](action-hurts-when-adding-motor-demands.md) — related