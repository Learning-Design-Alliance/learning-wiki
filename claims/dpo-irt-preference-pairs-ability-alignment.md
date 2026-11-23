---
type: claim
title: DPO training with IRT-likelihood preference pairs makes simulated student responses strongly follow their prompted ability (θ-Align)
description: DPO training with IRT-likelihood preference pairs makes simulated student responses strongly follow their prompted ability (θ-Align)
id: dpo-irt-preference-pairs-ability-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: alexander-scarlatos-2025
    resource: "https://doi.org/10.18653/v1/2025.emnlp-main.1274"
    title: "Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan. (2025). SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction. [doi:10.18653/v1/2025.emnlp-main.1274](https://doi.org/10.18653/v1/2025.emnlp-main.1274)"
    author: Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DPO training with IRT-likelihood preference pairs makes simulated student responses strongly follow their prompted ability (θ-Align)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SMART outperforms other simulation methods by a wide margin on θ-Align, the Spearman correlation between input ability and scored generated responses. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan. (2025). SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction. [doi:10.18653/v1/2025.emnlp-main.1274](https://doi.org/10.18653/v1/2025.emnlp-main.1274)

`q2 · i?` · `design · r2`

Distribution-level simulation metrics in Table 2 compare Response Gen ZS, Response Gen SFT, and SMART on both datasets; the article reports SMART's θ-Align advantage and attributes it to DPO training producing "a strong preference for the model to follow the input ability". No effect sizes are printed.

> "We see that SMART outperforms other methods by a wide margin on the θ-Align metric, which measures the correlation between the desired input ability and inferred ability by scoring the generated responses."

## Discussion


## Related Claims
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — related
- [Post-training alignment methods may induce sycophancy that deteriorates GenAI models' ability to disagree and push back](sycophancy-limits-genai-pushback.md) — related
- [Student performance correlates positively with the teacher's DPO optimization progress and with the share of positive-influence data](teacher-learning-student-performance-correlation.md) — related
