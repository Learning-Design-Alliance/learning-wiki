---
type: principle
id: competency-based-assessment
moved_from: [pattern/grading-by-contract-fricke]
aliases: [competency-based-learning-assessment, performance-based-teacher-certification-assessment]
title: Competency-Based Assessment
description: "Scoring a learner's response on a task that represents the intended capability against explicit criteria and a stated threshold, by consistent assessors, is expected to support better teaching, progression and certification decisions than a rank or seat time, though no claim here tests that comparison and assessor agreement is not guaranteed."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
sources:
  - id: henri-2017
    resource: "https://doi.org/10.1002/jee.20180"
    title: "Henri, M., Johnson, M. D., & Nepal, B. (2017). A review of competency-based learning: Tools, assessments, and recommendations. *Journal of Engineering Education, 106*(4), 607-638"
    author: "Henri, M., Johnson, M. D., & Nepal, B"
  - id: national-board-for-professional-teaching-standards-national-teacher-certification-and-a-performance-based-assessment-system-2000
    resource: "https://eric.ed.gov/"
    title: "National Board for Professional Teaching Standards' National Teacher Certification and a Performance-Based Assessment System. (2000). ERIC Digest. https://eric.ed.gov/"
    author: "National Board for Professional Teaching Standards' National Teacher Certification and a Performance-Based Assessment System"
  - id: fricke-1976
    resource: "https://eric.ed.gov/?id=ED127854"
    title: "Fricke, B. G. (1976). Grading by Contract. Memo to the Faculty, n57. https://eric.ed.gov/?id=ED127854"
    author: Fricke, B. G
---

# Competency-Based Assessment

> **Principle** · [All principles](index.md)
> **Evidence** · 46 claims (12 for, 32 mixed, 2 against) · 46 studies (11 review, 9 theoretical, 8 causal, 8 design, 6 associational, 2 quant-synthesis, 2 qualitative), `q1`–`q4` · 2 of 46 report an effect size · 41 claims rest on one study

## Conditional relationship

Competency-based assessment states a relationship about **judgement**, not first about learning: when a learner's response to a task that represents the intended capability is scored against explicit criteria and a stated threshold, by assessors whose scoring agrees, the resulting judgement ("demonstrated" or "not yet") is expected to support better decisions about that learner than a norm-referenced rank or a record of time spent. The decisions are what to teach next, whether to advance, and whether to certify. A second, learning relationship rides on the first: when criteria are visible to learners and a "not yet" leads to correction and another comparable attempt, the quality of the learner's work and later examination performance (`general-achievement`) are expected to improve. Both are conditional on four things a page cannot settle in advance: whether the task elicits the capability itself rather than a proxy for it (most of all for `complex-skill` goals in `workplace-clinical` settings), whether the threshold was set by a defensible procedure, whether assessors are consistent and calibrated, and whether the learner's starting response reflects capability or the conditions of the attempt.

The wider instructional model (pacing, progression and pathways around competencies) is [Competency-based Learning & Assessment](competency-based-assessment.md), and the [Competency-Based Learning pattern](../patterns/competency-based-learning.md) gives a reusable design. Two converted siblings sit inside this page's relationship. [Mastery Learning](mastery-learning.md) holds the conditional model of the progression rule (gate, correct, recheck); this page owns what the gate rests on, a criterion-referenced judgement, and does not repeat the gate's model. [Formative Assessment](formative-assessment.md) holds the model of interpreting a response and choosing a next action; a competency judgement is one such response read against a public standard, and the formative model applies to everything below the threshold.

## Default design, while the relationship is untested

The page's earlier guidance, kept as a concrete default a designer can act on and revise. Each step is a design proposal with its evidence status beside it; most is untested as written.

