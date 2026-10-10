---
type: principle
id: retrieval-practice
aliases: [balance-retrieval-success-and-retrieval-effort]
title: Retrieval Practice
description: "For learners who have studied material, recalling it from memory rather than restudying tends to raise delayed retention when initial retrieval mostly succeeds or is corrected by feedback; restudy can lead at a few minutes, transfer gains are smaller and conditional, and high element-interactivity material is contested."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: roediger-2006
    resource: "https://doi.org/10.1111/j.1467-9280.2006.01693.x"
    title: "Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science, 17*(3), 249-255"
    author: "Roediger, H. L., & Karpicke, J. D"
  - id: karpicke-2017
    resource: "https://doi.org/10.1016/B978-0-12-809324-5.21055-9"
    title: "Karpicke, J. D. (2017). Retrieval-Based Learning: A Decade of Progress. Learning and Memory: A Comprehensive Reference, 2nd edition, Volume 2. https://doi.org/10.1016/B978-0-12-809324-5.21055-9"
    author: Karpicke, J. D
---

# Retrieval Practice

> **Principle** · [All principles](index.md)
> **Evidence** · 21 claims (9 for, 10 mixed, 1 against, 1 unmarked) · 13 studies (6 quant-synthesis, 5 causal, 2 review), `q2`–`q4` · 9 of 13 report an effect size · 16 claims rest on one study

## Conditional relationship

For a learner who has already studied some material, recalling it from memory, rather than restudying it or not being tested, tends to raise performance on a **delayed** test of that material. The best-supported cases are adults and university students learning prose, word pairs and facts (`verbal-association`, `concept`), compared with restudy at a horizon of a day or more (`delayed-retention`). Two conditions bound the relationship. The initial retrieval has to mostly succeed, or be followed by corrective feedback; repeated failure with no feedback has shown about no benefit. And the horizon matters: on a test minutes after study, restudy has been ahead. Transfer to new questions (`near-transfer`) is smaller and depends on how the retrieval and the later task are configured. Whether the benefit holds for material high in element interactivity is contested. This is a bounded expectation for groups under stated conditions, not a forecast for one learner.

The [Team-Based Learning pattern](../patterns/team-based-learning.md) is one reusable design that puts this relationship to work: its individual readiness test is a retrieval attempt, and its team retest supplies immediate feedback. The retrieval evidence bears on those steps, not on the team formation, application exercises or peer evaluation around them. The pattern's response-dependent branches are design proposals, untested with learners.

## Observation, state and explanation

Record a response **under stated conditions**: the item format (free recall, cued recall, short answer, multiple choice), cues and notes allowed, the time since study, the stakes, and whether feedback followed. A score on a quiz is an observation. "Has a durable, retrievable memory" is an inferred state, and so is "studied the reading". Correct recognition of an option is a different performance from producing the answer, and an answer given two minutes after reading says little about one given a week later. Confidence is a separate observation; learners who restudied in the cited experiment were more confident and did worse at a week, so confidence alone does not settle the state.

Strengthened memory access is the explanation the claim pages give for the effect. It is a mechanism hypothesis; no observation in a single quiz measures it.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Recalls well right after studying, poorly a week later | Fluent restudy created short-lived access; the material was never well encoded; later learning interfered | Compare an unaided recall probe at the delay with the immediate one, on matched items; ask for a prediction of later recall first, and record whether any retrieval or feedback came between. |
| Fails most items on a first unaided attempt | The material was not studied or not encoded; the cues on the probe do not match how it was learned; the stakes or anxiety suppressed responding | Re-present the material, then probe again after a short gap; compare a cued with a free-recall version; compare a low-stakes attempt with a graded one. |
| Correct on multiple choice, wrong on short answer for the same content | Recognition without recall; a lure picked earlier has been learned as the answer; unfamiliarity with the response format | Give a short-answer version of the items; check whether wrong answers repeat options the learner selected before; note whether feedback followed the earlier test. |
| Recalls the fact, cannot use it on an application question | The retrieved item is not connected to the principle the question needs; the question demands knowledge that was never practised; reading or language load | Ask the application question with the fact supplied and without it; ask the learner to explain the relation; vary the wording of the question. |
| Scores rise across repeated quizzes but not on the later exam | Item-specific memory of the quiz questions; the exam measures something else; the gap before the exam was longer than any practised one | Probe with new items on the quizzed topics, at a delay like the exam's; compare the quiz and exam blueprints. |

