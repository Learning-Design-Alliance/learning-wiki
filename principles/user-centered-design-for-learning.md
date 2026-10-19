---
type: principle
id: user-centered-design-for-learning
aliases: [design-with-students-empathy-interviews]
title: User-Centered Design for Learning
description: "For learners who reach instruction through a digital interface, revising that interface against what representative users actually do on the real learning tasks (finding, reading, submitting, interpreting) is expected to remove avoidable effort and failed attempts that compete with the content, though no claim in the wiki compares a user-tested interface with an untested one on a learning outcome."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
sources:
  - id: coenraad-2021
    resource: "https://dschool.stanford.edu/resources/liberatory-design-cards"
    title: "Coenraad, M., Hodge, M., Ruiz, P., Mills, K., & Burke, Q. (2021). Empathy Interviews for Developing Inclusive Computing Pathways. Washington, D.C.: Center for Inclusive Innovation, Digital Promise. https://dschool.stanford.edu/resources/liberatory-design-cards"
    author: "Coenraad, M., Hodge, M., Ruiz, P., Mills, K., & Burke, Q"
---

# User-Centered Design for Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 22 claims (13 for, 8 mixed, 1 against) · 19 studies (7 design, 6 causal, 4 qualitative, 1 quant-synthesis, 1 associational), `q1`–`q4` · 3 of 19 report an effect size · 21 claims rest on one study

## Conditional relationship

This page owns the **interface** a learner must operate to reach instruction: a course page, a learning app, a dashboard, a report a learner or parent must read, an AI tool's screen. For learners who reach the content through such an interface, an interface whose navigation, labels, layout, placement of information and technical set-up have been checked against what representative users actually do on the real tasks (find the assignment, open the activity, submit work, read the feedback, interpret a score), and revised where they stall, is expected to cost them less avoidable effort and fewer failed attempts than an interface built from the designer's assumptions. The expected change is first in task completion, errors, time and rated usability on those tasks, and through them in what the learner can attend to: `immediate-performance` or understanding on the content, where the interface was taking effort from it. It is a precondition for the pedagogy, not a substitute for it: a usable interface around a weak activity is still a weak activity.

**No claim in the wiki compares a user-tested interface with an untested one on a learning outcome, or tests the user-centred process as such.** What the wiki holds is narrower. One design-comparison study of a school report card site found that moving a link to where the reader needs it improved usability, that showing points possible improved understanding of how a score is calculated, and that a feature which helped one task lowered usability ratings. One classroom study found that higher self-reported extraneous load predicted lower post-test scores, an association, not a test of interface design. The rest are single-group usability ratings of particular tools after they were built, which show the tool was rated usable by those who answered, not that user testing caused it or that learning followed. The steps below are therefore a **default design**, labelled step by step.

The relationship is conditional on four things: **who the users are and which tasks they must do** (learners, teachers and parents use the same system for different tasks); **the device and connection they actually have** (a site that works on a laptop can fail on a phone, and a login or loading failure stops everything before the interface design is even reached); **the learner's familiarity with this kind of interface** (expected to matter most for those new to its conventions, and for learners who depend on accessibility features; untested here); and **which outcome counts** (rated usability, success on a task, and learning can move apart).

How the converted siblings sit beside this page: [Cognitive Load Management](cognitive-load-management.md) and [Cognitive Load Theory](cognitive-load-theory.md) hold the model for removing avoidable processing from the *presentation of content*; this page applies the same lever to the controls and screens around it and owns the user-testing loop that finds where the effort is. [Digital Learning](digital-learning.md) decides whether a digital tool earns its place and credits gains to the method it carries. [Universal Design for Learning](universal-design-for-learning.md) holds the planning audit for demands that are not part of the goal, including access routes. [Technology Augments, Not Supplants, Processes](technology-augments-not-supplants-processes.md) holds what part of the learning process a tool may do for the learner. The design process itself is described in [Learner Experience Design](../processes/learner-experience-design.md) and [Design Thinking](../processes/design-thinking.md); its methods include [Learner Personas](../methods/learner-personas.md) and [Needs Analysis](../methods/needs-analysis.md).

## Default design, while the relationship is untested

The earlier page's guidance, kept as a concrete default a designer can act on and revise. Each step is a proposal; its evidence status is stated beside it. The quantities are untested proposals unless a claim is linked.

