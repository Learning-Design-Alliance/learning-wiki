---
type: claim
title: Right-hand-rule tasks are especially difficult for ChatGPT-4o, which states the rule correctly but applies it incorrectly in most cases
description: Right-hand-rule tasks are especially difficult for ChatGPT-4o, which states the rule correctly but applies it incorrectly in most cases
id: right-hand-rule-application-failure-chatgpt-4o
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: giulia-polverini-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010154"
    title: "Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic. (2025). Performance of ChatGPT on tasks involving physics visual representations: the case of the Brief Electricity and Magnetism Assessment. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010154](https://doi.org/10.1103/physrevphyseducres.21.010154)"
    author: Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
  - id: giulia-polverini-2025-2
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010154"
    title: "Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic. (2025). Performance of ChatGPT on tasks involving physics visual representations: the case of the Brief Electricity and Magnetism Assessment. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010154](https://doi.org/10.1103/physrevphyseducres.21.010154)"
    author: Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Right-hand-rule tasks are especially difficult for ChatGPT-4o, which states the rule correctly but applies it incorrectly in most cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Average performance on the seven right-hand-rule items was 35%; where the rule was invoked, 9% of responses stated it incorrectly and 41% implemented the correctly stated rule incorrectly. [→ Giulia Polverini 2025](#giulia-polverini-2025)
`q2 i?` For the force version of the rule, the chatbot stated it correctly 95% of the time but failed to apply it correctly in 70% of those cases, and sometimes described an anatomically impossible hand or the left hand. [→ Giulia Polverini 2025 (2)](#giulia-polverini-2025-2)

## Evidence

### Giulia Polverini 2025

Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic. (2025). Performance of ChatGPT on tasks involving physics visual representations: the case of the Brief Electricity and Magnetism Assessment. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010154](https://doi.org/10.1103/physrevphyseducres.21.010154)

`q2 · i?` · `qualitative · r2`

Qualitative analysis of responses on items 23-26 and 28-30, where the right-hand rule could be used; the rule was explicitly invoked and explained in 53% of cases, with alternatives such as cross-product formulas given otherwise.

> "Of the responses where some form of the RHR was invoked, 9% contained an incorrectly stated RHR, and 41% contained an incorrect implementation of the stated rule (see Fig. 10 for an example)."

### Giulia Polverini 2025 (2)

Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic. (2025). Performance of ChatGPT on tasks involving physics visual representations: the case of the Brief Electricity and Magnetism Assessment. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010154](https://doi.org/10.1103/physrevphyseducres.21.010154)

`q2 · i?` · `design · r2`

Analysis of the force-on-charged-particle/wire version of the rule across four items. The article attributes the failure to the chatbot lacking a body for the embodied off-loading humans use, and notes rule variants were inconsistent across repeated iterations of the same task.

> "This version of the RHR was explicitly stated in 79% of the responses on the four items where it could be used. When explicitly stated, it was correctly stated 95% of the time. However, the chatbot failed to correctly apply it in 70% of these cases, suggesting that it struggles with correctly applying this three-dimensional representation."

## Discussion


## Related Claims
- [ChatGPT-4o's BEMA performance exceeds the average score of a 12214-student university sample, but students outperform it on ten specific items](chatgpt-4o-exceeds-student-bema-average.md) — related
- [ChatGPT-4o outperforms students most on formal and mathematical reasoning items, where it averages 93% against students' 28%](chatgpt-4o-formal-math-items-advantage.md) — related
- [ChatGPT-4o's BEMA errors fall into three difficulty types, with spatial coordination of representations and rules the most prevalent](three-chatbot-difficulty-types-bema.md) — a broader claim this one bears on
- [The solved example mainly helps students invoke the correct principles (especially conservation of momentum), but invoking principles is not enough—students still fail to apply them correctly across connected sub-problems](invoking-versus-applying-principles.md) — related
- [With the solved analog provided, students typically invoke the correct principles but often fail to apply them correctly, e.g., using the same centripetal-acceleration sign as in the analog](invoke-principles-but-application-errors.md) — related
- [Coding chatbot answers by meaning rather than by stated letter raises measured BEMA performance, revealing answer-option-list misinterpretation](meaning-coding-raises-bema-scores.md) — related
- [Earlier LLM generations failed spatial-geometry steps in Electromagnetism, such as deducing induced-current direction with the right-hand rule](llm-spatial-geometry-em-bottleneck.md) — related
