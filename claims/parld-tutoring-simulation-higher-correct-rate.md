---
type: claim
title: "ParLD-guided tutoring instructions raise simulated students' correct-answer rate to 72.22% versus 56.48% for Direct Respond on MathDial"
description: "ParLD-guided tutoring instructions raise simulated students' correct-answer rate to 72.22% versus 56.48% for Direct Respond on MathDial"
id: parld-tutoring-simulation-higher-correct-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
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

# ParLD-guided tutoring instructions raise simulated students' correct-answer rate to 72.22% versus 56.48% for Direct Respond on MathDial

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the tutoring enhancement simulation on MathDial, ParLD (GPT-4.1) helps 72.22% of simulated students answer correctly versus 56.48% with Direct Respond, and ParLD reduces intersection average turns. [→ Fangzhou Yao 2026](#fangzhou-yao-2026)

## Evidence

### Fangzhou Yao 2026

Fangzhou Yao, Sheng Chang, Weibo Gao, Qi Liu. (2026). Conversational Learning Diagnosis via Reasoning Multi-Turn Interactive Learning. [doi:10.1609/aaai.v40i40.40736](https://doi.org/10.1609/aaai.v40i40.40736)

`q2 · i?` · `design · r2`

Simulation experiment (RQ3) on 108 filtered MathDial conversations with InstructGPT-simulated students, comparing ParLD against Direct Respond (DR) and Direct Analyze (DA) settings using Correct Rate, Avg. Turns, and Intersection Avg. Turns (Table 2). The article reports ParLD "significantly outperform both Direct Respond (DR) and Direct Analyze (DA), with DR performing the worst".

> "ParLD with GPT-4.1 helps 72.22% of students effectively learn the material, compared to just 56.48% with Direct Respond using GPT-4.1."

## Discussion


## Related Claims
- [ParLD (GPT-4.1) outperforms traditional knowledge-tracing baselines on final-turn performance prediction on MathDial and CoMTA](parld-outperforms-kt-baselines-performance-prediction.md) — related
- [Removing the Behavior Previewer hurts ParLD's prediction most; the full framework outperforms all ablation variants](parld-ablation-preview-reflector-contributions.md) — related
- [DPO training significantly increases the likelihood of correct next-turn student responses predicted by LLMKT, outperforming prompting, SFT, distillation, GPT-4o and human tutor utterances on the MathDial test set](dpo-tutor-training-raises-predicted-student-correctness.md) — related
- [A pedagogically informed Tutor Prompt yields higher Success@N and lower Telling@N than MathDial's Base Prompt in simulated tutor-student dialogues](tutor-prompt-outperforms-base-prompt-mathdial.md) — related
