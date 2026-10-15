---
type: claim
title: Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64
description: Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64
id: closed-llm-graders-below-human-floor
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
  - id: habibullah-2026-2
    resource: "https://arxiv.org/abs/2609.29333"
    title: "Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333"
    author: "Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N."
    q: 2
    i: 2
    kind: causal
    rigour: 2
---

# Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2` · `i2` medium

## Subclaims
`q2 i?` Across 570 dual-graded submissions the two human graders' totals agree to MAE 2.61/35 (95% CI [2.37, 2.85]; Pearson r=0.868), treated as the human-grader floor. [→ Habibullah 2026](#habibullah-2026)
`q2 i2` Six full-cohort closed-model configurations meet or undercut the floor; in a paired third-grader test three are significantly better than a human grader (e.g. D01 d=−0.54 [−0.71,−0.36]). [→ Habibullah 2026 (2)](#habibullah-2026-2)

## Evidence

### Habibullah 2026

Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333 [doi:10.48550/arxiv.2609.29333](https://doi.org/10.48550/arxiv.2609.29333)

`q2 · i?` · `causal · r2`

Observational analysis of the CV exam's dual grading by 20 graders in 10 fixed pairs; the grader-average total is the ground truth. The floor "pools across pairs whose internal disagreement varies by 4.2×", so pair assignment is a source of variability.

> "Across all 570 dual-graded submissions of the CV exam the two graders’ totals agree to MAE= 2.61/35 (95%bootstrap CI [2.37,2.85] ; Pearsonr= 0.868 )."

### Habibullah 2026 (2)

Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333

`q2 · i2` · `causal · r2`

Configuration-grid evaluation of closed models on the CV exam. Retested with the paired third-grader statistic, three configurations are better than a human grader — "D01 d=−0.54 [−0.71,−0.36]" — while Flash-Lite with thinking and both gpt-5.5 runs sit at parity.

> "Six full-cohort configurations meet or undercut the human floor of 2.61 with CI upper bounds below it (Table 10, Appendix C): D01 (gemini-3-flash-preview, neutral,t= 0 )at MAE= 1.64 (bound 1.79);"

## Discussion


## Related Claims
- [A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright](llm-grader-strict-persona-collapse.md) — related
- [The strict-persona vulnerability replicates on an independent machine-learning exam, but its direction is exam-specific: seven of 17 models improve because the persona cancels their over-marking](strict-persona-effect-exam-specific.md) — related
- [Grading skill transfers across exams: an adapter fine-tuned on one exam improves grading on the unseen other, though transfer stops short of in-domain performance](grading-skill-transfers-across-exams.md) — related
- [One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas](lora-finetuning-llm-grader-parity.md) — related
