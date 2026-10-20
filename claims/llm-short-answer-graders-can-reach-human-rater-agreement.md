---
type: claim
title: LLM Short-Answer Graders Agree With One Human Rater More, and the Other Less, Than the Two Raters Agree With Each Other
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: llm-short-answer-graders-can-reach-human-rater-agreement
evidence_strength:
sources:
  - id: porcaro-2026
    resource: "https://doi.org/10.5281/zenodo.23480844"
    title: "David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844"
    author: David S. Porcaro
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# LLM Short-Answer Graders Agree With One Human Rater More, and the Other Less, Than the Two Raters Agree With Each Other

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

On the one corpus in this release with two independent human raters (Mohler: undergraduate data-structures short answers, marked 0–5), an LLM grader scoring against a rubric and a model answer agreed with one rater more closely, and with the other less closely, than the two raters agreed with each other: 0.798 and 0.549 in quadratic-weighted kappa against the raters' 0.608 on the same 150 answers (one model, a single run). On 300 answers graded by three models (under assigned attainment labels, both gradings pooled) the same bracketing held for each: 0.597–0.741 against one rater, 0.366–0.472 against the other, 0.531 between the raters. The source reads this as showing that agreement with one human is a weak instrument on short free-text answers, and says the higher figure should not be read as better-than-human grading; it is not a finding that an LLM grader is as good as a human one.

## Subclaims

- Agreement should be read against a measured human-human ceiling, not against 1.0, and the source recommends stating the reliability of the human reference beside any agreement figure. That ceiling is often unmeasurable: the requirement of two or more independent grades per item ruled out most public grading data the author surveyed, and the corpus behind most of this release's figures (JorGPT) has one rater.
- Which human is chosen as the reference materially changes the measured agreement. On the one corpus here with two independent raters (Mohler) the same grader scores 0.549 against one rater and 0.798 against the other (a single run), and on three models grading 300 answers the choice of rater moves agreement by 0.23–0.27 in quadratic-weighted kappa (0.25–0.28 in Gwet's AC2).
- Agreement should be reported with a spread statistic beside it. A spread ratio (the grader's standard deviation over the human's) well below 1 means the grader concentrates its marks in the middle of the scale, which kappa alone can hide; the shipped prompt's ratio here was 0.94 and 0.89 on two model tiers, against 0.60–0.78 for the corpus's own baselines on a smaller first run. The source also recommends Pearson r beside kappa, to separate better ranking from a shift in where marks land.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `associational · r?`

A shipped LLM grading prompt scored public, teacher-graded corpora, and its agreement with the human marks (quadratic-weighted kappa, with bias and a spread ratio beside it) was read against human–human agreement measured on corpora with two or more raters (the article's Section 5.1): undergraduate computer-science answers with one teacher (JorGPT, a 150-answer stratified draw), data-structures answers with two independent raters (Mohler), whole Java programs with four raters (Menagerie), and a re-analysis of a deposit with four instructors on every item (HARMOGEN-R). Several figures are single runs. Observation records: `lazuli-grader-jorgpt-2026`, `lazuli-grader-mohler-2026` and `lazuli-grader-harmogen-2026` (supports), `lazuli-grader-menagerie-2026` (qualifies).

## Discussion

**Scope of the claim.** It is about *agreement on a rubric-scored ordinal scale for short free-text answers*, measured by quadratic-weighted kappa. It is not a claim that the grader is right, that it is fair, or that it is stable — those are separate propositions with separate evidence, and two of them come out considerably less well. It is also not a claim about production: the measurements are on university computer-science and data-structures corpora, other people's questions and other people's rubrics.

**Why the ceiling is the whole argument.** An agreement of 0.85 sounds like a 15% error rate and is not one. On the only corpus available with two independent raters, two graduate assistants marking the same answers to the same questions on the same course agreed at 0.519 — and lower still on the rows a consistency filter had removed, so the true figure is below that. Against a single human reference, much of what looks like machine error is disagreement the humans would have had with each other: if the grader's errors are independent of the raters', about half (0.45–0.55) of each of three graders' squared error against one human is that human's own disagreement with the others. The level is also a kappa statement: under Gwet's AC2 the same Mohler raters agree at 0.858, and no grader-versus-human comparison reverses.

**What the interventions found.** Four attempts on one model (Gemini 3.5 Flash Lite) detected no change in agreement: a stronger model tier, pooling three or four calls, anchor exemplars, and supplying the learner's previous attempt (three single runs, and an interval on the last that leaves room for a gain of +0.056). The pooling result is in the release's evidence records and interpretation, not its article. They are not four nulls: on a harsh second model the anchor exemplars did raise QWK by 0.033, and on the Mohler corpus sibling course context raised it by up to 0.035 in a single run (also a release-only result). A rescaling applied after grading did move agreement: fitting each grader's unlabeled marks to the teacher's mean and standard deviation, without information about the student, raised QWK by 0.047 to 0.132 on the models that mark below the teacher or compress the scale, and by 0.008 on Gemini, which already used the teacher's spread.

**What would falsify or bound this.** A well-moderated rater pair working to a shared rubric with adjudication would presumably agree far better than 0.519, and the claim should then be read against that higher bar. The corpora here record no rubric, training or moderation for their raters, so this is agreement between two people doing a job rather than agreement under a characterised protocol. On near-closed items the bar is high: on HARMOGEN-R, half multiple choice, four instructors agree at 0.981, and reaching that ceiling is a much weaker statement than reaching one of about 0.5.

**It does not extend to large artefacts or craft rubrics.** This release also had three models grade 60 whole student programs on four rubric dimensions, and in kappa every model agreed with the human graders far less than the humans agreed with each other (QWK 0.058 to 0.233 against 0.438, on fourteen levels); under AC2 no difference was resolved on fourteen levels. The claim is about short free-text answers judged on content.

## Related Claims

- [Human graders of open-ended work agree with each other less than treating one grade as ground truth implies.](human-graders-agree-less-than-single-grade-ground-truth-implies.md) — the ceiling this claim is read against
- [Pooling repeated LLM grades does not improve agreement on short answers.](pooling-repeated-llm-grades-does-not-improve-agreement.md) — one of the four attempts that detected no change in the residual gap
- [Graded exemplars shift an LLM grader by the level they are marked at.](graded-exemplars-shift-an-llm-grader-by-the-level-they-are-marked-at.md) — another, and the one that separates calibration from agreement
- [Peer feedback accuracy depends on expertise.](peer-feedback-accuracy-depends-on-expertise.md) — the same question about human raters
- [The TA ground truth was produced under a one-rater-per-item design with co-grading, an exceptions log, instructor audit, and student review, with an estimated grading-error rate of about 0.1% in the student-inspected subsample](ta-ground-truth-one-rater-per-item-error-rate.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — a narrower finding that bears on this claim
- [The LLM observation function's per-answer mastery evidence correlates with true mastery at r = 0.68 pooled, but only r ≈ 0.15 within the weak tier, making it least reliable for low-ability learners](collearn-observation-function-within-tier-reliability.md) — related
