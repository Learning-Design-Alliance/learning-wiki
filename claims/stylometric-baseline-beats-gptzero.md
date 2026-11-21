---
type: claim
title: "A stylometric logistic-regression baseline outperformed GPTZero, achieving 77% accuracy on short-answer detection"
description: "A stylometric logistic-regression baseline outperformed GPTZero, achieving 77% accuracy on short-answer detection"
id: stylometric-baseline-beats-gptzero
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

# A stylometric logistic-regression baseline outperformed GPTZero, achieving 77% accuracy on short-answer detection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` An open-source stylometric classifier using 13 writing-style features achieved 77% accuracy, outperforming GPTZero on the same in-domain test set. [→ Bhushan 2025](#bhushan-2025)

## Evidence

### Bhushan 2025

Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. [doi:10.1007/978-3-032-03870-8_4](https://doi.org/10.1007/978-3-032-03870-8_4)

`q2 · i?` · `design · r2`

Evaluation of a scikit-learn stylometric classifier with 13 writing-style features (word length, sentence length, readability scores, punctuation, formatting, human and LLM text markers) on the in-domain test set; the article reports the baseline "significantly outperformed GPTZero, achieving 77% accuracy".

> "this baseline significantly outperformed GPTZero, achieving 77% accuracy, highlighting that in AI detection of short responses, stylistic features are an accurate predictor."

## Discussion


## Related Claims
- [A fine-tuned GPT-4o model outperforms GPTZero at detecting LLM-generated short answers in an online lesson, achieving 80% accuracy versus GPTZero's 70%](fine-tuned-gpt4o-outperforms-gptzero-short-answers.md) — related
- [GPTZero fails entirely on ambiguous responses, scoring an F1 of 0.00 on the uncertain class in the in-domain test set](gptzero-fails-uncertain-class.md) — related
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — related
