---
type: claim
title: Course Context Raised an LLM Grader's Agreement on Terse Answers and Lowered It on Long Ones
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
id: course-context-helps-sparse-items-and-dilutes-rich-ones
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

# Course Context Raised an LLM Grader's Agreement on Terse Answers and Lowered It on Long Ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Evidence quality** · This claim rests on one research release that has not been peer-reviewed. Its research and writing were carried out by an AI system (Claude Code) under one human author, and its scope audit and reproduction were made by AI agents with no part in the work; no research team independent of the author has reviewed or replicated it. Treat it as a lead to check, not an established finding.

In this release's evidence records and interpretation (the finding is not in its article), course context — the other questions or skills a course covers — raised an LLM grader's agreement on one corpus of terse answers (by 0.022–0.035 in quadratic-weighted kappa) and lowered it on one of long answers (by 0.028–0.034), each in a single run at the edge of the instrument's ±0.02 resolution. The release offers signal density as a candidate reading, a hypothesis to test rather than a finding: surrounding material helps terse answers that carry little signal and dilutes long ones that already carry plenty. Relatedness was not detected to matter. The observation leads; the mechanism is a candidate.

## Subclaims

- On one-or-two-sentence answers, in a single run, sibling questions from the same course module raised agreement (0.703 to 0.738) and moved a harsh grader toward the human on both bias (−0.57 to −0.41) and error (MAE 0.93 to 0.83).
- On long answers, in a single run, adding more skills than the item needs lowered agreement and made the grader more generous (fifteen skills with one relevant: 0.838 to 0.804, bias +0.56 to +0.67). The two effects are of similar size and point opposite ways.
- Sibling questions drawn from *other* parts of the course scored within 0.013 of genuinely related ones, below resolution: a non-detection, not a demonstrated null. A goal graph is therefore not shown to add anything as a graph here, and a representative sample of what the course asks may serve.
- The candidate explanation is how much signal the item itself carries, not the presence or absence of a taxonomy; the release says it is fitted to two data points and offers it as a hypothesis to test per activity type, not as a finding.

## Evidence

### Porcaro 2026

David S. Porcaro. (2026). Reliability, calibration and attack surface of an LLM short-answer grader, measured against three human-graded corpora. Research release ai-grader-reliability-2026 1.0.0, Learning Design Alliance. https://doi.org/10.5281/zenodo.23480844

`q2 · i?` · `causal · r?`

Within-item context arms on the shipped grading prompt, single runs of 150 stratified answers on each of two public corpora: on terse data-structures answers with real curricular structure (Mohler), related sibling questions from the same module against unrelated ones of the same length and against none; on long undergraduate computer-science answers with no goal graph (JorGPT), a parent and four siblings, or fifteen skills with one relevant, against the single skill the product sends. These results are in the release's evidence records and interpretation, not in its article. Observation records: `lazuli-grader-mohler-2026` (supports), `lazuli-grader-jorgpt-2026` (qualifies).

## Discussion

**Scope of the claim, and why it is stated as a boundary condition.** Two corpora gave opposite answers, each in a single run by a margin at the edge of the measuring instrument's resolution. That rules out reporting either direction as the finding. The reconciling account — that surrounding questions tell the grader what this course is and what level it pitches at, which a sparse item cannot convey on its own and a rich one does not need — fits both results, but it is an interpretation fitted to two data points rather than a tested mechanism.

**The negative result inside it is the more useful one for system design.** The arm holding length and shape constant while varying only relatedness moved the score by less than the instrument can resolve. So the intuition that a structured goal graph gives the grader something a flat list cannot is not shown: related and unrelated siblings did not differ detectably (0.013, a single run), so a representative sample of the course's questions may serve as well. That is much cheaper to supply and does not depend on the graph being correct.

**How this should be settled rather than assumed.** It is testable per activity type: a short-answer check and an extended written response are different regimes, and the rule as stated predicts they want different amounts of context. Setting one global context policy for all of them is the thing this claim argues against, in either direction.

**A caveat specific to the dilution half.** The corpus that produced it has no curricular structure, so its "sibling" arm was built from unrelated questions — which makes that arm partly a second dilution arm rather than a test of hierarchy. The corpus with real structure was used to test that properly, and the sign flipped.

## Related Claims

- [Showing an LLM grader a learner's prior performance biases the grade.](showing-a-grader-a-learners-prior-performance-biases-the-grade.md) — context about the learner, which moves the mark on identical work
- [Graded exemplars shift an LLM grader by the level they are marked at.](graded-exemplars-shift-an-llm-grader-by-the-level-they-are-marked-at.md) — a targeted form of task context, which shifts the grade by its marked level
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the analogous trade in human readers, and a caution against pressing the analogy
