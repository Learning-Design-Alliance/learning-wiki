---
type: claim
title: Machine learning algorithms optimizing overall accuracy are inherently biased against minority groups when group data amounts vary, even absent historical bias
description: Machine learning algorithms optimizing overall accuracy are inherently biased against minority groups when group data amounts vary, even absent historical bias
id: ml-accuracy-optimization-biased-against-minority-groups
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: kenneth-holstein-and-shayan-doroudi-2021
    resource: "https://doi.org/10.48550/arXiv.2104.12920"
    title: "Kenneth Holstein and Shayan Doroudi. (2021). Equity and Artificial Intelligence in Education: Will \"AIEd\" Amplify or Alleviate Inequities in Education?. [doi:10.48550/arXiv.2104.12920](https://doi.org/10.48550/arXiv.2104.12920)"
    author: Kenneth Holstein and Shayan Doroudi
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Machine learning algorithms optimizing overall accuracy are inherently biased against minority groups when group data amounts vary, even absent historical bias

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Even without historical bias in a dataset, most machine learning algorithms will be inherently biased against minority groups because optimizing overall accuracy can be achieved by tailoring predictions to the majority group at the expense of minority groups. [→ Kenneth Holstein and Shayan Doroudi 2021](#kenneth-holstein-and-shayan-doroudi-2021)

## Evidence

### Kenneth Holstein and Shayan Doroudi 2021

Kenneth Holstein and Shayan Doroudi. (2021). Equity and Artificial Intelligence in Education: Will "AIEd" Amplify or Alleviate Inequities in Education?. [doi:10.48550/arXiv.2104.12920](https://doi.org/10.48550/arXiv.2104.12920)

`q2 · i?` · `theoretical · r3`

The chapter argues, citing Hardt (2014), that when the amount of data differs across demographic groups, accuracy-optimizing algorithms tailor predictions to the majority group, leaving minority groups with less nuanced predictions — for example, an at-risk student detector trained at a majority-white college. No effect size is printed.

> "most machine learning algorithms will be inherently biased against minority groups in our data (Hardt, 2014). This is because the algorithm will try to optimize overall accuracy of a model, and it can achieve that accuracy by tailoring its predictions to that of a majority group (at the expense of minority groups), it will do so."

## Discussion


## Related Claims
- [Human–AI feedback loops can compound historical biases: simulated predictive policing reinforced bias against Black people at twice the rate of white people](human-ai-feedback-loops-compound-bias.md) — a narrower finding that bears on this claim
- [Machine perception and learning depend on large, unbiased training data](ai-big-ideas-data-and-knowledge-dependence.md) — related
- [Demographic variables (gender, URM, first-generation, SES) were of low importance in the DFW classification models, and subgroup classification accuracy was approximately equal to the overall model](demographic-variables-low-importance-dfw-models.md) — reports the opposite
- [Algorithmic bias and data privacy are central ethical risks of AI in adult education](algorithmic-bias-privacy-risks-adult-education.md) — a broader claim this one bears on
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](data-balancing-improves-accuracy-increases-bias.md) — related
