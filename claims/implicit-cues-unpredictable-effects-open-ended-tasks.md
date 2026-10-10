---
type: claim
title: Implicit demographic cues produce larger and less predictable effects in open-ended tasks, including longer responses for laptop users and education-related length effects
description: Implicit demographic cues produce larger and less predictable effects in open-ended tasks, including longer responses for laptop users and education-related length effects
id: implicit-cues-unpredictable-effects-open-ended-tasks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: donya-rooein-2026
    resource: "https://arxiv.org/abs/2609.16993"
    title: "Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993"
    author: Donya Rooein, Luca Benedetto, Dirk Hovy
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: donya-rooein-2026-2
    resource: "https://arxiv.org/abs/2609.16993"
    title: "Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993"
    author: Donya Rooein, Luca Benedetto, Dirk Hovy
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Implicit demographic cues produce larger and less predictable effects in open-ended tasks, including longer responses for laptop users and education-related length effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Response length shows more significant effects under implicit than explicit conditioning, with laptop users consistently receiving longer responses across four models. [→ Donya Rooein 2026](#donya-rooein-2026)
`q2 i?` Default LLM behavior is English- and US-centric: language: English and nationality: US attributes shift conditioned responses closer to the model default (positive BERTScore coefficients). [→ Donya Rooein 2026 (2)](#donya-rooein-2026-2)

## Evidence

### Donya Rooein 2026

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993

`q2 · i?` · `causal · r2`

Regression analysis of response length in the QA task: "We consistently find that users who use laptops receive longer responses (4 models)" under implicit conditioning, and higher education levels also received longer responses. The implicit-vs-explicit regression-line coefficient was m = 1.20.

> "Notably, our findings were quite different when measuring differences in theresponse length(num- ber of words) of the LLM responses: indeed, we find more significant results for Imp than for Exp, and the coefficients were generally larger"

### Donya Rooein 2026 (2)

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993

`q2 · i?` · `causal · r2`

BERTScore F1 regression using the model default as reference in the QA task: responses for English-language and US-nationality profiles sit closer to the default. The authors also note contrasting effects: age and SES coefficients flipped sign between explicit and implicit conditions.

> "nationality: US, shows positive coefficients forExp conditioning (4 models). These results show, once more, that thedefaultof LLMs tends to be English- centric (and US-centric in particular)."

## Discussion


## Related Claims
- [Higher stated education and SES levels receive responses with more positive sentiment, an implicit bias that can disadvantage lower-education users](education-ses-sentiment-bias-qa.md) — related
- [LLMs exhibit demographic sensitivity: systematic output differences attributable solely to demographic context when task inputs are held constant](llm-demographic-sensitivity-educational-tasks.md) — a broader claim this one bears on
