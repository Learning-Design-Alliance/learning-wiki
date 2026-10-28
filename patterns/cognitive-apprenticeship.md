---
type: pattern
id: cognitive-apprenticeship
moved_from: [principle/notice-and-name-instructional-practices]
aliases: [four-reflection-methods-reification, guided-equation-appropriation]
title: Cognitive Apprenticeship
description: "A reusable modeling, coaching, scaffolding, fading, articulation and exploration policy for complex cognitive skills, whose phase transitions depend on observed unaided performance and remain an untested design proposal."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: lave-1991
    resource: "https://doi.org/10.1017/CBO9780511815355"
    title: "Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral participation*. Cambridge University Press"
    author: "Lave, J., & Wenger, E"
  - id: van-merriënboer-2018
    resource: "https://doi.org/10.4324/9781315113210"
    title: "van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge"
    author: "van Merriënboer, J. J. G., & Kirschner, P. A"
  - id: dozier-2008
    resource: "https://eric.ed.gov/?id=EJ1059644"
    title: "Dozier, C. L. (2008). Literacy coaching: Engaging and learning with teachers. The Language and Literacy Spectrum, 18. https://eric.ed.gov/?id=EJ1059644"
    author: Dozier, C. L
  - id: collins-1988
    resource: "https://eric.ed.gov/?id=ED331465"
    title: "Collins, Allan. (1988). Cognitive Apprenticeship and Instructional Technology. Technical Report. BBN Report No. 6899, BBN Labs, Inc. https://eric.ed.gov/?id=ED331465"
    author: Collins, Allan
  - id: kapon-schvartzer-2024
    resource: "https://doi.org/10.1080/07370008.2023.2197232"
    title: "Kapon, S., & Schvartzer, M. (2024). Guided Inquiry into a Physics Equation. Cognition and Instruction, 42(1), 159-206."
    author: "Kapon, S., & Schvartzer, M."
author: "Collins, Brown, & Newman (1989)"
grain_size: course, unit
---

# Cognitive Apprenticeship

> **Pattern** · [All patterns](index.md)
> **Evidence** · 31 claims (13 for, 15 mixed, 3 against) · 29 studies (10 causal, 5 quant-synthesis, 4 review, 4 qualitative, 3 associational, 2 theoretical, 1 design), `q1`–`q4` · 3 of 29 report an effect size · 27 claims rest on one study

## Description and scope

This is a reusable policy for teaching a complex cognitive skill whose expert reasoning is not visible in the finished product: writing, diagnosing, debugging, reading for meaning, solving a non-routine problem. An expert makes the reasoning visible (**modeling**). The learner attempts the task while the expert watches and responds (**coaching**), and gets support matched to where they struggle (**scaffolding**). That support is withdrawn as the learner shows they can work without it (**fading**). The learner then states their reasoning and compares it with the expert's (**articulation, reflection**), and finally applies the skill to new problems with little guidance (**exploration**). It instantiates the [scaffolding and fading principle](../principles/scaffolding-and-fading.md). The study configurations below are evidence about parts of this sequence. The whole sequence, and the response-dependent policy that moves a learner between its phases, is an **untested design proposal**: no claim in this wiki tests the full six-phase arc against an alternative.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Task-specific experience; an unassisted attempt at a representative task, with the learner's reasoning, errors and confidence. Preserve unknowns. A professional or graduate learner can still be a `novice` for this task. |
| Context and activities | Setting (one-to-one, small group, whole class, `online-self-paced`, `workplace-clinical`); who models (expert, peer, recorded); time available; how coaching and support are delivered and logged; tools and aids permitted. |
| Learner-valued goal | Ask what the learner wants to be able to do and why. Record it apart from the designer's objective; agreement is an observation. |
| Designer objective | The capability (`complex-skill`, `procedure`, `metacognitive-strategy`), a representative task, what must be done without support, and which aids remain legitimate at the end. |
| Outcome | Instrument and local criterion; immediate and delayed horizons; whether a standardised or researcher-made measure is used (they give different effect sizes, see below); any real-use outcome. |

A request to "use cognitive apprenticeship" does not specify these. Ask for them before fixing the length of each phase, a fading schedule or an expected gain.

## Sequence and conditional policy

