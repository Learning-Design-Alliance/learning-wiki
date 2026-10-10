---
type: claim
title: Back-translation yields higher human agreement on spatial checks, while LLM-as-a-Judge considerably outperforms it on the angle-label check
description: Back-translation yields higher human agreement on spatial checks, while LLM-as-a-Judge considerably outperforms it on the angle-label check
id: checkwise-backtranslation-spatial-strong-angle-weak
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: vishal-kumar-2025
    resource: "https://arxiv.org/abs/2511.08283"
    title: "Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky. (2025). DiagramIR: An Automatic Pipeline for Educational Math Diagram Evaluation. NeurIPS 2025 Workshop: MATH-AI. https://arxiv.org/abs/2511.08283"
    author: Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: vishal-kumar-2025-2
    resource: "https://arxiv.org/abs/2511.08283"
    title: "Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky. (2025). DiagramIR: An Automatic Pipeline for Educational Math Diagram Evaluation. NeurIPS 2025 Workshop: MATH-AI. https://arxiv.org/abs/2511.08283"
    author: Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Back-translation yields higher human agreement on spatial checks, while LLM-as-a-Judge considerably outperforms it on the angle-label check

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Back-translation performs better on both spatial checks even when the judge is given the image, but the judge considerably outperforms back-translation on the angle-labels check. [→ Vishal Kumar 2025](#vishal-kumar-2025)
`q2 i?` LLM-as-a-Judge considerably outperforms back-translation for the mathematical check about angle labels (0.829 vs. 0.652). [→ Vishal Kumar 2025 (2)](#vishal-kumar-2025-2)

## Evidence

### Vishal Kumar 2025

Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky. (2025). DiagramIR: An Automatic Pipeline for Educational Math Diagram Evaluation. NeurIPS 2025 Workshop: MATH-AI. https://arxiv.org/abs/2511.08283

`q2 · i?` · `design · r2`

Check-wise Cohen's kappa against human ratings (Table 3) on the 386-diagram test set; back-translation reached e.g. 0.604 vs 0.390 for diagram-fully-in-frame (GPT-5), showing back-translation "performs better for both spatial checks".

> "back-translation performs better for both spatial checks, despite the LLM-as-a-judge being provided the image to judge with"

### Vishal Kumar 2025 (2)

Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky. (2025). DiagramIR: An Automatic Pipeline for Educational Math Diagram Evaluation. NeurIPS 2025 Workshop: MATH-AI. https://arxiv.org/abs/2511.08283

`q2 · i?` · `design · r2`

Table 3 results for the labeled-angles check: the judge with image+code reached kappa 0.829 (GPT-5 mini) versus 0.652 for back-translation, an outcome the article calls considerably better judging.

> "LLM-as-a-judge considerably outperforms backtranslation for the mathematical check about angle labels (0.829 vs. 0.652)"

## Discussion


## Related Claims
- [Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models](backtranslation-outperforms-llm-judge-diagram-agreement.md) — related
- [GPT-4.1-Mini with back-translation matches the best LLM-judge (GPT-5) at 10.3x lower evaluation cost](gpt-4-1-mini-backtranslation-matches-frontier-judge-cost.md) — related
