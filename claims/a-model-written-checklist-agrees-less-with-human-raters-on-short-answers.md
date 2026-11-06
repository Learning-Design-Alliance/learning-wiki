---
type: claim
title: A Model-Written Yes/No Checklist Agrees Less With Human Raters on Short Answers
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-11-06
id: a-model-written-checklist-agrees-less-with-human-raters-on-short-answers
evidence_strength:
embargo: >-
  EMBARGOED — staged in learning-engineering-research (private). Not to be
  published until the embargo on release checklist-grading-2026 lifts.
---

# A Model-Written Yes/No Checklist Agrees Less With Human Raters on Short Answers

> **Claim** · [All claims](index.md)
> **Evidence** · `lazuli-grader-checklist-2026` (embargoed; not yet written into the argument below)

On short answers graded against a reference answer, an LLM grader's scores agreed less with human raters when it used a model-written checklist of yes/no checks than when it used a Likert rubric from the same criterion: by 0.106 in correlation with the raters' mean, for both models tested. The checklist gave partly and fully correct answers too little credit, and was not shown to give wrong answers too much.

## Subclaims

- The loss is not explained by noise: both formats gave nearly the same scores on a second grading (test–retest r 0.96 or above).
- The shortfall is largest for partly correct answers, which narrows the distance between partly correct and wrong answers. That is consistent with the lower correlation, though band means do not decompose a correlation.
- A checklist score should not be read on the same scale as a holistic grade: it runs low for good work, so a pass mark set for one format will not transfer to the other.

## Discussion

**What agreement here is, and is not.** Agreement with the human raters is one kind of validity evidence, read beside the raters' agreement with each other (0.621 here). It is not validity itself: the raters are an unreliable reference, which lowers both formats' correlations alike. The planted-error results are a second, independent kind of evidence, and they point the same way.

**Parallels.** Experienced clinicians score lower than residents on OSCE checklists while scoring higher on global ratings (Hodges et al., 1999), and an LLM grader of programs that checked one rubric point per call was harsher than teaching assistants because it withheld partial credit (Pathak et al., 2025).

**Scope.** Two models, one short-answer corpus. On student programs the models tracked the raters too weakly for the formats to be compared.

## Related Claims

- [Precise yes/no checklists were not shown to make LLM grading more reliable.](precise-yes-no-checklists-do-not-make-llm-grading-more-reliable.md)
- [Reference-answer checklists miss false claims and reward key terms.](reference-answer-checklists-miss-false-claims-and-reward-key-terms.md) — the mechanism
