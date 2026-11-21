---
type: claim
title: A shared-backbone framework with task-specific LoRA adapters achieves average QWK of 0.848 across 27 scoring tasks versus 0.888 for fully fine-tuned models
description: A shared-backbone framework with task-specific LoRA adapters achieves average QWK of 0.848 across 27 scoring tasks versus 0.888 for fully fine-tuned models
id: shared-backbone-lora-qwk-0-848-vs-0-888
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: latif-2024
    resource: "https://doi.org/10.48550/arXiv.2412.21065"
    title: "Latif, E., Zhou, Y., Fang, L., & Zhai, X. (2024). Efficient Multi-Task Inferencing with a Shared Backbone and Lightweight Task-Specific Adapters for Automatic Scoring. [doi:10.48550/arXiv.2412.21065](https://doi.org/10.48550/arXiv.2412.21065)"
    author: "Latif, E., Zhou, Y., Fang, L., & Zhai, X."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A shared-backbone framework with task-specific LoRA adapters achieves average QWK of 0.848 across 27 scoring tasks versus 0.888 for fully fine-tuned models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 27 mutually exclusive automated scoring tasks, the proposed shared-backbone framework attains an average QWK of 0.848, a relative reduction of only 4.5% compared with fully fine-tuned G-SciEdBERT baselines at 0.888. [→ Latif 2024](#latif-2024)

## Evidence

### Latif 2024

Latif, E., Zhou, Y., Fang, L., & Zhai, X. (2024). Efficient Multi-Task Inferencing with a Shared Backbone and Lightweight Task-Specific Adapters for Automatic Scoring. [doi:10.48550/arXiv.2412.21065](https://doi.org/10.48550/arXiv.2412.21065)

`q2 · i?` · `causal · r2`

Evaluation on 27 German PISA 2015 scoring tasks, each fine-tuned independently with approximately 1,000 human-scored responses per item, comparing the proposed framework against fully fine-tuned G-SciEdBERT baselines; the results table reports "average: 0.888" versus "average: 0.848".

> "While the fully fine-tuned G-SciEdBERT model achieves slightly higher QWK scores (average: 0.888), the proposed framework maintains competitive accuracy (average: 0.848), with a relative reduction of only 4.5%."

## Discussion


## Related Claims
- [Per-task QWK differences between the adapter framework and fully fine-tuned models range from 0.01 to 0.03, with negligible differences on binary-label tasks](per-task-qwk-differences-0-01-to-0-03.md) — related
- [LoRA adaptation adds only 0.6M trainable parameters on an 86.4M frozen backbone, keeping methods lightweight relative to LLM-based scoring](lora-parameter-efficiency-drawing-scoring.md) — related
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](llama-prediction-range-compression.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — related
- [Fine-tuned GPT-4o achieves state-of-the-art scoring of TOEFL argumentative essays with QWK 0.84 and RMSE 0.44 against official scores](wraft-finetuned-gpt4o-scoring-qwk-084.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
