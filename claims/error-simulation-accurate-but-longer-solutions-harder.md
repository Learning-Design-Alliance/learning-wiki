---
type: claim
title: LLM error simulation rarely fails, but the model is less likely to reproduce a targeted distractor on problems with longer correct solutions
description: LLM error simulation rarely fails, but the model is less likely to reproduce a targeted distractor on problems with longer correct solutions
id: error-simulation-accurate-but-longer-solutions-harder
status: draft
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
    kind: associational
    rigour: 1
---

# LLM error simulation rarely fails, but the model is less likely to reproduce a targeted distractor on problems with longer correct solutions

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r2`, 1 associational `r1` · `q2`

## Subclaims
`q2 i?` When prompted to simulate a problem-specific student error, DEEPSEEK-V3.2 achieves a mean accuracy of 0.92±0.02 against any faithful interpretation of the error. [→ Yanick Zengaffinen 2026](#yanick-zengaffinen-2026)
`q2 i?` Where the targeted distractor was not produced, the underlying problems tend to have longer correct solutions (p<0.05, Mann-Whitney U test). [→ Yanick Zengaffinen 2026 (2)](#yanick-zengaffinen-2026-2)

## Evidence

### Yanick Zengaffinen 2026

Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547 [doi:10.48550/arxiv.2603.15547](https://doi.org/10.48550/arxiv.2603.15547)

`q2 · i?` · `causal · r2`

Targeted error-simulation test over Eedi's 429 misconception-annotated problems, manually verified; the article notes this does not guarantee the most plausible interpretation is selected, as only 62% of faithful distractors appear in the human-authored set.

> "When prompted to simulate a problem-specific student error (sampled from Eedi’s misconception annotations for each of the 429 problems), DEEPSEEK-V3.2 achieves a mean accuracy of 0.92±0.02 , manually verified against any faithful interpretation of the error"

### Yanick Zengaffinen 2026 (2)

Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547

`q2 · i?` · `associational · r1`

Secondary comparison of solution step counts for problems where the targeted distractor was versus was not produced; only a p-value is printed, so no effect size is reported.

> "the underly- ing problems tend to have longer correct solutions (p <0.05, Mann-Whitney U test, comparing so- lution step counts), suggesting the model is less likely to reproduce the targeted distractor on prob- lems with longer solutions."

## Discussion


## Related Claims
- [LLM distractor-generation strategies differ by domain: error description and simulation dominate on math while conceptual linking and discriminability checks dominate on science](domain-shift-link-versus-error-strategies.md) — related
- [On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design](llms-solve-first-error-injection-edi.md) — related
- [Instruction-tuning a student model on a single misconception overgeneralizes the error across problems and degrades correct-solving accuracy](student-model-misconception-overgeneralization-degrades-accuracy.md) — related
- [Cognitive modeling of exact student responses is hardest for multi-select problems and rare-error answers, with select-all accuracy of only 12-15% and cognitive accuracy dropping to as low as 3.7% when answers are incorrect](cognitive-modeling-by-problem-type.md) — related
