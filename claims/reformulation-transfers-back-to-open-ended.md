---
type: claim
title: Learning from reformulated problems transfers back to original open-ended hard problems, and more generative formats transfer better
description: Learning from reformulated problems transfers back to original open-ended hard problems, and more generative formats transfer better
id: reformulation-transfers-back-to-open-ended
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: justin-chih-yao-chen-2026
    resource: "https://doi.org/10.48550/arXiv.2604.04767"
    title: "Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal. (2026). Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems. Preprint. Under review. [doi:10.48550/arXiv.2604.04767](https://doi.org/10.48550/arXiv.2604.04767)"
    author: Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Learning from reformulated problems transfers back to original open-ended hard problems, and more generative formats transfer better

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` After rejection fine-tuning on reformulated variants, models gain accuracy on the original open-ended hard problems: 11.1% (4-choice), 15.5% (10-choice), 18.9% (cloze). [→ Justin Chih-Yao Chen 2026](#justin-chih-yao-chen-2026)
`q2 i?` The more generative the training format, the better the transfer back to open-ended problems. [→ Justin Chih-Yao Chen 2026](#justin-chih-yao-chen-2026)

## Evidence

### Justin Chih-Yao Chen 2026

Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal. (2026). Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems. Preprint. Under review. [doi:10.48550/arXiv.2604.04767](https://doi.org/10.48550/arXiv.2604.04767)

`q2 · i?` · `causal · r2`

Rejection fine-tuning (RFT) experiment in Section 3.2 and Figure 2(b): correct chain-of-thought trajectories elicited from reformulated problems are used for SFT, then evaluated on the original open-ended Dhard. The article observes "the more the task is generative, the better the transfer back to the open-ended problem."

> "For example, on the original Dhard, model trained with 4-choice achieves 11.1%, 10 choice achieves 15.5%, and cloze achieves 18.9% accuracy."

## Discussion


## Related Claims
- [Training on reformulated hard problems improves pass@k at test time, suggesting acquisition of new reasoning capabilities](cog-drift-improves-passk.md) — related
- Cog-DRIFT outperforms GRPO and guided-exploration baselines, unlocking gains on originally unsolvable problems (+10.11% Qwen, +8.64% Llama on BigMath-Hard) — a broader claim this one bears on
- [Exposure to a diverse mixture of reformulations is critical for transfer; single-format training does not improve over no training](reformulation-diversity-critical.md) — related
- [Reformulating hard open-ended problems into MCQ or cloze formats reduces empirical difficulty, with a consistent ordering MCQ4 ≤ MCQ10 ≤ Cloze ≤ Open-ended](reformulation-reduces-difficulty-ordering.md) — related
