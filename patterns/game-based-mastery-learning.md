---
type: pattern
id: game-based-mastery-learning
aliases: [game-based-mastery-learning-eg-duolingo-pattern, game-based-mastery-learning-duolingo-pattern]
title: Game-Based Mastery Learning
description: "A reusable policy in which progress through short, cumulative levels depends on passing a check on the target, with attempt-feedback-retry lessons, review of earlier levels and points paid for accuracy and improvement rather than activity; expected to raise performance outside the app for itemisable, practice-heavy skills, but no claim tests the combination as a whole, only a mastery gate without a game layer, a game layer without a gate, and one app's level system on in-app measures."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
author: gamified mastery learning tradition
grain_size: lesson
---

# Game-Based Mastery Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 23 claims (12 for, 10 mixed, 1 against) · 29 studies (9 causal, 8 review, 7 quant-synthesis, 3 theoretical, 1 qualitative, 1 design), `q1`–`q4` · 5 of 29 report an effect size · 17 claims rest on one study

## Description and scope

A reusable policy for practice-heavy, cumulative skills in which **progress through levels depends on reaching a stated criterion, and the game layer (levels, a progress map, points or XP, streaks) reports that progress rather than paying for activity**: short lessons of attempt → immediate feedback → retry of missed items; a level opens only when a check on the target is passed; earlier levels come back in later sessions; points and badges are given for accuracy and improvement. The intended change is in what learners can do on a task outside the app (`immediate-performance`, `delayed-retention`, `general-achievement`), with continued practice over weeks (`persistence`) as a second, separately measured outcome. It suits `verbal-association` targets (vocabulary, notation), fact fluency and `procedure`s drilled to accuracy; it does not suit open-ended, whole-task judgement.

It sits inside two converted pages and does not repeat their models. The [Mastery Learning pattern](mastery-learning.md) owns the gate-correct-recheck loop: the unit check, the corrective step, the parallel recheck and the attempt limit. The [Gamification principle](../principles/gamification.md) owns what a game layer added to instruction should reward, how scores are shared and how theme and decoration are kept away from the moment of practice. This page owns their combination: **the gate as the game's level structure**, so that a level, a badge or a point means a criterion passed. Learning through a whole game, where the game is the activity, belongs to the [Game-based Learning principle](../principles/game-based-learning.md).

