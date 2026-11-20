---
type: claim
title: A Model-Written Yes/No Checklist Agrees Less With Human Raters on Short Answers
status: review
generated:
  by: claude/unspecified
  at: 2026-11-19
id: a-model-written-checklist-agrees-less-with-human-raters-on-short-answers
evidence_strength:
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: porcaro-2026
    resource: "https://doi.org/10.5281/zenodo.24023968"
    title: "David S. Porcaro. (2026). Precise yes/no checklists and an AI grader: reliability, validity, and what a checklist cannot see. Research release checklist-grading-2026 1.0.1, Learning Design Alliance. https://doi.org/10.5281/zenodo.24023968"
    author: David S. Porcaro
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# A Model-Written Yes/No Checklist Agrees Less With Human Raters on Short Answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

On short answers graded against a reference answer, an LLM grader's scores agreed less with human raters when it used a model-written checklist of yes/no checks than when it used a Likert rubric from the same criterion: by 0.106 in correlation with the raters' mean, for both models tested. The checklist gave partly and fully correct answers too little credit, and was not shown to give wrong answers too much.

## Subclaims

- The loss is not explained by noise: both formats gave nearly the same scores on a second grading (test–retest r 0.96 or above).
- The shortfall is largest for partly correct answers, which narrows the distance between partly correct and wrong answers. That is consistent with the lower correlation, though band means do not decompose a correlation.
- A checklist score should not be read on the same scale as a holistic grade: it runs low for good work, so a pass mark set for one format will not transfer to the other.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Precise yes/no checklists and an AI grader: reliability, validity, and what a checklist cannot see. Research release checklist-grading-2026 1.0.1, Learning Design Alliance. https://doi.org/10.5281/zenodo.24023968

`q2 · i?` · `causal · r?`

Two LLM graders (Gemini 3.5 Flash Lite and GPT-5.4 mini) graded 620 undergraduate short answers from a public data-structures corpus in two formats, a Likert rubric and a model-written checklist of yes/no checks, on identical inputs. Agreement with the human raters was the correlation of each format's score with the two raters' mean, read beside the raters' agreement with each other (0.621); a follow-up compared each format's signed error by band of human score. Intervals resample questions; verdicts were registered in advance. Observation record: `lazuli-grader-checklist-2026`.

## Discussion

**What agreement here is, and is not.** Agreement with the human raters is one kind of validity evidence, read beside the raters' agreement with each other (0.621 here). It is not validity itself: the raters are an unreliable reference, which lowers both formats' correlations alike. The planted-error results are a second, independent kind of evidence, and they point the same way.

**Parallels.** Experienced clinicians score lower than residents on OSCE checklists while scoring higher on global ratings (Hodges et al., 1999), and an LLM grader of programs that checked one rubric point per call was harsher than teaching assistants because it withheld partial credit (Pathak et al., 2025).

**Scope.** Two models, one short-answer corpus. On student programs the models tracked the raters too weakly for the formats to be compared.

## Related Claims

- [Precise yes/no checklists were not shown to make LLM grading more reliable.](precise-yes-no-checklists-do-not-make-llm-grading-more-reliable.md)
- [Reference-answer checklists miss false claims and reward key terms.](reference-answer-checklists-miss-false-claims-and-reward-key-terms.md) — the mechanism
