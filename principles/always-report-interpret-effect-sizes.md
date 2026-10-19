---
type: principle
id: always-report-interpret-effect-sizes
aliases: [report-effect-sizes-with-p-values]
title: Always report and interpret effect sizes alongside p values for primary outcomes
description: "For anyone writing or reading an evaluation of an instructional intervention, reporting a standardized effect size with its interval, comparison and measure beside every p value, and reading it against effects for the same kind of outcome rather than a universal label, is expected to lead to better adopt-or-revise decisions than significance alone; no claim in the wiki tests that expectation, though claims show significance and size diverging, significance filtering inflating sizes, and sizes depending on the measure."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
sources:
  - id: thompson-2000
    resource: "https://eric.ed.gov/?id=ED440121"
    title: "Thompson, B. (2000). The APA Task Force on Statistical Inference (TFSI) Report as a Framework for Teaching and Evaluating Students' Understandings of Study Validity. Paper presented at the annual meeting of the American Educational Research Association. https://eric.ed.gov/?id=ED440121"
    author: Thompson, B
  - id: mohamed-farrag-ahmed-badawi-2019
    resource: "https://doi.org/10.5539/elt.v12n4p166"
    title: "Mohamed Farrag Ahmed Badawi. (2019). The Effect of Explicit English Morphology Instruction on EFL Secondary School Students’ Morphological Awareness and Reading Comprehension. English Language Teaching, 12(4). https://doi.org/10.5539/elt.v12n4p166"
    author: Mohamed Farrag Ahmed Badawi
---

# Always report and interpret effect sizes alongside p values for primary outcomes

> **Principle** · [All principles](index.md)
> **Evidence** · 21 claims (13 for, 8 mixed) · 22 studies (8 quant-synthesis, 6 causal, 4 review, 4 theoretical), `q1`–`q4` · 6 of 22 report an effect size · 20 claims rest on one study

## Conditional relationship

This page owns one decision: **what a report of an instructional intervention must say about the size of its effect, and how a reader should read that size before acting on it.** The person here is whoever writes or reads an evaluation: a researcher or graduate student writing up a study, a designer reporting a pilot of their own course, a teacher, leader or purchaser reading a study before adopting a design (an `adult`, often a `novice` at reading statistics). Their usual starting response is to treat "statistically significant" as "it works" and "not significant" as "it does not work". The principle says: for every primary outcome, report a standardized effect size with its interval beside the p value, say what was compared with what, on which measure, at which horizon, and interpret the size against effects found for the same kind of outcome, measure and learners, not against a universal label. The expectation is that decisions made this way (adopt, revise, drop, test again) follow the size and reliability of the effect rather than the accident of whether a test crossed p < .05.

**No claim in the wiki tests that expectation**: nothing here compares the decisions or the later learning outcomes of readers given effect sizes with those of readers given p values alone. What the claims establish are the premises, each in education data:

- **Significance and size come apart.** In What Works Clearinghouse re-analyses, author-reported significant effects were no longer significant once clustering and multiple comparisons were corrected for, while one of those effects (0.35 on a reading test) was still large enough to count as substantively important by the Clearinghouse's convention.
- **Filtering on significance inflates the size.** A methodological commentary reports that applying the significance filter in education produces large magnitude (Type M) errors; a meta-analysis of test-enhanced learning found that publication-bias corrections cut its average transfer prediction substantially.
- **The size depends on the measure.** Across reviews of tutoring systems, early literacy, critical thinking and mindset, effects were larger, or more often significant, on researcher-made or aligned tests than on standardized ones.
- **Universal labels mislead.** Effects differ by subject tested and by grade, and shrink as a program scales up, so "0.4 is medium" says little without a reference class.

**The relationship is conditional on** the reader's decision (adopt a program, revise a design, plan a larger study); the outcome measure (aligned with what was taught, or standardized); the design (randomized or not, individuals or clusters, how many); and whether the reported effect survived a significance filter or a selective search. It rests on the view, set out in [Statistical significance as the criterion distinguishing a program effect from chance](../theories/statistical-significance-effect-criterion.md), that a program "has an effect" when a group difference is significant (A program is said to have an effect when the difference between program and non-program groups is statistically significant [~W]); this page keeps that criterion for chance and adds the size beside it.

