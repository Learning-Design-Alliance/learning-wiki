---
type: claim
title: BERT-based models outperformed traditional machine learning models at predicting essay cohesion scores on both Portuguese datasets
description: BERT-based models outperformed traditional machine learning models at predicting essay cohesion scores on both Portuguese datasets
id: bert-outperforms-traditional-cohesion
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

# BERT-based models outperformed traditional machine learning models at predicting essay cohesion scores on both Portuguese datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the BPNE dataset, BERT-Base obtained the highest scores among individual models for Kappa (0.354), QWK (0.547) and Pearson correlation (0.584), better than traditional models. [→ Bruno Alexandre Rosa 2025](#bruno-alexandre-rosa-2025)

## Evidence

### Bruno Alexandre Rosa 2025

Bruno Alexandre Rosa, Hilário Oliveira, Luiz Rodrigues, Eduardo Araujo Oliveira, Rafael Ferreira Mello. (2025). Enhancing Essay Cohesion Assessment: A Novel Item Response Theory Approach. arXiv preprint. [doi:10.48550/arXiv.2507.08487](https://doi.org/10.48550/arXiv.2507.08487)

`q2 · i?` · `design · r2`

Cross-validation comparison on the Brazilian Portuguese Narrative Essays dataset (Table 4, Results section). The article states "BERT-based models obtained better scores than traditional models", with BERT-Base highest on all three metrics; no effect size printed.

> "As seen in Table 4, BERT-based models obtained better scores than traditional models. The BERT-Base model obtained the highest scores for Kappa (0.354), QWK (0.547), and Pearson correlation (0.584)."

## Discussion


## Related Claims
- [On the Brazilian Portuguese Narrative Essays dataset, IRT adjustment of traditional models improved Kappa but reduced QWK and Pearson correlation, a mixed result](irt-multiregressor-bpne-mixed.md) — related
- [On the extended Essay-BR dataset, the IRT-Multiregressor combining BERT models achieved the best overall Kappa, QWK and Pearson correlation, surpassing BERT-Base alone](irt-multiregressor-all-bert-best-eebr.md) — related
- [On the extended Essay-BR dataset, the IRT-Multiregressor over traditional models improved Kappa, QWK and Pearson correlation over the best ensemble models](irt-multiregressor-traditional-eebr-gains.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — a broader claim this one bears on
