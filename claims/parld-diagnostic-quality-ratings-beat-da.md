---
type: claim
title: "Human raters judge ParLD's inferred cognitive states more accurate and coherent than Direct Analyze"
description: "Human raters judge ParLD's inferred cognitive states more accurate and coherent than Direct Analyze"
id: parld-diagnostic-quality-ratings-beat-da
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: fangzhou-yao-2026
    resource: "https://doi.org/10.1609/aaai.v40i40.40736"
    title: "Fangzhou Yao, Sheng Chang, Weibo Gao, Qi Liu. (2026). Conversational Learning Diagnosis via Reasoning Multi-Turn Interactive Learning. [doi:10.1609/aaai.v40i40.40736](https://doi.org/10.1609/aaai.v40i40.40736)"
    author: Fangzhou Yao, Sheng Chang, Weibo Gao, Qi Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human raters judge ParLD's inferred cognitive states more accurate and coherent than Direct Analyze

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Two mathematics-proficient students rated ParLD's diagnostic results higher than DA on 3-point scales for Accuracy (2.475 vs 2.1) and Coherence (2.7 vs 2.425) across 20 sampled simulated conversations. [→ Fangzhou Yao 2026](#fangzhou-yao-2026)

## Evidence

### Fangzhou Yao 2026

Fangzhou Yao, Sheng Chang, Weibo Gao, Qi Liu. (2026). Conversational Learning Diagnosis via Reasoning Multi-Turn Interactive Learning. [doi:10.1609/aaai.v40i40.40736](https://doi.org/10.1609/aaai.v40i40.40736)

`q2 · i?` · `design · r2`

Quality evaluation in which two mathematics-proficient students rated diagnostic results from 20 sampled simulated conversations on Accuracy and Coherence using a 3-point scale (1 = worst, 3 = best). The ratings favor ParLD over DA on both measures; no statistical test is reported.

> "ParLD outperformed DA (2.475 vs. 2.1 in Accuracy; 2.7 vs. 2.425 in Coherence), indicating its advantage in conversational learning diagnosis."

## Discussion


## Related Claims
- [Accurate LLM solution diagnosis does not reliably produce pedagogically actionable feedback, with lowest rubric scores on error identification and actionability](accurate-diagnosis-not-actionable-feedback.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
