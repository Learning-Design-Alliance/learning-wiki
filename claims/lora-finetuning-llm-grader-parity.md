---
type: claim
title: "One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas"
description: "One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas"
id: lora-finetuning-llm-grader-parity
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
    i: 3
    kind: causal
    rigour: 2
  - id: habibullah-2026-2
    resource: "https://arxiv.org/abs/2609.29333"
    title: "Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333"
    author: "Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` With the pooled marks adapter, every fine-tuned model grades as well as a human or better on both exams; the pooled adapter is significantly better in 9 of 10 model×exam cells (d from −0.94 to −1.13 on the ML exam). [→ Habibullah 2026](#habibullah-2026)
`q2 i?` Persona sensitivity nearly vanishes: pooled adapters move at most +0.32 MAE (marks recipe) across three harsh personas on both exams, where base models move up to 20 MAE points. [→ Habibullah 2026 (2)](#habibullah-2026-2)

## Evidence

### Habibullah 2026

Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333 [doi:10.48550/arxiv.2609.29333](https://doi.org/10.48550/arxiv.2609.29333)

`q2 · i3` · `causal · r2`

LoRA fine-tuning of five open models (4B–30B) on seed-fixed 80/20 student splits, evaluated on held-out students with a paired third-grader test. The printed paired effect sizes are large (d from −0.94 to −1.13 on the ML exam); the pooled fine-tune "lands at 1.75–2.01 MAE on the CV exam and 3.29–3.53 on the ML exam (marks recipe; Table 1)".

> "The pooled marks adapter is significantlybetterin 9 of 10 (model× exam) cells: all five models on the ML exam (d from−0.94 to−1.13, every CI below zero) and four of five on the CV ."

### Habibullah 2026 (2)

Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333

`q2 · i?` · `causal · r2`

Persona sweep re-run for base and pooled models on both exams. Bases reproduce the collapse (Qwen2.5-Coder-14B goes 4.06→23.81 under strict on the CV exam), while under a neutral prompt the worst base mis-grades 43 of 114 CV-exam students by more than 10 marks and every pooled model is at 0–1.

> "The pooled adapters are flat everywhere: at most +0.32 (marks) and +0.62 (bd) across three personas, two exams and five models, and the catastrophic tail the collapse creates is gone:"

## Discussion


## Related Claims
- [Grading skill transfers across exams: an adapter fine-tuned on one exam improves grading on the unseen other, though transfer stops short of in-domain performance](grading-skill-transfers-across-exams.md) — related
- [A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright](llm-grader-strict-persona-collapse.md) — related
- [Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64](closed-llm-graders-below-human-floor.md) — related
- [The strict-persona vulnerability replicates on an independent machine-learning exam, but its direction is exam-specific: seven of 17 models improve because the persona cancels their over-marking](strict-persona-effect-exam-specific.md) — related
- [The strict-persona collapse is attributed to the preamble's two credit-withholding policy sentences, not its harsh tone, with S2 alone causing refusal in two models](strict-preamble-policy-sentence-attribution.md) — related
