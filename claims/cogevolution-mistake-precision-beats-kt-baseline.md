---
type: claim
title: "CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948"
description: "CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948"
id: cogevolution-mistake-precision-beats-kt-baseline
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
---

# CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` CogEvolution performs comparably to the knowledge tracing-based PEERS model in mastery perception precision (AUC 0.80 vs 0.82), and both significantly outperform static persona models. [→ Wei Zhang 2026](#wei-zhang-2026)
`q2 i?` CogEvolution achieves higher Mistake Precision (76.8%) than PEERS (64.5%) and static agents, reproducing typical misconceptions consistent with real student cognitive gaps. [→ Wei Zhang 2026 (2)](#wei-zhang-2026-2)

## Evidence

### Wei Zhang 2026

Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786

`q2 · i?` · `design · r2`

Comparative evaluation on the CogMath-948 dataset (Table 2) reports AUC and RMSE for CogEvolution versus static LLM agents and the PEERS (BKT+LLM) baseline; the article states "performs comparably to the knowledge tracing-based PEERS model (AUC: 0.80 vs 0.82)". No effect size is printed.

> "In terms of mastery perception precision (AUC/RMSE), Co-gEvolution performs comparably to the knowledge tracing-based PEERS model (AUC: 0.80 vs 0.82), and both signifi-cantly outperform static persona models."

### Wei Zhang 2026 (2)

Wei Zhang, Yihang Cheng, Zhirong Ye & Kezhen Huang. (2026). CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution. https://arxiv.org/abs/2604.14786

`q2 · i?` · `design · r2`

Task-performance analysis for RQ1 on CogMath-948 reports Mistake Precision of 76.8% for CogEvolution, versus 64.5% for PEERS and 55.4% for GPT-4o in Table 2; the article attributes this to ICAP perception and memory retrieval reproducing "typical Misconceptions consistent with real student cognitive gaps". No effect size is printed.

> "More importantly, CogEvolution achieves a sig-nificantadvantageinMistakePrecision(76.8%)."

## Discussion


## Related Claims
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
- [CogEvolution's simulated learning trajectory fits the human power-law trajectory far better than baselines (R²LC 0.92 vs 0.78 PEERS, 0.45 static agents)](cogevolution-learning-curve-power-law-fit.md) — related
- [Mined misconception labels match personas' assigned misconceptions at F1 ≈ 0.56, a score that does not test whether generated questions elicit the named misconception](collearn-misconception-mining-f1.md) — related
