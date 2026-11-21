---
type: claim
title: On the extended Essay-BR dataset, the IRT-Multiregressor over traditional models improved Kappa, QWK and Pearson correlation over the best ensemble models
description: On the extended Essay-BR dataset, the IRT-Multiregressor over traditional models improved Kappa, QWK and Pearson correlation over the best ensemble models
id: irt-multiregressor-traditional-eebr-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: bruno-alexandre-rosa-2025
    resource: "https://doi.org/10.48550/arXiv.2507.08487"
    title: "Bruno Alexandre Rosa, Hilário Oliveira, Luiz Rodrigues, Eduardo Araujo Oliveira, Rafael Ferreira Mello. (2025). Enhancing Essay Cohesion Assessment: A Novel Item Response Theory Approach. arXiv preprint. [doi:10.48550/arXiv.2507.08487](https://doi.org/10.48550/arXiv.2507.08487)"
    author: Bruno Alexandre Rosa, Hilário Oliveira, Luiz Rodrigues, Eduardo Araujo Oliveira, Rafael Ferreira Mello
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the extended Essay-BR dataset, the IRT-Multiregressor over traditional models improved Kappa, QWK and Pearson correlation over the best ensemble models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The IRT-Multiregressor All Traditional approach achieved Kappa 0.421, QWK 0.581 and Pearson 0.587 on EEBR, improvements of 66.4%, 8.0% and 1.2% over the best ensemble models. [→ Bruno Alexandre Rosa 2025](#bruno-alexandre-rosa-2025)

## Evidence

### Bruno Alexandre Rosa 2025

Bruno Alexandre Rosa, Hilário Oliveira, Luiz Rodrigues, Eduardo Araujo Oliveira, Rafael Ferreira Mello. (2025). Enhancing Essay Cohesion Assessment: A Novel Item Response Theory Approach. arXiv preprint. [doi:10.48550/arXiv.2507.08487](https://doi.org/10.48550/arXiv.2507.08487)

`q2 · i?` · `design · r2`

Cross-validation results on the extended Essay-BR dataset (Table 3, Results section). The IRT-adjusted combination of traditional regressors improved on Stacked Linear Regression, the best ensemble, with "improvements of 66.4%, 8.0%, and 1.2%"; no effect size printed.

> "The proposed IRT-Multiregressor All Traditional approach achieved Kappa (0.421), QWK (0.581) and Pearson correlation (0.587). These results represent improvements of 66.4%, 8.0%, and 1.2% over the best ensemble models, respectively."

## Discussion


## Related Claims
- [BERT-based models outperformed traditional machine learning models at predicting essay cohesion scores on both Portuguese datasets](bert-outperforms-traditional-cohesion.md) — related
- [On the extended Essay-BR dataset, the IRT-Multiregressor combining BERT models achieved the best overall Kappa, QWK and Pearson correlation, surpassing BERT-Base alone](irt-multiregressor-all-bert-best-eebr.md) — related
- [On the Brazilian Portuguese Narrative Essays dataset, IRT adjustment of traditional models improved Kappa but reduced QWK and Pearson correlation, a mixed result](irt-multiregressor-bpne-mixed.md) — related
