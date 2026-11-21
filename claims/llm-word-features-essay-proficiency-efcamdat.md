---
type: claim
title: Word-level CEFR distributions predicted with an LLM differentiate essay-level proficiency bands better than PoS-based predictions and yield stronger holistic-score correlations on EFCAMDAT
description: Word-level CEFR distributions predicted with an LLM differentiate essay-level proficiency bands better than PoS-based predictions and yield stronger holistic-score correlations on EFCAMDAT
id: llm-word-features-essay-proficiency-efcamdat
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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
  - id: stefano-bannò-2025-2
    resource: "https://doi.org/10.18653/v1/2025.bea-1.45"
    title: "Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)"
    author: Stefano Bannò, Kate M. Knill, Mark J. F. Gales
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Word-level CEFR distributions predicted with an LLM differentiate essay-level proficiency bands better than PoS-based predictions and yield stronger holistic-score correlations on EFCAMDAT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On EFCAMDAT, vocabulary features extracted with Qwen 2.5 32B consistently outperform PoS-based features for predicting holistic essay scores, e.g. SVR PCC 0.771 vs 0.734 and naive-classifier PCC 0.636 vs 0.580. [→ Stefano Bannò 2025](#stefano-banno-2025)
`q2 i?` Cumulative distribution plots of predicted word-level CEFR levels show larger gaps between essay proficiency bands with Qwen than with the PoS-based model, indicating better differentiation across levels. [→ Stefano Bannò 2025 (2)](#stefano-banno-2025-2)

## Evidence

### Stefano Bannò 2025

Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)

`q2 · i?` · `associational · r2`

Essay-level experiment on 6,000 EFCAMDAT essays (1,000 per CEFR level), using predicted word-level CEFR proportions as features in a naive weighted classifier and an SVR with 5-fold cross-validation (Table 3). Qwen features give PCC 0.771 / SRC 0.749 (SVR) versus 0.734 / 0.713 for PoS features.

> "When used as features for predicting holistic scores, the vocabulary information extracted with Qwen consistently outperforms that derived from the PoS-based model both in the naive classifier and by the SVR."

### Stefano Bannò 2025 (2)

Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)

`q2 · i?` · `design · r2`

Figure-based analysis (Figures 5 and 6) of the predicted normalised distribution of words per word-level CEFR level across essay-level CEFR levels in EFCAMDAT, with eCDF of AUC values; the printed text states larger gaps "when using Qwen compared to the PoS-based model".

> "In both figures, we observe larger gaps – indicating better differentiation across levels – when using Qwen compared to the PoS-based model."

## Discussion


## Related Claims
- [On ELLIPSE, SVR predictions from LLM-extracted word-level vocabulary features correlate most strongly with the Vocabulary and Phraseology analytic scores](ellipse-vocabulary-analytic-correlation.md) — related
- [LLMs outperform a PoS-based baseline and a random baseline on word-level CEFR prediction of L2 learner writing, with the largest gains on ambiguous words](llms-beat-pos-baseline-word-level-cefr.md) — related
- [Rank-based metrics can be misleading for analytic assessment: systems prompted for holistic scoring achieve strong, sometimes stronger, correlations with analytic scores than when prompted for those aspects](rank-based-metrics-misleading-analytic-assessment.md) — related
