---
type: claim
title: "The strict-persona vulnerability replicates on an independent machine-learning exam, but its direction is exam-specific: seven of 17 models improve because the persona cancels their over-marking"
description: "The strict-persona vulnerability replicates on an independent machine-learning exam, but its direction is exam-specific: seven of 17 models improve because the persona cancels their over-marking"
id: strict-persona-effect-exam-specific
status: review
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
---

# The strict-persona vulnerability replicates on an independent machine-learning exam, but its direction is exam-specific: seven of 17 models improve because the persona cancels their over-marking

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` On the ML exam the same preamble worsens ten models, moving three out of the band and one into refusal, yet improves seven; across 16 non-refusal pairs neutral bias predicts the strict effect at r=−0.73 (permutation p=0.002), while on the CV exam zero of 17 improve. [→ Habibullah 2026](#habibullah-2026)

## Evidence

### Habibullah 2026

Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333 [doi:10.48550/arxiv.2609.29333](https://doi.org/10.48550/arxiv.2609.29333)

`q2 · i3` · `causal · r2`

A 162-configuration replication on the ML exam (1,038 students, ≈65-point scale, floor 5.13). The printed correlation r=−0.73 (permutation p=0.002) is a large effect linking neutral bias to the strict effect. The article reports "Under strictfour models cross from the graded band to above that exam’s ( MAE≥15.7 ); Llama-3.1-8B again refuses", and calls the improvements "calibration, not robustness".

> "The ML exam’s neutral prompt over-marks for 15 models, and across the 16 non-refusal pairs neutral bias predicts the strict effect atr=−0.73 (permutationp= 0.002 ); on the CV exam, whose neutral biases straddle zero (none above +1.68), zero of17 improve."

## Discussion


## Related Claims
- [Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64](closed-llm-graders-below-human-floor.md) — related
- [A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright](llm-grader-strict-persona-collapse.md) — related
- [The strict-persona collapse is attributed to the preamble's two credit-withholding policy sentences, not its harsh tone, with S2 alone causing refusal in two models](strict-preamble-policy-sentence-attribution.md) — related
- [One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas](lora-finetuning-llm-grader-parity.md) — related
