---
type: claim
title: All three assertion sources (word, corpus-derived, construct-derived) contribute to predictive accuracy
description: All three assertion sources (word, corpus-derived, construct-derived) contribute to predictive accuracy
id: all-assertion-sources-contribute-predictive-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
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

# All three assertion sources (word, corpus-derived, construct-derived) contribute to predictive accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models using words plus corpus-derived and construct-derived assertions reached macro-F1 0.527–0.673 against 0.339 for words only; the authors conclude all three sources contribute, though Table 1 reports no words-plus-construct-derived-only condition. [→ Julian Bernado 2026](#julian-bernado-2026)

## Evidence

### Julian Bernado 2026

Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043 [doi:10.48550/arxiv.2609.27043](https://doi.org/10.48550/arxiv.2609.27043)

`q2 · i?` · `design · r2`

Comparison in the TalkMoves classification experiment against a word-only baseline (macro-F1 0.339) and against annotators' corpus-only conditions. The article finds that "all three assertion sources contribute to predictive accuracy as measured by Macro-F1 and Cohen's κ."

> "Overall, we find that all three assertion sources contribute to predictive accuracy as measured by Macro-F1 and Cohen's κ."

## Discussion


## Related Claims
- [Cross-model agreement on assertions is moderate (median 0.401) and higher among construct-derived than corpus-derived assertions](assertion-cross-model-agreement-moderate-median-0401.md) — related
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — a broader claim this one bears on
- [LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)](llm-features-add-value-beyond-item-metadata.md) — a broader claim this one bears on
- [Episode-composition and transition features contribute predictive process evidence beyond semantics, with Epi.+Tran. reaching 0.136 permutation importance versus 0.084 for Sem. in the Both (Role) setting](episode-features-predictive-importance-beyond-semantics.md) — a broader claim this one bears on
- [EduBehaviors achieves 0.673 macro-F1 and 0.688 Cohen's kappa on Teacher TalkMoves, generally improving over direct LLM prompting](edubehaviors-matches-direct-llm-prompting-talkmoves.md) — related
- [EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
- [Reviewed CSCL systems are further characterized by interaction data type, derivation processes, and feedback type](cscl-systems-characterized-data-processes-feedback.md) — related
