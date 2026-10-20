---
type: pattern
id: case-based-learning
aliases: [case-based-learning-harvard-method]
title: Case-Based Learning
description: "A reusable policy for learning from realistic cases: establish what learners can already do with the target concept, have them compare several cases that share a principle rather than study one at a time, make the principle explicit, and judge the unit on transfer to a new case rather than on enjoyment or recall."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-17
grain_size: lesson
sources:
  - id: kim-2006
    resource: "https://doi.org/10.1111/j.1365-2929.2006.02544.x"
    title: "Kim, S., Phillips, W. R., Pinsky, L., Brock, D., Phillips, K., & Keary, J. (2006). A conceptual framework for developing teaching cases: A review and synthesis of the literature across disciplines. *Medical Education, 40*(9), 867-876"
    author: "Kim, S., Phillips, W. R., Pinsky, L., Brock, D., Phillips, K., & Keary, J"
  - id: kononowicz-2019
    resource: "https://doi.org/10.2196/14676"
    title: "Kononowicz, A. A., Woodham, L. A., Edelbring, S., Stathakarou, N., Davies, D., Saxena, N., Tudor Car, L., Carlstedt-Duke, J., Car, J., & Zary, N. (2019). Virtual patient simulations in health professions education: Systematic review and meta-analysis by the Digital Health Education Collaboration. *Journal of Medical Internet Research*"
    author: "Kononowicz, A. A., Woodham, L. A., Edelbring, S., Stathakarou, N., Davies, D., Saxena, N., Tudor Car, L., Carlstedt-Duke, J., Car, J., & Zary, N"
  - id: chernikova-2020
    resource: "https://doi.org/10.3102/0034654320933544"
    title: "Chernikova, O., Heitzmann, N., Stadler, M., Holzberger, D., Seidel, T., & Fischer, F. (2020). Simulation-based learning in higher education: A meta-analysis. *Review of Educational Research*"
    author: "Chernikova, O., Heitzmann, N., Stadler, M., Holzberger, D., Seidel, T., & Fischer, F"
  - id: sadaf-2022
    resource: "https://doi.org/10.24059/olj.v26i4.3474"
    title: "Sadaf, A., Kim, S. Y., & Olesova, L. (2022). Relationship between metacognition and online Community of Inquiry in an online case-based course. *Online Learning, 26*(4), 79-93"
    author: "Sadaf, A., Kim, S. Y., & Olesova, L"
  - id: zhang-2026
    resource: "https://doi.org/10.1371/journal.pone.0358951"
    title: "Zhang, B., et al. (2026). A sequential integrating virtual simulation and authentic video for preschool teacher candidates' observational skills training: A design-based intervention study. *PLoS One*"
    author: "Zhang, B., et al"
---

# Case-Based Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 45 claims (19 for, 25 mixed, 1 against) · 33 studies (13 causal, 6 quant-synthesis, 6 review, 3 design, 2 associational, 2 qualitative, 1 theoretical), `q2`–`q4` · 7 of 33 report an effect size · 40 claims rest on one study

## Description and scope

A reusable policy for organizing a lesson around realistic cases (scenarios, incidents, dilemmas or worked situations) that learners analyse, and for deciding how many cases to use, how learners work with them, and when the principle they share is made explicit. It applies the [case-based learning principle](case-based-learning.md), which has not yet been rewritten as a conditional model, and draws on [analogical reasoning](../principles/analogical-reasoning.md) and [cognitive flexibility](../principles/cognitive-flexibility.md). The study configurations below are evidence; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence about a learner group, not to certify that a learner "can reason from cases".

**What the evidence does and does not test.** The wiki's strongest evidence concerns one component, *comparing* cases (`case-comparison`), against studying the same cases one at a time, single cases, or conventional instruction. Case-based learning as a whole format has one non-randomized classroom comparison and a systematic review that found its effect on learning inconclusive. So this page treats comparison, an explicit principle and a transfer probe as the configuration, and treats "use cases" on its own as an unsupported promise.

[Problem-based learning](problem-based-learning.md) is a neighbouring, converted pattern: it organizes a unit around one problem learners must investigate and decides how much guidance to give before or after it. This pattern is narrower and works at lesson grain: the case is an object of analysis and comparison, not a driving problem, and its decisions concern case selection, comparison and the timing of the principle. Where a case is used as a problem to solve before instruction, use the problem-based pattern's guidance on problem-first phases. The [Harvard-method page](case-based-learning.md) describes one discussion-centred configuration of the format.

**Cases on screen, online and with AI (added 2026-10-17).** A case may be read and discussed in an online course, worked alone and asynchronously, or made interactive: a branching case or virtual patient that responds to the learner's decisions, a case written or varied by a generative AI, or a case in which an AI plays the client, patient or colleague. The analysis-and-comparison policy below applies to all of them. Where the point is to *rehearse a conversation* with the person in the case, use [Practice with Simulated People](practice-with-simulated-people.md); where an AI responds to a learner's analysis turn by turn, [AI Tutoring](ai-tutoring.md) decides what it may give away; where a learner works through cases alone with a mentor, [Mentor Support in Self-Paced Online Learning](mentor-support-in-self-paced-online-learning.md) decides when the mentor steps in.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Age band and task-specific starting knowledge (`novice`, `intermediate`, `advanced`, or `?`); a brief independent analysis of one case: what the learner thinks matters in it, what principle (if any) they name, and what they would do. Preserve unknowns. |
| Context and activities | Setting (`classroom`, `online-instructor-led`, `workplace-clinical`, ...), time available, group or individual work, who facilitates, and exactly which cases, prompts, explanations and feedback are planned and in what order. |
| Learner-valued goal | Ask what the learner wants to be able to do with cases like these and why (for example, decide in their own practice, argue a position, pass an exam). Record disagreement with the designer objective; negotiate rather than assume agreement. |
| Designer objective | The principle, concept or judgement (`principle`, `concept`, `complex-skill`) the cases are meant to carry, and whether the domain is well structured (one principle applies the same way across cases) or ill structured (the concept plays out differently case by case). |
| Outcome | Separate instruments for factual recall, use of the principle in a new case (`near-transfer`, `far-transfer`) and, where it matters, a decision or product; individual as well as group measures; immediate and delayed horizons. |

