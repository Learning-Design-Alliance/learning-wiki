---
type: claim
title: Showing a Grader a Learner's Prior Performance Biases the Grade
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: showing-a-grader-a-learners-prior-performance-biases-the-grade
evidence_strength:
sources:
  - id: porcaro-2026
    resource: "https://doi.org/10.5281/zenodo.23480844"
    title: "David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844"
    author: David S. Porcaro
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Showing a Grader a Learner's Prior Performance Biases the Grade

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

Telling an LLM grader how a learner has performed before — either by showing a previous attempt with its mark, or by supplying an attainment estimate — shifts the grade for identical work: an attainment label in its own direction, a low prior mark downward (a high one does not raise it). It is not shown to improve how well the grader ranks the work. Whether the shift moves a learner's mark toward or away from the teacher's depends on the grader.

## Subclaims

- On one model (Gemini 3.5 Flash Lite), a previous attempt that scored badly lowers the current grade on identical work by about half a grade point on a ten-point scale (0.44, 95% interval 0.26 to 0.62, in the re-run with intervals; 0.59 in the first run), while agreement stays within a few hundredths.
- An attainment label changes the mark on identical work: the same answer gets 0.28 to 0.75 points more under a high label than a low one on six models from five developers run through their APIs, frontier and open-weights included, inside both tails of the attainment distribution (6 or more and below 4 of 10; the middle was not sampled), on 300 answers from 33 students in one corpus. With one model's reasoning set to minimal the effect doubles, to 1.04. Claude Fable 5.1, graded on a 100-answer subset by a different route (as Claude Code subagents; 99 answers graded under both labels), shows it too (+0.31 [+0.19, +0.45], its low-tail interval including zero). Across the six API models the effect grows with the gap between the two labels rather than acting as a fixed step (pooled ρ = +0.84 [+0.38, +1.36]), over the label gaps observed (2.0 to 7.7 points). On whole programs it reached 1.4 to 2.3 points on a 14-level rubric on two of three models.
- The direction relative to the teacher is not fixed. For weaker students' work the true low label moved the mark toward the teacher on the one grader generous to it (Gemini 3.5 Flash Lite) and away on the three already harsh on it (GPT-4.1-mini, Qwen3-235B, Claude Opus 5.5); for stronger students' work the high label moved four of the five graders harsh on it toward the teacher (GPT-5-mini did not move). These calls are against each grader's own unlabeled mark; on the one model re-run against a same-length neutral sentence, about two-thirds of the high-tail reward (+0.14 of +0.22) was the sentence's presence, while the low-tail penalty was the label's. That pattern follows each model's own error in the tail; it is not a tested mechanism. The effect is therefore not a uniform penalty on learners described as weak, and a false low label costs strong work 0.30 to 0.79 points.
- For attempt history, the downward pull comes from the prior *mark*: the same weak previous answer shown without its grade moves the current grade slightly up (+0.14), not down, while a strong one shown without its grade lowers it by 0.24, so stripping the mark is not by itself safe. A high prior mark does not raise the grade.
- The label is not shown to improve ranking (no resolved change in Pearson r on any of nine runs, though the intervals reach +0.049, and the check was added after the runs). On three model configurations that mark strong work below the teacher it raised QWK by 0.029 to 0.046, consistent with moving where marks land. A rescaling that does not use the label, fitting each grader's unlabeled marks to the teacher's mean and standard deviation, agreed with the teacher better than the raw labeled marks on those three runs, by 0.038 QWK on average (95% interval 0.013 to 0.061); whether the label adds anything once both are calibrated is unresolved, with an addition above 0.035 ruled out.
- Over a course, feeding the learner model's belief back into the grader amplifies the effect modestly (by a factor of 1.066 to 1.167 over a 40-item term, in a simulation driven by four of the six measured graders) and the loop stays stable (largest eigenvalue 0.730 to 0.757; runaway would need a label effect 5.9 to 12.6 times each model's own). A strong learner whose record starts wrongly low takes 1 to 3 more items to recover.
- Context about the *task* behaves differently from context about the *learner*: graded example answers move the grade by the level they are marked at.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `causal · r?`

