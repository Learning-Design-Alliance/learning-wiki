---
type: claim
title: Coding chatbot answers by meaning rather than by stated letter raises measured BEMA performance, revealing answer-option-list misinterpretation
description: Coding chatbot answers by meaning rather than by stated letter raises measured BEMA performance, revealing answer-option-list misinterpretation
id: meaning-coding-raises-bema-scores
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
    kind: causal
    rigour: 1
  - id: giulia-polverini-2025-2
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010154"
    title: "Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic. (2025). Performance of ChatGPT on tasks involving physics visual representations: the case of the Brief Electricity and Magnetism Assessment. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010154](https://doi.org/10.1103/physrevphyseducres.21.010154)"
    author: Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Coding chatbot answers by meaning rather than by stated letter raises measured BEMA performance, revealing answer-option-list misinterpretation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ChatGPT-4's score improved by 10.5 percentage points and ChatGPT-4o's by 7.2 percentage points when coded by meaning, indicating both models extract relevant information from graphics despite mismatching letters with answer-option content. [→ Giulia Polverini 2025](#giulia-polverini-2025)
`q2 i?` The letter-meaning mismatch occurred in 26.8% of ChatGPT-4's responses and 10.8% of ChatGPT-4o's, most often from misreading the spatial arrangement of answer option lists. [→ Giulia Polverini 2025 (2)](#giulia-polverini-2025-2)

## Evidence

### Giulia Polverini 2025

Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic. (2025). Performance of ChatGPT on tasks involving physics visual representations: the case of the Brief Electricity and Magnetism Assessment. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010154](https://doi.org/10.1103/physrevphyseducres.21.010154)

`q2 · i?` · `causal · r1`

Quantitative analysis of ChatGPT-4's 60 iterations per screenshot, scored under two coding systems. Item 20 improved most, from 0% to 100% correctness, due to incorrect letter-to-meaning association; performance worsened on 5 of 31 items.

> "When coding ChatGPT-4’s responses by letter, the chatbot scored an average of 50.2% on the test. Passing from coding by letter to coding by meaning, its performance improved by 10.5 percentage points, indicating its ability to extract and process relevant information from graphical representations despite difficulties with answer option formats."

### Giulia Polverini 2025 (2)

Giulia Polverini, Jakob Melin, Elias Önerud, and Bor Gregorcic. (2025). Performance of ChatGPT on tasks involving physics visual representations: the case of the Brief Electricity and Magnetism Assessment. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010154](https://doi.org/10.1103/physrevphyseducres.21.010154)

`q2 · i?` · `design · r2`

Quantitative analysis comparing the two coding approaches across both models' response sets. Arrow-labeled answer option lists, present in 10 of 31 BEMA items, negatively impacted performance; the article notes other explanations such as multiple-choice answer-index biases cannot be excluded.

> "This mismatch between the two coding systems occurred in 26.8% of ChatGPT-4’s responses and 10.8% of ChatGPT-4o’s responses. The analysis suggests that most of the time this was caused by the chatbot misinterpreting the spatial arrangement of the answer option lists, mismatching a letter with the content belonging to another answer option due to their visual proximity."

## Discussion


## Related Claims
- [ChatGPT-4o's BEMA performance exceeds the average score of a 12214-student university sample, but students outperform it on ten specific items](chatgpt-4o-exceeds-student-bema-average.md) — related
- [ChatGPT-4o outperforms students most on formal and mathematical reasoning items, where it averages 93% against students' 28%](chatgpt-4o-formal-math-items-advantage.md) — related
- [ChatGPT-4o outperforms ChatGPT-4 on BEMA under both coding systems, with a 6.3-percentage-point advantage when coded by meaning](chatgpt-4o-outperforms-chatgpt-4-bema.md) — related
- [Validator false-negative cases reveal structural reasoning weaknesses, including answer-schema misinterpretation and internal inconsistency](code-gen-validator-fn-reasoning-weaknesses.md) — related
- [Agreement between GPT-4's answers and human-curated answers based on its explanations was low (κ=0.504), with frequent answer-explanation mismatches](gpt4-answer-explanation-consistency-low-kappa.md) — related
- [ChatGPT-4o's BEMA errors fall into three difficulty types, with spatial coordination of representations and rules the most prevalent](three-chatbot-difficulty-types-bema.md) — related
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [Right-hand-rule tasks are especially difficult for ChatGPT-4o, which states the rule correctly but applies it incorrectly in most cases](right-hand-rule-application-failure-chatgpt-4o.md) — related
- [ChatGPT-4o shows the overall best TUG-K performance, outperforming all other tested chatbots including its subscription-based counterpart ChatGPT-4](chatgpt-4o-best-tug-k-performance.md) — related