1. **Name the users and their tasks before drawing a screen.** List each kind of user (learner, teacher, parent, administrator) and the five to ten tasks each must do with the interface, worded as the user would say them ("find what's due this week", "see why my score dropped"). Build personas from interviews or observation of real users, not from the designer's guesses; where no real data exist, label the persona as an assumption to be checked. Untested; from the earlier page. See [Learner Personas](../methods/learner-personas.md).
2. **Watch a few users before designing.** Spend one to two days observing or interviewing five to eight representative users doing the current version of the tasks (or a paper version), noting where they hesitate and the words they use for things. Include users whose circumstances differ most from the designers' own (a different device, language, schedule or access need), since designers default to imagining users like themselves. Untested proposal; the earlier page's front-end analysis (ethnography, focus groups) and the merged empathy-interview page. Empathy interviews are a common way school improvement teams gather this kind of input, though no claim here measures what they change: [Empathy interviews became a widely adopted data-gathering technique for understanding stakeholder perspectives on problems](../claims/empathy-interviews-adopted-by-improvement-teams.md) [+W] and [Empathy interviews are among the most commonly discussed continuous improvement practices for advancing equity](../claims/empathy-interviews-central-equity-practice.md) [+W] (two interview studies of district and school improvement teams; adoption reported, no outcome measured). Keep input from the users going through the project, not only at the start: [Training and technical assistance is most engaging when it is grounded in clear expectations, designed around recipient needs, developed with ongoing recipient input, accessible, delivered by equipped providers, and framed as a partnership](../claims/ta-engagement-six-elements-interviews.md) [+W] (interviews with 12 people who design, provide and receive training and technical assistance; carried here from that setting to interface design).
3. **Arrange navigation in the users' own categories.** Before fixing menus, ask users to group the course's items (an open card sort, 30 to 40 items, 10 to 15 users) and name the groups; use their names where they agree. Untested; from the earlier page.
4. **Check paper or wireframe versions first, cheaply.** Run a heuristic evaluation against Nielsen's ten heuristics and a cognitive walkthrough of each core task on a paper prototype or wireframe (one to two hours per task by two reviewers), and fix what both find before any build. Untested; from the earlier page.
5. **Put information where the user makes the decision it serves.** Place each link, explanation or score breakdown beside the thing it explains, not at the top of the page or in a separate help area. [Moving the link to the STAR framework from the top of the page to beneath the STAR score improved the school report card site's usability](../claims/star-link-beneath-score-improves-usability.md) [+M] and [Reporting the number of points possible for each metric led to better understanding of how the STAR score is calculated](../claims/points-possible-improves-score-understanding.md) [+M] (one design-comparison study of a public school report card site; readers were not described as learners on the claim pages).
6. **Test the working version on the real tasks, in rounds.** With a functional prototype, have five users per round do each core task while thinking aloud; record whether they complete it unaided, the errors, the time, and where they stall. Fix the worst stalls and test again: three rounds before launch is a default. Move on from a task when four of five users in a round complete it unaided. The numbers are untested proposals. Test combinations of changes as well as each change: [The combination of moving the STAR link and reporting points possible produced the best performance on all measures](../claims/combined-design-changes-best-performance.md) [+M] (same report card study). Plan an explicit adjust-and-retest phase before judging whether the tool is useful: [After design adjustments, the LAD achieved good–excellent usability (SUS M = 4.13, equal to 78.25%)](../claims/thermos-lad-sus-good-excellent-usability.md) [+W] (42 students rating a learning analytics dashboard after adjustments; no comparison with the unadjusted version).
7. **Test on the devices and connections users have, and fix the plumbing first.** Include phone users in every round if any learner will use a phone, and check login, loading time and connectivity in the real setting before testing the design. [Participants who accessed the report card site with mobile devices had more difficulty using it](../claims/mobile-access-increases-report-card-difficulty.md) [~M]; [Technical issues (login scanning, internet connectivity, projector setup, and glitches) frustrated students and created a significant barrier to playlist implementation](../claims/technical-issues-barrier-playlist-implementation.md) [-M] (four after-school sites; educators' reports).
8. **Measure usability and the learning task separately, and report the spread.** Record task success on the content (can they read the score correctly, find and complete the activity) beside the usability rating; a feature can help the task and be disliked, or be liked and not help. Report the range of individual ratings, not only the mean, and how many of the users answered, and follow up the lowest and the silent: a rating from 30 of 46 users describes the 30, as in [Students rated AISSA's usability as excellent, with an average SUS score of 83.38 from 30 of 46 pilot students](../claims/aissa-sus-usability-83.md) [~W] (one pilot of an AI slide-feedback tool; no comparison, no learning outcome). [Making year-over-year change salient helped users identify which schools improved most but lowered usability and satisfaction ratings](../claims/year-over-year-salience-mixed-effects.md) [~M]; [The system receives a good average usability rating (SUS 69.7, grade B) but with wide individual variation attributed to UI consistency issues](../claims/photon-fusion-sus-good-but-variable-usability.md) [~W] (10 participants, one one-hour VR lab session).
9. **Give learners a short orientation, then fade it.** In the learner's first session with the interface, spend five to ten minutes on a guided walk through the two or three core tasks (find, do, submit) on their own device; in the second session give a one-page or one-screen reference and no walk-through; from the third, nothing, unless a learner fails a core task. A learner moves on when they complete each core task once unaided. Untested proposal.
10. **Keep watching after launch, and revise between terms.** In the first two weeks, read help requests and logs for where learners stall or drop out (a task many start and few finish), interview two or three of them, including learners who have stopped logging in at all, and fix the top problems before the next cohort; repeat each term. Untested proposal; the earlier page's iterative process budget. District teams in one study reported using empathy interviews for exactly this, to learn why students were not logging into remote classes: [Empathy interviews became a widely adopted data-gathering technique for understanding stakeholder perspectives on problems](../claims/empathy-interviews-adopted-by-improvement-teams.md) [+W] (reported use, no outcome measured).

When a condition is not met: if no real users can be reached before launch, run steps 4 and 9 and treat the first cohort as the first test round (step 10), saying so; if the interface is simple, familiar and used once, steps 3 and 6 can shrink to one quick round, since the earlier page judged the investment pays mainly when an interface is complex, novel or used repeatedly by many learners.

## Fitting the design to a situation

The three facts that most change the decision:

- **Who the users are, and which tasks they must do with the interface.** A learner submitting work, a teacher reading a dashboard and a parent reading a report need different tests with different people. If unstated, ask: who will use this, for which five tasks, and can we reach some of them before launch?
- **The device, connection and access needs the users actually have.** Phones, shared or school-managed devices, slow connections and assistive technology change what fails. If unstated, ask: what will they open it on, where, and does anyone use a screen reader, magnification or captions?
- **Which outcome decides success.** Rated usability, completing a task, and learning the content are separate outcomes and can disagree. If unstated, ask: what must a user be able to do with this screen, and how will we know they did it right, not only that they liked it?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Users are `novice` with this kind of interface, or new to digital learning | Add the first-session walk-through (step 9) and test with first-time users; use plain labels from their own words, not system terms | untested; from the earlier page (largest payoff for novices to the interface's conventions) |
| Users are experienced with this platform's conventions | Keep the platform's conventions rather than inventing new ones; test only the new or changed tasks; skip the orientation | untested proposal |
| Learners are `child` | Test with children of the age, in the setting, with a teacher or parent present and consent from both; watch rather than ask (ratings questionnaires are written for adults); keep sessions to 15–20 minutes; adults' ratings on a child's behalf do not replace a test with children | untested proposal for the session design; adults rating a tool for children: [Adults rated the LLM-powered iCub storytelling system as usable, with a total SUS score of 76.70 indicating good product usability](../claims/icub-storytelling-sus-76-good-usability.md) [~W] (25 adults rated a storytelling robot that most of them judged suited to children under 10; no children were tested, so the rating says nothing about whether children can use it) |
| Learners are `adult` or `adult-workplace` users with little time | Test in their workflow, on their work device, in 20–30 minute sessions; put the tasks they do most on the first screen | untested proposal |
| Learners depend on accessibility features (screen readers, captions, keyboard only; learners with autism or attention differences) | Recruit them for every test round, not a final check; test each core task with their own assistive technology; include them in the card sort | untested; from the earlier page (accessibility-dependent learners named as a main beneficiary) |
| Learners have low literacy or are working in a second language | Use short labels, icons with text, and feedback vocabulary they use; test whether they can say back what a message means | [Students encountered usability obstacles: text-recognition errors, feedback-generation delays, and overly complex vocabulary](../claims/ai-helper-usability-obstacles.md) [~W] (one think-aloud case study of an AI feedback tool; carried to interfaces generally) |
| Many users are on phones, or some join remotely while others are in the room | Design the phone layout first and test on phones in every round; run remote test sessions by screen share and in-room ones by observation, on the same tasks | [Participants who accessed the report card site with mobile devices had more difficulty using it](../claims/mobile-access-increases-report-card-difficulty.md) [~M] (report card site, not a course; the mixed-mode part is an untested proposal) |
| Unreliable connections, shared devices or school-managed logins | Fix and test login, loading and offline behaviour in the real setting before any design test; allow work to be saved and resumed | [Technical issues (login scanning, internet connectivity, projector setup, and glitches) frustrated students and created a significant barrier to playlist implementation](../claims/technical-issues-barrier-playlist-implementation.md) [-M]; [Digital game loading time caused issues but students had no significant navigation problems once the game loaded.](../claims/hero-elementary-game-loading-time-navigation-issues.md) [~W] |
| The interface wraps an AI tutor, chatbot or AI feedback tool | Test the operation of the AI separately from the quality of what it says: whether it accepts the learner's input (text recognition, uploads), how long a response takes and what the learner does while waiting, and whether learners can read the vocabulary of its generated messages; do not expect better content or a friendlier support layer to lift a low usability rating on its own | [Students encountered usability obstacles: text-recognition errors, feedback-generation delays, and overly complex vocabulary](../claims/ai-helper-usability-obstacles.md) [~W] (one think-aloud case study); [System usability was rated low in both conditions, with no significant difference between them](../claims/low-usability-both-conditions.md) [~M] (42 seventh graders; adding an LLM emotional-support chat to a mathematics tutor left both versions rated low, D and F grades; a non-significant difference, not shown equivalent) |
| One designer, no budget, a fixed short time (one day, or one 60-minute slot) | One round only: a 30-minute heuristic walk-through of the three core tasks, then three users doing them while thinking aloud (10 minutes each); fix the worst stall | untested proposal |
| Scarce facilitator or user time (volunteers, a busy shift, a tutor who checks in briefly) | Replace sessions with five-minute "hallway" tests of one task each, and ask for one screenshot of where they got stuck | untested proposal |
| No access to real users before launch | Treat personas and heuristics as assumptions; make the first cohort's first two weeks the test round (step 10) and say so | untested; from the earlier page (UCD's evidence comes from data about real users, not designer assumptions) |
| The brief names its own routine (its own usability questionnaire, rubric, review checklist, or template) | Keep it and run it as given; add only what the evidence says matters: a task-success check beside the rating, and the spread of individual scores | [Making year-over-year change salient helped users identify which schools improved most but lowered usability and satisfaction ratings](../claims/year-over-year-salience-mixed-effects.md) [~M]; [The system receives a good average usability rating (SUS 69.7, grade B) but with wide individual variation attributed to UI consistency issues](../claims/photon-fusion-sus-good-but-variable-usability.md) [~W] |
| The brief gives its own categories, labels or course structure | Use them as the starting navigation; card sorting checks them with users rather than replacing them | untested proposal |
| The interface shows private or sensitive data (grades, analytics, reflections, health) | Learners control who sees their records; in tests use invented data, never real learners' records; ask consent before recording screens | untested proposal |
| A real audience reads the product (parents reading a school report, the public, an employer) | Test with that audience, not with staff who know the system; check they can read the key number correctly, not only that they find it | [Reporting the number of points possible for each metric led to better understanding of how the STAR score is calculated](../claims/points-possible-improves-score-understanding.md) [+M] (public report card study) |
| High stakes (an exam platform, a certification submission) | Test with practice items and a mock submission, never during a live assessment; give every user one practice run before the real one | untested proposal |
| The learning task is a whole performance (a simulation, a project tool) the brief wants kept whole | Test whole task flows end to end, not isolated screens | untested proposal |
| The brief does not ask for a test of learning | Add no learning test or survey of your own; use task success on the brief's own tasks as the check | untested; brief convention |

Seven of the nineteen rows cite a claim. Each claim is a single study, most are about a tool or a report rather than a course, and those carried to learners or settings they did not test say so; the other rows are untested proposals.

## Observation, state and explanation

What can be observed is a user's attempt at a named task on a named device: completed or not, unaided or with help, the path taken, the errors, the time, and what they said while doing it. "Finds the interface confusing", "is overloaded" and "lacks digital skills" are inferred states. A usability rating is a self-report after the fact; it is not the attempt.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Learner does not submit an assignment | Cannot find the submit control; does not know the work is due; chose not to do the work; login or upload failed | Ask them to show you how they would submit a test file on their own device, and check the server log for a failed upload. |
| High average usability rating, but some learners keep failing a task | The mean hides a group with a different device, need or experience; the raters were the users who succeeded | Compare individual ratings and task success by device and by first-time vs returning user; compare the number who answered with the number who used it; ask the low scorers, and some who did not answer, to do the task while you watch. |
| Learners complete the task but misread the result (a score, a dashboard) | The display is usable but not understandable; the learner lacks the concept the display assumes | Ask them to say what the number means; give the same information in a second form (points possible, a short note) and see if the reading changes. |
| Rated usability falls after a change that was meant to help | The change added something users dislike but that helps the task; the change made the screen harder | Measure task success on the content before and after the change, not only the rating. |
| Learners stop using the tool after the first week, or never log in | Technical friction (login, loading, no device or connection at home); the content is not worth the effort; novelty gone; circumstances outside the course | Check logs for failed logins and load times; interview two who stopped and two who stayed, and ask those who never logged in what stopped them. |

These rows are proposals, untested as diagnostics. Keep the explanations that remain open rather than choosing the one whose name fits.

## Evidence and qualifications

No claim in the wiki tests the user-centred process against an untested build, or an interface's usability against learning on the content. The claims below test neighbouring parts.

- [Moving the link to the STAR framework from the top of the page to beneath the STAR score improved the school report card site's usability](../claims/star-link-beneath-score-improves-usability.md) [+M]; [Reporting the number of points possible for each metric led to better understanding of how the STAR score is calculated](../claims/points-possible-improves-score-understanding.md) [+M]; [The combination of moving the STAR link and reporting points possible produced the best performance on all measures](../claims/combined-design-changes-best-performance.md) [+M]: one design-comparison study (Chandler et al., 2021) of the DC online school report card, coded `q2`, causal, rigour not established, no effect size printed. Specific placement and display changes improved usability and understanding of how a score is calculated. It supports steps 5 and 6. The users are report-card readers, not learners in a course, and the claim pages do not describe the sample.
- [Making year-over-year change salient helped users identify which schools improved most but lowered usability and satisfaction ratings](../claims/year-over-year-salience-mixed-effects.md) [~M]: same study. **It limits the model**: a feature that helped users do a task was rated lower. Usability ratings and task success can move in opposite directions, so a design should not be judged on ratings alone.
- [Participants who accessed the report card site with mobile devices had more difficulty using it](../claims/mobile-access-increases-report-card-difficulty.md) [~M]: same study. Device is a condition on the relationship; test on phones.
- [Higher extraneous cognitive load predicted lower post-test scores after controlling for prior knowledge](../claims/extraneous-load-predicts-lower-post-test.md) [+M]: a classroom study of adolescents using a generative AI tutor in mathematics; in a regression adjusting for teacher-reported prior knowledge, self-reported extraneous load was the only significant predictor of the post-test (`associational`, `q2`, unstandardised coefficient only). It is consistent with the mechanism this page assumes, but the load was not traced to the interface and nothing was manipulated.
- [Technical issues (login scanning, internet connectivity, projector setup, and glitches) frustrated students and created a significant barrier to playlist implementation](../claims/technical-issues-barrier-playlist-implementation.md) [-M]: observation and interviews at four after-school sites; educators reported that login, device logistics and glitches impeded implementation and engagement. It qualifies the model: infrastructure failures can stop learners before interface design matters.
- [Digital game loading time caused issues but students had no significant navigation problems once the game loaded.](../claims/hero-elementary-game-loading-time-navigation-issues.md) [~W]: teachers' reports from the in-school arm of the same programme's evaluation (WestEd), no effect size. The barrier was loading, not navigation, which is the same point from the other side: check the plumbing before redesigning screens (step 7).
- [Students encountered usability obstacles: text-recognition errors, feedback-generation delays, and overly complex vocabulary](../claims/ai-helper-usability-obstacles.md) [~W]: one think-aloud and observation case study of a classroom AI feedback tool (`qualitative`, `q1`). The obstacles were input not being accepted, waits of minutes, and generated wording students could not read. It names what to test on an AI interface (situation table) and supports plain vocabulary for low-literacy readers.
- [System usability was rated low in both conditions, with no significant difference between them](../claims/low-usability-both-conditions.md) [~M]: 42 seventh graders used two versions of an algebra tutor, one adding an LLM chat that gave emotional support and mindful feedback; mean SUS 55.6 against 44.0, d = −0.48 printed, not significant (`causal`, `q3`). Both versions were rated poorly. It qualifies the model from the content side: changing what a tool says or how warmly it says it did not, here, make it rated usable, so the interface needs its own test. A non-significant difference in 42 students does not show the versions equal.
- [Students rated AISSA's usability as excellent, with an average SUS score of 83.38 from 30 of 46 pilot students](../claims/aissa-sus-usability-83.md) [~W]: a single-group rating of an AI slide-feedback tool in one university pilot, no comparison and no learning outcome; the claim page notes no DOI-registered source. Used for what its numbers show about reporting: 16 of 46 users did not answer, so the mean speaks for those who did (step 8).
- [Adults rated the LLM-powered iCub storytelling system as usable, with a total SUS score of 76.70 indicating good product usability](../claims/icub-storytelling-sus-76-good-usability.md) [~W]: 25 adults rated a storytelling robot after using it (`design`, `q3` as coded on the claim page); in the same study most judged it suited to children under 10. The raters were not the intended users, which is the limit the child row warns about.
- [The system receives a good average usability rating (SUS 69.7, grade B) but with wide individual variation attributed to UI consistency issues](../claims/photon-fusion-sus-good-but-variable-usability.md) [~W]: 10 participants after one hour in a VR lab; individual scores ranged from 50.0 to 92.5. A mean can hide users the interface fails.
- [After design adjustments, the LAD achieved good–excellent usability (SUS M = 4.13, equal to 78.25%)](../claims/thermos-lad-sus-good-excellent-usability.md) [+W]: 42 students rated a learning analytics dashboard after a round of adjustments. It shows the adjust-and-retest step in use; there is no rating of the version before adjustment on this claim page, so it does not show the adjustments raised usability.
- [Training and technical assistance is most engaging when it is grounded in clear expectations, designed around recipient needs, developed with ongoing recipient input, accessible, delivered by equipped providers, and framed as a partnership](../claims/ta-engagement-six-elements-interviews.md) [+W]: interviews with 12 people experienced in designing, providing and receiving training and technical assistance; no outcome was measured. It supports keeping users' input going through development, carried here from training design to interfaces.

Learners, products and outcomes differ across these claims (report-card readers, adolescents with an AI tutor, after-school and elementary children, VR lab participants, students rating a dashboard or an AI tool, adults rating a robot), so do not rank them. None follows learners from a user-tested interface to a learning outcome.

## The evidence by question

- *Does avoidable processing that the presentation imposes lower learning?* [Cognitive Overload Degrades Learning](../claims/cognitive-overload-degrades-learning.md) [+S]: the general claim, whose table gathers the studies behind it (8 distinct studies as the table counts them, mostly multimedia presentation design, one association study of extraneous load with a post-test). None of them manipulates the interface around the content, so for this page it supports the mechanism, carried from content presentation to controls and screens.
  - [Self-reported extraneous cognitive load correlates negatively with germane load and with expected probability of success in an algebra task](../claims/extraneous-cognitive-load-correlates-negatively-with-germane-load-and-probability-of-success.md) [+W]: one algebra study (Gupta & Zheng, 2020), correlations of r = −.26 with germane load and r = −.19 with a success measure. Small associations of self-reported load, not traced to any interface; consistent with the mechanism, not a test of it.
- *Does testing and revising an interface with users improve learning, compared with not doing so?* No claim in the wiki. The nearest are the report-card design comparison (usability and understanding of a score, not learning) and single-group usability ratings collected after a tool was built.

## Further evidence, not yet read against this model

Read against the model on 2026-10-19; these three are relevant but do not change it. Each says what it is and why it stays here.

- [91% of UAT participants rated the Taklif.AI user interface as intuitive](../claims/uat-91-percent-rate-interface-intuitive.md) [+W]: one user acceptance test of 68 participants in sessions of about 12 minutes; 62 of 68 scored the interface item 4 or above. No comparison and no learning outcome; a share above a cut-off reports neither the spread nor who failed a task, so it adds nothing step 8 does not already ask for.
- [The Bloom classification UI shows low perceived workload and high usability in a 50-participant user study](../claims/bloom-ui-low-workload-high-usability.md) [+W]: 50 online participants rating a question-classification tool for course authors after 10 minutes; low self-reported workload and a mean SUS of 78.2 (SD 14.07). Users are course authors, not learners, and there is no comparison, so it does not bear on the learner-facing relationship.
- [The authors argue partnership in course design is a promising avenue for LIS educators to begin decolonizing classroom hierarchies](../claims/partnership-decolonizing-classroom-hierarchies.md) [+W]: the authors' concluding argument, with no data in the article, about students as partners in designing a course's curriculum. It shares the stance of designing with users (step 2) but concerns curriculum, not the interface, and tests nothing.

## Objective and learner-valued goal

The designer's objective here is that users can do the core tasks unaided, on their own devices, so that their effort goes to the content. Elicit separately what the learner wants from the interface: to see quickly what is due, to know how they are doing, to finish on a phone on the bus, not to be seen struggling. These can diverge from the designer's objective: a learner may value a display they find pleasant over one that helps them interpret their progress correctly, as the report-card study's salience result suggests for readers in general. Record both, and when they diverge, keep the version that serves the task and explain it, or offer both views.

For example, a teacher-designer's objective for a course page is that every learner submits weekly work on time; a working adult learner's goal is to see in under a minute, on a phone, what is due and how long it will take. A page that passes a laptop usability test meets the first and fails the second. Test on the phone, with the due-date view first.

## What would revise this model?

The expectation should weaken if comparisons of a user-tested interface with an untested one, used by comparable learners on the same content, show no difference in task success or in learning on aligned measures, or if gains in rated usability are not followed by gains in task success. If the learners' failures in practice come mostly from infrastructure (logins, connections, devices) rather than interface design, the model should put plumbing first and design second, as step 7 begins to. If usability work helps novices to the interface and not experienced users, say so and limit the default to novices. Do not protect the model by calling every failure "not enough user testing" after the fact.

Rated usability, task success, understanding of what a screen shows, and learning on the content are separate claims. The present evidence establishes no number of users per round, no number of rounds and no usability threshold below which learning suffers.

## Related Principles
- [Scaffolding and Fading](scaffolding-and-fading.md) — both concern how much support structure a learner needs and when it should be reduced, though scaffolding targets content mastery while UCD targets interface usability
- [Cone of Experience (Concrete-to-Abstract Media Selection)](../theories/cone-of-experience.md) — both concern deliberate media/interface choice, though UCD addresses usability rather than concreteness/abstraction
- [Cognitive Load Management](cognitive-load-management.md) — removing avoidable processing from the presentation of content; this page applies the same lever to the interface around it
- [Digital Learning](digital-learning.md) — whether a digital tool earns its place; this page takes the tool as chosen and makes it operable
- [Universal Design for Learning](universal-design-for-learning.md) — planning alternatives for demands that are not part of the goal, including access routes

## Examples

- Building a persona from user interviews before designing a course's navigation structure
- Paper prototyping a course's menu structure and running an open card sort to check it against learners' own mental categories
- A heuristic evaluation of an LMS course page against Nielsen's 10 usability heuristics before launch
- [Use a design thinking process with Empathize, Define, Ideate, Prototype, and Test stages to reimagine school safety](../strategies/design-thinking-reimagining-school-safety.md)
- [Learner Experience Design (LXD)](../processes/learner-experience-design.md) — the user-centred course design process this principle supports
- [Distinguish learner research from user research and choose success metrics tied to educational outcomes rather than engagement](../strategies/distinguish-learner-research-from-user-research.md)
- [Begin inclusive design work with teacher self-reflection on intersecting identities](../designs/identity-reflection-before-empathy-interviews.md)
- [Extend empathy interviews to students' caregivers for an additional perspective](../strategies/caregiver-empathy-interview-extension.md)
- [Observe the classroom for dissonance between what students say and what teachers see](../strategies/classroom-observation-dissonance-inclusive-design.md)
- [Close the empathy exercise by reflecting on surprises, systemic oppression, and short- and long-term design goals](../strategies/empathy-exercise-reflection-and-forward-planning.md)
- [Conduct empathy interviews as story-based conversations in comfortable, student-chosen settings](../strategies/empathy-interview-conduct-practices.md)
- [Five-step empathy interview exercise for teachers designing inclusive computing pathways](../strategies/empathy-interview-five-step-exercise.md)
- [Inclusive Innovation Process](../strategies/inclusive_innovation_process.md)
- [Empathy Interview Protocol for inclusive computing pathways](../elements/empathy-interview-protocol-ct-pathways.md)
- [Conduct empathy interviews to understand user experiences with technology](../strategies/empathy-interviews-for-ai-policy-development.md)

## Key Sources
- Earnshaw, Y., Tawfik, A. A., & Schmidt, M. (2018). User experience design. In R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/user_experience_design](https://edtechbooks.org/lidtfoundations/user_experience_design)
- Nielsen, J. (1994). Heuristic evaluation. In J. Nielsen & R. L. Mack (Eds.), *Usability inspection methods* (pp. 25–62). Wiley.
- International Organization for Standardization. (2010). *Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems* (ISO 9241).
- Coenraad, M., Hodge, M., Ruiz, P., Mills, K., & Burke, Q. (2021). Empathy Interviews for Developing Inclusive Computing Pathways. Washington, D.C.: Center for Inclusive Innovation, Digital Promise. https://dschool.stanford.edu/resources/liberatory-design-cards

<!-- deprecated 2026-10-15: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Learning technologies fail not only when the pedagogy is wrong, but when the interface itself creates barriers — a learner who cannot find an assignment or navigate a confusing menu is paying a cognitive cost that has nothing to do with the content being taught (Earnshaw, Tawfik, & Schmidt, 2018). **Usability** describes how easily an interface can be used as intended; **user experience (UX)** is the broader "person's perceptions and responses that result from the use... of a product, system, or service" (ISO, 2010). **User-centered design (UCD)** is the practice of centering users' needs and mental models throughout the design process rather than treating the interface as an afterthought to the pedagogy.

The connection to instructional design runs directly through [Cognitive Load Theory](../theories/cognitive-load-theory.md): a poorly designed interface — confusing navigation, unfamiliar terminology, inconsistent layout — increases **extraneous cognitive load**, which competes with the working-memory resources a learner needs for germane, schema-building processing. Distributed cognition and activity theory extend the picture to collaborative and tool-mediated settings, treating knowledge as distributed across people and artifacts rather than held only in an individual mind.

UCD proceeds iteratively: identifying user needs (often via **personas** — detailed fictional users built from real interview/observation data), gathering requirements, and building prototypes of increasing fidelity — from **paper prototypes** (fast, cheap, focused on navigation and workflow, not visuals) to **wireframes** (layout, no visual polish) to **functional prototypes** (interactive, close to final). At each stage, evaluation methods appropriate to that fidelity level are used: ethnography and focus groups early (front-end analysis), card sorting to align navigation with users' mental models, heuristic evaluation (e.g., against Nielsen's 10 usability heuristics) and cognitive walkthroughs during prototyping, and think-aloud studies, A/B testing, or eye-tracking once a functional prototype exists.

## Implications

### Context
#### Requirements
- Access to real (or representative) users for needs identification, persona-building, and evaluation — UCD's evidence base comes from data about actual users, not designer assumptions
- An iterative process budget: UCD assumes multiple rounds of prototyping and revision rather than a single build-then-ship cycle
#### Constraints
- Adds design and evaluation overhead relative to skipping usability work entirely; the investment pays off mainly when the interface is complex, novel, or used repeatedly by many learners
- Usability improvements reduce *extraneous* load but do not by themselves improve the pedagogical design of the content — the two are complementary, not substitutes

### Target Learners
- Any learner using a digital interface to access instruction, but the payoff is largest for novices unfamiliar with the interface's conventions, and for accessibility-dependent learners (e.g., users with autism, as in eye-tracking studies of facial-expression-identification interfaces)

### Target Learning Objectives
- Not a content objective — a precondition for reliably measuring content learning at all: if learners cannot navigate the interface, learning-outcome data is confounded by usability failures

### Theory
#### Supporting
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) [+M] — extraneous cognitive load from a poorly designed interface directly competes with the working-memory resources needed for germane processing
- Distributed cognition and activity theory — extend the picture from an individual user's cognitive load to knowledge distributed across people, tools, and artifacts in collaborative or workplace learning contexts

## Claims

- [Training and technical assistance is most engaging when it is grounded in clear expectations, designed around recipient needs, developed with ongoing recipient input, accessible, delivered by equipped providers, and framed as a partnership](../claims/ta-engagement-six-elements-interviews.md) [+W] — attached 2026-10-08 from Kara Conroy et al. (2021), which proposed "Six-element pattern for engaging training and technical assistance design"; tests this page's relationship.
- [After design adjustments, the LAD achieved good–excellent usability (SUS M = 4.13, equal to 78.25%)](../claims/thermos-lad-sus-good-excellent-usability.md) [+W] — attached 2026-10-08 from de Vreugd et al. (2024), which proposed "Plan an explicit usability exploration and adjustment phase before evaluating a LAD's perceived usefulness".
- [Students rated AISSA's usability as excellent, with an average SUS score of 83.38 from 30 of 46 pilot students](../claims/aissa-sus-usability-83.md) [+W]
- [The system receives a good average usability rating (SUS 69.7, grade B) but with wide individual variation attributed to UI consistency issues](../claims/photon-fusion-sus-good-but-variable-usability.md) [~W]
- [Adults rated the LLM-powered iCub storytelling system as usable, with a total SUS score of 76.70 indicating good product usability](../claims/icub-storytelling-sus-76-good-usability.md) [+W]
- [91% of UAT participants rated the Taklif.AI user interface as intuitive](../claims/uat-91-percent-rate-interface-intuitive.md) [+W]
- [Digital game loading time caused issues but students had no significant navigation problems once the game loaded.](../claims/hero-elementary-game-loading-time-navigation-issues.md) [~W]
- [Moving the link to the STAR framework from the top of the page to beneath the STAR score improved the school report card site's usability](../claims/star-link-beneath-score-improves-usability.md) [+W]
- [Making year-over-year change salient helped users identify which schools improved most but lowered usability and satisfaction ratings](../claims/year-over-year-salience-mixed-effects.md) [~W]
- [The Bloom classification UI shows low perceived workload and high usability in a 50-participant user study](../claims/bloom-ui-low-workload-high-usability.md) [+W]

## Related Principles
- [Scaffolding and Fading](scaffolding-and-fading.md) — both concern how much support structure a learner needs and when it should be reduced, though scaffolding targets content mastery while UCD targets interface usability
- [Cone of Experience (Concrete-to-Abstract Media Selection)](../theories/cone-of-experience.md) — both concern deliberate media/interface choice, though UCD addresses usability rather than concreteness/abstraction

## Examples

- Building a persona from user interviews before designing a course's navigation structure
- Paper prototyping a course's menu structure and running an open card sort to check it against learners' own mental categories
- A heuristic evaluation of an LMS course page against Nielsen's 10 usability heuristics before launch
- [Use a design thinking process with Empathize, Define, Ideate, Prototype, and Test stages to reimagine school safety](../strategies/design-thinking-reimagining-school-safety.md)

## Key Sources
- Earnshaw, Y., Tawfik, A. A., & Schmidt, M. (2018). User experience design. In R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/user_experience_design](https://edtechbooks.org/lidtfoundations/user_experience_design)
- Nielsen, J. (1994). Heuristic evaluation. In J. Nielsen & R. L. Mack (Eds.), *Usability inspection methods* (pp. 25–62). Wiley.
- International Organization for Standardization. (2010). *Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems* (ISO 9241).
-->

<!-- merged 2026-10-15 from principles/design-with-students-empathy-interviews ("Design with students rather than for them by interviewing the actual users of the curriculum"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Design with students rather than for them by interviewing the actual users of the curriculum

> **Principle** · [All principles](index.md)
> **Evidence** · 3 claims (3 for) · 3 studies (2 qualitative, 1 design), `q1`–`q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
The article argues that designers "tend to unconsciously default to imagined users whose experiences are similar to their own", producing what Costanza-Chock calls "a spiral of exclusion". Empathy interviews counter this by having teachers hear the stories of the students who will actually use what they design. The guide invokes the disability rights mantra "Nothing about us without us" as the rationale for designing with rather than designing for marginalized learners.

## Design Implications

### Context
#### Requirements
- Teachers must select students whose experiences differ from their own and from the dominant society, and must attend to power dynamics so the selected student does not feel othered.
#### Constraints
- 

### Target Learners
- K-12 students in computing courses, particularly those from marginalized or non-dominant backgrounds

### Target Learning Objectives
- Inclusive computing curriculum design responsive to students' identities and experiences

### Claims

- [Empathy interviews became a widely adopted data-gathering technique for understanding stakeholder perspectives on problems](../claims/empathy-interviews-adopted-by-improvement-teams.md) [+W]
- [Empathy interviews are among the most commonly discussed continuous improvement practices for advancing equity](../claims/empathy-interviews-central-equity-practice.md) [+W]
- [The authors argue partnership in course design is a promising avenue for LIS educators to begin decolonizing classroom hierarchies](../claims/partnership-decolonizing-classroom-hierarchies.md) [+W]

## Related Principles
- 

## Examples

- [Begin inclusive design work with teacher self-reflection on intersecting identities](../designs/identity-reflection-before-empathy-interviews.md)
- [Extend empathy interviews to students' caregivers for an additional perspective](../strategies/caregiver-empathy-interview-extension.md)
- [Observe the classroom for dissonance between what students say and what teachers see](../strategies/classroom-observation-dissonance-inclusive-design.md)
- [Close the empathy exercise by reflecting on surprises, systemic oppression, and short- and long-term design goals](../strategies/empathy-exercise-reflection-and-forward-planning.md)
- [Conduct empathy interviews as story-based conversations in comfortable, student-chosen settings](../strategies/empathy-interview-conduct-practices.md)
- [Five-step empathy interview exercise for teachers designing inclusive computing pathways](../strategies/empathy-interview-five-step-exercise.md)
- [Inclusive Innovation Process](../strategies/inclusive_innovation_process.md)
- [Empathy Interview Protocol for inclusive computing pathways](../elements/empathy-interview-protocol-ct-pathways.md)
- [Conduct empathy interviews to understand user experiences with technology](../strategies/empathy-interviews-for-ai-policy-development.md)

## Key Sources
- Coenraad, M., Hodge, M., Ruiz, P., Mills, K., & Burke, Q. (2021). Empathy Interviews for Developing Inclusive Computing Pathways. Washington, D.C.: Center for Inclusive Innovation, Digital Promise. https://dschool.stanford.edu/resources/liberatory-design-cards
-->
