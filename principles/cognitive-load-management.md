---
type: principle
id: cognitive-load-management
aliases: [design-principles-depend-on-prior-knowledge, determine-element-interactivity-before-designing-instruction, low-task-complexity-child-learners-recasts, measured-pace-one-concept-at-a-time-older-learners, reduce-extraneous-optimize-intrinsic-increase-germane, cognitive-load-reduction]
title: Cognitive Load Management
description: "Across a sequence, matching how presentation, task order and support distribute processing demand to a learner's current task-specific capacity is expected to improve learning, while keeping effortful processing that the intended outcome and horizon need; in the wiki, single levers and two whole load-reducing designs are tested, the withdraw-and-restore policy is not."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
sources:
  - id: sweller-1998
    resource: "https://doi.org/10.1023/A:1022193728205"
    title: "Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296"
    author: "Sweller, J., van Merriënboer, J. J. G., & Paas, F"
  - id: clinton-2017
    resource: "https://eric.ed.gov/?id=ED574984"
    title: "Clinton, V., Cooper, J.L., Michaelis, J., Alibali, M.W., & Nathan, M.J. (2017). How Revisions to Mathematical Visuals Affect Cognition: Evidence from Eye Tracking. In Eye-tracking technology applications in educational research (pp. 195-218). IGI Global. https://eric.ed.gov/?id=ED574984"
    author: "Clinton, V., Cooper, J.L., Michaelis, J., Alibali, M.W., & Nathan, M.J"
  - id: kala-2023
    resource: "https://doi.org/10.36681/tused.2023.027"
    title: "Kala, N., & Ayas, A. (2023). Effect of instructional design based on cognitive load theory on students' performances and the indicators of element interactivity. Journal of Turkish Science Education, 20(3), 468-489. https://doi.org/10.36681/tused.2023.027"
    author: "Kala, N., & Ayas, A"
  - id: lihui-lv-chunyan-liu-2022
    resource: "https://doi.org/10.5539/elt.v15n9p95"
    title: "Lihui Lv & Chunyan Liu. (2022). Recast, Task Complexity and Child Learners' L2 Development. English Language Teaching, 15(9). https://doi.org/10.5539/elt.v15n9p95"
    author: "Lihui Lv & Chunyan Liu"
  - id: weintraub-2025
    resource: "http://doi.org/10.35847/LWeintraub.7.1.37"
    title: "Weintraub, L. (2025). Grandma Needs English, Too. Adult Literacy Education. http://doi.org/10.35847/LWeintraub.7.1.37"
    author: Weintraub, L
  - id: houichi-2020
    resource: "https://dx.doi.org/10.24093/awej/vol11no4.8"
    title: "Houichi, A., & Sarnou, D. (2020). Cognitive Load Theory and its Relation to Instructional Design: Perspectives of Some Algerian University Teachers of English. Arab World English Journal. https://dx.doi.org/10.24093/awej/vol11no4.8"
    author: "Houichi, A., & Sarnou, D"
---

# Cognitive Load Management

> **Principle** · [All principles](index.md)
> **Evidence** · 79 claims (32 for, 44 mixed, 3 against) · 66 studies (29 causal, 15 review, 10 quant-synthesis, 9 theoretical, 2 associational, 1 design), `q1`–`q4` · 24 of 66 report an effect size · 70 claims rest on one study

## Conditional relationship

For a learner whose current capacity on **the particular task** is limited (a `novice` on that task, whatever their standing in the wider domain), material whose interacting elements must be processed together (`complex-skill`, `principle` or multi-step `procedure` goals) is expected to be learned better when the design distributes processing demand over the sequence instead of presenting it all at once: avoidable processing removed from the presentation, component knowledge introduced before the whole (pretraining, segmenting, isolated parts first), and support withdrawn or effort reintroduced as the learner's task-specific capacity grows. Compared with an unmanaged version of the same material, this is expected to change performance, transfer or efficiency; which of them changes, and whether the change holds at a delayed horizon, differs between the claims below and must be stated for each design.

The relationship has two edges. Too much simultaneous demand for this learner is expected to impede learning; but **less effort is not the objective**. Conditions that slow performance during learning (retrieval, spacing, interleaving, problem-solving before instruction) can improve `delayed-retention`, `conceptual-understanding` or transfer, and support that helps at the start can become redundant later. Deferring intrinsic demand is a default for tasks learners cannot yet coordinate, not a rule for every task: for a procedural skill that could be attempted whole, one experiment found full complexity from the start beat a gradual ramp at two days (see *Evidence and qualifications*), so a ramp should be checked against a delayed probe rather than assumed. Managing load therefore means deciding, for a stated outcome and horizon, which demand to remove, which to defer and which to keep.

[Cognitive Load Theory](cognitive-load-theory.md), the converted sibling principle, holds the narrower model that sits inside this one: for task-specific novices on high-element-interactivity material, removing avoidable processing (integrated sources, segmented transient media, isolated elements, full examples) improves immediate performance or efficiency, a relationship that weakens with expertise. This page adds the sequence-level decisions around that lever: when to defer intrinsic demand, when to restore effortful processing, and how to tell which a response calls for. Working-memory limits and schema construction are the explanatory hypotheses of the [theory](../theories/cognitive-load-theory.md) and of the [expertise reversal effect](../theories/expertise-reversal-effect.md); they are not observations. The [4C/ID pattern](../patterns/4cid-four-component-instructional-design.md) is a reusable whole-task policy that applies both; its response-dependent branches remain proposals.

Two studies in the wiki test a whole load-reducing design rather than one lever, and they disagree on what it buys. In one small randomized study (37 first-year students, thermodynamics, eight sessions), a design built on cognitive load theory scored far higher than lecturer-designed instruction on the session retention and transfer tests, but not significantly higher on the achievement post-test or lower on the load scale ([CLT design raised retention and transfer](../claims/clt-instructional-design-raises-retention-transfer-thermodynamics.md) [+M]; [no difference on the post-test or load scale](../claims/no-group-difference-tat-posttest-cls.md) [~M]). Revising a middle-school mathematics lesson's visuals by signaling, contiguity and coherence changed no post-lesson test score, while eye-tracking indices of processing fell for low-prior-knowledge students and rose for middle-prior-knowledge ones ([revised visuals had no learning effect](../claims/revised-visuals-no-learning-effect.md) [~M]). Neither withdraws support or restores effort over the sequence, so the relationship as a whole stays untested here; the first supports its removal half, the second warns that removal can change processing without changing learning.

## Fitting the design to a situation

Ask for four facts when the brief omits them: **how much do these learners know about this particular task?**, **how many elements must be handled together?**, **is the outcome immediate performance, transfer or retention at a delay?**, and **the learners' age and language of instruction**. Ask also whether learners will work alone or in groups, and what tools (an AI chatbot, a search engine) they will use.

