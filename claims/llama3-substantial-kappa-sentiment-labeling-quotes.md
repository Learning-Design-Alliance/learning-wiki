---
type: claim
title: An open-source Llama3 model reached substantial agreement with a human coder when sentiment-labeling pre-extracted student reflection quotes
description: An open-source Llama3 model reached substantial agreement with a human coder when sentiment-labeling pre-extracted student reflection quotes
id: llama3-substantial-kappa-sentiment-labeling-quotes
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: xiomara-gonzalez-2026
    resource: "https://www.google.com/search?q=LLM-assisted+sentiment+analysis+for+integrated+computational+and+qualitative+mixed+methods+education+research"
    title: "Xiomara Gonzalez, Gabriella Coloyan Fleming, Andrew Katz, Maya Denton, Jessica Deters. (2026). LLM-assisted sentiment analysis for integrated computational and qualitative mixed methods education research: A case study of students' written reflection assignments. https://www.google.com/search?q=LLM-assisted+sentiment+analysis+for+integrated+computational+and+qualitative+mixed+methods+education+research"
    author: Xiomara Gonzalez, Gabriella Coloyan Fleming, Andrew Katz, Maya Denton, Jessica Deters
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
---

# An open-source Llama3 model reached substantial agreement with a human coder when sentiment-labeling pre-extracted student reflection quotes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r2` · `q2`

## Subclaims
`q2 i?` Human-LLM inter-rater agreement on sentiment labels was substantial for Reflection 1 (κ = 0.52), Reflection 3 (κ = 0.64), and Reflection 4 (κ = 0.67). [→ Xiomara Gonzalez 2026](#xiomara-gonzalez-2026)

## Evidence

### Xiomara Gonzalez 2026

Xiomara Gonzalez, Gabriella Coloyan Fleming, Andrew Katz, Maya Denton, Jessica Deters. (2026). LLM-assisted sentiment analysis for integrated computational and qualitative mixed methods education research: A case study of students' written reflection assignments. https://www.google.com/search?q=LLM-assisted+sentiment+analysis+for+integrated+computational+and+qualitative+mixed+methods+education+research

`q2 · i?` · `qualitative · r2`

Stage 4 reliability analysis comparing the first author's sentiment labels with Llama3's labels for quotes extracted from 51 students' study-abroad reflections. The authors report Cohen's kappa by time point, stating the results "indicated substantial for Reflection 1 (κ = 0.52), Reflection 3 (κ = 0.64), and Reflection 4 (κ = 0.67)".

> "The results indicated substantial for Reflection 1 (κ = 0.52), Reflection 3 (κ = 0.64), and Reflection 4 (κ = 0.67)."

## Discussion


## Related Claims
- [Prior experience living abroad was the only student variable significantly associated with sentiment about verbal communication, with small-to-medium effects differing by time point](lived-abroad-sentiment-differences-longitudinal.md) — related
- [Llama3 quote extraction failed and sentiment outputs required substantial post-processing, with 20% of Reflection 1 labels unmatched by the human coder](llama3-post-processing-burden-prompt-sensitivity.md) — related
- [Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models](backtranslation-outperforms-llm-judge-diagram-agreement.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — a broader claim this one bears on
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — related
- [Human-LLM sentiment divergences were patterned: the LLM tended to assign affective labels to statements a human coder read as neutral](llm-affective-label-bias-neutral-statements.md) — related
- [LLM-assisted sentiment labeling processed quotes roughly two to three times faster than human labeling and ran continuously without cognitive fatigue](llm-sentiment-labeling-efficiency-gain.md) — related
