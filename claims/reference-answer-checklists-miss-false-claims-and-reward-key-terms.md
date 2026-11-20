---
type: claim
title: Checklists Written From a Reference Answer Miss False Claims and Reward Key Terms
status: review
generated:
  by: claude/unspecified
  at: 2026-11-19
id: reference-answer-checklists-miss-false-claims-and-reward-key-terms
evidence_strength:
newest_evidence: 2026
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

# Checklists Written From a Reference Answer Miss False Claims and Reward Key Terms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

A yes/no checklist written from a reference answer mostly asks whether expected content is present, so content that is added, whether false or irrelevant, falls outside what it checks. When a false sentence was added to a good short answer, an LLM grader's checklist score fell by 17% of the scale against 47% for a Likert rubric. When a sentence naming the right technical terms without understanding was added to a weak answer, the checklist score rose more (35% against 27%).

## Subclaims

- Presence checks ("does the answer say that a stack removes the most recent item first?") still answer YES when a false claim is added, because the expected idea is still there.
- What the checklist did register of a false claim came mainly from error checks, which ask whether the answer avoids a particular mistake: where a checklist had them they carried 76% of its loss. Without them it lost 8% of its scale, where the Likert format lost 44%.
- The key-term gain came entirely from presence checks turning from NO to YES.
- Counted as one vote among several, error checks narrowed the gap but did not close it. Items that cap or veto a score, as in key-features scoring (Page & Bordage, 1995) or "invalidating" criteria in rubric-based rewards (Gunjal et al., 2025), may do better; that remains to be tested.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Precise yes/no checklists and an AI grader: reliability, validity, and what a checklist cannot see. Research release checklist-grading-2026 1.0.1, Learning Design Alliance. https://doi.org/10.5281/zenodo.24023968

`q2 · i?` · `causal · r?`

A false sentence was appended to 120 short answers the raters scored highly, and a sentence naming the reference answer's technical terms without understanding to 112 they scored low, each against a neutral sentence of matched length on the same answer; two LLM graders (Gemini 3.5 Flash Lite and GPT-5.4 mini) scored every version twice in a Likert format and with a model-written checklist. The checklist's change was split by check type, checks asking whether the answer avoids a particular mistake against checks asking whether expected content is present. Planted sentences were written by one model and checked by another, not by a person. Observation record: `lazuli-grader-checklist-2026`.

## Discussion

**Construct terms.** In Messick's terms, the missed false claim is construct underrepresentation and the key-term gain is construct-irrelevant variance. A decomposition of the reference suits a label about coverage (Zhang, 2026), not one that also penalizes errors.

**Practice.** An educator who uses a checklist should write checks for the specific errors and misconceptions that matter, and any new rubric format should be tested with planted errors against a matched neutral sentence before it is trusted.

**Scope.** Two models; the checklists were written by one model from one prompt with no human review; the planted sentences were clear contradictions of the key point, written by one model and checked by another. Subtler errors may be registered less by both formats.

## Related Claims

- [A model-written checklist agrees less with human raters on short answers.](a-model-written-checklist-agrees-less-with-human-raters-on-short-answers.md)
- [Precise yes/no checklists were not shown to make LLM grading more reliable.](precise-yes-no-checklists-do-not-make-llm-grading-more-reliable.md)
