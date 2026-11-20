---
type: claim
title: Precise Yes/No Checklists Were Not Shown to Make LLM Grading More Reliable
status: review
generated:
  by: claude/unspecified
  at: 2026-11-19
id: precise-yes-no-checklists-do-not-make-llm-grading-more-reliable
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

# Precise Yes/No Checklists Were Not Shown to Make LLM Grading More Reliable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

Replacing a Likert rubric with a checklist of precise yes/no checks, written by a model from the same criterion and scored as the share of YES, was not shown to make two LLM graders' scores more consistent. On short answers graded against a reference, both formats already gave nearly the same scores on a second grading (test–retest r 0.96 to 0.99), so a checklist had almost no room to help. On student programs, where the models were far less consistent, the checklist was less reliable wherever the data clearly showed a difference.

## Subclaims

- The reliability gains reported for checklists, for human raters and LLM judges alike, were measured where agreement started low. An LLM grading short answers against a reference answer does not start low.
- A checklist score has fewer possible values than a fine rating scale, and a coarser score loses repeatability on its own. A small reliability difference in favor of the rating scale can come from the scale alone, so it is not evidence that checklists make judgments less consistent.
- On programs, part of the checklist's loss in agreement between models came from one model answering YES to nearly every check, so its scores barely varied.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Precise yes/no checklists and an AI grader: reliability, validity, and what a checklist cannot see. Research release checklist-grading-2026 1.0.1, Learning Design Alliance. https://doi.org/10.5281/zenodo.24023968

`q2 · i?` · `causal · r?`

Two LLM graders (Gemini 3.5 Flash Lite and GPT-5.4 mini) graded the same work twice in each of two formats, a Likert rubric and a model-written checklist of yes/no checks scored as the share of YES: 620 undergraduate short answers from a public data-structures corpus and 226 first-year Java programs from a public corpus, each with independent human grades. Reliability was the correlation between a model's two gradings (test–retest) and between the two models' scores, compared between formats with intervals resampling questions or submissions and verdicts registered before any model call. Observation record: `lazuli-grader-checklist-2026`.

## Discussion

**Scope.** Two small, inexpensive models (Gemini 3.5 Flash Lite and GPT-5.4 mini), one short-answer corpus and one corpus of first-year Java programs. The claim is about model-written checklists of this kind read by an LLM grader, not about human raters using checklists, which is the setting of the health-evaluation framework that prompted the comparison (Mallinar et al., 2026).

**What would change it.** A model whose Likert grading is far less consistent than these, on work where a checklist's checks can each be answered reliably, is where a checklist could still help; that was not tested.

## Related Claims

- [A model-written checklist agrees less with human raters on short answers.](a-model-written-checklist-agrees-less-with-human-raters-on-short-answers.md) — consistency did not improve, and agreement with the raters fell
- [Reference-answer checklists miss false claims and reward key terms.](reference-answer-checklists-miss-false-claims-and-reward-key-terms.md) — what the checklist could not see
- [Pooling repeated LLM grades does not improve agreement on short answers.](pooling-repeated-llm-grades-does-not-improve-agreement.md) — the same ceiling, reached by a different route
