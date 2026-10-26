---
type: pattern
id: pair-c-framework
title: PAIR-C Framework (Pattern, Agents, Interactions, Relations, Causality)
description: "A reusable policy for teaching an emergent phenomenon (natural selection, collective behavior) by naming five dimensions on which decentralized, collective causation differs from sequential, individual causation and having learners use them while running an agent-based simulation; one quasi-experiment with pre-service teachers tests it, finding a near-transfer advantage over the same simulations without the framing, trends on deep understanding and misconceptions, and no far transfer."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
author: Su, Chi & Nagashima
grain_size: lesson
sources:
  - id: su-chi-nagashima-2026
    resource: "https://doi.org/10.1080/10508406.2025.2546471"
    title: "Su, M., Chi, M. T. H., & Nagashima, T. (2026). Applying the PAIR-C Framework to foster deep understanding and address misconceptions in science education. Journal of the Learning Sciences, 35(1), 130-175."
    author: "Su, M., Chi, M. T. H., & Nagashima, T."
---

# PAIR-C Framework (Pattern, Agents, Interactions, Relations, Causality)

> **Pattern** · [All patterns](index.md)
> **Evidence** · 13 claims (5 for, 7 mixed, 1 against) · 21 studies (8 causal, 5 quant-synthesis, 3 review, 2 qualitative, 2 theoretical, 1 design), `q1`–`q4` · 4 of 21 report an effect size · 8 claims rest on one study

## Description and scope

A reusable policy for teaching an **emergent phenomenon**: a system-wide pattern (a population's coloring changing over generations, an ant colony's foraging trail, a traffic jam) that arises from many decentralized, uncoordinated interactions with no agent in control. Learners commonly explain such phenomena with a sequential, individualistic causal schema (one agent causes the change, step by step, on purpose), which produces teleological ("the moths chose to change color") and anthropomorphic explanations. PAIR-C names five dimensions on which the two kinds of causal structure differ and has learners use them while they work with an agent-based simulation:

- **Pattern**: the macro-level, system-wide change;
- **Agents**: the individual entities, and whether control is centralized or decentralized;
- **Interactions**: whether interactions are uniform or random, simultaneous or serial, independent or dependent;
- **Relations**: how the interaction features combine and compare;
- **Causality**: how micro-level behavior sums to the macro-level pattern.

The policy is: **elicit each learner's explanation → introduce the five dimensions on an intuitive case → set emergent against sequential causal structure side by side → learners run an agent-based simulation with prompts framed on the dimensions → learners explain what they saw in the dimensions' terms → each stated misconception is answered by naming the dimension it violates → a second case, then a new phenomenon compared explicitly with the first**. The knowledge type is a `principle` (a causal model of how a kind of system works); the outcomes are `conceptual-understanding` of the inter-level mechanism, fewer misconceptions, `near-transfer` (the same concept in a new context) and `far-transfer` (an unrelated emergent phenomenon).

**One claim tests this pattern, and only partly.** In a single quasi-experiment with 50 pre-service teachers learning natural selection with NetLogo simulations, PAIR-C scaffolding beat traditional instruction using the same simulations on near-transfer gains; deep-understanding gains and the reduction in misconceptions favored PAIR-C but did not reach conventional significance; and neither group transferred to an unrelated emergent phenomenon ([PAIR-C scaffolding shows mixed evidence](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~M]). Persistence beyond the immediate posttest was not measured, and the claim page does not record how long the instruction ran. Everything else in the policy below (the session arc, the fading of prompts, the cross-domain comparison step, the responses to particular learner answers) is carried from neighbouring claims or is an untested proposal, and each step says which.

