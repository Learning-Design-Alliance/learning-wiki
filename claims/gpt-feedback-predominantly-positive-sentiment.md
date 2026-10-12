---
type: claim
title: GPT-generated tutor feedback is predominantly positive or neutral in sentiment
description: GPT-generated tutor feedback is predominantly positive or neutral in sentiment
id: gpt-feedback-predominantly-positive-sentiment
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: reddig-2025
    resource: "https://doi.org/10.1007/s40593-025-00505-6"
    title: "Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6"
    author: "Reddig, J. M., Arora, A., & MacLellan, C. J."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# GPT-generated tutor feedback is predominantly positive or neutral in sentiment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Automated sentiment analysis found most GPT-generated hints positive or neutral, with only 292 hints categorized as negative. [→ Reddig 2025](#reddig-2025)

## Evidence

### Reddig 2025

Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6

`q2 · i?` · `design · r3`

TextBlob lexicon-based sentiment analysis of the GPT-generated hints; polarity ranged from -0.75 to 1.00 with a high concentration just below 0.00, and the histogram was skewed right, indicating most feedback was neutral to positive.

> "The bar graph in Fig. 8 agrees, with most feedback falling into the positive category, and only 292 hints categorized as negative."

## Discussion


## Related Claims
- [Counterfactual fine-tuning reduces sentiment bias in LLM-generated forum replies](counterfactual-fine-tuning-reduces-sentiment-bias.md) — related
