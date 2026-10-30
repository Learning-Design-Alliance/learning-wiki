---
type: claim
title: "Domain adaptation through unsupervised pretraining gave mixed results: it slightly improved RoBERTa but degraded the Longformer for both Content and Wording"
description: "Domain adaptation through unsupervised pretraining gave mixed results: it slightly improved RoBERTa but degraded the Longformer for both Content and Wording"
id: domain-adaptation-mixed-roberta-helped-longformer-hurt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: mixed
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

# Domain adaptation through unsupervised pretraining gave mixed results: it slightly improved RoBERTa but degraded the Longformer for both Content and Wording

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Training from a domain-adapted model improved RoBERTa performance slightly compared to finetuning from the pretrained model. [→ Morris 2025](#morris-2025)
`q2 i?` The domain-adapted Longformer performed worse than the non-domain-adapted version for both content and wording, explaining 72% and 60% of the variance respectively. [→ Morris 2025](#morris-2025)

## Evidence

### Morris 2025

Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0

`q2 · i?` · `design · r2`

Results section comparison of pretrained versus domain-adapted (on 93,484 unlabeled Commonlit summaries from six sources) versions of each model on the held-out test set. The domain-adapted Longformer reached R2 of 0.72 (Content) and 0.60 (Wording), below its pretrained counterpart.

> "Training from a domain adapted model improved performance slightly in the Roberta model compared to finetuning from the pretrained model. However, the domain adapted Longformer model performed worse than the non-domain adapted version for both content and wording (explaining 72% and 60% of the variance, respectively)."

## Discussion


## Related Claims
- [Including the textbook source text in the model input improves automated summary scoring accuracy, with Longformer explaining 82% of Content and 70% of Wording score variance versus 67% and 41% for summary-only RoBERTa](longformer-source-text-outperforms-roberta-summary-scoring.md) — related
- [Monolingual English BERT shows only a slight advantage over multilingual BERT for English content scoring](monolingual-bert-slight-advantage-over-mbert.md) — related