These are proposals for telling explanations apart, untested with learners. A probe is itself a retrieval attempt and can change what it measures; record it as an exposure. One contrast shifts confidence among the explanations; it does not identify a cause.

## Evidence and qualifications

- [Retrieval practice improves long-term retention](../claims/retrieval-practice-improves-retention.md) [+S]: a meta-analysis of 159 effect sizes from 61 studies compared tested with restudied material (g = 0.50, 95% CI 0.42 to 0.58, heterogeneity high), larger at retention intervals of a day or more (0.69) than below a day (0.41), with feedback (0.73 against 0.39) and with cued recall rather than recognition (0.61 against 0.29); with no feedback and initial success at or below 50% it was about zero (0.03). Published studies showed larger effects than unpublished ones (0.58 against 0.25). An experiment with undergraduates reading science passages found restudy ahead at five minutes (81% against 75%) and testing ahead at two days and one week. Not settled: the abstracts available could not confirm the entries. It does not predict an individual's gain or the size of an effect on complex skills.
- [Retrieval Practice Improves Long Term Retention](../claims/retrieval-practice-improves-retention.md) [+S]: adds a second meta-analysis of practice testing across education levels (g = 0.51), with multiple-choice and constructed-response practice tests both effective. Its comparators mix rereading, filler tasks and no treatment, which is not the same contrast as testing against restudy. Not settled on the abstracts. The two pages record the same 2006 experiment with different counts (n=180 here; 120 + 180 across two experiments there), so read the full entry before quoting a sample size.
- [Feedback Enhances Retrieval Practice](../claims/feedback-enhances-retrieval-practice.md) [+S]: in a review of classroom studies (222 in the published abstract; 48,478 students), quizzing beat restudy and other controls overall (g = 0.499), and quizzes with corrective feedback produced g = 0.537 against 0.374 without. That is a between-study comparison, and another meta-analysis found no moderation (0.63 against 0.60). A word-pair experiment (258 participants, Luganda–English, final test one week later) found that supplying the answer after an error raised retention, while feedback after a correct response made little difference. One of two entries passes the judge; the other could not be confirmed. Feedback timing and elaborated against answer-only feedback are not tested here.
- [Retrieval Failure Reduces Benefit](../claims/retrieval-failure-reduces-benefit.md) [~M]: in the same 61-study meta-analysis, no-feedback studies whose initial recall was at or below 50% showed g = 0.03, and those above 75% showed g = 0.56. This is a moderator analysis across groups of studies, not a manipulation of success, so it gives no threshold for one learner. Not settled on the abstract. Pretesting studies, where failure followed by feedback helps, are a counterpoint the page records.
- [Retrieval Practice Improves Transfer](../claims/retrieval-practice-improves-transfer.md) [~S]: a meta-analysis of 122 experiments (192 effect sizes, N = 10,382) found transfer from practice testing against non-testing re-exposure (d = 0.40, 95% CI 0.31 to 0.50), strongest to application and inference questions and across test formats, weakest to rearranged items, untested material and worked-example problems; bias corrections often left no positive transfer when the favourable moderators were absent. Four prose-passage experiments found repeated testing ahead of repeated study on new inferential questions a week later. Both entries pass the judge (abstracts). It does not establish far transfer to new problem structures.
- [The argument that retrieval practice effects do not occur with materials high in element interactivity is contested](../claims/whether-element-interactivity-limits-retrieval-practice-effects-is-contested.md) [~M]: second-hand, from one review chapter: one study found effects with a randomly ordered text but not an intact one, another found them for both, and the chapter judges the limiting argument not convincing. Not yet checked against its sources. For `high` element-interactivity material or a `complex-skill` goal, treat the relationship as unsettled.

