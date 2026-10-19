---
type: principle
id: multimedia-learning
aliases: [visual-representations-benefit-only-with-adequate-processing-resources]
title: Multimedia Learning
description: "For a learner without a working model of a structure or process, a relevant picture placed with the words that explain it may improve a learning test over words alone, qualified by redundancy, decorative additions, pacing, prior knowledge and assessment horizon."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
sources:
  - id: fiorella-2015
    resource: "https://doi.org/10.1017/CBO9781107707085"
    title: "Fiorella, L., & Mayer, R. E. (2015). *Learning as a generative activity*. Cambridge University Press"
    author: "Fiorella, L., & Mayer, R. E"
  - id: clinton-2016
    resource: "https://doi.org/10.1080/00220973.2015.1048847"
    title: "Clinton, V., Alibali, M. W., & Nathan, M. J. (2016). Learning About Posterior Probability: Do Diagrams and Elaborative Interrogation Help? The Journal of Experimental Education, 84(3), 579-599. https://doi.org/10.1080/00220973.2015.1048847"
    author: "Clinton, V., Alibali, M. W., & Nathan, M. J"
---

# Multimedia Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 55 claims (22 for, 30 mixed, 3 against) · 46 studies (23 causal, 11 quant-synthesis, 7 review, 2 associational, 1 qualitative, 1 design, 1 theoretical), `q1`–`q4` · 16 of 46 report an effect size · 47 claims rest on one study

## Conditional relationship

For a learner who cannot yet describe the structure, process or spatial relation an explanation is about (a `novice` on that task, whatever their wider experience), studying the words together with a relevant picture that depicts what the words describe may produce a better learning test than studying the words alone. The relationship is bounded by what the picture carries, where it sits relative to the words, whether the same words arrive twice through competing channels, whether the presentation is system-paced or learner-paced, what the learner is asked to do while studying, the learner's prior knowledge of this content, and the outcome and horizon being assessed. An image added without a job can change nothing: two recorded experiments found no gain from an added image or graph. The evidence below is mostly from short `lab` lessons with `adult` (`postsecondary`) learners on `principle`-type knowledge (how something works), assessed soon after study; it does not establish delayed retention, transfer to use, or benefit for every kind of content. The [pattern](../patterns/multimedia-learning.md) specifies a reusable design policy; its local diagnostic branches remain proposals.

## Default design, while the dose is untested

No claim in the wiki sets how long a segment should run, how many pictures a lesson needs, or when to withdraw support. The steps follow a claim where one is named and are **labelled proposals** elsewhere; the [pattern](../patterns/multimedia-learning.md) gives the full sequence and observation policy, and the [modality principle](modality.md) the narration steps.

1. **Give the picture a job.** Use a single static diagram for how parts are arranged and an animation for how they move or change; for a list of verbal facts, a picture may add nothing. Basis: the animation-or-static row below.
2. **Configure it.** Write labels into the picture at the part they name; narrate a system-paced explanation and keep printed words beside the picture on learner-paced pages; leave out images unrelated to the content. Basis: the placement, modality and coherence rows below.
3. **Dose (proposal).** Segments of one to three minutes of narration, or one diagram with its paragraph, each followed by a pause or "next" and one "what happens if this part changes" question about the picture. No claim sets the length.
4. **Leave time to study the picture with the words.** In one experiment the diagram helped only when learners read the lesson twice, not when they answered questions while reading ([diagrams helped only in the read-twice condition](../claims/diagrams-help-posttest-only-read-twice-condition.md) [~M]).
5. **Across sessions, withdraw support as the learner explains unaided (proposal).** Early sessions: name the parts first, short segments, explicit cues on when to pause and replay. Once a learner answers a new changed-condition question correctly without supports on two occasions, lengthen the segments, drop the pretraining, and move to application tasks, without the picture if the target requires it. Basis for the direction: [segmentation helps less as prior knowledge grows](../claims/segmentation-benefits-shrink-with-expertise.md) [~M]; the criterion and the number of sessions are untested.
6. **Judge it on the brief's own test and horizon**, preferably an explanation or transfer item rather than recall of the words.

## Fitting the design to a situation

Three facts change the decision most. Ask for them when the brief omits them: **does the picture depict what the words explain** (a process, a structure, a spatial relation), or only decorate it; **who controls the pace** (system-paced video or narration, or learner-paced pages and pauses); and **how much the learners already know about this content**. Most rows below rest on Mayer (2008), a review that summarises a series of short lab experiments, largely from one research group, with transfer tested soon after study; read its median effect sizes as that programme's results, not as independent replications.

