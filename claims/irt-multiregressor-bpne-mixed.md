---
type: claim
title: On the Brazilian Portuguese Narrative Essays dataset, IRT adjustment of traditional models improved Kappa but reduced QWK and Pearson correlation, a mixed result
description: On the Brazilian Portuguese Narrative Essays dataset, IRT adjustment of traditional models improved Kappa but reduced QWK and Pearson correlation, a mixed result
id: irt-multiregressor-bpne-mixed
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
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

# On the Brazilian Portuguese Narrative Essays dataset, IRT adjustment of traditional models improved Kappa but reduced QWK and Pearson correlation, a mixed result

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On BPNE, the IRT-Multiregressor All Traditional approach obtained Kappa 0.347, QWK 0.450 and Pearson 0.456, improving Kappa by 15.7% and 23.0% over the best traditional and ensemble models but reducing QWK and Pearson correlation. [→ Bruno Alexandre Rosa 2025](#bruno-alexandre-rosa-2025)

## Evidence

### Bruno Alexandre Rosa 2025

Bruno Alexandre Rosa, Hilário Oliveira, Luiz Rodrigues, Eduardo Araujo Oliveira, Rafael Ferreira Mello. (2025). Enhancing Essay Cohesion Assessment: A Novel Item Response Theory Approach. arXiv preprint. [doi:10.48550/arXiv.2507.08487](https://doi.org/10.48550/arXiv.2507.08487)

`q2 · i?` · `design · r2`

Cross-validation results on the Brazilian Portuguese Narrative Essays dataset (Table 4, Results section). The IRT approach "improved Kappa by 15.7% and 23.0%" while QWK and Pearson correlation fell relative to the best traditional and ensemble models; no effect size printed.

> "The IRT-Multiregressor All Traditional approach obtained 0.347, 0.450, and 0.456, respectively. Compared to the best traditional and ensemble models, this approach improved Kappa by 15.7% and 23.0% but had a reduction of 10.7% and 4.7% in QWK and 13.1% and 11.4% in Pearson correlation, respectively."

## Discussion


## Related Claims
- [BERT-based models outperformed traditional machine learning models at predicting essay cohesion scores on both Portuguese datasets](bert-outperforms-traditional-cohesion.md) — related
- [On the extended Essay-BR dataset, the IRT-Multiregressor over traditional models improved Kappa, QWK and Pearson correlation over the best ensemble models](irt-multiregressor-traditional-eebr-gains.md) — related
- [On the extended Essay-BR dataset, the IRT-Multiregressor combining BERT models achieved the best overall Kappa, QWK and Pearson correlation, surpassing BERT-Base alone](irt-multiregressor-all-bert-best-eebr.md) — related
