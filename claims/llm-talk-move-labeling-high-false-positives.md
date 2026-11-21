---
type: claim
title: LLMs classifying Talk Moves show higher recall than precision, overproducing labels at a high false-positive rate
description: LLMs classifying Talk Moves show higher recall than precision, overproducing labels at a high false-positive rate
id: llm-talk-move-labeling-high-false-positives
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kirk-vanacore-and-rené-f-kizilcec-2026
    resource: "https://doi.org/10.1145/3774398.3811605"
    title: "Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)"
    author: Kirk Vanacore and René F. Kizilcec
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLMs classifying Talk Moves show higher recall than precision, overproducing labels at a high false-positive rate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All evaluated models displayed higher recall than precision, tending to overproduce labels and yielding relatively high false-positive rates even in the best-performing configuration. [→ Kirk Vanacore and René F. Kizilcec 2026](#kirk-vanacore-and-rene-f-kizilcec-2026)

## Evidence

### Kirk Vanacore and René F. Kizilcec 2026

Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)

`q2 · i?` · `causal · r2`

Overall performance analysis in the results section of the benchmark experiment. The article reports that all six models "tended to overproduce labels, resulting in a relatively high rate of false positives"; no standardized effect size is printed.

> "all models displayed higher recall than precision, suggesting that while models were able to identify many true instances, they also tended to overproduce labels, resulting in a relatively high rate of false positives."

## Discussion


## Related Claims
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [GPT-3's recall varies significantly across talk moves, performing far worse than RoBERTa for Connecting](gpt3-recall-varies-connecting-worst.md) — related
- [GPT-3 achieves higher precision than RoBERTa for every talk-move classifier, with gains of at least 5 and up to 21 points](gpt3-higher-precision-than-roberta-talk-moves.md) — related