A request for "more realistic, engaging teaching" does not specify these inputs. Ask for them before choosing cases, a number of cases or a predicted gain. Check first that each case actually instantiates the target principle and that a correct analysis of it requires the principle, not only common sense or reading the case.

## Sequence and conditional policy

1. **Elicit briefly.** Give one case and ask each learner (not only the group) what matters in it and why. Keep this short and record it as a learning exposure.
2. **Select at least two cases that share the target principle.** Choose cases whose surface details differ while the principle stays the same; for an ill-structured target, add cases in which the concept plays out differently. Record how the cases differ and on which dimension they are meant to contrast.
3. **Have learners compare, not just read.** Present the cases together and prompt for what is the same, what differs and why. Studying the same cases one after another is a different configuration with weaker recorded results; record which was delivered.
4. **Make the principle explicit after the comparison.** State the principle, connected to what learners found in the cases; correct a principle that learners have abstracted wrongly.
5. **Reobserve individually on a new case.** Use a case with new surface details, scored separately for recall and for use of the principle, at the agreed horizon. If the response disagrees with the expectation, revise the interpretation or the configuration.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Learner retells the case but names no principle | Ask what would change the outcome of the case; give a second case and ask what the two have in common. | If the comparison releases a principle, continue with comparison. If not, the learner may lack the concept the cases presuppose: teach it explicitly or use a worked example before further cases. Neither branch is a validated diagnosis. |
| Learner names a principle, but a surface feature of the case | Give a case with the same surface feature and a different principle, and one with different surface and the same principle. | Choose cases that vary the misleading surface feature and hold the principle constant, and prompt for the contrast. The comparison evidence does not establish how many cases are enough. |
| Lively discussion, but individual answers on a new case do not use the principle | Individual analysis of a changed case, matched in demand to the discussion. | Add an individual comparison task and an explicit statement of the principle; record who contributed what. A review of the format notes that any benefit may come from group work rather than from the cases, so discussion alone does not show learning. |
| Principle used on the new case, factual recall weak | Score recall separately under the same conditions. | Add targeted recall practice if recall is part of the objective. In one small experiment, multiple-case study improved transfer essays while a drill group recalled more facts, so this pattern is expected rather than a failure. |
| Correct on an immediate new case, not at a delay | A matched new case after the agreed interval. | Plan a later comparison or retrieval of the principle. The comparison meta-analysis found larger benefits on immediate than on delayed tests, so an immediate success does not forecast a delayed one. |

## Choosing configurations from evidence

