---
type: claim
title: On ELLIPSE, SVR predictions from LLM-extracted word-level vocabulary features correlate most strongly with the Vocabulary and Phraseology analytic scores
description: On ELLIPSE, SVR predictions from LLM-extracted word-level vocabulary features correlate most strongly with the Vocabulary and Phraseology analytic scores
id: ellipse-vocabulary-analytic-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: stefano-bannò-2025
    resource: "https://doi.org/10.18653/v1/2025.bea-1.45"
    title: "Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)"
    author: Stefano Bannò, Kate M. Knill, Mark J. F. Gales
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# On ELLIPSE, SVR predictions from LLM-extracted word-level vocabulary features correlate most strongly with the Vocabulary and Phraseology analytic scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Despite high inter-correlation among ELLIPSE analytic scores, an SVR trained on holistic scores correlates most strongly with Vocabulary scores (PCC 0.637) followed by Phraseology (PCC 0.630), suggesting the features target lexical aspects of language. [→ Stefano Bannò 2025](#stefano-banno-2025)

## Evidence

### Stefano Bannò 2025

Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)

`q2 · i?` · `associational · r2`

Experiment on the ELLIPSE corpus (359 training and 175 test essays) using Qwen-extracted word-level CEFR features in an SVR trained on holistic scores, evaluated on holistic and analytic scores with PCC and SRC (Table 4). Overall PCC is 0.650; Vocabulary 0.637 and Phraseology 0.630 lead the analytic dimensions.

> "the SVR (trained on holistic scores) predictions correlate most strongly with the Vocabulary scores, followed by Phraseology, suggesting our features are effectively targeting lexical aspects of language."

## Discussion


## Related Claims
- [Word-level CEFR distributions predicted with an LLM differentiate essay-level proficiency bands better than PoS-based predictions and yield stronger holistic-score correlations on EFCAMDAT](llm-word-features-essay-proficiency-efcamdat.md) — related
