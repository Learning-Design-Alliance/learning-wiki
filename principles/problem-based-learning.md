---
type: principle
id: problem-based-learning
moved_from: [pattern/problem-centered-task-level-progression-pattern]
aliases: [real-world-problem-solving-maker-context]
title: Problem-based Learning
description: "For learners who must apply knowledge to ill-structured problems, organizing work around problems has a small, highly variable and possibly inflated average effect; what is better supported is guidance for novices on the target content, with a problem-first phase as a narrower option followed by instruction."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
sources:
  - id: thorndahl-2020
    resource: "https://doi.org/10.14434/ijpbl.v14i1.28773"
    title: "Thorndahl, K., & Stentoft, D. (2020). Thinking critically about critical thinking and problem-based learning in higher education: A scoping review. *The Interdisciplinary Journal of Problem-Based Learning, 14*(1)"
    author: "Thorndahl, K., & Stentoft, D"
  - id: lin-2017
    resource: "https://doi.org/10.11114/jets.v5i6.2320"
    title: "Lin, L. F. (2017). Impacts of the problem-based learning pedagogy on English learners' reading comprehension, strategy use, and active learning attitudes. *Journal of Education and Training Studies, 5*(6), 109-125"
    author: Lin, L. F
  - id: molenda-2002
    resource: "https://eric.ed.gov/?id=ED470983"
    title: "Molenda, Michael. (2002). A New Framework for Teaching in the Cognitive Domain. ERIC Digest. https://eric.ed.gov/?id=ED470983"
    author: Molenda, Michael
  - id: lundberg-2018
    resource: "https://eric.ed.gov/?id=EJ1179517"
    title: "Lundberg, M., & Rasmussen, J. (2018). Foundational Principles and Practices to Consider in Assessing Maker Education. i-manager's Journal of Educational Technology, Vol. 14 No. 4, January - March 2018. https://eric.ed.gov/?id=EJ1179517"
    author: "Lundberg, M., & Rasmussen, J"
---

# Problem-based Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 64 claims (21 for, 38 mixed, 5 against) · 54 studies (13 quant-synthesis, 11 review, 10 causal, 8 qualitative, 6 theoretical, 4 associational, 2 design), `q1`–`q4` · 10 of 54 report an effect size · 59 claims rest on one study

## Conditional relationship

Problem-based learning (PBL) organizes learning around ill-structured or authentic problems that learners investigate, usually in small groups with a facilitator. Read the evidence in two layers.

**As a curriculum format, its average effect is small and unreliable.** The best-documented synthesis in the wiki, a re-analysis of a PBL meta-analysis of 353 outcomes, reports a modest overall effect (g = 0.27) with large heterogeneity, individual outcomes from g = −1.26 to g = 1.91, publication bias that would shrink the effect to about g = 0.10, and no tutor-background category that predicts learning. So "use PBL" is not, by itself, a decision the evidence supports or rules out: what varies between implementations matters more than the label.

**Within a problem-centred design, guidance is the better-supported lever.** For a learner who is a `novice` on the target relation, leaving essential content to be discovered without support learns less than explicit instruction, while discovery with feedback, worked examples or scaffolding does better than other instruction. Starting with a problem *before* instruction is a narrower configuration (productive failure): it has meta-analytic support for conceptual knowledge and transfer when instruction follows, no procedural advantage, a reversal for second- to fifth-grade `child` learners, and is reported most reliably in well-structured domains. It is not evidence that open problems help novices learn content on their own.

The relationship is therefore conditional on the learner's starting knowledge of the target content, on the guidance and consolidation provided, on the outcome chosen (conceptual, transfer, procedural, product) and on the horizon. The [pattern](../patterns/problem-based-learning.md) specifies a reusable design policy; its local diagnostic branches remain proposals.

## Fitting the design to a situation

Ask for four facts when the brief omits them: **what do learners already know of the content the problem needs?**, **is the outcome basic knowledge, or understanding and transfer?**, **how old are the learners?**, and **will explicit instruction consolidate the problem work?**