| If the brief says… | Then change… | Basis |
|---|---|---|
| The lesson explains a process or system, and learners are `novice` on it | Add a picture that depicts the process or structure the words describe; keep it to the parts the words name, and say what job it does, since an image added without one may change nothing | [Words with pictures against words alone](../claims/multimedia-principle-improves-learning.md) [+M] (two lab experiments, immediate test); [words with corresponding graphics beat words alone on transfer](../claims/generative-processing-principles-mayer-2008.md) [+M] (Mayer's programme, 11 of 11 comparisons, median d = 1.39). Against: [an instructional image added to biology texts changed neither test scores nor monitoring accuracy](../claims/instructional-visuals-no-effect-test-performance-or-test-explain-accuracy.md) [-M] (163 and 48 undergraduates online, d = 0.01 and 0.06), and [graphs did not improve vector-calculus problem solving](../claims/no-overall-multimedia-effect-vector-calculus.md) [-M] (36 engineering-physics students, 56% against 52% correct) |
| Learners will answer questions while reading the illustrated text, or will read it only once | Leave time to study the diagram with the text (a second reading); do not expect the diagram to add on its own while attention goes to the questions | [Diagrams helped only when students read the lesson twice, not when they answered questions while reading](../claims/diagrams-help-posttest-only-read-twice-condition.md) [~M] (198 undergraduates, posterior probability lesson, no effect size printed) |
| The choice is between a static picture and an animation | Choose by what the learner must identify: an animation for how parts move or change, a single static picture for how they are arranged (not a strip of snapshots); expect a small average advantage for animation, and none when the changes shown are not what is to be learned | [Animation beat static pictures for identifying motions](../claims/animation-beats-static-pictures-for-identifying-motions.md) [+M] (88 pre-service teachers, d = 2.33 and 2.41) and [a single picture beat animation for arrangements](../claims/single-picture-beats-animation-for-spatial-arrangements.md) [~M] (d = 1.30); [animation's small overall advantage](../claims/animation-small-overall-advantage-over-static-graphics.md) [~M] (61 studies, g = 0.23); [a re-analysis found the advantage only when features of the change were relevant](../claims/reanalysis-features-of-change-moderator.md) [~M] (g = 0.34 and 0.65 against 0.04, reported second-hand). See the pattern's row for pacing and commentary |
| The picture on offer is a photograph or a realistic rendering | Prefer a diagram or animation that shows the process, or ask learners to sketch it; how realistic an animation looks mattered less than whether it showed the process | [Sketching and animation gave the best understanding of a geoscience text, a photograph the worst](../claims/sketching-animation-best-understanding-photograph-worst.md) [~M] (120 undergraduates, six conditions, ηp² = .19 for condition); [abstract and concrete animations did not differ](../claims/abstract-concrete-representation-no-difference.md) [~M] (a middle-school electricity quasi-experiment; not an equivalence test) |
| Words and the picture they describe are on different parts of the screen or page, or arrive at different times | Put each label or sentence next to the part of the picture it refers to, and present narration at the same time as the matching animation | [Spatially integrating text and diagrams](../claims/split-attention-effect-degrades-learning.md) [+M] (meta-analysis, g = 0.63); [Contiguity principles](../claims/contiguity-principles-mayer-2008.md) [+M] (Mayer's programme, effect size 1.12) |
| The lesson carries interesting but unneeded material (stories, background music, decorative images, extra facts) | Cut it, and keep only what the explanation needs; replace a decorative photograph with a sketch of what the problem is about. A decorative picture thematically related to the topic need not be cut, but do not count on it for transfer | [Coherence principle](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+M] (13 of 14 experiments, median d = 0.97); [Interesting but irrelevant additions](../claims/seductive-details-effect.md) [~M] (harm depends on image type and on learners' prior knowledge); a curriculum revision [replaced a decorative photograph in a math problem with a problem-relevant sketch](../claims/decorative-images-distract-from-math-problems.md) [+W] (the developers' view, no data). Qualified by Scherer et al.: [related decorative pictures raised knowledge scores](../claims/related-decorative-pictures-improve-knowledge-exp1.md) [~M] (71 teacher-education students, ηp² = .075) and [eighth-graders' monitoring accuracy on knowledge items](../claims/related-pictures-improve-metacognitive-monitoring-exp2.md) [~M], but [not transfer in either experiment](../claims/related-decorative-pictures-no-transfer-effect.md) [~M] |
| An animation or diagram is explained by narration, and on-screen text repeats the narration word for word | Drop the duplicated on-screen text, or keep only key terms | [Redundancy principle](../claims/redundancy-principle-mayer-2008.md) [+M] (5 of 5 experiments, median d = 0.72); qualified by [Duplicated words](../claims/redundancy-hurts-learning.md) [~S] (with no picture, or for low prior knowledge learners at the system's pace, spoken plus written did not hurt). Where the duplicate is already there, removing it is a small change, not a rescue: [adding written text to narration made no significant difference with abstract or concrete animation](../claims/redundancy-effect-not-significant-middle-school.md) [~M] (middle-school classroom quasi-experiment), [redundant text inside a diagram did not affect posttest accuracy](../claims/redundant-text-no-effect-posterior-probability-lesson.md) [~M] (198 undergraduates, learner-paced), and [the overall spoken–written effect is small and varies widely](../claims/verbal-redundancy-small-overall-effect.md) [~M] (g = 0.15, I² = .82); none of these is an equivalence test |
| No picture or animation, the presentation is system-paced, and learners may miss spoken words | Give the words both spoken and written (key terms if not the full text); the spoken–written advantage disappears once a picture is added and is larger for unsegmented presentations | [With images or animation, spoken–written was no better than spoken-only](../claims/images-animation-eliminate-redundancy-benefit.md) [~M] (g = 0.06, against 0.45 and 0.24 without); [the advantage held for system-paced, not learner-paced, material](../claims/system-paced-moderates-verbal-redundancy.md) [~M] (g = 0.34 against 0.12); [larger for unsegmented presentations](../claims/segmentation-moderates-verbal-redundancy.md) [~M] (g = 0.53 against 0.15); all moderator analyses in Adesope and Nesbit's meta-analysis. See also the pattern's row for second-language and less fluent readers |
| Words accompany a diagram or animation, and the words could be spoken | Speak them rather than print them, when learners can follow spoken language at that pace | [Modality principle](../claims/modality-principle-mayer-2008.md) [+M] (17 of 17 experiments, median d = 1.02); [Modality effect](../claims/modality-effect-narration-over-text.md) [+W] (Sweller and colleagues' review); [animation or picture with voice beat picture with text](../claims/voice-media-outperform-picture-text-overall.md) [+M] (36 adults, 15-minute immunology lesson, p = .004, no effect size printed) |
| Learners are reading in a second language, are deaf or hard of hearing, or study where they cannot listen | Keep printed words, placed next to the picture, signal the key words in them, and give learner control of pace | In one middle-school quasi-experiment, [spoken text did not differ reliably from signaled written text](../claims/spoken-versus-signaled-written-null.md) [~M] with abstract or concrete animation (not an equivalence test, and not with these learners); the rest is untested, since the modality evidence assumes learners can follow the spoken words |
| The lesson is a long continuous video or narrated animation | Break it into meaningful segments, with a pause or "next" between them; expect learners to take longer | [Segmenting improves retention and transfer](../claims/segmenting-improves-multimedia-learning.md) [+M] (56 investigations, small-to-medium effects); [learner-paced segments beat continuous presentation on transfer](../claims/segmenting-principle-mayer-2008.md) [+M] (Mayer's programme, 3 of 3 experiments with a "continue" button, median d = 0.98); [Segmentation increases learning time](../claims/segmenting-increases-learning-time.md) [~M]; [the effects hold for system-paced segmentation too](../claims/segmenting-effects-confirmed-system-paced.md) [+M] |
| Learners have high prior knowledge of the content | Segmenting may still help their retention; drop pretraining and extra signals they do not need, and check transfer, not only effort | [High prior knowledge learners benefited more from segmenting for retention](../claims/prior-knowledge-moderates-segmenting-retention.md) [~M] (meta-analysis); this runs against [Segmenting and prior knowledge](../claims/segmentation-benefits-shrink-with-expertise.md) [~M] (one experiment: efficiency gain only for lower prior knowledge), so record prior knowledge and outcome type before deciding. In a middle-school electricity quasi-experiment, [prior science level and pretest raised achievement but did not interact with the multimedia configuration](../claims/treatment-science-pretest-independent-effects.md) [~M]; a nonsignificant interaction does not show the configurations work equally at every level |
| The lesson uses technical parts or terms learners have not met | Before the main lesson, give a short primer naming the key parts and what each does | [Pretraining principle](../claims/pretraining-principle-mayer-2008.md) [+M] (5 of 5 experiments, median d = 0.85) |
| The essential points are easy to miss in a busy display or long text | Signal them: headings, an outline, highlighting or spoken emphasis on the essential words, and nothing else highlighted | [Signaling principle](../claims/signaling-principle-mayer-2008.md) [+M] (6 of 6 experiments, median d = 0.52); a review reports [the effect extends from animations to video](../claims/signaling-improves-retention-transfer-video.md) [+W] (second-hand, no effect sizes); in a middle-school quasi-experiment, [signaling written text helped with abstract animation only](../claims/signaling-effect-abstract-only.md) [~M] (d = .35; not significant with concrete animation) |
| `online-self-paced`, no teacher present | Give learners pause and replay control, segment the material, and place a short check after each segment | untested proposal for the check; segmenting evidence above |
| A digital storybook for young children | Keep animated illustrations, sound and music that match the story; leave out hotspots, games and other interactive features | [Multimedia-only stories helped comprehension; stories that also had interactive features did not](../claims/multimedia-only-benefits-interactive-features-detrimental.md) [+M] (meta-analysis, g+ = 0.39 against −0.14). The gain was larger in studies of children the authors classed as disadvantaged (g+ = 0.66): a difference reflecting circumstances, not a property of the children or a cause |
| The test that matters is transfer, or delayed, or use on a real task | Judge the configuration on a transfer item, not a retention or multiple-choice test; do not rely on these effects to carry to a delayed test or real use | [Spoken–written advantages were large for retention and absent for transfer](../claims/outcome-constructs-test-formats-moderate-redundancy.md) [~M] (g = 0.53 against 0.01; multiple-choice 0.63 against mixed 0.11); the delayed and real-use cases are untested, since the evidence above is mostly immediate tests |

## Observation, state and explanation

Record what the learner did with the material **under stated conditions**: which representation they had, whether they could pause, replay or re-read, how words and picture were placed, and what they were asked to do afterwards. Recalling a sentence, labelling a diagram, explaining how one part acts on another, and predicting what happens when something changes are different performances. "Visual learner" or "low attention" are not observations, and a learner's stated preference for a format does not show which format helps them learn.

Building an integrated model of words and picture, extraneous load from search or duplication, and attention drawn away by decoration are explanatory hypotheses. Test scores, reported effort, time on a screen and where a learner looked are observations; none directly measures the model. Lower reported effort could reflect easier processing or disengagement.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Recalls the words but cannot explain how the parts relate | No integrated model built; the picture did not show the relation; the test asked for recall and the learner answered at that level | Ask for a prediction or a "what if this part changed" explanation with the picture available and then withdrawn; compare a version where the picture depicts the causal relation with one where it only shows the object. |
| Describes the picture but not the explanation's key steps | Attention went to the visual and the words were not processed; the words were too fast to follow (system-paced narration); language access to the words is limited | Offer the same words as re-readable text or with pause control and the same picture; check comprehension of the words alone in an accessible form. |
| Reports high effort and does no better with the picture than without | Picture and words are placed apart, forcing search; the same words appear as narration and on-screen text over a visualization; the content is too much for one unsegmented pass | Re-present one segment with labels placed on the picture and no duplicated text, or with learner-controlled pauses, and compare effort and the explanation produced. Vary one feature at a time. |
| Does well with or without the picture | The learner already has the model (prior knowledge); the test is too easy or close to the words; the picture adds nothing for this content | Give a harder changed-condition question before deciding; record prior knowledge of this content. For a learner who already knows it, extra support may be unnecessary or a cost. |
| Engages more with an illustrated version but learns no more | Decorative or interesting-but-irrelevant images raise mood or interest without informing; they may also draw attention from the informative picture; the image raised the learner's confidence rather than their understanding | Remove the decorative image and keep the informative one; compare explanation quality, not liking. Ask the learner to judge their understanding and then explain: with an image, undergraduates [rated their ability to draw the process higher with no better test score](../claims/image-condition-inflated-draw-judgment-magnitude.md) [~M] (d = 0.32), so a confident judgment beside a picture is not evidence of learning. |

These are proposals and have not been tested with learners as diagnostic branches. A single contrast does not identify a cause, and probing can itself change what the learner knows. Match demands across versions, repeat where feasible, and record what remains unresolved.

## Evidence and qualifications

- [Words with pictures against words alone](../claims/multimedia-principle-improves-learning.md) [+M]: two randomized lab experiments (`randomized`, n=48 and n=47 German university students) found a text-with-picture group scored higher on a learning-outcomes test than a text-only group, η²=.14 and .09 as printed on the claim page; the timing of the test is not reported there. The same page records a randomized 2×2×2 experiment on youth interrogation rights (adults n=207; youth aged 12–17 n=193) in which, once words were present, adding an animation gave no reliable further comprehension gain (d=−0.07, 95% CI [−0.62, 0.48] for adults). That second entry is not settled against its abstract; read the page before relying on either direction. Neither study predicts delayed retention or transfer, and a non-significant difference is not equivalence.
- [Spatially integrating text and diagrams](../claims/split-attention-effect-degrades-learning.md) [+M]: a random-effects meta-analysis of 58 comparisons (n=2426) found integrated placement of mutually referring text and diagrams beat separated placement, g=0.63 as printed. Learners, outcomes and horizons are not broken down on the page; the benefit is reported as holding across the moderators examined. Not yet checked against its source. It supports placement, not the decision to add a picture.
- [Duplicated words](../claims/redundancy-hurts-learning.md) [~S]: an experiment found removing text that duplicated narration improved learning from a diagram lesson (no effect size recorded), while a meta-analysis of 57 studies, mostly with postsecondary students, found spoken–written presentations did not differ from written-only ones and *outperformed* spoken-only ones, for low prior knowledge learners, system-paced material and picture-free material; key-term text beat verbatim text. Checked by the judge on the abstract. It qualifies a blanket "never duplicate" rule: the harm is recorded where text competes with a visualization, not for words alone.
- [Interesting but irrelevant additions](../claims/seductive-details-effect.md) [~M]: a meta-analysis (abstract only) found seductive details can hinder learning depending on image type, delivery format and other features; three experiments with 7th and 8th graders found decorative pictures neither helped nor harmed overall but weakened the benefit of instructional pictures, most for lower prior knowledge; a within-subjects e-learning study found a small cost (η²=.04) and, in a harder follow-up, harm only for students with low attentional inhibition. Not settled against its sources. It limits "add a picture" to pictures that inform.
- [Segmenting and prior knowledge](../claims/segmentation-benefits-shrink-with-expertise.md) [~M]: a randomized experiment with 75 Dutch secondary students studying narrated animated worked examples in probability found segmented examples more efficient (equal transfer, lower effort) for lower prior knowledge, with the advantage gone at higher prior knowledge; no interaction on transfer performance alone, and no effect size beyond regression coefficients. Not yet checked against its source. It is one study of one support, not a general expertise-reversal estimate for pictures.
- [Diagrams helped only in the read-twice condition](../claims/diagrams-help-posttest-only-read-twice-condition.md) [~M]: a randomized factorial experiment (N = 198 undergraduates, a posterior probability lesson) found a diagram × questioning interaction: with diagrams, students who read the lesson twice did better on the posttest than without, while those answering elaborative questions as they read gained nothing from the diagram. No effect size is printed (B = 3.11 in a mixed-effects model). In the same study [text duplicated inside the diagram](../claims/redundant-text-no-effect-posterior-probability-lesson.md) [~M] made no difference. It bounds the relationship by what else the learner is asked to do while studying.
- [Instructional images and test scores](../claims/instructional-visuals-no-effect-test-performance-or-test-explain-accuracy.md) [-M]: Jaeger and Fiorella's online experiments (163 and 48 undergraduates, biology texts) found adding an instructional image did not change test performance (d = 0.01, 0.06) or the accuracy of learners' judgments of their understanding; with the image, [judgments of being able to draw the process were higher](../claims/image-condition-inflated-draw-judgment-magnitude.md) [~M] (d = 0.32). With [graphs added to vector-calculus problems](../claims/no-overall-multimedia-effect-vector-calculus.md) [-M], 36 engineering-physics students did not answer more correctly (56% against 52%). These are the recorded cases against the default; both used pictures whose job relative to the test is not stated on the claim pages.
- [Related decorative pictures](../claims/related-decorative-pictures-improve-knowledge-exp1.md) [~M]: in Scherer et al.'s two randomized experiments, pictures related to the topic but carrying no needed information raised knowledge scores for university students (ηp² = .075) and [monitoring accuracy on knowledge items for eighth-graders](../claims/related-pictures-improve-metacognitive-monitoring-exp2.md) [~M], with [no effect on transfer in either](../claims/related-decorative-pictures-no-transfer-effect.md) [~M]. It narrows the coherence rule: the harm is recorded for irrelevant additions, not for every picture without an explanatory job.

Retain learners, assignment, materials, pacing, comparator, instrument and horizon when transporting these observations. Do not rank them by effect label: an η² from a two-group lab study, a pooled g from a meta-analysis and a regression β answer different questions.

## The evidence by question

Each question below links a general claim that gathers the studies behind it into one table, one row per distinct study, with each study's design and effect as recorded and no averaged verdict (`eval/synthesis/multimedia-learning.json`, `scripts/synthesize_claim.py`). The count is of distinct studies across the claim and the narrower claims that bear on it.

- Do words with a relevant picture beat words alone? [Multimedia Principle Improves Learning](../claims/multimedia-principle-improves-learning.md) [+S]: 8 distinct studies.
- How much do the design principles add, and when do they matter most? [Multimedia design principles improve learning by g = 0.38 on average across the 11 largest reviews, an effect the authors call moderate, with large differences between principles](../claims/multimedia-design-principles-improve-learning-overall.md) [~M]: 2 distinct studies.
- Should words sit next to, and arrive with, the picture they describe? [Split Attention Effect Degrades Learning](../claims/split-attention-effect-degrades-learning.md) [+M]: 5 distinct studies.
- Should the words be spoken or printed? [Presenting words as spoken narration rather than on-screen text alongside graphics improves learning](../claims/modality-effect-narration-over-text.md) [~S]: 7 distinct studies.
- Does presenting the same words twice (spoken and written) hurt or help, and for whom? [On-screen text that duplicates the narration of a diagram can hurt learning, but spoken–written redundancy is not harmful on average and helps over spoken-only presentation in some conditions](../claims/redundancy-hurts-learning.md) [~S]: 7 distinct studies.
- Should interesting but unneeded material be cut? [Coherence Principle Irrelevant Material Hurts Learning](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [+S]: 10 distinct studies.
- Should continuous presentations be segmented, and does learner control of pace help? [Segmenting multimedia instruction into learner-paced segments improves retention and transfer performance with small-to-medium effects](../claims/segmenting-improves-multimedia-learning.md) [+M]: 4 distinct studies.
- Animation or a static picture? [Animation beats static pictures for identifying motions](../claims/animation-beats-static-pictures-for-identifying-motions.md) [+M] against [a single picture beats animation for spatial arrangements](../claims/single-picture-beats-animation-for-spatial-arrangements.md) [~M] (one experiment), with [a small overall animation advantage](../claims/animation-small-overall-advantage-over-static-graphics.md) [~M] (one meta-analysis). Not yet gathered into a synthesis table.
- Does an added picture help when it has no stated job? [Instructional visuals did not affect test performance](../claims/instructional-visuals-no-effect-test-performance-or-test-explain-accuracy.md) [-M] and [related decorative pictures did not affect transfer](../claims/related-decorative-pictures-no-transfer-effect.md) [~M]: two studies, not yet gathered into a synthesis table.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision). Reread 2026-10-19 (wave 2): of the 38 bullets then here and in a linker-added "## Claims" section, 29 claims were worked into the model above (the default design, situation rows, the observation table, the evidence and qualifications, the evidence-by-question list); the nine below stay with a note. -->
Claims linked to this page later go here until they are read against the model. Read on 2026-10-19 and left here because they do not change it:

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — read 2026-10-19: reviews and list-recall experiments on working-memory capacity; no words-and-pictures comparison, so it is background for the load explanations, not a test of them.
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M] — read 2026-10-19: worked examples against problem solving in algebra; not a test of adding or placing a picture (see the [worked examples principle](worked-examples.md)).
- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — read 2026-10-19: prompts to explain while studying text, examples or problems (g = .55); none of its entries prompts learners to explain how a picture and its words relate, so the pattern's prompt to do so stays a proposal.
- [Related prior knowledge is the single most powerful influence mediating subsequent learning, so multimedia should layer information by complexity](../claims/prior-knowledge-most-powerful-influence-multimedia-layering.md) [+W] — read 2026-10-19: a 1993 review's assertion from schema theory, no comparison; the prior-knowledge row rests on the experiments and meta-analysis cited there.
- [The voluntary/involuntary attention distinction in the embedded-processes model maps onto signaling, coherence, and split-attention principles](../claims/voluntary-involuntary-attention-distinction-explains-multimedia-principles.md) [+W] — read 2026-10-19: a theoretical mapping with no data; one more explanatory hypothesis of the kind the observation section lists, not an observation.
- [A dynamic geometry model of the quilt problem helped an informal educator understand its spatial relations](../claims/geometry-software-model-helped-informal-educator-understand-spatial-relations.md) [~W] — read 2026-10-19: one participant's own report in a narrative inquiry; no comparison or learning measure.
- [Students answered questions requiring coordination of two or more representations less accurately than questions answerable from a single representation](../claims/coordination-of-two-representations-correctless.md) [-W] — read 2026-10-19: ten chemistry students with linked multiple representations; multiple representations are scoped out of this page and the pattern.
- [Adding theory annotations to a video model yields no additional skill benefit over the same unannotated model](../claims/theory-annotation-no-extra-skill-benefit.md) [~W] — read 2026-10-19: a pre-registered trial of video modelling of a teaching skill (58 trainees); video modelling is scoped out, though the null for added explanatory text is consistent with the coherence row.
- [Matching modality by conveying complementary information through auditory and visual channels increases retention, transfer, and engagement](../claims/modality-matching-complementary-channels-video.md) [+W] — read 2026-10-19: a practice essay reporting Mayer and Moreno second-hand; the modality and picture rows rest on the primary claims.

## Objective and learner-valued goal

Ask what the learner wants to be able to do with the material and why, separately from the designer's objective. Agreement, divergence and uncertainty are observations; do not infer that a learner values understanding because they watched to the end, or that they prefer video because they clicked it. Choose a representative task, criterion, permitted aids (can the diagram be consulted at test?) and horizon. Recalling the explanation, explaining a mechanism, troubleshooting a real device and passing a recognition quiz require different evidence.

For example, an apprentice may want to find out why a pump in their own workplace keeps failing, while the designer's objective is a module quiz on the pump cycle's stages. An immediate stage-naming quiz cannot show whether the apprentice can reason about a fault. The pattern shows how to keep both aims and test the capability that matters.

## What would revise this model?

The bounded words-with-pictures expectation should weaken if comparable learners and aligned outcomes show no advantage of informative, integrated pictures over words alone under defensible comparisons, or if the advantage seen on an immediate test is absent at a delayed one. If placement, pacing or language access explain a learner's difficulty better than the presence of a picture, revise the local interpretation rather than adding media. If duplicated text helps the learners in front of you (for example where words alone are hard to follow), keep that observation rather than deleting text by rule. Do not protect the model by relabelling every failure as a decorative picture or low prior knowledge after the fact.

A learning-phase preference, immediate recall, explanation of a mechanism, delayed retention and use on a real task are separate claims. The present evidence does not establish a universal best format, an optimal segment length, or a forecast for an individual learner.

## Related Principles
- [Modality Principle](modality.md)
- [Segmenting Principle](segmenting.md)
- [Signaling Principle](signaling.md)
- [Contiguity Principle (Spatial and Temporal)](contiguity.md)
- [Coherence Principle](coherence.md)
- [Pre-training Principle](pretraining.md)

- [Multimodal Instruction](multimodal-instruction.md) — multimedia learning is a more specific representational principle within the broader multimodal design space
- [Dual Coding](dual-coding.md) — provides the clearest explanatory account for why coordinated representations can improve learning
- [Digital Learning](digital-learning.md) — many digital environments operationalize multimedia principles directly
- [Redundancy Principle](redundancy.md)

## Related Patterns
- [Multimedia Learning](../patterns/multimedia-learning.md)

## Examples

- [Illustrated mitosis learning material (11 pages, 1113 words) with EMME videos demonstrating multimedia processing strategies](../designs/mitosis-illustrated-text-emme-material.md)

### Illustrative

**[Multimedia Learning](../elements/multimedia-learning.md)** — A lesson combines a labeled diagram, short narration, and a brief practice prompt so learners can connect process language to a visible structure.

**[Multimedia Learning](../patterns/multimedia-learning.md)** — A reusable design pattern in which text, visuals, and interaction are coordinated intentionally rather than layered arbitrarily.

**[Flipped Learning](flipped-learning.md)** — Pre-class micro-lessons often rely on multimedia principles: concise visuals, narrated explanation, and signaling that reduce learner confusion before live practice.

## Key Sources
- Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Fiorella, L., & Mayer, R. E. (2015). *Learning as a generative activity*. Cambridge University Press. [https://doi.org/10.1017/CBO9781107707085](https://doi.org/10.1017/CBO9781107707085)
- Clinton, V., Alibali, M. W., & Nathan, M. J. (2016). Learning About Posterior Probability: Do Diagrams and Elaborative Interrogation Help? The Journal of Experimental Education, 84(3), 579-599. https://doi.org/10.1080/00220973.2015.1048847

<!-- deprecated 2026-10-01: superseded by the conditional model above. The old body follows verbatim.

## Description
Multimedia learning is the principle of combining words, visuals, and other media in ways that support understanding without overloading attention.

## Implications

Multimedia learning is strongest when multiple representations clarify a concept, process, or relationship better than a single mode alone. The principle is not “add more media.” It is coordinate modes so that each contributes something instructionally useful. Well-designed multimedia can make structure more visible and reduce interpretive burden [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M]; poorly designed multimedia can split attention, duplicate information unnecessarily, and increase extraneous cognitive load. Multimedia environments are especially strong when learners are prompted to explain how the representations relate instead of only viewing them side by side [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].

### Context
#### Requirements
- **A real representational reason to use multiple modes** — visuals, narration, text, or interaction should each contribute to understanding rather than decorate the lesson
- **Alignment between modes** — the verbal and visual channels need to reinforce the same underlying idea
- **Attention to cognitive load** — pacing, layout, and signaling affect whether learners can process the combined information productively
#### Constraints
- **More media is not automatically better** — unnecessary animation, text duplication, or interface clutter can reduce comprehension
- **Weak coordination can split attention** — learners may waste effort reconciling mismatched or badly organized representations

### Target Learners
- Learners studying content with complex structures, spatial relations, or processes that benefit from coordinated visual and verbal explanation
- Learners who need multiple access routes into the same concept
- Learners in digital or mixed-media environments where representational choices materially affect comprehension

### Target Learning Objectives
- Improve comprehension of complex ideas, processes, and relationships
- Support retention through coordinated verbal and visual encoding
- Reduce unnecessary interpretive effort when representation is the main barrier

### Theory
#### Supporting
- [Dual Coding Theory](../theories/dual-coding-theory.md) — coordinated verbal and visual representations can improve encoding and recall when they reinforce one another
- [Cognitive Load Theory](cognitive-load-theory.md) — good multimedia design reduces extraneous load and supports schema formation

#### Contradicting / Qualifying
- [Information Processing Theory](../theories/information-processing-theory.md) — multiple channels still compete for limited attention; multimedia succeeds only when design helps learners select and organize relevant information

### Claims

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — multimedia can help when it organizes information into more meaningful units, but only if the design is coherent
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M] — explicit visual-verbal models can reduce unproductive search for novices when the representation clarifies task structure
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — multimedia environments become stronger when learners are prompted to explain the relationship between representations
-->

<!-- merged 2026-10-07 from principles/visual-representations-benefit-only-with-adequate-processing-resources ("Incorporate relevant visual representations in lessons, but consider the resource demands of working with them"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Incorporate relevant visual representations in lessons, but consider the resource demands of working with them

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article concludes that relevant visual information such as diagrams in texts can improve learning, though not under all instructional conditions: "diagrams fostered students' application of the lesson content relative to text alone only if students read the lesson twice, and not if they answered questions while reading". Visual representations may be beneficial only if students have adequate resources available to process them, so teachers should consider the resource demands of working with visuals.

## Design Implications

### Context
#### Requirements
- Students must have adequate resources available to process the visual representations
#### Constraints
- The benefit of diagrams was limited to the read-twice condition in this study and did not appear when students answered questions while reading

### Target Learners
- undergraduate students reading lessons independently

### Target Learning Objectives
- applying lesson content to posterior probability problems

### Claims
- [Diagrams Help Posttest Only Read Twice Condition](../claims/diagrams-help-posttest-only-read-twice-condition.md) [+M]

## Related Principles
- 

## Examples
-

## Key Sources
- Clinton, V., Alibali, M. W., & Nathan, M. J. (2016). Learning About Posterior Probability: Do Diagrams and Elaborative Interrogation Help? The Journal of Experimental Education, 84(3), 579-599. https://doi.org/10.1080/00220973.2015.1048847
-->
