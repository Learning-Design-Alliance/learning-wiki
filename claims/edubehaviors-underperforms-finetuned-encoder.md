---
type: claim
title: EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data
description: EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data
id: edubehaviors-underperforms-finetuned-encoder
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

# EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Despite generally beating direct prompting, EduBehaviors strictly underperforms the specialized fine-tuned classifier (RoBERTa-base at 0.76 macro-F1) trained on gold TalkMoves labels. [→ Julian Bernado 2026](#julian-bernado-2026)

## Evidence

### Julian Bernado 2026

Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043

`q2 · i?` · `design · r2`

Stated comparison in the Limitations section, benchmarking against the fine-tuned RoBERTa-base result (0.76 macro-F1, no agreement metrics) reported in the original TalkMoves paper. The framework "strictly underperforms the original fined-tuned encoder-based classifier."

> "While our framework outperforms directly prompting LLMs in most of the tested cases, it strictly underperforms the original fined-tuned encoder-based classifier trained on the golden dataset annotated by experts."

## Discussion


## Related Claims
- [EduBehaviors achieves 0.673 macro-F1 and 0.688 Cohen's kappa on Teacher TalkMoves, generally improving over direct LLM prompting](edubehaviors-matches-direct-llm-prompting-talkmoves.md) — related
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related
