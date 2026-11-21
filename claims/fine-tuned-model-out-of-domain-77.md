---
type: claim
title: "The fine-tuned model generalized to out-of-domain lessons with 77% overall accuracy"
description: "The fine-tuned model generalized to out-of-domain lessons with 77% overall accuracy"
id: fine-tuned-model-out-of-domain-77
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
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

# The fine-tuned model generalized to out-of-domain lessons with 77% overall accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On a test set of 150 responses from six additional lessons, the fine-tuned model achieved 77% overall accuracy, performing similarly to its in-domain performance. [→ Bhushan 2025](#bhushan-2025)

## Evidence

### Bhushan 2025

Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. [doi:10.1007/978-3-032-03870-8_4](https://doi.org/10.1007/978-3-032-03870-8_4)

`q2 · i?` · `design · r2`

Out-of-domain evaluation on 150 responses from six additional lessons on the same platform, intended to test generalizability to different content in the same instructional context; the article reports "an overall accuracy of 77%" and similar performance to the in-domain test set.

> "we found that our fine-tuned model achieved an overall accuracy of 77% and performed similarly to the out-of-domain test set."

## Discussion


## Related Claims
- [A fine-tuned GPT-4o model outperforms GPTZero at detecting LLM-generated short answers in an online lesson, achieving 80% accuracy versus GPTZero's 70%](fine-tuned-gpt4o-outperforms-gptzero-short-answers.md) — related
- [A fine-tuned BERT encoder achieves the best agreement with human coding (AUROC 0.916) among three encoder variants on held-out student responses to the same four problems](bert-finetuned-best-auroc-sensemaking.md) — related
- [Fine-tuned Flan-T5 models perform very poorly on held-out Socratic debugging dialogues](flan-t5-finetuning-poor-socratic-debugging.md) — related