1. **State each competency as an observable performance under stated conditions** (task, aids, time, setting), specific enough that two assessors would agree on what counts. Untested here; from the earlier page. The bearing evidence is that assessors differ when it is not done well (see Evidence, below), and one design demonstration in which competencies in a new area (students' use of generative AI in introductory physics) were stated so that they could be observed in students' work and scored with rubrics anchored in an expert answer key: [AI interaction competencies observable and scorable](../claims/ai-interaction-competencies-observable-scorable.md) [+W]. It shows the step can be done in one course, not that it makes judgements agree.
2. **Choose a task that elicits the competence itself, not a correlate of it.** For a `complex-skill` goal, prefer an integrated performance that resembles real use (a live scenario, an observed lesson) over an explanation of the steps on paper. Untested here. The nearest claim, [a training-design argument that practising whole complex tasks improves transfer](../claims/whole-task-performance-improves-transfer.md) [~W], is about how to train, not how to assess, and is itself an argument from prior research rather than a comparison of whole-task with part-task practice; it is carried here only as a reason to sample the integrated performance.
3. **Write the threshold down, and set it by a stated procedure.** Say what separates "not yet demonstrated" from "demonstrated", and if a panel sets the cut, use a method robust to one deviant rating. One standard-setting report bears on the method (see Evidence); none tests whether a given threshold predicts later performance.
4. **Share the criteria with learners before the attempt, with an exemplar and practice in applying them.** Evidence: two comparison-group studies of rubric-referenced self-assessment (see Evidence), with a cost noted beside them. A narrative review of goal-setting research holds that specific, difficult goals lead to higher performance than vague "do your best" goals, provided the person is committed and able: [Specific, difficult goals lead to higher performance](../claims/specific-difficult-goals-lead-to-higher-performance.md) [+W]. That is a reason to make the criterion specific, carried from goals to assessment criteria; it does not test visible criteria.
5. **Calibrate assessors and check their agreement before relying on a judgement.** Use a shared rubric, score common samples together, and look at the spread between assessors on the same work. Evidence: two studies show assessors on one rubric can differ substantially; neither tests calibration as a remedy.
6. **Allow reassessment after correction, on a comparable but changed task**, so a judgement reflects capability rather than timing. Evidence: the mastery-learning synthesis (see Evidence) supports the correct-and-recheck loop at programme level; the gate's own model is on [Mastery Learning](mastery-learning.md). Where an earlier attempt was supported, withdraw the support across attempts before the judgement that certifies: [fading support promotes the transfer of responsibility to the learner](../claims/fading-support-promotes-transfer-of-responsibility.md) [~M] (worked-example fading favoured near transfer in three experiments; carried here from instruction to assessment, untested there).
7. **Record what the judgement does not cover**: the aids allowed, the attempt number, the assessor, and the horizon. A "demonstrated" today is not evidence of `delayed-retention` or of performance in the learner's later setting. Untested here; from the earlier page.

## Fitting the design to a situation

Ask for four facts when the brief omits them: **what the judgement decides (feedback, progression, a credential)**, **how many assessors score each performance**, **how the threshold will be set**, and **whether reassessment is allowed**.

| If the brief says… | Then change… | Basis |
|---|---|---|
| Several assessors will score the same kind of performance | Calibrate them on common samples and check their spread before relying on a judgement; raters on one scale differed in severity | [Raters differed in severity](../claims/raters-differed-severity-mfrm.md) [~M]; [Engineering rubric scorers differed by 1.2 of 9 points](../claims/engineering-rubric-low-scoring-reliability.md) [-W] |
| A panel will set the pass threshold | Use a cut-score method that resists one deviant rating, and record the method | [Mean-classification cut-score method more robust to outliers](../claims/mean-classification-cut-score-method-robust.md) [~W] |
| AI will score responses | Write the required conditions into the rubric explicitly, keep human review of borderline and high-stakes decisions, and check agreement with human scorers | [Explicit rubric conditions reduced AI disagreement](../claims/explicit-rubric-conditions-reduce-ai-disagreement.md) [~W]; [AI not yet best practice for competency assessment](../claims/ai-not-best-practice-competency-based-assessment.md) [~W] |
| Learners should improve, not only be certified | Share the criteria with an exemplar before the attempt and have learners self-assess a draft against them | [Rubric-referenced self-assessment improved work](../claims/rubrics-improve-student-work.md) [~M] |
| The judgement controls progression to the next unit | Allow reassessment after correction on a comparable but changed task | [Mastery learning improves outcomes](../claims/mastery-learning-improves-outcomes.md) [+M] |
| A test places learners into levels | Check measurement precision at the cut scores that matter, not only overall reliability | [Placement test precision declines above the 40th percentile](../claims/cmi-ela-test-precision-declines-above-40th-percentile.md) [~W] |
| The test was built by picking items that spread learners out | Choose items that represent the competency domain, not those that discriminate best between learners | [Statistical item selection conflicts with criterion-referenced definitions](../claims/statistical-item-selection-conflicts-criterion-referenced-definition.md) [~W]; [Criterion-referenced tests need construct validation](../claims/criterion-referenced-tests-need-construct-validation.md) [~W] |
| Checks must be short | Use an adaptive mastery test; in one military-training simulation it shortened tests by 30–81% with the same decision for 96% of trainees | [Adaptive mastery testing reduces length and preserves decisions](../claims/adaptive-mastery-testing-reduces-length-preserves-decisions.md) [~W] |
| Learners whose capability is still emerging (young children, early stages) | Add an assisted attempt beside the unassisted one, and record what help made the difference | [Static assessment misses developing functions](../claims/static-assessment-misses-emerging-functions.md) [~W] |
| Learners are novices on the task being judged | Frame early attempts and feedback around the process criteria (the steps and strategy), and judge against the outcome threshold once the process is in place; withdraw prompts across attempts before the judgement that counts | [Process goals outperform outcome goals for novices](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M] (high-school writers learning one revision skill; a goal-setting finding carried to assessment criteria); [Fading support transfers responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [~M] |
| Drafts need frank feedback, but every judgement also counts toward the grade (writing courses) | Consider separating feedback on drafts from the grade up to a stated level, for example a grade guaranteed for completing specified work, with judged quality deciding only the grades above it; record that this credits completion, not demonstrated capability | Authors' account of their own writing courses, untested: [a contract guarantees a B for completed activities](../claims/contract-guarantees-b-for-completion-not-quality.md) [~W]; [decoupling evaluation from grades eases feedback](../claims/decoupling-evaluation-from-grades-improves-feedback.md) [~W]; [contract grading yields more student work](../claims/contract-yields-more-student-work.md) [~W]; [fourteen weeks of contract work warrants a B](../claims/fourteen-weeks-contract-work-warrants-b.md) [~W] |
| Practising professionals will be certified on portfolios or observed practice (teachers) | Say which later outcome the certification is meant to predict, and check it against that outcome; a credential can agree with observation scores and not with student-learning measures | [Board certification identifies more expert teachers](../claims/board-certification-identifies-more-expert-teachers.md) [+W]; [Certified teachers differ only on observation scores, not value added](../claims/experience-credentials-teacher-evaluation-scores.md) [~M] |
| Graduation or certification will rest on performance assessments | Give learners more than one occasion to demonstrate each competency, and record the conditions of each | [Performance assessments expand opportunities to demonstrate mastery](../claims/performance-assessments-expand-mastery-demonstration-opportunities.md) [~W] |

## Observation, state and explanation

What an assessor observes is a **response to one task under stated conditions** (task, aids, time, attempt number, assessor, prior exposures), scored against a criterion. "Competent" and "not yet competent" are inferences from that score, and they depend on the task sampling the capability, the threshold, and the assessor. A score from a lenient assessor and one from a severe assessor are not the same observation. "Novice" means novice on this task, not in the field.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Below threshold on a performance task, but explains the steps correctly | Capability not yet integrated under task conditions; the task adds demands the competency does not include (time, equipment, language); assessor severity | Re-score the same performance with a second, calibrated assessor; give a component probe and a whole task with the extraneous demand removed; record which steps failed. |
| Meets threshold on one attempt, fails a comparable task later | Narrow task sampled only part of the competency; forgetting; first task resembled practice items; first assessor lenient | Compare the two tasks' demands; check the first score against a second assessor; re-probe at a stated delay on a changed task. |
| Two assessors disagree on the same work | Criterion wording admits several readings; assessors weight criteria differently; one is more severe; the work is genuinely borderline | Have both score shared anchor samples and explain each score against the criterion; see whether disagreement is spread or concentrated on one criterion or one assessor. |
| Meets threshold only with support (prompts, a checklist, a partner) | Capability is developing and shows only when assisted; support carries part of the performance; the competency as written includes the support | Decide whether the support belongs to the competency; vary the support while holding the task constant; reassess unaided after a stated interval. |
| Repeated "not yet", then disengagement or withdrawal | Correction repeats the original instruction; a prerequisite gap; the threshold is above what instruction teaches; the judgement is experienced as threat; the learner's goal differs from the competency | Change the form of correction and observe the next attempt; probe a prerequisite; ask what the learner wants from the course; check how other learners fare on the same task and threshold. |

These rows are proposals for interpreting responses, untested with learners. A probe can shift confidence between explanations; one contrast does not identify a cause, and a reassessment is itself an exposure that can change the response. Record what remains unresolved rather than recording "competent" or "not yet" alone.

## Evidence and qualifications

No claim in the wiki tests this relationship as stated: none compares decisions or learning under criterion-referenced competency judgements against norm-referenced grading or seat-time credit. The claims below test neighbouring parts of it; of the six read at conversion, none has been read at full text with an effect size.

- [Self-assessing against a rubric improved the quality of student work in two non-randomised studies, one of which also found more stress and performance-avoidance](../claims/rubrics-improve-student-work.md) [~M]: two comparison-group studies (`controlled-nonrandom` as far as the claim page reports). Middle-school writers (n = 162) who reviewed a model essay, generated criteria and self-assessed a draft against a rubric scored higher on total essay scores and on every rubric criterion than a comparison condition that generated criteria and reviewed drafts without the rubric step. Pre-service teachers (n = 218) who self-assessed a concept map with a rubric produced work an expert rated higher, and self-assessed more accurately, than those with no tool, but also reported more difficulty coping with stress and a higher performance/avoidance orientation, which the authors judge detrimental to learning. No effect sizes; horizon immediate, one task each. One of two entries passes the judge, on abstracts. It supports making criteria visible and practising their use (step 4); it does not show that a competency threshold improves learning, and it carries a motivational cost to watch for.
- [Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]: a meta-analysis of 108 controlled evaluations (`synthesis-experimental`) at college, high-school and upper-elementary levels reports positive effects of mastery programmes on examination performance against conventionally paced instruction, apparently stronger for weaker students, varying with procedure, design and content; positive effects on attitudes; possibly more time on instructional tasks; and, for self-paced college programmes, often reduced completion. No pooled effect size recorded; checked by the judge on the abstract only. It bears on judging against a criterion and re-attempting rather than averaging, not on the quality of the judgement itself, and it does not predict one learner's gain or a delayed outcome.
- [Raters differed significantly in severity/leniency in the MFRM analysis](../claims/raters-differed-severity-mfrm.md) [~M]: in a many-facet Rasch analysis of three raters scoring open-ended items in a crossed design (`correlational`), the rater facet was significant, so the raters differed in severity, while item and person reliabilities stayed above .80. Not yet checked against its source. It qualifies the relationship: a judgement depends on who scored it, and high reliability in one facet does not remove differences in another.
- [In one community-college lab class, six scorers rating six teams with an engineering rubric differed by a mean of 1.2 of 9 points, which the authors read as a sign the rubric may not be reliable](../claims/engineering-rubric-low-scoring-reliability.md) [-W]: six scorers rated six teams on one inquiry-lab rubric; the mean class standard deviation was 1.2 of 9 points, which the authors took to mean the rubric may not have been reliable. One small design report, not yet checked. It limits the relationship: having a rubric does not by itself make judgements consistent.
- [A mean-classification cut-score method outperformed a contrasting-groups-style mean method because it was more robust to outliers](../claims/mean-classification-cut-score-method-robust.md) [~W]: a standard-setting report for alternate portfolio assessments of students with significant disabilities applied two methods of computing a cut score to panelists' ratings of 15 portfolios per grade and content area; one was heavily influenced by deviant ratings, the other more robust. Not yet checked. It bears on how a threshold is computed from panel judgements (step 3), not on whether any threshold is valid for a decision.
- [Static individual assessment misses developing functions; ZPD-based assessment reveals potential competencies](../claims/static-assessment-misses-emerging-functions.md) [~W]: a theoretical argument in a review paper, attributed to Vygotsky, that unassisted individual testing shows only matured functions, while assisted performance reveals developing ones. No data. It qualifies single-attempt, unassisted judgements: a "not yet" may misread a developing capability, which is a reason to record support and allow reassessment, not evidence that assisted scores should certify.

Keep the population, setting, comparator, instrument and horizon with each finding. Do not combine these into one strength: two are about learners' work, one about programme outcomes, and three about the judgement itself.

Read since conversion (2026-10-15), none of which tests the relationship either:

- [An ERIC digest reports that a 2000 validity study gave strong initial evidence that National Board certification identifies teachers who are more expert and whose students learn more deeply](../claims/board-certification-identifies-more-expert-teachers.md) [+W]: an ERIC digest reporting, second-hand and without effect sizes, a validity study (Bond et al., 2000) of a performance-based certification built on portfolios, videotaped teaching and student work. It is the nearest the wiki holds to the model's predictive side (does a performance-based judgement pick out people who do the work better), but it compares certified with uncertified teachers, not performance-based certification with a test or with seat time, and the claim page records it as `review · r1`. Against it, an analysis of one district's 2013-14 evaluation scores found certified teachers differed from others only on observation scores, not on value added: [Certified teachers differ only on observation scores, not value added](../claims/experience-credentials-teacher-evaluation-scores.md) [~M]. Together they say a performance credential may agree with one later measure and not another, which is why a certification must name the outcome it predicts.
- [Focused rubric refinement that made required conditions explicit reduced AI–official disagreements on targeted questions](../claims/explicit-rubric-conditions-reduce-ai-disagreement.md) [~W]: in one study of AI grading of handwritten physics answers, rewriting the rubric to state the conditions for awarding marks raised agreement with official scores on the questions refined (on one 40-response part, mean absolute difference fell from 1.1 to 0.4 marks and r rose from 0.70 to 0.82). It bears on step 1 and the AI row: criteria stated so that a scorer cannot read them two ways are scored more consistently, shown here for an AI scorer on targeted questions only.
- Four claims from one source, Danielewicz and Elbow (2009), describe a grading contract in first-year writing that guarantees a B for completing specified work and reserves higher grades for judged quality: [contract guarantees a B for completion](../claims/contract-guarantees-b-for-completion-not-quality.md) [~W], [decoupling evaluation from grades eases feedback](../claims/decoupling-evaluation-from-grades-improves-feedback.md) [~W], [contract grading yields more student work](../claims/contract-yields-more-student-work.md) [~W] and [fourteen weeks of contract work warrants a B](../claims/fourteen-weeks-contract-work-warrants-b.md) [~W]. They were attached as testing this page's relationship; they do not. They are the authors' account of their own practice with no data printed, and up to the B the contract credits completed work, which is closer to the seat-time comparator this page sets against a judgement of capability. What they bear on is the cost the rubric study also found: tying every judgement to the grade may make frank feedback harder to give and hear (the drafts row above).

How far each may be carried: the rubric studies are self-assessment with one rubric on one task, so they do not show that assessor-scored competency rubrics help learning; the mastery synthesis is about unit gates in courses, not certification of workplace competence; the two reliability claims are single instruments and do not estimate agreement for any other rubric; the cut-score report is one population and one panel procedure.

## The evidence by question

- *Does a pass on the check mean what the criterion says: are the items, cut scores and raters dependable?* [Criterion-referenced tests require empirically-based construct validation studies](../claims/criterion-referenced-tests-need-construct-validation.md) [~W]
- *Does giving learners the criteria, and having them apply them to their own or peers' work, improve the work?* [Self-assessing against a rubric improved the quality of student work in two non-randomised studies, one of which also found more stress and performance-avoidance](../claims/rubrics-improve-student-work.md) [~M]

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Re-read 2026-10-15: eleven of the claims listed here were worked into the model above. These two were left because they bear only on the comparator, not on the relationship.

- [Transcript grades are a blurred currency of performance information, partly due to grade inflation driven by student pressure](../claims/transcript-grades-blurred-currency.md) [+W] — an author's framing statement (1976) with no data, about why course grades carry little information; it motivates the page's comparison but does not test either side of it
- [The hybrid grading contract helps resist grade inflation by reserving grades above B for exceptionally high quality](../claims/hybrid-contract-resists-grade-inflation.md) [+W] — the authors' reasoned position from their own writing courses, about keeping high grades scarce; bears on what a grade signals, not on judging a competency against a threshold
- [Written knowledge tests, OSCEs and situational judgement tests all show predictive validity for later clinical performance](../claims/assessments-predictive-validity-later-clinical-performance.md) [+W] — attached 2026-10-31 from McLachlan JC et al. (2025), which proposed "Commission research on the predictive validity of prescribing competence assessments"; tests this page's relationship.
- [Twenty of 34 tools assessed the two highest Miller levels ('shows how' and 'does'), with team work, risk management and communication the most assessed skills](../claims/most-tools-target-higher-miller-levels.md) [+W] — attached 2026-11-01 from Okuyama Ayako et al. (2011), which proposed "Adapt context-specific assessment tools to each discipline rather than copying them across working environments".

## Objective and learner-valued goal

The designer's objective names the competency, the task that represents it, the criterion and threshold, the permitted aids and the horizon at which the judgement is meant to hold. Elicit separately what the learner wants from the assessment: a credential for a job, recognition of experience they already have, confidence that they can do the work unsupervised, or simply to finish. Agreement and divergence are both observations, and a learner may value the credential more than the capability or the reverse.

For example, a nurse returning to practice may value being trusted to run a medication round alone, while the programme's objective is a pass on a simulated medication-safety scenario scored on a checklist. A pass serves the programme's decision; whether it serves the learner's aim depends on whether the scenario includes the interruptions and judgement calls of a real round, and on a later observation in practice. Recording both keeps a scenario pass from being read as the capability the learner came for, and tells the designer where the task may be a proxy.

## What would revise this model?

The model should weaken if criterion-referenced judgements, made with calibrated assessors on representative tasks, predict later performance in the target setting no better than norm-referenced grades or time-based credit, or if they lead to no better decisions about what to teach next. If assessor disagreement on well-specified rubrics stays large after calibration, the threshold cannot carry the weight the principle puts on it, and judgements should be reported with their uncertainty or replaced by multiple assessors and attempts. If making criteria visible reliably raises stress or performance-avoidance enough to lower learning, as one rubric study suggests it can, the default design's step 4 needs a different form. Do not protect the model by calling every inconsistent judgement a poorly written rubric.

A score on a rubric, agreement between assessors, a threshold's defensibility, learning gains from the assessment process, and performance in the learner's real setting are separate claims. The present evidence does not establish how to set a threshold for a given decision, how much calibration produces acceptable agreement, or whether competency judgements transfer across settings.

## Claims

- [AI assessors show emerging reliability: acceptable AI-human rater agreement (Cohen's 0.78) in a 12-educator case study and human-comparable feedback helpfulness ratings with 45 learners](../claims/agentic-assessment-rater-agreement-and-helpfulness.md) [~W]
- [Threshold-setting methods are compared using reading scores from over 728,923 students on a computer-adaptive test of nearly 12,000 items](../claims/large-scale-cat-threshold-method-comparison.md) [~W]
- [AI is currently not best practice for competency-based micro-credential assessment; human assessors remain indispensable](../claims/ai-not-best-practice-competency-based-assessment.md) [~W]
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](../claims/prompting-limited-uneven-proficiency-control-writing-simulation.md) [~W]
- [The VCP rubric was difficult for teams to use because it lacked standardized calibration and its process and content categories were unclear](../claims/vcp-rubric-lacked-calibration-and-clarity.md) [~W]
- [Students reported first-pass false-positive deductions at a mean of 2.94 per term, normalising to about 0.6% of rubric items](../claims/student-reported-grading-errors-lata.md) [~W]
- [Case-study states use performance-based assessments to provide more opportunities for students to demonstrate mastery of skills and content](../claims/performance-assessments-expand-mastery-demonstration-opportunities.md) [+W]
- [LLMs support the shift from memorization-focused to competency-based assessment by generating rubrics, varied assessment items and authentic scenario-based tasks](../claims/llms-support-competency-based-assessment-design.md) [+W]
- [ELPAC overall PL 4 remains the appropriate Criterion 1 reclassification threshold, with 2017-18 and 2022-23 data converging on the same level](../claims/elpac-pl4-threshold-validated-replication.md) [+W]
- [Providing a rubric reduces bias in self-assessment, moving judgments closer to expert ratings](../claims/rubrics-reduce-self-assessment-bias.md) [~W]
- [Graduate attributes ('wicked competences') may not be amenable to conventional assessment because they are context-dependent, partly specifiable and developed over years](../claims/wicked-competences-resist-conventional-assessment.md) [-W]
- [The test's exercises were validated by six expert judges who reached practical agreement after modification](../claims/six-judge-validity-agreement-test-exercises.md) [~W]
- [Digital-competency disparities may confound computerized PISA-VET assessments of vocational competence](../claims/pisa-vet-digital-competency-confound.md) [~W]
- [The 4-category rating scale of the POET-O functions properly overall but its threshold structure could be improved](../claims/poet-o-rating-scale-functions-with-disordered-thresholds.md) [~W]
- [Competencies related to social determinants of health, equity and social accountability have emerged as central axes of public health competency assessment](../claims/sdoh-equity-central-axes-assessment.md) [+W]
- [Global entrustment scales and standardised rubrics dominate EPA assessment, but validation of assessment tools is reported in only a small minority of studies](../claims/epa-assessment-tools-validation-gap.md) [~W]
- [Rubric application boosts student performance and skill acquisition across dental disciplines](../claims/rubrics-boost-student-performance-skill-acquisition.md) [+W]
- [The CALM tool showed only weak inter-rater agreement (weighted Kappa 0.45) in its single ED video-review study](../claims/calm-weak-kappa-045-single-study.md) [~W]
- [Checklists show reasonable validity and reliability but have an early ceiling effect and are most appropriate for novice learners in formative settings](../claims/checklists-valid-but-ceiling-effect-novice-formative.md) [~W]
- [The heterogeneity of suturing assessment tools precludes meta-analysis, though their content could be merged into a panel of competence markers](../claims/heterogeneous-suturing-tools-preclude-meta-analysis.md) [~W]

## Related Principles
- [Mastery Learning](mastery-learning.md) — the progression rule that learners advance on demonstrated mastery rather than schedule
- [Formative Assessment](formative-assessment.md) — the feedback cycles that make a mastery threshold reachable rather than merely a sorting line
- [Authentic Audiences & Purposes](authentic-audiences-purposes.md) — credible demonstrations often involve products or performances for real stakeholders
- [Goal Setting & Monitoring](goal-setting-monitoring.md) — competency systems need visible progress and next-step clarity
- [Guided Practice](guided-practice.md) — repeated coached attempts are often necessary before a valid mastery judgment
- [NBPTS Five Core Propositions for Accomplished Teaching](../theories/nbpts-five-core-propositions.md)

## Examples

- A teacher preparation program assesses classroom facilitation through observed teaching, annotated lesson plans, and a rubric tied to explicit competencies instead of a single written final.
- A cybersecurity course certifies learners on incident response only after they complete a live scenario within defined quality criteria, not merely explain the steps on paper.
- [Standards-/Mastery-Based Grading](../strategies/standards-based-grading.md) — classroom grading organised around demonstrated standards rather than averaged scores.
- [Frame course specifications in competencies and build in 'I can do...' benchmark tasks as informal assessment](../strategies/competency-course-specifications-benchmark-tasks.md)
- Performance checklists and rubric-based demonstrations in technical training, clinical education, and workplace certification
- [Grade Students Based on Demonstrated Learning](../strategies/grade_students_based_on_demonstrated_learning.md) — evaluation based on evidence rather than averages or behavior proxies
- Applied projects, simulations, and observed performances are stronger competency evidence than multiple-choice recall alone
- [Portfolio entries with written commentary for assessing teaching practice](../products/national-board-certification.md)
- [Reorient AI assessment toward formative, holistic portraits of learner competencies rather than automated grading](../strategies/ai-assessment-holistic-competency-portraits.md)
- [Clarify assessment purpose, define skill expectations with rubrics and progressions, and calibrate on student work](../strategies/clarify-purpose-norm-expectations-calibrate-pog.md)
- [Learning Contracts](../elements/learning-contracts.md)
- [Learning Contracts](../strategies/learning_contracts.md)
- [Negotiate learning contracts at the start of term and allow test retakes until mastery](../strategies/negotiate-contracts-allow-retakes.md)
- [Separate competency assessment from courses, conducted by an independent unit using evidence-centered assessment design](../strategies/independent-competency-assessment-separation.md)

## Key Sources
- Le, C., Wolfe, R. E., & Steinberg, A. (2014). *The past and the promise: Today's competency education movement*. Jobs for the Future.
- Henri, M., Johnson, M. D., & Nepal, B. (2017). A review of competency-based learning: Tools, assessments, and recommendations. *Journal of Engineering Education, 106*(4), 607-638. [doi:10.1002/jee.20180](https://doi.org/10.1002/jee.20180)
- Collins, J. B., Harsy, A., Hart, J., Haymaker, K. A., Hoofnagle, A. M., Kuyper Janssen, M., & O'Shaughnessy, J. (2019). Mastery-based testing in undergraduate mathematics courses. *PRIMUS, 29*(5), 441-460. [doi:10.1080/10511970.2018.1488317](https://doi.org/10.1080/10511970.2018.1488317)
- Shearer, R. L. (2017). Adaptive learning, competency-based education, and personalization: Implications for distance education and adult learners. *Journal of Lifelong Learning Society, 13*(1), 49-71.
- National Board for Professional Teaching Standards' National Teacher Certification and a Performance-Based Assessment System. (2000). ERIC Digest. https://eric.ed.gov/
- Fricke, B. G. (1976). Grading by Contract. Memo to the Faculty, n57. https://eric.ed.gov/?id=ED127854

<!-- deprecated 2026-10-02: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Competency-based assessment judges a learner against explicit statements of what they should be able to do, at a defined standard, using evidence that actually elicits that performance. It replaces the question "how much of the course did this learner complete, and how did they score relative to peers?" with "can this learner do this thing, to this standard, and what is the evidence?"

This principle covers the *assessment* half of competency-based design: specifying competencies so they can be judged, choosing evidence that genuinely elicits them, setting mastery thresholds, and keeping judgments consistent across assessors. The wider instructional model it sits inside — flexible pacing, progression rules, learner pathways, and how instruction is organised around competencies — is [Competency-based Learning & Assessment](competency-based-assessment.md).

## Implications
Competency-based assessment shifts the design question from time spent to demonstrated capability. That usually improves transfer and the quality of decisions made from assessment results, provided the tasks mirror meaningful performance rather than proxies for it [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [~M].

The burden it creates is specification. Competencies, acceptable evidence, and mastery thresholds all have to be defined well enough that two assessors reach the same judgment on the same work — otherwise "mastery" is just a differently-worded impression. Vague competencies also fail learners directly: without clear criteria they cannot tell what they are aiming at [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [+M].

### Context
#### Requirements
- Competencies stated as observable performance, specific enough that different assessors agree on what counts
- Assessment tasks that genuinely elicit the target competence, not a proxy that correlates with it
- Explicit mastery thresholds — what distinguishes "yet to demonstrate" from "demonstrated"
- Shared rubrics and assessor calibration, since consistency is what makes a mastery claim mean anything
- Opportunity for reassessment, so a judgment reflects capability rather than timing

#### Constraints
- Complex competencies are expensive to assess well; the richer the performance, the more assessor time and calibration it demands
- Competencies defined too narrowly fragment into a checklist that no longer describes real capability
- A mastery claim is only as good as the evidence behind it — a confident threshold on weak evidence is worse than an honest grade
- Single-attempt, single-assessor judgments reintroduce exactly the noise this approach is meant to remove

### Target Learners
- Learners in workforce, technical, clinical, and performance-oriented domains where competence is directly observable
- Learners whose prior experience should count, but only where it can be evidenced
- Learners who benefit from multiple attempts and feedback rather than a single averaged score

### Target Learning Objectives
- Judge learning by demonstrated performance against clear, public criteria
- Produce assessment results specific enough to act on, rather than a rank
- Support transfer by drawing evidence from authentic or application-rich tasks

### Theory
#### Supporting
- [Competency-based Learning & Assessment](competency-based-assessment.md) — the wider instructional model this assessment approach belongs to
- Experiential and apprenticeship perspectives support performance-based demonstration over purely declarative testing

#### Contradicting / Qualifying
- Novices often need process coaching and scaffolding before they can demonstrate mastery independently, so early competency judgments can misread developmental stage as incapability [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M]
- Support should fade toward independent demonstration rather than becoming a permanent feature of the assessment [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [~S]

### Claims

- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [~M] — competency judgments are stronger when they rest on integrated performances that resemble actual use
- [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [+M] — well-specified mastery criteria focus effort and make expectations legible
- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M] — novices need process-level guidance before a mastery judgment is meaningful
-->

<!-- merged 2026-10-05 from principles/competency-based-learning-assessment ("Competency-based Learning & Assessment"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Competency-based Learning & Assessment

> **Principle** · [All principles](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 6 studies (2 causal, 2 review, 2 theoretical), `q2`–`q3` · 0 of 6 report an effect size · 2 claims rest on one study

## Description
Competency-based learning and assessment organize progress around demonstrated mastery rather than seat time, pacing norms, or one-shot averages. Learners advance by showing they can perform clearly defined competencies, often through applied tasks, performance assessments, or repeated attempts. The design promise is tighter alignment between what matters and what is assessed, but that promise depends on the quality of the competencies, evidence, and supports.

This page covers the whole model — how instruction, pacing, progression, and assessment are organised around competencies. The narrower question of how to judge a competency credibly (specification, evidence, thresholds, assessor calibration) is [Competency-Based Assessment](competency-based-assessment.md).

## Implications
Competency-based learning and assessment are strongest when mastery is defined as credible performance rather than completion or time spent. Clear competencies, repeated attempts, and authentic evidence usually make progress more legible and improve transfer because learners are judged on what they can actually do [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M]. But the system only works if competencies are well specified [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [+M] and learners receive enough process support to reach them [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M]; otherwise “mastery” becomes either a vague slogan or a fragmented checklist.

### Context
#### Requirements
- Explicit competencies that describe observable performance, not vague aspirations
- Assessments that actually elicit the target competence in credible ways
- Opportunities for practice, feedback, revision, and reassessment before high-stakes judgments
- Tracking systems and instructional routines that let learners know where they are and what remains to be demonstrated

#### Constraints
- Competencies can become atomized checklists if they are defined too narrowly
- Flexible pacing sounds equitable but can become isolating or unmanageable without strong advising and feedback loops
- Reliable assessment of complex competencies is labor-intensive and requires shared rubrics or calibration
- Mastery claims are only as trustworthy as the evidence used to infer them

### Target Learners
- Adult, professional, and nontraditional learners who need transparent progress markers and flexible routes to mastery
- Learners whose prior experience should count only when it can be demonstrated through evidence
- Learners in workforce, technical, health, and performance-oriented domains where competencies can be observed in practice
- Learners who benefit from multiple attempts and feedback cycles rather than single averaged scores

### Target Learning Objectives
- Demonstrate usable competence on clearly defined skills or performances
- Support transfer by linking assessment to authentic or application-rich tasks
- Make learner progress inspectable so feedback and next steps are concrete
- Separate "not yet" from failure by allowing revision and reassessment

### Theory
#### Supporting
- Self-regulated-learning perspectives support competency systems when progress markers, feedback, and revision make self-monitoring actionable
- Adult-learning perspectives support flexible pathways and recognition of prior experience, provided competence is still demonstrated
- Experiential and apprenticeship perspectives support performance-based demonstrations over purely declarative testing
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M] supports competency assessment when evidence comes from integrated performances instead of isolated fragments

#### Contradicting / Qualifying
- Competency systems fail when competencies are underspecified, overfragmented, or detached from authentic performance
- Learners still need explicit goals and calibrated challenge; mastery alone is not motivational without clear standards [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [+M]
- Novices often need process coaching and scaffolds before they can demonstrate mastery independently [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M]

### Claims
- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [+M] — competency claims are stronger when based on integrated performances that resemble real use
- [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [+M] — well-specified mastery criteria focus effort and clarify expectations
- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M] — learners often need process-level guidance before they can demonstrate mastery
- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [~S] — supports and reassessment opportunities should gradually lead toward independent demonstration, not permanent dependence on scaffolds

## Related Principles
- [Competency-Based Assessment](competency-based-assessment.md) — the assessment component of this model: specifying competencies, eliciting evidence, and setting defensible mastery thresholds
- [Authentic Audiences & Purposes](authentic-audiences-purposes.md) — credible demonstrations often involve products or performances for real stakeholders
- [Goal Setting & Monitoring](goal-setting-monitoring.md) — competency systems need visible progress and next-step clarity
- [Guided Practice](guided-practice.md) — repeated coached attempts are often necessary before a valid mastery judgment
- [Formative Assessment](formative-assessment.md) — feedback cycles are part of making mastery achievable rather than merely sortable

## Examples
<!- - Links to elements or patterns that apply this principle - ->
- Performance checklists and rubric-based demonstrations in technical training, clinical education, and workplace certification
- [Standards-/Mastery-Based Grading](../strategies/standards-based-grading.md) — classroom grading organized around demonstrated standards
- [Grade Students Based on Demonstrated Learning](../strategies/grade_students_based_on_demonstrated_learning.md) — evaluation based on evidence rather than averages or behavior proxies
- Applied projects, simulations, and observed performances are stronger competency evidence than multiple-choice recall alone

## Key Sources
- Henri, M., Johnson, M. D., & Nepal, B. (2017). A review of competency-based learning: Tools, assessments, and recommendations. *Journal of Engineering Education, 106*(4), 607-638. [doi:10.1002/jee.20180](https://doi.org/10.1002/jee.20180)
- Collins, J. B., Harsy, A., Hart, J., Haymaker, K. A., Hoofnagle, A. M., Kuyper Janssen, M., & O'Shaughnessy, J. (2019). Mastery-based testing in undergraduate mathematics courses. *PRIMUS, 29*(5), 441-460.
- Shearer, R. L. (2017). Adaptive learning, competency-based education, and personalization: Implications for distance education and adult learners. *Journal of Lifelong Learning Society, 13*(1), 49-71.
-->

<!-- merged 2026-10-07 from principles/performance-based-teacher-certification-assessment ("Performance-based assessment should anchor advanced teacher certification"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Performance-based assessment should anchor advanced teacher certification

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 review), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The digest states that "From the beginning, the National Board has been committed to developing an assessment that is performance-based that also serves as a professional development" experience, contrasting with state licensure that merely indicates a licensee has satisfied minimum entry-level requirements. Certification of advanced teaching expertise should therefore rest on demonstrated performance of teaching practice, including classroom artifacts, videotaped instruction, and student work, rather than on tests of knowledge alone, so that what is certified is what teachers can actually do with students.

## Design Implications

### Context
#### Requirements
- Advanced certification assessments must include direct performance evidence of teaching practice, such as portfolios, videotaped instruction, and student work samples, rather than relying solely on examinations of declarative knowledge.
#### Constraints
- 

### Target Learners
- experienced teachers seeking advanced certification

### Target Learning Objectives
- demonstrate advanced teaching expertise through authentic performance evidence

### Claims

- [National Board certification identifies teachers who are more expert and whose students achieve deeper learning](../claims/board-certification-identifies-more-expert-teachers.md) [+W]

## Related Principles

- [NBPTS Five Core Propositions for Accomplished Teaching](../theories/nbpts-five-core-propositions.md)

## Examples

- [Portfolio entries with written commentary for assessing teaching practice](../products/national-board-certification.md)

## Key Sources
- National Board for Professional Teaching Standards' National Teacher Certification and a Performance-Based Assessment System. (2000). ERIC Digest. https://eric.ed.gov/
-->

<!-- merged 2026-10-14 from patterns/grading-by-contract-fricke ("Grading by contract: students propose specific work and criteria within teacher-presented options"), folded in as a narrower page that rested on two studies or fewer after an evidence search (upgrade_worklist.py, 2026-10-14): its body as it stood. Its bullets this page lacked were added above.

# Grading by contract: students propose specific work and criteria within teacher-presented options

> **Pattern** · [All patterns](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (1 design, 1 theoretical), `q1` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
Contract grading is a course-level arrangement in which the teacher presents a number of options (such as a specified number of correct responses or quality of performance), and within these limits each student may then propose a specific set of work at the beginning of the term. The work is completed when the agreed criteria are met, and the plan can incorporate mastery-learning features allowing students to repeat a given test. The memo reports that about one-third of Michigan graduate TAs used some variation of a contract plan.

## Design Implications

### Context
#### Requirements
- The teacher must present a set of grading options and accept student proposals within those limits
#### Constraints
- 

### Target Learners
- university students

### Target Goals
- meeting explicit, individually negotiated performance criteria

### Claims

- Mastery Criterion Beats Fixed Trials [+M]
- [Transcript grades are a blurred currency of performance information, partly due to grade inflation driven by student pressure](../claims/transcript-grades-blurred-currency.md) [+W]
- [A unilateral grading contract guarantees students a course grade of B based solely on completion of specified activities, not on judged writing quality](../claims/contract-guarantees-b-for-completion-not-quality.md) [+W] — attached 2026-10-14 from Danielewicz et al. (2009), which proposed "Guarantee a grade for completing specified activities so teacher and student attention shifts from grading to learning"; tests this page's relationship.
- [Decoupling evaluation from grades makes teacher feedback easier to give and more effective for learning](../claims/decoupling-evaluation-from-grades-improves-feedback.md) [+W] — attached 2026-10-14 from Danielewicz et al. (2009), which proposed "Guarantee a grade for completing specified activities so teacher and student attention shifts from grading to learning"; tests this page's relationship.
- [Contract grading yields more total work from students, especially skilled writers who previously skipped learning tasks](../claims/contract-yields-more-student-work.md) [+W] — attached 2026-10-14 from Danielewicz et al. (2009), which proposed "Guarantee a grade for completing specified activities so teacher and student attention shifts from grading to learning"; tests this page's relationship.
- [The authors report that fourteen weeks of contract-required work improves writing quality enough to warrant a B](../claims/fourteen-weeks-contract-work-warrants-b.md) [+W]
- [The hybrid grading contract helps resist grade inflation by reserving grades above B for exceptionally high quality](../claims/hybrid-contract-resists-grade-inflation.md) [+W]

## Related Patterns
- 

## Examples

- [Learning Contracts](../elements/learning-contracts.md)
- [Learning Contracts](../strategies/learning_contracts.md)
- [Negotiate learning contracts at the start of term and allow test retakes until mastery](../strategies/negotiate-contracts-allow-retakes.md)

## Key Sources
- Fricke, B. G. (1976). Grading by Contract. Memo to the Faculty, n57. https://eric.ed.gov/?id=ED127854
-->
