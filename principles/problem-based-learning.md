---
type: principle
id: problem-based-learning
title: Problem-based Learning
description: "For learners who must apply knowledge to ill-structured problems, organizing work around problems has a small, highly variable and possibly inflated average effect; what is better supported is guidance for novices on the target content, with a problem-first phase as a narrower option followed by instruction."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: thorndahl-2020
    resource: "https://doi.org/10.14434/ijpbl.v14i1.28773"
    title: "Thorndahl, K., & Stentoft, D. (2020). Thinking critically about critical thinking and problem-based learning in higher education: A scoping review. *The Interdisciplinary Journal of Problem-Based Learning, 14*(1)"
    author: "Thorndahl, K., & Stentoft, D"
  - id: lin-2017
    resource: "https://doi.org/10.11114/jets.v5i6.2320"
    title: "Lin, L. F. (2017). Impacts of the problem-based learning pedagogy on English learners' reading comprehension, strategy use, and active learning attitudes. *Journal of Education and Training Studies, 5*(6), 109-125"
    author: Lin, L. F
---

# Problem-based Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 12 claims (3 for, 8 mixed, 1 against) · 18 studies (7 causal, 5 quant-synthesis, 3 review, 2 theoretical, 1 qualitative), `q2`–`q4` · 3 of 18 report an effect size · 7 claims rest on one study

## Conditional relationship

Problem-based learning (PBL) organizes learning around ill-structured or authentic problems that learners investigate, usually in small groups with a facilitator. Read the evidence in two layers.

**As a curriculum format, its average effect is small and unreliable.** The best-documented synthesis in the wiki, a re-analysis of a PBL meta-analysis of 353 outcomes, reports a modest overall effect (g = 0.27) with large heterogeneity, individual outcomes from g = −1.26 to g = 1.91, publication bias that would shrink the effect to about g = 0.10, and no tutor-background category that predicts learning. So "use PBL" is not, by itself, a decision the evidence supports or rules out: what varies between implementations matters more than the label.

**Within a problem-centred design, guidance is the better-supported lever.** For a learner who is a `novice` on the target relation, leaving essential content to be discovered without support learns less than explicit instruction, while discovery with feedback, worked examples or scaffolding does better than other instruction. Starting with a problem *before* instruction is a narrower configuration (productive failure): it has meta-analytic support for conceptual knowledge and transfer when instruction follows, no procedural advantage, a reversal for second- to fifth-grade `child` learners, and is reported most reliably in well-structured domains. It is not evidence that open problems help novices learn content on their own.

The relationship is therefore conditional on the learner's starting knowledge of the target content, on the guidance and consolidation provided, on the outcome chosen (conceptual, transfer, procedural, product) and on the horizon. The [pattern](../patterns/problem-based-learning.md) specifies a reusable design policy; its local diagnostic branches remain proposals.

## Observation, state and explanation

Record what the learner does with a stated problem **under stated conditions**: what they identify as the question, what they say they need to know, which resources they consult, which solutions they generate, what help they receive and from whom, and what they produce. "Ready for open problems" is an inferred state, not an observation. Activity, talk volume and enthusiasm are observations of participation; none directly measures whether the target concept was learned. In a group, a shared product does not show what each member can do.

Activation of prior knowledge, noticing gaps and comparing one's own solutions with the canonical one are explanatory hypotheses offered by the claims below; they have not been observed directly in the studies the wiki records.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Novice on the target content, given an open problem to learn it from | Missing the content the problem needs; problem too hard to generate partial solutions; access or language demand | Ask for the key relation directly in a short probe; if absent, teach it (explanation, worked example) before or alongside the problem and observe whether the problem work then uses it. |
| Cannot start: no question framed, no learning issues listed | Missing task-specific knowledge to enter the problem; problem framed in unfamiliar language or representation; unclear what a product should look like | Ask for a first decision with a short prompt in a familiar representation; show the form of a finished product without its content; record whether either releases a start. |
| Busy and engaged, but the product shows little use of the target concept | Productive generation that awaits consolidation; floundering search without schema; target concept not actually needed by the problem as posed | Ask the learner to name the idea their solution depends on; check whether a correct solution to the problem as written requires the target concept at all. |
| Group product strong, individual explanation weak | Work carried by one or two members; learning distributed but not yet individually consolidated; explanation probe harder than the task | Ask each learner for an individual explanation or a changed-condition problem under matched conditions; record who did what during the problem phase. |
| Generates several flawed solutions, then learns quickly from instruction | Problem-first preparation, as productive-failure accounts propose; instruction alone would have sufficed; extra time on task | Only a comparison with an instruction-first condition of matched time can attribute the gain; a single learner's trajectory cannot. |
| Succeeds on a conceptual probe, fails a routine procedure (or the reverse) | Different outcomes from the same sequence; procedure not practised; probe misaligned with what was taught | Score procedural and conceptual items separately, at the same horizon, and preserve both. |