| If the brief says… | Then change… | Basis |
|---|---|---|
| A new topic with many unfamiliar parts or terms (equipment, anatomy, a system) | Start with a short primer that names the parts and what they do, then the main lesson | [A pretraining primer improved knowledge and transfer](../claims/pretraining-improves-transfer.md) [+M] |
| A complex whole task that novices cannot yet coordinate | Teach the interacting parts in isolation first, then combine them in the whole task | [Isolated parts first helped novices on complex tasks](../claims/part-task-practice-reduces-load-for-novices.md) [+M] |
| Transient media (video, narrated animation) carry the content | Segment it at conceptual breaks; allow extra time; cut background music, busy backgrounds and other interesting but unneeded material | [Segmenting and worked examples improved learning, with qualifications](../claims/cognitive-load-management.md) [+M]; [Segmenting improves multimedia learning](../claims/segmenting-improves-multimedia-learning.md) [+M]; [Weeding extraneous content improved retention and transfer from video, reported second-hand in an essay](../claims/weeding-extraneous-content-improves-video-learning.md) [+W] |
| A picture or animation has to be explained in words | Give the explanation as narration rather than as on-screen text beside the picture | [Picture or animation with voice beat picture with text, 36 adults, 15 minutes of immunology](../claims/voice-media-outperform-picture-text-overall.md) [+W] |
| Novices learning a structured problem type (mathematics, science procedures) | Begin with worked examples before unaided problems | [Worked examples improve mathematics performance](../claims/worked-examples-improve-math-performance.md) [+M] |
| Learners are progressing, or are experienced on the task | Withdraw guidance step by step and check with an unsupported changed problem before removing it entirely | [Guidance that helps novices can become redundant as expertise grows](../claims/expertise-reversal-effect.md) [~M] |
| The outcome is retention at a delay (an exam weeks away) | Once the material is understood, reintroduce effort: spaced practice and retrieval quizzes, even though practice gets harder | [Effortful conditions can improve delayed retention](../claims/desirable-difficulties-enhance-learning.md) [~M] |
| The goal is conceptual understanding, with secondary or older students | Consider a problem-solving attempt before instruction, always followed by the instruction | [Problem-solving before instruction improved conceptual learning](../claims/productive-failure-improves-conceptual-learning.md) [~M] |
| Learners are in grades 2–5, or the skill is domain-general | Teach first, then practise; the problem-first advantage reversed for these groups | [Problem-solving before instruction improved conceptual learning](../claims/productive-failure-improves-conceptual-learning.md) [-M] |
| The material is word lists or vocabulary | Present items blocked by category rather than interleaved; interleaving hurt for words | [Effortful conditions can improve delayed retention](../claims/desirable-difficulties-enhance-learning.md) [~M] |
| Instruction is in the learners' second language | Give explanations in the first language or bilingually where possible | [Foreign-language AI explanations impose a double burden](../claims/double-burden-language-of-ai-instruction.md) [~W] |
| Child learners writing a target form in a second language | Keep the task simple while the form is new; written production fell as task complexity rose, though oral production of the same form did not differ | [Higher task complexity went with lower written production](../claims/task-complexity-negatively-related-child-written-production.md) [-W]; [Task complexity showed no effect on oral production](../claims/task-complexity-no-effect-child-oral-production.md) [~W] |
| A unit mixes topics of low and high element interactivity (a science unit) | Classify the topics for these learners (expert judgement first, then rated effort and study time from the first sessions) and give the high-interactivity ones the most sequencing and support | [Mental effort and study time rose with element interactivity](../claims/mental-effort-study-time-indicate-element-interactivity.md) [+M]; [Retention and transfer scores fell as interactivity rose](../claims/retention-transfer-scores-decrease-with-element-interactivity.md) [+W]; [CLT design produced higher effective learning scores at retention and transfer](../claims/clt-design-effective-learning-retention-transfer.md) [+M]; counting elements is not enough, since problems with the same number of moves can differ sharply in difficulty ([difficulty is not set by element interactivity alone](../claims/difficulty-beyond-element-interactivity.md) [~W]) |
| Revising existing materials (adding signals, moving labels next to what they label, cutting decorative visuals) for a class whose prior knowledge varies | Check the revision on a learning outcome and separately for each prior-knowledge level; do not expect test gains from the revision alone | [Revised visuals had no learning effect](../claims/revised-visuals-no-learning-effect.md) [~M]; [Revised visuals changed processing of text in opposite directions by prior knowledge](../claims/revised-visuals-processing-text-prior-knowledge-interaction.md) [~M]; [and of the mathematics visuals](../claims/revised-visuals-processing-math-visuals-interaction.md) [~M] |
| Learners are older adults (55+) | Slow the pace, introduce one new concept per activity with extra review and wait time, and avoid fast, competitive drills; do not lower expectations of what they can learn | [Fast drills disadvantage older learners](../claims/rote-drills-disadvantage-older-learners.md) [~W]; [Learning ability does not decline with age in healthy adults](../claims/learning-ability-does-not-decline-with-age.md) [+W]; [One digest's account that older adults can learn a language](../claims/no-evidence-older-adults-cannot-learn-language.md) [~W]; [An older-beginner class taught this way made gains, with no comparison group](../claims/older-beginner-esl-outcome-gains.md) [+W]; set task difficulty per learner rather than one level for all: in laboratory working-memory tasks (not learning tasks), age-group differences in accuracy were much smaller in studies that titrated difficulty to each person ([titration reduced age differences](../claims/titration-reduces-age-differences-storage-dual-task.md) [+W]; [titration, not domain overlap, accounted for it](../claims/titration-dominates-domain-overlap-combined-metaregression.md) [~W]) |
| Learners will work in groups on the task | Use groups for high-complexity tasks and individual work for simple ones; structure the communication and division of work, and prefer groups that have worked together before when the information to share is dense | [Group learning was more efficient for high-complexity tasks and individual for low, as one review reports an earlier experiment](../claims/collective-working-memory-effect-complexity-dependent.md) [+W]; [Collaboration spreads load across working memories for high-load tasks, reported second-hand](../claims/collaborative-learning-collective-working-memory-advantage.md) [+W]; [Communication and coordination costs can cancel that benefit (theoretical)](../claims/transactive-costs-annul-load-sharing-benefit.md) [+W]; [Experienced groups were more efficient only at high information density](../claims/zambrano-2019-efficiency-advantage-only-high-density.md) [~W]; [Low information density lowered effort and raised efficiency during the group learning phase](../claims/zambrano-2019-low-density-lower-effort-learning.md) [+W] |
| Learners research a question with a generative AI chatbot rather than a search engine | Keep the effortful part of the inquiry: ask for justification from several sources, or have learners search and weigh sources themselves, and judge the work on its reasoning, not its ease | [Web search produced better justifications than an AI chatbot, 91 students](../claims/web-search-higher-quality-justifications-than-llm.md) [+M]; [In an exploratory analysis, lower germane load in the chatbot group accounted for that difference](../claims/germane-load-mediates-tool-effect-on-justification-quality.md) [+W] |
| A rule-governed skill learners can attempt whole from the start (verb conjugation), tested days later | Do not assume a gradual ramp of complexity is better; try full complexity from the start with a delayed check, keeping simpler steps for learners who stall | [Constantly high complexity beat a gradual increase on posttest time and trials two days later, 132 participants](../claims/constantly-high-complexity-improves-posttest-performance.md) [~M] |
| The plan is to make material harder to perceive (a hard-to-read font) so learners work harder | Do not; reintroduce effort through retrieval, spacing or an announced test instead | [Disfluency had no effect while expecting a test improved retention and transfer](../claims/disfluency-no-effect-test-expectancy.md) [~W]; [Disfluency helped only learners with high working memory capacity](../claims/disfluency-benefits-high-working-memory-only.md) [~W]; [Neither disfluency nor prompted imagination improved performance in two small experiments](../claims/gcl-activation-no-task-performance-effect.md) [-W] |

## Observation, state and explanation

Record a response **under stated conditions**: the task and its representation, how many elements must be handled together as judged for this learner, the supports present (integrated labels, segments, a primer, worked steps, hints, aids), the pacing, the time taken and the response mode. "Overloaded", "under-challenged" and "novice" are inferred states. Accuracy, time, a rated mental effort, errors and confidence are observations; none measures working-memory load or a schema directly. A synthesis below found that integrated designs improved learning without reliably changing load ratings, so a rating and a learning outcome can move apart, and a low rating can also mean disengagement or an easy-looking task. The same split appears in eye-tracking: revised mathematics visuals shortened fixations on the text for low-prior-knowledge students and lengthened them for middle-prior-knowledge ones, with no difference in test scores or in time spent on the lesson ([on the text](../claims/revised-visuals-cognitive-load-text-prior-knowledge-interaction.md) [~M]; [on the mathematics visuals](../claims/revised-visuals-cognitive-load-math-visuals-interaction.md) [~M]; [no difference in lesson time](../claims/revisions-no-effect-time-with-lesson.md) [~M]). In the other direction, rated mental effort and study time across eight sessions ranked topics almost exactly as experts had classified their element interactivity, so the two together are a usable observation of how demanding a topic is for a group ([Mental effort and study time indicate element interactivity](../claims/mental-effort-study-time-indicate-element-interactivity.md) [+M]).

A rating also depends on when it is taken and what produced it. Example–problem pairs lowered rated effort during learning but raised it on the near-transfer test, against problem–example pairs ([effort reversed between phases](../claims/effort-reversal-learning-versus-transfer-phase.md) [~W]). Presenting principles before a case comparison raised rated germane load and lowered rated extraneous load by large amounts, yet timing made no difference to the knowledge test ([ratings moved](../claims/input-before-raises-germane-lowers-extraneous-load.md) [~W]; [knowledge did not](../claims/input-timing-no-effect-knowledge-case-comparison.md) [~W]). Expert example standards raised rated effort and difficulty while making learners' judgements of their own examples more accurate ([standards raised effort and difficulty](../claims/expert-standards-increase-difficulty-effort.md) [~W]; [in a second experiment too](../claims/standards-increase-cognitive-load-evaluation.md) [~W]). A review argues that effort ratings blend task demand with feelings and motivational beliefs, and that high effort can mean either more productive activity or less prior knowledge, so a high rating is not by itself a sign of good or bad design ([effort self-reports are not a valid measure of a task's cognitive demand](../claims/effort-self-reports-not-valid-cognitive-requirements.md) [~W]; [high effort is not necessarily better learning](../claims/high-effort-not-indicative-better-learning.md) [~W]). Read an effort rating beside a learning outcome at the horizon that matters, never alone.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Stalls at the start of a new topic, misusing its terms and asking what parts are called | Component vocabulary missing, so names and relations are being learned at once; a representation the learner cannot read; a language barrier unrelated to the topic | Give a short primer naming the parts, then the same task; separately present the representation with a familiar example. Record which change restores progress and every support given. |
| Fluent, error-free practice with heavy support, then poor on a delayed or changed task | Support removed the processing the outcome needed; performance during learning mistaken for learning; forgetting over the delay | Compare an immediate and a delayed probe on the same items, and a changed item; then give a retrieval or problem-first episode with feedback and see whether the delayed result changes. |
| Rates effort high and progresses slowly, yet improves across sessions | Genuinely high intrinsic demand for this learner, which is not by itself a problem; extraneous demand from the presentation; unfamiliar language | Remove one avoidable demand (split sources, redundant text) while holding the task constant; if effort falls and progress rises, the demand was avoidable. If not, keep the task and sequence it. |
| Skips segments, examples or explanations and does as well without them | Rising task-specific expertise making the support redundant; impatience with a correct need for it; the outcome measure too easy to show the difference | Give an unsupported changed problem; if independent success holds, withdraw support provisionally and re-check later. If it fails, the support may still be needed in a shorter form. |
| Rates the task harder after a support (a drawing aid, a checklist, a prompt) is added | The support itself adds processing; it exposes difficulty the learner had not noticed; the rating reflects frustration rather than demand | Compare learning with and without the support on the same outcome, not only the rating; a drawing study found both kinds of support raised rated difficulty against none ([drawing support raised perceived difficulty](../claims/drawing-support-increased-perceived-difficulty.md) [-W]). If learning does not improve, drop or simplify the support. |
| Struggles on a problem attempted before instruction, then learns well from the instruction | Productive generation preparing the instruction; learning from the instruction alone; exposure from the attempt as a pretest | Compare conceptual and procedural items separately and note the learner's age and the skill's generality; record the attempts the learner produced. |

