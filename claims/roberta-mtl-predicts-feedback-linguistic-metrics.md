---
type: claim
title: A fine-tuned RoBERTa multi-task model predicts feedback linguistic metrics with low test MAEs
description: A fine-tuned RoBERTa multi-task model predicts feedback linguistic metrics with low test MAEs
id: roberta-mtl-predicts-feedback-linguistic-metrics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: antoun-yaacoub-2025
    resource: "https://doi.org/10.1109/iccsm66818.2025.00026"
    title: "Antoun Yaacoub, Zainab Assaghir, Lionel Prevost, Jérôme Da-Rugna. (2025). Analyzing Feedback Mechanisms in AI-Generated MCQs: Insights into Readability, Lexical Properties, and Levels of Challenge. ESIEA Lab / Lebanese University. [doi:10.1109/iccsm66818.2025.00026](https://doi.org/10.1109/iccsm66818.2025.00026)"
    author: Antoun Yaacoub, Zainab Assaghir, Lionel Prevost, Jérôme Da-Rugna
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A fine-tuned RoBERTa multi-task model predicts feedback linguistic metrics with low test MAEs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The RoBERTa-MTL model achieved test MAEs of 2.6 characters for length, 2.0 for Flesch-Kincaid Grade Level, 0.03 for vocabulary richness, and 0.04 for lexical density. [→ Antoun Yaacoub 2025](#antoun-yaacoub-2025)

## Evidence

### Antoun Yaacoub 2025

Antoun Yaacoub, Zainab Assaghir, Lionel Prevost, Jérôme Da-Rugna. (2025). Analyzing Feedback Mechanisms in AI-Generated MCQs: Insights into Readability, Lexical Properties, and Levels of Challenge. ESIEA Lab / Lebanese University. [doi:10.1109/iccsm66818.2025.00026](https://doi.org/10.1109/iccsm66818.2025.00026)

`q2 · i?` · `associational · r2`

Evaluation of a fine-tuned RoBERTa-base multi-task model (dropout 0.1, 10 epochs, AdamW) on a held-out test set, predicting four linguistic metrics of AI-generated feedback. The authors call the Flesch-Kincaid MAE of 2.0 "a strong result" given readability subjectivity.

> "The model achieves a test MAE of 2.6 characters for feedback length, 2.0 for Flesch -Kincaid Grade Level, 0.03 for vocabulary richness, and 0.04 for lexical density."

## Discussion


## Related Claims
- [AI-generated feedback length and readability increase with question difficulty](feedback-length-readability-increase-with-difficulty.md) — related
- [Fine-tuned RoBERTa detects sentence-level emotions in reflective essays with a micro F1 of 0.70](papagai-roberta-emotion-detection-f1-070.md) — related
- [A fine-tuned DistilRoBERTa recipe-quality predictor achieves a test-set MAE of 0.39, slightly better than but not significantly different from a mean-prediction baseline of 0.42.](relexset-predictor-mae-better-than-baseline.md) — related
- [The three fine-tuned LLMs differ significantly in response length, readability, and similarity to posts](llm-response-length-readability-differences.md) — related