**No claim in this wiki tests this combination as a whole**, against the same practice without a game layer or against conventional pacing. The claims that bear on it are of four kinds: a meta-analysis of mastery programmes without a game layer ([mastery learning improves outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]); a meta-analysis of game layers without a mastery gate ([gamification has small positive effects](../claims/gamification-has-small-positive-effects-on-learning-outcomes.md) [+M]); one analysis of a commercial gamified language app's level system, reported as four claims from one study (the Duolingo case study, below); and the reward experiments that limit what points should be given for ([expected tangible rewards reduce later free-choice engagement](../claims/rewards-undermine-intrinsic-motivation.md) [~S]). Each is carried to this pattern by extrapolation, and the page says how far. The sequence below is the earlier page's (short attempt-feedback-retry cycles, visible progression, mastery thresholds, rewards kept aligned) made concrete; each step states its evidence status, and the response-dependent branches are **untested design proposals**.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | A short placement check on the first two or three levels' targets, scored item by item, before any lesson. Record accuracy, response time and which items were missed; record whether the learner has used a gamified app before and how they speak of points and streaks. Use `novice`, `intermediate` or `advanced` only where the check shows it; keep unknowns. |
| The skill and its levels | Whether the skill is cumulative (later items need earlier ones), whether it breaks into items that can be scored instantly (a word, a sum, a keystroke sequence), and the order of levels. If the target is an open performance (a conversation, an essay, a clinical judgement), record which parts are itemisable and which are not. |
| Context and activities | Setting (`online-self-paced`, `classroom`, `online-instructor-led`, `workplace-clinical`), device (phone, shared computers), session length and frequency, who sees progress (the learner, a teacher, peers, an employer), whether a teacher or facilitator is present and for how long, and any game layer already in place (an app's XP, streaks or leagues; a class points chart). |
| Learner-valued goal | Ask what the learner wants to be able to do and by when (order a meal on holiday, pass a certification, keep up with classmates), and what they think of streaks and rankings. Record disagreement with the designer objective. |
| Designer objective | The capability each level stands for, the criterion that opens the next level, and which later levels depend on it. Name the instrument outside the app that will judge the course. |
| Outcome | Accuracy on new items of passed levels at a stated delay; performance on a task with no game around it; continued practice after week 2 and after any points are hidden; time per level. Each with its instrument and horizon, recorded separately. |

A request to "gamify the course with levels" does not specify these. Ask what the levels stand for, what opens a level and what the outcome outside the app is before choosing points, streaks or a criterion.

## Sequence and conditional policy

The default sequence across a course. Quantities are labelled proposals where no claim gives them; set them locally and record them.

1. **Map the skill into short cumulative levels and state each level's criterion.** A level is 3–6 lessons of 10–15 scorable items on one target (proposal). The criterion is a check on that target without hints, for example 8 of 10 correct on new items (proposal); tell learners what it is. Evidence status: [mastery effects vary with the standard, pacing and test type](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [+M]: in a moderator regression over 103 studies of mastery programmes (no game layer), programmes with a higher unit mastery standard had larger effects. The size of standard that suits a given app is not on the claim page.
2. **Place before the first lesson.** Run the placement check; a learner who meets a level's criterion skips it (tests out). Untested proposal; from the earlier page's "learners at different speeds through the same progression map".
3. **Run each lesson as attempt → immediate feedback → retry.** Each item is answered and marked at once, with the correct answer and one informational sentence ("finished action, so past tense"); missed items return at the end of the lesson until each is answered correctly once. A lesson lasts 5–10 minutes (proposal). Evidence status: untested as a step here; the earlier page's first requirement. The informational sentence is the [Gamification principle](../principles/gamification.md)'s step 3, resting on verbal positive feedback raising later free-choice engagement in the [rewards meta-analysis](../claims/rewards-undermine-intrinsic-motivation.md) [+S] (laboratory tasks).
4. **Make a level mean the skill passed, and repeat lessons at harder settings.** A level opens on the step 1 check, taken on a later day than the last lesson (proposal), not on lessons completed. Inside a level, the same lesson can be redone at a harder setting (fewer word banks, typed rather than chosen answers). Evidence status: in one analysis of a commercial language app's data ([Duolingo case study](../claims/rdd-review-exercises-causal-leveling-up.md) [+M]), a regression discontinuity found that learners who had studied a lesson twice (two levels) answered later review items on it correctly more often than learners who had studied it once, at least for the first level-up; completing more levels went with higher post-test accuracy on items first answered wrongly ([levelling up and checkpoint accuracy](../claims/leveling-up-associated-checkpoint-quiz-accuracy.md) [+W]), and levelling up earlier lessons in a skill went with better review accuracy on later ones ([transfer across lessons](../claims/leveling-up-benefit-transfers-across-lessons.md) [+W]). One study, no effect size printed, in-app measures only.
5. **Give points for accuracy and improvement, never for opening the app.** XP for correct first attempts on new or harder items and for beating the learner's own previous score on a lesson; none for log-ins, time or lessons finished regardless of accuracy. The level map shows criteria passed, not points accumulated. Evidence status: [expected tangible rewards for doing or finishing a task](../claims/rewards-undermine-intrinsic-motivation.md) [~S] lowered later free-choice engagement in laboratory experiments (d = −0.28 to −0.40 across engagement-, completion- and performance-contingent rewards), more for children; undermining was reported weaker for well-defined tasks with a clear quality standard. Carried from laboratory puzzles to points in an app.
6. **When a learner fails the level check, change the correction and cap the attempts.** After a failed check, give a different explanation or a worked example on the missed items, then a parallel check; after a third failed check (proposal), advance with the gap recorded and re-probe it in the next level's first lesson, or route the learner to a person. Evidence status: [in one product's logs](../claims/espark-post-quiz-mastery-failure-rate.md) [~W], students who needed all three post-quiz attempts on a quest reached the 80% criterion only 14% of the time and were promoted after making a video instead. The corrective loop itself is the [Mastery Learning pattern](mastery-learning.md)'s steps 4–7.
7. **Bring earlier levels back.** Open each session with 2–3 minutes of review items from passed levels, weighted toward items missed before (proposal); a passed level whose review accuracy falls below the criterion reopens for one lesson. Evidence status: untested here; the earlier page's "retention through revisit". The [Spaced Learning principle](../principles/spaced-learning.md) owns the schedule.
8. **Prompt the next level; plan for drop-off.** Show the next level on the map and offer it at the end of each lesson. In a self-paced course, set a weekly target of lessons and a soft deadline per level; a streak, if used, tolerates one missed day. Evidence status: in randomised A/B tests in the same app, a visual stand-in for the level system and a pop-up prompting the next level raised lessons completed per level by more than 10% and overall study activity ([level prompts](../claims/ab-tests-level-interventions-increase-lessons.md) [+M]); this measures practice, not learning. Self-paced mastery courses lost more students: in 23 of 32 college studies completion was higher in the conventional class ([self-paced mastery reduces completion](../claims/self-paced-mastery-programs-reduce-college-course-completion.md) [-M]). The streak rule is an untested proposal.
9. **Judge the course outside the app.** Test the capability on a task with no game around it, at the horizon the objective sets; record practice volume, streaks and enjoyment separately. Evidence status: in the mastery meta-analysis, effects on standardised tests were near zero (−0.05 to 0.09) in the four studies that used both kinds of test, against up to 0.64 on locally developed tests ([effects vary with test type](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]); a review of tutoring systems argues that platform interaction and task completion cannot by themselves establish cognitive engagement ([behavioural engagement](../claims/behavioural-engagement-not-cognitive-engagement.md) [~M]).

