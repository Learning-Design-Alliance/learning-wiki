---
type: element
id: simulation
aliases: [simulations]
title: Simulation
description: A simulation is an interactive model of a system or environment in which learners act, observe consequences, and iterate, learning through controlled experimentation rather than direct instruction.
canonical: true
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Simulation

> **Element** · [All elements](index.md)
> **Evidence** · 115 claims (63 for, 44 mixed, 8 against) · 87 studies (36 review, 17 quant-synthesis, 16 causal, 8 design, 5 qualitative, 3 theoretical, 2 associational), `q1`–`q4` · 20 of 87 report an effect size · 105 claims rest on one study

## Description
A simulation is an interactive model of a real or hypothetical system — physical, biological, economic, social, or procedural — in which learners take actions, observe the consequences, and adjust their approach. Unlike a [Demonstration](demonstration.md), which presents expert performance for observation, a simulation makes the learner the actor, embedding practice inside a simplified environment where errors are safe and consequences are visible.

## Design Implications

Simulations support learning by making system dynamics explorable: learners build causal mental models by manipulating variables and observing outcomes, which is difficult to convey through exposition alone [~M]. Their effectiveness depends on structure — unguided exploration of a complex simulation can overwhelm novices, so effective designs pair the environment with goals, prompts, or [Scaffolding](scaffolding.md) [~S]. Simulations are most powerful when followed by debriefing, in which learners articulate what happened and why; without debriefing, experience alone often fails to produce transferable understanding [~M].

### Context
#### Requirements
- A model whose behavior is faithful enough to the target system that inferences from it transfer
- Clear goals or challenge scenarios that direct exploration toward the learning objective
- Feedback that makes the link between actions and outcomes visible ([Feedback](feedback.md))
- A structured debrief or reflection step that converts experience into generalizable principles

#### Constraints
- Unguided discovery within a simulation is ineffective for novices; minimal-guidance exploration produces poorer learning than structured instruction [~S] — learners may draw wrong conclusions from the model or flounder without building usable schemas
- Simulations of complex systems can impose heavy extraneous load; without [Cognitive Load Management](../principles/cognitive-load-management.md), learners attend to interface mechanics rather than underlying principles
- A simplified model can teach misconceptions if its divergences from reality are not made explicit
- Fidelity costs: high-fidelity simulations are expensive to build and maintain, and added fidelity does not reliably improve learning outcomes [~W]

