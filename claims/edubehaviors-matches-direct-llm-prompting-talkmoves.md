---
type: claim
title: "EduBehaviors achieves 0.673 macro-F1 and 0.688 Cohen's kappa on Teacher TalkMoves, generally improving over direct LLM prompting"
description: "EduBehaviors achieves 0.673 macro-F1 and 0.688 Cohen's kappa on Teacher TalkMoves, generally improving over direct LLM prompting"
id: edubehaviors-matches-direct-llm-prompting-talkmoves
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: julian-bernado-2026
    resource: "https://arxiv.org/abs/2609.27043"
    title: "Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043"
    author: Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# EduBehaviors achieves 0.673 macro-F1 and 0.688 Cohen's kappa on Teacher TalkMoves, generally improving over direct LLM prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the TalkMoves Teacher TalkMoves task, the best EduBehaviors configuration attains 0.673 macro-F1 and 0.688 Cohen's kappa, generally outperforming direct LLM prompting (maximum reported macro-F1 0.61, kappa 0.58). [→ Julian Bernado 2026](#julian-bernado-2026)

## Evidence

### Julian Bernado 2026

Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043

`q2 · i?` · `design · r2`

Classification experiment on a sample of 10 TalkMoves sessions (3,217 teacher utterances) with leave-one-session-out cross validation, fitting L1-penalized logistic regression over assertion values. "GPT 5.6 Luna attains the highest Macro-F1 of 0.673, and Gemini 3.6 Flash attains the highest Cohen's κ of 0.702."

> "GPT 5.6 Luna attains the highest Macro-F1 of 0.673, and Gemini 3.6 Flash attains the highest Cohen's κ of 0.702."

## Discussion


## Related Claims
- [EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