These rows are proposals, untested with learners. A probe can shift confidence among the explanations; it does not identify a cause on its own. The probe itself is a learning exposure and should be recorded as one.

## Evidence and qualifications

- [The overall PBL effect in a tutor-background meta-analysis is modest, with large heterogeneity](../claims/pbl-overall-effect-modest-large-heterogeneity.md) [~M]: a re-analysis (Walker & Leary, 2023) of the Leary et al. (2013) data, 353 outcomes, reports g = 0.27 with I² = 80% of variability attributable to heterogeneity; [individual outcomes range from g = −1.26 to g = 1.91](../claims/massive-range-pbl-outcome-effect-sizes.md) [~M]. Not yet checked against its source. It does not predict the effect of any one PBL implementation, and the claim pages do not report learners, comparators or horizons by outcome.
- [Publication bias in the same data](../claims/publication-bias-pbl-tutor-meta-analysis.md) [~M]: a funnel plot and Egger's test indicate publication bias, and trim-and-fill drops the overall effect to g = 0.103. Treat the average as possibly overstated.
- [Tutor background does not predict learning](../claims/tutor-background-meta-regression-not-predictive.md) [~M]: in a meta-regression with content novices as the reference, no tutor-expertise category predicted student learning (R² = .01, p = .14), and [the largest subgroup difference was not significant](../claims/tutor-background-meta-regression-not-predictive.md) [~M]. A nonsignificant moderator is not evidence that facilitation does not matter; it says tutors' credentials alone did not explain the variation.
- [A small meta-analysis reports a large pooled effect on achievement](../claims/pbl-large-positive-effect-academic-achievement.md) [+W]: five studies, random-effects ES = 1.560 (95% CI 0.768–2.353), heterogeneous; the claim page records that the article describes its z-test as not significant (z = 3.859; p > .05), which is internally inconsistent. Do not weigh it against the 353-outcome synthesis.
- [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [-S]: a meta-analysis of 580 comparisons found explicit instruction outperformed unassisted discovery (d = 0.38 favouring explicit instruction), while 360 comparisons found enhanced or assisted discovery (feedback, worked examples, scaffolding, elicited explanations) outperformed other instruction. An experiment with 112 third- and fourth-grade `novice` children (the claim page does not say how they were assigned) found many more mastered the control-of-variables procedure under direct instruction, and those taught directly did as well on a later transfer task as the few who discovered it. The Klahr & Nigam entry passes the judge; the registry attaches the wrong abstract to the meta-analysis (recorded as a registry problem), and the narrative review is unsettled. This bounds the principle: it predicts poor learning when PBL means leaving novices to discover essential content unsupported, not that guided problem work fails. The claim page does not break the meta-analytic result down by prior knowledge.
- [Productive Failure Improves Conceptual Learning](../claims/productive-failure-improves-conceptual-learning.md) [~S]: a three-level meta-analysis (`synthesis-mixed`: experimental and quasi-experimental comparisons, 53 studies, 166 comparisons) set problem solving followed by instruction against the same instruction taught first. It favoured problem-first on conceptual knowledge and transfer (g = 0.36) and found no difference on procedural knowledge (g = −0.03); the advantage was larger for implementations following productive-failure design criteria (generating multiple solutions, group work, instruction building on student solutions) and reversed for second to fifth graders and for domain-general skills. One entry passes the judge on its abstract; the synthesis entry is unsettled on its abstract. It does not predict an advantage for problem-first work with no subsequent instruction, for young children, or on procedural fluency, and the claim page reports no delayed-horizon breakdown. Marked `~` because its support for problem-first work is conditional on instruction following and on learner age.
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]: one-to-one tutoring studies in which support was adjusted to each learner response outperformed fixed, moderate or no support on immediate and one-month tests of long division (N = 8 per condition), and interactive tutoring gave similar immediate learning but better transfer; a dynamic-assessment synthesis ranked scaffolding above coaching but below explicit strategy training. None of its three judged entries passes; they could not be confirmed on their abstracts. Its evidence comes mostly from one-to-one tutoring, not from facilitated PBL groups, so it supplies a candidate facilitation policy rather than a tested PBL result.
- [Case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [~M]: in one community-college biology cohort (n = 56; a non-randomized within-cohort comparison of matched topics), case-taught topics scored higher on course exams; a systematic review of 104 papers in health professional education (it passes the judge) concluded that students enjoy case-based learning but the evidence on learning compared with other activities is inconclusive, and that any benefit of small-group case work may come from the group work rather than the cases. It does not establish an advantage for authentic-problem formats in general and does not report delayed outcomes.

Retain learner age and starting knowledge, the exact comparator (instruction-first, lecture, unassisted discovery), the amount and timing of guidance, time on task, outcome type and horizon when transporting these results. A pooled g over unlike implementations is not a forecast for one class or one learner, and a nonsignificant procedural difference does not establish equivalence.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M] — checked by the judge: all 1 entries pass (abstract)
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M] — not settled: the text available could not confirm the entries (abstract)
- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M] — not settled: the text available could not confirm the entries (abstract)