1. **Elicit.** Ask for an unassisted attempt and the learner's reasoning before any modeling. Keep it short; it is a probe, not a treatment. Record it.
2. **Model with reasons.** Show expert performance on a representative task, narrating the decisions and the cues that triggered them, not just the steps. If the learner already produces adequate unaided reasoning on varied cases, shorten or skip modeling (expertise reversal).
3. **Coach and scaffold contingently.** The learner attempts a comparable task. Raise support after a failure and lower it after a success, starting from the least support that might do (a cue before a hint, a hint before a partial solution). Record each level given and whether the learner applied, copied or ignored it.
4. **Check before withdrawing.** Before removing a support, ask the learner to do or explain the next step without it. Withdraw gradually, and announce it.
5. **Articulate and reflect.** Ask the learner to state their reasoning and compare their process with the model, naming one difference that mattered.
6. **Explore and reobserve.** Pose a changed problem with minimal guidance, under the agreed aids and at the stated horizon. If the response disagrees with the expectation, revise the interpretation or the configuration, not only the learner's label.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Cannot start after watching the model | Ask what the expert did first and why; give a matched task with a first-step cue only. | If the learner can name the reason but not act on it, coach the first step with minimal prompts. If they cannot name it, model again on a contrasting case, with the decision point marked. Neither branch is a validated diagnosis. |
| Succeeds only at the support level last given | Present the next comparable step at one level lower (a cue instead of a hint). | If the lower level is enough, keep fading one level at a time. If not, hold the level and change the case. One success does not establish readiness; no fading threshold is supported. |
| Correct answer, but copied rather than applied | Ask for an explanation, and pose a changed case the copied move would not solve. | Treat the support as not yet taken up. Check understanding explicitly before the next withdrawal; the link to later accuracy is associational. |
| Fluent with the expert's model, poor on a changed problem | Vary one relevant condition, not only surface details; ask what changes and why. | Add articulation and comparison across contrasting cases before exploration; do not repeat the same model. |
| Avoids or refuses support it still needs; or relies on support it no longer needs | Offer the task with support optional; ask privately about purpose and barriers. | Negotiate the goal or conditions when they drive the pattern. Help use alone is not evidence of competence or of its absence. |

## Choosing configurations from evidence

- **The whole approach.** [Cognitive apprenticeship methods were reported more effective than traditional methods for college writing](../claims/ca-methods-more-effective-than-traditional-writing-college.md) [+W]. This is second-hand: a narrative review reports an earlier study's finding, with no design detail and no effect size. The judge checked the review's text, not the original study. Treat it as a pointer, not as a forecast.
- **Modeling with gradual handover, in reading.** [Reciprocal teaching improves reading comprehension](../claims/reciprocal-teaching-improves-reading-comprehension.md) [+M]. Teachers model four strategies and hand the discussion-leader role to students. A review of 16 studies reports a median effect of .32 on standardised comprehension tests and .88 on researcher-made tests. The outcome instrument changes the size of the benefit, so state which one a design will use. Read from an abstract; not yet checked against its sources.
- **Model first, then attempt.** [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+M]. Dutch secondary-school `novice` learners in circuit troubleshooting (96 analysed, randomised) did better on an immediate test, with lower reported mental effort, when training began with a worked example than when it began with a problem. This supports putting modeling before attempts in a short `procedure` task. It establishes no delayed or far-transfer effect. Not yet checked against its sources.
- **Contingent coaching.** [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]. In small one-to-one tutoring studies, fully contingent support beat fixed or no support in long division, at an immediate and a one-month test. A dynamic-assessment synthesis ranked explicit strategy training above scaffolding and scaffolding above coaching. So "coaching" without contingent support, or in place of explicit strategy teaching, is not what this evidence supports. Not settled: abstracts could not confirm the entries.
- **Fading.** [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]. Across three experiments, a gradual move from complete to incomplete examples to independent problems favoured near transfer over static example–problem arrangements, and removing the last steps first did better than removing the first steps first. No fading rate is established. Not settled: abstracts could not confirm the entries.
- **When to shorten the arc.** [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]. Full guidance helps `novice` learners more than knowledgeable ones and can become redundant for them, so a learner who already performs unaided should not be sent through every phase. Reviews only, not settled against their sources. They give no individual cut-off.

Do not rank these against one another or average them: their learners, tasks, comparators and outcomes differ. Nothing here supports a fixed duration for each phase (the old "weeks, not a single lesson" is a design judgement, not a finding).

## The evidence by question

Each question below links a general claim that gathers the studies behind it into one table, one row per distinct study, with each study's design and effect as recorded and no averaged verdict (`eval/synthesis/cognitive-apprenticeship.json`, `scripts/synthesize_claim.py`). The count is of distinct studies across the claim and the narrower claims that bear on it.

