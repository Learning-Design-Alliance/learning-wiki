---
type: claim
title: "Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment"
description: "Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment"
id: cogevolution-ablation-module-contributions
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

# Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Removing ICAP cognitive depth perception drops R²LC sharply to 0.58 (from 0.92). [→ Wei Zhang 2026](#wei-zhang-2026)
`q2 i?` Removing structured retrieval decreases Mistake Precision by 12.3% (to 64.5%). [→ Wei Zhang 2026 (2)](#wei-zhang-2026-2)
`q2 i?` Removing the evolutionary update mechanism significantly reduces mistake fidelity and alignment, falling back to static persona modeling (Mistake Precision 55.1%, R²LC 0.51). [→ Wei Zhang 2026 (3)](#wei-zhang-2026-3)

## Evidence

### Wei Zhang 2026

Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786

`q2 · i?` · `design · r2`

Ablation experiment (Table 3) on CogMath-948 with the w/o ICAP variant; the article reports "R²LC todropsharplyto0.58" alongside Mistake Precision 68.5% and Align 0.73. No effect size is printed.

> "Removing cognitive depth perception renders the agent unable to distinguish between shallow and deep learning,causing𝑅 2𝐿𝐶 todropsharplyto0.58,demonstrating the validity of cognitive features in simulating agent cognitive psychological validity."

### Wei Zhang 2026 (2)

Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786

`q2 · i?` · `design · r2`

Ablation experiment (Table 3) with the w/o Meta-Ret variant reports a "12.3%decreaseinMistakePrecision" (76.8% to 64.5%), with R²LC 0.85 and Align 0.88. No effect size is printed.

> "Removing structured retrieval leads to a 12.3%decreaseinMistakePrecision,indicatingthatknowl-edge assimilation is crucial for reproducing specific cogni-tive misconceptions."

### Wei Zhang 2026 (3)

Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786

`q2 · i?` · `design · r2`

Ablation experiment (Table 3) with the w/o Evo-Update variant reports Mistake Precision 55.1% (down 21.7), R²LC 0.51 (down 0.41), and Align 0.76, which the article describes as falling back to static persona modeling. No effect size is printed.

> "Removing the evolutionary update mechanismresultsinsignificantlyreducedbehavioralmis-take fidelity and cognitive alignment (Align), causing the agent's simulation capability to fall back to static persona modeling."

## Discussion


## Related Claims
- [Taxonomy quality drives CLARA performance: degraded taxonomies reduce alignment, and removing SEL causes the largest degradation](clara-taxonomy-quality-ablation.md) — related
- [CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948](cogevolution-mistake-precision-beats-kt-baseline.md) — related
- [CogEvolution's simulated learning trajectory fits the human power-law trajectory far better than baselines (R²LC 0.92 vs 0.78 PEERS, 0.45 static agents)](cogevolution-learning-curve-power-law-fit.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
