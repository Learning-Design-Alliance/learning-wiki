---
type: claim
title: GPT-generated tutor feedback is predominantly positive or neutral in sentiment
description: GPT-generated tutor feedback is predominantly positive or neutral in sentiment
id: gpt-feedback-predominantly-positive-sentiment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

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
- [GPT4-coded sentiment of students' open-ended general feedback about the intervention was overwhelmingly positive](positive-sentiment-open-ended-feedback.md) — related
- [LLM-generated forum replies are more neutral and less varied in sentiment than human replies](llm-replies-more-neutral-than-human.md) — related
- [90% of open-ended survey responses about the ChatGPT activity were neutral in sentiment, with 2% positive and 8% negative](open-ended-responses-mostly-neutral-sentiment.md) — related
