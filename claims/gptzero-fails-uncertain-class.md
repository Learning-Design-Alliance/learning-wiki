---
type: claim
title: GPTZero fails entirely on ambiguous responses, scoring an F1 of 0.00 on the uncertain class in the in-domain test set
description: GPTZero fails entirely on ambiguous responses, scoring an F1 of 0.00 on the uncertain class in the in-domain test set
id: gptzero-fails-uncertain-class
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

# GPTZero fails entirely on ambiguous responses, scoring an F1 of 0.00 on the uncertain class in the in-domain test set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPTZero misclassified all uncertain-class instances in the in-domain test set, and both models tended to overestimate LLM-authorship for ambiguous content. [→ Bhushan 2025](#bhushan-2025)

## Evidence

### Bhushan 2025

Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. [doi:10.1007/978-3-032-03870-8_4](https://doi.org/10.1007/978-3-032-03870-8_4)

`q2 · i?` · `design · r2`

Performance comparison on the in-domain test set (333 responses) shows GPTZero scored 0.00 precision, recall, and F1 on the uncertain class. The article reports "GPTZero’s F1 score of 0.00 for these cases" and that GPTZero misclassified 86 uncertain responses as LLM-generated, versus 28 for the fine-tuned model.

> "GPTZero’s F1 score of 0.00 for these cases highlights its difficulty in handling edge cases, misclassifying all instances"

## Discussion


## Related Claims
- [A fine-tuned GPT-4o model outperforms GPTZero at detecting LLM-generated short answers in an online lesson, achieving 80% accuracy versus GPTZero's 70%](fine-tuned-gpt4o-outperforms-gptzero-short-answers.md) — related
- [A stylometric logistic-regression baseline outperformed GPTZero, achieving 77% accuracy on short-answer detection](stylometric-baseline-beats-gptzero.md) — related
- [Independent evaluation found commercial AI-text detectors neither sufficiently accurate nor sufficiently reliable for high-stakes use](detectors-insufficient-accuracy-high-stakes.md) — a broader claim this one bears on
