---
type: claim
title: "All three evaluated LLMs' F1 scores fell with Level-4 prompting in preliminary experiments"
description: "All three evaluated LLMs' F1 scores fell with Level-4 prompting in preliminary experiments"
id: level4-prompting-lowers-f1-preliminary
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
sources:
  - id: effat-farhana-2024
    title: Effat Farhana 2024
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# All three evaluated LLMs' F1 scores fell with Level-4 prompting in preliminary experiments

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In preliminary experiments on five PhET simulations, F1 scores of ChatGPT-3.5, PaLM 2, and LLaMA-2 (70B) all dropped under Level-4 prompting relative to other levels. [→ Effat Farhana 2024](#effat-farhana-2024)

## Evidence

### Effat Farhana 2024

Effat Farhana, Souvika Sarkar, Ralph Knipper, Indrani Dey, Hari Narayanan, Sadhana Puntambekar, and Santu Karmaker. 2024. SimPal: Towards a Meta-Conversational Framework to Understand Teacher's Instructional Goals for K-12 Physics. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3664695

`q2 · i?` · `design · r2`

Preliminary experiment on five PhET simulations across TELeR Levels 1-4. Table 3 shows Level 4 F1 of 0.711 (ChatGPT-3.5), 0.818 (PaLM 2), and 0.7894 (LLaMA-2), below those models' best levels; based on these results the authors selected ChatGPT-3.5 and PaLM 2 with Level 2 and Level 3 prompting.

> "Table 3 shows that all three LLMs' F1-scores fall with Level-4 prompting."

## Discussion


## Related Claims
- [Level 3 TELeR prompting yielded higher F1 than Level 2 for both LLMs on Golabz simulations](level3-prompting-beats-level2-golabz.md) — related
- [ChatGPT-3.5 outperformed PaLM 2 in F1 with Level 3 prompting on both simulation sources](chatgpt-outperforms-palm2-level3.md) — related
- [Golabz simulations outperformed PhET in F1 score, attributed to content alignment differences](golabz-outperformed-phet-f1.md) — related
- [SimPal identifies instructional-goal-relevant physics variables with moderate F1 (up to 0.60) across 63 simulations](simpal-variable-extraction-f1-moderate.md) — related