**How this sits beside the converted siblings.** [Evidence-Based Teaching and Scientific Reasoning](evidence-based-teaching-and-scientific-reasoning.md) holds the wider decision of adopting an approach on the grounds of a comparison that could have come out otherwise; reading the size of that comparison's effect is one move inside it, and this page gives that move's detail without repeating its model. [Validity, Reliability and Bias in Classroom Assessment](validity-reliability-and-bias-in-classroom-assessment.md) holds whether a classroom measure measures what it claims; this page takes the measure as given and asks how big the difference on it is. How a study should be designed so its effect can be trusted at all is in [Designing a Valid Experiment](../methods/designing-a-valid-experiment.md).

## Default design, while the relationship is untested

The earlier page's requirements, made into a routine a writer or reader can follow. Each step is a proposal; its evidence status is stated beside it.

1. **Report a standardized effect size for every primary outcome, with an interval.** Give the group means, standard deviations and n, the effect size (Cohen's d or Hedges' g for two groups; name the index), and its 95% confidence interval, every time a p value is reported. From the earlier page and its source (the APA Task Force); the requirement itself is untested here as a cause of better decisions. Where a study reports only test statistics, as one randomized trial of self-regulated learning training reported group-by-time interactions with no effect size per outcome, the reader cannot tell how much each outcome moved ([In a randomized trial of SRL interventions in an online mathematics preparation course, group and time interacted significantly on SRL knowledge, self-efficacy and the SRL overall score, with Group TDP (training + diary + peer feedback) showing the most prominent gains](../claims/srl-web-training-peer-feedback-group-by-time-interaction-online-math-prep.md) [~W]).
2. **Say what was compared with what.** Name the comparison condition (business as usual, an active alternative, no treatment, a pre-test), the unit assigned (learners, classes, schools) and the horizon of the outcome (`immediate-performance`, `delayed-retention`). An effect size without its comparison cannot be read. Untested proposal.
3. **Name the measure and its alignment.** Say whether the outcome is a researcher-made test of what was taught or a standardized test, and report them separately when both exist. Evidence: effects were much larger on local than on standardized tests across tutoring-system evaluations ([ITS evaluation results depend strongly on test type: effects are large on locally developed tests (ES = 0.73) and small on standardized tests (ES = 0.13)](../claims/test-type-moderates-its-effects.md) [+M]).
4. **Correct the significance test for the design, and keep the effect size whatever the test says.** In a class- or school-randomized study, test at the level assigned or correct for clustering; report the effect size whether or not the corrected test is significant. Evidence: [Greenwood et al. (1993) reported a statistically significant CWPT effect on CTBS-Reading, but the WWC-corrected analysis was not statistically significant](../claims/cwpt-ctbs-effect-significance-discrepancy.md) [+M].
5. **Read a non-significant result against the smallest effect the study could detect.** Report the minimum detectable effect size; if it is larger than the effect that would matter, call the result inconclusive, not "no effect". Evidence: a 50-person, 10-school study reported it could detect only d = 0.81 ([The evaluation used a school-level cluster-randomized quasi-experiment (N = 50) that was powered only to detect large effects (d = 0.81)](../claims/cluster-randomized-quasi-experiment-powered-for-large-effects.md) [+M]).
6. **Interpret the size against a reference class, not a universal label.** Compare it with effects from studies of the same kind of outcome, measure type, subject and grade, and with earlier studies of the same program. Where a convention is needed for a reader, the Clearinghouse's +0.25 "substantively important" line (about 10 percentile points) is a convention, not a finding ([The guide treats an effect size of +0.25 or higher as substantively important, equivalent to raising performance at least 10 percentile points](../claims/effect-size-025-substantively-important-threshold.md) [+W]). Cohen's labels (0.2, 0.5, 0.8) are untested as a guide for education decisions here.
7. **Translate the size into the reader's terms.** Add one plain sentence: the improvement in percentile points, or the raw-score difference on the test the reader knows. Never write a d of 0.65 as "65%"; a meta-analysis of self-regulated learning interventions did ([Self-regulated learning interventions have a moderate effect (0.65) on learning outcomes in online and blended environments](../claims/srl-interventions-moderate-effect-online-blended.md) [~W]: the claim page quotes the authors saying the interventions "affect learning results ... by 65%"). Untested proposal, from the earlier page's "practical significance".
8. **Expect a single significant result to be too large.** Before acting on one significant study, especially a small one or one found by a search for positive results, discount its size and look for a replication or a pre-registered test. Evidence: Large Type M (magnitude) errors almost certainly exist when applying the statistical significance filter in education research [+M]. The amount to discount is not given by any claim here.

