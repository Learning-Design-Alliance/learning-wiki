---
type: claim
title: LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)
description: LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)
id: llm-difficulty-labels-fail-to-predict-empirical-item-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yuan-an-2026
    resource: "https://doi.org/10.48550/arxiv.2609.27063"
    title: "Yuan An, Lei Wang. (2026). Student Use of LLMs and the Limits of AI-Generated Question Difficulty in Data Science Courses. https://arxiv.org/abs/2609.27063 [doi:10.48550/arxiv.2609.27063](https://doi.org/10.48550/arxiv.2609.27063)"
    author: Yuan An, Lei Wang
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` The LLM-assigned difficulty label showed no meaningful correlation with empirical item difficulty measured from 7,888 student responses, and assigned Bloom levels performed similarly. [→ Yuan An 2026](#yuan-an-2026)

## Evidence

### Yuan An 2026

Yuan An, Lei Wang. (2026). Student Use of LLMs and the Limits of AI-Generated Question Difficulty in Data Science Courses. https://arxiv.org/abs/2609.27063 [doi:10.48550/arxiv.2609.27063](https://doi.org/10.48550/arxiv.2609.27063)

`q2 · i?` · `associational · r2`

Construct-validity audit (Stage 2) of 311 deployed LLM-generated MCQs in two data science courses, correlating features and labels with empirical difficulty (1−p) from student responses. The audit found "no meaningful correlation with empirical difficulty (ρ= 0.06)" for labels and ρ= 0.02 for Bloom levels.

> "The LLM-assigned difficulty label showed no meaningful correlation with empirical difficulty (ρ= 0.06), and assigned Bloom levels showed similar results (ρ= 0.02)."

## Discussion

## Related Claims

- [AI-generated assessment items frequently need faculty correction, supporting AI as a draft generator within quality assurance](genai-assessment-items-draft-generator-quality-assurance.md) — the general claim this finding bears on, with the studies behind it

- [Students perform better overall on LOCS exam questions than on HOCS exam questions](locs-exam-questions-outperform-hocs.md) — the general claim this finding bears on, with the studies behind it
- [LLM-generated difficulty ratings show only moderate rank alignment with empirical student performance on basic arithmetic items](llm-difficulty-moderate-rank-alignment-arithmetic.md) — reports the opposite
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [LLM difficulty labels track structural question features: stem length, option length, and digits in stems rise monotonically across Easy, Medium, and Hard labels](llm-difficulty-labels-track-structural-item-features.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [LLM-generated retrieval practice was practical to deploy and well received, but high correctness rates (about 70% of items at p=1.0) restricted score variance](llm-generated-retrieval-practice-deployable-but-high-accuracy-limits-variance.md) — related
- [A 50-disposable-account staging rehearsal produced 56 evidence rows, with 46 (82.1%) assigned to higher-order Bloom categories](fifty-account-rehearsal-56-rows-82-percent-higher-order.md) — related
