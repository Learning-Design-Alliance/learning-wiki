---
type: principle
id: pretraining
title: Pre-training Principle
description: "For learners new to a system or topic whose main lesson will use many unfamiliar parts or terms, a short primer giving the name, location and behaviour of each key component before that lesson is expected to improve transfer from it over the same lesson without a primer; claims in the wiki test this (Mayer's 5 of 5 experiments, median d = 0.85, and one VR experiment), bounded by prior knowledge, the complexity and pacing of the main lesson, and short lab tests."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-14
sources:
  - id: mayer-2008
    resource: "https://doi.org/10.1037/0003-066x.63.8.760"
    title: "Mayer, R. E. (2008). Applying the Science of Learning: Evidence-Based Principles for the Design of Multimedia Instruction. *American Psychologist*"
    author: "Mayer, R. E"
  - id: delgado-mayer-2024
    resource: "https://doi.org/10.1111/jcal.13099"
    title: "Delgado, C. Y., & Mayer, R. E. (2024). Implementing Pretraining to Optimise Learning in Immersive Virtual Reality. *Journal of Computer Assisted Learning, 41*(1)"
    author: "Delgado, C. Y., & Mayer, R. E"
  - id: noetel-et-al-2022
    resource: "https://doi.org/10.3102/00346543211052329"
    title: "Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C. (2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research, 92*(3), 413–454"
    author: "Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C"
  - id: kalyuga-et-al-2003
    resource: "https://doi.org/10.1207/s15326985ep3801_4"
    title: "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31"
    author: "Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J"
  - id: pollock-et-al-2002
    resource: "https://doi.org/10.1016/S0959-4752(01)00016-0"
    title: "Pollock, E., Chandler, P., & Sweller, J. (2002). Assimilating complex information. *Learning and Instruction, 12*(1), 61–86"
    author: "Pollock, E., Chandler, P., & Sweller, J"
  - id: ceballos-nutta-2022
    resource: "https://eric.ed.gov/?id=EJ1380081"
    title: "Ceballos, M., & Nutta, J. W. (2022). Emergent bilinguals and multimedia instructional design: Applying the science of learning principles to dual language instruction. *Education Leadership Review, 23*(1)"
    author: "Ceballos, M., & Nutta, J. W"
---

# Pre-training Principle

> **Principle** · [All principles](index.md)
> **Evidence** · 17 claims (7 for, 10 mixed) · 23 studies (9 review, 8 quant-synthesis, 5 causal, 1 theoretical), `q1`–`q4` · 7 of 23 report an effect size · 12 claims rest on one study

## Conditional relationship

This page owns one decision: **whether to teach the names and characteristics of a lesson's key components before the lesson, rather than leaving learners to pick them up during it.** For a learner who is new to a system or topic (a `novice` on that content), when the main lesson will explain how something works using many parts or terms the learner has not met, a short primer before that lesson, giving each key component's name, where it is and what it does, is expected to produce better transfer from the main lesson than the same lesson without the primer.

The relationship is tested in the claims below, though on a narrow base:

