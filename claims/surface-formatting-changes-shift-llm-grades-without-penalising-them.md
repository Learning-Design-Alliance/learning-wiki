---
type: claim
title: Surface Formatting Changes Shift LLM Grades, With No Consistent Penalty Detected
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: surface-formatting-changes-shift-llm-grades-without-penalising-them
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

# Surface Formatting Changes Shift LLM Grades, With No Consistent Penalty Detected

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

In this release's evidence records and interpretation (the finding is not in its article), reformatting an answer without changing its words moved the grade a level in about two cases in five on matched answers (39%, against 25% for re-grading identical text; 17–37% across seven variants at n = 30 each), with no consistent direction across variants and no intervals. The release reads it as a shift in where the grader settles rather than a penalty for any particular style, and on matched cases it was larger than the noise of simply grading the same text twice. One model, single runs; no penalty was detected, which is not the same as showing there is none.

## Subclaims

- No penalty was detected for bullets, lowercase starts, or one-line-per-sentence layout: signed changes run from −0.10 to +0.22 across variants with no consistent direction, at n = 30 each and with no interval, which cannot show that any one variant's mean is zero.
- The movement is not merely re-sampling. On matched cases, reformatting moves the grade more than twice as far as re-grading byte-identical text does (mean absolute change 0.46 against 0.21).
- Averaging repeated grades did not remove it: a median of three grades left 37% of reformatted cases moving a level, against 39% for a single grade, which the release attributes to the reformat shifting the grader's centre rather than adding noise around it.
- Grading byte-identical text twice already lands on a different integer level about a quarter of the time, which is the floor any account of this has to start from.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `causal · r?`

Layout-only edits that keep every word and its order (whitespace, one paragraph, one line per sentence, bullets, lowercased sentence starts, final punctuation, and a typo variant) applied to answers from a public, teacher-graded corpus of undergraduate computer-science answers, graded by one model against a re-grade of the byte-identical text on the same 100 answers, with a seven-variant sweep at n = 30 each and a full-corpus scan for identical answers from different students. Single runs. These results are in the release's evidence records and interpretation, not in its article. Observation record: `lazuli-grader-jorgpt-2026`.

## Discussion

**Scope of the claim.** The perturbations tested preserve the words and their order exactly; only layout, capitalisation and punctuation vary. Variants that alter characters as well as layout behave about the same, so the sensitivity is not specific to whitespace. Nothing here speaks to substantive edits, where a real grade change and a noise flip are inseparable by construction.

**Why "no penalty detected" matters as much as "it moves".** The complaint a learner makes is directional — they reformatted and the mark went *down*. That happens (10–30% of cases per variant moved down), and marks also go up, with no consistent direction detected across variants. On the release's reading the fix is therefore not a formatting-invariance instruction or a style rule for learners, but not re-grading unchanged words at all.

**The fix that follows is architectural rather than prompt-level.** Key the grade on a normalised content signature — words in order, case and punctuation stripped — and return the stored grade when a learner resubmits the same words. In the measurement every layout-only variant hit such a signature, and the typo variant, which changes a word, correctly did not. It also removes the cost of the re-grade.

**One non-obvious constraint on that fix.** The cache must be keyed per learner and never shared on content alone. In the corpus measured, 2% of answers were identical text from *different* students, and the human graded 15 of those 18 groups differently — mostly crediting one and zeroing the rest. An integrity judgement is about provenance, not content, so a content-only cache would hand the credited grade to the student who was zeroed.

**What is left over.** Residual movement on genuinely edited resubmissions stays. The release's working record names two options there: a better model and showing bands rather than false-precision points.

## Related Claims

- [Pooling repeated LLM grades does not improve agreement on short answers.](pooling-repeated-llm-grades-does-not-improve-agreement.md) — the intervention this rules out, and why
- [LLM short-answer graders agree with one human rater more, and the other less, than the two raters agree with each other.](llm-short-answer-graders-can-reach-human-rater-agreement.md) — stability and agreement are separate properties
- [Fluent illusions mislead self-assessment.](fluent-illusions-mislead-self-assessment.md) — surface fluency affecting judgement, in human readers
