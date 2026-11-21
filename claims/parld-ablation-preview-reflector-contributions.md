---
type: claim
title: "Removing the Behavior Previewer hurts ParLD's prediction most; the full framework outperforms all ablation variants"
description: "Removing the Behavior Previewer hurts ParLD's prediction most; the full framework outperforms all ablation variants"
id: parld-ablation-preview-reflector-contributions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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

# Removing the Behavior Previewer hurts ParLD's prediction most; the full framework outperforms all ablation variants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the ablation study on MathDial, the w/o P variant (State Analyzer only, without the ZPD-Behavior schema) performs the worst, and the full ParLD outperforms all variants for both GPT-4.1 and GPT-4o. [→ Fangzhou Yao 2026](#fangzhou-yao-2026)

## Evidence

### Fangzhou Yao 2026

Fangzhou Yao, Sheng Chang, Weibo Gao, Qi Liu. (2026). Conversational Learning Diagnosis via Reasoning Multi-Turn Interactive Learning. [doi:10.1609/aaai.v40i40.40736](https://doi.org/10.1609/aaai.v40i40.40736)

`q2 · i?` · `design · r2`

Ablation study (RQ2) on the MathDial dataset comparing full ParLD against w/o P, w/o R, and w/o P+R variants in the performance prediction task, with results shown in Figure 2. The article reports the "w/o P" variant "performs the worst in predicting whether a student has effectively learned the material".

> "The experimental results in Figure 2 demonstrate that, for both GPT-4.1 and GPT-4.0, ParLD outperforms all variants, confirming the contribution of each component to the reliability of its learning diagnosis."

## Discussion


## Related Claims
- [Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other](knowledge-behavior-profile-complementary-signals.md) — related
- [ParLD-guided tutoring instructions raise simulated students' correct-answer rate to 72.22% versus 56.48% for Direct Respond on MathDial](parld-tutoring-simulation-higher-correct-rate.md) — related
