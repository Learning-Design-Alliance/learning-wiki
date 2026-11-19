---
type: claim
title: Fine-tuned RoBERTa detects sentence-level emotions in reflective essays with a micro F1 of 0.70
description: Fine-tuned RoBERTa detects sentence-level emotions in reflective essays with a micro F1 of 0.70
id: papagai-roberta-emotion-detection-f1-070
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: solopova-2023
    resource: "https://doi.org/10.1007/978-3-031-42608-7_16"
    title: "Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)"
    author: Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned RoBERTa detects sentence-level emotions in reflective essays with a micro F1 of 0.70

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A multi-label sentence-level emotion classifier for reflective essays, built on pre-trained RoBERTa, achieved a micro F1 of 0.70 and a hamming score of 0.67 across all emotion labels. [→ Solopova 2023](#solopova-2023)

## Evidence

### Solopova 2023

Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)

`q2 · i?` · `design · r2`

Model-development evaluation on annotated reflective sentences: the article framed emotion detection as multi-label sentence-level classification and reports the RoBERTa model achieved "a micro F1 of 0.70 and a hamming score of 0.67 across all emotion labels".

> "We achieved the best results with a pre-trained RoBERTa [25] , with a micro F1 of 0.70 and a hamming score of 0.67 across all emotion labels."

## Discussion


## Related Claims
- [A new sentence-level emotion annotation of 6543 reflective sentences defines 17 emotion labels plus a no-emotion label](papagai-6543-sentence-emotion-annotation-17-labels.md) — related
- [Fine-tuned ELECTRA classifies Gibbs cycle phases in reflective sentences, with top-3 predictions reaching up to 98% F1](papagai-electra-gibbs-cycle-top3-f1-098.md) — related
- [The best-scoring prompt-engineered approaches did not match the fine-tuned models on emotion detection and Gibbs cycle tasks](papagai-finetuned-outperforms-gpt3-davinci.md) — related
