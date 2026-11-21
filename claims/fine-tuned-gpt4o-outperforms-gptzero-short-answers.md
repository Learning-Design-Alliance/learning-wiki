---
type: claim
title: "A fine-tuned GPT-4o model outperforms GPTZero at detecting LLM-generated short answers in an online lesson, achieving 80% accuracy versus GPTZero's 70%"
description: "A fine-tuned GPT-4o model outperforms GPTZero at detecting LLM-generated short answers in an online lesson, achieving 80% accuracy versus GPTZero's 70%"
id: fine-tuned-gpt4o-outperforms-gptzero-short-answers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: bhushan-2025
    resource: "https://doi.org/10.1007/978-3-032-03870-8_4"
    title: "Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. [doi:10.1007/978-3-032-03870-8_4](https://doi.org/10.1007/978-3-032-03870-8_4)"
    author: Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A fine-tuned GPT-4o model outperforms GPTZero at detecting LLM-generated short answers in an online lesson, achieving 80% accuracy versus GPTZero's 70%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On an in-domain test set of 333 responses, the fine-tuned GPT-4o model achieved 80% accuracy and a weighted F1 of 0.78, outperforming GPTZero's 70% accuracy and 0.50 macro F1. [→ Bhushan 2025](#bhushan-2025)

## Evidence

### Bhushan 2025

Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. [doi:10.1007/978-3-032-03870-8_4](https://doi.org/10.1007/978-3-032-03870-8_4)

`q2 · i?` · `design · r2`

Evaluation of the fine-tuned GPT-4o model and GPTZero on the in-domain test set of 333 responses from the Using Motivational Strategies lesson. The fine-tuned model achieved "an overall accuracy of 80%, outperforming GPTZero, which had an accuracy of 70%"; the article also reports a weighted F1 of 0.78 versus GPTZero's macro F1 of 0.50.

> "achieving an F1 score of 86% and an overall accuracy of 80%, outperforming GPTZero, which had an accuracy of 70%."

## Discussion


## Related Claims
- [GPTZero fails entirely on ambiguous responses, scoring an F1 of 0.00 on the uncertain class in the in-domain test set](gptzero-fails-uncertain-class.md) — related
- [A stylometric logistic-regression baseline outperformed GPTZero, achieving 77% accuracy on short-answer detection](stylometric-baseline-beats-gptzero.md) — related
- [The fine-tuned model generalized to out-of-domain lessons with 77% overall accuracy](fine-tuned-model-out-of-domain-77.md) — related
