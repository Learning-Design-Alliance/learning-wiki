---
type: claim
title: On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design
description: On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design
id: llms-solve-first-error-injection-edi
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yanick-zengaffinen-2026
    resource: "https://doi.org/10.48550/arxiv.2603.15547"
    title: "Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547 [doi:10.48550/arxiv.2603.15547](https://doi.org/10.48550/arxiv.2603.15547)"
    author: Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
---

# On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On Eedi, models construct a step-by-step solution first in 95.2% of traces on average, and among these diverge at a specific step to inject an error in 73.8% of cases. [→ Yanick Zengaffinen 2026](#yanick-zengaffinen-2026)

## Evidence

### Yanick Zengaffinen 2026

Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547 [doi:10.48550/arxiv.2603.15547](https://doi.org/10.48550/arxiv.2603.15547)

`q2 · i?` · `qualitative · r2`

Targeted trace-level analysis reported in the discussion section (pointing to Appendix C.1) of LLM reasoning traces on Eedi; the article states similarity-based strategies are rare (≈3% of traces) and confined to settings such as rounding or magnitude-estimation problems.

> "models construct a step-by-step solution first in 95.2% of traces on average across models, and among these solve-first traces, diverge at a specific step to inject an error in 73.8% of cases"

## Discussion


## Related Claims
- [Providing the correct solution in the prompt improves LLM alignment with human-authored distractors, confirming correct-solution recovery as a primary bottleneck](correct-solution-in-prompt-bottleneck.md) — related
- [LLM distractor-generation strategies differ by domain: error description and simulation dominate on math while conceptual linking and discriminability checks dominate on science](domain-shift-link-versus-error-strategies.md) — related
- [LLM error simulation rarely fails, but the model is less likely to reproduce a targeted distractor on problems with longer correct solutions](error-simulation-accurate-but-longer-solutions-harder.md) — related
- [LLM-generated ideas diverge from lesson ideas in grounding, misconception substance, vocabulary, uncertainty markers, and analogy use](llm-idea-divergence-patterns-qualitative.md) — related
- [Candidate selection is a second bottleneck: an oracle ranker over proposed candidates substantially raises proportional match, and plausibility checks reject some valid distractors](candidate-selection-loss-oracle-ranker.md) — related
- [Instruction-tuning a student model on a single misconception overgeneralizes the error across problems and degrades correct-solving accuracy](student-model-misconception-overgeneralization-degrades-accuracy.md) — related
- [Step-by-step automated annotations accelerated correction of procedural misconceptions, with intervention students rectifying fundamental errors weeks before control peers](automated-annotations-accelerate-misconception-correction.md) — related
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
- [LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select](llm-distractor-prediction-asymmetry.md) — related
