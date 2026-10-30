---
type: claim
title: Monolingual English BERT shows only a slight advantage over multilingual BERT for English content scoring
description: Monolingual English BERT shows only a slight advantage over multilingual BERT for English content scoring
id: monolingual-bert-slight-advantage-over-mbert
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: andrea-horbach-2024
    resource: "https://doi.org/10.1007/s40593-023-00370-1"
    title: "Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1"
    author: Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Monolingual English BERT shows only a slight advantage over multilingual BERT for English content scoring

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Comparing the two transformer models on the three English datasets, results were mixed with a tendency favoring the monolingual model (.671 vs .660 average QWK). [→ Andrea Horbach 2024](#andrea-horbach-2024)

## Evidence

### Andrea Horbach 2024

Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1

`q2 · i?` · `design · r2`

Study 1 comparison of a monolingual English BERT and multilingual BERT on the three English datasets. The article reports mixed results with a slight monolingual advantage (.671 versus .660 average QWK) and chose M-BERT for all experiments for consistency.

> "Results are mixed, but we see a tendency that the monolingual BERT model indeed has a slight advantage over the multilingual model (.671 for the monolingual versus .660 for the multilingual model)."

## Discussion


## Related Claims
- [M-BERT with machine translation is the best crosslingual method, outperforming logistic regression with MT and M-BERT zero-shot](mbert-with-mt-best-crosslingual-method.md) — related
- [Pretraining a multilingual transformer on the large English ASAP dataset and fine-tuning on small target-language data outperforms all monolingual and crosslingual baselines](pretrain-english-finetune-target-best-crosslingual-scoring.md) — related
- [Crosslingual content scoring transfer works better between closely related languages, with Chinese the hardest target in this setup](crosslingual-transfer-language-proximity.md) — related
- [Machine translation of training and test data does not degrade monolingual content scoring performance and can normalize learner errors](mt-normalizes-learner-errors-scoring.md) — related
- [Domain adaptation through unsupervised pretraining gave mixed results: it slightly improved RoBERTa but degraded the Longformer for both Content and Wording](domain-adaptation-mixed-roberta-helped-longformer-hurt.md) — related
