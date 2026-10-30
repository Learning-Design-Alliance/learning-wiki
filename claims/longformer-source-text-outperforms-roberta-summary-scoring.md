---
type: claim
title: "Including the textbook source text in the model input improves automated summary scoring accuracy, with Longformer explaining 82% of Content and 70% of Wording score variance versus 67% and 41% for summary-only RoBERTa"
description: "Including the textbook source text in the model input improves automated summary scoring accuracy, with Longformer explaining 82% of Content and 70% of Wording score variance versus 67% and 41% for summary-only RoBERTa"
id: longformer-source-text-outperforms-roberta-summary-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00395-0"
    title: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0"
    author: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Including the textbook source text in the model input improves automated summary scoring accuracy, with Longformer explaining 82% of Content and 70% of Wording score variance versus 67% and 41% for summary-only RoBERTa

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Longformer models that include both the summary and the source text achieve higher accuracy than RoBERTa models that consider only the summary, for both Content and Wording scores. [→ Morris 2025](#morris-2025)
`q2 i?` The Wording advantage is largest: the pretrained Longformer reported almost double the R2 value relative to the RoBERTa model. [→ Morris 2025](#morris-2025)

## Evidence

### Morris 2025

Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0

`q2 · i?` · `design · r2`

Comparison of four finetuned encoder-only LLMs on a held-out test set of 702 summaries from the training corpus, evaluated by correlation with human rater judgments and explained variance (R2). The Longformer with source text reached R2 of 0.82 (Content) and 0.70 (Wording) versus 0.67 and 0.41 for RoBERTa, "explaining 82% versus 67% of the variance, respectively."

> "For Content scores, the Longformer model, in which both the summary and the source were included in the input, achieved higher accuracy than the RoBERTa model that considered only the summary (explaining 82% versus 67% of the variance, respectively). For Wording scores, the Longformer model outperformed the RoBERTa model (explaining 70% versus 41% of the variance, respectively)."

## Discussion


## Related Claims
- [Domain adaptation through unsupervised pretraining gave mixed results: it slightly improved RoBERTa but degraded the Longformer for both Content and Wording](domain-adaptation-mixed-roberta-helped-longformer-hurt.md) — related
- [SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations](roberta-svm-most-accurate-scoring-pisa.md) — related
- A principal component analysis distills the seven-criterion summary rubric into two components, Content and Wording, explaining approximately 73% of shared variance — related