**Dose and progression across sessions** (for teaching this to graduate students or teachers, the earlier page's target learners). An untested proposal: four sessions of about 60 minutes. Session 1: from one real report, the learner extracts means, SDs and n and computes d by hand (20 minutes), then reads two studies with the same p value and very different d (20 minutes), then writes the one-sentence translation (20 minutes); the teacher supplies the studies and a worked calculation. Session 2: the learner reads a study with a significant author-reported result that a re-analysis corrected (step 4), and a non-significant one with a large minimum detectable effect (step 5); the teacher supplies the pairs, learners write the reading. Session 3: the learner places a reported effect against a reference class (same measure type, subject and grade) the teacher has gathered, then finds one themselves. Session 4: the learner writes the effect-size paragraph for a study of their own choice, or their own pilot, unaided, and a peer checks it against steps 1–8. A learner moves on when their unaided paragraph for a new study covers the comparison, the measure, the interval and the translation; one who still writes "significant, so it works" repeats session 2 with a new pair.

When the routine cannot be followed in full: if the source prints no SDs, report the test statistic, the n per group and that no effect size could be computed; do not estimate one by assumption.

## Fitting the design to a situation

The three facts that most change the decision:

- **Who reads the report, and what will they decide with it.** A journal referee, a funder, a school board choosing a program and a designer revising a course need the same numbers but different translations and different reference classes. If unstated, ask: who acts on this result, and what are their options?
- **What the outcome measure is.** A test written for the intervention and a standardized test give different sizes for the same program, so a size means nothing until the measure is named. If unstated, ask: who wrote the test, and how close is it to what was taught?
- **How the study was designed and found.** Clustering, a small sample, adaptive assignment, or a result picked because it was significant each change how far the reported size can be trusted. If unstated, ask: what was randomized, how many units were there, and how was this study chosen from others?

| If the brief says… | Then change… | Basis |
|---|---|---|
| The reader is a teacher, leader or purchaser, `novice` at statistics, or has low confidence with numbers | Lead with one sentence in percentile points or raw-score difference on a test they know, then the d and its interval; keep the p value in a note | [The guide treats an effect size of +0.25 or higher as substantively important, equivalent to raising performance at least 10 percentile points](../claims/effect-size-025-substantively-important-threshold.md) [+W] (a reporting convention, not tested with readers) |
| The learners are graduate students in educational research (a course on reading studies) | Run the four-session arc above; use real published pairs where significance and size disagree as the compared cases | untested proposal; the earlier page's source proposes the Task Force report as a teaching framework |
| The outcome is a researcher-made or aligned test | Report it apart from any standardized outcome; compare its size only with other aligned-test effects; expect a smaller effect on a standardized test | [ITS evaluation results depend strongly on test type: effects are large on locally developed tests (ES = 0.73) and small on standardized tests (ES = 0.13)](../claims/test-type-moderates-its-effects.md) [+M]; [Language and early writing interventions showed larger effects on researcher-developed than standardized outcome measures, while phonological awareness, print knowledge, and decoding effects were comparable across measure types](../claims/researcher-developed-measures-larger-language-effects.md) [~M] (tutoring systems and early literacy; the gap is not the same for every skill) |
| The study randomized classes or schools | Test significance at the level assigned or correct for clustering; report the effect size either way; state the number of clusters | [Greenwood et al. (1993) reported a statistically significant CWPT effect on CTBS-Reading, but the WWC-corrected analysis was not statistically significant](../claims/cwpt-ctbs-effect-significance-discrepancy.md) [+M]; [Clustering effects vary by design but are typically large in education random-assignment evaluations](../claims/clustering-effects-large-school-samples-education-trials.md) [+M] |
| A small pilot of one course or class, or a single session only | Report the effect size, interval and minimum detectable effect; call a non-significant result inconclusive; plan the next test rather than a verdict | [The evaluation used a school-level cluster-randomized quasi-experiment (N = 50) that was powered only to detect large effects (d = 0.81)](../claims/cluster-randomized-quasi-experiment-powered-for-large-effects.md) [+M] (pre-service teachers; carried to any small pilot) |
| The decision rests on one significant study, or on studies found by searching for positive results | Discount the reported size; look for a replication, a pre-registered trial or a bias-corrected meta-analytic estimate before adopting | Large Type M (magnitude) errors almost certainly exist when applying the statistical significance filter in education research [+M]; [Publication-bias assessments substantially reduce the intercept prediction, often indicating no positive transfer when the identified moderators are absent](../claims/publication-bias-reduces-intercept-no-transfer-without-moderators.md) [+M] (test-enhanced learning transfer) |
| An online platform assigned learners adaptively (a multi-armed bandit or similar) | Report that assignment was adaptive and treat the effect size as likely overstated, especially a small one; confirm with a fixed-allocation comparison | [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](../claims/mab-overestimates-effect-sizes.md) [+M] (simulation) |
| A program moves from pilot to wide use (a district, a state) | Expect the scaled effect to be smaller than the pilot's; set the adoption threshold against the scaled estimate, not the pilot's | [Effect sizes of Pre-K Mathematics decreased over time as the intervention moved through successive scale-up phases](../claims/pre-k-math-effect-sizes-decreased-over-scale-up.md) [~M] (one pre-K mathematics program) |
| Comparing effects across subjects or grades (a mathematics program against a reading program; primary against secondary) | Compare sizes only within the same subject and grade band; do not rank a mathematics effect above a reading effect on size alone | [Effect sizes based on mathematics tests are significantly larger than effect sizes based on reading tests in targeted secondary interventions](../claims/math-test-effects-larger-than-reading.md) [~M]; [Interventions in higher Grades tend to have somewhat lower effect sizes; other study characteristics show few significant moderator effects](../claims/grade-level-moderates-effect-size.md) [~M] (struggling learners, targeted interventions) |
| The report uses a non-standard index (a gain ratio, a percentage gain, a pre-post change only) | Report the raw means and SDs as well, name the index and its own threshold, and do not compare it with d benchmarks | [Within the explicit morphology instruction group, the pre-to-post gain ratio was above Blake's 1.2 minimum for morphological awareness (1.28) and below it for reading comprehension (1.06)](../claims/emi-effect-size-larger-for-awareness-than-comprehension.md) [~M] (one EFL study reporting Blake's modified gain ratio from experimental-group pre-post means) |
| The report says an effect of 0.65 means a 65% improvement, or a reader made that error | Use the error as the worked contrast: show what a d of 0.65 means in percentile points and why it is not a percentage | [Self-regulated learning interventions have a moderate effect (0.65) on learning outcomes in online and blended environments](../claims/srl-interventions-moderate-effect-online-blended.md) [~W] (the misreading is quoted on the claim page) |
| Several outcomes reported only as a multivariate test or interaction | Give an effect size per primary outcome, with its interval, beside the omnibus test | [In a randomized trial of SRL interventions in an online mathematics preparation course, group and time interacted significantly on SRL knowledge, self-efficacy and the SRL overall score, with Group TDP (training + diary + peer feedback) showing the most prominent gains](../claims/srl-web-training-peer-feedback-group-by-time-interaction-online-math-prep.md) [~W] (reported no per-outcome effect size) |
| The brief names its own reporting template, standard or rubric (a journal's, a funder's, the Clearinghouse's) | Keep it and its categories as given; add only what it lacks among: effect size with interval, comparison, measure type, horizon | untested proposal |
| A fixed short time budget (a 45-minute professional-development slot for teachers) | One study, 10 minutes extracting the numbers, 15 computing d and the percentile translation, 15 reading it against a supplied reference class, 5 writing the one-sentence verdict | untested proposal |
| Mixed modes: some readers in the room, some remote or on phones; or a self-paced online module | Put the numbers in a shared table everyone can see, give the d calculation as a fill-in template, and collect each person's one-sentence translation in writing | untested proposal |
| One facilitator for many teachers, or scarce facilitator time | Give a worked example and an answer key so peers check each other's calculations; the facilitator reads only the final translations | untested proposal |
| The audience is a board, funder or the public, who should see the conclusion and not the analysis | Give the translated effect, the comparison and the uncertainty in two sentences; put the effect sizes, intervals and test statistics in an appendix | untested proposal |
| Data are from a small group of identifiable learners (one class, a small program) | Report effect sizes for groups only; suppress cells too small to protect privacy and say so; the learners or institution decide who sees individual results | untested proposal |
| The brief wants a whole results section or evaluation report written, not separate exercises | Keep it whole: draft the full section once, then revise once against steps 1–8 | untested proposal |

Eleven of the nineteen rows rest on a claim. None tests the reporting move itself on readers' decisions; each shows a reason the move matters (sizes diverge from significance, depend on the measure, shrink with scale) in the settings its study covered, and the rows carry that to the reader's setting. The rest are untested proposals.

## Observation, state and explanation

What can be observed is what a report contains (which numbers, which comparison, which measure) and what a reader writes or decides after reading it. "Understands practical significance" and "over-trusts p values" are inferred states.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| A report gives p values and no effect sizes | The writer was not asked for them; the analysis (a multivariate test, an interaction) has no obvious single effect size; the effect is small and the writer prefers not to show it | Ask for the means, SDs and n per outcome and compute d; compare with the significance verdict. |
| A large effect from a small or single study | A real large effect; inflation from the significance filter; an aligned measure written for the intervention | Check the measure, the sample, the minimum detectable effect, and whether a larger or independent study found a similar size. |
| A significant result with a tiny effect | A very large sample; a real but practically small effect | Translate into percentile points or raw score; ask whether that difference would change the reader's decision. |
| A non-significant result with a moderate effect size | Too few units to detect it; clustering not accounted for; no effect, with a noisy estimate | Report the interval and the minimum detectable effect; look for other studies. |
| A reader concludes "it works" or "it doesn't" from p alone, or reads d as a percentage | Habit from training that emphasized significance; no translation given | Ask the reader to state the size in percentile points and the comparison condition; see whether their decision changes. |

These rows are proposals, untested with readers as diagnostics. A second look at a report can change the reader's reading of it, so record what was asked and in what order.

## Evidence and qualifications

No claim in the wiki tests whether reporting and interpreting effect sizes improves the decisions or outcomes that follow. The claims below support its premises in education data, and qualify it.

- [ITS evaluation results depend strongly on test type: effects are large on locally developed tests (ES = 0.73) and small on standardized tests (ES = 0.13)](../claims/test-type-moderates-its-effects.md) [+M]: one meta-analysis of 50 intelligent tutoring evaluations (Kulik & Fletcher 2016), three entries coded `q2`–`q4`, `quant-synthesis`; test type was the moderator most strongly related to effect size (local 0.73, standardized 0.13, both 0.45; a homogeneity analysis gave 0.62, 0.09 and 0.46). One study within it, reported second-hand, found 0.99 on local tests against 0.36 on standardized ones. It supports naming the measure beside every effect size.
- [Greenwood et al. (1993) reported a statistically significant CWPT effect on CTBS-Reading, but the WWC-corrected analysis was not statistically significant](../claims/cwpt-ctbs-effect-significance-discrepancy.md) [+M]: a WWC intervention report on a randomized trial of 218 sixth graders in six schools; after correction for clustering the effect was not significant, but its size (0.35, improvement index +14) was still substantively important by the WWC's +0.25 convention. Coded `q3`, `i1`. It is the clearest case here of significance and size giving different readings of the same result.
- [Author-reported statistically significant program effects did not remain significant after WWC corrections for clustering and multiple comparisons](../claims/wwc-corrections-eliminate-author-reported-significance.md) [+M]: a WWC report on two randomized trials of a drug-prevention program; significant author-reported findings were not significant after correction. No effect size is attached. It supports correcting the test for the design; it does not show the size of the effects.
- Large Type M (magnitude) errors almost certainly exist when applying the statistical significance filter in education research [+M]: an invited commentary (Deke 2023, `q2`, `theoretical`) reporting two methodological studies' conclusion that significance filtering in education produces large magnitude errors. It prints no figure. It supports reading a lone significant effect as an overestimate; it is second-hand.
- [Publication-bias assessments substantially reduce the intercept prediction, often indicating no positive transfer when the identified moderators are absent](../claims/publication-bias-reduces-intercept-no-transfer-without-moderators.md) [+M]: one meta-analysis of test-enhanced learning (Pan & Rickard 2018, `q4`); bias corrections left moderator estimates almost unchanged but cut the predicted transfer effect, often to none. It shows how much a published average can fall once selection is accounted for, in one literature.
- [The evaluation used a school-level cluster-randomized quasi-experiment (N = 50) that was powered only to detect large effects (d = 0.81)](../claims/cluster-randomized-quasi-experiment-powered-for-large-effects.md) [+M]: one study of 50 pre-service teachers in 10 schools; its sensitivity analysis gave a minimum detectable d of 0.81, so small and moderate effects could go undetected. It is an example of reporting the minimum detectable effect, not a test of doing so.
- [Clustering effects vary by design but are typically large in education random-assignment evaluations](../claims/clustering-effects-large-school-samples-education-trials.md) [+M]: a methodological paper on power in education experiments (Schochet 2005); large school samples are needed. It supports step 4 and the clustering row.
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](../claims/mab-overestimates-effect-sizes.md) [+M]: simulations of adaptive (multi-armed bandit) assignment in educational experiments; a true effect of 0.2 was measured as 0.30 on average, a true 0.8 as 0.93. It limits trust in effect sizes from adaptive platforms, not in effect sizes as such.
- **Qualifications.** Universal size labels do not travel: in a review of targeted secondary interventions, effect sizes on mathematics tests were larger than on reading tests, and quasi-experiments gave larger effects than randomized trials ([Effect sizes based on mathematics tests are significantly larger than effect sizes based on reading tests in targeted secondary interventions](../claims/math-test-effects-larger-than-reading.md) [~M]); in the companion K–6 review, higher grades tended to show somewhat lower effects, with no significant differences between quasi-experiments and randomized trials, general and subdomain tests, or mathematics and reading tests ([Interventions in higher Grades tend to have somewhat lower effect sizes; other study characteristics show few significant moderator effects](../claims/grade-level-moderates-effect-size.md) [~M]); and one program's effects decreased through successive scale-up phases ([Effect sizes of Pre-K Mathematics decreased over time as the intervention moved through successive scale-up phases](../claims/pre-k-math-effect-sizes-decreased-over-scale-up.md) [~M]). An effect size is also not self-interpreting: the WWC's +0.25 line is a stated convention with no data behind it ([The guide treats an effect size of +0.25 or higher as substantively important, equivalent to raising performance at least 10 percentile points](../claims/effect-size-025-substantively-important-threshold.md) [+W]), and in the early-literacy review the gap between researcher-developed and standardized measures held for language and early writing but not for phonological awareness, so the measure gap is not the same everywhere.
- **The old page's own examples.** [Within the explicit morphology instruction group, the pre-to-post gain ratio was above Blake's 1.2 minimum for morphological awareness (1.28) and below it for reading comprehension (1.06)](../claims/emi-effect-size-larger-for-awareness-than-comprehension.md) [~M]: the merged page's source (one EFL secondary study, `q2`, `causal`, `r1`–`r2`) reported Blake's modified gain ratio from the experimental group's pre- and post-test means alongside significance tests. It illustrates reporting a size beside significance; it also shows a within-group gain index that cannot be compared with between-group d benchmarks, which is why the routine asks for the index to be named. [Self-regulated learning interventions have a moderate effect (0.65) on learning outcomes in online and blended environments](../claims/srl-interventions-moderate-effect-online-blended.md) [~W] (one meta-analysis of 15 studies, `q3`, `i2`) reports a pooled d with the misreading "65%". [In a randomized trial of SRL interventions in an online mathematics preparation course, group and time interacted significantly on SRL knowledge, self-efficacy and the SRL overall score, with Group TDP (training + diary + peer feedback) showing the most prominent gains](../claims/srl-web-training-peer-feedback-group-by-time-interaction-online-math-prep.md) [~W] (one randomized trial, `q3`, `i?`) reports interactions without per-outcome effect sizes. The earlier page cited both SRL claims as support; they bear on this page only as examples of reporting, not on its relationship. The second carries a `## Studies bearing on this claim` table gathering 7 distinct studies, which is about self-regulated learning, not reporting.