## Objective and learner-valued goal

Ask what the learner wants from the problem, and why, separately from the designer's objective. A problem chosen for its authenticity to the designer may not be one the learner cares about, and a learner's interest in solving the problem may diverge from the designer's interest in a concept the problem is meant to carry. Agreement, divergence and uncertainty are observations; engagement during the problem phase does not establish that the learner values the target capability. Choose a representative instrument, criterion, permitted resources and horizon for each outcome that matters: conceptual understanding, transfer, procedural fluency and the quality of the product are different claims.

For example, a nursing student may value making a safe decision for the patient in a case, while the designer's objective is that the student can explain the physiological principle the case was built around. A correct group care plan cannot establish either the individual decision or the explanation. The pattern shows how to record both aims and test the one each party cares about.

## What would revise this model?

The problem-first expectation should weaken if comparable learners, with comparable consolidation instruction and time, fail to show a conceptual or transfer advantage over instruction-first sequences on aligned measures, or if the advantage disappears at a delayed horizon. If younger learners, domain-general skills or other populations repeatedly show the reversal recorded in the synthesis, narrow the principle to the populations where it holds. If matched-time comparisons attribute PBL gains to group work, feedback or extra time rather than to the problem-first order, revise the explanation. Do not protect the model by relabelling every failure as poor facilitation or insufficient authenticity after the fact.

An engaging problem phase, an immediate conceptual gain, delayed retention, transfer to practice and the learner's valued use are separate claims. The evidence recorded here does not establish an optimal amount of guidance, a readiness threshold for open problems, or the effect of whole PBL curricula against conventional instruction.

At the curriculum level, the expectation of a small and variable average should change if bias-corrected syntheses with stated comparators and horizons show a consistent effect, or if moderators (guidance, consolidation, prior knowledge, outcome type) are found that explain the variation.

## Related Principles
- [Inquiry-based Learning](inquiry-based-learning.md) — PBL is one inquiry form centered on authentic problems.
- [Experiential Learning](experiential-learning.md) — problem-centered work often provides the concrete experience that later reflection builds on.
- [Authentic Audiences & Purposes](authentic-audiences-purposes.md) — real stakeholders or consequences often strengthen PBL design.
- [Guided Practice](guided-practice.md) — novices often need coached practice with inquiry and problem-solving moves inside PBL.

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

<!-- deprecated 2026-10-01: superseded by the conditional model above. Old body kept verbatim.

## Description
Problem-based learning organizes learning around complex, meaningful problems that do not have a single obvious answer. Learners investigate the problem, identify what they need to know, gather evidence, propose solutions, and revise their thinking as they work. The strength of PBL is that it ties knowledge to use and makes learning purposeful, but it is not equivalent to leaving learners on their own. Strong PBL depends on careful facilitation, scaffolds for inquiry and collaboration, and enough domain grounding that the problem is challenging without becoming chaotic.

## Implications
Problem-based learning is strongest when the problem requires learners to integrate knowledge in ways that resemble real use, which is why whole-task work often supports transfer better than fragmented drill alone [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+S]. At the same time, open problems can impose too much search on novices without enough prior structure [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M], so facilitation and scaffolding matter [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]. Novice learners often need process guidance for how to investigate, compare evidence, and decide what to do next [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M], not just exposure to a challenging problem.

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
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+S] — integrated, authentic problem solving is often better preparation for later transfer than isolated subskill practice
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] — learners benefit when facilitation responds to where their inquiry or reasoning is actually breaking down
- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M] — novices often need explicit investigation and decision routines before open-ended success criteria become productive
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M] — beginners can waste effort on unguided search unless the problem space is structured well enough to support learning
-->

<!-- deprecated 2026-10-02: superseded after the brief test, which found answers following the previous version into problem-first designs for novices.

## Conditional relationship

For a learner who must integrate knowledge to act on an ill-structured or authentic problem (a `complex-skill` or `principle` goal, not a `verbal-association` one), starting work from a problem *may* support conceptual understanding and transfer, provided the problem phase is followed or accompanied by guidance that connects the learner's attempts to the canonical ideas. The relationship is conditional on the learner's task-specific starting knowledge (`novice` learners left to discover essential content without support learn less), on age (in the one synthesis recorded here the problem-first advantage reversed for `child` learners in second to fifth grade), on the outcome chosen (no advantage is recorded for procedural fluency) and on the horizon at which it is measured. The wiki holds no direct comparison of whole problem-based curricula with conventional instruction; the evidence below concerns components of the relationship: problem-first sequencing, the amount of guidance, contingent support and case-based formats. The [pattern](../patterns/problem-based-learning.md) specifies a reusable design policy; its local diagnostic branches remain proposals.
-->