These rows are proposals, untested with learners. A probe can shift confidence among explanations; a single contrast does not identify a cause, and each probe is itself a learning exposure that changes the state.

## Evidence and qualifications

- [Managing load through segmenting and worked examples improved learning, with qualifications](../claims/cognitive-load-management.md) [+M]: two meta-analyses. Segmented multimedia (56 investigations, 88 comparisons) had small to medium effects on retention and transfer against continuous presentation, lowered overall rated load and lengthened learning time; learners with high prior knowledge gained **more** on retention than those with little, against what the expertise reversal effect predicts. Worked examples in mathematics (55 studies, elementary to postsecondary) gave g = 0.48, and adding self-explanation prompts produced a negative effect against examples without them, so an added effort-inducing activity did not help there. Horizons are not separated on the claim page. Not yet checked against its sources.
- [Reducing split attention improves learning, though load measures do not show why](../claims/cognitive-load-reduction-improves-learning.md) [+M]: integrated rather than separated text and diagrams, g = 0.63 over 58 comparisons (2,426 participants), holding across many moderators; a second meta-analysis of 50 studies reports the benefit for novices largest with complex materials. A systematic review of 41 comparisons found integrated designs did not reliably change any cognitive-load measure, so the benefit stands while its explanation by reduced load is not established. Not settled: the abstracts available could not confirm the entries.
- [A pretraining primer before a complex lesson improved transfer](../claims/pretraining-improves-transfer.md) [+M]: one randomized experiment, n=93; a video naming a micropipette's parts before an immersive VR procedure lesson, against the same lesson with no primer. The primed group scored higher on a knowledge test, made fewer errors on a real-life transfer task and reported lower load; errors inside VR did not differ. No standardized effect size, delayed horizon or prior-knowledge moderation is reported. It supports deferring component knowledge out of a complex task, not a primer for learners who already know the parts. Not yet checked against its sources.
- [Guidance that helps novices can become redundant or counterproductive as expertise grows](../claims/expertise-reversal-effect.md) [~M]: a synthesis of cognitive load studies, read from its abstract, reporting that integrated explanations, worked examples and step-by-step guidance help novices and can depress performance relative to leaner conditions as prior knowledge increases. No effect sizes, threshold or horizon are recorded. It argues for changing support over time; it does not say when, and the segmenting result above runs the other way on retention. Not settled against its sources.
- [Effortful conditions can slow learning-phase performance while improving delayed retention](../claims/desirable-difficulties-enhance-learning.md) [~M]: three meta-analyses of classroom quizzing (222 studies, g = 0.499 against restudy and other strategies), spaced against massed retrieval (29 studies, g = 0.74) and interleaving for category learning (59 studies, g = 0.42, but blocking beat interleaving for words, g = -0.39). It limits this principle: minimizing effort is not the goal when the outcome is delayed retention. The claim page itself says the difficulty must be surmountable, and none of these studies manipulated presentation load, so it does not say how the two interact. Partly checked: 1 of 2 entries pass, the rest could not be confirmed.
- [A CLT-based design raised retention and transfer in thermodynamics](../claims/clt-instructional-design-raises-retention-transfer-thermodynamics.md) [+M]: one randomized study, 37 first-year students (18 and 19), eight sessions, against lecturer-designed instruction, with a memory-span test and the achievement pre-test as covariates. Session retention test means were 77.07 against 38.48 (ηp2 = .72) and transfer 62.96 against 29.67 (ηp2 = .71). The achievement post-test and the load scale did not differ significantly (both ηp2 = .09, p = .07 and .09), which is not equivalence ([no group difference](../claims/no-group-difference-tat-posttest-cls.md) [~M]); combining performance and effort, the design's effective learning scores were higher at retention and transfer and about equal on the post-test, because its students also reported more effort ([effective learning scores](../claims/clt-design-effective-learning-retention-transfer.md) [+M]). Session scores fell in both groups as the topics' element interactivity rose ([retention and transfer fell with interactivity](../claims/retention-transfer-scores-decrease-with-element-interactivity.md) [+W]), a descriptive pattern. Rigour is coded r1 on the main entries; the claim pages do not say what the design changed session by session, so it tests a load-reducing package, not this page's sequence of withdrawal and restored effort.
- [Revising visuals by signaling, contiguity and coherence did not change learning](../claims/revised-visuals-no-learning-effect.md) [~M]: one experiment, 62 middle-school students reading a mathematics lesson with original or revised visuals. Condition did not affect the post-lesson test (F(1, 56) = .00, p = .96) and did not interact with prior knowledge; prior knowledge itself predicted scores (d = 1.30, low against high). Eye-tracking measures of processing showed condition-by-prior-knowledge interactions, reduced for low and increased for middle prior knowledge ([text processing](../claims/revised-visuals-processing-text-prior-knowledge-interaction.md) [~M]; [mathematics visuals](../claims/revised-visuals-processing-math-visuals-interaction.md) [~M]). It qualifies the removal lever: applied together to existing material, the principles changed how learners processed it without a measured learning gain, and in opposite directions for neighbouring prior-knowledge groups.
- [Problem-solving before instruction improved conceptual learning and transfer, not procedure](../claims/productive-failure-improves-conceptual-learning.md) [~M]: a meta-analysis of 53 studies (166 comparisons), problem-solving first against the same instruction first: g = 0.36 on conceptual knowledge and transfer, g = −0.03 on procedural knowledge; the advantage **reversed** for second to fifth graders and for domain-general skills. One more randomized study pair in mathematics. It limits the load-reduction default for conceptual goals in older learners; it does not license unguided problem-solving for novices, since instruction follows in every comparison. Partly checked: 1 of 2 entries pass.
- [Constantly high task complexity improved delayed posttest performance against gradually increasing complexity](../claims/constantly-high-complexity-improves-posttest-performance.md) [~M]: one 2×2 experiment, 132 participants learning Italian verb conjugation, complexity (constant high against gradually rising) crossed with a desirable difficulty (interleaving). Two days later the constant-high groups needed less time and fewer trials (η² = 0.09); complexity did not interact with the desirable difficulty ([no interaction](../claims/complexity-difficulty-interaction-not-significant-performance.md) [~W]), and the constant-high groups reported lower intrinsic load and less metacognitive strategy use ([lower rated load and strategy use](../claims/high-complexity-lowers-icl-and-metacognitive-strategy-use.md) [~W]). It runs against this page's default of deferring intrinsic demand, for one procedural skill that can be attempted whole; it does not test isolated parts for a task novices cannot yet coordinate, and the learners' prior knowledge is not given on the claim page. Rigour not established from the text.
- [Students who researched with web search wrote better justifications than students using an AI chatbot](../claims/web-search-higher-quality-justifications-than-llm.md) [+M]: one randomized experiment, n = 91, a science inquiry task. The chatbot group reported lower intrinsic, extraneous and especially germane load ([lower germane load](../claims/llm-search-lower-germane-cognitive-load.md) [+W]) and gave fewer relevant aspects in its justifications (η² = 0.11); an exploratory mediation found the germane-load difference accounted for the quality difference ([mediation](../claims/germane-load-mediates-tool-effect-on-justification-quality.md) [+W]). It supports the "keep productive effort" edge: a tool that removes effort can remove the processing the outcome needed. Outcome was immediate; no delayed horizon.
- Collaborative cognitive load: a review reports earlier experiments in which groups learned more efficiently than individuals on high-complexity tasks and less efficiently on simple ones ([collective working memory effect](../claims/collective-working-memory-effect-complexity-dependent.md) [+W]; [collaboration aids high-load tasks](../claims/collaborative-learning-collective-working-memory-advantage.md) [+W]), and argues that coordination costs can cancel the benefit ([transactive costs](../claims/transactive-costs-annul-load-sharing-benefit.md) [+W]); one experiment found groups with prior experience together more efficient only when the information to share was dense ([Zambrano 2019](../claims/zambrano-2019-efficiency-advantage-only-high-density.md) [~W]). The first findings are second-hand, without sample sizes or effect sizes, and efficiency combines performance with rated effort.