How the converted siblings sit beside this one. [Cognitive Disequilibrium](../principles/cognitive-disequilibrium.md) owns confronting a confident but inaccurate explanation and supporting its resolution; PAIR-C is one configuration of that, with the five dimensions as the resolving vocabulary. [Simulations and Immersive Virtual Environments](../principles/simulations-immersive-virtual-environments.md) owns practicing inside a simulation with guidance and debrief; here the simulation is used to make an invisible mechanism visible, not to rehearse a performance. [Inquiry-based Learning](../principles/inquiry-based-learning.md) and [Scaffolding](../principles/scaffolding.md) own guided inquiry and contingent support in general. [Transfer of Learning](../principles/transfer-of-learning.md) and [Analogical Reasoning](../principles/analogical-reasoning.md) own comparing cases to transfer a structure, which is the step this pattern's own study suggests is missing for far transfer. The [concept attainment pattern](concept-attainment.md) is the nearest converted pattern for teaching a category from contrasted instances. This page does not repeat their models.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Before any instruction, ask each learner to explain one emergent phenomenon in writing or aloud ("why are most moths in this sooty forest dark?"). Record the causal structure the explanation uses: an agent that wants or chooses, a single cause acting step by step, need-driven change, use and disuse, or decentralized variation and selection. Record prior knowledge of the domain and of simulations. Keep the answer rather than a label such as `novice`. |
| The phenomenon | Whether the target really is emergent (many agents, no controller, the pattern arising from their interactions) or a sequential process (digestion, a production line), which PAIR-C does not fit. Which simulation, video or physical model shows agent-level behavior. Which second phenomenon in another domain shares the structure. |
| Context and activities | Setting (`classroom`, `online-self-paced`, `online-instructor-led`, `workplace-clinical`), `single-session` or `days-weeks`, devices available (computers, phones only, none), group size, whether a teacher is present to answer misconceptions as they arise, minutes per session. |
| Learner-valued goal | Ask what the learner wants: to explain evolution to their own pupils, to pass a biology course, to understand a system at work (epidemics, markets, crowds). Record disagreement with the designer objective, and any belief the topic touches (natural selection can). |
| Designer objective | Which of these the assessment will weigh: explaining the target phenomenon at both levels, removing named misconceptions, applying the explanation to the same concept in a new context, or recognizing the same causal structure in a different phenomenon. |
| Outcome | Shallow items, deep (inter-level causal) items, near-transfer items, far-transfer items on an unrelated emergent phenomenon, and misconceptions coded from open explanations against a named set of categories, each scored apart; immediate or `delayed-retention`. The tested study used all five. |

A request to "use PAIR-C for evolution" does not specify these. Ask what phenomenon, which simulation, what learners currently say, and which transfer the assessment will weigh before choosing the arc below.

## Sequence and conditional policy

The default arc is the earlier page's six steps, spread over four sessions, with a seventh step proposed for far transfer. Minutes and the number of sessions are proposals; the claim page does not report the study's dose.

**Session 1 (about 50 minutes): from the learner's explanation to the dimensions.**

1. **Elicit** (5–10 min). Each learner writes an explanation of the target phenomenon before any teaching, and the teacher sorts them by causal structure (above). Evidence status: untested here; surfacing the prior explanation is the precondition [conflict-based instruction](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+S] works from (science conceptual learning in 218 studies, g = 1.10 for cognitive-conflict strategies, k = 150, with a small experiment finding that staged contradictions helped only learners who reported being confused).
2. **Introduce the five dimensions on an intuitive case** (10 min), such as ant pheromone trails: no ant directs the trail; it forms from many ants each following local cues. Evidence status: from the earlier page; part of the tested PAIR-C package, not isolated.
3. **Set emergent against sequential causal structure side by side** (10 min): a two-column table, one row per dimension (decentralized versus a single controlling agent; random, simultaneous interactions versus serial steps; converging, collective change versus incremental, cumulative change). Fill the sequential column from the learners' own explanations in step 1 where possible. Evidence status: part of the tested package; [comparing cases](../claims/comparing-contrasting-cases-improves-learning.md) [~M] found larger gains when the principle comes after a prompted comparison, though in one algebra study comparison raised procedural knowledge, not conceptual knowledge.
4. **Run the simulation with dimension-framed prompts** (20–25 min). Learners manipulate an agent-based model of the target (Peppered Moths, Rock Pocket Mice in NetLogo) with an annotated diagram or short video beside it marking agent-level events, and a prompt for each dimension ("Is any moth controlling the change? Point to where the color shift happens across the population"). Evidence status: tested as a package in [the PAIR-C study](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~M] against the same simulations without the framing; [guidance added to simulation-based inquiry](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M] improved learning outcomes (d = 0.49) and inquiry skills (d = 0.41) independent of guidance type, as reported second-hand in a review.

**Session 2 (about 40 minutes): explaining and correcting.**