### Target Learners
- Novices who need to build an initial causal model of a system before formal instruction [~M]
- Intermediate learners consolidating and testing understanding through experimentation
- Learners for whom real-world practice is dangerous, expensive, slow, or ethically impossible (e.g., flight, surgery, emergency response)
- Less beneficial for learners with strong prior knowledge, who may extract little from guided exploration [Expertise reverses the benefit of instructional guidance.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Conceptual understanding of dynamic systems and causal relationships
- Procedural fluency and decision-making under realistic constraints
- Transfer: applying principles across varied scenarios by experiencing multiple cases
- Diagnosis and troubleshooting: interpreting system states and responding

### Affordances
- [Active Learning](../principles/active-learning.md) — simulation enacts this principle by requiring learners to generate actions and predictions rather than receive explanations; the environment responds to what the learner does, not what the learner is told
- [Scaffolding](../principles/scaffolding.md) — simulations can stage complexity, starting with few variables and adding them as competence grows; [Fading](fading.md) applies naturally by progressively removing hints, prompts, and constraints
- [Cognitive Load Management](../principles/cognitive-load-management.md) — a well-designed simulation strips away irrelevant real-world complexity, letting learners attend to the variables that matter
- [Feedback](feedback.md) — the simulation's response to learner actions is immediate, task-level feedback; effectiveness rises when debriefing elevates it to the process level [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- [Simulations/Immersive Virtual Environments](../principles/simulations-immersive-virtual-environments.md)
- [Experiential Learning](../principles/experiential-learning.md)

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [+S]
- [Teacher-guided inquiry outperforms student-led](../claims/teacher-guided-inquiry-outperforms-student-led.md) [+S]
- [Expertise reversal: guidance hurts experts](../claims/expertise-reversal-effect.md) [~S]
- [Simulation-based education with deliberate practice improves clinical outcomes](../claims/simulation-based-education-with-deliberate-practice-improves-clinical-outcomes.md) [+M]
- [Simulation-based education improves outcomes](../claims/simulation-based-education-improves-outcomes.md) [+M]
- [Physical experience enhances science learning](../claims/physical-experience-enhances-science-learning.md) [~M]
- [Virtual simulation stimulated higher self-reported purposefulness than authentic video](../claims/vs-higher-purposefulness-reflection.md) [+M]
- [Authentic video outperformed virtual simulation on analysis and support dimensions](../claims/av-advantage-analysis-support-dimensions.md) [-M]
- [Pretraining improves transfer](../claims/pretraining-improves-transfer.md) [+M]
- [Feedback improves learning](../claims/feedback-improves-learning.md) [+S]
- [Students find computer-based simulation feedback insufficient](../claims/simucase-feedback-insufficient.md) [+M]
- [Graduate SLP students perceive the simulation's learning mode as highly beneficial](../claims/simucase-learning-mode-perceived-beneficial.md) [+M]
- [Reflective practice improves outcomes when structured](../claims/reflective-practice-improves-outcomes-when-structured.md) [+S]
- [Students perceive debriefing as among the most beneficial components of a simulated clinical course](../claims/debriefing-psychometric-instruction-valued.md) [+M]
- [The closer training content is to authentic clinical scenarios, the smoother its translation into practice](../claims/contextualized-teaching-facilitates-transfer.md) [+W]
- [Students recommend integrating computer-based simulation cases into each course to make learning more concrete](../claims/students-recommend-simulation-in-each-course.md) [+W]
- [In a qualitative pilot with 10 speech-language pathology graduate students, most felt the Simucase assessment cases lacked authenticity because they included too few behavioral modifications](../claims/simucase-lacks-behavioral-authenticity.md) [-W]
- [Adaptive AI feedback provides tailored scaffolding and AI simulates authentic interaction scenarios (Contextual Affordance Pathway)](../claims/ai-contextual-affordances-scaffolding-simulation.md) [+M]
- [AI-enhanced simulation in high-acuity nursing training improves clinical confidence and emergency preparedness](../claims/ai-simulation-improves-clinical-confidence-nursing.md) [+W]
- [LLMs help bridge the gap between theoretical curricula and real-world skills by creating simulated scenarios, cases and problem contexts that are hard to reproduce in traditional classrooms](../claims/llm-simulations-bridge-theory-practice-gap.md) [+W]
- [Expert evaluation found the virtual patient realistic and immediate ACT feedback increased therapists' awareness of intervention choices](../claims/expert-evaluation-realism-and-feedback-awareness.md) [+W]
- [AI-generated and prebuilt simulations produced higher immediate conceptual-assessment scores than physical laboratory work, but the advantage did not persist in later examinations](../claims/simulation-advantage-immediate-not-sustained.md) [+W]
- [Learner acceptance of AI simulations is generally high, with System Usability Scale scores of 61.6 to 78.56 and 72%-93% willingness to recommend](../claims/ai-simulation-high-learner-acceptance.md) [+W]
- [In the pilot, 93% of students found controlling the wave in the air natural and 86% reported feeling more engaged and focused than in regular learning](../claims/ar-gesture-control-felt-natural-and-increased-engagement-pilot.md) [+W]
- [Low-equity participants' simulation responses converged over successive simulations toward those of a high-equity reference group](../claims/low-equity-participants-converge-toward-high-equity-responses.md) [~W]
- [The CATALST simulation-based statistics course achieved a high pass rate comparable to or better than the traditional course at the same institution](../claims/catalst-pass-rate-comparable-to-traditional.md) [+W]
- [In one reviewed study, Anatomage virtual dissection increased medical student engagement by 34% over cadaver-based practice, constrained by equipment costs exceeding $72,000 per station](../claims/anatomage-vr-engagement-34-percent.md) [~W]
- [Overall 3E, Empower, and Empathize scores were higher in the second AI-patient encounter, but the uncontrolled design precludes attributing this to training](../claims/session2-3e-scores-higher-uncontrolled.md) [~W]
- [AI-driven case simulations in ambulatory settings support diagnostic reasoning and anticipatory thinking in nursing education](../claims/ai-ambulatory-case-simulations-diagnostic-reasoning.md) [+W]
- [Controlled GenAI virtual-patient and communication studies reported short-term skill gains, but positive findings were not universal](../claims/genai-virtual-patient-short-term-gains-mixed.md) [~W]
- [AI-powered simulations show short-term gains in communication confidence and structured knowledge in RCTs, with limited or inferior effects for tactile psychomotor skills](../claims/ai-simulation-short-term-gains-nursing.md) [~W]
- [Persistent technical limitations constitute an authenticity gap in AI-powered nursing simulations](../claims/ai-simulation-authenticity-gap.md) [~W]
- [Simulation-response convergence was corroborated by survey-based changes in mindsets and practices and by human rater ratings for Roster Justice](../claims/convergence-corroborated-by-surveys-and-human-raters.md) [~W]
- [Domain-specific challenges and authentic environmental prompting in the VR simulation fostered both experiential and vicarious learning of teaching](../claims/vr-authentic-prompting-fosters-experiential-vicarious-learning.md) [+W] — attached 2026-10-18 from Ke et al. (2021), which proposed "Multiuser VR-supported teaching simulation for participatory training of student instructors".
- [Topic complexity moderates the simulation advantage: the multidimensional Baltic Sea topic showed a much larger simulation benefit than the one-dimensional ocean acidification topic](../claims/complexity-moderates-simulation-advantage.md) [+W]
- [CVS skill is the strongest predictor of performing valid (unconfounded) experiments in simulation-based inquiry](../claims/cvs-predicts-proportion-valid-experiments.md) [~W]
- [Simulator feedback responds authentically to student error, e.g. logs fall from the cargo when the grapple is opened incorrectly.](../claims/simulator-authentic-error-feedback-log-drops.md) [+W]
- [The simulation advantage and interest differences hold across subgroups of age, gender, school form, and grade](../claims/no-subgroup-differences-method-comparison.md) [+M]
- [In an open simulation game, third-order interventions effectively evoked third-order responses](../claims/open-sg-tol-interventions-elicit-tol-responses.md) [~W]
- [Secondary school students learn more complex marine ecology content from interactive computer simulations than from hands-on experiments, with a larger advantage for the more complex multidimensional topic](../claims/simulations-beat-experiments-complex-content-knowledge.md) [+W]
- [Support conditions did not differ from control in learning scores within the environment](../claims/no-condition-differences-learning-scores-swlep.md) [~W]
- [Both physical and virtual training conditions produced equal gains in children's explicit verbal knowledge of the control of variables strategy](../claims/explicit-cvs-knowledge-equal-conditions.md) [~W]
- [Virtual labs showed a limitation in helping students transfer what they learned from teacher demonstration to new inquiry contexts](../claims/virtual-lab-transfer-from-demonstration-limited.md) [-W]
- [In a medical ABC-VR case, 12 of 14 students met the required learning goals of a post-VR mock knee exam](../claims/abc-vr-medical-case-12-of-14-met-goals.md) [+W]
- [The advantage of simulation games shrinks or reverses when the comparison group learns via active instructional methods](../claims/active-comparison-instruction-reverses-simulation-game-advantage.md) [~M]
- [Independent expert teachers accepted 86% of generated STEM learning interactives, rating most as good or excellent, with biology simulations weakest on aesthetics and UX](../claims/expert-rating-40-requests-86-percent-acceptance.md) [~W]
- [In an open simulation game with wide scope and low distance, second-order interventions effectively elicited second-order responses](../claims/open-sg-sol-interventions-elicit-sol-responses.md) [~W]
- [Published studies of simulation games report substantially larger effects than unpublished studies, indicating publication bias](../claims/publication-bias-in-simulation-games-research.md) [~M]
- [In simulations, superficial reflection stays at consistently low frequency across all reflection-reward levels, and misuse remains negligible, indicating the main governance challenge is normalised opportunistic AI use rather than overt misconduct](../claims/superficial-reflection-low-misuse-negligible.md) [~W]
- [Simulation games are more effective when they actively rather than passively convey course material](../claims/simulation-games-effective-when-instruction-active.md) [+W]
- [Student satisfaction with virtual patients is generally positive, with item-level comparisons dominating and some confidence exceptions](../claims/vp-satisfaction-generally-positive.md) [+W]
- [Adaptable task progression is descriptively more beneficial than fixed task progression in simulation-based learning](../claims/adaptable-task-progression-higher-effects.md) [~W]
- [VR improved movement-based transfer test performance versus reading in security training, while learning in VR without the possibility to act was detrimental](../claims/vr-transfer-benefit-but-actionless-vr-detrimental.md) [+W]
- [Performance during the virtual pipetting lesson predicts real-life transfer test performance](../claims/in-lesson-performance-predicts-real-life-transfer.md) [+W]
- [In Desktop-VR, interaction format (object movement vs. camera movement vs. no interaction) showed no significant main effect on learning outcomes](../claims/no-main-effect-interaction-format-desktop-vr.md) [~W]
- [Skill level and simulator technology interact on the CoV of LPMC-to-RPMC directed connectivity, in opposite directions for experts and novices](../claims/cov-lpmc-rpmc-interaction-experts-novices.md) [~W]
- [Simulator technology (physical vs VR) significantly affects directed connectivity from RPFC to LPMC, with higher flow in the VR simulator](../claims/simulator-technology-rpfc-lpmc-connectivity.md) [~W]
- [Skill level interacts with simulator technology on directed connectivity from LPMC to RPFC and SMA to LPFC](../claims/skill-by-simulator-interaction-connectivity.md) [~W]
- [Immersive VR L2 vocabulary learning outperforms word-to-word association, especially for struggling learners, with manipulable-context words learned better](../claims/ivr-vocabulary-beats-association-strugglers-gain-more.md) [+W]
- [In two minimally-guided PhET simulation activities, spectral clustering consistently identifies a larger systematic-inquiry cluster and a smaller free-exploration cluster across all three feature paradigms](../claims/systematic-free-inquiry-clusters-simulations.md) [~W]
- [Most learners (68%) maintain the same inquiry-strategy cluster across two different simulations, indicating stable rather than task-specific approaches](../claims/inquiry-cluster-stability-across-simulations.md) [~W]
- [Systematic inquiry behavior is associated with gaining quantitative understanding of simulation variables, while free exploration is associated with only qualitative understanding](../claims/systematic-strategy-quantitative-understanding.md) [~W]
- [In an authentic vocational classroom setting, a lesson orchestrated around an iVR serious game produced significantly stronger factual knowledge gains than a student video design control group](../claims/ivr-authentic-classroom-factual-knowledge-gains.md) [+M] — attached 2026-10-28 from P. Spangenberger et al. (2025), which proposed "MARLA: a curriculum-aligned iVR serious game for offshore wind energy troubleshooting"; tests this page's relationship.
- [No difference in troubleshooting transfer (flashlight task) between the iVR and control groups](../claims/ivr-authentic-classroom-no-transfer-difference.md) [-W]
- [Patient simulation is the most prevalent role in higher education, concentrated in medical training contexts](../claims/higher-education-patient-simulator-role.md) [~W]
- [An LX design integrating an immersive VR simulation in an inquiry-based Physics learning environment was enacted with 109 high-school students and evaluated for conceptual learning gains](../claims/lx-design-immersive-vr-special-relativity-109-students.md) [+W] — attached 2026-10-29 from Yiannis Georgiou et al. (2023), which proposed "Immersive VR simulation of the Special Theory of Relativity for high-school Physics".
- [Simulated embodied experience in a virtual environment accelerated Chinese vocabulary learning more than a traditional web-based context](../claims/ve-context-accelerates-chinese-vocabulary-learning.md) [+W]
- [Teacher candidates moved from abstract inclusivity ideals to specific instructional and relational strategies after the simulation](../claims/simulation-shift-abstract-to-actionable-inclusivity.md) [+M] — attached 2026-10-29 from Hoda Harati et al. (2026), which proposed "Building Inclusive Classrooms simulation (SchoolSims platform)"; tests this page's relationship.
- [The simulation increased teacher candidates' confidence and self-efficacy for addressing sensitive topics, but did not alleviate concerns about parent and administrator backlash](../claims/simulation-confidence-gain-persistent-backlash-concerns.md) [~M] — attached 2026-10-29 from Hoda Harati et al. (2026), which proposed "Building Inclusive Classrooms simulation (SchoolSims platform)"; tests this page's relationship.
- [Teacher educators found the simulation fostered critical thinking and reflection but faced integration, accessibility, and binary-decision limitations](../claims/teacher-educators-simulation-value-and-challenges.md) [~M] — attached 2026-10-29 from Hoda Harati et al. (2026), which proposed "Building Inclusive Classrooms simulation (SchoolSims platform)".
- [A review reports that IVR serious-game training gave better airplane-evacuation spatial knowledge than safety cards in one study, and that in a separate spacecraft-evacuation study the body orientation used in training shaped which spatial skills were learned](../claims/ivr-sgs-spatial-knowledge-evacuation.md) [+W]
- [IVR serious games validate evacuation facility designs, with participants preferring green and white flashing exit-portal lights](../claims/ivr-sgs-evacuation-facility-validation.md) [+W]
- [IVR serious games show that other evacuees strongly influence participants' evacuation behavior](../claims/ivr-sgs-social-influence-evacuation-behavior.md) [~W]
- [Haptic virtual reality simulation reduces procedural time for pulpotomy training compared with conventional simulators](../claims/ir-reduces-procedural-time-dental.md) [+W] — attached 2026-10-31 from Ruslin Muhammad et al. (2026), which proposed "Haptic VR dental simulators (SIMtoCARE dente, Simodont, VirtEasy, Omni haptic) used for preclinical dental skill training".
- [Most learner-facing studies of technology-enhanced simulation in laparoscopic training report favorable learner responses, mainly confidence, satisfaction, perceived safety and self-efficacy](../claims/simulation-laparoscopic-favorable-perceptions.md) [+M] — attached 2026-10-31 from Vega Ochoa AD et al. (2026), which proposed "Corpus of 11 included studies on student perceptions of laparoscopic simulation (2020-2025)".
- [VR simulator training yields a higher rate of optimal (Grade I) pedicle screw placement than traditional training among residents and early-career surgeons](../claims/vr-training-higher-grade-i-pedicle-screw-placement.md) [+W] — attached 2026-10-31 from Pasqualotto Eric et al. (2026), which proposed "Virtual reality surgical simulators for pedicle screw placement training (ImmersiveSimTM, VSTS, IVRSS-PSP)"; tests this page's relationship.
- [VR-trained trainees show shorter screw penetration distances and fewer displaced screws per resident](../claims/vr-training-shorter-penetration-fewer-displaced-screws.md) [+W] — attached 2026-10-31 from Pasqualotto Eric et al. (2026), which proposed "Virtual reality surgical simulators for pedicle screw placement training (ImmersiveSimTM, VSTS, IVRSS-PSP)"; tests this page's relationship.
- [Increasing the proportion of simulation within a nursing course shows mixed effects on competency outcomes (Hayden et al. trial)](../claims/more-vs-less-simulation-mixed.md) [~W]
- [Virtual haptic drilling training achieved outcomes similar to conventional practice in less time in restorative dentistry](../claims/ir-shortens-dental-training-duration.md) [~W]
- [IR-based surgical training improved novice surgeons' self-confidence in oral surgery studies](../claims/ir-boosts-novice-surgeon-confidence.md) [+W]
- [High-fidelity manikins and virtual reality were the most common paediatric SBE modalities across the reviewed studies](../claims/high-fidelity-manikins-vr-most-common-modalities.md) [~W]
- [Where cost was studied, AI-generated virtual patients showed savings from obviating faculty time and human standardized patients, but cost evaluation remains sparse and none reached Kirkpatrick level 4](../claims/ai-virtual-patient-cost-savings-sparse-evidence.md) [~W]
- [Across the reviewed studies, simulation-based interventions consistently improved paediatric undergraduate learning outcomes, including clinical reasoning, procedural skills and confidence](../claims/sbe-consistently-improved-paediatric-ume-outcomes.md) [+W]
- [Simulation-based education consistently improved nurses' confidence in delirium recognition and assessment across included studies](../claims/sbe-delirium-confidence-gains.md) [+W]
- [Simulation-based education plus clinical teaching compared to clinical teaching only shows a large pooled advantage (SMD 0.82) in undergraduate nursing students](../claims/sbe-plus-clinical-pooled-smd-0-82.md) [+W]
- [Simulation-based education compared to patient-based clinical teaching alone shows a large pooled advantage in objectively assessed outcomes in undergraduate nursing students](../claims/sbe-vs-clinical-pooled-smd-0-96.md) [+W]
- [Simulation-based education combined with workflow redesign improved ICU nurses' delirium-assessment documentation rates on day and night shifts](../claims/sbe-delirium-documentation-improvement-icu.md) [+W]
- [Virtual laboratories match physical laboratories on conceptual mastery, with domain-specific advantages and disadvantages](../claims/virtual-matches-physical-conceptual-mastery.md) [~W]
- [Simulation dominates the literature on obstetric emergency knowledge-building, but evidence for sustained behaviour change and clinical impact remains limited](../claims/simulation-dominates-oe-training-limited-clinical-impact.md) [~W]
- [AccuTouch VR simulator training improved live fibreoptic intubation performance in inexperienced paediatric residents, reducing time to intubation from 5.15 to 0.88 minutes](../claims/accutouch-training-improves-live-intubation-time.md) [+W]
- [IVR simulation significantly improves nursing students' knowledge acquisition with a small-to-medium effect](../claims/ivr-improves-nursing-knowledge-acquisition.md) [+W]
- [Most digital teaching methods demonstrated positive effects on practical skills acquisition, particularly simulation-based, VR-supported or interactive formats, but effect magnitude and consistency varied substantially](../claims/digital-methods-mostly-positive-practical-skills-effects.md) [+W]
- [Training on a simple low-fidelity 'choose-the-hole' bench model transferred to real clinical fibreoptic intubation performance in an RCT](../claims/choose-the-hole-bench-model-predictive-validity-rct.md) [+W]
- [IVR simulation does not significantly improve nursing students' skill performance](../claims/ivr-no-significant-skill-performance-effect.md) [-W]
- [All three ECE modalities show significant positive effects, with real clinical interactions showing the largest pooled effect](../claims/ece-types-subgroup-effects.md) [~W]
- [Predictive validity of airway simulators is rarely evaluated, and the two tracheal-intubation studies assessing it found no improvement in real-world neonatal intubation outcomes after simulator training](../claims/airway-simulator-predictive-validity-rarely-shown.md) [-W]
- [Adverse effects of IVR simulation in nursing education are generally mild visual and vestibular symptoms](../claims/ivr-adverse-effects-mild-visual-vestibular.md) [~W]
- [Feedback during distance simulation improved performance, while one at-home robotic surgery practice program showed no improvement](../claims/feedback-benefits-at-home-practice-null.md) [+W]
- [Learner perceptions of GenAI-supported virtual patients were positive across 14 of the 15 reviewed studies](../claims/genai-vp-positive-learner-perceptions.md) [+W]
- [Front-of-neck access simulators are severely under-validated, with only one study meeting inclusion criteria, and real-world predictive validity cannot ethically be evaluated for FONA](../claims/fona-simulators-undervalidated-single-study.md) [-W]
- [In an RCT reviewed by this study, an LLM-based digital patient improved ophthalmology medical history-taking skills relative to control](../claims/llm-digital-patient-improves-history-taking-rct.md) [+W]
- [Manikin-based simulation produced equal or superior competency outcomes versus traditional clinical practice, except in the Patient Safety domain](../claims/manikin-simulation-competency-versus-clinical.md) [+W]
- [Two included studies allowed participants to act on feedback from an earlier simulation attempt, enabling a 'second go'](../claims/second-go-feedback-iteration-simulation.md) [~W]
- [Performance-based assessments dominate the studied assessments in entry-level physical therapy education, with simulation-based the most common format](../claims/pt-education-assessments-performance-based-dominant.md) [+W]
- [Virtual simulation teaching enhances learning outcomes and deepens professional cognition through repeated practice, trial-and-error, and error-correction feedback](../claims/vs-advantages-learning-outcomes.md) [+W]
- [High-fidelity simulation improves ECT procedural skills substantially but does not reliably improve theoretical knowledge or confidence](../claims/hfs-ect-procedural-skills.md) [~W]
- [Single-group studies uniformly reported improvement after distance simulation training in self-assessment, knowledge, or skills](../claims/single-group-prepost-all-improved.md) [~W]
- [Included studies used a varied range of simulation modalities, from Deaf standardized patients to VR with manipulated audio and 360 video](../claims/varied-simulation-modalities-deaf-patient-education.md) [+W]
- [A minority of nursing students report negative emotional responses to virtual simulation teaching, including fear, anxiety, and burnout](../claims/vs-negative-emotional-experiences.md) [~W]
- [Validation quality does not consistently correlate with simulator fidelity, and high-fidelity VR simulators' superiority over simpler models for fibreoptic intubation has not been demonstrated](../claims/simulator-fidelity-does-not-track-validation-quality.md) [-W]
- [Adding task interruptions to ALS simulation to increase realism did not improve technical or non-technical performance, including at 3-month retention](../claims/task-interruptions-no-performance-benefit.md) [~W]
- [A social robotic LLM-enhanced virtual patient was rated higher than a conventional computer-based platform for authenticity and learning effect](../claims/robotic-vp-higher-authenticity-than-computer-platform.md) [~W]

## Design Decisions
<!-- Decision section (2026-09-30 pilot): drafted from the linked claim pages only; every choice
     cites the claims that settle it, with markers capped by each claim's recorded evidence. -->

### How much guidance should learners get inside the simulation?
- **Default:** give novices structure — goals, prompts, feedback, worked examples — rather than leaving them to discover the model's rules unaided; explicit instruction beat unassisted discovery (d = 0.38, 580 comparisons), while discovery enhanced with feedback, worked examples or scaffolding beat other instruction (d = 0.30) — [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [+S], [Guided discovery outperforms pure discovery](../claims/minimal-guidance-less-effective-for-novices.md) [+S]
- **Default:** in inquiry settings, teacher-led guidance outperformed student-led conditions by about .40 in effect size (37 studies, overall g = .50) — [Teacher-guided inquiry outperforms student-led](../claims/teacher-guided-inquiry-outperforms-student-led.md) [+S]
- **Changes when:** learners already hold the relevant schemas → fade the guidance; formats that help novices lost their advantage, and in several paradigms reversed, for more experienced learners — [Expertise reversal: guidance hurts experts](../claims/expertise-reversal-effect.md) [~S]
- **Tested with:** meta-analyses of discovery and inquiry learning (largely school science), 112 third- and fourth-graders learning experimental design, electrical trainees reading circuit diagrams; none of these claims tests guidance levels inside a simulation specifically.
- **Not settled:** how fast to fade guidance within a simulation, and whether the discovery findings carry over unchanged to interactive models; no wiki claim tests it.

### What should the simulation be built around?
- **Default:** repeated, goal-directed practice with mastery standards and immediate feedback; simulation-based medical education with deliberate practice beat traditional clinical education (d = 0.71, 14 studies, mostly procedural skills) — [Simulation-based education with deliberate practice improves clinical outcomes](../claims/simulation-based-education-with-deliberate-practice-improves-clinical-outcomes.md) [+M]
- **Default:** against no intervention, technology-enhanced simulation gave large pooled effects on knowledge and skills (g ≈ 1.09–1.20) and a moderate one on direct patient outcomes (g = 0.50, k = 32) — [Simulation-based education improves outcomes](../claims/simulation-based-education-improves-outcomes.md) [+M]
- **Changes when:** the comparison is equally long non-simulation practice → the no-intervention meta-analysis cannot say, and its subgroup analyses found no consistent interaction with feedback, repetition, mastery learning, distributed practice or curricular integration — [Simulation-based education improves outcomes](../claims/simulation-based-education-improves-outcomes.md) [~M]
- **Tested with:** physicians, nurses, dentists and other health-professions trainees (609 studies, 35,226 trainees; 14 studies for the deliberate-practice comparison).
- **Not settled:** which design features drive the effect, how durable gains are, dose–response for amount of practice, and cost against low-fidelity alternatives; both claim pages list these as open.

### How realistic does the simulation need to be?
- **Default:** a virtual model can stand in for physical materials for conceptual learning; physical, virtual and combined manipulation of heat-and-temperature experiments were equally effective and all beat traditional instruction — [Physical experience enhances science learning](../claims/physical-experience-enhances-science-learning.md) [~M]
- **Changes when:** the goal is reflecting on the situation → a simplified virtual simulation gave higher self-reported purposefulness of reflection than authentic video (d = 0.507) — [Virtual simulation stimulated higher self-reported purposefulness than authentic video](../claims/vs-higher-purposefulness-reflection.md) [+M]
- **Changes when:** the goal is analysing rich real situations → authentic video outscored the simplified simulation on the analysis and support dimensions of observation assignments — [Authentic video outperformed virtual simulation on analysis and support dimensions](../claims/av-advantage-analysis-support-dimensions.md) [-M]
- **Tested with:** 234 undergraduates in physics (physical vs virtual); 34 preschool teacher candidates in 8 groups in one design-based study (simulation vs video), which is one small study.
- **Not settled:** fidelity levels in procedural or clinical simulation; no wiki claim compares high- and low-fidelity versions of the same simulation, so the Constraints line above on fidelity cost rests on no recorded study.

### What should learners get before the simulation?
- **Default:** a short primer naming the parts and functions of the system; a pretraining video before an immersive-VR procedural lesson gave better knowledge scores and fewer errors on a real-world transfer task, with lower reported load — [Pretraining improves transfer](../claims/pretraining-improves-transfer.md) [+M]
- **Tested with:** 93 participants learning a micropipette procedure in VR; one randomised experiment, read as an abstract, no effect size.
- **Not settled:** whether pretraining is redundant for learners who already know the terms (the claim page expects so but records no test), and whether gains last to delayed tests.

### What feedback should the simulation itself give?
- **Default:** say why a response is wrong, not only that it is; high-information feedback (d = 0.99) far outperformed reinforcement or punishment (d = 0.24), and over a third of feedback interventions lowered performance — [Feedback improves learning](../claims/feedback-improves-learning.md) [+S]
- **Default:** students in a computer-based clinical simulation found right/wrong marking without reasoning not beneficial — [Students find computer-based simulation feedback insufficient](../claims/simucase-feedback-insufficient.md) [+M]
- **Default:** let learners retry cases without grade penalty; students rated an unlimited-attempts learning mode highly beneficial — [Graduate SLP students perceive the simulation's learning mode as highly beneficial](../claims/simucase-learning-mode-perceived-beneficial.md) [+M]
- **Tested with:** 435 education studies and 607 effect sizes across settings (feedback); 10 speech-language pathology graduate students in one focus-group pilot (the two simulation claims, which report perceptions, not learning).
- **Not settled:** immediate versus end-of-scenario feedback inside a simulation; no wiki claim tests it.

### What should follow the simulation?
- **Default:** a structured reflection with specific prompts rather than a generic invitation; metacognitive-reflection prompts were the strongest moderator in 48 writing-to-learn studies (b = 0.48), and specific prompts beat generic ones for 208 engineering students — [Reflective practice improves outcomes when structured](../claims/reflective-practice-improves-outcomes-when-structured.md) [+S]
- **Default:** students in a simulated clinical course named the weekly debriefing among its most beneficial parts — [Students perceive debriefing as among the most beneficial components of a simulated clinical course](../claims/debriefing-psychometric-instruction-valued.md) [+M]
- **Tested with:** school writing-to-learn studies and a first-year engineering course (structured reflection); 10 SLP graduate students (debriefing, perception only).
- **Not settled:** no wiki claim compares a simulation with and without a debrief; see [Debrief](debrief.md) for the debrief's own decisions.

## The evidence by question
- *Does practising in a simulation improve knowledge and skill more than no simulation or conventional training, and for which skills and horizons?* [Simulation Based Education Improves Outcomes](../claims/simulation-based-education-improves-outcomes.md) [+M]
- *How much guidance should learners get while they explore a simulation, and does the answer change with what they already know?* [Supplementing simulation-based inquiry with learner guidance has a modest effect on learning outcomes (d = 0.49) and inquiry skills (d = 0.41), independent of guidance type (review attribution to D'Angelo et al., 2014)](../claims/guidance-improves-inquiry-learning-outcomes.md) [+M]
- *Can a virtual simulation stand in for physical materials or authentic situations, and what does each format do better?* [Physical Experience Enhances Science Learning](../claims/physical-experience-enhances-science-learning.md) [~M]

## Related Elements
- [Practice](practice.md) — simulation is a structured environment for deliberate practice with built-in consequences
- [Case Studies](case-studies.md) — a case presents a snapshot of a system; a simulation lets learners intervene in it
- [Coaching](coaching.md) — instructor or system guidance during simulation attempts
- [Fading](fading.md) — progressively removing scaffolds within the simulation as expertise grows
- [Feedback](feedback.md) — the core mechanism through which simulation actions become learning
- [Scenario-Based Learning](scenario-based-learning.md)
- [Role-Playing](role-playing.md)

## Patterns That Use This Element
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — simulation provides the exploration and articulation phases in a safe environment
- [Case-Based Learning](../patterns/case-based-learning.md) — interactive cases extend static cases into consequential decision-making [Case-based learning improves exam performance.](../claims/case-based-learning-improves-exam-performance.md) [+M]
- [Anchored Instruction](../patterns/anchored-instruction.md) — simulations serve as the anchor problem context in which knowledge is applied

## Examples

**[PhET Interactive Simulations](https://phet.colorado.edu)** — Research-based physics, chemistry, and math simulations (e.g., *Circuit Construction Kit*) with guided-inquiry activity sheets; studies show conceptually targeted sims outperform real equipment demonstrations for building circuit understanding.

**[SimSchool](https://simschool.org)** — A classroom simulation in which teacher candidates practice instructional decisions and see simulated student responses, bridging coursework and live teaching.

**[Flight simulators](https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afs/afs200)** — The canonical high-fidelity example; FAA-approved simulators substitute for substantial flight hours, illustrating how simulation enables safe practice of high-stakes procedures.

**[NetLogo](https://ccl.northwestern.edu/netlogo)** — Agent-based modeling environment used in science education for learners to build and perturb models of complex systems (epidemics, ecosystems), supporting exploration of emergent behavior.
- [Embed puzzles and challenges in simulations for continued engagement and self-assessment](../strategies/embed-puzzles-and-challenges-in-sims.md)
- [Use simulation as a non-threatening alternative to direct experimentation when testing office reorganizations](../strategies/simulation-as-non-threatening-experimentation-alternative.md)
- [Embed the ReACT reasoning-acting-observing-reflecting cycle in tutoring systems to mirror inquiry-based learning](../strategies/react-cycle-inquiry-based-learning.md)
- [Use fidelity-aware simulated patients as a low-risk complement to supervision for deliberate psychotherapy practice](../strategies/fidelity-aware-simulated-patients-deliberate-practice.md)
- [Implement AI simulations as complements within a stepped simulation continuum, with layered interaction modes and blended feedback](../strategies/stepped-ai-simulation-integration-strategies.md)
- [Vocational education programs should let trainees experience and reflect on authentic errors, e.g. via error management training and negative knowledge-diaries](../strategies/error-management-training-negative-knowledge-diaries.md)
- [Deliver a short post-exploration instructional video to complement science simulations](../strategies/short-post-simulation-video-strategy.md)
- [Implement modelling as short, computer-simulation-supported activities at the high school level](../strategies/short-computer-supported-high-school-modelling-activities.md)
- [Integrate AI-driven simulation into dental curricula as a complement to traditional training, attending to domain-specific effectiveness and the lack of long-term validated outcomes](../strategies/ads-curricular-integration-strategy.md)

## Key Sources
- Garris, R., Ahlers, R., & Driskell, J. E. (2002). Games, motivation, and learning: A research and practice model. *Simulation & Gaming, 33*(4), 441–467. [doi:10.1177/1046878102238607](https://doi.org/10.1177/1046878102238607)
- Finkelstein, N. D., Adams, W. K., Keller, C. J., Kohl, P. B., Perkins, K. K., Podolefsky, N. S., Reid, S., & LeMaster, R. (2005). When learning about the real world is better done virtually: A study of substituting computer simulations for laboratory equipment. *Physical Review Special Topics — Physics Education Research, 1*(1), 010101. [doi:10.1103/physrevstper.1.010103](https://doi.org/10.1103/physrevstper.1.010103)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Issenberg, S. B., McGaghie, W. C., Petrusa, E. R., Lee Gordon, D., & Scalese, R. J. (2005). Features and uses of high-fidelity medical simulations that lead to effective learning: A BEME systematic review. *Medical Teacher, 27*(1), 10–28. [doi:10.1080/01421590500046924](https://doi.org/10.1080/01421590500046924)
- Wouters, P., van Nimwegen, C., van Oostendorp, H., & van der Spek, E. D. (2013). A meta-analysis of the cognitive and motivational effects of serious games. *Journal of Educational Psychology, 105*(2), 249–265. [doi:10.1037/a0031311](https://doi.org/10.1037/a0031311)
- de Freitas, S. (2006). Learning in immersive worlds. JISC.

<!-- merged 2026-10-09 from elements/simulations ("Simulations"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Simulations

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (4 for, 1 against) · 4 studies (2 quant-synthesis, 2 qualitative), `q1`–`q4` · 2 of 4 report an effect size · 5 claims rest on one study

## Description
Simulations are the element in which learners engage with realistic, model-based scenarios that approximate authentic systems or environments.

## Design Implications

### Affordances
- [Simulations/Immersive Virtual Environments](../principles/simulations-immersive-virtual-environments.md)
- [Experiential Learning](../principles/experiential-learning.md)

### Claims
<!- - Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] - ->
- [Simulation Based Education Improves Outcomes](../claims/simulation-based-education-improves-outcomes.md) [+M]
- [The closer training content is to authentic clinical scenarios, the smoother its translation into practice](../claims/contextualized-teaching-facilitates-transfer.md) [+W]
- [Students recommend integrating computer-based simulation cases into each course to make learning more concrete](../claims/students-recommend-simulation-in-each-course.md) [+W]
- [In a qualitative pilot with 10 speech-language pathology graduate students, most felt the Simucase assessment cases lacked authenticity because they included too few behavioral modifications](../claims/simucase-lacks-behavioral-authenticity.md) [-W]
- [Simulation Based Education With Deliberate Practice Improves Clinical Outcomes](../claims/simulation-based-education-with-deliberate-practice-improves-clinical-outcomes.md) [+W]

## Related Elements
- [Scenario-Based Learning](scenario-based-learning.md)
- [Role-Playing](role-playing.md)

## Key Sources
- de Freitas, S. (2006). Learning in immersive worlds. JISC.
-->
