---
type: claim
title: "Training on reformulated hard problems improves pass@k at test time, suggesting acquisition of new reasoning capabilities"
description: "Training on reformulated hard problems improves pass@k at test time, suggesting acquisition of new reasoning capabilities"
id: cog-drift-improves-passk
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

# Training on reformulated hard problems improves pass@k at test time, suggesting acquisition of new reasoning capabilities

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` At k=128, Cog-DRIFT improves pass@k over the base model by +3.33% (AIME2024), +3.33% (AIME2025), and +2.02% (GPQA), outperforming both base and GRPO-trained models as k increases. [→ Justin Chih-Yao Chen 2026](#justin-chih-yao-chen-2026)

## Evidence

### Justin Chih-Yao Chen 2026

Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal. (2026). Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems. Preprint. Under review. [doi:10.48550/arXiv.2604.04767](https://doi.org/10.48550/arXiv.2604.04767)

`q2 · i?` · `causal · r2`

Pass@k analysis in Section 6, Figure 3: pass@k plotted for k from 1 to 128 using Qwen on AIME2024, AIME2025, and GPQA. The authors interpret the gains as evidence that "training on reformulated hard problems can effectively learn reasoning capabilities" rather than only distribution sharpening.

> "At k= 128, Cog-DRIFT improves over the base model by +3.33%, +3.33%, and +2.02% on AIME2024, AIME2025, and GPQA, respectively. In contrast, GRPO again exhibits degraded performance, echoing the finding that directly training on hard problems fails to generalize."

## Discussion


## Related Claims
- Cog-DRIFT outperforms GRPO and guided-exploration baselines, unlocking gains on originally unsolvable problems (+10.11% Qwen, +8.64% Llama on BigMath-Hard) — related
- [Learning from reformulated problems transfers back to original open-ended hard problems, and more generative formats transfer better](reformulation-transfers-back-to-open-ended.md) — related
- [Exposure to a diverse mixture of reformulations is critical for transfer; single-format training does not improve over no training](reformulation-diversity-critical.md) — related
