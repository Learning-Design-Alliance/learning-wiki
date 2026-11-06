---
type: claim
title: Precise Yes/No Checklists Were Not Shown to Make LLM Grading More Reliable
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-11-06
id: precise-yes-no-checklists-do-not-make-llm-grading-more-reliable
evidence_strength:
embargo: >-
  EMBARGOED — staged in learning-engineering-research (private). Not to be
  published until the embargo on release checklist-grading-2026 lifts.
---

# Precise Yes/No Checklists Were Not Shown to Make LLM Grading More Reliable

> **Claim** · [All claims](index.md)
> **Evidence** · `lazuli-grader-checklist-2026` (embargoed; not yet written into the argument below)

Replacing a Likert rubric with a checklist of precise yes/no checks, written by a model from the same criterion and scored as the share of YES, was not shown to make two LLM graders' scores more consistent. On short answers graded against a reference, both formats already gave nearly the same scores on a second grading (test–retest r 0.96 to 0.99), so a checklist had almost no room to help. On student programs, where the models were far less consistent, the checklist was less reliable wherever the data clearly showed a difference.

## Subclaims

- The reliability gains reported for checklists, for human raters and LLM judges alike, were measured where agreement started low. An LLM grading short answers against a reference answer does not start low.
- A checklist score has fewer possible values than a fine rating scale, and a coarser score loses repeatability on its own. A small reliability difference in favor of the rating scale can come from the scale alone, so it is not evidence that checklists make judgments less consistent.
- On programs, part of the checklist's loss in agreement between models came from one model answering YES to nearly every check, so its scores barely varied.

## Discussion

**Scope.** Two small, inexpensive models (Gemini 3.5 Flash Lite and GPT-5.4 mini), one short-answer corpus and one corpus of first-year Java programs. The claim is about model-written checklists of this kind read by an LLM grader, not about human raters using checklists, which is the setting of the health-evaluation framework that prompted the comparison (Mallinar et al., 2026).

**What would change it.** A model whose Likert grading is far less consistent than these, on work where a checklist's checks can each be answered reliably, is where a checklist could still help; that was not tested.

## Related Claims

- [A model-written checklist agrees less with human raters on short answers.](a-model-written-checklist-agrees-less-with-human-raters-on-short-answers.md) — consistency did not improve, and agreement with the raters fell
- [Reference-answer checklists miss false claims and reward key terms.](reference-answer-checklists-miss-false-claims-and-reward-key-terms.md) — what the checklist could not see
- [Pooling repeated LLM grades does not improve agreement on short answers.](pooling-repeated-llm-grades-does-not-improve-agreement.md) — the same ceiling, reached by a different route
