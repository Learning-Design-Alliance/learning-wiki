---
type: claim
title: "Candidate selection is a second bottleneck: an oracle ranker over proposed candidates substantially raises proportional match, and plausibility checks reject some valid distractors"
description: "Candidate selection is a second bottleneck: an oracle ranker over proposed candidates substantially raises proportional match, and plausibility checks reject some valid distractors"
id: candidate-selection-loss-oracle-ranker
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yanick-zengaffinen-2026
    resource: "https://doi.org/10.48550/arxiv.2603.15547"
    title: "Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547 [doi:10.48550/arxiv.2603.15547](https://doi.org/10.48550/arxiv.2603.15547)"
    author: Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: yanick-zengaffinen-2026-2
    resource: "https://arxiv.org/abs/2603.15547"
    title: "Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547"
    author: Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: qualitative
    rigour: 3
---

# Candidate selection is a second bottleneck: an oracle ranker over proposed candidates substantially raises proportional match, and plausibility checks reject some valid distractors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` An oracle ranker raises DEEPSEEK-V3.2's proportional match from 0.52 to 0.67 on Eedi and from 0.14 to 0.29 on SciQ, showing the model proposes valid distractors it then discards. [→ Yanick Zengaffinen 2026](#yanick-zengaffinen-2026)
`q2 i?` The model argues against keeping 28% of candidates matching human-authored distractors on Eedi and 15% on SciQ, though the checks reject invalid candidates 1.5–1.9× as often as valid ones. [→ Yanick Zengaffinen 2026 (2)](#yanick-zengaffinen-2026-2)

## Evidence

### Yanick Zengaffinen 2026

Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547 [doi:10.48550/arxiv.2603.15547](https://doi.org/10.48550/arxiv.2603.15547)

`q2 · i?` · `causal · r2`

Oracle-ranker analysis in the failure-mode section: each annotated INST candidate is matched against the human-authored set, and the gap to the final set quantifies selection loss. Significant under paired t-test, p<10−7; no effect size printed.

> "The oracle raises DEEPSEEK-V3.2’s proportional match from 0.52 to 0.67 on Eedi and from 0.14 to 0.29 on SciQ (paired t-test, p <10−7), recovering about a third of the otherwise-missed distractors on Eedi and a sixth on SciQ."

### Yanick Zengaffinen 2026 (2)

Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547

`q2 · i?` · `qualitative · r3`

Trace-level classification of plausibility and discriminability checks arguing for or against keeping each candidate; the article adds that the checks do discriminate, rejecting invalid candidates 1.5–1.9× as often as valid ones.

> "we find that the model argues against keeping 28% of the candidates that match human-authored ones on Eedi and 15% on SciQ under DEEPSEEK-V3.2 (the same pattern holds for GLM-4.7)"

## Discussion

## Related Claims

- [AI-generated assessment items frequently need faculty correction, supporting AI as a draft generator within quality assurance](genai-assessment-items-draft-generator-quality-assurance.md) — the general claim this finding bears on, with the studies behind it
- [Providing the correct solution in the prompt improves LLM alignment with human-authored distractors, confirming correct-solution recovery as a primary bottleneck](correct-solution-in-prompt-bottleneck.md) — related
- [On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design](llms-solve-first-error-injection-edi.md) — related
- [Providing baselines with oracle knowledge-concept selection substantially improves their performance, identifying concept selection as a key bottleneck, though baselines with oracle KCs still trail KT4EQG](concept-selection-bottleneck-baselines.md) — related
