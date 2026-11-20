---
type: claim
title: Level 3 TELeR prompting yielded higher F1 than Level 2 for both LLMs on Golabz simulations
description: Level 3 TELeR prompting yielded higher F1 than Level 2 for both LLMs on Golabz simulations
id: level3-prompting-beats-level2-golabz
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
sources:
  - id: effat-farhana-2024
    title: Effat Farhana 2024
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Level 3 TELeR prompting yielded higher F1 than Level 2 for both LLMs on Golabz simulations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In Golabz simulations, Level 3 prompting produced higher F1 scores than Level 2 prompting for both ChatGPT-3.5 and PaLM 2. [→ Effat Farhana 2024](#effat-farhana-2024)

## Evidence

### Effat Farhana 2024

Effat Farhana, Souvika Sarkar, Ralph Knipper, Indrani Dey, Hari Narayanan, Sadhana Puntambekar, and Santu Karmaker. 2024. SimPal: Towards a Meta-Conversational Framework to Understand Teacher's Instructional Goals for K-12 Physics. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3664695

`q2 · i?` · `design · r2`

Results section comparison across TELeR prompt levels on the 63-simulation evaluation. Table 6 shows ChatGPT-3.5 Golabz F1 of 0.60 at Level 3 versus 0.541 at Level 2, and PaLM 2 Golabz F1 of 0.568 at Level 3 versus 0.525 at Level 2.

> "Level 3 prompting resulted in higher F1 scores for both LLMs than Level 2 in Golabz simulations."

## Discussion


## Related Claims
- [ChatGPT-3.5 outperformed PaLM 2 in F1 with Level 3 prompting on both simulation sources](chatgpt-outperforms-palm2-level3.md) — related
- [Golabz simulations outperformed PhET in F1 score, attributed to content alignment differences](golabz-outperformed-phet-f1.md) — related
- [SimPal identifies instructional-goal-relevant physics variables with moderate F1 (up to 0.60) across 63 simulations](simpal-variable-extraction-f1-moderate.md) — related
- [All three evaluated LLMs' F1 scores fell with Level-4 prompting in preliminary experiments](level4-prompting-lowers-f1-preliminary.md) — related