5. **Structured reflection in the dimensions' terms** (15 min). Each learner rewrites their step 1 explanation, one sentence per dimension, then compares it with the original. Evidence status: from the earlier page; untested as a separate step.
6. **Answer each stated misconception by naming the dimension it violates** (throughout, and 15–20 min of targeted cases). "The moths chose to change color" → Agents: no moth controls the population's coloring; Interactions: variation is random, survival depends on each moth's match to the bark. Name the misconception, say why it is wrong, give the correct account. Evidence status: [instruction that confronts misconceptions](../claims/misconceptions-interfere-with-new-learning.md) [+S] (a meta-analysis and a two-decade review of refutation text, both read from abstracts) produced conceptual change more often than standard exposition; [contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M] outperformed fixed or absent support, mostly in one-to-one tutoring.

**Session 3 (about 40 minutes): a second case in the same domain, prompts faded.** A second simulation (Rock Pocket Mice after Peppered Moths). Prompts shrink from one per dimension to a single "which dimension explains what you just saw?" and then to none; learners write the five-dimension explanation unaided. Evidence status: fading is an untested proposal here. The study's significant result was on near transfer, which is what this session practises.

**Session 4 (about 40 minutes): a new phenomenon, compared explicitly.**

7. **Cross-domain comparison** (proposed addition). Give an emergent phenomenon from another domain (geese flight formation, a traffic jam, a forest-fire spread model) and have learners fill the same two-column table for it beside the natural-selection table, then state what the two share. Evidence status: untested for emergent phenomena. Neither group in the PAIR-C study transferred to an unrelated emergent phenomenon, and the claim page reports the authors' suggestion that explicit cross-domain analogical comparison may be needed; [comparing analogous cases](../claims/comparing-contrasting-cases-improves-learning.md) [+M] improved transfer of a principle with novice undergraduates (48% against 19% in a negotiation experiment), carried here to a different domain and a different kind of principle.

**When a learner moves on** (proposed, untested): from session 1–2 to session 3 when their rewritten explanation of the target names decentralized control and random variation without teleological or need-driven language; from session 3 to session 4 when they do so on the second case without prompts. A learner who still explains with a controlling agent after session 3 gets the one-to-one response in the table below, not a fourth simulation.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Teleological explanation persists after the simulation ("they adapted because they needed to") | Ask what a single moth did during its life that changed its color; then ask where in the simulation the population's coloring changed. | If they say the moth changed itself, they hold need-driven change: point to the Agents and Interactions rows and replay a run with selection off. If they say the population changed but still use "needed to" or "chose to", it may be wording, not model: ask them to restate without those words before acting. Neither branch tested. |
| Correct account of the target, but the second case is explained sequentially | Ask which dimension the two cases share and which they think differs. | If they think the cases differ in structure, set the two tables side by side (step 7). If they see the shared structure but misread the second simulation's display, teach the display. Untested. |
| Can recite the five dimensions, cannot apply them to an unseen phenomenon | Give a new phenomenon and ask only "is anything in control here?" | Recital without application is the pattern the study's absent far transfer would predict; add the cross-domain comparison rather than another round of the dimensions. Carried from [the PAIR-C study](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~M] and [comparing analogous cases](../claims/comparing-contrasting-cases-improves-learning.md) [+M]. |
| Learners watch the simulation without manipulating it, or change many settings at once | Ask what they expect if only one setting changes, before they run it. | Require a written prediction for each run; if the interface itself is the obstacle, demonstrate one run first. Proposed from the guidance evidence: [guidance in inquiry](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M]. |
| A pair reaches the correct account through one partner | Collect each partner's written explanation separately. | Reflect and rewrite individually; in the one qualitative study of pairs at a physics simulation, conceptual change came only for students who were engaged and prepared to reconstruct their own conceptions ([collaborative simulation work](../claims/cscl-simulation-conceptual-change-cognitive-engagement.md) [~W]). |

## Fitting the design to a situation

**The three facts that most change the decision:**