Within-item ablations in which the same public, teacher-graded answers were graded under prompts that differed only in what they said about the student (the article's Sections 5.2–5.7): a marked or unmarked previous attempt (150 answers, one model), the student's held-out attainment and a swapped label from the opposite tail (300 answers from 33 students in a 79-student undergraduate corpus, six API models, intervals resampling students), the same labels on short answers marked out of 5 and on 60 whole Java programs, assigned labels on 3,000 school essays with demographic fields (two models), and a simulated course in which grades feed the learner model. The original arms were not pre-registered; the re-tests were, each with a synthetic detection floor. Observation records: `lazuli-grader-jorgpt-2026`, `lazuli-grader-menagerie-2026` and `lazuli-grader-loop-simulation-2026` (supports), `lazuli-grader-asap2-2026` (qualifies).

## Discussion

**Scope of the claim.** Two separate manipulations, both on identical current work: a real previously-graded answer to the same question supplied as the learner's prior attempt, and the learner's own mean grade across their other answers, held out from the case being graded. The second is a stand-in for a mastery estimate, cleaner than one would be, and a mastery estimate is what a system with a learner model would naturally have available to pass.

**Why accuracy does not argue for it.** The label is not shown to improve how the grader ranks work on any model (no resolved change in Pearson r; intervals allow gains up to +0.049). Where it raises agreement, the gain is consistent with moving a harsh grader's marks toward the teacher's level (a reading, not a measured decomposition), and a calibration that does not need to know who wrote the work did at least as well: on the three runs where the label raised QWK, the label-free rescaling beat the raw labeled marks by 0.038 on average. That rescaling has to be fitted on work representative of the students it will grade; fitted on one tail and applied to the other, it left the low tail too generous by 0.40 to 0.60 points on five of seven runs (resolved from zero on two).

**The architectural argument, which is the durable part.** In a system that maintains a belief about a learner's mastery, the grader's job is to assess the work and the belief's job is to be updated *by* that assessment. Feeding the belief back into the grader closes a loop that must stay open: the belief then partly determines the evidence that updates it; in simulation this amplifies the label's effect by 7–17% over a term and stays stable. The belief update already carries the learner's history — that is what it is for — so the grader does not need it and should not have it.

**Why it is worth stating as a claim rather than a bug.** This is the most natural next step for anyone who has built a learner model. The graph knows where the learner sits; the grader is a call away; passing it through looks like personalisation. It is the one to refuse, and the reason is structural rather than empirical, which is why the measurement matters mainly as confirmation.

**What would bound this.** The label effect is established on six models from five developers, including two open-weights families and a frontier model; its magnitude varies by a factor of almost three between them (+0.28 to +0.75), with the frontier model smallest, and changes again by item type (0.4 to 2.8 times its short-answer size on whole programs), so it has to be measured per model and per kind of work. The label tested is one fixed sentence stating a number; qualitative or implied descriptions of a student were not tested and may move the mark more. Only the mark was analysed, not the feedback text. Nothing here says whether a *human* grader shown the same information behaves differently; the pooled human grading-bias effect in experiments is g = 0.36 (Malouff & Thorsteinsson 2016), and the comparison on the same items is future work.

**The gap this claim cannot close on its own.** Prior attainment is not a protected attribute, so this is not by itself a demographic-fairness finding. But wherever prior attainment correlates with a protected attribute — which it frequently does — an attainment-keyed bias becomes a demographic one while remaining invisible to an audit that inspects only protected attributes. That route was tested on ASAP 2.0, a public essay corpus with demographic fields, on two models with assigned labels. Relative to no label, the low label did not fall harder on any group tested: every resolved difference favoured the focal group, each time on one model only (English learners and disability-identified students on Qwen, economically disadvantaged students on GPT-4.1-mini), and on Qwen partly an artefact of matching on a noisy human score; race and ethnicity were underpowered. The spread between the high and low labels was equivalent across groups within a margin of ±0.10 of a level fixed in advance, with every estimated difference within ±0.045. Against a same-length mid label (3.0/6) instead of no label, the low value took 0.06–0.08 more off the work of English learners, economically disadvantaged and disability-identified students on Qwen (also partly the matching artefact; corrected at the reliability implied by the data paper's rater agreement (0.75–0.86), the English-learner difference stays beyond the multiple-testing bar, the economic one only at 0.86, and the disability one at neither). A deployment whose labels track attainment would open a projected 0.01–0.07 of a level through who receives which label. The grader's own gap with no label at all is 0.21–0.32 of a level against English learners and disability-identified students at equal human score. Corrected for matching on a noisy score, 0.15–0.27 remains at equal true quality at that reliability (two expert reads, adjudicated, r = .75 before adjudication), and it would vanish only near 0.5, which that agreement rules out. That is a fairness problem larger than the label's, measured against human raters whose own group neutrality is not tested: whether those raters, who had anti-bias training, marked every group alike at equal quality is the open question. On this evidence the harm of the label is borne by any learner given a false low label rather than concentrated on a protected group; the labels were assigned, and the scope is one corpus, one two-read, adjudicated human score per essay and two models.

## Related Claims

- [Graded exemplars shift an LLM grader by the level they are marked at.](graded-exemplars-shift-an-llm-grader-by-the-level-they-are-marked-at.md) — the contrast: context about the work, which shifts the grade by the level it is marked at
- [Course context helps sparse items and dilutes rich ones.](course-context-helps-sparse-items-and-dilutes-rich-ones.md) — the other context result, and its boundary
- [LLM short-answer graders can reach human rater agreement.](llm-short-answer-graders-can-reach-human-rater-agreement.md) — the agreement these interventions on one model did not detectably move
