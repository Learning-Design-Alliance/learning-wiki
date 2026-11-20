---
type: claim
title: SimPal identifies instructional-goal-relevant physics variables with moderate F1 (up to 0.60) across 63 simulations
description: SimPal identifies instructional-goal-relevant physics variables with moderate F1 (up to 0.60) across 63 simulations
id: simpal-variable-extraction-f1-moderate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
source_checked: 2026-11-20
sources:
  - id: effat-farhana-2024
    title: Effat Farhana 2024
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SimPal identifies instructional-goal-relevant physics variables with moderate F1 (up to 0.60) across 63 simulations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` Evaluated on 63 PhET and Golabz physics simulations with ChatGPT-3.5 and PaLM 2, SimPal's variable generation reached micro-averaged F1 scores around 0.52-0.60, which the authors characterize as a high degree of accuracy with a well-defined prompt. [→ Effat Farhana 2024](#effat-farhana-2024)

## Evidence

### Effat Farhana 2024

Effat Farhana, Souvika Sarkar, Ralph Knipper, Indrani Dey, Hari Narayanan, Sadhana Puntambekar, and Santu Karmaker. 2024. SimPal: Towards a Meta-Conversational Framework to Understand Teacher's Instructional Goals for K-12 Physics. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3664695

`q2 · i?` · `design · r2`

Final case-study evaluation of SimPal's LLM variable generation against manually built gold standards on 63 physics simulations, computing "the final Precision, Recall, and micro-averaged F1 score". Table 6 reports F1 values from 0.525 to 0.60 across LLM, prompt level, and source.

> "We evaluated SimPal's performance in 63 Physics simulations, including 32 from PhET and 31 from Golabz, as depicted in Table 4."

## Discussion


## Related Claims
- [ChatGPT-3.5 outperformed PaLM 2 in F1 with Level 3 prompting on both simulation sources](chatgpt-outperforms-palm2-level3.md) — related
- [Golabz simulations outperformed PhET in F1 score, attributed to content alignment differences](golabz-outperformed-phet-f1.md) — related
- [Level 3 TELeR prompting yielded higher F1 than Level 2 for both LLMs on Golabz simulations](level3-prompting-beats-level2-golabz.md) — related
- [All three evaluated LLMs' F1 scores fell with Level-4 prompting in preliminary experiments](level4-prompting-lowers-f1-preliminary.md) — related
