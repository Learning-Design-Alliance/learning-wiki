---
type: claim
title: "CogEvolution's simulated learning trajectory fits the human power-law trajectory far better than baselines (R²LC 0.92 vs 0.78 PEERS, 0.45 static agents)"
description: "CogEvolution's simulated learning trajectory fits the human power-law trajectory far better than baselines (R²LC 0.92 vs 0.78 PEERS, 0.45 static agents)"
id: cogevolution-learning-curve-power-law-fit
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: wei-zhang-2026
    resource: "https://arxiv.org/abs/2604.14786"
    title: "Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786"
    author: "Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang"
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: wei-zhang-2026-2
    resource: "https://arxiv.org/abs/2604.14786"
    title: "Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786"
    author: "Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang"
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: wei-zhang-2026-3
    resource: "https://arxiv.org/abs/2604.14786"
    title: "Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786"
    author: "Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CogEvolution's simulated learning trajectory fits the human power-law trajectory far better than baselines (R²LC 0.92 vs 0.78 PEERS, 0.45 static agents)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` CogEvolution produces an error-rate trajectory that tightly aligns with the ground-truth human trajectory (R²LC = 0.92), with a steep drop in the first 20 steps followed by gradual stabilization. [→ Wei Zhang 2026](#wei-zhang-2026)
`q2 i?` Static agents exhibit a nearly flat trajectory (R²LC = 0.45), showing no learning effect from practice without a state update mechanism. [→ Wei Zhang 2026 (2)](#wei-zhang-2026-2)
`q2 i?` The PEERS model shows a downward but overly linear trend (R²LC = 0.78), struggling to capture diminishing returns characteristic of cognitive saturation. [→ Wei Zhang 2026 (3)](#wei-zhang-2026-3)

## Evidence

### Wei Zhang 2026

Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786

`q2 · i?` · `design · r2`

Learning-curve fitting analysis for RQ2 over 100 practice opportunities on CogMath-948 (Figure 2) fits each agent's error-rate sequence to the power function E(n)=A·n^-α; CogEvolution reaches "R²LC =0.92" against the ground-truth human trajectory. No effect size is printed.

> "In sharp contrast,CogEvolution(Blue Circle) produces a curvethattightlyalignswiththeGroundTruth(𝑅 2 𝐿𝐶 =0.92). The trajectory displays a steep drop in the first 20 steps, followed by a gradual stabilization."

### Wei Zhang 2026 (2)

Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786

`q2 · i?` · `design · r2`

The same Figure 2 learning-curve analysis reports static agents' "nearly flat trajectory (𝑅2𝐿𝐶 =0.45)", which the authors interpret as standard LLMs relying on pre-trained knowledge without manifesting learning from practice.

> "As observed in Figure 2, theStatic Agents(Grey Square) exhibit a nearly flat trajectory (𝑅2𝐿𝐶 =0.45)."

### Wei Zhang 2026 (3)

Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786

`q2 · i?` · `design · r2`

In the same RQ2 analysis, PEERS achieves "R²LC =0.78" with an overly linear trajectory; the authors attribute this to BKT-based probability transitions failing to capture diminishing returns of cognitive saturation.

> "ThePEERSmodel (Green Triangle) shows a downward trend (𝑅2 𝐿𝐶 =0.78), but its trajectory is overly linear. This suggests that while BKT-based probability transitions can simulate performance improvement, they struggle to capture thediminishing returns characteristic of cognitive saturation."

## Discussion


## Related Claims
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
- [CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948](cogevolution-mistake-precision-beats-kt-baseline.md) — related
