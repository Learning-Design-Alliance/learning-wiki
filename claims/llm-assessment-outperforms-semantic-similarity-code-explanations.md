---
type: claim
title: LLM-based automated assessment of student code self-explanations outperforms semantic similarity methods on a balanced classification task
description: LLM-based automated assessment of student code self-explanations outperforms semantic similarity methods on a balanced classification task
id: llm-assessment-outperforms-semantic-similarity-code-explanations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: arun-balajiee-lekshmi-narayanan-2026
    resource: "https://doi.org/10.48550/arxiv.2605.21614"
    title: "Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614 [doi:10.48550/arxiv.2605.21614](https://doi.org/10.48550/arxiv.2605.21614)"
    author: Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-based automated assessment of student code self-explanations outperforms semantic similarity methods on a balanced classification task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In 5-fold cross-validation on a balanced dataset, LLM-based scoring achieved F1 = 0.98 and accuracy = 0.96 while the best semantic similarity method reached F1 = 0.72 and accuracy = 0.65. [→ Arun-Balajiee Lekshmi-Narayanan 2026](#arun-balajiee-lekshmi-narayanan-2026)

## Evidence

### Arun-Balajiee Lekshmi-Narayanan 2026

Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614 [doi:10.48550/arxiv.2605.21614](https://doi.org/10.48550/arxiv.2605.21614)

`q2 · i?` · `design · r2`

Comparison experiment on the balanced SelfCode2.0 subset using 5-fold cross-validation, with LLMs run zero-shot and semantic similarity thresholds tuned on training folds. Table 1 reports LLM Behavior at "F1 = 0.98, Accuracy = 0.96" versus Deep Tutor, RoBERTa and GPT-SE (best F1 = 0.72, accuracy = 0.65).

> "the LLM Behavior (F1 = 0.98, Accuracy = 0.96) outperforms Deep Tutor (F1 = 0.69, Accuracy = 0.6) and RoBERTa (F1 = 0.7, Accuracy = 0.61)"

## Discussion


## Related Claims
- [LLM-based assessment can replace similarity-based methods because it needs no ground-truth response and no correctness threshold](llm-assessment-needs-no-ground-truth-or-threshold.md) — related
- [A construction-focused correctness rubric underperformed behavior-focused and undefined prompts for LLM scoring of code explanations](construction-rubric-underperformed-llm-scoring.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [LLM-based scoring produced fewer false negatives than Deep Tutor on a balanced test set, which the authors expect would spare students the frustration of correct explanations judged incorrect](llm-scoring-fewer-false-negatives-than-deep-tutor.md) — related