- **Whether to expect anything from the format itself.** [Case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [~M] rests on one non-randomized within-cohort comparison in an introductory community-college biology course (56 students; case-taught topics scored higher on regular exams than matched topics taught by short lecture, reading and discussion, an 18-percentage-point average difference, no standardized effect size) and on a systematic review of 104 papers in health professional education that found the evidence inconclusive on whether case-based learning improves learning more than other activities, noting that gains may come from the group work. Plan and evaluate a specific configuration; do not promise a gain from the label. Neither entry reports a delayed outcome.
- **Compare cases rather than study them one at a time.** [Comparing contrasting cases improves learning](../claims/comparing-contrasting-cases-improves-learning.md) [+M]: across 57 experiments (336 tests) case comparison produced greater learning than single, sequential or non-analogous case study, traditional instruction and controls (d = .50, 95% CI [.44, .56]); in a randomized experiment with undergraduate novices learning negotiation, 48% of those who compared two cases on one page used the principle in a new negotiation against 19% of those who studied the same cases separately. The pooled estimate mixes several comparison conditions, so it is not solely a "compare vs. same cases separately" effect. The same evidence underlies [multiple contrasting cases support abstraction](../claims/comparing-contrasting-cases-improves-learning.md) [+M].
- **When the principle is stated, and on which outcome to judge.** The same meta-analysis found larger benefits when learners were asked to find similarities, when the principle was given *after* the comparison, with perceptual content, and on immediate tests. That supports step 4's order and the delayed probe in the table; it does not set a lag or a dose. In seventh-grade algebra, comparing solution methods side by side raised procedural knowledge and flexibility but not conceptual knowledge (abstract only), so a comparison may change how learners use and choose methods without changing their grasp of the concept.
- **Multiple perspectives in ill-structured domains.** [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [~M]: in a small randomized experiment (34 paid university volunteers, the social impact of technology), revisiting short cases under several themes produced better transfer essays than computer drill, while drill produced better factual recall; the treatment bundled several features, so which one mattered is not known. The comparison meta-analysis does not isolate ill-structured domains or multiple perspectives, and its smaller delayed benefit cuts against the theory's prediction that the advantage grows at delay. Choose this configuration for an ill-structured target judged on transfer, and measure recall separately.
- **Novices.** No claim recorded here tests case-based learning by prior knowledge. The claim pages' discussions propose, without evidence entries, that novices may need the concept supplied or comparison scaffolded; the comparison experiments themselves used novices. Treat expertise as an open moderator and elicit the starting response rather than assume. The nearest evidence since this was written: in simulation-based learning in higher education, examples were associated with larger effects for learners at lower education levels and reflection phases for those at higher levels ([Prior knowledge moderates scaffolding effectiveness](../claims/prior-knowledge-moderates-scaffolding-effectiveness.md) [~M]), and in one experiment novices who learned the causal mechanism of artificial diseases diagnosed difficult cases with irrelevant findings better than those who learned feature lists ([Biomedical causal knowledge improves novice diagnostic accuracy on difficult cases with irrelevant findings](../claims/biomedical-causal-knowledge-improves-novice-diagnosis-irrelevant-findings.md) [+M]), which supports supplying the concept before novices work difficult cases. Neither tests case comparison by prior knowledge.

*Evidence added 2026-10-17: cases online, interactive, and with AI.*

- **Interactive case simulations (virtual patients) against traditional teaching.** A meta-analysis of randomised trials in the health professions ([Kononowicz et al. 2019](https://doi.org/10.2196/14676)) found virtual patients no better than traditional education on knowledge (SMD = 0.11, 95% CI −0.17 to 0.39; [Virtual patients are as effective as traditional education for knowledge outcomes](../claims/vp-traditional-knowledge-no-difference.md) [~M]; a nonsignificant difference, not shown equivalence) and better on skills outcomes (SMD = 0.90, 95% CI 0.49 to 1.32, I² = 88%; [Virtual patients more effectively improve skills than traditional education](../claims/vp-traditional-skills-advantage.md) [+M]; the claim page does not list which skills). Added *to* traditional teaching, they improved knowledge (SMD = 0.73; [Virtual patients blended with traditional education improve knowledge more than traditional education alone](../claims/vp-blended-knowledge-advantage.md) [+M]) and probably skills (SMD = 0.60, interval crossing zero; [Virtual patients blended with traditional education show moderate positive skills effects, but the pooled interval crosses zero](../claims/vp-blended-skills-mixed.md) [~M]). An exploratory reading of the same trials found large advantages over lectures and reading and small or negative ones over active comparators such as group discussion or mannequins ([Virtual patients show larger advantages over passive traditional learning than over active learning](../claims/vp-passive-versus-active-comparison.md) [~M]), and no difference from other digital formats ([Virtual patients show no significant differences versus other types of digital education](../claims/vp-vs-other-digital-no-difference.md) [~M]). Design variants rarely differed; the exceptions were empathic feedback and a narrative structure for communication skills and scaffolding for diagnostic efficiency ([Virtual patient design-variant comparisons rarely show significant differences, with feedback and scaffolding exceptions](../claims/vp-design-variants-mostly-null.md) [~M]). For this pattern: an interactive case is a good replacement for a lecture or reading and a weak replacement for an active case discussion, so add it to the discussion rather than swap one for the other, and expect its gain on reasoning and skills rather than recall.
- **Case-based simulations in higher education ([Chernikova et al. 2020](https://doi.org/10.3102/0034654320933544)).** Across 145 studies, simulation-based learning had a large effect on complex skills (g = 0.85) against several kinds of control ([Simulation-based learning has a large positive overall effect on complex skills in higher education](../claims/simulation-based-learning-large-positive-effect-complex-skills.md) [+M]); the effect was g = 0.82 for diagnostic skills and 0.44 for communication ([Simulation effects vary by complex skill](../claims/simulation-effects-vary-by-complex-skill.md) [~M]); document-based simulations, in which learners work on case documents such as X-rays or students' homework, were the least effective type (g = 0.31; [Live simulations with real patients showed the greatest effects among simulation types](../claims/simulation-type-moderates-effectiveness.md) [~M]); more authentic simulations were associated with larger effects (g = 0.86 against 0.58; [High authenticity simulations show higher effects than low authenticity simulations](../claims/high-authenticity-simulations-higher-effects.md) [~M]); and prompts alone were associated with smaller effects while examples with prompts did well in a few medical studies ([Presence versus absence of individual scaffolding types did not support the added-value hypothesis, but scaffolding combinations partly did](../claims/scaffolding-added-value-partly-supported.md) [~M]). These are comparisons between groups of studies. For this pattern: a static written case is the weakest of the simulated formats in that synthesis, so where a case can carry decisions and consequences, let it; pair prompts with an example for novices.
- **Online and asynchronous case work.** One survey of 47 graduate students in an online case-based instructional-design course found cognitive presence rated highest and teaching presence most variable ([In an online case-based course, students perceive cognitive presence as highest and least variable](../claims/cognitive-presence-highest-least-variable-online-cbi.md) [~W]); co-regulation (regulating learning with peers) was more strongly related to the three presences than self-regulation ([Co-regulation shows stronger relationships with the three CoI presences than self-regulation in an online case-based course](../claims/co-regulation-stronger-presence-relationships-than-self-regulation.md) [~W]); and social presence, not teaching presence, was most associated with metacognition ([Social presence shows the strongest association with metacognition in an online case-based course](../claims/social-presence-strongest-metacognition-association-cbi.md) [~W]). These are correlations in one course with no learning outcome. Interviews with international students in an online programme found some uncomfortable with case-based learning for its lack of structured content, wanting the instructor to recap key points ([Some Chinese students felt uncomfortable with case-based learning due to lack of structured instruction content](../claims/case-based-learning-uncomfortable-unstructured-instruction.md) [~W]), and wanting more global cases tied to their own workplaces ([International students wanted more global cases and closer connections between case analyses and their local work contexts](../claims/lack-of-global-cases-local-relevance.md) [~W]). For this pattern: online, keep a peer exchange on each case, make step 4's principle statement and recap explicit in writing, and draw cases from learners' settings. No claim in this wiki compares asynchronous with synchronous case discussion, or measures what online case work does to learning.
- **AI-generated and AI-facilitated cases.** A scoping review of generative AI in medical education found case-based learning benefits mainly where AI was embedded in faculty-guided cases, and null or unfavourable effects with complex cases and team workflows (already cited below). Controlled studies of AI virtual patients reported short-term gains in history taking and communication, but not universally, and some learners rated human cases more authentic ([Controlled GenAI virtual-patient and communication studies reported short-term skill gains, but positive findings were not universal](../claims/genai-virtual-patient-short-term-gains-mixed.md) [~M]); in one small comparison, students rated a PBL tutorial with an AI-simulated patient higher than their earlier ones ([GenAI-condition students rated their PBL tutorial significantly higher](../claims/genai-virtual-patient-higher-perceived-tutorial-quality.md) [+W], 26 students, perceptions). Reviews describe AI case simulations supporting diagnostic reasoning in nursing ([AI-driven case simulations in ambulatory settings support diagnostic reasoning](../claims/ai-ambulatory-case-simulations-diagnostic-reasoning.md) [+W], narrative, no effect sizes) and LLMs generating cases and problem contexts hard to reproduce in classrooms ([LLMs help bridge the gap between theoretical curricula and real-world skills by creating simulated scenarios, cases and problem contexts](../claims/llm-simulations-bridge-theory-practice-gap.md) [+W], an argument in a review); eight medical students rated an LLM-gamified version of five cases more engaging than the original case material ([In a pilot with eight medical students, multimodal MedGame was perceived as more engaging and useful](../claims/multimodal-medgame-higher-perceived-engagement-pilot.md) [+W]). For this pattern: an AI can produce the surface-varied cases step 2 needs and play the person in an interactive case, but a person checks that each case instantiates the principle, and the learner's individual analysis, not the AI conversation, is what is judged. No claim in this wiki tests AI-generated cases against human-written ones on learning.
- **Teacher education.** In one design study with 34 preschool teacher candidates, observation assignments after an authentic classroom video scored higher than after a simplified virtual simulation on the total and on the analysis and support dimensions, with no difference on basic observation, while the simulation produced higher self-reported purposefulness of reflection ([In the initial skill acquisition phase, authentic video yielded higher overall observation assignment scores than virtual simulation](../claims/av-outperforms-vs-total-observation-score.md) [~M]; [Authentic video outperformed virtual simulation on the higher-order analysis and support dimensions](../claims/av-advantage-analysis-support-dimensions.md) [~M]; [Virtual simulation stimulated higher self-reported purposefulness than authentic video](../claims/vs-higher-purposefulness-reflection.md) [~M]; a fixed order, so order and condition are confounded). Six teachers judged LLM-simulated student ideas realistic and useful as material for thinking about student understanding ([Teachers judged LLM-simulated student ideas realistic and most useful when the ideas sparked sensemaking](../claims/teachers-perceive-llm-ideas-realistic-sensemaking-useful.md) [+W]).
- **Technology and business.** In one design study, a teacher modelling AI outputs as contrasting cases was what students named as the turning point toward judging AI output critically ([Students perceived the teacher's modeling with contrasting cases as a turning point that repositioned them as active gatekeepers of AI-generated content](../claims/contrasting-cases-gatekeeper-repositioning.md) [+W]). No claim in this wiki tests learning from business cases or from technology cases (incident reviews, architecture or troubleshooting cases); the comparison evidence above includes a negotiation task, which is the nearest business-like outcome.

Do not rank these results against one another: their comparators (separate cases, drill, lecture and reading, other activities) and outcomes (exam items, transfer essays, a negotiation, procedural knowledge) differ. A precise abstention names the missing comparison, outcome or observation and the next way to resolve it.

## Fitting the design to a situation

Ask for four facts when the brief omits them: **is the domain well structured or ill structured?**, **is the outcome recall, use of a principle on a new case, or a procedure?**, **is the test immediate or delayed?**, and **will learners work in groups or alone?**

| If the brief says… | Then change… | Basis |
|---|---|---|
| The goal is applying a principle to new cases | Present two or more cases that share the principle side by side and prompt for what is the same and why, rather than one case at a time | [Comparing cases side by side improves learning and transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M]; [Analogical reasoning improves transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] |
| The plan states the principle first and then shows cases as illustrations | Reverse the order: have learners compare first and state the principle after, connected to what they found | [Analogical reasoning improves transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] (moderator in the meta-analysis) |
| The domain is ill structured (the concept plays out differently case by case) | Revisit several short cases under different themes; expect better transfer essays, and plan separate work for factual recall, which drill did better | [Multiple cases from different perspectives support transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [~M] |
| The goal is understanding why a mathematical method works, not only choosing a method | After comparing solution methods, add an explicit explanation of why each works; comparison raised procedural knowledge and flexibility but not conceptual knowledge | [Comparing cases: procedural gain, no conceptual gain in one algebra study](../claims/comparing-contrasting-cases-improves-learning.md) [~M] |
| The test that matters is weeks later | Add a later comparison or retrieval of the principle; benefits were larger on immediate than delayed tests | [Analogical reasoning improves transfer](../claims/comparing-contrasting-cases-improves-learning.md) [~M] |
| The course is in the health professions and relies on small-group case discussion | Do not expect the case format alone to raise learning; a review judged the evidence inconclusive and said any benefit may come from the group work. Add individual analysis of a new case | [Case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [~M] |
| Learners work alone (`online-self-paced`) | Put both cases on one screen with a written prompt to describe their similarities | [Comparing cases side by side improves learning and transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] (undergraduates comparing two cases on one page) |
| Cases are complex and supported by AI tools or team workflows (medical education) | Keep a faculty member guiding how the tool is used in each case; complex cases and team workflows showed null or unfavourable effects | [Case-based learning benefits depended on faculty-guided embedding](../claims/genai-cbl-faculty-guided-conditional-benefits.md) [~W] |
| Learners lack the concept the cases presuppose | Teach the concept or give a worked example before the cases, then compare | no claim here tests case-based learning by prior knowledge; nearest: [Biomedical causal knowledge improves novice diagnostic accuracy on difficult cases](../claims/biomedical-causal-knowledge-improves-novice-diagnosis-irrelevant-findings.md) [+M] and [Prior knowledge moderates scaffolding effectiveness](../claims/prior-knowledge-moderates-scaffolding-effectiveness.md) [~M] (examples for lower levels, reflection for higher) |
| Many learners discuss one case in a large group | Add an individual comparison task on a changed case before the group discussion ends | untested proposal |
| Learners work through cases self-paced online (`online-self-paced`), with a mentor available on demand | Put the cases side by side with a written comparison prompt; require a short individual written analysis of each new case; have the mentor read a sample and return the principle statement with feedback; add an asynchronous peer exchange on each case; recap the principle in writing; use cases from the learners' own workplaces where possible | [Comparing cases side by side improves learning and transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M]; [Co-regulation shows stronger relationships with the three CoI presences than self-regulation in an online case-based course](../claims/co-regulation-stronger-presence-relationships-than-self-regulation.md) [~W]; [Some Chinese students felt uncomfortable with case-based learning due to lack of structured instruction content](../claims/case-based-learning-uncomfortable-unstructured-instruction.md) [~W]; mentor role from [Mentor Support in Self-Paced Online Learning](mentor-support-in-self-paced-online-learning.md), untested for case work |
| An AI is the case partner: it writes or varies the cases, plays the client or patient, or questions the learner's analysis | Have the AI generate surface-varied cases holding the principle constant, and check each one before use; let it play the person in an interactive case; have it ask for the principle rather than supply it; judge the learner's individual analysis of a new case without the AI; keep a person reviewing complex cases | [Case-based learning benefits depended on faculty-guided embedding](../claims/genai-cbl-faculty-guided-conditional-benefits.md) [~W]; [Controlled GenAI virtual-patient and communication studies reported short-term skill gains, but positive findings were not universal](../claims/genai-virtual-patient-short-term-gains-mixed.md) [~M]; see [AI Tutoring](ai-tutoring.md) and [Practice with Simulated People](practice-with-simulated-people.md) |
| An interactive case simulation (virtual patient, branching case) is available | Use it alongside the case discussion, not in place of it; expect gains on reasoning and skills more than on recall; give feedback inside the case | [Virtual patients blended with traditional education improve knowledge more than traditional education alone](../claims/vp-blended-knowledge-advantage.md) [+M]; [Virtual patients show larger advantages over passive traditional learning than over active learning](../claims/vp-passive-versus-active-comparison.md) [~M]; [Virtual patients are as effective as traditional education for knowledge outcomes](../claims/vp-traditional-knowledge-no-difference.md) [~M] (health professions) |
| The cases are static documents only (a written case, a record, a work sample) | Build in decision points with consequences revealed in stages, or pair the document with a worked analysis for novices | [Live simulations with real patients showed the greatest effects among simulation types](../claims/simulation-type-moderates-effectiveness.md) [~M] (document-based least effective, g = 0.31, higher education) |
| Teacher education: cases of classroom practice for observation | Start with a simplified simulated classroom for reflection, then move to authentic classroom video for analysis and proposing support | [In the initial skill acquisition phase, authentic video yielded higher overall observation assignment scores than virtual simulation](../claims/av-outperforms-vs-total-observation-score.md) [~M]; [Virtual simulation stimulated higher self-reported purposefulness than authentic video](../claims/vs-higher-purposefulness-reflection.md) [~M] (one design study, 34 candidates) |
| Learners come from varied countries or workplaces (international, working professionals) | Mix global and local cases, and ask learners to bring or adapt a case from their own work | [International students wanted more global cases and closer connections between case analyses and their local work contexts](../claims/lack-of-global-cases-local-relevance.md) [~W] |
| Business or technology cases (a strategy decision, an incident review, a troubleshooting case) | Keep the comparison policy: two cases sharing one principle, an individual written recommendation before discussion, the principle stated after | untested in these domains in this wiki; the comparison evidence includes a negotiation task ([Comparing cases side by side improves learning and transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M]) |

## The evidence by question

- *Does comparing analogous cases improve transfer more than studying cases one at a time?* [Analogical Reasoning Improves Transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M]
- *Does teaching through realistic cases, by itself, raise learning?* [Case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [~M]
- *Do interactive virtual-patient cases improve knowledge or skills more than traditional teaching?* [Virtual patients more effectively improve skills than traditional education (pooled SMD=0.90)](../claims/vp-traditional-skills-advantage.md) [+M]
- *What supports case work online and asynchronously?* [Co-regulation shows stronger relationships with the three CoI presences than self-regulation in an online case-based course](../claims/co-regulation-stronger-presence-relationships-than-self-regulation.md) [~W]
- *Can an AI write, run or facilitate the cases?* [Case-based learning benefits depended on faculty-guided embedding, while complex cases and team workflows showed null or unfavorable effects](../claims/genai-cbl-faculty-guided-conditional-benefits.md) [~W]

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02 (maintainer's decision): claims this page cited before the 2026-10-02 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. Both claims it cited before the 2026-10-02 rewrite are now read in the model above, so none remains here.
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+W] aligns with case-based learning when the case requires integrating multiple concepts into a coherent response
- Transfer is stronger when learners articulate why a response fits the case rather than merely selecting an option [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- Facilitation matters: questioning and hints often outperform simply telling learners what the right answer was [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M] — some novices need component instruction or worked examples before cases become productive
- [Studying theoretical content with text-based cases yields a small advantage in productive scientific knowledge application over studying the same content with theoretical models](../claims/text-based-cases-small-advantage-knowledge-application.md) [+M] — attached 2026-10-18 from Baier et al. (2021), which proposed "Use text-based cases to connect scientific theory to real-world classroom situations in teacher education, but treat them as one option rather than a panacea against inert knowledge"; tests this page's relationship.
- [Both case-based and model-based interventions increase pre-service teachers' self-reported use of theory-based knowledge when analysing classroom situations](../claims/both-interventions-increase-theory-based-knowledge-usage.md) [+M] — attached 2026-10-18 from Baier et al. (2021), which proposed "Use text-based cases to connect scientific theory to real-world classroom situations in teacher education, but treat them as one option rather than a panacea against inert knowledge"; tests this page's relationship.

## Illustrative design instance and observation record

*Illustration only, invented, not a tested lesson.* A workplace session for new team leads on handling conflict between staff. The designer's objective is that each lead can recognise when a dispute is about a task rather than a relationship and choose a response that fits; one lead says she wants to stop avoiding difficult conversations. Agree that both a correct reading of a new case and a planned first conversation matter. Ask each lead to analyse one short case; most describe who was at fault and none distinguishes task from relationship. Give two further cases with different settings and the same underlying distinction, ask leads to compare all three in pairs, then state the distinction explicitly against what they found. Assess individually with a new case at the end of the session and again three weeks later, scored separately for reading the case and for the planned response.

Record: **cases and how they differ → each learner's first analysis → comparison prompts, explanation and facilitation actually given, with timing → principles learners named → candidate interpretations and confidence basis → distinguishing probe → principle statement delivered → individual analysis of a new case at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Case studies](../elements/case-studies.md), [case-based learning](../elements/case-based-learning.md), [comparing cases](../elements/comparing-cases.md), [discussion-based learning](../elements/discussion-based-learning.md), [self-explanation](../elements/self-explanation.md), [scaffolding](../elements/scaffolding.md) and [worked examples](../elements/worked-examples.md).

This pattern is scoped to lessons in which cases are analysed and compared and the principle they share is made explicit. Whole case-based curricula, cases used as unguided problems before any instruction, discussion formats judged on participation, and assessment of professional competence need distinct configurations and evidence. Apart from the virtual-patient trials pooled by Kononowicz et al. (interactive cases against traditional teaching, in the health professions), the wiki records no randomized comparison of case-based learning as a whole format with another approach, and none of online or AI-run case work against face-to-face case work; the diagnostic branches above remain to be tested with actual learners.

## Claims

- [Case-based learning benefits depended on faculty-guided embedding, while complex cases and team workflows showed null or unfavorable effects](../claims/genai-cbl-faculty-guided-conditional-benefits.md) [~W]
- [Presenting principles before case comparison yields higher germane load and lower extraneous load than presenting them after](../claims/input-before-raises-germane-lowers-extraneous-load.md) [~W]
- [Timing of instructional input (before vs. after case comparison) did not significantly affect conceptual knowledge acquisition](../claims/input-timing-no-effect-knowledge-case-comparison.md) [~W]
- [Providing key features during case comparison improves student teachers' ability to explain teacher behavior with operant conditioning principles, but not lower levels of understanding](../claims/key-features-improve-explanation-in-case-comparison.md) [+W]
- [Providing key features during case comparison reduces learning time](../claims/key-features-reduce-learning-time.md) [+W]
- [Case-based learning does not produce a larger increase in self-reported theory-based knowledge usage than studying with theoretical models](../claims/no-group-difference-theory-usage-increase.md) [-W]
- [Structure-emphasizing example sets, using varied cover stories across problem types, lead students to categorize problems by structure rather than surface features](../claims/structure-emphasizing-cover-stories-categorization.md) [+W]

## Related Patterns
- [Problem-Based Learning (PBL)](problem-based-learning.md)
- [Socratic Seminar](../elements/socratic-seminar.md)
- [Practice with Simulated People](practice-with-simulated-people.md) — when the case becomes a conversation to rehearse with a simulated or AI-played person.
- [AI Tutoring](ai-tutoring.md) — when an AI questions or responds to a learner's case analysis, and what it should hold back.
- [Mentor Support in Self-Paced Online Learning](mentor-support-in-self-paced-online-learning.md) — who reads a self-paced learner's case analyses and when they step in.

## Key Sources
- Herreid, C. F. (2011). *Case study teaching*. NSTA Press.
- Kaddoura, M. A. (2011). Critical thinking skills of nursing students in lecture-based teaching and case-based learning. *International Journal for the Scholarship of Teaching and Learning, 5*(2). [doi:10.20429/ijsotl.2011.050220](https://doi.org/10.20429/ijsotl.2011.050220)
- Hoffer, E. R. (2020). Case-based teaching: Using stories for engagement and inclusion. *International Journal on Social and Educational Sciences, 2*(2), 75-80.
- Vinney, L., Friberg, J. C., & Smyers, M. (2019). Case-based perspective-taking as a mechanism to improve metacognition and higher-level thinking. *Journal of the Scholarship of Teaching and Learning, 19*(3), 91-104. [doi:10.14434/josotl.v19i2.24006](https://doi.org/10.14434/josotl.v19i2.24006)
- Ellet, W. (2007). *The case study handbook: How to read, discuss, and write persuasively about cases*. Harvard Business School Press.
- Christensen, C. R., Garvin, D. A., & Sweet, A. (1991). *Education for judgment: The artistry of discussion leadership*. Harvard Business School Press.
- Kim, S., Phillips, W. R., Pinsky, L., Brock, D., Phillips, K., & Keary, J. (2006). A conceptual framework for developing teaching cases: A review and synthesis of the literature across disciplines. *Medical Education, 40*(9), 867-876. [https://doi.org/10.1111/j.1365-2929.2006.02544.x](https://doi.org/10.1111/j.1365-2929.2006.02544.x)
- Kononowicz, A. A., Woodham, L. A., Edelbring, S., Stathakarou, N., Davies, D., Saxena, N., Tudor Car, L., Carlstedt-Duke, J., Car, J., & Zary, N. (2019). Virtual patient simulations in health professions education: Systematic review and meta-analysis by the Digital Health Education Collaboration. *Journal of Medical Internet Research*. [https://doi.org/10.2196/14676](https://doi.org/10.2196/14676)
- Chernikova, O., Heitzmann, N., Stadler, M., Holzberger, D., Seidel, T., & Fischer, F. (2020). Simulation-based learning in higher education: A meta-analysis. *Review of Educational Research*. [https://doi.org/10.3102/0034654320933544](https://doi.org/10.3102/0034654320933544)
- Sadaf, A., Kim, S. Y., & Olesova, L. (2022). Relationship between metacognition and online Community of Inquiry in an online case-based course. *Online Learning, 26*(4), 79-93. [https://doi.org/10.24059/olj.v26i4.3474](https://doi.org/10.24059/olj.v26i4.3474)
- Liu, X., Liu, S., Lee, S.-h., & Magjuka, R. J. (2010). Cultural differences in online learning: International student perceptions. *Educational Technology & Society, 13*(3), 177-188. https://www.jstor.org/stable/jeductechsoci.13.3
- Zhang, B., et al. (2026). A sequential integrating virtual simulation and authentic video for preschool teacher candidates' observational skills training: A design-based intervention study. *PLoS One*. [https://doi.org/10.1371/journal.pone.0358951](https://doi.org/10.1371/journal.pone.0358951)

<!-- deprecated 2026-10-02: superseded by the conditional model above. Old body kept verbatim.

## Description
Case-based learning is the short-form canonical pattern for learning through analysis of realistic cases.

## Design

### Elements Used
- [Case Studies](../elements/case-studies.md)
- [Discussion-Based Learning](../elements/discussion-based-learning.md)

## Claims

- [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]
- [Multiple Contrasting Cases Support Abstraction](../claims/comparing-contrasting-cases-improves-learning.md) [+M]
-->

<!-- merged 2026-10-05 from principles/case-studiescase-based-learning ("Case Studies/Case-based Learning"), misfiled as a principle and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Case Studies/Case-based Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 11 studies (4 causal, 3 quant-synthesis, 1 review, 1 associational, 1 qualitative, 1 theoretical), `q2`–`q4` · 1 of 11 report an effect size · 2 claims rest on one study

## Description
Case studies use realistic scenarios, dilemmas, or incidents as the object of analysis so learners must interpret evidence, weigh alternatives, and justify action. Rather than receiving rules first and applying them later, learners grapple with ambiguity closer to professional practice: what matters here, what information is missing, what options are plausible, and how should a decision be defended?

## Implications
Case-based learning is powerful because it places concepts inside realistic uncertainty instead of leaving them as detached rules. When learners have to interpret evidence, justify a decision, and compare alternatives, they are more likely to build transferable judgment than when they only rehearse isolated subskills [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M]. That transfer is stronger when learners explain why their response fits the case rather than simply picking an answer [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. The tradeoff is that ambiguity can overload novices, so the strongest case designs combine realism with structure: prompts, expert modeling, staged information release, and responsive questioning that helps learners move through complexity without simply being told the answer [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M].

### Context
#### Requirements
- A well-chosen case with enough complexity to require interpretation, not just recall
- Time for analysis, discussion, and revision of judgment rather than a single quick answer
- Facilitation that pushes learners to justify claims with evidence from the case
- Clear connection between case analysis and underlying concepts, frameworks, or procedures

#### Constraints
- Poorly written or overly contrived cases reduce authenticity and invite superficial discussion
- Novices can become overwhelmed by ambiguity if cases are introduced without enough framing, vocabulary, or modeling
- Discussion can collapse into opinion-sharing unless learners are held to evidence, criteria, and reasoning
- Case learning is weaker when learners never compare their judgment to expert reasoning or later outcomes

### Target Learners
- Learners preparing for professions where judgment under uncertainty matters
- Learners developing analytical reasoning, decision-making, and argumentation
- Learners who benefit from concrete scenarios instead of abstract exposition alone
- More effective once learners have at least minimal background knowledge about the domain and its core concepts

### Target Learning Objectives
- Apply concepts to realistic, messy, and incomplete situations
- Strengthen evidence-based reasoning and decision justification
- Compare multiple interpretations or solution paths without assuming one obvious answer
- Build transfer from classroom knowledge to practice-oriented situations

### Theory
#### Supporting
- Situated and experiential perspectives support case work because learners engage with realistic situations that approximate use contexts
- Constructivist perspectives support case analysis as an active process of interpretation, comparison, and meaning-making
- Social constructivist perspectives support discussion-based case teaching where reasoning is sharpened through challenge and perspective-taking
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M] aligns with case-based learning when the case requires integrating multiple concepts into a coherent response

#### Contradicting / Qualifying
- Cases are not automatically effective for novices; some learners need models, prompts, or worked analyses before open discussion
- Transfer is stronger when learners articulate why a response fits the case rather than merely selecting an option [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- Facilitation matters: questioning and hints often outperform simply telling learners what the right answer was [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]

### Claims
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M] — cases can approximate whole-task professional reasoning better than isolated subskill drills
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — discussion and written justification improve learning when learners explain why their interpretation fits the evidence
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] — instructor probing and responsive hints improve transfer more than answer-giving alone
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M] — some novices need component instruction or worked examples before cases become productive

## Related Principles
- [Authentic Audiences & Purposes](../principles/authentic-audiences-purposes.md) — cases become stronger when decisions are framed for realistic stakeholders
- [Inquiry-based Learning](../principles/inquiry-based-learning.md) — case work often begins with uncertainty, question generation, and evidence seeking
- [Explaining Their Thinking](../principles/cognitive-activation.md) — case analysis depends on visible reasoning, not just chosen conclusions
- [Ask Experts](../principles/ask-experts.md) — expert commentary can make tacit judgment visible after learners attempt a case themselves

## Examples
<!- - Links to elements or patterns that apply this principle - ->
- [Case-Based Learning (Harvard Method)](case-based-learning.md) — structured whole-class analysis of a complex case
- [Case Studies](../strategies/case_studies.md) — localized use of real or simulated scenarios for application and discussion
- Medical diagnosis cases, business decision memos, legal briefs, and engineering incident reviews are all common implementations
- Interrupted cases, where new information is released in stages, can preserve uncertainty while creating natural decision points

## Key Sources
- Kaddoura, M. A. (2011). Critical thinking skills of nursing students in lecture-based teaching and case-based learning. *International Journal for the Scholarship of Teaching and Learning, 5*(2).
- Hoffer, E. R. (2020). Case-based teaching: Using stories for engagement and inclusion. *International Journal on Social and Educational Sciences, 2*(2), 75-80.
- Vinney, L., Friberg, J. C., & Smyers, M. (2019). Case-based perspective-taking as a mechanism to improve metacognition and higher-level thinking. *Journal of the Scholarship of Teaching and Learning, 19*(3), 91-104.
- Ellet, W. (2007). *The case study handbook: How to read, discuss, and write persuasively about cases*.
-->

<!-- merged 2026-10-15 from patterns/case-based-learning-harvard-method ("Case-Based Learning (Harvard Method)"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Case-Based Learning (Harvard Method)

> **Pattern** · [All patterns](index.md)
> **Evidence** · 4 claims (1 for, 3 mixed) · 11 studies (4 causal, 3 quant-synthesis, 1 review, 1 associational, 1 qualitative, 1 theoretical), `q2`–`q4` · 1 of 11 report an effect size · 2 claims rest on one study

## Description
Case-based learning in the Harvard method uses a carefully written case as the center of discussion, analysis, and decision making. Learners study a realistic situation, identify the central problem, weigh competing interpretations, and defend a course of action in discussion. The pattern does not treat the case as an illustration after the fact; the case is the primary vehicle through which learners reason.

This pattern is especially useful when the goal is judgment under uncertainty. It gives learners practice dealing with incomplete information, multiple stakeholders, and tradeoffs that do not have a single clean answer. The instructor's role is to orchestrate discussion so that learners justify claims, compare alternatives, and surface assumptions.

## Implications

### Context
#### Requirements
- **A well-chosen case**: The case needs enough complexity, ambiguity, and evidence to support serious analysis.
- **Structured discussion leadership**: The instructor must keep the discussion analytic rather than purely opinion-based.
- **Expectation of preparation**: Learners need time to read, annotate, and form an initial position before class.
- **Decision pressure**: Cases work best when learners must recommend or justify a response.
#### Constraints
- **Weak preparation collapses discussion**: If learners have not read or analyzed the case, the method becomes shallow.
- **Participation inequality**: A few strong voices can dominate without facilitation norms.
- **Novice uncertainty**: Learners may need more scaffolding if they lack domain knowledge or case-reading habits.
- **Not ideal for first exposure to simple procedures**: The method is stronger for reasoning than for basic memorization.
#### Grain Size
- Lesson
- Course

### Target Goals
- **Decision making under ambiguity**: Evaluating options with incomplete or conflicting evidence.
- **Professional judgment**: Learning to reason like a practitioner in context.
- **Discussion-based argumentation**: Defending claims and responding to alternatives.

### Target Learners
- **Higher education and professional learners**: Strong fit for business, law, medicine, public policy, and leadership contexts.
- **Learners preparing for complex practice**: Useful when future work involves tradeoffs and stakeholder reasoning.
- **Discussion-ready groups**: The method assumes active interpretation and participation.

### Theory
#### Supporting
- Situated learning perspectives — cases situate reasoning in realistic professional contexts.
- Social constructivist perspectives — understanding is refined through discussion and perspective comparison.
- Reflective judgment traditions — learners improve by weighing evidence and defending choices under uncertainty.
#### Contradicting / Qualifying
- Cases are stronger for analysis and judgment than for introducing large amounts of unfamiliar content.
- Instructors often need to add scaffolds for novices so discussion does not reward confidence over reasoning.

### Claims
#### Supporting
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [~M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [~S]
#### Contradicting
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M]

## Design

### Sequence
1. Assign a case and ask learners to identify the core problem, evidence, and possible actions.
2. Have learners take a position or prepare a recommendation before discussion.
3. Conduct class discussion that compares interpretations, assumptions, and tradeoffs.
4. Push learners to justify recommendations with evidence from the case.
5. Debrief the decision process and key lessons.

### Elements Used
- [Case Study](../elements/case-study.md)
- [Class Discussion](../elements/class-discussion.md)
- [Reflection](../elements/reflection.md)
- [Assessment](../elements/assessment.md)

### Affordances
- [Case Studies/Case-Based Learning](case-based-learning.md)
- [Debate](debate.md)
- [Perspective-Seeking/Multiple Perspectives](../principles/cognitive-flexibility.md)
- [Peer Discussion](../principles/peer-discussion.md)

### Personalization
- Cases can be selected for discipline, role, or stakeholder relevance.
- Learners can prepare individual positions before group discussion to broaden participation.
- Facilitation can vary from tightly guided questioning to more open Socratic exchange.

## Related Patterns
- [Problem-Based Learning (PBL)](problem-based-learning.md)
- [Socratic Seminar](../elements/socratic-seminar.md)

## Examples
- Business strategy cases where learners recommend a course of action to a leadership team.
- Clinical or legal cases in which learners interpret evidence and justify decisions.
- Public policy discussions where learners weigh stakeholder tradeoffs from a shared dossier.

## Impact
- Supports judgment, reasoning, and discussion-based professional learning.
- Most effective when preparation and facilitation make evidence use visible and accountable.

## Key Sources
- Christensen, C. R., Garvin, D. A., & Sweet, A. (1991). *Education for judgment: The artistry of discussion leadership*. Harvard Business School Press.
- Ellet, W. (2007). *The case study handbook: How to read, discuss, and write persuasively about cases*. Harvard Business School Press.
- Kim, S., Phillips, W. R., Pinsky, L., Brock, D., Phillips, K., & Keary, J. (2006). A conceptual framework for developing teaching cases: A review and synthesis of the literature across disciplines. *Medical Education, 40*(9), 867-876. [https://doi.org/10.1111/j.1365-2929.2006.02544.x](https://doi.org/10.1111/j.1365-2929.2006.02544.x)
-->
