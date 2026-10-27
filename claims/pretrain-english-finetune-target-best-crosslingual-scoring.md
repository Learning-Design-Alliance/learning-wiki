---
type: claim
title: Pretraining a multilingual transformer on the large English ASAP dataset and fine-tuning on small target-language data outperforms all monolingual and crosslingual baselines
description: Pretraining a multilingual transformer on the large English ASAP dataset and fine-tuning on small target-language data outperforms all monolingual and crosslingual baselines
id: pretrain-english-finetune-target-best-crosslingual-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
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

# Pretraining a multilingual transformer on the large English ASAP dataset and fine-tuning on small target-language data outperforms all monolingual and crosslingual baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In Study 3, M-BERT models pretrained on about 2000 English answers and fine-tuned on about 270 target-language answers outperformed all three baselines for every target dataset. [→ Andrea Horbach 2024](#andrea-horbach-2024)

## Evidence

### Andrea Horbach 2024

Andrea Horbach, Joey Pehlke, Ronja Laarmann-Quante, Yuning Ding. (2024). Crosslingual Content Scoring in Five Languages Using Machine-Translation and Multilingual Transformer Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00370-1

`q2 · i?` · `design · r2`

Experimental Study 3, a fine-tuning experiment with M-BERT pretrained on the original English ASAP data and fine-tuned per target language via cross-validation. The article reports that "in all cases results outperform all three baselines", e.g. QWK .783 for French versus a .726 monolingual baseline.

> "We see that in all cases results outperform all three baselines. The improvement over the monolingual baseline indicates that we indeed benefit from more training data than the approximately 300 training instances in each dataset, even if it is not in the target language."

## Discussion


## Related Claims
- [Crosslingual content scoring transfer works better between closely related languages, with Chinese the hardest target in this setup](crosslingual-transfer-language-proximity.md) — related
- [M-BERT with machine translation is the best crosslingual method, outperforming logistic regression with MT and M-BERT zero-shot](mbert-with-mt-best-crosslingual-method.md) — related
- [Monolingual English BERT shows only a slight advantage over multilingual BERT for English content scoring](monolingual-bert-slight-advantage-over-mbert.md) — related
