---
type: claim
title: A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright
description: A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright
id: llm-grader-strict-persona-collapse
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: habibullah-2026
    resource: "https://doi.org/10.48550/arxiv.2609.29333"
    title: "Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333 [doi:10.48550/arxiv.2609.29333](https://doi.org/10.48550/arxiv.2609.29333)"
    author: "Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Prepending a strict persona to the best prompt pushes 14 of 17 open-weights models above the graded band (MAE rising ×1.69 to ×7.11), with Llama-3.1-8B and Mistral-Small-24B awarding 0.00/35 on average. [→ Habibullah 2026](#habibullah-2026)
`q2 i?` Parameter count does not order the damage: the strict/neutral MAE ratio correlates with size at ρ=−0.21 (p=0.42), with opposite directions across matched rungs of GLM and Gemma. [→ Habibullah 2026](#habibullah-2026)

## Evidence

### Habibullah 2026

Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333 [doi:10.48550/arxiv.2609.29333](https://doi.org/10.48550/arxiv.2609.29333)

`q2 · i?` · `causal · r2`

Full-cohort configuration-grid evaluation on the CV exam (570 dual-graded students, 35-point base scale), comparing each model's strict and neutral runs identical bar the persona sentence. The quote fragment "14 of the 17 config-matched pairs out of the graded band" states the headline result; three models stop grading outright.

> "Prepending a short “strict grader” preamble to the otherwise-best prompt takes 14 of the 17 config-matched pairs out of the graded band, all six families represented, MAE rising×1.69 to×7.11."

## Discussion


## Related Claims
- [Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64](closed-llm-graders-below-human-floor.md) — related
- [The strict-persona vulnerability replicates on an independent machine-learning exam, but its direction is exam-specific: seven of 17 models improve because the persona cancels their over-marking](strict-persona-effect-exam-specific.md) — related
- [The strict-persona collapse is attributed to the preamble's two credit-withholding policy sentences, not its harsh tone, with S2 alone causing refusal in two models](strict-preamble-policy-sentence-attribution.md) — related
- [One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas](lora-finetuning-llm-grader-parity.md) — related
- [Grading skill transfers across exams: an adapter fine-tuned on one exam improves grading on the unseen other, though transfer stops short of in-domain performance](grading-skill-transfers-across-exams.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
