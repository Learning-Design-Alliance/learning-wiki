---
type: claim
title: Three-parameter IRT item curves fitted with the R mirt package reproduced Inep-provided ENEM scores with correlations above 0,995 in all studied years
description: Three-parameter IRT item curves fitted with the R mirt package reproduced Inep-provided ENEM scores with correlations above 0,995 in all studied years
id: irt-mirt-enem-score-validation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: barroso-2018
    resource: "https://doi.org/10.48550/arXiv.1802.09880"
    title: "Barroso, M. F., Rubini, G., & Silva, T. (2018). Dificuldades na aprendizagem de Física sob a ótica dos resultados do Enem. Originally published 2014. [doi:10.48550/arXiv.1802.09880](https://doi.org/10.48550/arXiv.1802.09880)"
    author: "Barroso, M. F., Rubini, G., & Silva, T."
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# Three-parameter IRT item curves fitted with the R mirt package reproduced Inep-provided ENEM scores with correlations above 0,995 in all studied years

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fitting the three-parameter logistic model with the mirt package in R yielded score correlations with Inep's provided scores above 0,995 in every year studied. [→ Barroso 2018](#barroso-2018)

## Evidence

### Barroso 2018

Barroso, M. F., Rubini, G., & Silva, T. (2018). Dificuldades na aprendizagem de Física sob a ótica dos resultados do Enem. Originally published 2014. [doi:10.48550/arXiv.1802.09880](https://doi.org/10.48550/arXiv.1802.09880)

`q2 · i?` · `associational · r?`

Methodological validation within the study: because Inep does not publish item parameters, the authors fitted the three-parameter logistic model using the mirt package in R on publicly released ENEM response data for completers from 2009 to 2014.

> "A utilização deste método para ajuste do modelo aos dados forneceu coeficientes de correlação entre os resultados para os escores obtidos e os escores fornecidos pelo Inep superiores a 0,995 em todos os anos estudados."

## Discussion


## Related Claims
- [Female Enem candidates score lower than male candidates on the Natural Sciences test and are relatively more represented in lower score deciles](enem-gender-gap-natural-sciences.md) — related
- [Independently estimated 3PL item parameters reproduce official Enem scores (R² = 0.9992), validating the researchers' mirt-based analysis pipeline](enem-mirt-parameters-validate-official-scores.md) — possibly the same claim (merge candidate)
- [Some Enem Natural Sciences items violate the monotonic increase postulated by the 3PL IRT model, raising unidimensionality concerns](enem-items-violate-irt-monotonicity.md) — related
