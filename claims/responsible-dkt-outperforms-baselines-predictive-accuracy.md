---
type: claim
title: Responsible-DKT outperforms a neural-symbolic baseline without knowledge injection and a fully data-driven PyTorch DKT in predictive accuracy across training ratios and sequence lengths
description: Responsible-DKT outperforms a neural-symbolic baseline without knowledge injection and a fully data-driven PyTorch DKT in predictive accuracy across training ratios and sequence lengths
id: responsible-dkt-outperforms-baselines-predictive-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hooshyar-2026
    resource: "https://doi.org/10.48550/arxiv.2604.08263"
    title: "Hooshyar, D.; Šír, G.; Yang, Y.; Kärkkäinen, T.; Hämäläinen, R.; Krivich, E.; Cukurova, M.; Gašević, D.; Azevedo, R. (2026). Neural-Symbolic Knowledge Tracing: Injecting Educational Knowledge into Deep Learning for Responsible Learner Modelling. arXiv preprint. https://arxiv.org/abs/2604.08263 [doi:10.48550/arxiv.2604.08263](https://doi.org/10.48550/arxiv.2604.08263)"
    author: Hooshyar, D.; Šír, G.; Yang, Y.; Kärkkäinen, T.; Hämäläinen, R.; Krivich, E.; Cukurova, M.; Gašević, D.; Azevedo, R.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Responsible-DKT outperforms a neural-symbolic baseline without knowledge injection and a fully data-driven PyTorch DKT in predictive accuracy across training ratios and sequence lengths

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Responsible-DKT achieves over 0.80 AUC with only 10% of training data and reaches up to 0.90 AUC, improving performance by up to 13% over the baseline models. [→ Hooshyar 2026](#hooshyar-2026)

## Evidence

### Hooshyar 2026

Hooshyar, D.; Šír, G.; Yang, Y.; Kärkkäinen, T.; Hämäläinen, R.; Krivich, E.; Cukurova, M.; Gašević, D.; Azevedo, R. (2026). Neural-Symbolic Knowledge Tracing: Injecting Educational Knowledge into Deep Learning for Responsible Learner Modelling. arXiv preprint. https://arxiv.org/abs/2604.08263 [doi:10.48550/arxiv.2604.08263](https://doi.org/10.48550/arxiv.2604.08263)

`q2 · i?` · `design · r2`

The paper reports experiments on a real-world dataset of 6th-grade students' Maths interactions, comparing Responsible-DKT against BaseNS-DKT and Classic-DKT across training ratios and sequence lengths; the abstract reports "over 0.80 AUC with only 10% of training data" and up to 0.90 AUC, a 13% improvement over baselines. No per-condition test statistics are printed in the available text.

> "The model achieves over 0.80 AUC with only 10% of training data and reaches up to 0.90 AUC, improving performance by up to 13% over the baseline models."

## Discussion


## Related Claims
- [Symbolic knowledge injection improves temporal reliability of predictions, yielding lower early- and mid-sequence errors and the lowest prediction inconsistency rates across sequence lengths](responsible-dkt-temporal-reliability.md) — related
- [The neural-symbolic architecture enables empirical evaluation of embedded pedagogical rules, showing that repeated-incorrect (non-mastery) patterns play a stronger role in prediction updates](non-mastery-rules-stronger-prediction-role.md) — related