None of these claims measures what a reader does differently with an effect size in hand. Do not rank them by their own effect sizes; they are about different questions.

## The evidence by question

- *Does the kind of outcome measure (a researcher-made or aligned test against a standardized one) change the size of the effect a study reports?* [ITS evaluation results depend strongly on test type: effects are large on locally developed tests (ES = 0.73) and small on standardized tests (ES = 0.13)](../claims/test-type-moderates-its-effects.md) [+M]
- *Does a significance verdict alone give a reliable reading of an intervention's effect in education studies?* Large Type M (magnitude) errors almost certainly exist when applying the statistical significance filter in education research [+M]

## Further evidence, not yet read against this model

- "P Values Confounded Indices" [+M]: listed on the earlier page with no link and no claim page; it names the Task Force report's point that a p value confounds effect size with sample size. No claim page in the wiki carries it, so it supports nothing here until one is written from the source.
- [The type of CT measure employed (standardized vs. non-standardized; item format) influences evaluation of intervention effectiveness](../claims/ct-measure-type-influences-effectiveness-evaluation.md) [+M]: a systematic review of 33 critical-thinking intervention studies in higher education; 93% of studies with non-standardized measures reported significant improvement against 55% with standardized ones. Bears on the measure question (it counts significant results, not sizes); member of the first question above.
- [Training effects were larger on outcome measures aligned with the trained skill (blending, segmenting) than on less aligned measures](../claims/alignment-trained-skill-larger-effects-phonological-awareness.md) [+M]: a WWC footnote on phonological awareness training studies. Bears on the measure question; no figures.
- [Type of achievement measure moderates the correlation only when laboratory measures are excluded; course-exam correlation drops to r = .04](../claims/achievement-measure-moderator-lab-exclusion.md) [+M]: a growth-mindset meta-analysis's sensitivity analysis; a correlational outcome, so it bears on the measure question only indirectly.
- For within-subjects designs, the author recommends reporting Cohen's d_rm or Cohen's d_av rather than Cohen's dz [+W] — attached 2026-10-16 from Lakens (2013), which proposed "Always report effect sizes, specify the standardizer used, report generalized eta squared for ANOVAs, and interpret effect sizes rather than relying on Cohen's benchmarks".
- [Cohen's small, medium, and large effect size benchmarks are arbitrary and should not be interpreted rigidly](../claims/cohen-benchmarks-arbitrary.md) [+W] — attached 2026-10-16 from Lakens (2013), which proposed "Always report effect sizes, specify the standardizer used, report generalized eta squared for ANOVAs, and interpret effect sizes rather than relying on Cohen's benchmarks".

## Objective and learner-valued goal

The objective this page serves is a decision about a design or program that follows the size and reliability of its effect on an outcome that matters, at the horizon that matters. Elicit separately what the person writing or reading the report values: a researcher may value a publishable significant result; a graduate student, passing the methods course; a purchaser, a clear yes or no; a teacher, whether their own learners will do better. Agreement and divergence are both observations. A writer who values publication may leave out a small effect size; a reader who wants a yes or no may skip the interval. Make the translated size and its uncertainty the shortest sentence in the report, so it is the one most readers see.

For example, a school leader wants to know whether a reading program will help the struggling readers in their own school. The study reports a significant effect on a researcher-made test and a small, non-significant effect on the state test. The objective this page sets is to state both sizes with their measures; the leader's goal is the state test, so the second number is the one that bears on their decision. Record both.

## What would revise this model?

The expectation should weaken if studies of readers (teachers, leaders, researchers) given effect sizes with intervals and translations make no better, or worse, adoption decisions than readers given p values alone, judged against later outcomes; or if readers routinely misread effect sizes in ways that cost more than misreading p values. If measure-type gaps disappear in studies with well-aligned standardized tests, step 3 becomes a reporting detail rather than an interpretive rule. If bias-corrected or pre-registered estimates in education turn out close to the significant published ones, step 8's discount should shrink. Do not protect the model by blaming every misread effect on a missing translation.

Reporting an effect size, interpreting it against a reference class, and the decision that follows are separate claims. The present evidence establishes no threshold that makes an education effect worth acting on, no discount factor for a single study, and no reference class that serves every outcome.

## Claims

- [Comprehension strategy instruction shows a large overall effect, but reliability is undermined by few standardized measures](../claims/comprehension-strategy-large-effect-unreliable.md) [~W]
- [The positive GenAI writing effect is robust across dependence-aware, sensitivity, and risk-of-bias specifications, but the wide prediction interval spans near-zero to large effects](../claims/genai-writing-effect-robustness-checks.md) [+W]

## Related Principles

- [Designing a Valid Experiment](../methods/designing-a-valid-experiment.md)
- [Evidence-Based Teaching and Scientific Reasoning](evidence-based-teaching-and-scientific-reasoning.md) — the wider decision of adopting an approach on a comparison; reading the effect's size is one move in it.
- [Validity, Reliability and Bias in Classroom Assessment](validity-reliability-and-bias-in-classroom-assessment.md) — whether the measure behind an effect size measures what it claims.

## Examples
-

## Key Sources
- Thompson, B. (2000). The APA Task Force on Statistical Inference (TFSI) Report as a Framework for Teaching and Evaluating Students' Understandings of Study Validity. Paper presented at the annual meeting of the American Educational Research Association. https://eric.ed.gov/?id=ED440121
- Mohamed Farrag Ahmed Badawi. (2019). The Effect of Explicit English Morphology Instruction on EFL Secondary School Students’ Morphological Awareness and Reading Comprehension. English Language Teaching, 12(4). https://doi.org/10.5539/elt.v12n4p166

<!-- deprecated 2026-10-15: superseded by the conditional model above. The previous body, kept verbatim.

## Description
The principle, drawn from the APA Task Force on Statistical Inference report, is that researchers must report effect-size estimates whenever p values are reported, and interpret them in practical and theoretical context against previously reported effects. The paper notes the 1994 APA manual merely "encourage" (p. 18) effect size reporting, and that this encouragement proved ineffectual, so journals now require it.

## Design Implications

### Context
#### Requirements
- Effect-size estimates must accompany reported p values; interpretation requires placing effect sizes in the context of previously reported effects.
- Compute and report an effect-size measure alongside significance tests when evaluating an instructional intervention
#### Constraints
- The 1994 APA manual's mere encouragement of effect-size reporting was ineffectual across 23 journals, per the paper's summary of 11 empirical studies.
- The article's illustration uses Blake's modified gain ratio in a single quasi-experimental study; it does not claim this measure generalizes to all designs

### Target Learners
- graduate students in educational research
- behavioral science researchers
- EFL first-year secondary school students

### Target Learning Objectives
- interpreting research results
- understanding statistical significance versus practical significance
- Morphological awareness
- Reading comprehension

### Claims
- P Values Confounded Indices [+M]
- [Emi Effect Size Larger For Awareness Than Comprehension](../claims/emi-effect-size-larger-for-awareness-than-comprehension.md) [+M]
- [In a randomized trial of SRL interventions in an online mathematics preparation course, group and time interacted significantly on SRL knowledge, self-efficacy and the SRL overall score, with Group TDP (training + diary + peer feedback) showing the most prominent gains](../claims/srl-web-training-peer-feedback-group-by-time-interaction-online-math-prep.md) [+W]
- [Self-regulated learning interventions have a moderate effect (0.65) on learning outcomes in online and blended environments](../claims/srl-interventions-moderate-effect-online-blended.md) [+W]

## Related Principles

- [Designing a Valid Experiment](../methods/designing-a-valid-experiment.md)

## Examples
-

## Key Sources
- Thompson, B. (2000). The APA Task Force on Statistical Inference (TFSI) Report as a Framework for Teaching and Evaluating Students' Understandings of Study Validity. Paper presented at the annual meeting of the American Educational Research Association. https://eric.ed.gov/?id=ED440121
- Mohamed Farrag Ahmed Badawi. (2019). The Effect of Explicit English Morphology Instruction on EFL Secondary School Students’ Morphological Awareness and Reading Comprehension. English Language Teaching, 12(4). https://doi.org/10.5539/elt.v12n4p166

-->
<!-- merged 2026-10-07 from principles/report-effect-sizes-with-p-values ("Report effect sizes alongside p values when evaluating instructional interventions"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Report effect sizes alongside p values when evaluating instructional interventions

> **Principle** · [All principles](index.md)
> **Evidence** · 3 claims (3 for) · 3 studies (2 causal, 1 quant-synthesis), `q2`–`q3` · 2 of 3 report an effect size · 3 claims rest on one study

## Description
The article argues that statistical significance alone can mislead about the practical value of an intervention, because most prior EFL morphology studies failed to report effect sizes, making it "impossible for readers/researchers to estimate how practically significant the findings were". It therefore reports both p and t values and Blake's modified gain ratio, citing Huck's caution that a statistically significant result can be "completely devoid of any practical significance whatsoever". The principle is that both substantive significance (effect size) and statistical significance should be reported.

## Design Implications

### Context
#### Requirements
- Compute and report an effect-size measure alongside significance tests when evaluating an instructional intervention
#### Constraints
- The article's illustration uses Blake's modified gain ratio in a single quasi-experimental study; it does not claim this measure generalizes to all designs

### Target Learners
- EFL first-year secondary school students

### Target Learning Objectives
- Morphological awareness
- Reading comprehension

### Claims

- [Emi Effect Size Larger For Awareness Than Comprehension](../claims/emi-effect-size-larger-for-awareness-than-comprehension.md) [+M]
- [In a randomized trial of SRL interventions in an online mathematics preparation course, group and time interacted significantly on SRL knowledge, self-efficacy and the SRL overall score, with Group TDP (training + diary + peer feedback) showing the most prominent gains](../claims/srl-web-training-peer-feedback-group-by-time-interaction-online-math-prep.md) [+W]
- [Self-regulated learning interventions have a moderate effect (0.65) on learning outcomes in online and blended environments](../claims/srl-interventions-moderate-effect-online-blended.md) [+W]

## Related Principles

- [Always report and interpret effect sizes alongside p values for primary outcomes](always-report-interpret-effect-sizes.md)

## Examples
-

## Key Sources
- Mohamed Farrag Ahmed Badawi. (2019). The Effect of Explicit English Morphology Instruction on EFL Secondary School Students’ Morphological Awareness and Reading Comprehension. English Language Teaching, 12(4). https://doi.org/10.5539/elt.v12n4p166
-->
