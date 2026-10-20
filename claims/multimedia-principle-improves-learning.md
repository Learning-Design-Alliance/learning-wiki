---
type: claim
title: Multimedia Principle Improves Learning
status: review
generated:
  by: claude/unspecified
  at: 2026-09-25
id: multimedia-principle-improves-learning
aliases: [multimedia-learning-more-effective-with-words-and-pictures, multimedia-principle, multimedia-words-plus-images-beat-words-alone, words-and-pictures-better-than-words-alone]
evidence_strength: moderate
sources:
  - id: seufert-et-al-2025
    resource: "https://doi.org/10.3389/fpsyg.2025.1480935"
    title: "Seufert, T., Magner, U., & von Randow, J. (2025). Cucumber or grapes?—Context effects in multimedia learning. *Frontiers in Psychology, 16*, Article 1480935. [doi:10.3389/fpsyg.2025.1480935](https://doi.org/10.3389/fpsyg.2025.1480935)"
    author: "Seufert, T., Magner, U., & von Randow, J."
    q: 3
    i: 2
    n: 48; n=47 German university students
    kind: causal
    rigour: 2
  - id: lively-et-al-2023
    resource: "https://doi.org/10.1177/00938548221093283"
    title: "Lively, C. J., Snook, B., Luther, K., Mccardle, M. I., & House, J. C. (2023). A preliminary exploration of the multimedia principle's applicability for improving comprehension of youth interrogation rights. *Criminal Justice and Behavior, 50*(2), 252–271. [doi:10.1177/00938548221093283](https://doi.org/10.1177/00938548221093283)"
    author: "Lively, C. J., Snook, B., Luther, K., Mccardle, M. I., & House, J. C."
    q: 3
    i: 0
    n: 207 adults (Experiment 1); n=193 youth aged 12–17 (Experiment 2)
    kind: causal
    rigour: 2
---

# Multimedia Principle Improves Learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q3` · `i0`–`i2`

Presenting words and corresponding pictures together produces better learning than words alone, because learners can use both verbal and visual channels to build integrated mental representations.

## Subclaims

