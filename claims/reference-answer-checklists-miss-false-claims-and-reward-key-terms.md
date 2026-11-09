---
type: claim
title: Checklists Written From a Reference Answer Miss False Claims and Reward Key Terms
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-11-06
id: reference-answer-checklists-miss-false-claims-and-reward-key-terms
evidence_strength:
embargo: >-
  EMBARGOED — staged in learning-engineering-research (private). Not to be
  published until the embargo on release checklist-grading-2026 lifts.
---

# Checklists Written From a Reference Answer Miss False Claims and Reward Key Terms

> **Claim** · [All claims](index.md)
> **Evidence** · `lazuli-grader-checklist-2026` (embargoed; not yet written into the argument below)

A yes/no checklist written from a reference answer mostly asks whether expected content is present, so content that is added, whether false or irrelevant, falls outside what it checks. When a false sentence was added to a good short answer, an LLM grader's checklist score fell by 17% of the scale against 47% for a Likert rubric. When a sentence naming the right technical terms without understanding was added to a weak answer, the checklist score rose more (35% against 27%).

## Subclaims

- Presence checks ("does the answer say that a stack removes the most recent item first?") still answer YES when a false claim is added, because the expected idea is still there.
- What the checklist did register of a false claim came mainly from error checks, which ask whether the answer avoids a particular mistake: where a checklist had them they carried 76% of its loss. Without them it lost 8% of its scale, where the Likert format lost 44%.
- The key-term gain came entirely from presence checks turning from NO to YES.
- Counted as one vote among several, error checks narrowed the gap but did not close it. Items that cap or veto a score, as in key-features scoring (Page & Bordage, 1995) or "invalidating" criteria in rubric-based rewards (Gunjal et al., 2025), may do better; that remains to be tested.

## Discussion

**Construct terms.** In Messick's terms, the missed false claim is construct underrepresentation and the key-term gain is construct-irrelevant variance. A decomposition of the reference suits a label about coverage (Zhang, 2026), not one that also penalizes errors.

**Practice.** An educator who uses a checklist should write checks for the specific errors and misconceptions that matter, and any new rubric format should be tested with planted errors against a matched neutral sentence before it is trusted.

**Scope.** Two models; the checklists were written by one model from one prompt with no human review; the planted sentences were clear contradictions of the key point, written by one model and checked by another. Subtler errors may be registered less by both formats.

## Related Claims

- [A model-written checklist agrees less with human raters on short answers.](a-model-written-checklist-agrees-less-with-human-raters-on-short-answers.md)
- [Precise yes/no checklists were not shown to make LLM grading more reliable.](precise-yes-no-checklists-do-not-make-llm-grading-more-reliable.md)