Retain the comparator (restudy, rereading, filler or nothing), the item format, feedback, initial success, the horizon and the learners when transporting these results. The pooled values come from different comparisons and should not be ranked against one another or read as an individual's expected gain.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~S] — not settled: the text available could not confirm the entries (abstract)
- [Retrieval practice effects become more robust as initial retrieval success increases, especially above 75%, while retrieval made too easy yields smaller effects](../claims/retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) [+M] — checked by the judge: all 2 entries pass (full text)
- [Initial retrieval conditions that provide less cue support, such as free recall rather than recognition or fewer letter cues, tend to produce better retention despite lower initial success](../claims/less-initial-retrieval-support-produces-better-retention.md) [~M] — checked by the judge: all 4 entries pass (full text)
- [Evidence on whether initial short-answer questions produce more learning than initial multiple-choice questions is mixed, with recent studies finding little or no difference](../claims/short-answer-versus-multiple-choice-retrieval-practice-evidence-is-mixed.md) [~M] — checked by the judge: all 5 entries pass (full text)
- [Initial short-answer tests outperform initial multiple-choice tests mainly when feedback follows them; without feedback, the higher initial success of multiple-choice tests can favor multiple-choice](../claims/feedback-determines-whether-short-answer-retrieval-outperforms-multiple-choice.md) [~M] — checked by the judge: all 3 entries pass (full text)
- [Taking initial multiple-choice tests without feedback can lead students to later produce the incorrect lure answers they selected, even when an overall retrieval practice benefit occurs](../claims/multiple-choice-lures-can-be-learned-as-false-knowledge.md) [-M] — partly checked: 1 of 2 entries pass, the rest could not be confirmed (full text)
- [Spaced Retrieval Improves Retention](../claims/spaced-retrieval-improves-retention.md) [+M] — not yet checked against its sources
- [Retrieval practice effects are larger at retention intervals greater than 1 day (g = 0.69) than at intervals less than 1 day (g = 0.41) in Rowland's (2014) meta-analysis](../claims/retrieval-practice-effects-larger-at-retention-intervals-over-one-day.md) [+M] — not yet checked against its sources
- [The benefits of retrieval practice do not depend on an exact match between initial retrieval practice conditions and the final test format](../claims/retrieval-practice-benefits-do-not-require-matching-initial-and-final-test-formats.md) [+M] — not yet checked against its sources
- [Classroom quizzing delivered by clickers, computer software, or paper improves student performance on classroom exams in middle school and college courses](../claims/classroom-quizzing-improves-exam-performance-across-grades-and-content.md) [+M] — not yet checked against its sources
- [Retrieval practice benefits have been observed in children, healthy older adults, and memory-impaired patient groups, not only college students](../claims/retrieval-practice-benefits-generalize-to-children-older-adults-and-memory-impaired-patients.md) [+M] — not yet checked against its sources
- [Retrieval practice benefits learners regardless of trait anxiety level, but higher trait or induced anxiety is associated with smaller testing effects](../claims/higher-anxiety-is-associated-with-smaller-testing-effects.md) [~M] — not yet checked against its sources
- [Spaced Retrieval Outperforms Massed Retrieval Despite Lower Initial Recall](../claims/spaced-retrieval-outperforms-massed-retrieval-despite-lower-initial-recall.md) [+W]
- [Effect Of More Multiple Choice Alternatives Depends On Initial Retrieval Success](../claims/effect-of-more-multiple-choice-alternatives-depends-on-initial-retrieval-success.md) [~W]
- [Adaptive spaced retrieval practice produced higher end-of-semester posttest performance than learner-directed AI study, but fixed spaced retrieval did not significantly outperform learner-directed study](../claims/adaptive-retrieval-posttest-retention-advantage.md) [~M] — attached 2026-10-10 from Mahir Akgun et al. (2026), which proposed "Follow GenAI-enabled adaptive pretesting with structured spaced retrieval practice rather than learner-directed AI study to preserve gains"; tests this page's relationship.

## Objective and learner-valued goal

Ask what the learner wants to be able to do with the material and why, and record it apart from the designer's objective. Agreement, divergence and uncertainty are observations, not assumptions. Then fix the target: the capability (recall a term, explain a relation, apply it to a case), a representative instrument, a criterion chosen locally, the aids permitted, and the horizon. Retrieval evidence is mostly about delayed recall of studied material; if the target is application or a whole skill, say so, because the expectation is weaker there.

For example, a nursing student may value being able to answer a patient's question about a medication on placement, while the designer's objective is one-week cued recall of drug classes and their actions. A recall quiz serves the designer's objective directly and the learner's only in part: answering a patient is an application to a new question, which is where the transfer evidence is conditional. Keep both aims, and assess the application at its own horizon rather than inferring it from quiz scores.

## What would revise this model?

The delayed-retention expectation should weaken if comparable learners, at equal time, on aligned delayed outcomes, show no advantage for retrieval over restudy in defensible comparisons, including unpublished ones; the publication-bias gap already recorded is a reason to watch for this. If within-study manipulations of feedback or of initial success fail to reproduce the between-study moderators, the conditions above should be restated. If retrieval on `high` element-interactivity material or `complex-skill` goals is shown, under controlled comparisons, to help or not to help, replace the "contested" line with that finding. Do not protect the model by relabelling every null as too little feedback or too low success after the fact.

A within-session quiz score, delayed recall, transfer to new questions and valued use are separate claims. The present evidence does not establish an optimal success rate for an individual, an optimal schedule, or a benefit across all domains.

## Design Decisions
<!-- Decision section (2026-09-30 pilot): drafted from the linked claim pages only; every choice
     cites the claims that settle it, with markers capped by each claim's recorded evidence. -->

### Should learners retrieve, or restudy?
- **Default:** replace some restudy with recall from memory; two meta-analyses put testing against restudy or rereading at g = 0.50 and g = 0.51, and repeated testing beat repeated study one week later (61% against 40%) at equal time — [Retrieval Practice Improves Long Term Retention](../claims/retrieval-practice-improves-retention.md) [+S], [Retrieval practice improves long-term retention](../claims/retrieval-practice-improves-retention.md) [+S]
- **Changes when:** only performance minutes after study matters → restudy was ahead on a five-minute test (81% against 75%) and testing won only at two days and one week — [Retrieval practice improves long-term retention](../claims/retrieval-practice-improves-retention.md) [~S]
- **Changes when:** the setting is a classroom → quizzing still beat restudy and other controls across 222 classroom studies (g = 0.499) — [Feedback Enhances Retrieval Practice](../claims/feedback-enhances-retrieval-practice.md) [+S], [Classroom quizzing delivered by clickers, computer software, or paper improves student performance on classroom exams in middle school and college courses](../claims/classroom-quizzing-improves-exam-performance-across-grades-and-content.md) [+M]
- **Tested with:** undergraduates reading science prose; 61 studies of tested against restudied material; classroom studies from middle school to college.
- **Not settled:** Rowland's published studies showed larger effects than unpublished ones (0.58 against 0.25), and the author advises caution about publication bias.

### Should feedback follow retrieval?
- **Default:** give corrective feedback; the testing effect was g = 0.73 with feedback against 0.39 without in one meta-analysis, and g = 0.537 against 0.374 across classroom studies — [Retrieval practice improves long-term retention](../claims/retrieval-practice-improves-retention.md) [+S], [Feedback Enhances Retrieval Practice](../claims/feedback-enhances-retrieval-practice.md) [+S]
- **Changes when:** the learner answered correctly → feedback after correct responses made little difference, even at low confidence; supplying the answer after an error is what raised one-week retention — [Feedback Enhances Retrieval Practice](../claims/feedback-enhances-retrieval-practice.md) [~S]
- **Changes when:** the error was made with high confidence → corrected high-confidence errors are remembered better than low-confidence ones, so correct them clearly — [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [+S]
- **Tested with:** Luganda–English word pairs (258 participants); classroom quizzing studies.
- **Not settled:** the feedback comparisons are across studies, and Adesope et al. (2017) found no moderation by feedback (g = 0.63 against 0.60); feedback timing and elaborated against answer-only feedback after retrieval have no wiki evidence.

### How hard should retrieval be?
- **Default:** pitch retrieval so it usually succeeds, or follow it with feedback; with no feedback and initial success at or below 50% the effect was about zero (g = 0.03), and effects were more robust above 75% success — [Retrieval Failure Reduces Benefit](../claims/retrieval-failure-reduces-benefit.md) [+M], [Retrieval practice effects become more robust as initial retrieval success increases, especially above 75%, while retrieval made too easy yields smaller effects](../claims/retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) [+M]
- **Changes when:** retrieval is made easy with many cues → more initial cues gave smaller effects; free recall beat recognition and fewer letter cues beat more, despite lower success during practice — [Initial retrieval conditions that provide less cue support, such as free recall rather than recognition or fewer letter cues, tend to produce better retention despite lower initial success](../claims/less-initial-retrieval-support-produces-better-retention.md) [~M]
- **Tested with:** lab word lists and word pairs reported in one review chapter; the Rowland moderator analysis.
- **Not settled:** the success threshold comes from a between-study moderator analysis, not a manipulation; where "effortful but achievable" lies for a given learner is not given.

### Which question format: multiple choice or short answer?
- **Default:** either format works when feedback follows; studies disagree and one set of four experiments found d = 0.07 between them — [Evidence on whether initial short-answer questions produce more learning than initial multiple-choice questions is mixed, with recent studies finding little or no difference](../claims/short-answer-versus-multiple-choice-retrieval-practice-evidence-is-mixed.md) [~M], [Retrieval Practice Improves Long Term Retention](../claims/retrieval-practice-improves-retention.md) [+S]
- **Changes when:** there is no feedback → short answer's advantage appears mainly with feedback; without it the higher success of multiple choice can favour multiple choice — [Initial short-answer tests outperform initial multiple-choice tests mainly when feedback follows them; without feedback, the higher initial success of multiple-choice tests can favor multiple-choice](../claims/feedback-determines-whether-short-answer-retrieval-outperforms-multiple-choice.md) [~M]
- **Changes when:** multiple choice is used without feedback → students later produced the wrong lures they had chosen; give feedback after multiple-choice quizzes — [Taking initial multiple-choice tests without feedback can lead students to later produce the incorrect lure answers they selected, even when an overall retrieval practice benefit occurs](../claims/multiple-choice-lures-can-be-learned-as-false-knowledge.md) [-M]
- **Tested with:** college students on lectures and SAT II questions, online college courses, seventh-grade science.
- **Not settled:** whether matching practice format to the final exam matters is answered only for exact matching (it is not required) — [The benefits of retrieval practice do not depend on an exact match between initial retrieval practice conditions and the final test format](../claims/retrieval-practice-benefits-do-not-require-matching-initial-and-final-test-formats.md) [+M].

### When should retrieval happen?
- **Default:** space retrieval across sessions after a delay rather than straight after study; spaced beat massed retrieval at g = 0.74, and massed retrieval immediately after study produced very little learning — [Spaced Retrieval Improves Retention](../claims/spaced-retrieval-improves-retention.md) [+M], [Retrieval practice effects become more robust as initial retrieval success increases, especially above 75%, while retrieval made too easy yields smaller effects](../claims/retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) [+M]
- **Changes when:** the outcome is measured within a day → the effect is smaller (g = 0.41) than at intervals over a day (g = 0.69) — [Retrieval practice effects are larger at retention intervals greater than 1 day (g = 0.69) than at intervals less than 1 day (g = 0.41) in Rowland's (2014) meta-analysis](../claims/retrieval-practice-effects-larger-at-retention-intervals-over-one-day.md) [~M]
- **Tested with:** 29 studies of spaced against massed retrieval; the Rowland meta-analysis.
- **Not settled:** gap lengths for retrieval are not given on these pages; see [Spaced Repetition](../elements/spaced-repetition.md) for gap decisions.

### Will it help learners apply knowledge, not only recall it?
- **Default:** expect some transfer (d = 0.40 across 192 effect sizes), strongest to application and inference questions and across test formats, with elaborated retrieval practice and initial test performance among the strong moderators — [Retrieval Practice Improves Transfer](../claims/retrieval-practice-improves-transfer.md) [~S]
- **Changes when:** the transfer is to rearranged items, untested material or worked-example problems → transfer was weakest there, and bias-corrected estimates often showed none when the favourable moderators were absent — [Retrieval Practice Improves Transfer](../claims/retrieval-practice-improves-transfer.md) [-S]
- **Tested with:** 122 experiments (N = 10,382); prose passages with inferential questions one week later.
- **Not settled:** far transfer to novel problem structures.

### For whom, and with what material?
- **Default:** use it beyond college students; benefits have been reported for children aged 9–11, adults aged 55–65 and memory-impaired patients — [Retrieval practice benefits have been observed in children, healthy older adults, and memory-impaired patient groups, not only college students](../claims/retrieval-practice-benefits-generalize-to-children-older-adults-and-memory-impaired-patients.md) [+M]
- **Changes when:** learners are anxious or the quiz feels high-stakes → benefits held for high and low trait anxiety, but effects were smaller with higher trait anxiety and when anxiety was induced; keep it low-stakes — [Retrieval practice benefits learners regardless of trait anxiety level, but higher trait or induced anxiety is associated with smaller testing effects](../claims/higher-anxiety-is-associated-with-smaller-testing-effects.md) [~M]
- **Changes when:** learners are younger children → a few studies suggest benefits are clearer at age 8 than at 6 — [Retrieval practice benefits have been observed in children, healthy older adults, and memory-impaired patient groups, not only college students](../claims/retrieval-practice-benefits-generalize-to-children-older-adults-and-memory-impaired-patients.md) [~M]
- **Tested with:** evidence reported second-hand in one review chapter (Karpicke 2017).
- **Not settled:** whether retrieval practice works for material high in element interactivity is contested — one study found effects with randomly ordered but not intact text, another found them for both — [The argument that retrieval practice effects do not occur with materials high in element interactivity is contested, and the chapter judges its research base not convincing](../claims/whether-element-interactivity-limits-retrieval-practice-effects-is-contested.md) [~M].

## Related Principles
- [Spaced Learning](spaced-learning.md)
- [Immediate Feedback](immediate-feedback.md)
- [Desirable Difficulties Enhance Learning](../claims/desirable-difficulties-enhance-learning.md)

## Examples
- A biology course opens each lesson with short no-notes prompts that ask learners to explain last week’s concepts before new content begins.
- A language app revisits previously learned vocabulary with delayed recall items and immediate corrective feedback rather than only offering rereading.

## Key Sources
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science, 17*(3), 249-255. [https://doi.org/10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Karpicke, J. D. (2017). Retrieval-Based Learning: A Decade of Progress. Learning and Memory: A Comprehensive Reference, 2nd edition, Volume 2. https://doi.org/10.1016/B978-0-12-809324-5.21055-9

<!-- deprecated 2026-10-01: superseded by the conditional model above; the earlier body is kept for history.
## Description
Retrieval practice is the principle of strengthening learning by having learners actively recall information, ideas, or procedures from memory rather than only restudy them. It is useful when the goal is durable retention and easier future access.

## Implications
Retrieval practice works because the act of remembering strengthens future access better than passive review alone. The design implication is to build in frequent recall opportunities, preferably spaced over time and followed by feedback when correctness matters. Difficult retrieval can be productive, and even high-confidence errors can improve retention once corrected [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~S], but retrieval demands need to stay calibrated so learners are challenged without getting lost or simply rehearsing mistakes.

### Context
#### Requirements
- **Questions or prompts that require recall**
- **Sufficient spacing or repetition for retrieval to matter**
- **Feedback when accuracy is important**
#### Constraints
- **Retrieval without feedback can reinforce errors**
- **Very difficult retrieval can become discouraging if learners lack enough support**

### Target Learning Objectives
- Improve retention, fluency of recall, and transfer through repeated remembering.

### Theory
#### Supporting
- Testing-effect research.
- [Metacognition](self-regulated-learning.md)

### Claims
- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~S] — retrieval becomes especially memorable when confident mistakes are corrected clearly after recall
- [Retrieval Practice Improves Long Term Retention](../claims/retrieval-practice-improves-retention.md) [+S]
- [Retrieval practice improves long-term retention](../claims/retrieval-practice-improves-retention.md) [+S]
- [Feedback Enhances Retrieval Practice](../claims/feedback-enhances-retrieval-practice.md) [+S]
- [Retrieval Failure Reduces Benefit](../claims/retrieval-failure-reduces-benefit.md) [+M]
- [Retrieval practice effects become more robust as initial retrieval success increases, especially above 75%, while retrieval made too easy yields smaller effects](../claims/retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) [+M]
- [Initial retrieval conditions that provide less cue support, such as free recall rather than recognition or fewer letter cues, tend to produce better retention despite lower initial success](../claims/less-initial-retrieval-support-produces-better-retention.md) [~M]
- [Evidence on whether initial short-answer questions produce more learning than initial multiple-choice questions is mixed, with recent studies finding little or no difference](../claims/short-answer-versus-multiple-choice-retrieval-practice-evidence-is-mixed.md) [~M]
- [Initial short-answer tests outperform initial multiple-choice tests mainly when feedback follows them; without feedback, the higher initial success of multiple-choice tests can favor multiple-choice](../claims/feedback-determines-whether-short-answer-retrieval-outperforms-multiple-choice.md) [~M]
- [Taking initial multiple-choice tests without feedback can lead students to later produce the incorrect lure answers they selected, even when an overall retrieval practice benefit occurs](../claims/multiple-choice-lures-can-be-learned-as-false-knowledge.md) [-M]
- [Spaced Retrieval Improves Retention](../claims/spaced-retrieval-improves-retention.md) [+M]
- [Retrieval practice effects are larger at retention intervals greater than 1 day (g = 0.69) than at intervals less than 1 day (g = 0.41) in Rowland's (2014) meta-analysis](../claims/retrieval-practice-effects-larger-at-retention-intervals-over-one-day.md) [+M]
- [Retrieval Practice Improves Transfer](../claims/retrieval-practice-improves-transfer.md) [~S]
- [The benefits of retrieval practice do not depend on an exact match between initial retrieval practice conditions and the final test format](../claims/retrieval-practice-benefits-do-not-require-matching-initial-and-final-test-formats.md) [+M]
- [Classroom quizzing delivered by clickers, computer software, or paper improves student performance on classroom exams in middle school and college courses](../claims/classroom-quizzing-improves-exam-performance-across-grades-and-content.md) [+M]
- [Retrieval practice benefits have been observed in children, healthy older adults, and memory-impaired patient groups, not only college students](../claims/retrieval-practice-benefits-generalize-to-children-older-adults-and-memory-impaired-patients.md) [+M]
- [Retrieval practice benefits learners regardless of trait anxiety level, but higher trait or induced anxiety is associated with smaller testing effects](../claims/higher-anxiety-is-associated-with-smaller-testing-effects.md) [~M]
- [The argument that retrieval practice effects do not occur with materials high in element interactivity is contested, and the chapter judges its research base not convincing](../claims/whether-element-interactivity-limits-retrieval-practice-effects-is-contested.md) [~M]
-->

<!-- merged 2026-10-07 from principles/balance-retrieval-success-and-retrieval-effort ("Balance Retrieval Success and Retrieval Effort"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Balance Retrieval Success and Retrieval Effort

> **Principle** · [All principles](index.md)
> **Evidence** · 5 claims (3 for, 1 mixed, 1 unmarked) · 4 studies (3 quant-synthesis, 1 review), `q2`–`q4` · 3 of 4 report an effect size · 4 claims rest on one study

## Description
The chapter's common theme across manipulations of initial retrieval practice: "Conditions that provide less retrieval support and require more effort from the learner tend to produce greater gains in learning, as long as learners can successfully retrieve material". Spacing, fewer cues, and recall formats add effort, while learning to criterion or feedback can protect success.

## Design Implications

### Context
#### Requirements
- Learners must be able to successfully retrieve material during initial retrieval practice.
- Design conditions that require effort, for example by spacing retrieval trials, while affording relatively high initial retrieval success.
- A learn-to-criterion procedure can help ensure high levels of initial retrieval success.
#### Constraints
- The chapter states the optimal balance between retrieval success and retrieval effort is not entirely clear-cut.
- When initial retrieval success is low, harder conditions such as more multiple-choice alternatives can hurt learning.

### Target Learners
- Learners across ages studying verbal, visual, and text materials

### Target Learning Objectives
- Long-term retention
- Transfer to new questions

### Claims
- [Retrieval Practice Effects More Robust When Initial Retrieval Success Exceeds 75 Percent](../claims/retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) [+M]
- [Less Initial Retrieval Support Produces Better Retention](../claims/less-initial-retrieval-support-produces-better-retention.md) [+W]
- [Spaced Retrieval Outperforms Massed Retrieval Despite Lower Initial Recall](../claims/spaced-retrieval-outperforms-massed-retrieval-despite-lower-initial-recall.md) [+W]
- [Effect Of More Multiple Choice Alternatives Depends On Initial Retrieval Success](../claims/effect-of-more-multiple-choice-alternatives-depends-on-initial-retrieval-success.md) [~W]

## Related Principles
- [Retrieval Practice](retrieval-practice.md)
- [Desirable Difficulties Enhance Learning](../claims/desirable-difficulties-enhance-learning.md)

## Examples
-

## Key Sources
- Karpicke, J. D. (2017). Retrieval-Based Learning: A Decade of Progress. Learning and Memory: A Comprehensive Reference, 2nd edition, Volume 2. https://doi.org/10.1016/B978-0-12-809324-5.21055-9
-->
