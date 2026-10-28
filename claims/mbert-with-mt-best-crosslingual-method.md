---
type: claim
title: M-BERT with machine translation is the best crosslingual method, outperforming logistic regression with MT and M-BERT zero-shot
description: M-BERT with machine translation is the best crosslingual method, outperforming logistic regression with MT and M-BERT zero-shot
id: mbert-with-mt-best-crosslingual-method
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: andrea-horbach-2024
    resource: "https://doi.org/10.1007/s40593-023-00370-1"
    title: "Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1"
    author: Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# M-BERT with machine translation is the best crosslingual method, outperforming logistic regression with MT and M-BERT zero-shot

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across Study 2 blocks, the M-BERT setting almost always outperformed logistic regression, and machine translation was beneficial compared with zero-shot multilingual representations. [→ Andrea Horbach 2024](#andrea-horbach-2024)

## Evidence

### Andrea Horbach 2024

Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1

`q2 · i?` · `causal · r2`

Experimental Study 2 comparing three crosslingual methods per target-language block in QWK. The article reports that "the M-BERT setting almost always outperforms logistic regression" and that MT helps over zero-shot, with no clear train-vs-test translation preference.

> "we see that the M-BERT setting almost always outperforms logistic regression and that machine translation is beneficial (comparing M-BERT MT with zero-shot). The best crosslingual method per block (highlighted in bold print) is often M-BERT with MT with no clear tendency whether translating training or test data is more beneficial."

## Discussion


## Related Claims
- [Crosslingual content scoring transfer works better between closely related languages, with Chinese the hardest target in this setup](crosslingual-transfer-language-proximity.md) — related
- [Pretraining a multilingual transformer on the large English ASAP dataset and fine-tuning on small target-language data outperforms all monolingual and crosslingual baselines](pretrain-english-finetune-target-best-crosslingual-scoring.md) — related
- [Monolingual English BERT shows only a slight advantage over multilingual BERT for English content scoring](monolingual-bert-slight-advantage-over-mbert.md) — related
- [Machine translation of training and test data does not degrade monolingual content scoring performance and can normalize learner errors](mt-normalizes-learner-errors-scoring.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
