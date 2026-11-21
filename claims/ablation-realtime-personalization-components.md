---
type: claim
title: Removing real-time adjustment or personalized recommendations lowers engagement and retention in ablations
description: Removing real-time adjustment or personalized recommendations lowers engagement and retention in ablations
id: ablation-realtime-personalization-components
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: yongjie-li-2025
    resource: "https://doi.org/10.48550/arXiv.2507.18949"
    title: "Yongjie Li, Ruilin Nong, Jianan Liu, Lucas Evans. (2025). Adaptive Learning Systems: Personalized Curriculum Design Using LLM-Powered Analytics. [doi:10.48550/arXiv.2507.18949](https://doi.org/10.48550/arXiv.2507.18949)"
    author: Yongjie Li, Ruilin Nong, Jianan Liu, Lucas Evans
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Removing real-time adjustment or personalized recommendations lowers engagement and retention in ablations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Ablating any framework component (real-time adjustment, personalized recommendations, dynamic pathways, adaptive assessment, resource adjustment) produces a marked decline in LES and KRR for both models. [→ Yongjie Li 2025](#yongjie-li-2025)

## Evidence

### Yongjie Li 2025

Yongjie Li, Ruilin Nong, Jianan Liu, Lucas Evans. (2025). Adaptive Learning Systems: Personalized Curriculum Design Using LLM-Powered Analytics. [doi:10.48550/arXiv.2507.18949](https://doi.org/10.48550/arXiv.2507.18949)

`q2 · i?` · `design · r2`

Ablation study (Table II) testing five degraded configurations for Llama-3-7b and GPT-4. For example, Llama-3-7b 'reached a LES of 70.2% and KRR of 76.5% when real-time adjustments were not in place,' below its full-framework values. Only descriptive percentages are printed; no effect sizes.

> "The results reveal that removing any of these components leads to a marked decline in engagement scores (LES) and knowledge retention rates (KRR)."

## Discussion


## Related Claims
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — a broader claim this one bears on
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](ablation-structural-components-lower-judge-scores.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Each pedagogical verification component contributes to a distinct quality dimension: layout verification most strongly](verification-components-ablation-contributions.md) — related
- [Real-time feedback and dynamic pathway adjustments yield the largest engagement and retention gains among adjustment types](adjustment-types-feedback-pathway-gains.md) — a narrower finding that bears on this claim
- [GPT-4 outperforms Llama-3-7b on learner engagement and knowledge retention across all tested datasets](gpt4-outperforms-llama3-les-krr.md) — related
- [GPT-4 with real-time analysis achieves higher engagement improvement and user satisfaction than Llama-3-7b with dynamic adjustment](ml-integration-engagement-satisfaction.md) — related
- [Removing any of TASA's three modules degrades performance, with the forgetting score contributing an average 6.8% drop in normalized learning gain when eliminated](tasa-ablation-module-importance.md) — related
