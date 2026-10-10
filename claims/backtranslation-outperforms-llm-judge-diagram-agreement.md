---
type: claim
title: Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models
description: Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models
id: backtranslation-outperforms-llm-judge-diagram-agreement
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: vishal-kumar-2025
    resource: "https://arxiv.org/abs/2511.08283"
    title: "Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky. (2025). DiagramIR: An Automatic Pipeline for Educational Math Diagram Evaluation. NeurIPS 2025 Workshop: MATH-AI. https://arxiv.org/abs/2511.08283"
    author: Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Back-translation achieves higher agreement with human ratings (Cohen's kappa 0.48-0.56) than LLM-as-a-Judge in its strongest setting (kappa 0.39-0.47) across four models. [→ Vishal Kumar 2025](#vishal-kumar-2025)

## Evidence

### Vishal Kumar 2025

Vishal Kumar, Shubhra Mishra, Rebecca Hao, Rizwaan Malik, David Broman, Dorottya Demszky. (2025). DiagramIR: An Automatic Pipeline for Educational Math Diagram Evaluation. NeurIPS 2025 Workshop: MATH-AI. https://arxiv.org/abs/2511.08283

`q2 · i?` · `design · r2`

Comparison on a 386-diagram test set of teacher-generated TikZ geometric figures, reported in Table 2: back-translation reached kappa 0.483-0.563 versus 0.388-0.498 for LLM-as-a-Judge with code+image, showing "comparable agreement with human raters" was exceeded by back-translation on every model.

> "We find that back-translation outperforms LLM-as-a-Judge in its strongest setting (where it uses both code and image input), demonstrating comparable agreement with human raters"

## Discussion


## Related Claims
- [Back-translation yields higher human agreement on spatial checks, while LLM-as-a-Judge considerably outperforms it on the angle-label check](checkwise-backtranslation-spatial-strong-angle-weak.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [GPT-4.1-Mini with back-translation matches the best LLM-judge (GPT-5) at 10.3x lower evaluation cost](gpt-4-1-mini-backtranslation-matches-frontier-judge-cost.md) — a narrower finding that bears on this claim