- Does the whole cognitive-apprenticeship approach beat traditional instruction? [The review reports that cognitive apprenticeship instructional methods were significantly more effective than traditional methods for college-level writing skills](../claims/ca-methods-more-effective-than-traditional-writing-college.md) [+M]: 4 distinct studies.
- Does modelling strategies and handing the lead to learners improve reading comprehension, and on which measures? [Reciprocal Teaching Improves Reading Comprehension](../claims/reciprocal-teaching-improves-reading-comprehension.md) [+M]: 2 distinct studies.
- Should modelling come before the learner's first attempts? [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S]: 7 distinct studies.

## Fitting the design to a situation

Ask for three facts when the brief omits them: **the learner's unassisted attempt and reasoning on a representative task**, **who coaches, and how many learners each coach serves**, and **which outcome measure and horizon will judge the design**.

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are new to this task | Put modelling first: a worked or narrated example, then the learner's attempt, rather than starting with a problem | [Example-problem sequences reduce cognitive load](../claims/worked-example-problem-sequences.md) [+M]; [Example-based sequences outperform problem-only practice](../claims/worked-examples-with-practice-improve-transfer.md) [+M] |
| The target is reading comprehension | Use reciprocal teaching: model summarising, questioning, clarifying and predicting, then hand the discussion lead to learners | [Reciprocal teaching improves reading comprehension](../claims/reciprocal-teaching-improves-reading-comprehension.md) [+M]; [Reciprocal teaching raises comprehension of poor readers](../claims/reciprocal-teaching-raises-reading-comprehension-poor-readers.md) [+W] |
| Success will be judged on a standardised test | Expect a smaller gain than researcher-made tests show (median .32 against .88 for reciprocal teaching) and set expectations accordingly | [Reciprocal teaching improves reading comprehension](../claims/reciprocal-teaching-improves-reading-comprehension.md) [~M] |
| One-to-one or small-group coaching is possible | Coach contingently: least help first, more after a failure, less after a success | [Contingent scaffolding improves learning](../claims/contingent-scaffolding-improves-learning.md) [+M] |
| One instructor coaches a whole online cohort | Set limits on coaching time, and use recorded models or peer coaching for part of it; coaching without a time limit became a large, open-ended load for the instructor | [Web-based cognitive apprenticeship required large instructor time](../claims/web-based-ca-instructor-time-burden.md) [~W] |
| Support moves from worked examples to independent problems | Fade from complete to incomplete examples to independent problems across the cases, not in one step | [Fading support promotes transfer of responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M] |
| A learner already performs the task unaided | Shorten or skip modelling and coaching for that learner and move to articulation and exploration | [Worked-example guidance becomes less effective with expertise](../claims/worked-examples-less-effective-with-expertise.md) [~M] |
| The course replaces traditional instruction in technical mathematics and is judged on exams | Do not promise exam gains; one community-college quasi-experiment found none, and higher mathematics anxiety alongside more confidence. Track anxiety as an outcome | [No significant exam differences in technical mathematics](../claims/cognitive-apprenticeship-no-significant-exam-differences-technical-math.md) [-M]; [Anxiety rose while confidence grew](../claims/cognitive-apprenticeship-attitude-anxiety-confidence-effects.md) [~M] |
| Learners are learning to program or debug | Order tasks from completing a program to fixing a faulty one to building one; reasoning shifted toward diagnosis as tasks moved on | [Scaffolded task progression shifts novices toward diagnosis](../claims/scaffolded-task-progression-diagnostic-shift.md) [+W] |
| The brief fixes a length for each phase (weeks of modelling, then coaching) | Move learners between phases on their unaided performance instead; no phase length is established | untested proposal |

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] — not settled: the text available could not confirm the entries (abstract)
- [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [Mentored inquiry with staged mechanistic sensemaking supports the transition from intuitive to formal equation reasoning](../claims/mentored-inquiry-supports-transition-from-intuitive-to-formal-equation-reasoning.md) [+W]
- [A network of three mutually overlapping intuitive ideas (less distance implies less time, bunched up means faster, faster implies less time) stabilizes students' initial thinking](../claims/network-of-intuitive-ideas-stabilizes-thinking.md) [~W]

## Illustrative design instance and observation record

*Illustration only, not a tested design.* A first-year nursing student wants to stop freezing when a patient's vital signs change. The designer wants the student to reason aloud from observations to a priority action. Agree that both matter, and that the target is a simulated deterioration case handled without prompts, assessed with an agreed reasoning rubric now and again in four weeks. The instructor models one case, narrating which cue changed their priority. The student then works a second case with prompts that are withdrawn after the student explains the next step correctly. The student articulates their reasoning against the instructor's, and finally works a changed case alone. None of these choices (the number of cases, the four-week horizon, the withdrawal rule) is established by the evidence above.

Record: **task and conditions → model shown (what was narrated) → learner attempt → support level given and whether it was applied, copied or ignored → check before withdrawal and its result → candidate interpretations and their basis → next activity and why → unassisted response at the stated horizon**. Keep the learner's stated purpose and any change in it. An agent may summarise this record, but must not invent missing inputs or assign numerical probabilities to a learner's state without a calibrated model.

## Elements and limits

[Modeling](../elements/modeling.md), [think-aloud](../elements/think-aloud.md), [demonstration](../elements/demonstration.md), [worked examples](../elements/worked-examples.md), [coaching](../elements/coaching.md), [eliciting student thinking](../elements/eliciting-student-thinking.md), [feedback](../elements/feedback.md), [hints](../elements/hints.md), [scaffolding](../elements/scaffolding.md), [fading](../elements/fading.md), [articulation](../elements/articulation.md), [reflection](../elements/reflection.md) and [practice](../elements/practice.md). Principles the sequence draws on: [worked examples](../principles/worked-examples.md), [scaffolding](../principles/scaffolding.md), [guided practice](../principles/guided-practice.md) and [purposeful reflection](../principles/reflection.md).

This pattern is general across domains; a clinical round, a writing workshop or a design studio is a design that uses it, not a separate pattern. It depends on someone being able to make their reasoning explicit, and contingent coaching is hard to sustain for many learners at once. The evidence for contingency comes mostly from one-to-one tutoring. Whether the full sequence improves independent performance more than explicit strategy instruction, or more than its parts used alone, has not been tested here, and neither has its diagnostic policy.

## Claims

- [Scaffolded task progression shifts novice reasoning from local completion toward diagnosis and systematic debugging as task demands increase](../claims/scaffolded-task-progression-diagnostic-shift.md) [~W]
- [Integrating cognitive apprenticeship methods in a Web-based course required a significant and largely unbounded instructor time investment](../claims/web-based-ca-instructor-time-burden.md) [~W]
- [Scaffolding effects varied by education population, with traditional learners significantly outperforming underperforming learners](../claims/education-population-moderates-scaffolding-effect.md) [~W]
- [No effect of fading on productive learning events including self-explanations was found in Experiment 2's think-aloud analysis](../claims/fading-no-effect-productive-learning-events.md) [-W]
- [Teacher and researcher coaches both used a cognitive apprenticeship approach but differed in scaffolding style](../claims/bioworld-coaching-styles-cognitive-apprenticeship.md) [~W]
- [Expert scaffolding is associated with ILS adoption, but the fading stage shows a comparatively low rate (8.27%) and was a non-significant predictor](../claims/expert-scaffolding-associated-with-adoption-except-fading.md) [~W]
- [Model-observer gender combination affects mental effort invested during example study: male students invest less effort with a male model, female students more effort with a male model](../claims/gender-interaction-mental-effort-example-study.md) [~W]
- [No significant differences in learning measures across teacher-coached, researcher-coached, and BioWorld-alone conditions](../claims/bioworld-coaching-condition-null-manova.md) [-W]
- [Students start with video modeling examples but shift toward worked examples and practice problems as the learning phase progresses](../claims/video-examples-first-shift-to-worked-examples.md) [~W]
- [Scaffold effects peak at 2–4 weeks of treatment and decrease dramatically for treatments lasting 9–24 weeks](../claims/treatment-duration-moderates-scaffold-effects.md) [~W]
- [Experts introduce procedure and planning explanations over time, typically after an initial step or action is completed](../claims/planning-explanations-later-in-turn.md) [+W]
- [Experts scaffold by reassuring novices to continue acting or thinking, removing uncertainty about whether they chose the right action](../claims/reassurance-cues-sustain-novice-continuation.md) [~W]
- [Active verbal cues from experts most often prompt nonverbal action from novices, often preceding explanatory information](../claims/verbal-cues-prompt-nonverbal-action.md) [~W]
- [Customized scaffolding (fading/adding) outperforms non-customized scaffolding in PBL-STEM, with fading/adding highest at g = 0.590](../claims/scaffolding-customization-fading-adding-highest.md) [~W]
- [Expert modeling, feedback, hints, and multiple strategies improve cognitive outcomes, but question prompts show no evident difference from control](../claims/scaffolding-strategy-moderator-question-prompts-null.md) [+W]
- [Instructor motion is positively associated with BtBC only during scaffolding, not explanation](../claims/instructor-motion-btbc-scaffolding-only.md) [~W]
- [Engagement was reported more during the unscaffolded fadeout phase, while curiosity and neutral were reported more during the scaffolded learning phase](../claims/affect-differences-scaffolded-fadeout-phases.md) [~W]
- [A simulated learning companion using menu-based dialogue in an ITS encourages student reflection and articulation, enhancing learning](../claims/menu-based-learning-companion-encourages-reflection-articulation.md) [+W]

## Related Patterns
- [Four-Component Instructional Design](4cid-four-component-instructional-design.md) — shares the principle of worked examples fading to full tasks; provides more formal scaffolding design rules for complex learning
- [Guided Discovery Learning](../principles/inquiry-based-learning.md) — similar progression from support to independence, but begins with learner exploration rather than expert modeling
- [Three fading-based scaffolding approaches: supportive, intrinsic and reflective scaffolding](../principles/scaffolding-and-fading.md)
- (none yet linked)

## Examples

**Medical education — clinical rounds:** Attending physicians model diagnostic reasoning by thinking aloud through a patient case, then coach residents through their own case assessments with progressively less guidance over weeks.

**Writing instruction — writer's workshop:** Teacher models drafting and revision strategies on a shared text, thinking aloud about audience and structure; students write alongside with peer and teacher coaching; feedback is gradually reduced as writers develop independent revision habits. Uses [teacher modeling](../elements/demonstration.md), [conferencing](../elements/feedback.md), and [author's chair](../elements/articulation.md) sharing.

**Engineering education — design studios:** Expert designers walk through a design decision process on a real project; students work on their own projects with structured critiques (charettes) that fade from expert-led to peer-led over the semester.

**[Replit](https://replit.com) and paired programming environments:** Expert-novice pairing where the expert narrates code decisions; over time the novice takes the keyboard while the expert coaches. Fading occurs as the novice's contributions increase.
- [Interactive Modeling](../strategies/interactive_modeling.md)
- [Model Empathy and Explain](../strategies/model_empathy_and_explain.md)
- [Connecting Struggles to Strategies](../strategies/connecting_struggles_to_strategies.md)
- [Mentor Text Analysis](../strategies/mentor-text-analysis.md)
- A high-school student researching wave velocity in liquids spent under 10 minutes deriving the phase-velocity equation v = (gλ/2π + σ/2πλρ)tanh(2πh/λ), but "hours and days" across three mentoring sessions working through what each term meant, why surface tension was negligible in his experimental conditions, and why velocity increased with depth — moving over the course of the year from "classic ADHD" disengagement (his 10th-grade teacher's description) to sustained, self-directed inquiry.

## Key Sources
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship: Teaching the crafts of reading, writing, and mathematics. In L. B. Resnick (Ed.), *Knowing, learning, and instruction: Essays in honor of Robert Glaser* (pp. 453–494). Lawrence Erlbaum. [doi:10.4324/9781315044408-14](https://doi.org/10.4324/9781315044408-14)
- Collins, A., Brown, J. S., & Holum, A. (1991). Cognitive apprenticeship: Making thinking visible. *American Educator, 15*(3), 6–11, 38–46.
- Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral participation*. Cambridge University Press. [doi:10.1017/cbo9780511815355](https://doi.org/10.1017/cbo9780511815355)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge. [doi:10.4324/9781315113210](https://doi.org/10.4324/9781315113210)
- Dozier, C. L. (2008). Literacy coaching: Engaging and learning with teachers. The Language and Literacy Spectrum, 18. https://eric.ed.gov/?id=EJ1059644
- Collins, Allan. (1988). Cognitive Apprenticeship and Instructional Technology. Technical Report. BBN Report No. 6899, BBN Labs, Inc. https://eric.ed.gov/?id=ED331465
- Kapon, S., & Schvartzer, M. (2024). Guided Inquiry into a Physics Equation. *Cognition and Instruction, 42*(1), 159-206. [https://doi.org/10.1080/07370008.2023.2197232](https://doi.org/10.1080/07370008.2023.2197232)

<!-- deprecated 2026-10-01: superseded by the conditional model above. The former body, kept verbatim:

## Description
Cognitive apprenticeship adapts the structure of traditional craft apprenticeship to the teaching of complex cognitive skills. Experts make their thinking visible through modeling and narration; learners then practice under coaching with gradually fading support until they can perform independently. Where traditional apprenticeship involves observable physical skill, cognitive apprenticeship focuses on surfacing invisible mental processes — how an expert reads, writes, solves problems, or debugs code.

## Implications

The pattern is grounded in the idea that expert performance is largely tacit: practitioners cannot simply tell novices what to do because much of their knowledge is embedded in practice rather than explicit rules. By externalizing expert reasoning through [think-aloud](../elements/think-aloud.md) and [demonstration](../elements/demonstration.md), cognitive apprenticeship makes that tacit knowledge learnable. The sequence of modeling → coaching → fading mirrors the natural progression from high support to independence, reducing cognitive load during acquisition [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] while building the metacognitive awareness needed for self-regulated performance.

### Context
#### Requirements
- An expert or instructor capable of making their reasoning explicit, not just demonstrating correct outcomes
- Structured opportunities for guided practice with feedback ([Coaching](../elements/coaching.md))
- A mechanism for progressively reducing support ([Fading](../elements/fading.md))
- Tasks that are sufficiently complex to require expert thinking — simple procedural tasks don't benefit from the full pattern

#### Constraints
- Time-intensive; difficult to scale in large classrooms without significant support structures
- Quality depends heavily on the instructor's ability to articulate reasoning, which varies widely
- Premature fading (removing support before competence develops) can cause setbacks [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Less effective for well-defined procedural tasks where direct instruction is more efficient

#### Grain Size
Course or unit — the full modeling → coaching → fading arc typically unfolds over weeks, not a single lesson.

### Target Goals
- Acquisition of complex cognitive skills: writing, mathematical reasoning, scientific inquiry, clinical diagnosis, programming
- Transfer of expert heuristics and strategies that are not easily articulated as rules
- Metacognitive awareness: learners monitoring and regulating their own thinking

### Target Learners
- Novices entering a domain with complex cognitive demands
- Learners who need to internalize expert judgment, not just follow procedures
- Apprentices, graduate students, medical residents, and others in professional formation contexts

### Theory
#### Supporting
- [Situated Learning](../theories/situated-learning.md) (Lave & Wenger) — learning is embedded in authentic practice; cognitive apprenticeship situates skill development in real or realistic tasks
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) (Sweller) — modeling and fading manage cognitive load by providing support during acquisition and withdrawing it as schema develops
- [Self-Regulated Learning](../theories/self-regulated-learning.md) (Zimmerman) — explicit modeling of metacognitive moves supports learners in developing their own monitoring and control

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — some constructivist approaches favor learner-driven discovery over expert-led modeling; highly structured apprenticeship may limit generative processing

### Claims
#### Supporting
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] — worked examples (the modeling phase) reduce unnecessary search for novices
- [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+S] — pairing demonstration with practice supports transfer
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+M] — example–problem sequences outperform problem-only practice

#### Contradicting

- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — expertise reversal: too much guidance can impede learners who already have strong prior knowledge

## Design

### Sequence
1. **Modeling** — Expert performs the target task while thinking aloud, using [worked examples](../elements/demonstration.md) or [think-aloud](../elements/think-aloud.md) to surface reasoning and decision points
2. **Coaching** — Learner attempts the task while the expert observes, gives targeted [feedback](../elements/feedback.md), and prompts reflection with [questions](../elements/eliciting-student-thinking.md)
3. **Scaffolding** — Expert provides [structured support](../elements/scaffolding.md) (hints, partial solutions, checklists) calibrated to where the learner struggles
4. **Fading** — Support is progressively reduced as competence develops, using [fading](../elements/fading.md) to shift responsibility to the learner
5. **Articulation** — Learner explains their reasoning aloud or in writing ([Articulation](../elements/articulation.md)), making tacit knowledge explicit
6. **Reflection** — Learner compares their performance to the expert model and identifies gaps ([Reflection](../elements/reflection.md))
7. **Exploration** — Learner applies skills to novel problems with minimal guidance

### Affordances
- [Worked Examples](../principles/worked-examples.md) — enacts this principle by making the modeling phase a narrated, annotated demonstration of expert problem-solving, giving learners a complete cognitive model to study before attempting tasks themselves
- [Scaffolding](../principles/scaffolding.md) — applies this principle by calibrating support (hints, partial solutions, checklists) to exactly where the learner struggles, providing just enough assistance to keep them progressing without removing the cognitive work that drives learning
- [Guided Practice](../principles/guided-practice.md) — implements this principle through the coaching phase, where learners attempt authentic tasks with expert observation and targeted feedback rather than practicing in isolation or receiving only after-the-fact grades
- [Purposeful Reflection](../principles/reflection.md) — builds this principle directly into the sequence: the articulation and reflection phases require learners to compare their own performance to the expert model and name specific gaps, turning implicit self-assessment into deliberate metacognitive work

### Personalization

**Novices with no prior knowledge:** Extend the modeling phase — provide multiple worked examples across varied problem types before moving to coaching. Use explicit think-alouds at every decision point, not just key steps. Keep tasks simple and well-defined during early modeling so the process itself is the focus.

**Learners with some background knowledge:** Compress or skip early modeling; start at the coaching phase with more complex or ambiguous tasks. Reduce the amount of narrated reasoning and shift responsibility for articulation to the learner earlier.

**Learners with anxiety or low confidence:** Consider peer modeling rather than expert modeling — watching someone of similar status struggle and succeed reduces the intimidation of expert performance. Build early wins with simpler tasks before increasing challenge.

**Learners with diverse prior knowledge in the same cohort:** Use differentiated fading — keep scaffolds available for those who need them while allowing more advanced learners to bypass them. Pair-based coaching (stronger with weaker) can extend reach in large classrooms.

**Learners with language or learning differences:** Supplement verbal think-alouds with written annotations or visual step-maps so the reasoning is persistent and reviewable, not just heard once. Extend the coaching phase and reduce the pace of fading.
-->

<!-- merged 2026-10-07 from principles/notice-and-name-instructional-practices ("Notice and name instructional practices and the purposes behind them"), misfiled as a principle and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Notice and name instructional practices and the purposes behind them

> **Principle** · [All principles](index.md)
> **Evidence** · no claims cited

## Description
Drawing on Johnston (2004), the author names for teachers the practices enacted with them and articulates the purpose of each, so explicitness operates on two levels: it names the practice and the purpose behind it. The same specificity is modeled with children, for example asking a child after a Running Record how she knew to self-correct. As teachers model naming for students, students begin to name their own practices, which the author says encourages a shared language.

## Design Implications

### Context
#### Requirements
- The coach must articulate purpose aloud while enacting a practice with teachers or students
#### Constraints
- 

### Target Learners
- classroom teachers and elementary students

### Target Learning Objectives
- developing a shared professional language for literacy practices
- students articulating their own literate strategies

### Claims
- 

## Related Principles
- 

## Examples

- [Interactive Modeling](../strategies/interactive_modeling.md)
- [Model Empathy and Explain](../strategies/model_empathy_and_explain.md)
- [Connecting Struggles to Strategies](../strategies/connecting_struggles_to_strategies.md)
- [Mentor Text Analysis](../strategies/mentor-text-analysis.md)

## Key Sources
- Dozier, C. L. (2008). Literacy coaching: Engaging and learning with teachers. The Language and Literacy Spectrum, 18. https://eric.ed.gov/?id=EJ1059644
-->

<!-- merged 2026-10-15 from patterns/four-reflection-methods-reification ("Four methods of reflection on performance: imitation, replay, abstracted replay, and spatial reification"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Four methods of reflection on performance: imitation, replay, abstracted replay, and spatial reification

> **Pattern** · [All patterns](index.md)
> **Evidence** · no claims cited

## Description
The paper enumerates four ways of permitting students to reflect on their performance: "(1) imitation, (2) replay, (3) abstracted replay and (4) spatial reification," illustrated via tennis coaching. Technology makes the last three forms possible, which the authors call "a genuinely new teaching method emerging out of technology." Reflection turns the student's performance into an object of study, lets students compare their performance to others', supports characterizing strategies abstractly, and permits comparison of multiple performances to form abstractions about expert versus novice performance.

## Design Implications

### Context
#### Requirements
- Multiple views of performance and the ability to compare one's performance to expert performance
#### Constraints
- 

### Target Learners
- Students learning cognitive skills such as geometry proof construction

### Target Goals
- Analyzing one's own problem-solving processes and forming hypotheses about what makes performance successful

### Claims
- 

## Related Patterns

- [Three fading-based scaffolding approaches: supportive, intrinsic and reflective scaffolding](../principles/scaffolding-and-fading.md)

## Examples
-

## Key Sources
- Collins, Allan. (1988). Cognitive Apprenticeship and Instructional Technology. Technical Report. BBN Report No. 6899, BBN Labs, Inc. https://eric.ed.gov/?id=ED331465
-->

<!-- merged 2026-10-15 from patterns/guided-equation-appropriation ("Guided Equation Appropriation"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Guided Equation Appropriation

> **Pattern** · [All patterns](index.md)
> **Evidence** · 2 claims (1 mixed, 1 unmarked) · 2 studies (2 qualitative), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
When a student encounters a physics equation directly (e.g., looked up or given), they can often derive or apply it long before they understand what it means or implies. This pattern sequences instruction to build understanding in the other direction: mechanistic, intuitive reasoning first, formal equation second, deep interpretive reading of the equation third — with a mentor making seven specific kinds of moves throughout to keep the student's own reasoning central rather than substituting the mentor's expertise for it.

## Implications

### Context
#### Requirements
- An authentic, extended inquiry context (the source case was a year-long student research project) rather than a single lesson, since deep interpretive reading of an equation took "hours and days" even after derivation took minutes
- A mentor willing to withhold explanation until the student has attempted mechanistic reasoning and dimensional/qualitative hypothesizing on their own
#### Constraints
- This is evidence from a single mentored student over one year; the specific pacing (weeks between sessions) may not transfer to a standard classroom period structure
- Depends on a mentor skilled at anticipating student difficulties well enough to sequence the seven instructional moves responsively, rather than following a fixed script
#### Grain Size
Unit (the source study analyzed an equation-focused sequence unfolding across multiple 3-hour sessions over several weeks, within a year-long project)

### Target Goals
- Reading comprehension of a physics equation at the textually-explicit, textually-implicit, and scriptally-implicit levels
- [Mentored inquiry with staged mechanistic sensemaking supports the transition from intuitive to formal equation reasoning](../claims/mentored-inquiry-supports-transition-from-intuitive-to-formal-equation-reasoning.md)

### Target Learners
- Students engaged in an extended, equation-centered research inquiry with access to sustained one-on-one or small-group mentoring

### Theory
#### Supporting
- [Equations as Language](../theories/equations-as-language.md)
#### Contradicting / Qualifying
- (none yet linked)

### Claims
#### Supporting
#### Contradicting

- (none yet linked)
- [A network of three mutually overlapping intuitive ideas (less distance implies less time, bunched up means faster, faster implies less time) stabilizes students' initial thinking](../claims/network-of-intuitive-ideas-stabilizes-thinking.md) [~W]

## Design

### Sequence
1. **Anticipating the formalism**: before the equation is introduced, the student crafts a mechanistic explanation of the phenomenon (identifying relevant entities, variables, and relations), generates qualitative predictions ("if X increases, Y decreases"), and hypothesizes a crude mathematical form (e.g., via dimensional analysis) — all without being given the actual equation.
2. **Introducing the equation**: the formal equation is introduced once the student has an intuitive stance to compare it against.
3. **Reading through the equation — textually explicit**: identify what each variable and parameter in the equation means.
4. **Reading through the equation — textually implicit**: mentally simulate how changing one variable affects another; test special cases; run numerical simulations to check inferred relationships.
5. **Reading through the equation — scriptally implicit**: identify compound terms as meaningful conceptual units (not just symbols), substitute real values, and explicate the equation's meaning in words, connecting it back to the mechanistic explanation from step 1.

Throughout, the mentor makes seven kinds of moves: disciplining perception (directing attention to relevant features), telling (re-explaining when needed), explicating continuity (connecting new work to prior steps), deliberate attentiveness (examining student work and asking clarifying questions), capitalizing on student ideas (elaborating and re-voicing rather than replacing them), responsive sequencing (timing new activities to the student's progress), and encouraging autonomy (framing the work as joint inquiry and inviting self-correction).

### Affordances
- (none yet linked)

### Personalization
- The specific phenomenon and equation are interchangeable; what matters structurally is that the student's own mechanistic reasoning precedes the formal equation, and that all three reading-comprehension levels are explicitly worked through rather than assumed once derivation succeeds.

## Related Patterns
- (none yet linked)

## Examples
- A high-school student researching wave velocity in liquids spent under 10 minutes deriving the phase-velocity equation v = (gλ/2π + σ/2πλρ)tanh(2πh/λ), but "hours and days" across three mentoring sessions working through what each term meant, why surface tension was negligible in his experimental conditions, and why velocity increased with depth — moving over the course of the year from "classic ADHD" disengagement (his 10th-grade teacher's description) to sustained, self-directed inquiry.

## Key Sources
- Kapon, S., & Schvartzer, M. (2024). Guided Inquiry into a Physics Equation. *Cognition and Instruction, 42*(1), 159-206. [https://doi.org/10.1080/07370008.2023.2197232](https://doi.org/10.1080/07370008.2023.2197232)
-->