Keep learners, task, comparator, outcome and horizon with each result when transporting it. Effort ratings, efficiency, immediate performance, delayed retention and transfer are different outcomes; a non-significant difference is not equivalence; pooled effects do not forecast one learner's response, and these unlike comparisons are not ranked here. **No claim in the wiki tests the general relationship as stated**, a sequence-level policy of removing, deferring and restoring demand against a fixed design; most claims test one lever each, and the two whole-design comparisons above test the removal half only, with a large gain on session tests in one and no learning difference in the other.

## The evidence by question

- *Should component knowledge come before the whole task?* [Pretraining learners on a system's key parts and terms before the main lesson improved knowledge and real-world transfer in one VR experiment, and is reported second-hand to improve learning in multimedia studies](../claims/pretraining-improves-transfer.md) [+M]
- *When should support be withdrawn as the learner improves?* [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]
- *Should complexity rise gradually, or can a whole task be given at full complexity from the start?* [For Italian verb conjugation, constantly high complexity beat a gradual increase two days later](../claims/constantly-high-complexity-improves-posttest-performance.md) [~M]; no claim in the wiki compares the two for a task novices cannot yet coordinate.
- *Does a tool that makes the task easier help?* [An AI chatbot lowered rated load and produced weaker justifications than web search](../claims/web-search-higher-quality-justifications-than-llm.md) [+M]; [deliberately disfluent text did not improve outcomes](../claims/disfluency-no-effect-test-expectancy.md) [~W], so neither easing nor arbitrary hardening is the lever.
- *When the outcome is retention at a delay, should effortful practice be reintroduced once the material is understood, and for which material?* [Retrieval practice and spaced retrieval improve achievement and retention by medium amounts, while interleaving helps category learning only for some materials and blocking beats it for words](../claims/desirable-difficulties-enhance-learning.md) [~M]

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02 (maintainer's decision): claims this page cited before the 2026-10-02 rewrite which the rewrite did not use as core evidence. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked. The rest of that list was read against the model on 2026-10-15 and now sits in it. The claims linked since were read on 2026-10-19: most now sit in the model, and those below were read and do not change it.

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+M] — not settled: the text available could not confirm the entries (abstract). Bears on the explanatory hypothesis only (immediate-memory capacity and how grouping stretches it), not on any learning comparison the model makes; its discussion's point that a chunk must be meaningful to the learner is consistent with the expertise qualification.
- [Under high extraneous load (hint presentation and L and rL condition), no test-score increases were observed on identical or near-transfer problems](../claims/extraneous-load-eliminates-germane-load-learning-gains.md) [~W] — read 2026-10-19: a conference paper (Reversi training) reporting no pre-post gain within one condition, not a between-condition test of removing extraneous load, and r1; consistent with the removal lever but too weak to change it.
- [Solving problems with graphs increased mental effort, shown by a higher proportion of silence in think-aloud data](../claims/graphs-increase-mental-effort-silence.md) [~W] — read 2026-10-19: silence rose from 62% to 66% with a graph, marginal (p = .07), interpreted by the authors as effort; an observation-method lead, not a learning comparison.
- [Participants valued multimodal experiences combining visualization with hands-on interaction, while reporting challenges with complex or unclear visualizations](../claims/multimodal-valued-complex-visualizations-hinder.md) [+W] — read 2026-10-19: participant reports from a small mixed-reality toolkit user study (r1); consistent with the coherence advice in the revising-materials row, no learning outcome compared.
- [The prior knowledge of the intended audience determines a text's information density, rate of new information, and accompanying background](../claims/audience-prior-knowledge-determines-information-density.md) [~W] — read 2026-10-19: a 1977 theoretical paper on writing decisions; consistent with the expertise qualification, no data.
- [TBRS-model-derived hypotheses about presentation-pace effects were supported in two experiments, provided prior knowledge is taken into account](../claims/tbrs-hypotheses-tested-two-experiments.md) [+W] — attached 2026-10-21 from Sébastien Puma et al. (2018), which proposed "When investigating presentation-pace effects during learning, take learners' prior knowledge into account".
- [Concept-map generation requires age-appropriate instructional support: younger learners profit from high-coherence, pre-structured maps](../claims/concept-mapping-support-age-interaction.md) [+W] — attached 2026-10-22 from Garvin Brod (2021), which proposed "Match the amount of instructional support in generative learning activities to learners' age, giving younger learners more structure"; tests this page's relationship.
- [Generating drawings is effective for university students but largely ineffective for elementary-school children unless instructional support is extremely high](../claims/drawing-ineffective-elementary.md) [~W] — attached 2026-10-22 from Garvin Brod (2021), which proposed "Match the amount of instructional support in generative learning activities to learners' age, giving younger learners more structure"; tests this page's relationship.
- [Benefits of learning with more than two external representations primarily depend on the provision of appropriate instructional support.](../claims/mer-benefits-depend-on-instructional-support.md) [+W] — attached 2026-10-22 from Rexigel et al. (2024), which proposed "Do not assume a universal ideal number of external representations; tailor representational sets to learners and context"; tests this page's relationship.
- [Some studies found that presenting more than two representations negatively impacted learning and problem-solving, especially for students with low prior knowledge.](../claims/more-than-two-representations-negative-effects-low-prior-knowledge.md) [+W] — attached 2026-10-22 from Rexigel et al. (2024), which proposed "Do not assume a universal ideal number of external representations; tailor representational sets to learners and context"; tests this page's relationship.
- [Gesturing while explaining problem solving reduces cognitive load](../claims/gesturing-reduces-cognitive-load.md) [+W] — attached 2026-10-22 from Fred Paas et al. (2011), which proposed "Use biologically primary skills (communication, gesture, movement, object manipulation) to scaffold acquisition of biologically secondary knowledge"; tests this page's relationship.
- [Sensorimotor action supports learning when it makes concept-relevant relations easier to process](../claims/action-helps-when-concept-relevant-relations-easier.md) [+W] — attached 2026-10-22 from Fred Paas et al. (2026), which proposed "Optimize cognitive load in embodied instruction: aim for better learning and transfer, not movement or lower load for its own sake"; tests this page's relationship.
- [Embodied action can harm learning when it adds motor demands, redundant cues, or irrelevant activity without improving understanding](../claims/action-hurts-when-adding-motor-demands.md) [+W] — attached 2026-10-22 from Fred Paas et al. (2026), which proposed "Optimize cognitive load in embodied instruction: aim for better learning and transfer, not movement or lower load for its own sake"; tests this page's relationship.
- [Consistently high task complexity yields faster immediate problem-solving than gradually increasing complexity, with no post-test difference](../claims/high-complexity-faster-immediate-performance.md) [~W] — attached 2026-10-22 from Ines Zeitlhofer et al. (2024), which proposed "Expose learners to consistently high task complexity to stimulate germane processing without harming intrinsic interest"; tests this page's relationship.
- [Task complexity strongly affects germane cognitive load in Round 1, with effects dissipating by post-test](../claims/complexity-germane-load-round-effects.md) [~W] — attached 2026-10-22 from Ines Zeitlhofer et al. (2024), which proposed "Expose learners to consistently high task complexity to stimulate germane processing without harming intrinsic interest"; tests this page's relationship.

## Objective and learner-valued goal

Ask what the learner wants to accomplish and why, separately from the designer's objective. Agreement, divergence and uncertainty are observations; do not infer motivation from compliance or from a low effort rating. The designer chooses the representative task, the permitted aids, the criterion and the horizon. Load management is a means to that objective, and the objective decides which effort is avoidable: an aid that removes effort is a support if the objective allows it and an obstacle to the target if it does not. How much effort a learner chooses to spend also matters: a review argues that load-based designs tested in the laboratory, such as worked examples, may not deliver their effect when learners are not motivated to study the material carefully, and that authentic-setting studies seldom check this ([optimal task design may depend on effort allocation](../claims/task-design-depends-on-effort-allocation.md) [~W]).

For example, a laboratory trainee may value getting through a pipetting session without the embarrassment of handling equipment they cannot name, while the designer's objective is accurate unaided pipetting a week later. A primer and step-by-step guidance can serve the first and raise in-session accuracy, yet the delayed, unaided performance remains untested until it is probed. Record both aims, say when the guidance is withdrawn, and check the delayed task.

## What would revise this model?

The model should weaken if comparable learners on comparable material learn as well from the unmanaged design under defensible comparisons with aligned outcomes, or if deferring component knowledge (primers, segments, parts first) repeatedly fails to help on tasks with many interacting elements; the Italian conjugation result, where a gradual ramp lost to constant high complexity, is one such signal for a simpler procedural task. The expertise qualification should weaken if, as in the segmenting synthesis, higher prior knowledge keeps predicting larger rather than smaller benefits. The "keep productive effort" edge should weaken if effortful conditions fail to improve delayed outcomes for the learners and materials in question, as interleaving did for word lists and problem-first designs did for younger children. If rated effort falls without any gain in performance, transfer or retention, the design reduced discomfort, not demand on learning. Do not protect the model by relabelling every failure after the fact as "too much load" or "too little challenge".

A learning-phase efficiency gain, immediate performance, near transfer, delayed retention and unaided use in the learner's setting are separate claims. The present evidence does not establish a threshold of expertise at which to remove support, an optimal amount of difficulty, an ordering of load-management techniques, or that changes in load cause the gains they accompany.

## Claims

- [Invested mental effort and perceived task difficulty are significantly positively correlated at all measurement points except MP2.5, with correlations increasing as material complexity rises](../claims/effort-difficulty-positively-correlated-except-mp25.md) [~W]
- [Delayed cognitive load assessments after learning exceed the average of during-learning assessments only when complexity decreases across the learning material](../claims/delayed-icl-exceeds-average-only-decreasing-complexity.md) [~W]
- [Prior knowledge correlates negatively with delayed ICL and ECL and positively with delayed GCL, consistent with meta-analytic findings](../claims/prior-knowledge-correlates-with-load-types.md) [~W]
- [Coherence principle: people learn better when extraneous material is excluded rather than included (d = 0.86 across 19 tests)](../claims/coherence-principle-extraneous-material-effect.md) [~W]
- [Presenting primary knowledge first and then secondary knowledge was more efficient in both performance and motivation](../claims/primary-first-sequencing-benefits.md) [+W]
- [Students invest more mental effort in paper-based questions than in equivalent computer-based questions](../claims/greater-mental-effort-paper-questions.md) [~W]
- [Perceived task difficulty relates to cognitive strategy use with both a linear and a negative quadratic (inverted U) component, and the quadratic relationship is fully mediated by cognitive load](../claims/task-difficulty-inverted-u-cognitive-strategies.md) [~W]
- [Fifth and sixth graders showed higher delayed retention and lower cognitive load when learning science from videos than from illustrated texts](../claims/video-better-retention-lower-load-classroom.md) [~W]
- [Task complexity has a strong omnibus multivariate effect on performance, GCL, meta-awareness, and intrinsic interest combined](../claims/complexity-omnibus-manova-effect.md) [~W]

## Related Principles
- [Segmenting Principle](segmenting.md)
- [Coherence Principle](coherence.md)
- [Contiguity Principle (Spatial and Temporal)](contiguity.md)

- [Cognitive Load Theory](cognitive-load-theory.md)
- [Use the age-friendly ESL classroom as a remedy for social isolation by building a supportive community of learners with confidence-building and peer mentoring](expanding-social-networks.md)
- [Contextualize abstract content in familiar, personal topics and teach new vocabulary primarily through visuals and body language](cultural-life-experiences-connections.md)
- [Pre-training Principle](pretraining.md)
- [Scaffolding](scaffolding.md)

## Examples

- A math lesson introduces multi-step equation solving in short worked chunks, with each step visually separated and narrated before learners attempt a full problem.
- A science simulation hides advanced controls for novices, then gradually reveals more variables once learners can explain the core system.
- [Consider a focused more is more approach combining minimized extraneous processing with prompts for generative processing](../strategies/focused-more-is-more-generative-processing.md)
- [Step One: a free age-friendly pre-beginning ESL and citizenship curriculum for older immigrants](../products/step-one.md)
- [Accommodating Processing Speed Challenges](../strategies/accommodating_processing_speed_challenges.md)
- [Allow Think-Time and Re-reading (Processing Speed)](../strategies/allow-think-time-and-re-reading-processing-speed.md)
- [Wait Time](../strategies/wait-time.md)
- [Allowing Think-Time and Re-Reading](../strategies/allowing_think-time_and_re-reading.md)
- [Jointly varying intrinsic and extraneous load in a Reversi game to isolate germane load effects](../designs/reversi-training-conditions-varying-intrinsic-and-extraneous-load.md)
- [Progressively disclose analytical depth: start beginners with streamlined visual interfaces, then introduce richer analytical tools as expertise grows](../strategies/progressive-disclosure-visual-to-analytical-support.md)
- [Apply cognitive science design principles simultaneously and in combination when revising curriculum, with targeted rather than arbitrary development decisions](../strategies/apply-cognitive-principles-simultaneously-in-curriculum-revision.md)
- A history text is reorganized into short sections with headings, key dates, and a timeline so learners can process causal relationships without hunting for structure.
- A coding tutorial removes unnecessary UI options and provides starter files so novices can focus on the target concept before handling full project complexity.
- [Present information in a manner that encourages learner activities that optimize intellectual performance](../strategies/present-information-to-optimize-intellectual-performance.md)
- [Manage intrinsic load with a part-whole approach, task variability, and self-explanation to raise germane load](../strategies/part-whole-variability-self-explanation-raise-germane-load.md)

## Key Sources
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Clinton, V., Cooper, J.L., Michaelis, J., Alibali, M.W., & Nathan, M.J. (2017). How Revisions to Mathematical Visuals Affect Cognition: Evidence from Eye Tracking. In Eye-tracking technology applications in educational research (pp. 195-218). IGI Global. https://eric.ed.gov/?id=ED574984. [doi:10.4018/978-1-5225-1005-5.ch010](https://doi.org/10.4018/978-1-5225-1005-5.ch010)
- Kala, N., & Ayas, A. (2023). Effect of instructional design based on cognitive load theory on students' performances and the indicators of element interactivity. Journal of Turkish Science Education, 20(3), 468-489. https://doi.org/10.36681/tused.2023.027
- Lihui Lv & Chunyan Liu. (2022). Recast, Task Complexity and Child Learners' L2 Development. English Language Teaching, 15(9). https://doi.org/10.5539/elt.v15n9p95
- Weintraub, L. (2025). Grandma Needs English, Too. Adult Literacy Education. http://doi.org/10.35847/LWeintraub.7.1.37
- Houichi, A., & Sarnou, D. (2020). Cognitive Load Theory and its Relation to Instructional Design: Perspectives of Some Algerian University Teachers of English. Arab World English Journal. https://dx.doi.org/10.24093/awej/vol11no4.8

<!-- deprecated 2026-10-02: superseded by the conditional model above; the principle body as it stood before the rewrite, kept verbatim.

## Description
Cognitive load management is the short-form canonical target for instructional choices that reduce extraneous processing, sequence support, and calibrate task demands to learner expertise.

## Implications
Cognitive load management matters when instruction risks overwhelming working memory before learners have formed stable schemas. In practice, this means chunking information and removing unnecessary complexity so learners can devote more attention to the underlying idea or procedure [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S]. These moves usually make early learning more manageable, but the same supports can become inefficient once learners are more knowledgeable, so guidance should fade or simplify as expertise grows [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M].

### Context
#### Requirements
- **Attention to what consumes working memory**
- **Support matched to task complexity and learner expertise**
#### Constraints
- **Over-management can remove productive challenge**

### Target Learning Objectives
- Preserve capacity for understanding and schema construction.

### Theory
#### Supporting
- [Cognitive Load Theory](cognitive-load-theory.md)

### Claims

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S] — reducing unnecessary processing and organizing material into coherent units preserves capacity for schema formation
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M] — supports that help novices can become inefficient or redundant as learner expertise increases
-->

