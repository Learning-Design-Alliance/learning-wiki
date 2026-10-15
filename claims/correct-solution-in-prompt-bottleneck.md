---
type: claim
title: Providing the correct solution in the prompt improves LLM alignment with human-authored distractors, confirming correct-solution recovery as a primary bottleneck
description: Providing the correct solution in the prompt improves LLM alignment with human-authored distractors, confirming correct-solution recovery as a primary bottleneck
id: correct-solution-in-prompt-bottleneck
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
---

# Providing the correct solution in the prompt improves LLM alignment with human-authored distractors, confirming correct-solution recovery as a primary bottleneck

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Providing the correct answer in the prompt improves proportional match on Eedi (0.52±0.03→0.56±0.03) and SciQ (0.14±0.02→0.18±0.03), relative improvements of 6.4% and 30.7%. [→ Yanick Zengaffinen 2026](#yanick-zengaffinen-2026)

## Evidence

### Yanick Zengaffinen 2026

Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547 [doi:10.48550/arxiv.2603.15547](https://doi.org/10.48550/arxiv.2603.15547)

`q2 · i?` · `causal · r2`

Prompting experiment in the failure-mode analysis section: DEEPSEEK-V3.2 and GLM-4.7 run with and without the correct answer supplied. Both improvements are significant under a paired t-test, p<0.01, per the article's footnote; no effect size is printed.

> "Providing the correct answer to the MCQ in the prompt improves proportional match on both Eedi (0.52±0.03→0.56±0.03 ) and SciQ (0.14±0.02→0.18±0.03"

## Discussion


## Related Claims
- [Candidate selection is a second bottleneck: an oracle ranker over proposed candidates substantially raises proportional match, and plausibility checks reject some valid distractors](candidate-selection-loss-oracle-ranker.md) — related
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
- [On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design](llms-solve-first-error-injection-edi.md) — related
