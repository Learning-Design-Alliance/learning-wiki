---
type: claim
title: "Grading skill transfers across exams: an adapter fine-tuned on one exam improves grading on the unseen other, though transfer stops short of in-domain performance"
description: "Grading skill transfers across exams: an adapter fine-tuned on one exam improves grading on the unseen other, though transfer stops short of in-domain performance"
id: grading-skill-transfers-across-exams
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Grading skill transfers across exams: an adapter fine-tuned on one exam improves grading on the unseen other, though transfer stops short of in-domain performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Mean MAE on the ML exam falls from 7.95 (base) to 5.36 under the CV-exam adapter, and on the CV exam from 5.54 to 3.57 under the ML-exam adapter, with every model improving in both directions but one exception. [→ Habibullah 2026](#habibullah-2026)

## Evidence

### Habibullah 2026

Habibullah, A., Alshoibi, Y., Alshiekh, M., Khan, S., & Khan, N. (2026). Where LLM graders succeed and break: Evidence from two computer-science exams. arXiv. https://arxiv.org/abs/2609.29333 [doi:10.48550/arxiv.2609.29333](https://doi.org/10.48550/arxiv.2609.29333)

`q2 · i?` · `causal · r2`

Cross-exam transfer evaluation of per-exam LoRA adapters on held-out students of the unseen exam. The article notes the one negative transfer cell is Gemma-4-E4B on the ML exam (4.66→4.79), the strongest base there with the least room to improve.

> "An adapter fine-tuned on one exam improves grading on the other, which it never saw: mean MAE on the ML examfalls from 7.95 (base) to 5.36 under the CV-exam adapter, and on the CV exam from5.54 to 3.57 under the ML-examadapter."

## Discussion


## Related Claims
- [Six closed-model configurations grade at or below the human inter-grader floor of 2.61/35 on the CV exam, with the best reaching MAE 1.64](closed-llm-graders-below-human-floor.md) — related
- [One LoRA adapter fine-tuned on the two exams' pooled ~3,900 dual-graded examples brings five small open models to parity or better with a human grader and makes them insensitive to harsh personas](lora-finetuning-llm-grader-parity.md) — related
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — a broader claim this one bears on
- [Transfer between two specific datasets is asymmetric: Sangodiah-trained models transfer unusually well to Gani questions](sangodiah-gani-asymmetric-transfer.md) — related
- [A short strict-grader preamble knocks 14 of 17 open-weights LLM graders out of the graded band on a computer-vision exam, with three stopping grading outright](llm-grader-strict-persona-collapse.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — related
