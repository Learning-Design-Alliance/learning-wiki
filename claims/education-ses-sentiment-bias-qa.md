---
type: claim
title: Higher stated education and SES levels receive responses with more positive sentiment, an implicit bias that can disadvantage lower-education users
description: Higher stated education and SES levels receive responses with more positive sentiment, an implicit bias that can disadvantage lower-education users
id: education-ses-sentiment-bias-qa
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

# Higher stated education and SES levels receive responses with more positive sentiment, an implicit bias that can disadvantage lower-education users

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Education level positively predicts response sentiment, with an average sentiment difference of 0.3 between the lowest and highest of four education levels. [→ Donya Rooein 2026](#donya-rooein-2026)
`q2 i?` Under implicit conditioning, additional behavioral attributes (tech: Smartphone, religion: Christian, hobbies: Use social media) strongly affect sentiment inconsistently across models. [→ Donya Rooein 2026 (2)](#donya-rooein-2026-2)

## Evidence

### Donya Rooein 2026

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993

`q2 · i?` · `causal · r2`

Multivariate regression on sentiment of QA responses across 200 demographic profiles, with sentiment on a {0,1,2,3,4} scale and σsentiment = 0.07. Education carried positive coefficients for the two Llama models (Exp) and, with a smaller coefficient, Qwen-30B (Imp).

> "This indicates that higher education level receives responses with more positive sentiment, which can be problematic especially with Exp: indeed, the dataset contains 4 education lev- els (from‘High school or below’to‘Doctorate or above’) and the coefficient indicates that, on aver- age, there is a difference of 0.3 between the senti- ment of the lowest and higher education level"

### Donya Rooein 2026 (2)

Donya Rooein, Luca Benedetto, Dirk Hovy. (2026). The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment. https://arxiv.org/abs/2609.16993

`q2 · i?` · `causal · r2`

Same sentiment regression analysis of the implicit condition: several behavioral attributes exceeded the sentiment standard deviation although absent from explicit-condition results. The authors suggest LLMs pick up topics in these users' prompt histories, but effects are not consistent across models.

> "for Imp there are several attributes which have a strong effect on the sentiment of the responses (|µb|≥σ sentiment) even though they do not appear from the analysis onExp:Tech: Smartphone,reli- gion: Christian,hobbies: Use social media."

## Discussion


## Related Claims
- [Implicit demographic cues produce larger and less predictable effects in open-ended tasks, including longer responses for laptop users and education-related length effects](implicit-cues-unpredictable-effects-open-ended-tasks.md) — related
- [Explicitly mentioned education and SES cues lead most models to produce less readable responses for higher-education users, showing partial readability adaptation](explicit-education-cues-readability-adaptation.md) — related