- **Whether the phenomenon is genuinely emergent.** The five dimensions exist to contrast decentralized, collective causation with sequential, individual causation; a sequential process gives the framework nothing to contrast. If unstated, ask: is there any agent controlling the outcome, or does it arise from many agents' local interactions?
- **Which transfer the assessment weighs.** The one study found a significant effect on near transfer only, and no far transfer in either group. If unstated, ask: will learners be tested on the same concept in a new context, or on a different phenomenon altogether?
- **What learners currently say, and who they are.** The tested learners were pre-service teachers; the misconceptions coded were teleological reasoning, anthropomorphism, directed variation and use-and-disuse. If unstated, ask: what does a learner write when asked to explain the phenomenon now, and how old are they?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are pre-service or practicing teachers (`adult`, `postsecondary`) learning natural selection | Run the default arc as given, with the NetLogo moths and mice; add step 7 if they must teach recognizing emergence to pupils. | [The PAIR-C study](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~M]: this population and domain, near transfer only |
| Learners are `adolescent` (secondary science) or younger | Keep the five dimensions but give each one a question in plain words and a picture; use one simulation per session; the teacher runs a demonstration run before learners take over. | Untested: the study's population was adults; [guidance in simulations](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M] reports age as a moderator without saying which way on its claim page |
| Learners are `novice` in the domain and with simulations | Add a 10-minute guided run of the interface before step 4; keep a prompt for every dimension through session 2; state the correct account at the end of session 1 rather than waiting for learners to reach it. | [Guidance in inquiry](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M], across inquiry studies, not this pattern |
| The goal is recognizing the same structure in other phenomena (`far-transfer`) | Do not stop after the target domain: add session 4's side-by-side comparison with a second, unrelated phenomenon, and test on a third. | Untested proposal; [the PAIR-C study](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~M] found no far transfer without it; [comparing analogous cases](../claims/comparing-contrasting-cases-improves-learning.md) [+M] carried from negotiation cases; [simulation games](../claims/simulation-near-transfer-robust-far-transfer-weak.md) [~W] support near transfer, far transfer less robust |
| The phenomenon is a sequential process (digestion, a production line) | Do not use PAIR-C; use the sequential column alone as an explanation frame, or a worked causal chain. | Untested; follows from the framework's own scope |
| Learners' reported errors are given ("the moths changed color to hide") | Use those exact sentences as the misconceptions in step 6 and as the sequential column in step 3. | [Instruction that confronts misconceptions](../claims/misconceptions-interfere-with-new-learning.md) [+S], science and reading studies, not this pattern |
| The brief names its own misconception categories, rubric or explanation template | Keep them; map each of the brief's categories to the dimension it violates rather than replacing them with the study's nine categories. | Untested |
| The brief names its own routine (its worksheet, prompts or exit ticket) | Keep it; change only what the evidence says matters: the side-by-side emergent/sequential contrast and one dimension-framed prompt per run. | Untested; the tested package bundled annotations, prompts and feedback, so no single feature is isolated |
| One teacher for 25–35 learners | Prepare a card per expected misconception with the dimension it violates and the correcting sentence; circulate during step 4 and answer from the cards; collect written explanations to read between sessions. | [Contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [~M]: evidence mostly from one-to-one tutoring, and the claim page notes that contingency across 30 students is hard |
| Scarce facilitator time (a busy teacher, a short check-in) | Put the dimension prompts and the misconception cards inside the simulation worksheet so learners self-check; spend the facilitator's minutes only on learners whose rewritten explanation still has a controlling agent. | Untested; [guidance in simulations](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M] found the effect independent of guidance type |
| `online-self-paced`, no teacher | Embed one prompt per dimension in the simulation page; require a written prediction before each run; show a model five-dimension explanation after the learner submits theirs; offer the misconception cards as feedback keyed to common answers. | [Guidance in simulations](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M], reported second-hand; untested for this pattern |
| Mixed mode: some learners remote, some in the room; or phone-only | Use one simulation shared on screen by the teacher with learners calling the settings; remote learners write explanations in a shared document; on phones, use a short video of runs with the agent-level events marked instead of the live model. | Untested proposal |
| `single-session` only (about 60 minutes) | Steps 1–6 in one session: elicit 5, dimensions on ants 8, contrast table 7, simulation with prompts 25, rewrite and correct 15; name in the plan that near transfer is the most this session can aim at. | Untested; minutes are proposals |
| A fixed short time budget (20–30 minutes) | Elicit 3, contrast table with the dimensions 7, one 10-minute run with prompts, rewrite 5; drop the ant example and the second case. | Untested |
| Low confidence or low literacy | Learners say or draw their explanations; the contrast table uses icons (one arrow from a controller against many small arrows); misconceptions are corrected in a private exchange, not in front of the class. | Untested |
| The topic touches beliefs learners hold privately (evolution, for some learners) | The learner decides who sees their explanation; the aim is to explain the mechanism the scientific account proposes, not to require assent; correct the model, not the learner's beliefs. | Untested |
| A whole-task performance the brief wants kept whole (explaining an unseen phenomenon, teaching a mini-lesson) | Assess with one whole explanation of a new phenomenon scored on the five dimensions, not split into separate items per dimension. | Untested |
| A product for a real audience (pre-service teachers designing a lesson for pupils) | Have them build the contrast table and misconception cards for their pupils as the product; the audience is the class they will teach. | Untested |
| High stakes, or assessment weeks later | Test at the delay that matters on new items, including a far-transfer phenomenon; do not reuse the practice simulations. | Untested; the study measured immediate gains only |

Eight of the nineteen rows cite a claim, each carried beyond the population or setting its claim page reports, as its Basis cell says; the other eleven are untested proposals.

## Choosing configurations from evidence

- **The pattern itself.** [PAIR-C scaffolding shows mixed evidence for deep understanding and reduced misconceptions in emergent-phenomena instruction](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~M]: a quasi-experiment (no random individual assignment) with 50 pre-service teachers (24 PAIR-C, 26 control), both groups using the same NetLogo simulations, assessed pre and post. Near-transfer gains favored PAIR-C (Condition × Time interaction F = 4.64, p = .036); deep-understanding gains (p = .059) and misconception reduction (p = .060 for categories, p = .095 for frequency) favored it without reaching p < .05; neither group achieved far transfer to geese flight formation. Coded `q2 · i1 · causal · r2`. A nonsignificant trend does not establish an effect, and nothing here tells which feature of the package (annotations, prompts, feedback) did the work.
- **Guidance with simulations and inquiry.** [Supplementing simulation-based inquiry with learner guidance modestly improves learning outcomes](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M] (d = 0.49 on learning outcomes, d = 0.41 on inquiry skills, independent of guidance type, reported from D'Angelo et al. through a review) and [Guidance during inquiry learning improves post-inquiry learning outcomes](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M] (a meta-analysis, d = 0.50; its table gathers 4 distinct studies, including the PAIR-C study as a qualifying one). These bear on whether to guide the simulation at all, not on PAIR-C's dimensions as the guidance.
- **Confronting the misconception.** [Instruction that confronts science misconceptions produces conceptual change more often than standard exposition](../claims/misconceptions-interfere-with-new-learning.md) [+S]: a meta-analysis and a review of refutation text, both read from abstracts, neither with a recorded pooled effect; its table gathers 4 distinct studies. [Conflict-based instruction improves science conceptual learning](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+S]: 218 studies, g = 1.10 (adjusted 0.93), with wide heterogeneity; its table gathers 5 distinct studies. The qualification on the same page: in one experiment contradictions helped only learners who reported being confused, and no study isolates disequilibrium as the mechanism. So name the misconception and resolve it; do not expect a surprising simulation run alone to do it.
- **Contingent correction.** [Contingent scaffolding improves learning more than fixed or absent support](../claims/contingent-scaffolding-improves-learning.md) [+M]: five studies, mostly one-to-one tutoring; its table gathers 20 distinct studies across narrower claims, including the PAIR-C study. Carried to a teacher answering misconceptions during simulation work.
- **Limits on transfer.** [Comparing analogous cases improves transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] (its table gathers 5 distinct studies) is the basis for the proposed cross-domain step and is untested on emergent phenomena. [Simulation games support near transfer, but evidence for long-term or far transfer is less robust](../claims/simulation-near-transfer-robust-far-transfer-weak.md) [~W] (a review citing meta-analyses) and [comparing cases raised procedural knowledge, not conceptual knowledge, in one algebra study](../claims/comparing-contrasting-cases-improves-learning.md) [~M] limit what to expect. [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [~M] adds that the approach presupposes prior knowledge to compare across cases, a reason to fix the target domain first and add the second phenomenon later.

Do not report PAIR-C as significantly improving deep understanding or reducing misconceptions: the claim page records trends. Do not rank it against other conceptual-change designs (refutation text, predict-observe-explain): no claim compares them. A precise abstention names the missing comparison (PAIR-C with and without a cross-domain comparison step, on far transfer and at a delay, with school-age learners) and the local observation that would stand in for it.

## The evidence by question

- *Does adding guidance to inquiry and simulation work improve what learners learn?* [Guidance during inquiry learning improves post-inquiry learning outcomes (d = 0.50)](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M]
- *Does instruction that names and confronts a science misconception change learners' conceptions more than standard exposition?* [Instruction that confronts science misconceptions (conceptual-conflict interventions, refutation text) produces conceptual change more often than standard exposition](../claims/misconceptions-interfere-with-new-learning.md) [+S]

## Further evidence, not yet read against this model

Every claim the earlier page cited is used in the model above: [the PAIR-C study](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~M] (the earlier page marked it [~W]) and [contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M]. Claims found in the search and read, but not used as core evidence:

- [Newell's complex systems theory of interdisciplinarity fails to explain integration](../claims/newell-complex-systems-theory-integration-gap.md) [~W]: a theoretical claim about interdisciplinary studies that shares the words "complex systems"; it does not bear on teaching emergent phenomena.
- [A demonstration-plus-guided-inquiry-plus-computational-model sequence helped most students predict increasing gravitational-wave frequency, but only about half predicted increasing amplitude](../claims/guided-inquiry-computational-model-overcomes-amplitude-misconception.md) [~W]: one classroom design report in high-school physics with no comparison; a reminder that a guided model sequence can leave one misconception in place while fixing another, not evidence for PAIR-C.

## Illustrative design instance and observation record

*Invented illustration, not a tested lesson.* A secondary biology department (`adolescent`, `classroom`, `days-weeks`, one teacher for 28 students, computers shared in pairs) wants students to explain antibiotic resistance and to recognize the same mechanism elsewhere. The teacher brings the students' own pre-unit answers, most saying "the bacteria got used to the antibiotic". The table changed the default: the plain-words version of each dimension; the students' sentences as the sequential column and as the misconception cards; a demonstration run before pairs use the simulation; individual rewrites after paired work; and a session 4 comparing resistance with peppered moths. A student says she wants to understand why her doctor told her to finish the course of tablets; the department's objective is the inter-level explanation. They agree to include one item on finishing a course of antibiotics in the far-transfer test, scored separately. The PAIR-C claim covers adults learning natural selection at an immediate posttest, not this age, phenomenon or horizon; these are local choices to observe, not settled ones.

Record: **phenomenon and why it is emergent → the second phenomenon used for comparison → each learner's starting explanation and its causal structure → simulation runs, settings changed, predictions made → prompts given and which dimension each named → misconceptions stated and the dimension used to answer each → rewritten explanation per session → prompts withdrawn and when → near- and far-transfer explanations, scored per dimension → candidate interpretations (model changed, wording changed only, recitation without application, partner's account copied) and their basis → reobservation at the stated delay**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical probabilities of conceptual change without a calibrated model.

## Elements and limits

[Simulation](../elements/simulation.md), [prediction](../elements/prediction.md), [prompts](../elements/prompts.md), [misconception probes](../elements/misconception-probes.md), [comparing cases](../elements/comparing-cases.md), [analogies](../elements/analogies.md), [feedback](../elements/feedback.md), [reflection activities](../elements/reflection-activities.md) and [visual imagery](../elements/visual-imagery.md). Principles the pattern draws on: [Cognitive Disequilibrium](../principles/cognitive-disequilibrium.md), [Simulations and Immersive Virtual Environments](../principles/simulations-immersive-virtual-environments.md), [Inquiry-based Learning](../principles/inquiry-based-learning.md), [Scaffolding](../principles/scaffolding.md), [Analogical Reasoning](../principles/analogical-reasoning.md) and [Transfer of Learning](../principles/transfer-of-learning.md). Theory: [Constructivism](../theories/constructivism.md).

This pattern is scoped to explaining one emergent phenomenon with an agent-based model and the five dimensions, at lesson and short-unit grain. Sequential processes and phenomena with a real controlling agent need other configurations. Whether PAIR-C produces deeper understanding or fewer misconceptions than other conceptual-change designs, whether it transfers across domains with an explicit comparison step, whether it works with school-age learners, and whether its gains last remain to be tested.

## Claims

- [The framework and recommendations are consensus positions from physical-science-weighted contributors, not empirical findings](../claims/open-knowledge-consensus-not-empirical.md) [-W]
- [The evolution teaching interventions significantly improved student understanding with effect sizes above the 0.40 implementation threshold in both tranches](../claims/evolution-sow-improve-understanding-large-effect.md) [+W]

## Related Patterns
- (none yet linked)

## Examples
- Pre-service teachers used PAIR-C-scaffolded NetLogo simulations (Peppered Moths, Rock Pocket Mice) to learn natural selection, contrasted with a traditional-instruction control group using the same simulations without the PAIR-C framing.

## Key Sources
- Su, M., Chi, M. T. H., & Nagashima, T. (2026). Applying the PAIR-C Framework to foster deep understanding and address misconceptions in science education. *Journal of the Learning Sciences, 35*(1), 130-175. [https://doi.org/10.1080/10508406.2025.2546471](https://doi.org/10.1080/10508406.2025.2546471)

<!-- deprecated 2026-10-15: superseded by the conditional model above. The previous body, kept verbatim.

## Description
PAIR-C is a scaffolding framework for teaching emergent phenomena — systems where a macro-level pattern (e.g., a species' traits changing over generations, an ant colony's foraging trails) arises from many decentralized, uncoordinated micro-level interactions with no controlling agent. Learners typically default to a sequential-process schema (a single agent causing change in a step-by-step, cumulative way) when reasoning about these phenomena, producing well-documented misconceptions such as teleological reasoning ("organisms choose to evolve") and anthropomorphism. PAIR-C makes the contrast between emergent and sequential causal structure explicit through five dimensions: **Pattern** (the macro-level, system-wide change), **Agents** (the individual entities involved, and whether control is centralized or decentralized), **Interactions** (whether agent interactions are uniform/random, simultaneous/serial, independent/dependent), **Relations** (how interaction features combine and compare), and **Causality** (how micro-level behavior sums to produce the macro-level pattern).

## Implications

### Context
#### Requirements
- A domain involving genuinely emergent (decentralized, collective) causal structure, ideally paired with an interactive simulation or agent-based model learners can manipulate
- Instruction that names and applies the five PAIR-C dimensions explicitly, rather than only presenting the correct causal story
#### Constraints
- Evidence so far comes from a single domain (natural selection) and did not produce far transfer to other emergent phenomena — [PAIR-C scaffolding shows mixed evidence for deep understanding and reduced misconceptions in emergent-phenomena instruction](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~W]
- Grain Size: lesson (a bounded instructional sequence around one simulation-based topic)

### Target Goals
- Deep, causal understanding of how micro-level, decentralized interactions produce macro-level emergent patterns
- Reducing misconceptions that come from over-applying sequential/individualistic causal schemas to emergent phenomena

### Target Learners
- Studied with pre-service teachers; the framework's target is any learner encountering emergent-systems content for the first time (e.g., natural selection, collective behavior, ecosystem dynamics)

### Theory
#### Supporting
- [Constructivism](../theories/constructivism.md) — learners construct causal schemas through guided contrast and interaction with a simulation, rather than by being told the correct explanation
#### Contradicting / Qualifying
- The source study found no far transfer to unrelated emergent phenomena, suggesting PAIR-C scaffolding alone may be insufficient without explicit cross-domain analogical comparison

### Claims
- [PAIR-C scaffolding shows mixed evidence for deep understanding and reduced misconceptions in emergent-phenomena instruction](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~W]

## Design

### Sequence
1. Introduce the five PAIR-C dimensions with a concrete, intuitive example (e.g., ant pheromone trails).
2. Explicitly contrast emergent-process features (decentralized control, converging change, collective summing) with sequential-process features (a single controlling agent, incremental/cumulative change).
3. Provide visual scaffolds (annotated diagrams or video) highlighting agent-level interactions and their cumulative effect.
4. Have learners manipulate an agent-based simulation of the target phenomenon (e.g., a natural-selection model) while observing which macro-level features emerge without any agent directly controlling them.
5. Use structured reflection prompts that connect learners' observations back to the PAIR-C dimensions.
6. When learners state a misconception (e.g., "the moths chose to change color"), correct it by pointing to the relevant PAIR-C feature it violates (e.g., "no controlling agent," "random variation").

### Affordances
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]

## Related Patterns
- (none yet linked)

## Examples
- Pre-service teachers used PAIR-C-scaffolded NetLogo simulations (Peppered Moths, Rock Pocket Mice) to learn natural selection, contrasted with a traditional-instruction control group using the same simulations without the PAIR-C framing.

## Key Sources
- Su, M., Chi, M. T. H., & Nagashima, T. (2026). Applying the PAIR-C Framework to foster deep understanding and address misconceptions in science education. *Journal of the Learning Sciences, 35*(1), 130-175. [https://doi.org/10.1080/10508406.2025.2546471](https://doi.org/10.1080/10508406.2025.2546471)
-->