| If the brief says… | Then change… | Basis |
|---|---|---|
| The plan is to convert a whole course or curriculum to PBL and expects a clear gain | Promise no gain from the label; the average effect is small (g = 0.27), ranges from strongly negative to strongly positive, and may be overstated by publication bias. Specify the guidance and consolidation and evaluate that configuration, recording how faithfully each group's sessions follow it | [The overall PBL effect is modest with large heterogeneity](../claims/pbl-overall-effect-modest-large-heterogeneity.md) [~M]; Publication bias in the same data [~M]; [An older review's equivocal results on knowledge and clinical reasoning, attributed to how faithfully programmes implement PBL](../claims/pbl-evidence-base-equivocal.md) [~W] (second-hand, in an essay) |
| The outcome that matters is basic factual knowledge on an exam soon after the unit (for example, a board or licensing exam) | Do not rely on problem work alone for it; add explicit teaching and practice of the knowledge base, timed for the exam. If retention months later matters too, measure it separately: the two horizons have pointed different ways | [PBL: null or negative on basic knowledge, positive on understanding and transfer](../claims/pbl-null-basic-knowledge-positive-transfer.md) [~M]; [Traditional instruction did better for short-term retention on standardized board exams](../claims/traditional-instruction-short-term-retention-board-exams.md) [-W]; [PBL did better for long-term retention](../claims/pbl-superior-long-term-retention.md) [+W] (both from one meta-synthesis of meta-analyses, no effect sizes in the text available) |
| The outcome is conceptual understanding and transfer | Use a problem-centred design with consolidating instruction afterwards | [PBL: positive on understanding and transfer](../claims/pbl-null-basic-knowledge-positive-transfer.md) [+M]; [Problem-first improves conceptual learning when instruction follows](../claims/productive-failure-improves-conceptual-learning.md) [+M] |
| Learners are novices on the content the problem needs | Make that content explicit (explanation, worked examples) before or alongside the problem; leaving it to be found unsupported learns less | [Minimal guidance is less effective for novices](../claims/minimal-guidance-less-effective-for-novices.md) [-M]; [Worked examples reduce novice search](../claims/worked-examples-reduce-novice-search.md) [+M] |
| Learners already have strong knowledge of the domain | Lower the guidance and give more open problems, checking on an unaided task first | [The advantage of guidance recedes with high prior knowledge](../claims/guidance-advantage-recedes-with-high-prior-knowledge.md) [~W] (a review's argument) |
| Learners are in the early primary years and the plan is problem-first | Teach first and use the problem as application | [PS-I effects are negative for 2nd–5th graders and rise with age](../claims/psi-effect-increases-with-grade-level.md) [-M] |
| Facilitators are not content experts (or the brief insists they must be) | Do not choose tutors on content background alone; prepare every facilitator in the guidance and consolidation moves | [Tutor background did not predict learning](../claims/tutor-background-meta-regression-not-predictive.md) [~M] |
| Small groups, each with a facilitator | Have facilitators raise support after a failed step and lower it after success, rather than give fixed hints | [Contingent scaffolding improves learning](../claims/contingent-scaffolding-improves-learning.md) [+M] (one-to-one tutoring, not PBL groups) |
| Tutorial groups are large | Split them into small or medium groups for the problem work; do not run the self-directed phase as one large group | [Small and medium tutorial groups gained self-directed-learning readiness; large groups declined](../claims/tutorial-group-size-moderates-sdl.md) [~W] (one pre–post study reported in a review; a self-report scale, not achievement) |
| To save time, learners will be handed the learning issues for each problem | Let each group generate its own learning issues from the problem, with the facilitator checking that they reach the target content | [Groups that generated their own learning issues studied more materials and spent more time on self-study](../claims/self-generated-learning-issues-benefit-pbl.md) [+W] (one experiment reported in a review; study behaviour, no achievement outcome) |
| Content is taught in lectures running alongside the problem sessions | Write problems the lectured content informs but does not settle, and ask for questions and challenges rather than a summary of the lecture | [More lecture coverage went with less critical discussion in PBL sessions, but more willingness to speak](../claims/scope-of-pbl-implementation-shapes-discussion.md) [~W] (one qualitative cross-curriculum study) |
| Groups will work together over several weeks (online or face to face) | Set up how the group plans, monitors and shares work in the first sessions, since groups' regulation settled early and rarely changed; online, re-launch the group's script part-way through | [Most groups settled into stable regulatory patterns early, with little change](../claims/stable-early-regulatory-patterns-limited-change.md) [~W] (one sequence-analysis study of collaborative groups); [Online PBL groups drifted from the scripted sequence to social bonding](../claims/pbl-group-sequence-derails-to-social.md) [~W]; the early set-up and re-launch are untested proposals |
| AI tools (a generative chatbot, an adaptive tutor) will be added to the problem work | Embed the tool in facilitator-guided problem work rather than leave it as an open answer source; check that learners can already use the tool fluently; evaluate the AI-supported configuration as a whole, on individual outcomes | [Benefits of generative AI in medical case- and problem-based learning appeared when it was embedded in faculty-guided work; in one pilot, open access to a language model did not improve accuracy and disrupted teamwork](../claims/genai-cbl-faculty-guided-conditional-benefits.md) [~W] (a scoping review); [AI-supported PBL gave high normalised gains against a control group's low gains](../claims/ai-pbl-high-ngain-versus-control-low.md) [~W] (one quasi-experiment, which cannot separate the AI from the PBL); [Years of coding experience went with higher scores in AI-supported PBL](../claims/coding-experience-associated-with-pbl-performance.md) [~W] (exploratory, one course); a review of 50 studies lists as themes that [AI supports educator–student collaboration through feedback and scaffolding](../claims/ai-pbl-enhances-educator-student-collaboration.md) [~W] and [adaptive, personalised learning linked to engagement and problem solving](../claims/ai-pbl-adaptive-personalized-engagement.md) [~W], with no comparisons on the claim pages; [Adult learners expect AI to activate background knowledge and sharpen their questioning](../claims/ai-supports-problem-centered-critical-thinking.md) [+W] (20 interviews; expectations, not outcomes) |
| The goal is application of a skill, and a participatory simulation is an option | Expect the simulation to give larger application gains and PBL larger knowledge gains, in one trial with 54 seventh and eighth graders; choose by the outcome that matters | [Simulation gave larger application gains](../claims/simulation-larger-application-gains.md) [~W]; [PBL gave larger knowledge gains](../claims/problem-based-larger-knowledge-gains.md) [~W] |
| The learners are adult professionals in a preparation programme (for example school leaders) | Tie the problems to the learners' own practice through fieldwork, not only to classroom cases | [Problem-based learning connecting coursework and practice](../claims/problem-based-principal-preparation-self-efficacy.md) [+W] |
| Collaboration skills are a goal | Ask learners to reflect in writing on how the group worked, and prompt for thinking processes, which learners rarely mention unprompted | [PBL students named valuing others' perspectives and interdependence](../claims/pbl-attitudes-valuing-interdependence-self.md) [+W]; [Students rarely referred to higher-level processing benefits](../claims/minimal-reference-higher-level-processing-benefits.md) [~W] |
| Every problem product will be graded | Keep the problem phase low-stakes and grade the individual consolidation and transfer tasks | untested proposal |

## Observation, state and explanation

Record what the learner does with a stated problem **under stated conditions**: what they identify as the question, what they say they need to know, which resources they consult, which solutions they generate, what help they receive and from whom, and what they produce. "Ready for open problems" is an inferred state, not an observation. Activity, talk volume and enthusiasm are observations of participation; none directly measures whether the target concept was learned. [Engagement is reported higher during PBL than during traditional instruction](../claims/pbl-engagement-higher-than-traditional.md) [+W] (second-hand, in a scaffolding framework), so expect it, and do not read it as learning. In a group, a shared product does not show what each member can do.

Activation of prior knowledge, noticing gaps and comparing one's own solutions with the canonical one are explanatory hypotheses offered by the claims below; they have not been observed directly in the studies the wiki records.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Novice on the target content, given an open problem to learn it from | Missing the content the problem needs; problem too hard to generate partial solutions; access or language demand | Ask for the key relation directly in a short probe; if absent, teach it (explanation, worked example) before or alongside the problem and observe whether the problem work then uses it. |
| Cannot start: no question framed, no learning issues listed | Missing task-specific knowledge to enter the problem; problem framed in unfamiliar language or representation; unclear what a product should look like | Ask for a first decision with a short prompt in a familiar representation; show the form of a finished product without its content; record whether either releases a start. |
| Busy and engaged, but the product shows little use of the target concept | Productive generation that awaits consolidation; floundering search without schema; target concept not actually needed by the problem as posed | Ask the learner to name the idea their solution depends on; check whether a correct solution to the problem as written requires the target concept at all. |
| Group discussion is fluent explanation-building, with little checking against the problem's data | The group is theorising ahead of its evidence; members are reasoning privately and the talk shows only part of it; the problem gives too few data to check against | Ask which facts in the problem the explanation does not yet account for, and ask each member privately what they are unsure of. In one tutorial group, [discussion during problem analysis was mainly theory building, with less data exploration and meta-reasoning](../claims/pbl-discussion-mainly-theory-building.md) [~W] (one qualitative study). |
| Group product strong, individual explanation weak | Work carried by one or two members; learning distributed but not yet individually consolidated; explanation probe harder than the task | Ask each learner for an individual explanation or a changed-condition problem under matched conditions; record who did what during the problem phase. |
| Generates several flawed solutions, then learns quickly from instruction | Problem-first preparation, as productive-failure accounts propose; instruction alone would have sufficed; extra time on task | Only a comparison with an instruction-first condition of matched time can attribute the gain; a single learner's trajectory cannot. |
| Succeeds on a conceptual probe, fails a routine procedure (or the reverse) | Different outcomes from the same sequence; procedure not practised; probe misaligned with what was taught | Score procedural and conceptual items separately, at the same horizon, and preserve both. |

These rows are proposals, untested with learners. A probe can shift confidence among the explanations; it does not identify a cause on its own. The probe itself is a learning exposure and should be recorded as one.

## Evidence and qualifications

- [The overall PBL effect in a tutor-background meta-analysis is modest, with large heterogeneity](../claims/pbl-overall-effect-modest-large-heterogeneity.md) [~M]: a re-analysis ([Walker & Leary, 2023](https://doi.org/10.14434/ijpbl.v17i2.35844)) of the Leary et al. (2013) data, 353 outcomes, reports g = 0.27 with I² = 80% of variability attributable to heterogeneity; [individual outcomes range from g = −1.26 to g = 1.91](../claims/massive-range-pbl-outcome-effect-sizes.md) [~M]. Not yet checked against its source. It does not predict the effect of any one PBL implementation, and the claim pages do not report learners, comparators or horizons by outcome.
- Publication bias in the same data [~M]: a funnel plot and Egger's test indicate publication bias, and trim-and-fill drops the overall effect to g = 0.103. Treat the average as possibly overstated.
- [Tutor background does not predict learning](../claims/tutor-background-meta-regression-not-predictive.md) [~M]: in a meta-regression with content novices as the reference, no tutor-expertise category predicted student learning (R² = .01, p = .14), and [the largest subgroup difference was not significant](../claims/tutor-background-meta-regression-not-predictive.md) [~M]. A nonsignificant moderator is not evidence that facilitation does not matter; it says tutors' credentials alone did not explain the variation.
- [A small meta-analysis reports a large pooled effect on achievement](../claims/pbl-large-positive-effect-academic-achievement.md) [+W]: five studies, random-effects ES = 1.560 (95% CI 0.768–2.353), heterogeneous; the claim page records that the article describes its z-test as not significant (z = 3.859; p > .05), which is internally inconsistent. Do not weigh it against the 353-outcome synthesis.
- [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [-S]: a meta-analysis of 580 comparisons found explicit instruction outperformed unassisted discovery (d = 0.38 favouring explicit instruction), while 360 comparisons found enhanced or assisted discovery (feedback, worked examples, scaffolding, elicited explanations) outperformed other instruction. An experiment with 112 third- and fourth-grade `novice` children (the claim page does not say how they were assigned) found many more mastered the control-of-variables procedure under direct instruction, and those taught directly did as well on a later transfer task as the few who discovered it. The Klahr & Nigam entry passes the judge; the registry attaches the wrong abstract to the meta-analysis (recorded as a registry problem), and the narrative review is unsettled. This bounds the principle: it predicts poor learning when PBL means leaving novices to discover essential content unsupported, not that guided problem work fails. The claim page does not break the meta-analytic result down by prior knowledge.
- [More teacher guidance within inquiry goes with larger advantages over traditional instruction](../claims/teacher-guided-inquiry-larger-effects.md) [+M]: a review of inquiry-learning syntheses reports one science meta-analysis with d = 0.25 for minimal-guidance inquiry over traditional instruction against d = 0.65 for teacher-directed inquiry, and a second meta-analysis finding only g = 0.15 for more over less guided inquiry. Both second-hand, about inquiry rather than PBL specifically; they point the same way as the default (guide the problem work) but disagree on how much it buys.
- [Practising whole complex tasks is argued to favour transfer](../claims/whole-task-performance-improves-transfer.md) [+W]: a training-design argument, the rationale for posing a whole problem rather than its parts; no study comparing whole-task with part-task practice is recorded on that claim, and the [pattern](../patterns/problem-based-learning.md) records one experiment in which absolute novices did better with isolated parts first.
- [Productive Failure Improves Conceptual Learning](../claims/productive-failure-improves-conceptual-learning.md) [~S]: a three-level meta-analysis (`synthesis-mixed`: experimental and quasi-experimental comparisons, 53 studies, 166 comparisons) set problem solving followed by instruction against the same instruction taught first. It favoured problem-first on conceptual knowledge and transfer (g = 0.36) and found no difference on procedural knowledge (g = −0.03); the advantage was larger for implementations following productive-failure design criteria (generating multiple solutions, group work, instruction building on student solutions) and reversed for second to fifth graders and for domain-general skills. One entry passes the judge on its abstract; the synthesis entry is unsettled on its abstract. It does not predict an advantage for problem-first work with no subsequent instruction, for young children, or on procedural fluency, and the claim page reports no delayed-horizon breakdown. Marked `~` because its support for problem-first work is conditional on instruction following and on learner age.
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]: one-to-one tutoring studies in which support was adjusted to each learner response outperformed fixed, moderate or no support on immediate and one-month tests of long division (N = 8 per condition), and interactive tutoring gave similar immediate learning but better transfer; a dynamic-assessment synthesis ranked scaffolding above coaching but below explicit strategy training. None of its three judged entries passes; they could not be confirmed on their abstracts. Its evidence comes mostly from one-to-one tutoring, not from facilitated PBL groups, so it supplies a candidate facilitation policy rather than a tested PBL result.
- [Case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [~M]: in one community-college biology cohort (n = 56; a non-randomized within-cohort comparison of matched topics), case-taught topics scored higher on course exams; a systematic review of 104 papers in health professional education (it passes the judge) concluded that students enjoy case-based learning but the evidence on learning compared with other activities is inconclusive, and that any benefit of small-group case work may come from the group work rather than the cases. It does not establish an advantage for authentic-problem formats in general and does not report delayed outcomes.

Retain learner age and starting knowledge, the exact comparator (instruction-first, lecture, unassisted discovery), the amount and timing of guidance, time on task, outcome type and horizon when transporting these results. A pooled g over unlike implementations is not a forecast for one class or one learner, and a nonsignificant procedural difference does not establish equivalence.

## The evidence by question

Each question below links a general claim that gathers the studies behind it into one table, one row per distinct study, with each study's design and effect as recorded and no averaged verdict (`eval/synthesis/problem-based-learning.json`, `scripts/synthesize_claim.py`). The count is of distinct studies across the claim and the narrower claims that bear on it.

- Does PBL as a curriculum format raise achievement over conventional instruction, and how reliably? [The overall effect of PBL in the tutor-background meta-analysis is modest (g = 0.27) with large, statistically significant heterogeneity](../claims/pbl-overall-effect-modest-large-heterogeneity.md) [~M]: 4 distinct studies.
- For which outcomes: basic knowledge, application and transfer, or professional skills? [Problem-based learning shows null or negative effects on basic knowledge acquisition but positive effects on conceptual understanding and transfer relative to direct instruction](../claims/pbl-null-basic-knowledge-positive-transfer.md) [~M]: 3 distinct studies.
- How much guidance do novices need inside a problem-centred design? [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [-S]: 13 distinct studies.
- What do learners say they learn about collaboration from PBL? [Teacher education students in PBL identified valuing others' perspectives, interdependence, and learning about self as attitudes necessary for collaborative learning](../claims/pbl-attitudes-valuing-interdependence-self.md) [~M]: 2 distinct studies.
- Where is the research on PBL thin? [A review found considerable research on flexible knowledge, problem solving and self-directed learning, little on collaboration and motivation, and minimal outside medical and gifted education](../claims/pbl-evidence-uneven-across-goals.md) [~W].

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M] — read 2026-10-19: the one experiment is high-school writing revision, not problem-based work; it suggests framing a novice's goal for the problem as the investigative process rather than the finished solution, but nothing recorded tests that in PBL, so it does not change the model.
- [Ways of dealing with anomalous data, and the conditions determining them, can be described during PBL problem analysis](../claims/anomalous-data-handling-conditions-pbl.md) [~W] — read 2026-10-19: the claim page records only that these could be described from stimulated recall, not what they were, so it gives the model nothing to act on.
- [The PBL assumption that student-generated learning issues guide self-directed learning had never been empirically tested before this study](../claims/pbl-learning-issues-assumption-untested.md) [~W] — read 2026-10-19: a framing statement from Dolmans et al. (1994); the claim page does not record the study's result.
- [Despite extensive research on PBL, there is heated debate about its effectiveness](../claims/heated-debate-pbl-effectiveness.md) [~W] — read 2026-10-19: the authors' motivating sentence, with no evidence of its own; the model already plans for a variable effect.
- [PBL offers potential to help students develop flexible understanding and lifelong learning skills](../claims/pbl-potential-flexible-understanding-lifelong-learning.md) [~W] — read 2026-10-19: a review's statement of potential, not a measured effect.
- [Learning through the experience of solving problems can build both content knowledge and thinking strategies](../claims/problem-experience-builds-content-and-thinking-strategies.md) [+W] — read 2026-10-19: the review's theoretical rationale for PBL, not a test of any configuration.
- [Review synthesis: explicit teaching matters, but its advantage over other approaches varies by context and structure](../claims/explicit-instruction-context-dependent-synthesis.md) [~W] — read 2026-10-19 (not about this page): a narrative review of four studies of explicit grammar teaching for second-language learners; no problem-based condition.
- [Publication-bias checks indicate the pooled effect is unlikely to result from publication bias](../claims/srl-meta-analysis-publication-bias-absent.md) [~W] — read 2026-10-19 (not about this page): the bias check of a meta-analysis of self-regulated learning strategies ([Ergen & Kanadli 2017](https://doi.org/10.14689/ejer.2017.69.4)), not of PBL; it says nothing about the PBL publication bias recorded above.

On 2026-10-19 (wave 2) the other claims linked here were read and moved into the model: worked examples (already in the novice row), whole-task practice and teacher-guided inquiry (evidence and qualifications), the short- and long-term retention pair (the basic-knowledge row), the equivocal-evidence essay (the curriculum row), engagement and theory-building discussion (observation), the evidence-gaps review (by question), and the rows on group size, learning issues, lectures alongside PBL, groups working over several weeks, and AI tools.
- [Spontaneous responsiveness to real-world events in PBL can deepen student-directed inquiry beyond what designed curriculum achieves](../claims/spontaneous-authenticity-in-pbl-deepens-student-directed-inquiry.md) [+W]
- [In one extreme case, two sixth-graders with a choice-rich, ungraded STEAM infrastructure extended a game-design challenge into a year-long self-directed project well beyond its designed scope](../claims/choice-rich-infrastructure-supports-productive-deviation-and-learning.md) [+W]
- [Students rated real-world projects and discussions with structured or guiding questions as the most beneficial learner-to-content strategies](../claims/real-world-projects-structured-questions-top-content-strategies.md) [+W]
- [Talladega County Schools' graduation rate rose from just above 70 percent in 2008 to 93 percent after its transition to project-based learning supported by digital technologies](../claims/talladega-graduation-rate-70-to-93-pbl-digital.md) [+W]

## Objective and learner-valued goal

Ask what the learner wants from the problem, and why, separately from the designer's objective. A problem chosen for its authenticity to the designer may not be one the learner cares about, and a learner's interest in solving the problem may diverge from the designer's interest in a concept the problem is meant to carry. Agreement, divergence and uncertainty are observations; engagement during the problem phase does not establish that the learner values the target capability. Choose a representative instrument, criterion, permitted resources and horizon for each outcome that matters: conceptual understanding, transfer, procedural fluency and the quality of the product are different claims.

For example, a nursing student may value making a safe decision for the patient in a case, while the designer's objective is that the student can explain the physiological principle the case was built around. A correct group care plan cannot establish either the individual decision or the explanation. The pattern shows how to record both aims and test the one each party cares about.

## What would revise this model?

The problem-first expectation should weaken if comparable learners, with comparable consolidation instruction and time, fail to show a conceptual or transfer advantage over instruction-first sequences on aligned measures, or if the advantage disappears at a delayed horizon. If younger learners, domain-general skills or other populations repeatedly show the reversal recorded in the synthesis, narrow the principle to the populations where it holds. If matched-time comparisons attribute PBL gains to group work, feedback or extra time rather than to the problem-first order, revise the explanation. Do not protect the model by relabelling every failure as poor facilitation or insufficient authenticity after the fact.

An engaging problem phase, an immediate conceptual gain, delayed retention, transfer to practice and the learner's valued use are separate claims. The evidence recorded here does not establish an optimal amount of guidance, a readiness threshold for open problems, or the effect of whole PBL curricula against conventional instruction.

At the curriculum level, the expectation of a small and variable average should change if bias-corrected syntheses with stated comparators and horizons show a consistent effect, or if moderators (guidance, consolidation, prior knowledge, outcome type) are found that explain the variation.

## Claims

- [Student-centered, problem-driven learning has a small, positive, heterogeneous effect on students' motivation compared to teacher-centered instruction (d = 0.498)](../claims/problem-driven-learning-small-positive-effect-motivation.md) [~W]
- [Scaffolding effects in PBL are higher in Engineering, Technology, and Mathematics than in Science, and relatively low in integrated STEM education](../claims/discipline-moderator-scaffolding-effects-bma.md) [~W]
- [Metacognitive and strategic scaffolding show larger effects in PBL-STEM than conceptual scaffolding](../claims/scaffolding-intervention-type-moderator-bma.md) [~W]
- [Scientific discipline does not significantly moderate PBL’s effect on secondary science achievement](../claims/pbl-discipline-moderator-no-significant-difference.md) [~W]
- [Effect sizes of PBL on science achievement differ significantly by publication type, with conference proceedings showing a negative effect](../claims/pbl-effect-differs-by-publication-type.md) [~W]
- [PBL effect sizes on science achievement do not differ significantly across educational levels](../claims/pbl-effect-similar-across-educational-levels.md) [~W]
- [Grade level (JHS vs SHS) does not significantly moderate PBL’s effect on science achievement, though the SHS effect size is descriptively larger](../claims/pbl-grade-level-moderator-no-significant-difference.md) [~W]
- [PBL effect sizes on science achievement do not differ significantly between studies conducted in Turkey and abroad](../claims/pbl-effect-similar-national-vs-international.md) [~W]
- [PBL has a large and positive effect (ES = .871) on secondary students’ achievement in science compared with conventional teaching](../claims/pbl-large-positive-effect-secondary-science-achievement.md) [-W]
- [PBL combined with virtual simulation improved theoretical knowledge and practical skills in clinical biochemistry](../claims/pbl-virtual-simulation-improves-theory-and-skills.md) [+W]
- [Problem-based learning in orthodontic postgraduate education enhances student engagement and understanding](../claims/problem-based-learning-enhances-orthodontic-engagement.md) [+W]
- [3D + PBL improves communication ability in orthopedic education](../claims/3d-pbl-improves-communication-ability-orthopedics.md) [+W]
- [3D + PBL improves passing rate of exams in orthopedic education](../claims/3d-pbl-improves-exam-passing-rate.md) [~W]
- [Publication bias is present in studies of theoretical scores comparing 3D + PBL with LBL](../claims/publication-bias-theoretical-scores-3d-pbl.md) [-W]
- [Of 4310 screened abstracts, 21 studies of PBL in PGME were included, spanning eight specialties and four Kirkpatrick outcome levels](../claims/pbl-pgme-21-studies-kirkpatrick-coverage.md) [+M]
- [PBL and active learning activities promote SDL while lectures and tests deter it, though evidence is inconsistent](../claims/pbl-promotes-sdl-lectures-deter.md) [~W]

## Related Principles
- [Inquiry-based Learning](inquiry-based-learning.md) — PBL is one inquiry form centered on authentic problems.
- [Experiential Learning](experiential-learning.md) — problem-centered work often provides the concrete experience that later reflection builds on.
- [Authentic Audiences & Purposes](authentic-audiences-purposes.md) — real stakeholders or consequences often strengthen PBL design.
- [Guided Practice](guided-practice.md) — novices often need coached practice with inquiry and problem-solving moves inside PBL.
- [Real-world Math](cultural-life-experiences-connections.md)
- [Provide student choice to build ownership and self-efficacy in maker education](autonomy.md)

## Examples
- **Community issue investigation**: Learners analyze a local problem, gather evidence, and propose responses.
- **Case-based team problem solving**: Small groups work through a realistic professional dilemma with incomplete information.
- **Design challenge**: Learners create and defend a solution to a practical constraint-based problem.
- **Cross-disciplinary PBL module**: Learners integrate literacy, numeracy, and research skills to address a shared problem.

## Key Sources
- Marra, R. M., Jonassen, D. H., Palmer, B., & Luft, S. (2014). Why problem-based learning works: Theoretical foundations. *Journal on Excellence in College Teaching, 25*(3-4), 221-238.
- Thorndahl, K., & Stentoft, D. (2020). Thinking critically about critical thinking and problem-based learning in higher education: A scoping review. *The Interdisciplinary Journal of Problem-Based Learning, 14*(1). [https://doi.org/10.14434/ijpbl.v14i1.28773](https://doi.org/10.14434/ijpbl.v14i1.28773)
- Lin, L. F. (2017). Impacts of the problem-based learning pedagogy on English learners' reading comprehension, strategy use, and active learning attitudes. *Journal of Education and Training Studies, 5*(6), 109-125. [https://doi.org/10.11114/jets.v5i6.2320](https://doi.org/10.11114/jets.v5i6.2320)
- Savery, J. R. (2019). Overview of problem-based learning: Definitions and distinctions. In R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/overview_of_problem_based_learning](https://edtechbooks.org/lidtfoundations/overview_of_problem_based_learning)
- Molenda, Michael. (2002). A New Framework for Teaching in the Cognitive Domain. ERIC Digest. https://eric.ed.gov/?id=ED470983
- Lundberg, M., & Rasmussen, J. (2018). Foundational Principles and Practices to Consider in Assessing Maker Education. i-manager's Journal of Educational Technology, Vol. 14 No. 4, January - March 2018. https://eric.ed.gov/?id=EJ1179517

<!-- deprecated 2026-10-01: superseded by the conditional model above. Old body kept verbatim.

## Description
Problem-based learning organizes learning around complex, meaningful problems that do not have a single obvious answer. Learners investigate the problem, identify what they need to know, gather evidence, propose solutions, and revise their thinking as they work. The strength of PBL is that it ties knowledge to use and makes learning purposeful, but it is not equivalent to leaving learners on their own. Strong PBL depends on careful facilitation, scaffolds for inquiry and collaboration, and enough domain grounding that the problem is challenging without becoming chaotic.

## Implications
Problem-based learning is strongest when the problem requires learners to integrate knowledge in ways that resemble real use, which is why whole-task work often supports transfer better than fragmented drill alone [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M]. At the same time, open problems can impose too much search on novices without enough prior structure [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M], so facilitation and scaffolding matter [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]. Novice learners often need process guidance for how to investigate, compare evidence, and decide what to do next [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M], not just exposure to a challenging problem.

### Context
#### Requirements
- **A meaningful, complex problem**: The problem should require investigation, judgment, and integration of knowledge rather than simple recall.
- **Access to evidence and resources**: Learners need materials, data, cases, or sources they can use to investigate the problem.
- **Facilitative support**: Instructors need to guide process, questioning, and evidence use without taking over the problem.
- **A product or decision point**: PBL is strongest when learners must articulate, defend, or test a proposed response.
#### Constraints
- **Novice overload**: Learners without sufficient background knowledge can flounder if the problem is too open too soon.
- **Process without rigor**: PBL can become busy but shallow if evidence use and synthesis are weak.
- **Time intensity**: Good PBL typically requires more time than direct instruction for setup, inquiry, and reflection.
- **Group coordination burden**: Collaboration can obscure individual learning unless roles and accountability are clear.

### Target Learners
- **Learners tackling authentic or interdisciplinary problems**: Strong fit when knowledge has to be integrated rather than applied one fact at a time.
- **Adult learners seeking relevance**: PBL works well when learners need to see why the content matters.
- **Learners developing self-directed inquiry habits**: The model builds planning, monitoring, evidence use, and revision.
- **Collaborative groups**: PBL often benefits from distributed roles and shared reasoning.

### Target Learning Objectives
- **Problem solving and reasoning**: Applying knowledge to ambiguous, open-ended situations.
- **Evidence-based inquiry**: Identifying what must be learned and using sources to inform a response.
- **Self-directed learning**: Planning, monitoring, and revising a learning path through the problem.
- **Transfer to authentic situations**: Using knowledge in contexts closer to real practice or decision making.

### Theory
#### Supporting
- Constructivist perspectives — learners build understanding through active problem engagement.
- Situated and experiential learning traditions — problems grounded in realistic contexts strengthen relevance and application.
- Self-regulated learning — PBL demands planning, monitoring, and adaptation across an extended task.
#### Contradicting / Qualifying
- PBL is weaker when learners lack enough conceptual grounding to investigate productively; some direct teaching is often needed first or during the task.
- Not every objective requires full PBL; some foundational skills are acquired more efficiently through explicit instruction and guided practice.
- Savery (2019) himself notes that meta-analyses (Newman, 2003; Sanson-Fisher & Lynagh, 2005) found the evidence base for PBL's superiority over traditional instruction "methodologically flawed" and inconclusive — a caution against treating PBL's effectiveness as more settled than the literature actually supports.
- Reigeluth (2011), in [Learner-Centered Paradigm of Education](../theories/learner-centered-paradigm.md), identifies four specific weaknesses of problem-based instruction — team assessment can hide an individual "loafer," insufficient repeated practice for transfer, no automaticity training, and inefficient unguided search — addressed by the [Project Space and Instructional Space](../patterns/project-and-instructional-space.md) pattern.

### Claims

- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M] — integrated, authentic problem solving is often better preparation for later transfer than isolated subskill practice
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] — learners benefit when facilitation responds to where their inquiry or reasoning is actually breaking down
- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M] — novices often need explicit investigation and decision routines before open-ended success criteria become productive
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M] — beginners can waste effort on unguided search unless the problem space is structured well enough to support learning
-->

<!-- deprecated 2026-10-02: superseded after the brief test, which found answers following the previous version into problem-first designs for novices.

## Conditional relationship

For a learner who must integrate knowledge to act on an ill-structured or authentic problem (a `complex-skill` or `principle` goal, not a `verbal-association` one), starting work from a problem *may* support conceptual understanding and transfer, provided the problem phase is followed or accompanied by guidance that connects the learner's attempts to the canonical ideas. The relationship is conditional on the learner's task-specific starting knowledge (`novice` learners left to discover essential content without support learn less), on age (in the one synthesis recorded here the problem-first advantage reversed for `child` learners in second to fifth grade), on the outcome chosen (no advantage is recorded for procedural fluency) and on the horizon at which it is measured. The wiki holds no direct comparison of whole problem-based curricula with conventional instruction; the evidence below concerns components of the relationship: problem-first sequencing, the amount of guidance, contingent support and case-based formats. The [pattern](../patterns/problem-based-learning.md) specifies a reusable design policy; its local diagnostic branches remain proposals.
-->

<!-- merged 2026-10-15 from patterns/problem-centered-task-level-progression-pattern ("Problem-centered instruction with task-level engagement and problem progression"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Problem-centered instruction with task-level engagement and problem progression

> **Pattern** · [All patterns](index.md)
> **Evidence** · no claims cited

## Description
Within Merrill's framework, the problem-centered element holds that "Learning is promoted when learners are engaged in solving real-world problems." Its corollaries specify that learners are shown the tasks they will be able to do, are engaged at the problem or task level rather than just the operation or action level, and solve a progression of problems that are explicitly compared to one another. The digest presents these as the prescriptions for effective instruction supporting the framework's central problem element.

## Design Implications

### Context
#### Requirements
- Learners must be shown the tasks they will be able to do and engaged at the problem or task level
#### Constraints
- The pattern is presented as part of a framework aimed primarily at cognitive learning

### Target Learners
- learners solving real-world problems in instruction

### Target Goals
- applying skills to whole tasks rather than isolated operations

### Claims
- 

## Related Patterns

- [Merrill's First Principles of Instruction](../patterns/4cid-four-component-instructional-design.md)

## Examples
-

## Key Sources
- Molenda, Michael. (2002). A New Framework for Teaching in the Cognitive Domain. ERIC Digest. https://eric.ed.gov/?id=ED470983
-->

<!-- merged 2026-10-19 from principles/real-world-problem-solving-maker-context ("Involve students in real-world problem solving to deepen engagement, retention, and understanding"), a narrower page folded into its canonical page (fragment step): its body as it stood. Its bullets this page lacked were added above.

# Involve students in real-world problem solving to deepen engagement, retention, and understanding

> **Principle** · [All principles](index.md)
> **Evidence** · 5 claims (5 for) · 5 studies (2 qualitative, 1 associational, 1 design, 1 theoretical), `q2` · 0 of 5 report an effect size · 5 claims rest on one study

## Description
The paper argues that achieving high levels of engagement, increasing graduation rates, and deepening understanding of content requires involving students in meaningful problem solving embedded into their daily classes. Providing meaning through relevant context for learning directly affects the retention and success of all students, especially those who are more at risk, and maker education is presented as a way to provide a relevant context for learning.

## Design Implications

### Context
#### Requirements
- Meaningful problem solving must be embedded into students' daily classes
#### Constraints
- Especially important for retaining students who are more at risk of failure or dropping out

### Target Learners
- K-12 students, including those more at risk of failure or dropping out

### Target Learning Objectives
- Engagement, graduation, retention, and deeper understanding of content

### Claims

- [Maker Education Assessment Principles Practices Framework](../theories/maker-education-assessment-principles-practices-framework.md) [+M]
- [Spontaneous responsiveness to real-world events in PBL can deepen student-directed inquiry beyond what designed curriculum achieves](../claims/spontaneous-authenticity-in-pbl-deepens-student-directed-inquiry.md) [+W]
- [In one extreme case, two sixth-graders with a choice-rich, ungraded STEAM infrastructure extended a game-design challenge into a year-long self-directed project well beyond its designed scope](../claims/choice-rich-infrastructure-supports-productive-deviation-and-learning.md) [+W]
- [Student engagement is higher during PBL than during traditional instruction](../claims/pbl-engagement-higher-than-traditional.md) [+W]
- [Students rated real-world projects and discussions with structured or guiding questions as the most beneficial learner-to-content strategies](../claims/real-world-projects-structured-questions-top-content-strategies.md) [+W]
- [Talladega County Schools' graduation rate rose from just above 70 percent in 2008 to 93 percent after its transition to project-based learning supported by digital technologies](../claims/talladega-graduation-rate-70-to-93-pbl-digital.md) [+W]

## Related Principles

- [Real-world Math](cultural-life-experiences-connections.md)
- [Provide student choice to build ownership and self-efficacy in maker education](autonomy.md)

## Examples
-

## Key Sources
- Lundberg, M., & Rasmussen, J. (2018). Foundational Principles and Practices to Consider in Assessing Maker Education. i-manager's Journal of Educational Technology, Vol. 14 No. 4, January - March 2018. https://eric.ed.gov/?id=EJ1179517
-->
