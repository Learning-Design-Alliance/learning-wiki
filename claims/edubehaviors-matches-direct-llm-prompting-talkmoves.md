---
type: claim
title: "EduBehaviors achieves 0.764 macro-F1 and 0.756 Cohen's kappa on Teacher TalkMoves, improving over direct LLM prompting"
description: "EduBehaviors achieves 0.764 macro-F1 and 0.756 Cohen's kappa on Teacher TalkMoves, improving over direct LLM prompting"
id: edubehaviors-matches-direct-llm-prompting-talkmoves
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-06
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

# EduBehaviors achieves 0.764 macro-F1 and 0.756 Cohen's kappa on Teacher TalkMoves, improving over direct LLM prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-11-06 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the TalkMoves Teacher TalkMoves task, the best EduBehaviors configuration (Claude Opus 5 as annotator) attains 0.764 macro-F1 and 0.756 Cohen's kappa, and every LLM annotator tested outperforms the direct-prompting baseline (macro-F1 0.61, kappa 0.58); the MPNet encoders without per-call charges are competitive on macro-F1 (0.590) and higher on kappa (0.636). [→ Julian Bernado 2026](#julian-bernado-2026)

## Evidence

### Julian Bernado 2026

Julian Bernado, Ana Trindade Ribeiro, Xander Beberman, and Susanna Loeb. (2026). EduBehaviors: Assertion-Based Schemas for Auditable Coding of Educational Dialogues. https://arxiv.org/abs/2609.27043 [doi:10.48550/arxiv.2609.27043](https://doi.org/10.48550/arxiv.2609.27043)

`q2 · i?` · `design · r2`

Classification experiment on a random sample of 50 TalkMoves sessions (14,341 teacher utterances) with 5-fold session-grouped cross validation, fitting L1-penalized logistic regression over assertion values; encoders trained on those 50 sessions were also tested on 495 unseen sessions (153,985 teacher utterances). Claude Opus 5 gave the best result (macro-F1 0.764, κ 0.756), followed by Gemini 3.8 Flash (0.750, 0.731) and GPT-5.6 Luna (0.728, 0.722), against a direct-prompting baseline of 0.61 macro-F1 and κ 0.58.

> "Claude Opus 5 attains the highest Macro-F1 of 0.764 as well as the highest Cohen's κ of 0.756. ... All of our annotators outperform the direct prompting baseline (Macro-F1 of 0.61 and Cohen's κ of 0.58)."

## Discussion


## Related Claims
- [EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
- [ModernBert classifiers are more consistent than out-of-the-box LLMs at facilitation timing prediction, outperforming them in three of five datasets](modernbert-beats-llms-facilitation-timing.md) — a broader claim this one bears on
- [All three assertion sources (word, corpus-derived, construct-derived) contribute to predictive accuracy](all-assertion-sources-contribute-predictive-accuracy.md) — related
