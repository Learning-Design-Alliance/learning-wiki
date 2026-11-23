---
type: claim
title: Unmodified gradient saliency explanations help end-users realize the most important features in NLP predictions
description: Unmodified gradient saliency explanations help end-users realize the most important features in NLP predictions
id: unmodified-saliency-explanations-highlight-important-features
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: adel-rahimi-2022
    resource: "https://doi.org/10.48550/arXiv.2211.15351"
    title: "Adel Rahimi, Shaurya Jain. (2022). Testing the effectiveness of saliency-based explainability in NLP using randomized survey-based experiments. [doi:10.48550/arXiv.2211.15351](https://doi.org/10.48550/arXiv.2211.15351)"
    author: Adel Rahimi, Shaurya Jain
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Unmodified gradient saliency explanations help end-users realize the most important features in NLP predictions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Participants mainly agreed with predictions and top-weighted words when shown unmodified gradient explanations, averaging 4.02 out of 5 agreement points. [→ Adel Rahimi 2022](#adel-rahimi-2022)

## Evidence

### Adel Rahimi 2022

Adel Rahimi, Shaurya Jain. (2022). Testing the effectiveness of saliency-based explainability in NLP using randomized survey-based experiments. [doi:10.48550/arXiv.2211.15351](https://doi.org/10.48550/arXiv.2211.15351)

`q2 · i?` · `causal · r1`

Survey responses to predictions with unmodified simple gradient explanations; the article reports an average of 4.02/5 (median 4, range 2-5, mode 4). The authors interpret this as explanations "effective in helping end-users realise the most important features in predictions in a consumable form."

> "The high average score shows that survey-takers were mainly aligned with the predictions and the top-weighted words for classifying the sentences with unmodiﬁed explanations."

## Discussion


## Related Claims
- Survey participants averaged 6.43 out of 10 in correctly accepting unmodified saliency explanations and rejecting fabricated ones — a broader claim this one bears on
- Simple gradient explanations in NLP are not effective for people assessing the accuracy of a model or understanding its internals — related
- Participants often agreed with predictions justified by fabricated (randomly highlighted) saliency explanations — related
