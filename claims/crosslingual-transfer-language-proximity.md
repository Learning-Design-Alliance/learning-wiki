---
type: claim
title: Crosslingual content scoring transfer works better between closely related languages, with Chinese the hardest target in this setup
description: Crosslingual content scoring transfer works better between closely related languages, with Chinese the hardest target in this setup
id: crosslingual-transfer-language-proximity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
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

# Crosslingual content scoring transfer works better between closely related languages, with Chinese the hardest target in this setup

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In Study 2, transfer between related languages such as French and Spanish worked well, while transfer involving Chinese performed far worse. [→ Andrea Horbach 2024](#andrea-horbach-2024)

## Evidence

### Andrea Horbach 2024

Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1

`q2 · i?` · `design · r2`

Experimental Study 2, crosslingual scoring experiments comparing logistic regression and M-BERT with and without machine translation across five target languages. The article reports the language-proximity pattern, with the worst gap for Chinese (.550 monolingual vs .457 best crosslingual).

> "Overall, we observe that the transfer often works well for highly related languages, such as Franch and Spanish, while for Chinese, which is in our setup phylogenetically farthest from the other languages, the transfer does not nearly work as well."

## Discussion


## Related Claims
- [Part of the crosslingual performance drop is attributable to differences between learner populations and datasets, not only language](dataset-population-differences-drive-scoring-drop.md) — related
- [Pretraining a multilingual transformer on the large English ASAP dataset and fine-tuning on small target-language data outperforms all monolingual and crosslingual baselines](pretrain-english-finetune-target-best-crosslingual-scoring.md) — related
- [Machine translation of training and test data does not degrade monolingual content scoring performance and can normalize learner errors](mt-normalizes-learner-errors-scoring.md) — related
- [M-BERT with machine translation is the best crosslingual method, outperforming logistic regression with MT and M-BERT zero-shot](mbert-with-mt-best-crosslingual-method.md) — related
- [Monolingual English BERT shows only a slight advantage over multilingual BERT for English content scoring](monolingual-bert-slight-advantage-over-mbert.md) — related
