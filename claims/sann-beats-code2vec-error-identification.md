---
type: claim
title: SANN code vectors outperform explainable baseline code2vec in logical error identification
description: SANN code vectors outperform explainable baseline code2vec in logical error identification
id: sann-beats-code2vec-error-identification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: muntasir-hoq-2025
    resource: "https://doi.org/10.48550/arXiv.2505.10913"
    title: "Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)"
    author: Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SANN code vectors outperform explainable baseline code2vec in logical error identification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On caughtSpeeding incorrect solutions, the proposed framework achieved 97% recall and 85% precision versus code2vec's 43% recall and 37% precision, and beat a naive baseline's RMSE of 1.65 with 0.45. [→ Muntasir Hoq 2025](#muntasir-hoq-2025)

## Evidence

### Muntasir Hoq 2025

Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)

`q2 · i?` · `design · r2`

Baseline comparison on incorrect caughtSpeeding solutions. Because expert labeling was labor-intensive, GPT-4o-mini with few-shot prompting was used as evaluator for both models' outputs; a naive baseline predicting average errors per problem achieved RMSE 1.65 versus the framework's 0.45.

> "Based on the evaluation, code2vec achieved a recall of 43% and a precision of 37%. Our framework outperformed code2vec with a recall of 97% and a precision of 85%."

## Discussion


## Related Claims
- [Expert evaluation shows high recall and precision for SANN-identified logical errors across five problems](sann-high-recall-precision-logical-errors.md) — related
- [Modified SANN outperforms baseline models in predicting program correctness](sann-outperforms-baselines-correctness-prediction.md) — related
- [LSTM model using SANN code embeddings predicts final exam grades better than baselines (R2 = 0.50, RMSE = 0.17)](sann-embeddings-predict-final-exam-grades.md) — related
- [Concatenating SANN code vectors with DKT inputs improves next-attempt prediction by about 10% AUC over original DKT](sann-code-vectors-improve-knowledge-tracing.md) — related
- [Pattern-based KC similarity retrieves bundle-aligned programming learning items better than code-embedding and other KC baselines in both retrieval directions](pattern-kc-retrieval-outperforms-baselines.md) — related
- [A SANN model pretrained on FalconCode and fine-tuned on LLM-generated synthetic code outperformed synthetic-only, pretrained-only, and GPT-4o baselines at predicting correctness on an unseen problem](fine-tuned-sann-outperforms-baselines-unseen-problem.md) — related
