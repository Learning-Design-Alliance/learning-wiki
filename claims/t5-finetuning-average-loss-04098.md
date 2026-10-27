---
type: claim
title: The fine-tuned T5 question-extraction model reached an average training loss of 0.4098, indicating imperfect question extraction
description: The fine-tuned T5 question-extraction model reached an average training loss of 0.4098, indicating imperfect question extraction
id: t5-finetuning-average-loss-04098
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: sovrano-francesco-2024
    resource: "https://doi.org/10.1007/s40593-024-00399-w"
    title: "Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio. (2024). How to Improve the Explanatory Power of an Intelligent Textbook: a Case Study in Legal Writing. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00399-w"
    author: Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# The fine-tuned T5 question-extraction model reached an average training loss of 0.4098, indicating imperfect question extraction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Sovrano Francesco 2024: no comparison group (read from the study by two models, 2026-10-27)

## Subclaims
`q1 i?` After five epochs of fine-tuning on QAMR and QADiscourse, the T5 model's average loss was 0.4098, so extracted questions can contain errors that propagate downstream. [→ Sovrano Francesco 2024](#sovrano-francesco-2024)

## Evidence

### Sovrano Francesco 2024

Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio. (2024). How to Improve the Explanatory Power of an Intelligent Textbook: a Case Study in Legal Writing. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00399-w

`q1 · i?` · `causal · r2`

Numerical training result: T5 was fine-tuned on QAMR (107,880 questions) and QADiscourse (16,613 questions) for five epochs on four extraction tasks. The article notes the residual loss suggests no over-fitting but also that extracted questions "can be imperfect, containing errors that could propagate to the Intelligent Explanation Generator."

> "At the end of the training, the average loss was 0.4098, meaning that our fine-tuned T5 model cannot perfectly extract AMRs or EDUs from the text composing the training set."

## Discussion


## Related Claims
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — related
- [Reinforcement learning with a learned alignment reward substantially improves question-concept alignment after supervised fine-tuning, while answerability remains high throughout training](alignment-rl-improves-concept-alignment.md) — related
- [Special-issue evidence: a knowledge-graph-enriched legal-writing textbook led to better learning outcomes than baselines, and aggregated emoji annotations helped teachers identify challenging text](special-issue-textbook-enhancements-outcomes.md) — related