- **The direction.** In 5 of 5 experiments from Mayer's programme (computer-based lessons on brakes, pumps and geology), learners given a pre-lesson on the name, location and behaviour of each component outperformed learners without one on transfer tests, median d = 0.85 ([Mayer 2008](https://doi.org/10.1037/0003-066x.63.8.760)). One later randomised experiment (Delgado & Mayer 2024, n = 93) found the same direction in immersive virtual reality: a video naming a micropipette's parts before the VR lesson raised knowledge scores and cut errors on a real-life transfer task, with lower reported load and no difference inside VR.
- **Who the learners are.** The primer substitutes for knowledge the learner lacks. Guidance that helps novices shrinks, disappears or reverses as expertise grows (Kalyuga et al. 2003, as recorded on the expertise-reversal claims), and the isolated-elements method, the closest relative of pre-training in that review, helped novices and lost its benefit for experienced learners. Noetel et al. (2022) did not find prior knowledge to moderate the multimedia principles as a group, so the size of this boundary for pre-training itself is not established in the wiki.
- **What the main lesson is like.** Across multimedia principles, design mattered more for complex material (g = 0.70) than for simple material (g = 0.20), and more for system-paced media such as lectures (g = 0.41) than learner-paced media (g = 0.27) ([Noetel et al. 2022](https://doi.org/10.3102/00346543211052329)). These moderators are recorded for the principles as a group, not for pre-training alone.
- **The outcome and horizon.** The tests recorded are transfer and knowledge tests given soon after a short lesson. No claim in the wiki measures a delayed test, a classroom course, or a comparison of the primer with the same content given during or after the lesson.

How this sits inside its umbrella: [Multimedia Learning](multimedia-learning.md) holds the model for words with pictures and the table of all its principles; this page is its pre-training row in depth. [Cognitive Load Management](cognitive-load-management.md) holds the sequence-level model (what to defer, when to restore effort), in which pre-training is one way of introducing component knowledge before the whole; [part-task practice](../elements/part-task-practice.md) is another. Pre-training differs from an [advance organizer](../elements/advance-organizers.md), which gives a general frame at a higher level of abstraction, and from [activating prior knowledge](activation.md), which retrieves what the learner already knows: a primer teaches new component knowledge the lesson presupposes.

## Default design, while the dose is untested

The claims establish the direction and what a primer contains (name, location, behaviour of each component); they do not set its length, its distance from the lesson, or a progression. The steps below are a **labelled proposal**: contents follow the evidence, doses are untested choices.

1. **Check the condition** (basis: [expertise-reversal claims](../claims/expertise-reversal-isolated-elements-and-imagination-review.md) [~M]). Will the main lesson use parts or terms these learners have not met, and does it explain how they interact (a causal system, a procedure on equipment, a process)? If the learners already know the parts, or the lesson is simple, skip the primer.
2. **List the components the lesson presupposes** (untested proposal): read the main lesson and list every part, term or state it names without explaining. Keep to that list; the primer is not a preview of the whole lesson.
3. **Primer, about 2–5 minutes, immediately before the main lesson** (contents from [Mayer 2008](../claims/pretraining-principle-mayer-2008.md) [+M]; the length is an untested proposal): for each component, its name, where it sits (pointed out on a picture or the object), and what it does or what states it can be in (a valve open or closed, a piston up or down). Show it one component at a time, without yet explaining how the parts act on each other.
4. **Close the primer with learners naming the parts** (untested proposal): labelling a picture, pointing to a named part, or saying what one part does. This is part of the primer, not an extra test, and it tells the teacher whether the primer did its job.
5. **Main lesson, using the same names** (untested proposal; the order is from [Delgado & Mayer 2024](../claims/pretraining-improves-transfer.md) [+M]): the explanation, animation, simulation or procedure, referring to each part by the name the primer used, so learners spend the lesson on how the parts interact rather than on what they are called.
6. **Across sessions** (untested proposal): give a primer at the start of each unit that introduces a new system or a new set of parts, covering only what is new. In later sessions on the same system, replace the primer with a 1-minute recall (learners name the parts from a picture) and drop it once learners name them without help, since support a learner no longer needs can become a cost ([expertise reversal](../claims/expertise-reversal-effect-compound.md) [~M]).
7. **Judge it on the brief's own test of the main lesson** (untested proposal): transfer to a changed problem or a real task is what the recorded experiments measured; do not judge the primer by how well learners recall the primer itself.

## Fitting the design to a situation

Three facts change the decision most. Ask for them when the brief omits them: **do the learners already know the parts and terms the lesson uses?** (ask what they would call the components, or for a learner profile); **how complex is the main lesson, and who controls its pace?** (how many parts interact; is it a video or lecture, or pages the learner moves through); and **what does the brief's own assessment ask for?** (recall, explanation, or use on a real task, and when).

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` on a system with many unfamiliar parts or terms (equipment, anatomy, a mechanism, a geological process) | Give the primer: name, location and behaviour of each component, before the main lesson | [Pretraining principle: pre-lessons on names, locations, and characteristics of key components improve transfer](../claims/pretraining-principle-mayer-2008.md) [+M] (5 of 5 experiments, median d = 0.85) |
| Learners already know the parts (advanced learners, a refresher, practitioners) | Skip the primer, or replace it with a 1-minute naming check and teach only the parts they miss | [Isolated-elements benefit disappears for experienced learners](../claims/expertise-reversal-isolated-elements-and-imagination-review.md) [~M]; [Multimedia principles benefit novices more](../claims/expertise-reversal-effect.md) [~M]; qualified by [prior knowledge did not moderate the principles as a group](../claims/design-principle-effects-moderated-by-pacing-and-complexity.md) [~M] |
| A mixed class: some know the parts, some do not | Make the primer short and skippable (a labelled picture learners can consult), rather than a fixed segment for all | untested proposal |
| The main lesson is simple (few parts, little interaction between them) | The primer is unlikely to pay for its time; fold the few terms into the lesson | [Design principles mattered more for complex (g = 0.70) than simple (g = 0.20) media](../claims/design-principle-effects-moderated-by-pacing-and-complexity.md) [~M] (principles as a group, carried to pre-training) |
| The main lesson is system-paced (a lecture, a video that plays straight through, a narrated animation) | Give the primer; learners cannot stop the lesson to work out a term | [Design principles mattered more in system-paced (g = 0.41) than learner-paced (g = 0.27) media](../claims/design-principle-effects-moderated-by-pacing-and-complexity.md) [~M] (principles as a group) |
| Self-paced pages or an online course with no teacher (`online-self-paced`) | Put the primer as its own short page before the lesson, and keep the labelled picture available to reopen during the lesson | untested proposal |
| The lesson is in immersive VR or a simulation | Give the primer outside the headset or simulation, as a short video naming the parts, before learners enter | [Pretraining before an immersive-VR lesson improved knowledge and real-world transfer](../claims/pretraining-improves-transfer.md) [+M] (one experiment, n = 93) |
| The lesson is a video | Make the primer a separate short clip before the main video, not a section inside it | [Pretraining before an immersive-VR lesson improved knowledge and real-world transfer](../claims/pretraining-improves-transfer.md) [+M] (the primer there was a video); the separate clip is an untested proposal |
| Slides or a live lecture | Open with one slide per component (picture, name, what it does) before the explanation slides | untested proposal, carried from [Mayer 2008](../claims/pretraining-principle-mayer-2008.md) [+M] (computer-based lessons) |
| Print (a textbook section, a manual) | Put a labelled diagram and a short list of the parts with their functions before the explanatory text | untested proposal; teaching word meanings improved comprehension of text using those words: [Vocabulary instruction improves comprehension](../claims/vocabulary-instruction-improves-comprehension.md) [+M] (carried to pre-training) |
| Phone-only | One screen per component (picture, name, one line on what it does), swiped through before the lesson | untested proposal |
| A single session | Spend the first few minutes of that session on the primer, then the main lesson | untested proposal for the timing; direction from [Mayer 2008](../claims/pretraining-principle-mayer-2008.md) [+M] |
| A fixed short time budget (for example 20 minutes in all) | Keep the primer to the parts the lesson names, a few minutes at most, and cut anything else before cutting the primer when the lesson is complex | untested proposal; complexity moderator from [Noetel 2022](../claims/design-principle-effects-moderated-by-pacing-and-complexity.md) [~M] |
| Children (primary or lower secondary) | Use the primer with real objects or pictures and spoken names; the experiments recorded here do not report child samples | untested for pre-training; [Vocabulary instruction improves comprehension](../claims/vocabulary-instruction-improves-comprehension.md) [+M] (pre-K–12, comprehension of texts using the taught words) |
| Low literacy, or the lesson is in the learners' second language | Make the key terms the primer's content, with a picture for each and, where possible, the first-language word beside it | [Pretraining claim, second-hand report on dual-language instruction](../claims/pretraining-improves-transfer.md) [+M] (Ceballos & Nutta's report is second-hand and coded r1); [Foreign-language explanations reduced learning outcomes](../claims/double-burden-language-of-ai-instruction.md) [~M] |
| Learners who are deaf or hard of hearing | Give the primer as a labelled picture with printed or signed names, not narration alone | untested proposal |
| Learners who are blind or have low vision | Give the primer with a tactile model or the object itself, and describe each part's location in words | untested proposal |
| One teacher for a large class | Give the primer to the whole class at once from one projected picture, with learners naming parts aloud together | untested proposal |
| The brief supplies its own lesson, routine or rubric | Keep them as given; add the primer in front and change nothing in the lesson or its assessment | untested proposal |
| The material is private or proprietary (internal equipment, a company's system) | Build the primer only from the brief's own materials and parts list; it needs no learner data | untested proposal |
| The brief wants the task kept whole (a whole-task or 4C/ID design) | The primer gives component names and behaviours only; it does not split the task into part-task practice, and the main task stays whole | [Isolated parts first helped novices on complex tasks](../claims/part-task-practice-reduces-load-for-novices.md) [~M] (the part-task alternative, kept distinct) |
| High stakes (certification, safety-critical procedures) | Give the primer, and let the brief's own assessment show whether learners can use the parts on the real task; add no extra test | [Pretraining before an immersive-VR lesson reduced errors on a real-life transfer task](../claims/pretraining-improves-transfer.md) [+M]; the high-stakes setting is untested |
| The outcome that matters is delayed (an exam weeks later) | Use the primer for the first lesson, but do not count on it for retention; plan spaced retrieval of the parts and the explanation | untested; the recorded tests were given soon after the lesson |

## Observation, state and explanation

Record what the learner did, under stated conditions: whether they had a primer and what it covered, the medium and pacing of the main lesson, and what they were asked to do afterwards. "Lacks the vocabulary" or "overloaded" are inferred states. Naming a part, pointing to it, saying what it does, explaining how two parts act on each other, and using the parts on a real task are observations of different performances. These rows are proposals, untested with learners as diagnostics.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Names the parts after the primer but cannot explain how the system works | The primer worked; the main lesson did not show the interactions; the test asked for more than the lesson taught | Ask a "what happens if this part fails" question with a picture available; check whether the lesson showed that interaction. |
| Cannot name the parts at the end of the primer | Too many components at once; the names were not tied to a picture or object; the language of the primer is not the learner's | Repeat with fewer components per screen, each with its picture; try the first-language word beside it. |
| Does no better on transfer with the primer than without | The learners already knew the parts; the main lesson was simple or learner-paced; the lesson did not reuse the primer's names | Ask learners to name the parts before any primer; count the components the lesson actually uses; check the lesson's wording against the primer's. |
| Finds the primer tedious, skips it, or rates it unnecessary | Prior knowledge (expertise reversal); the primer covers parts the lesson does not use | Give a 1-minute naming check first and drop the primer for those who pass. |

## Evidence and qualifications

- [Pretraining principle: pre-lessons on names, locations, and characteristics of key components improve transfer](../claims/pretraining-principle-mayer-2008.md) [+M]: Mayer's (2008) review of his group's experiments; 5 of 5 experiments on brakes, pumps and geology, median d = 0.85 on transfer. All from one research programme with computer-based lessons; read the median as that programme's result, not as independent replications.
- [Pretraining before the main lesson improved knowledge and real-world transfer in one VR experiment](../claims/pretraining-improves-transfer.md) [+M]: Delgado & Mayer (2024), n = 93, randomised, against no pretraining; no standardised effect size printed; errors inside VR did not differ. The same claim records Ceballos & Nutta's (2022) second-hand report of pretraining studies in dual-language instruction (r1). Neither compares the primer with the same content given during or after the lesson.
- [Multimedia design principles improve learning by g = 0.38 on average across the 11 largest reviews, an effect the authors call moderate, with large differences between principles](../claims/multimedia-design-principles-improve-learning-overall.md) [+M]: the umbrella estimate across principles ([Noetel et al. 2022](https://doi.org/10.3102/00346543211052329)); the principle itself explained most of the variance, so the average does not forecast pre-training's own effect.
- [Design principle effects are larger in system-paced and in complex media, and learner prior knowledge was not a significant moderator (p = 0.14)](../claims/design-principle-effects-moderated-by-pacing-and-complexity.md) [~M]: complex over simple, system-paced over learner-paced; prior knowledge not a significant moderator (p = 0.14), which does not establish that it makes no difference.
- [The isolated-elements method benefits novices but the benefit disappears for experienced learners](../claims/expertise-reversal-isolated-elements-and-imagination-review.md) [~M] and [Expertise reversal: effects for novices decrease, disappear, and can reverse](../claims/expertise-reversal-effect-compound.md) [~M]: the reason to drop the primer for learners who know the parts. Neither tests pre-training directly.
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition](../claims/part-task-practice-reduces-load-for-novices.md) [+M]: Pollock et al. (2002); presenting isolated parts before the integrated whole helped novices on high-element-interactivity tasks. A neighbouring way of deferring component knowledge, with practice rather than a primer.
- [Cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) [+M]: the mechanism the primer is meant to address; indirect, since it tests reducing load, not pre-training.

Taken together: for novices facing a complex lesson on a system with many unfamiliar parts, a primer on those parts before the lesson improved transfer in every experiment recorded here, in one programme's lab lessons and one VR study. The wiki holds no claim on its dose, on delayed tests, on classroom courses, on children, or on a comparison with teaching the same parts during the lesson.

## The evidence by question

- *Does a primer on the key parts and terms before a complex lesson improve learning and transfer?* [Pretraining before the main lesson improved knowledge and real-world transfer](../claims/pretraining-improves-transfer.md) [+M]
- *Does the benefit shrink for learners who already know the parts?* [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows](../claims/expertise-reversal-effect.md) [~M]
- *For which material and pacing is a primer most worth its time?* [Multimedia design principles produce a moderate average improvement in learning](../claims/multimedia-design-principles-improve-learning-overall.md) [+M]
- *Does other material given before the lesson (an organizer, an activation prompt) do the same job?* [Advance organizers produce a small average learning benefit, larger for high-ability than for low-ability learners](../claims/advance-organizers-improve-learning.md) [~M]

## Further evidence, not yet read against this model

- [Multimedia Principles Benefit Novices](../claims/expertise-reversal-effect.md) [~M]: rests on the same two Kalyuga studies as the expertise-reversal claim; its discussion recommends pre-training for novices.
- [The learning benefit of increasing integration is substantially larger for high element interactivity materials](../claims/element-interactivity-moderates-contiguity-effect.md) [~M]: the complexity moderator for contiguity ([Ginns 2006](https://doi.org/10.1016/j.learninstruc.2006.10.001)), a sibling principle.
- [Advance organizers produce a small average learning benefit, larger for high-ability than for low-ability learners](../claims/advance-organizers-improve-learning.md) [~M]: a frame before the lesson rather than component knowledge; mean ES 0.21, with no special benefit for low-knowledge learners.
- [Prior-knowledge activation instructions before study had little effect on retention](../claims/prior-knowledge-activation-little-effect-on-retention.md) [~M]: talking about a topic before study is not the same as being taught its parts.
- [Prior Knowledge Determines New Learning](../claims/prior-knowledge-determines-new-learning.md) [~M]: prior knowledge predicts later knowledge strongly but not gains, which varied widely across studies.
- [Vocabulary Instruction Improves Comprehension](../claims/vocabulary-instruction-improves-comprehension.md) [+M] and [Pairing contextual encounters with explicit instruction produces stronger vocabulary outcomes than either alone](../claims/pairing-contextual-encounters-with-explicit-instruction-produces-stronger-vocabulary-outcomes-than-either-alone.md) [+M]: teaching the words a text uses, a reading-side relative of the primer.
- [Segmenting improves multimedia learning](../claims/segmenting-improves-multimedia-learning.md) [+M]: the sibling principle for the main lesson itself; its discussion treats pre-training as the front-loaded counterpart.
- [English-delivered AI explanations impose a double cognitive burden](../claims/double-burden-language-of-ai-instruction.md) [~M]: reported second-hand; why the primer's terms matter more in a second language.

## Objective and learner-valued goal

The designer's objective is that learners understand how a system works well enough to use that understanding on problems and tasks the lesson did not show. Ask separately what the learner wants: a technician who needs to operate the real equipment values the names because they are what colleagues and manuals use, while a learner who already works with the system will value getting to the new material quickly. Where the two diverge, the naming check in step 6 lets the second group skip the primer.

## What would revise this model?

The expectation should weaken if comparisons with novices, holding total time equal, find no transfer advantage for a primer over teaching the same parts during the lesson; that would locate the effect in extra exposure rather than in the order. It should narrow if studies outside Mayer's programme, in classrooms and with delayed tests, find the effect only on immediate lab tests. It would be extended by studies of the primer's length, of children, and of learners in a second language.

## Related Principles
- [Modality Principle](modality.md)
- [Redundancy Principle](redundancy.md)
- [Segmenting Principle](segmenting.md)
- [Signaling Principle](signaling.md)
- [Contiguity Principle (Spatial and Temporal)](contiguity.md)
- [Coherence Principle](coherence.md)

- [Multimedia Learning](multimedia-learning.md): the umbrella model; this page is its pre-training principle in depth
- [Cognitive Load Management](cognitive-load-management.md): the sequence-level model in which pre-training is one way to defer component knowledge
- [Chunking](chunking.md): limiting how much new material arrives at once
- [Worked Examples](worked-examples.md): another support for novices that fades with expertise
- [Activation](activation.md): retrieving prior knowledge, as distinct from teaching new component knowledge
- [Explicit Vocabulary Instruction](explicit-instruction-vocabulary.md): teaching words before or alongside reading
- [Sequencing](sequencing.md): ordering what comes first in a unit
- [Holistic Learning](holistic-learning.md)

## Examples

- [Pre Training](../strategies/pre-training.md): the strategy that carries this principle into an activity
- [Advance Organizers](../elements/advance-organizers.md) and [Part-task practice](../elements/part-task-practice.md): neighbouring building blocks placed before the main task
- [4C/ID](../patterns/4cid-four-component-instructional-design.md): a whole-task pattern whose supportive information plays a similar role
- [Multimedia Learning pattern](../patterns/multimedia-learning.md)

## Key Sources

- Mayer, R. E. (2008). Applying the Science of Learning: Evidence-Based Principles for the Design of Multimedia Instruction. *American Psychologist*. [doi:10.1037/0003-066x.63.8.760](https://doi.org/10.1037/0003-066x.63.8.760)
- Delgado, C. Y., & Mayer, R. E. (2024). Implementing Pretraining to Optimise Learning in Immersive Virtual Reality. *Journal of Computer Assisted Learning, 41*(1). [doi:10.1111/jcal.13099](https://doi.org/10.1111/jcal.13099)
- Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B., & Lonsdale, C. (2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research, 92*(3), 413–454. [doi:10.3102/00346543211052329](https://doi.org/10.3102/00346543211052329)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/s15326985ep3801_4](https://doi.org/10.1207/s15326985ep3801_4)
- Pollock, E., Chandler, P., & Sweller, J. (2002). Assimilating complex information. *Learning and Instruction, 12*(1), 61–86. [doi:10.1016/S0959-4752(01)00016-0](<https://doi.org/10.1016/S0959-4752(01)00016-0>)
- Ceballos, M., & Nutta, J. W. (2022). Emergent bilinguals and multimedia instructional design: Applying the science of learning principles to dual language instruction. *Education Leadership Review, 23*(1). [ERIC EJ1380081](https://eric.ed.gov/?id=EJ1380081)
