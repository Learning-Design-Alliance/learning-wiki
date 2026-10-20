---
type: claim
title: Delimiting Untrusted Learner Text Defeats Authority-Claim Injection
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: delimiting-untrusted-learner-text-defeats-authority-claim-injection
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

# Delimiting Untrusted Learner Text Defeats Authority-Claim Injection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

An AI grader that interpolates a learner's answer into its prompt without a boundary can be made to inflate the grade by appending a sentence claiming the work has already been approved — and wrapping the answer in a per-submission unguessable marker reduces it from 90% of attempts inflated (+4.6 mean) to 8% (−0.42 mean), where instructing the model to resist it does not. Measured on one model and one payload family, 50 answers per arm, in a single run; the deployed defence has not been re-measured.

## Subclaims

- The successful attack does not look like an attack. Overt payloads — "ignore all previous instructions", a forged rubric, a plea — are penalised or ignored; the one that works is written in the register of a legitimate annotation.
- Instructing a model to treat the response as untrusted is a mitigation rather than a fix: in the measurements available it more than halved the average gain (+2.19 against +4.60) and still left the majority of attempts succeeding (68%).
- A structural defence works because the learner cannot forge a delimiter they have never seen. The property is about what is possible, not about what the model is persuaded to do; 8% of attempts still inflated, by at most one point.
- A prompt's documented penalty for manipulation is not evidence that the penalty fires. Here it fired on none of the successful attacks while firing reliably on the obvious ones.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `causal · r?`

Adversarial payloads appended to 50 real answers from a public, teacher-graded corpus of undergraduate computer-science answers, graded by one model under three prompt arms (the shipped prompt, an added instruction that the response is untrusted, and the response wrapped in a per-submission unguessable marker), so the graded content is identical across arms and any movement is the payload's. A single run. These results are in the release's evidence records and interpretation, not in its article. Observation record: `lazuli-grader-jorgpt-2026`.

## Discussion

**Scope of the claim.** Measured on one model and one grading prompt, with payloads appended to real answers so that the graded content is identical across arms and any movement is attributable to the payload. The specific rates are properties of a particular model's instruction-following as much as of the prompt, and should not be carried across providers. The structural argument is not model-specific.

**Why the failure mode is a design flaw rather than a model weakness.** When untrusted text is interpolated as an undelimited blob, nothing in the prompt distinguishes the learner's words from a claim about *who is speaking*. The model is not being fooled by a clever argument; it is being given a document in which a sentence of provenance metadata is indistinguishable from content. No amount of instruction repairs an ambiguity in the input format — and a defence that works by persuasion degrades silently, because the next payload phrased slightly differently is a new experiment.

**Why this belongs in a learning-design knowledge base and not only in a security tracker.** Any assessment scored by a model whose input includes learner-authored text has this surface, and it is not exotic: the successful payload is one sentence that an ordinary person might discover by accident while trying to add a note for their instructor. Where a grade gates progression, certification or credit, the integrity of the assessment depends on a property of the prompt's input format that nobody reviewing the rubric would think to check.

**The generalisation worth keeping.** Where a system reads text authored by someone with an interest in the outcome, the boundary between that text and the instructions must be unforgeable rather than merely stated. That is the same principle as parameterised queries, and the argument for it is the same: it removes a class of attack instead of raising the cost of one instance.

## Related Claims

- [LLM short-answer graders can reach human rater agreement.](llm-short-answer-graders-can-reach-human-rater-agreement.md) — accuracy is not the only property an assessment needs
- [Surface formatting changes shift LLM grades without penalising them.](surface-formatting-changes-shift-llm-grades-without-penalising-them.md) — the other way the same grade moves without the work changing