`q3 i2` Two direct experimental replications with German university students (n=48, n=47) find that learners score higher on a learning-outcomes test after studying text-with-pictures than text-alone, a medium-to-large effect on both occasions. [→ Seufert et al. 2025](#seufert-et-al-2025)

`q3 i0` An applied field test with real interrogation-rights material finds that once words are present (as on-screen caption or audio), adding an animated visual on top of them produces no further, reliably detectable comprehension gain over words alone — a boundary case for the principle in complex, multi-part legal content. [→ Lively et al. 2023](#lively-et-al-2023)

## Evidence

### Seufert et al. 2025

Seufert, T., Magner, U., & von Randow, J. (2025). Cucumber or grapes?—Context effects in multimedia learning. *Frontiers in Psychology, 16*, Article 1480935. [doi:10.3389/fpsyg.2025.1480935](https://doi.org/10.3389/fpsyg.2025.1480935)

`q3 · two independent lab experiments (2×2 between-subjects each), not pre-registered` · `i2 · medium-to-large effect, η²=.09–.14` · `n=48; n=47 German university students` · `causal · r2`

Two experiments (fictitious text about a chocolate factory, ~265 words) randomly assigned university students to read text-only or the same text with an accompanying illustration, then tested recall/application of the content. In Experiment 1 (N=48), the text-with-pictures group scored higher on the learning-outcomes test than the text-only group, F(1,44)=7.12, p=.01, η²=.14. In Experiment 2 (N=47), the effect replicated: F(1,43)=4.25, p<.05, η²=.09. The authors also found the same pattern (pictures beating text-alone) for situational interest and lower extraneous cognitive load, extending the classic learning-outcome finding to those measures.

### Lively et al. 2023

Lively, C. J., Snook, B., Luther, K., Mccardle, M. I., & House, J. C. (2023). A preliminary exploration of the multimedia principle's applicability for improving comprehension of youth interrogation rights. *Criminal Justice and Behavior, 50*(2), 252–271. [doi:10.1177/00938548221093283](https://doi.org/10.1177/00938548221093283)

`q3 · randomized 2 (Animation) × 2 (Audio) × 2 (Caption) between-subjects experiment, not pre-registered` · `i0 · negligible effect for animation on top of a text/audio channel; d=−0.07 [−0.62, 0.48] (caption alone vs. animation+caption)` · `n=207 adults (Experiment 1); n=193 youth aged 12–17 (Experiment 2)` · `causal · r2`

Adults (Experiment 1, N=207) and youth (Experiment 2, N=193) were each randomly shown one of eight presentations of youth interrogation rights, crossing whether an animation, an audio narration, and an on-screen caption (text) were present, then answered open-ended recall questions. Any condition that included words (caption and/or audio) produced far higher comprehension than a no-information baseline (d's around 2.0–2.9) or than animation-with-no-words (d=1.39–1.72). But the six word-containing conditions — including caption-only ("words alone") — scored about the same as each other: adding the animation to caption-only text produced no reliable gain (Cohen's d=−0.07, 95% CI [−0.62, 0.48] for Experiment 1; a comparable near-zero difference in Experiment 2). The authors explicitly note this departs from the multimedia principle's usual prediction that dual-channel (words+picture) presentations outperform single-channel ones. The abstract reports that in both experiments the animation-plus-caption presentation produced the highest comprehension; its advantage over caption alone was the small, unreliable difference above.

## Studies bearing on this claim

<!-- synthesis:start -->
*Do words with a relevant picture beat words alone?* This table gathers the studies behind this claim and the 8 narrower claims that bear on it: **15 distinct studies** (7 causal, 4 review, 2 theoretical, 1 quant-synthesis, 1 design), `q1`–`q4`, 6 of 15 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Seufert et al. 2025](https://doi.org/10.3389/fpsyg.2025.1480935) | q3 · causal · r2 | i2 · medium-to-large effect, η²=.09–.14 | this claim |
| [Lively et al. 2023](https://doi.org/10.1177/00938548221093283) | q3 · causal · r2 | i0 · negligible effect for animation on top of a text/audio channel; d=−0.07 [−0.62, 0.48] (caption alone vs. animation+caption) | this claim |
| Ceballos & Nutta 2022 | q2 · review · r2 | i? | [A practice article reports that the studies it cites found better post-test outcomes from ](multimedia-principle-words-and-pictures-outcomes.md) (supports) |
| [Hahn and Klein 2025](https://doi.org/10.3389/fpsyg.2025.1544764) | q2 · causal · r1 | i2 · medium effect, d=0.40 | [Multiple representations improve learning](multiple-representations-improve-learning.md) (supports) |
| [Rau 2017](https://doi.org/10.1007/s10648-016-9365-3) | q2 · review · r? | i? | [Multiple representations improve learning](multiple-representations-improve-learning.md) (supports) |
| [Richard E. Mayer 2008](https://doi.org/10.1037/0003-066x.63.8.760) | q3 · theoretical · r3 | i3 | [Generative processing principles: words with pictures and conversational-style words impro](generative-processing-principles-mayer-2008.md) (supports) |
| Alty 2002 | q3 · causal · r? | i? | [In one 37-student classroom experiment, recall and retention differ across media combinati](media-combinations-affect-recall-and-retention.md) (supports) |
| Kutbay 2020 | q2 · causal · r2 | i3 | [All ten multimedia treatment conditions produced significant pre-to-post achievement gains](all-treatments-produced-significant-gains.md) (supports) |
| [Guo et al. 2020](https://doi.org/10.1177/2332858420901696) | q4 · quant-synthesis · r2 | i1 · small-to-moderate effect, g=0.39 | [Adding relevant pictures or graphics to text improves learning from it, with a small poole](dual-coding-improves-learning.md) (supports) |
| [Carney and Levin 2002](https://doi.org/10.1023/a:1013176309260) | q2 · review · r? | i? | [Adding relevant pictures or graphics to text improves learning from it, with a small poole](dual-coding-improves-learning.md) (supports) |
| [Higdon et al. 2025](https://doi.org/10.1177/17470218241235520) | q3 · causal · r? | i? | [Adding relevant pictures or graphics to text improves learning from it, with a small poole](dual-coding-improves-learning.md) (supports) |
| [Siddhanth Sridhar 2026](https://doi.org/10.48550/arxiv.2609.14408) | q1 · design · r1 | i? | [Students and teachers responded positively to automatically generated textbook videos, fin](generated-textbook-videos-easier-to-follow-than-plain-text.md) (supports) |
| [Kalyuga et al. 2003](https://doi.org/10.1207/s15326985ep3801_4) | q2 · review · r2 | i? | [Instructional guidance that helps novices can become redundant or counterproductive as exp](expertise-reversal-effect.md) (qualifies) |
| [Kalyuga et al. 1998](https://doi.org/10.1518/001872098779480587) | q3 · causal · r? | i? | [Instructional guidance that helps novices can become redundant or counterproductive as exp](expertise-reversal-effect.md) (qualifies) |
| Obikwelu 2013 | q1 · theoretical · r2 | i? | [Instructional guidance that helps novices can become redundant or counterproductive as exp](expertise-reversal-effect.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

The multimedia principle is a cornerstone claim of Mayer's cognitive theory of multimedia learning, grounded in the assumption that working memory has separate visual and verbal processing channels and that coordinating both yields richer mental models than either channel alone. It sits within the broader framework of [Cognitive Load Theory](../theories/cognitive-load-theory.md) and is closely related to [Dual Coding Theory](../theories/dual-coding-theory.md), which likewise predicts a benefit from combining verbal and visual codes.

The effect is not unconditional. Adding pictures only helps when the pictures are relevant and meaningfully connected to the words; decorative or seductive visuals can impair learning, as captured by the claim that [irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) [~M]. When the combined presentation exceeds working memory capacity, [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) [-M], and the benefit of adding a second channel can disappear or reverse. The principle is therefore best understood as applying to explanatory visuals (illustrations, diagrams, animations) that support the verbal explanation, for learners who are novices in the domain [~S].

Boundary conditions worth noting for design practice:

- **Relevance.** The visual must carry explanatory weight. Illustrations that merely decorate text consume visual-channel capacity without contributing to the mental model, producing the coherence-principle violation above [~M].
- **Novice status.** Novices benefit most because they lack the prior knowledge needed to mentally generate a structure from words alone; the picture supplies that structure externally. For advanced learners, a supporting visual can be redundant with an already-formed mental model — a likely expertise-reversal pattern, where the benefit shrinks or reverses (see [Expertise Reversal Effect](../theories/expertise-reversal-effect.md)) [~S].
- **Capacity.** If words and pictures must be processed simultaneously and jointly exceed working memory capacity, integration fails and the second channel becomes a source of extraneous load rather than a resource [-M]. Presentation design (segmentation, pacing, placement) determines whether the combined message fits within capacity.

Open questions include how the effect scales with learner expertise, how it interacts with animation versus static images, pacing, and learner control, and whether the effect holds equally for complex, high-element-interactivity content. Specific studies establishing the effect and its boundary conditions still need to be added to the Evidence section.

*Merged from “Multimedia Learning More Effective With Words And Pictures” (multimedia-learning-more-effective-with-words-and-pictures):* This is Mayer's *multimedia principle*, the first and most robust of the principles derived from [Cognitive Load Theory](../theories/cognitive-load-theory.md) and [Dual Coding Theory](../theories/dual-coding-theory.md). The proposed mechanism is that visual and verbal channels are processed separately, so well-matched words and pictures allow learners to build both verbal and pictorial mental models and to make referential connections between them — something words alone cannot support.

The benefit is moderated by learner characteristics and design quality. Pictures must be *relevant* to the learning goal; decorative or seductive graphics can depress learning (see [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md)). Novices benefit most, because they lack the prior knowledge to generate their own internal visualizations; for advanced learners, added graphics may be redundant — an instance of the expertise reversal pattern described in [Expertise Reversal Effect](../theories/expertise-reversal-effect.md). Overloading either channel — e.g., dense text plus complex animation without segmentation — can produce overload rather than benefit, connecting to [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) and [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md).

Design implications follow directly: when explaining a process, structure, or spatial relationship, include a diagram, animation, or illustration that corresponds to the verbal explanation, and place words and pictures contiguously rather than on separate screens or pages. Static, well-labeled illustrations are often as effective as animation when pacing cannot be learner-controlled.

Open questions include how the principle extends to immersive and interactive media, and how it interacts with learner-controlled pacing.

*Merged from “People learn better from words and pictures than from words alone” (multimedia-principle):* The multimedia principle is one of the most consistently supported effects in Mayer's cognitive theory of multimedia learning, grounded in [dual coding](../theories/dual-coding-theory.md) and [cognitive load theory](../theories/cognitive-load-theory.md): verbal and pictorial channels each have limited capacity, and well-designed graphics let learners distribute processing across both [+S]. It is closely related to, but distinct from, the coherence principle — adding *relevant* graphics helps, while adding *irrelevant* graphics hurts (see [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md)).

Boundary conditions to keep in mind: the benefit is largest for novices, who lack mental models that words alone can activate [+M]; for experts, decorative or redundant graphics can impose extraneous load — an instance of the [expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Graphics must also be *relevant and explanatory* — decorative illustrations that do not support the explanation should be expected to produce no benefit or a penalty, consistent with the coherence principle [~S]. Static illustrations are generally sufficient; animation adds value mainly when the content depicts movement or processes over time [~M].

The evidence recorded above qualifies the claim: in one applied study, once words were present, adding an animation gave no reliable further gain.

*Merged from “Multimedia Words Plus Images Beat Words Alone” (multimedia-words-plus-images-beat-words-alone):* **Mechanism.** The effect is typically explained by dual coding: presenting information in both verbal and visual channels allows parallel processing and richer memory encoding, provided the two representations refer to the same content. Well-designed visuals can also reduce extraneous load by making spatial or relational structure explicit, consistent with [Cognitive Load Reduction](../principles/cognitive-load-management.md).

**Boundary conditions.** The multimedia effect is not unconditional. Irrelevant or decorative images can impair learning [-M] — see [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md). The benefit is strongest when the image is referentially relevant, presented contiguously with the words, and matched to the learner's prior knowledge [~M]; for high-knowledge learners, redundant pictures may add load without benefit (an expertise-reversal pattern, cf. [Expertise Reversal Effect](../theories/expertise-reversal-effect.md)) [-M]. Simple recall of verbal facts may also show little benefit, since the effect is most reliable for relational or explanatory understanding [~M].

**Design implications.** Practitioners should select visuals that depict the same referential content as the words (not decoration), place them adjacent to the corresponding text or narration, and prefer explanatory graphics (diagrams, animations of processes) over representational stock imagery. Where the verbal channel is already sufficient — e.g., rote verbal facts or highly experienced learners — adding pictures offers little gain and may impose [cognitive overload](../claims/cognitive-overload-degrades-learning.md).

**Open questions.** Much of the supporting literature comes from short, lab-style lessons in science and technical domains; effect sizes in authentic classroom settings and with complex, extended curricula are less well established [~W].

*Merged from “Words and pictures are better than words alone” (words-and-pictures-better-than-words-alone):* The claim is a cornerstone of multimedia learning theory and is closely tied to [Dual Coding Theory](../theories/dual-coding-theory.md): verbal and pictorial information are processed in partly separate channels, so presenting both gives learners two coordinated routes into the same content. It also connects to [Cognitive Load Theory](../theories/cognitive-load-theory.md) — a well-designed picture can offload working memory that would otherwise be spent constructing a mental image from verbal description alone.

Important boundary conditions follow from this framing. The picture must be *relevant* and *integral* to the explanation; decorative or tangential images add extraneous load rather than support, as captured by the [coherence principle](coherence-principle-irrelevant-material-hurts-learning.md) [-M]. The benefit is also strongest for novices, who lack the prior knowledge to generate their own mental imagery from text; experts may find accompanying pictures redundant — the same expertise-reversal pattern documented for [worked examples](../theories/expertise-reversal-effect.md) [~M]. Finally, when words and pictures are presented in ways that force split attention (e.g., a diagram separated from its labels), the advantage can disappear or reverse — see [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) [-M].

Design implications: prefer illustrations that depict the causal or structural relations described in the text (not merely decorative icons); place words physically near the corresponding picture elements; and for complex dynamic content, consider whether a static diagram with learner-controlled pacing outperforms continuous animation [~W].

Open questions include how the effect scales across media formats (static illustrations vs. animation) and how it interacts with learner-controlled pacing. Evidence entries establishing the effect's strength and scope still need to be added.

## Related Claims

- [Coherence principle: irrelevant material hurts learning](coherence-principle-irrelevant-material-hurts-learning.md) — pictures must be relevant; decorative visuals undermine the multimedia benefit
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — overload is the boundary condition where adding a channel stops helping
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical framework in which the multimedia principle is situated
- [Dual Coding Theory](../theories/dual-coding-theory.md) — the complementary account of why verbal and visual codes combine productively
- [Expertise Reversal Effect](../theories/expertise-reversal-effect.md) — supporting visuals may become redundant for advanced learners
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — segmentation manages the capacity limits that multimedia design must respect
- [Advance organizers improve learning](advance-organizers-improve-learning.md) — another way of supporting mental model construction before or during instruction
- [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — the broader family of effects the multimedia principle belongs to
- [Cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) — the overload condition the multimedia principle is designed to avoid
- [Analogical reasoning improves transfer](comparing-contrasting-cases-improves-learning.md) — pictures often carry the analogical structure that supports transfer from words
- [Split Attention Effect Degrades Learning](split-attention-effect-degrades-learning.md) — related
- [Hispanic adults valued culturally relevant visual design — bright colors, Hispanic representation, and realistic imagery — in lung cancer screening educational materials](culturally-relevant-visual-design-lcs-materials.md) — a narrower finding that bears on this claim
- [Decorative Illustrations Do Not Improve Learning](seductive-details-effect.md) — related
- [Adding relevant pictures or graphics to text improves learning from it, with a small pooled effect on reading comprehension, though whether dual coding explains the benefit is disputed](dual-coding-improves-learning.md) — a narrower finding that bears on this claim
- [In one 37-student classroom experiment, recall and retention differ across media combinations in the direction Dual Coding Theory predicts](media-combinations-affect-recall-and-retention.md) — a broader claim this one bears on
- [MLM-script presentations fall between the other two groups: above the Textbook group but below the MLM group, as multimedia learning theory predicts](mlm-script-intermediate-between-mlm-and-textbook.md) — a narrower finding that bears on this claim
- [Cognitive Load Management](cognitive-load-management.md) — related
- [Redundancy Effect Impairs Learning](redundancy-principle.md) — related
- [Multiple representations improve learning](multiple-representations-improve-learning.md) — a narrower finding that bears on this claim
- [Combining textual and pictorial glosses improves incidental vocabulary learning more than single-mode glosses](multimodal-glosses-improve-incidental-vocabulary-learning.md) — a narrower finding that bears on this claim
- [Four of six activity groups are rated better in multimedia format, but quizzes and picture descriptions are rated equally across formats](activity-format-moderates-motivational-ratings.md) — related
- [A practice article reports that the studies it cites found better post-test outcomes from words with relevant pictures than from words alone, especially with spoken words](multimedia-principle-words-and-pictures-outcomes.md) — related
- [Dual coding elucidation raises adolescent EFL learners' awareness of lexical errors and correct usage more than verbal-only elucidation](dual-coding-elucidation-improves-lexical-error-awareness.md) — a narrower finding that bears on this claim
- [A WestEd research bulletin reports a curriculum revision that replaced a decorative photograph in a math problem with a problem-relevant sketch, on the developers' view that such photographs distract students](decorative-images-distract-from-math-problems.md) — related
- [Multiple representations and explanations of math concepts aid student understanding, but faculty lack time to source or develop them](multiple-representations-aid-understanding-faculty-time.md) — a broader claim this one bears on
- [Participants valued multimodal experiences combining visualization with hands-on interaction, while reporting challenges with complex or unclear visualizations](multimodal-valued-complex-visualizations-hinder.md) — related
- [Contiguity principles: near placement and simultaneous presentation of corresponding words and pictures improve transfer](contiguity-principles-mayer-2008.md) — related
- [Modality effect: presenting explanatory text in spoken rather than written form with visual information increases effective working memory capacity and learning](modality-effect-narration-over-text.md) — related
- [Dual-mode (auditory plus visual) presentation of worked examples enhances subsequent problem-solving efficiency, except under high visual-search conditions without attention cues](dual-mode-worked-example-presentation.md) — related
- [Concreteness, imagery, and verbal associative processes play major roles across multiple educational domains](concreteness-imagery-associative-roles-educational-domains.md) — a broader claim this one bears on
- [Basic DCT mechanisms can be used to model diverse educational phenomena](dct-mechanisms-model-educational-phenomena.md) — a broader claim this one bears on
- [Sketching and viewing animations produced the best understanding of a geoscience text, while the photograph condition produced the worst](sketching-animation-best-understanding-photograph-worst.md) — related
- [Media-rich videos combining text, pictures and voiceovers are rated more engaging than text-only videos](media-rich-videos-more-engaging-than-text-only.md) — related
- [Multimedia learning principles are not clearly attributable to the multicomponent model or to applied multimedia theories](multimedia-principles-not-attributable-to-multicomponent-model.md) — related