<!-- merged 2026-10-07 from principles/design-principles-depend-on-prior-knowledge ("Apply instructional design principles with attention to learners' prior knowledge, since effects on cognition depend on proficiency level"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Apply instructional design principles with attention to learners' prior knowledge, since effects on cognition depend on proficiency level

> **Principle** · [All principles](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The article concludes that although many instructional design principles are framed as "one size fits all," their effects on student cognition may depend on students' level of prior knowledge. Revisions based on signaling, contiguity, and coherence principles reduced cognitive load and processing for low prior knowledge students but increased them for middle prior knowledge students. Curriculum developers should therefore consider prior knowledge when applying such principles, and the authors caution it "may be premature to apply these principles to curriculum development on a large scale."

## Design Implications

### Context
#### Requirements
- Assessment of learners' prior knowledge before applying design revisions
#### Constraints
- The findings do not support the effectiveness of the "less is more" approach in improving student learning; combining principles makes it uncertain how each principle individually related to the findings

### Target Learners
- middle-school mathematics students

### Target Learning Objectives
- learning from lessons with text and visual representations

### Claims

- [Revised Visuals No Learning Effect](../claims/revised-visuals-no-learning-effect.md) [~M]
- [Revised Visuals Processing Text Prior Knowledge Interaction](../claims/revised-visuals-processing-text-prior-knowledge-interaction.md) [+M]
- [Revisions to math-relevant visuals affect cognitive load differently by prior knowledge group, including reduced load for high prior knowledge students](../claims/revised-visuals-cognitive-load-math-visuals-interaction.md) [+W]
- [Revised visuals reduce cognitive load while reading lesson text for low prior knowledge students but increase it for middle prior knowledge students](../claims/revised-visuals-cognitive-load-text-prior-knowledge-interaction.md) [+W]
- [Revised visuals reduce cognitive processing of math-relevant visuals for low prior knowledge students but increase it for middle prior knowledge students](../claims/revised-visuals-processing-math-visuals-interaction.md) [+W]
- [Revisions made no reliable difference to total time spent with the lesson](../claims/revisions-no-effect-time-with-lesson.md) [+W]

## Related Principles
- 

## Examples

- [Consider a focused more is more approach combining minimized extraneous processing with prompts for generative processing](../strategies/focused-more-is-more-generative-processing.md)

## Key Sources
- Clinton, V., Cooper, J.L., Michaelis, J., Alibali, M.W., & Nathan, M.J. (2017). How Revisions to Mathematical Visuals Affect Cognition: Evidence from Eye Tracking. In Eye-tracking technology applications in educational research (pp. 195-218). IGI Global. https://eric.ed.gov/?id=ED574984. [doi:10.4018/978-1-5225-1005-5.ch010](https://doi.org/10.4018/978-1-5225-1005-5.ch010)
-->

<!-- merged 2026-10-07 from principles/determine-element-interactivity-before-designing-instruction ("Teachers should determine a topic's element interactivity level and develop an instructional design appropriate to it"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Teachers should determine a topic's element interactivity level and develop an instructional design appropriate to it

> **Principle** · [All principles](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
The article concludes that "Teachers are responsible for determining a topic's level of element interactivity and developing an appropriate instructional design." Because complexity within CLT arises from element interactivity, teachers should first classify the topics they teach (e.g. with expert judgement into low, high, very high) and then design instruction — such as CLT-based materials — that manages working memory load accordingly. The study's evidence that scores, mental effort and study time track interactivity level grounds this recommendation.

## Design Implications

### Context
#### Requirements
- Determination of students' prior knowledge before classifying topics, since interactivity level depends on the learner's existing schemata.
#### Constraints
- The study's classification was made relative to topics within one unit, judged by two expert lecturers with over ten years' experience each.

### Target Learners
- first-year university chemistry students
- high school chemistry students

### Target Learning Objectives
- effective learning of high element interactivity science topics at retention and transfer levels

### Claims

- [Mental Effort Study Time Indicate Element Interactivity](../claims/mental-effort-study-time-indicate-element-interactivity.md) [+M]
- [Clt Design Effective Learning Retention Transfer](../claims/clt-design-effective-learning-retention-transfer.md) [+M]
- [In one thermodynamics study, retention and transfer scores tended to be lower on topics of higher element interactivity, a descriptive pattern with several sessions that did not fit it](../claims/retention-transfer-scores-decrease-with-element-interactivity.md) [+W]
- [A CLT-based instructional design yields significantly higher retention and transfer scores than lecturer-designed instruction in thermodynamics, controlling for prior knowledge and memory span](../claims/clt-instructional-design-raises-retention-transfer-thermodynamics.md) [+W]
- [No significant difference between groups on the thermodynamics achievement post-test or cognitive load scale after CLT-based versus lecturer-designed instruction](../claims/no-group-difference-tat-posttest-cls.md) [~W]

## Related Principles
- 

## Examples
-

## Key Sources
- Kala, N., & Ayas, A. (2023). Effect of instructional design based on cognitive load theory on students' performances and the indicators of element interactivity. Journal of Turkish Science Education, 20(3), 468-489. https://doi.org/10.36681/tused.2023.027
-->

<!-- merged 2026-10-07 from principles/low-task-complexity-child-learners-recasts ("For child beginner language learners, keep task complexity low or moderate so attention remains available for noticing recasts"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# For child beginner language learners, keep task complexity low or moderate so attention remains available for noticing recasts

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends that when designing tasks for young foreign language beginners, cognitive demands should match learners' cognitive development level: "it is better to set a moderate or low task complexity level to allow the learners to have more attention available for the development of the target-like language." Otherwise learners become cognitively overloaded and have little attention left to notice recasts and process the target language.

## Design Implications

### Context
#### Requirements
- Tasks must still elicit production of the target form so that recasts can be supplied in response to errors
#### Constraints
- Grounded in child learners aged 11-12 learning English in China; the authors state task complexity should not exceed child learners' cognitive load

### Target Learners
- child beginner EFL learners in primary school

### Target Learning Objectives
- grammar acquisition through corrective feedback during task-based interaction

### Claims
- [Task Complexity Negatively Related Child Written Production](../claims/task-complexity-negatively-related-child-written-production.md) [+M]
- [Task Complexity No Effect Child Oral Production](../claims/task-complexity-no-effect-child-oral-production.md) [~M]

## Related Principles
- 

## Examples
-

## Key Sources
- Lihui Lv & Chunyan Liu. (2022). Recast, Task Complexity and Child Learners' L2 Development. English Language Teaching, 15(9). https://doi.org/10.5539/elt.v15n9p95
-->

<!-- merged 2026-10-07 from principles/measured-pace-one-concept-at-a-time-older-learners ("Teach older language learners at a measured pace, one new skill or concept at a time, with extra review and wait time"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Teach older language learners at a measured pace, one new skill or concept at a time, with extra review and wait time

> **Principle** · [All principles](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 3 studies (2 review, 1 design), `q1`–`q2` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
Because older adults tend to process information more slowly and may have declining working memory, the author delivers instruction in careful stages, provides more repetition and review than a typical ESL class, and lets students demonstrate comprehension (yes/no, "or", and "show me" tasks) before producing new language from memory. She reports that "A few extra seconds of "wait time" can make a big difference in students' willingness to take risks, their ability to produce responses, and to develop confidence in speaking English." She also found combining several new concepts in one activity caused lessons to fail to connect.

## Design Implications

### Context
#### Requirements
- Instructors must plan staged presentation of new information and resist combining multiple new concepts in a single activity
#### Constraints
- The author notes not every older student exhibits the same characteristics, but the older the student, the more likely modifications are needed

### Target Learners
- older adult beginning-level English learners

### Target Learning Objectives
- oral English comprehension and production
- retention of new vocabulary and concepts

### Claims

- [Older Beginner Esl Outcome Gains](../claims/older-beginner-esl-outcome-gains.md) [+M]
- [Common language teaching methods such as oral drills, memorization, and fast-paced competitive activities disadvantage older learners](../claims/rote-drills-disadvantage-older-learners.md) [+W]
- [Learning ability does not decline with age in healthy older adults](../claims/learning-ability-does-not-decline-with-age.md) [~W]
- [Healthy older adults can learn another language, by one digest's account](../claims/no-evidence-older-adults-cannot-learn-language.md) [~W] — the absence is the source's, not the literature's: Grognet (1997), a practitioner digest that cites no studies, asserts that research does not show older adults cannot learn another language, and adds that adults need more deliberate effort than children; no study recorded in this wiki tests the point.

## Related Principles

- [Use the age-friendly ESL classroom as a remedy for social isolation by building a supportive community of learners with confidence-building and peer mentoring](expanding-social-networks.md)
- [Contextualize abstract content in familiar, personal topics and teach new vocabulary primarily through visuals and body language](cultural-life-experiences-connections.md)

## Examples

- [Step One: a free age-friendly pre-beginning ESL and citizenship curriculum for older immigrants](../products/step-one.md)
- [Accommodating Processing Speed Challenges](../strategies/accommodating_processing_speed_challenges.md)
- [Allow Think-Time and Re-reading (Processing Speed)](../strategies/allow-think-time-and-re-reading-processing-speed.md)
- [Wait Time](../strategies/wait-time.md)
- [Allowing Think-Time and Re-Reading](../strategies/allowing_think-time_and_re-reading.md)
- [Think-Time and Re-Reading](../strategies/allowing_think-time_and_re-reading.md)

## Key Sources
- Weintraub, L. (2025). Grandma Needs English, Too. Adult Literacy Education. http://doi.org/10.35847/LWeintraub.7.1.37
-->

<!-- merged 2026-10-07 from principles/reduce-extraneous-optimize-intrinsic-increase-germane ("Manage the three load types: reduce extraneous load, optimize intrinsic load, and increase germane load"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Manage the three load types: reduce extraneous load, optimize intrinsic load, and increase germane load

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 2 studies (2 quant-synthesis), `q4` · 1 of 2 report an effect size

## Description
The article states that instructional material is most effective when no load type overburdens working memory capacity, and that educators must manage the three loads differentially. It attributes to Van Merrienboer and Sweller the directive that "Educators must seek to reduce extraneous load, optimize intrinsic load, and increase germane load". Reducing extraneous load frees working-memory capacity that can then be allocated to germane processing, supporting schema construction in long-term memory.

## Design Implications

### Context
#### Requirements
- Teachers must understand human cognitive architecture and the three load types to apply the principle
#### Constraints
- The extent to which instructional features contribute to extraneous or germane load may depend on the learner and their experienced intrinsic load

### Target Learners
- university EFL students

### Target Learning Objectives
- effective instructional design that avoids working memory overload

### Claims

- [Clt Three Load Types Framework](../theories/clt-three-load-types-framework.md) [+M]
- [Cognitive Load Management](../claims/cognitive-load-management.md) [+M]

## Related Principles
- 

## Examples

- [Jointly varying intrinsic and extraneous load in a Reversi game to isolate germane load effects](../designs/reversi-training-conditions-varying-intrinsic-and-extraneous-load.md)

## Key Sources
- Houichi, A., & Sarnou, D. (2020). Cognitive Load Theory and its Relation to Instructional Design: Perspectives of Some Algerian University Teachers of English. Arab World English Journal. https://dx.doi.org/10.24093/awej/vol11no4.8
-->

<!-- merged 2026-10-15 from principles/cognitive-load-reduction ("Cognitive Load Reduction"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Cognitive Load Reduction

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 3 studies (2 review, 1 causal), `q2`–`q3` · 0 of 3 report an effect size

## Description
Cognitive load reduction is the short-form canonical target for instructional moves that simplify presentation, reduce extraneous processing, and make initial learning more manageable.

## Implications
Cognitive load reduction is most useful at the point where presentation format, task setup, or competing demands would otherwise consume the attention learners need for understanding. The practical implication is not to make learning easy in the abstract, but to remove avoidable processing so learners can focus on the structure of the idea or task [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S]. Chunking, signaling, and simplification often help novices learn faster at first, but oversimplifying can also weaken later transfer if learners never reconnect the simplified version to authentic complexity.

### Context
#### Requirements
- **Attention to sources of unnecessary processing**
- **Design choices that simplify without removing the core learning**
#### Constraints
- **Too much simplification can weaken later transfer**

### Target Learning Objectives
- Preserve working-memory capacity for understanding and schema formation.

### Theory
#### Supporting
- [Cognitive Load Management](cognitive-load-management.md)
- [Cognitive Load Theory](cognitive-load-theory.md)

### Claims
- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S] — reducing extraneous processing helps working memory stay available for understanding and schema formation

## Related Principles
- [Scaffolding](scaffolding.md)

## Examples
- A history text is reorganized into short sections with headings, key dates, and a timeline so learners can process causal relationships without hunting for structure.
- A coding tutorial removes unnecessary UI options and provides starter files so novices can focus on the target concept before handling full project complexity.

## Key Sources
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251-296. [https://doi.org/10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
-->
