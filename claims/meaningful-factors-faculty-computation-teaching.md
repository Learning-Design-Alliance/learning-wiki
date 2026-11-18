---
type: claim
title: The most predictive factors of faculty having experience teaching computation are using computation in research with students, not personally using computation, and beliefs that computation brings new physics and new problems to the classroom
description: The most predictive factors of faculty having experience teaching computation are using computation in research with students, not personally using computation, and beliefs that computation brings new physics and new...
id: meaningful-factors-faculty-computation-teaching
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
sources:
  - id: nicholas-t-young-2019
    resource: "https://doi.org/10.1103/physrevphyseducres.15.010114"
    title: "Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)"
    author: Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: nicholas-t-young-2019-2
    resource: "https://doi.org/10.1103/physrevphyseducres.15.010114"
    title: "Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)"
    author: Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The most predictive factors of faculty having experience teaching computation are using computation in research with students, not personally using computation, and beliefs that computation brings new physics and new problems to the classroom

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Recursive backward elimination identified five meaningful features: "I use computation in research with students", "I do not personally use computation", "computation allows me to bring new physics into my classroom", "computation allows me to bring new problems into my classroom", and the highest physics degree offered by the institution. [→ Nicholas T. Young 2019](#nicholas-t-young-2019)
`q2 i?` Faculty with experience teaching computation tend to use computation to give undergraduate students research experience, while those without tend not to personally use computation and agree less that computation brings new physics and new problems. [→ Nicholas T. Young 2019 (2)](#nicholas-t-young-2019-2)

## Evidence

### Nicholas T. Young 2019

Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)

`q2 · i?` · `associational · r2`

Feature-importance analysis of the 30-trial conditional inference forest on 44 survey variables; importances were AUC-based permutation importances, and the meaningful set was selected via recursive backward elimination as printed in the Results section.

> "When we perform the recursive backward elimination technique, we ﬁnd that the meaningful features are “I use computation in research with students”, “I do not personally use computation”, “computation allows me to bring new physics into my classroom”, “computation allows me to bring new problems into my classroom”, and the highest physics degree oﬀered by the institution."

### Nicholas T. Young 2019 (2)

Nicholas T. Young, Grant Allen, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Identifying features predictive of faculty integrating computation into physics courses. [doi:10.1103/physrevphyseducres.15.010114](https://doi.org/10.1103/physrevphyseducres.15.010114)

`q2 · i?` · `associational · r2`

Response-distribution analysis of the five meaningful variables (Fig. 3), with χ2 tests with corrected p<0.05 printed for all five plots; direction words are the article's own 'tend to' hedges.

> "faculty who have experience teaching computation tend to use computation to provide undergraduate students with research experience while faculty who do not have experience teaching computation tend not to personally use computation"

## Discussion


## Related Claims
- [Model results are robust to varying training fraction and number of trees, but the highest-physics-degree factor is only marginally meaningful](hyperparameter-robustness-variable-importance.md) — related
- [Faculty at institutions offering only bachelors degrees in physics were more likely than faculty at any other institution type to have experience teaching computation](bachelors-institutions-more-likely-computation-teaching.md) — related
- [Demographic, departmental, and institutional factors are less useful predictors of faculty experience teaching computation](demographic-departmental-factors-less-predictive.md) — related
- [A reduced model using only the five meaningful features performs nearly as well as the full 44-feature model](five-feature-model-nearly-full-performance.md) — related