**Dose and progression across sessions** (all proposals; the only durations on the claim pages are the gamification meta-analysis's finding that duration did not moderate cognitive outcomes, and the Duolingo data windows of two and four months):

| Phase | Session | Support and the source of items | Moving on |
|---|---|---|---|
| Week 1 | 10–15 minutes, 5 days a week; two lessons a session | Short lessons (about 10 items), choices from a word bank or options, feedback and an informational sentence after every item, an easy first level so every learner passes a check early | Level check on day 3 or later; 8 of 10 on new items |
| Weeks 2–4 | 10–20 minutes, 4–5 days a week | Each lesson redone once at a harder setting (typed answers, fewer hints); 2–3 minutes of review items from passed levels at the start; points weighted to harder and previously missed items | Check on a later day than the last lesson; at most three checks, then advance with the gap recorded |
| Week 5 onward | 15–20 minutes, 3–4 days a week | Mixed review across levels replaces most new-item drill; points move from every item to every level; personal records and the learner's own targets replace streak messages | Level criterion as before; one item set per month checked outside the app |
| Before the course ends | One week | Points and streaks hidden; practice continues on the level map alone | Outside-app test at the stated delay; the drop in practice, if any, is recorded |

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Levels and points rise; the outside test does not | Give the same items once in the app's format and once outside it; check what share of points came from items already passed. | If accuracy holds in the app only, the format is carrying the answer (word banks, recognition): move to typed or spoken answers before the check. If points come from easy items, change what earns them. Neither branch is tested. |
| Passes the level check, fails review items on it a week later | Re-probe two items from the level with changed surface details. | Reopen the level for one lesson and add its items to review; a one-day check may be measuring short-term retention. Untested. |
| Practice drops after week 2, or when points are hidden | Compare practice before, during and after; ask what the learner did instead. | If the drop starts with hiding points, points may have displaced interest the learner had: give fewer, informational awards. If it starts before, check difficulty and the learner's goal. Untested. |
| Many quick answers, falling accuracy, a long streak | Compare response time with accuracy for one week; remove the speed element for one session. | If accuracy recovers, speed or volume is what earns points: pay for accuracy on new items only. Untested. |
| Repeated failed checks on one level | Give a prerequisite item from the level before; ask the learner to explain one wrong answer. | If the prerequisite fails, reopen that level; if not, change the correction's form (worked example, a person) rather than cycling the same lesson. Untested. |

## Fitting the design to a situation

**The three facts that most change the decision:**

- **Whether the skill breaks into items scored on the spot.** The loop depends on instant marking and on a check that stands for the skill; a whole performance does not break that way. If unstated, ask: can each practice attempt be marked right or wrong at once, and does passing the items predict doing the real task?
- **Whether learners already want to do the practice.** Points for doing a task risk lowering later engagement most where interest already exists; a dull, necessary drill carries less of that risk. If unstated, ask: do learners practise this now without being made to?
- **Who paces and who sees progress.** Self-paced mastery courses lose more learners; progress seen by a teacher, peers or an employer is a different design from progress only the learner sees. If unstated, ask: is there a class timetable or deadline, and who will see levels, streaks or rankings?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` in the domain | Word banks and recognition items first, typed or spoken answers only after the first level is passed; feedback with the correct answer on every item; a criterion check on day 3 or later | Untested here; the feedback and gate steps rest on the claims in steps 3–4, none tested with novices separately |
| Learners are `advanced`, or already accurate | Placement check and test-out by level; harder settings (typed answers, mixed review) from the start; no points for easy items | Untested proposal; the earlier page's "difficulty should rise in response to growing skill" |
| Learners are `child`ren (under 12) | No tangible prizes for finishing lessons; points and badges for accuracy and effort, worded as information; no public individual ranking; a teacher sees the level map | [Rewards claim](../claims/rewards-undermine-intrinsic-motivation.md) [-S]: tangible rewards more detrimental for children than college students, laboratory tasks |
| `adult`s in a `workplace-clinical` setting (onboarding, compliance) | Levels tied to job tasks passed at a criterion; no badges for completion or seat time; no ranking among colleagues; the manager sees criteria passed, not streaks | Untested proposal; mastery evidence is from school and college courses ([mastery learning improves outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]) |
| Goal is `verbal-association` (vocabulary, terms, notation) | The full loop fits; check recall on new sentences a week after the level, outside the app | [Duolingo level analysis](../claims/rdd-review-exercises-causal-leveling-up.md) [+M] (in-app items, one study); [gamified vocabulary, reported in a review](../claims/quizizz-gamification-better-memorization.md) [+W] |
| Goal is a `complex-skill` or whole-task performance the brief wants kept whole (a conversation, a case, a project) | Use levels only for the itemisable parts (vocabulary, a calculation); the whole performance stays one task, judged on the brief's own rubric, outside the level map; do not split it into items to fit the gate | Untested; the earlier page's constraint "weak fit for complex open-ended performance" |
| `online-self-paced`, no teacher | The software runs feedback, retries, checks and review; a weekly lesson target and a soft deadline per level; a streak that survives one missed day | [Self-paced mastery reduces completion](../claims/self-paced-mastery-programs-reduce-college-course-completion.md) [-M] (college PSI courses, carried to apps); [level prompts](../claims/ab-tests-level-interventions-increase-lessons.md) [+M] (practice volume only) |
| `classroom`, one teacher and many learners | Learners work the levels on devices; the class keeps a common pace with a weekly level target; the teacher spends the session's last 10 minutes with learners who failed a check twice | [Mastery effects vary with pacing](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M] (group-based programmes had larger effects, no game layer); [group-based mastery and attrition](../claims/mastery-improves-engagement-attrition.md) [+M] (one synthesis) |
| Mixed modes: some learners remote, some in the room, or phone-only | One tool reached the same way by everyone; lessons short enough for a phone (about 10 items); no speed-ranked live rounds; level checks run in the tool, not on paper in the room | Untested proposal |
| Scarce facilitator time (volunteers, a busy shift, a tutor who checks in briefly) | Automate feedback, retries and checks; the facilitator spends about 5 minutes a week on a list of learners who failed a check twice or stopped practising, and contacts those | Untested proposal; the attempt cap rests on [eSpark logs](../claims/espark-post-quiz-mastery-failure-rate.md) [~W] |
| Time is a `single-session` | Do not build levels, streaks or a points economy; one short lesson with feedback and retry of missed items, one check at the end; claim nothing about persistence | Untested; no claim here tests a single session |
| A fixed short time budget per session (for example 15 minutes) | 2 minutes review, 10 minutes of one lesson with feedback and retries, 3 minutes for a level check when one is due; never two checks in one session | Untested proposal |
| Learners already practise willingly, or find the task interesting | Keep the level map and informational feedback; drop expected points, prizes and streak rewards | [Rewards claim](../claims/rewards-undermine-intrinsic-motivation.md) [~S] (laboratory tasks, free-choice time; carried to apps) |
| Learners have low confidence or low literacy | Private progress only; a first level everyone passes; feedback with icons and audio; a failed check shown as "one more lesson", not a lost life | Untested proposal |
| Progress or answers are private or sensitive (health, a second-chance course) | The learner controls who sees levels and streaks; no shared boards; a teacher or employer sees only what the learner releases | Untested proposal |
| Levels or points feed a grade, or stakes are high | Keep points formative; grade on an aligned task outside the app at the delay that matters; never grade on streaks or practice volume | [Effects vary with test type](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M] (near-zero effects on standardised tests); [behavioural engagement](../claims/behavioural-engagement-not-cognitive-engagement.md) [~M] |
| The brief names its own routine (an app's XP, streaks or leagues; a class points chart; its own level criterion or rubric) | Keep it; change only what the evidence says matters: points for accuracy and improvement rather than log-ins or completion, a level that opens on a check rather than on lessons finished, and an outside check beside the app's own | [Rewards claim](../claims/rewards-undermine-intrinsic-motivation.md) [~S]; [mastery standard](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]; the combination is untested |
| The brief gives its own categories or skill map (CEFR bands, a job's competency list) | Use those as the levels and their criteria; do not substitute a level scheme of your own | Untested proposal |
| The criterion is set by an automated rule ("N correct in a row") | Prefer a check on new items over a streak of correct answers; if a streak rule is kept, record how many items learners need to pass | [Simulated mastery learning](../claims/problem-counts-by-knowledge-tracing-condition.md) [~W]: with 30 simulated students per condition, a streak rule gave more problems than knowledge tracing (about 17 against 11 for one problem type); simulated, not real learners |
| The brief reports an error learners actually made | Make it a feedback item: a near-miss answer shown beside the correct one, with the sentence that separates them, in the lesson and in the check | Untested proposal |

Ten of the twenty rows link a claim (children, adults at work, vocabulary, self-paced, a classroom with one teacher, scarce facilitator time, already-interested learners, high stakes, the brief's own routine, and the automated criterion), and each says where it carries the claim beyond the learners or settings it tested; only the vocabulary and self-paced rows draw on a gamified app, and that is one study. The other rows are untested proposals or the earlier page's guidance.

## Choosing configurations from evidence

- **Whether to gate at all.** [Mastery learning programmes, 108 controlled evaluations](../claims/mastery-learning-improves-outcomes.md) [+M]: across 103 studies of examination performance, mastery programmes (Keller's self-paced PSI and Bloom's group-based Learning for Mastery) raised scores by 0.52 SD on average against conventionally paced classes, at college, high-school and upper-elementary levels; the claim's table gathers 7 distinct studies behind the question. No study had a game layer. It supports a level that opens on a criterion as a candidate configuration, not a gamified app.
- **What the gate's effect depends on.** [Mastery effects vary with the standard, pacing and test type](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]: larger effects with a higher unit standard, group-based rather than self-paced programmes, locally developed tests, and comparison groups receiving less quiz feedback; standardised-test effects near zero where both were used. Its table gathers 6 distinct studies. For an app this means: a high criterion, some common pacing where possible, and an outside test that is not the app's own.
- **Whether a game layer adds anything.** [Gamification has small positive effects](../claims/gamification-has-small-positive-effects-on-learning-outcomes.md) [+M]: a meta-analysis of 40 experiments (2013–2017, school, university, work and informal settings) found cognitive g = .49, motivational g = .36 and behavioural g = .25, all heterogeneous; among the more rigorous designs only the cognitive effect held (g = .42). It pools many combinations of elements and does not show that levels, points or streaks carry the effect, nor that a game layer adds to a mastery gate.
- **What a level structure does inside one app.** The Duolingo case study (Portnoff et al. 2021), one study read as four claims: a regression discontinuity on about two months of review data ([levelling up and later accuracy](../claims/rdd-review-exercises-causal-leveling-up.md) [+M]); a regression over four months of checkpoint quiz data controlling for item, user, course and prior proficiency ([levels and checkpoint accuracy](../claims/leveling-up-associated-checkpoint-quiz-accuracy.md) [+W]); the same review analysis for earlier lessons ([transfer across lessons](../claims/leveling-up-benefit-transfers-across-lessons.md) [+W]); and randomised A/B tests of level prompts ([level prompts](../claims/ab-tests-level-interventions-increase-lessons.md) [+M], more than 10% more lessons per level). No effect size is printed for any of them, every outcome is measured inside the app, and none compares the app with or without its game layer. It says that studying a lesson again at a higher level goes with better later in-app accuracy and that prompts raise practice; it does not say the game layer caused learning.
- **What points should pay for.** [Expected tangible rewards reduce later free-choice engagement](../claims/rewards-undermine-intrinsic-motivation.md) [~S]: two competing meta-analyses of laboratory experiments (128 and 96 studies), the 1971 experiment and two reviews. Deci et al. (1999) found engagement-, completion- and performance-contingent tangible rewards lowered later free-choice engagement (d = −0.28 to −0.40) and verbal positive feedback raised it (d = 0.33); Cameron and Pierce (1994) found no overall undermining and a minimal effect only for expected tangible rewards for doing a task. The claim's table gathers 8 distinct studies. This is the limit on the pattern: a game layer that pays for opening the app or finishing lessons is the configuration most at risk.
- **The cost of self-pacing.** [Self-paced mastery reduces completion](../claims/self-paced-mastery-programs-reduce-college-course-completion.md) [-M]: in 32 PSI studies, 23 had higher completion in the conventional class (h = −0.14 on attrition), while the examination advantage held either way. Group-based mastery classes reported lower attrition in 7 of 8 disciplines in one evaluation ([group-based mastery and attrition](../claims/mastery-improves-engagement-attrition.md) [+M]). Most gamified apps are self-paced; the drop-off risk is in the brief, not a side issue.
- **What the platform's own data can show.** [Behavioural engagement indicators do not establish cognitive engagement](../claims/behavioural-engagement-not-cognitive-engagement.md) [~M] (a review's argument about tutoring platforms) and [gamification's effect on engagement in adaptive platforms is mixed](../claims/gamification-engagement-mixed-evidence.md) [~M] (one review citing one study of large impact and another of minimal effect). Streaks, XP and lessons completed are observations about practice, not about the capability.

Do not rank this pattern against an ungamified mastery course or a conventional course from these claims: none compares them. A precise abstention names the missing comparison (the same levelled practice with and without the game layer, on an outside test at a stated delay, with practice after the layer is removed) and the local observation that would stand in for it.

## The evidence by question

- *In a gamified mastery app, does working through a lesson's levels raise practice and later accuracy?* [Completing more skill levels is associated with higher Checkpoint Quiz post-test accuracy](../claims/leveling-up-associated-checkpoint-quiz-accuracy.md) [+W] gathers the narrower claims from the same app study (one study, in-app measures).
- *Does adding a game layer to instruction raise outcomes, and which outcomes?* [Gamification has small positive effects on cognitive, motivational and behavioral learning outcomes](../claims/gamification-has-small-positive-effects-on-learning-outcomes.md) [+M] gathers the narrower claims on gamified practice and engagement.
- For the gate itself (whether it raises examination performance, which variant, at what cost), use the questions on the [Mastery Learning principle](../principles/mastery-learning.md), starting from [Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [+M] (7 distinct studies in its table).

## Further evidence, not yet read against this model

Claims found while converting this page that bear on it but are not part of the model above. Each says what it is and how far it bears on the page.

- [Quizizz-based gamification improved word memorization over traditional methods for intermediate learners](../claims/quizizz-gamification-better-memorization.md) [+W] — one study reported second-hand in a review, no effect size; a gamified quiz platform for vocabulary, with no mastery gate.
- [In one mixed-methods study of university students, reported in a review, gamified vocabulary learning gave better test results, motivation and satisfaction than traditional instruction](../claims/gamification-raises-motivation-satisfaction.md) [+W] — one study reported second-hand; gamified vocabulary practice, no gate described.
- [BKT is the most efficient knowledge tracing approach overall in simulated online mastery learning, though DKT is more efficient for AS and M problems](../claims/bkt-most-efficient-online-mastery-learning.md) [~W] — simulated students; bears on how software decides a level is passed, not on the game layer.
- [Reviewed literature identifies personalisation, adaptive support, rapid feedback, and teacher-facing automation as recurring pedagogical opportunities of AI in mathematics education](../claims/ai-math-pedagogical-opportunities-personalisation-feedback.md) [+W]
- [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [+M]
- [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [~M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]
- [Worked examples can become redundant or counterproductive for advanced learners.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

## Illustrative design instance and observation record

*Invented illustration, not a tested course.* Adult learners in a hospital's housekeeping team (`adult`, `workplace-clinical`, phone-only) learn 200 English workplace phrases over eight weeks, in 15-minute slots at the start of shifts, with a supervisor who can spare about 5 minutes a week. The brief names its own skill map (the hospital's list of phrases by task: greeting a patient, reporting a spill, asking for a colleague) and wants no ranking among staff. The table changed the default: levels follow the hospital's task list; each level is four lessons of about 10 items with audio, feedback and retry of missed items; a level opens on 8 of 10 on new items, taken on a later shift; points come only for correct first attempts and personal bests; progress is private, and the supervisor sees only a list of who failed a check twice or has not practised for a week. A learner says she wants to understand patients' requests on the ward; the designer's objective is producing the phrases. They agree to add a listening item to each level check, and in week 8 points are hidden and a supervisor asks each learner three ward questions face to face. The level-analysis claims come from a language app's in-app data, not from this population, setting or outcome; these are local choices to observe.

Record: **level, its target and criterion → placement result → lessons taken, items, attempts and feedback received → points earned and for what → level check form, date, attempt number and response → correction given after a failed check → review accuracy on passed levels → practice per week, before and after points were hidden → outside-app test and horizon → candidate interpretations (skill passed, app format carrying the answer, short-term retention, points displacing interest) and their basis**, alongside the learner's stated goal and any change in it. An agent may summarise this record but must not fabricate missing inputs or assign a probability that a learner "has mastered" a level without a calibrated model.

## Elements and limits

[Adaptive mastery learning](../elements/adaptive-mastery-learning.md), [adaptive difficulty](../elements/adaptive-difficulty.md), [feedback](../elements/feedback.md), [practice](../elements/practice.md), [reassessment](../elements/reassessment.md), [formative assessment](../elements/formative-assessment.md), [progress tracking](../elements/progress-tracking.md) and [gamification](../elements/gamification.md). Principles the pattern draws on: [Mastery Learning](../principles/mastery-learning.md), [Gamification](../principles/gamification.md), [Game-Based Learning](../principles/game-based-learning.md), [Immediate Feedback](../principles/immediate-feedback.md), [Spaced Learning](../principles/spaced-learning.md) and [Self-monitoring](../principles/self-monitoring.md).

This pattern is scoped to cumulative skills that break into items scored on the spot. Open-ended performances, contested judgement and programme-level certification need other configurations ([competency-based learning](competency-based-learning.md), [epistemic games](epistemic-games.md)). The policy supports observation and design reasoning; whether a gamified mastery course produces better outside-app performance than the same levelled practice without the game layer, for which learners, at what cost in drop-off and at what horizon, remains to be tested.

## Claims

- [Point values and point order altered item selection and recall: Easy First order produced higher recall, and points increased goal pursuit but appeared to hurt recall](../claims/point-values-order-alter-selection-recall.md) [~W]

## Related Patterns
- [Programmed Instruction](programmed-instruction.md) — the historic ancestor of this pattern's small-step, immediate-feedback, self-paced core
- [Epistemic Games](epistemic-games.md) — uses game structures for situated professional judgment rather than repeatable skill drills
- [Mastery Learning](mastery-learning.md) — owns the gate-correct-recheck loop this pattern turns into levels
- [Competency-Based Learning](competency-based-learning.md) — programme-level progression on demonstrated competence, without the game layer
- [Cognitive Load Reduction (CLT Scaffolding Approach)](../principles/cognitive-load-theory.md)
- [Traditional Lecture / Reading / Midterm / Final Assessment](traditional-lecture-based-instruction.md)
- [Scaffolding via level-gated progression and hearts in Duolingo](../designs/duolingo-scaffolding-hearts-progression.md)

## Examples
- [Scaffolding via level-gated progression and hearts in Duolingo](../designs/duolingo-scaffolding-hearts-progression.md) — a design that uses this pattern
- Duolingo-style language progression with retries, review lessons and a level map; the [level analysis](../claims/rdd-review-exercises-causal-leveling-up.md) [+M] comes from one such app's data
- Mastery-based digital math practice in which a skill opens only after a check on new items
- Duolingo-style language progression with retries, streaks, and review loops.
- Mastery-based digital math practice with adaptive item difficulty.
- Technical skill trainers that unlock later levels only after demonstrated competence.

## Key Sources
- Gee, J. P. (2003). *What video games have to teach us about learning and literacy*. Palgrave Macmillan. [doi:10.1145/950566.950595](https://doi.org/10.1145/950566.950595)
- Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)
- Sailer, M., & Homner, L. (2020). The gamification of learning: A meta-analysis. *Educational Psychology Review, 32*(1), 77–112. [doi:10.1007/s10648-019-09498-w](https://doi.org/10.1007/s10648-019-09498-w)
- Portnoff, L., Gustafson, E., Bicknell, K., & Rollinson, J. (2021). Methods for language learning assessment at scale: Duolingo case study. *Proceedings of the 14th International Conference on Educational Data Mining (EDM21)*. https://educationaldatamining.org/edm2021/
- Kapp, K. M. (2012). *The gamification of learning and instruction*. Pfeiffer.
- Van Eck, R. (2006). Digital game-based learning: It's not just the digital natives who are restless. *EDUCAUSE Review, 41*(2), 16-30.

<!-- deprecated 2026-10-15: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Game-Based Mastery Learning is the short-form canonical target for mastery designs that combine progression gates, repeated practice, feedback, and game-like incentives or progression signals.

## Implications

### Context
#### Requirements
- **Short cycles of attempt, feedback, and retry**
- **Visible progression and mastery thresholds**
#### Constraints
- **Rewards can distort motivation if poorly aligned**
#### Grain Size
- Lesson
- Unit

### Target Goals
- Build incremental skill mastery and persistence through feedback-rich progression.

### Theory
#### Supporting

- [Mastery Learning](../principles/mastery-learning.md)
- [Game-Based Learning](../principles/game-based-learning.md)
- [Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]

## Claims
- [Expected tangible rewards reduce later free-choice engagement with a rewarded task, while verbal praise does not](../claims/rewards-undermine-intrinsic-motivation.md) [-S]

## Related Patterns
- [Game-Based Mastery Learning (e.g., Duolingo Pattern)](game-based-mastery-learning.md)
- [Programmed Instruction](programmed-instruction.md) — the historic ancestor of this pattern's small-step, immediate-feedback, self-paced core
- [Epistemic Games](epistemic-games.md) — uses game structures for situated professional judgment rather than repeatable skill drills

## Key Sources
- Gee, J. P. (2003). *What video games have to teach us about learning and literacy*. Palgrave Macmillan. [doi:10.1145/950566.950595](https://doi.org/10.1145/950566.950595)
-->

<!-- merged 2026-10-15 from patterns/game-based-mastery-learning-eg-duolingo-pattern ("Game-Based Mastery Learning (e.g., Duolingo Pattern)"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Game-Based Mastery Learning (e.g., Duolingo Pattern)

> **Pattern** · [All patterns](index.md)
> **Evidence** · 5 claims (2 for, 3 mixed) · 12 studies (4 review, 3 theoretical, 2 causal, 2 quant-synthesis, 1 qualitative), `q1`–`q4` · 0 of 12 report an effect size · 1 claim rests on one study

## Description
Game-Based Mastery Learning combines mastery progression with game-like mechanics such as levels, streaks, rewards, adaptive challenge, and immediate feedback. The pattern works by requiring learners to demonstrate competence before moving forward while using feedback and progression signals to sustain engagement. Its value is not the game layer alone; it is the pairing of repeated practice, visible progress, and retry loops.

This pattern can be highly effective for incremental skill development, especially when tasks can be broken into frequent attempts with fast feedback. It becomes weaker when reward mechanics overshadow learning goals or when mastery thresholds are poorly calibrated.

## Implications

### Context
#### Requirements
- **Frequent checkable tasks**: The pattern needs short cycles of attempt, feedback, and retry.
- **Visible progression**: Learners need to see what they have mastered and what comes next.
- **Clear mastery thresholds**: Advancement rules should reflect meaningful competence rather than arbitrary completion.
- **Adaptive or sequenced challenge**: Difficulty should rise in response to growing skill.
#### Constraints
- **Motivational distortion**: Rewards can crowd out intrinsic interest if they become the main reason for participation.
- **Mastery frustration**: Thresholds that are too strict can demotivate struggling learners.
- **Shallow gamification**: Points and badges alone do not create strong learning.
- **Weak fit for complex open-ended performance**: The pattern works best for modular skill progression rather than ambiguous whole-task judgment.
#### Grain Size
- Lesson
- Unit

### Target Goals
- **Incremental skill mastery**: Building competence through repeated successful performance.
- **Persistence and return**: Encouraging ongoing engagement across many short practice cycles.
- **Retention through revisit**: Bringing earlier material back into later practice.

### Target Learners
- **Learners working on cumulative skills**: Strong fit for language, math, notation, and other practice-heavy domains.
- **Learners benefiting from visible progress markers**: Especially useful when momentum and habit matter.
- **Digital learning participants**: Many implementations depend on platform-based tracking and adaptation.

### Theory
#### Supporting

- Mastery learning perspectives — progression should depend on competence rather than simple seat time.
- Feedback and self-regulation perspectives — visible progress and frequent correction support monitoring and persistence.
- Game-based motivation perspectives — challenge, progression, and reward can sustain engagement when aligned well.
- [Reviewed literature identifies personalisation, adaptive support, rapid feedback, and teacher-facing automation as recurring pedagogical opportunities of AI in mathematics education](../claims/ai-math-pedagogical-opportunities-personalisation-feedback.md) [+W]

#### Contradicting / Qualifying
- Extrinsic mechanics should support learning goals, not replace them.
- Some domains require richer forms of assessment than rapid mastery loops can provide.

### Claims
#### Supporting
- [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [+M]
- [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [~M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]
#### Contradicting
- [Worked examples can become redundant or counterproductive for advanced learners.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

## Design

### Sequence
1. Present a short challenge at an appropriate difficulty level.
2. Give immediate feedback and allow retry or correction.
3. Require a defined mastery threshold before progression.
4. Reintroduce prior content through review or spaced challenge.
5. Increase difficulty or reduce support as competence grows.

### Elements Used
- [Adaptive Difficulty](../elements/adaptive-difficulty.md)
- [Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md)
- [Feedback](../elements/feedback.md)
- [Practice](../elements/practice.md)

### Affordances
- [Game-Based Learning](../principles/game-based-learning.md)
- [Immediate Feedback](../principles/immediate-feedback.md)
- [Competency-Based Learning & Assessment](../principles/competency-based-assessment.md)
- [Self-monitoring](../principles/self-monitoring.md)

### Personalization
- Difficulty can adapt to learner performance.
- Different learners can move at different speeds through the same progression map.
- Feedback and hints can be faded as mastery grows.

## Related Patterns

- [Cognitive Load Reduction (CLT Scaffolding Approach)](../principles/cognitive-load-theory.md)
- [Traditional Lecture / Reading / Midterm / Final Assessment](traditional-lecture-based-instruction.md)
- [Mastery learning cycle of formative tests, correctives, and relearning](mastery-learning.md)
- [Scaffolding via level-gated progression and hearts in Duolingo](../designs/duolingo-scaffolding-hearts-progression.md)

## Examples
- Duolingo-style language progression with retries, streaks, and review loops.
- Mastery-based digital math practice with adaptive item difficulty.
- Technical skill trainers that unlock later levels only after demonstrated competence.

## Impact
- Often increases persistence and visibility of progress in modular skill domains.
- Works best when mastery definitions are instructionally meaningful and not merely gamified gating.

## Key Sources
- Gee, J. P. (2003). *What video games have to teach us about learning and literacy*. Palgrave Macmillan. [doi:10.1145/950566.950595](https://doi.org/10.1145/950566.950595)
- Kapp, K. M. (2012). *The gamification of learning and instruction*. Pfeiffer.
- Van Eck, R. (2006). Digital game-based learning: It's not just the digital natives who are restless. *EDUCAUSE Review, 41*(2), 16-30.
-->

<!-- merged 2026-10-15 from patterns/game-based-mastery-learning-duolingo-pattern ("Game-Based Mastery Learning (Duolingo Pattern)"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Game-Based Mastery Learning (Duolingo Pattern)

> **Pattern** · [All patterns](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 quant-synthesis), `q4` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
This page is the short-form canonical target for Duolingo-style game-based mastery learning, where frequent practice, progression gates, feedback, and motivational signals are combined in a mastery sequence.

## Implications

### Context
#### Requirements
- **Short feedback-rich practice cycles**
- **Visible progression and challenge calibration**
#### Constraints
- **Gamification signals must stay aligned with learning goals**
#### Grain Size
- Lesson
- Unit

### Target Goals
- Build incremental skill mastery with persistent return to practice.

### Theory
#### Supporting

- [Mastery Learning](../principles/mastery-learning.md)
- [Game-Based Learning](../principles/game-based-learning.md)
- [Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]

## Related Patterns

- [Game-Based Mastery Learning](game-based-mastery-learning.md)
- [Scaffolding via level-gated progression and hearts in Duolingo](../designs/duolingo-scaffolding-hearts-progression.md)

## Key Sources
- Gee, J. P. (2003). *What video games have to teach us about learning and literacy*. Palgrave Macmillan. [doi:10.1145/950566.950595](https://doi.org/10.1145/950566.950595)
-->
