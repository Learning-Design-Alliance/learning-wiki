---
type: claim
title: "Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data"
description: "Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data"
id: edubehaviors-underperforms-finetuned-encoder
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-07
recheck_by: 2029
sources:
  - id: julian-bernado-2026
    resource: "https://doi.org/10.48550/arxiv.2609.27043"
    title: "Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043 [doi:10.48550/arxiv.2609.27043](https://doi.org/10.48550/arxiv.2609.27043)"
    author: Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-11-07 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` EduBehaviors beat direct prompting in every tested case that used LLM-annotated assertions, but only two models (Claude Opus 5.0 and Gemini 3.8 Flash) reached macro-F1 comparable to the fine-tuned classifier (RoBERTa-base at 0.76) trained on gold TalkMoves labels; the best configuration reached 0.764. [→ Julian Bernado 2026](#julian-bernado-2026)

## Evidence

### Julian Bernado 2026

Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043 [doi:10.48550/arxiv.2609.27043](https://doi.org/10.48550/arxiv.2609.27043)

`q2 · i?` · `design · r2`

Stated comparison in the Limitations section, benchmarking against the fine-tuned RoBERTa-base result (0.76 macro-F1, no agreement metrics) reported in the original TalkMoves paper. The best configuration (Claude Opus 5) reached macro-F1 0.764 and Cohen's κ 0.756; the authors judge only two models comparable to the fine-tuned classifier.

> "While we are able to demonstrate that the EduBehaviors framework outperforms directly prompting LLMs in all tested cases that used LLM-annotated assertions, only two models, Claude Opus 5.0 and Gemini 3.8 Flash, produced macro-F1 scores comparable to the original fine-tuned encoder-based classifier trained on the golden dataset annotated by experts."

## Discussion


## Related Claims
- [EduBehaviors achieves 0.764 macro-F1 and 0.756 Cohen's kappa on Teacher TalkMoves, improving over direct LLM prompting](edubehaviors-matches-direct-llm-prompting-talkmoves.md) — related
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related
- [A model trained only on the 300-conversation BEA dataset plateaus at 74.84% average macro F1 due to limited data size and diversity](small-labeled-data-plateaus-evaluator.md) — related
- [ModernBert classifiers are more consistent than out-of-the-box LLMs at facilitation timing prediction, outperforming them in three of five datasets](modernbert-beats-llms-facilitation-timing.md) — related
- [All three assertion sources (word, corpus-derived, construct-derived) contribute to predictive accuracy](all-assertion-sources-contribute-predictive-accuracy.md) — related
- [Fine-tuning BERT-based classifiers on LLM-augmented student-response data outperforms unaugmented training for all tested concepts](llm-augmentation-beats-unaugmented-small-education-data.md) — related
