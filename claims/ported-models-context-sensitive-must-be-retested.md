---
type: claim
title: A student model that is easily ported to another ITS may still fail there, because student behaviour depends on domain, interface, and the system that generated training data, so ported models must be re-tested.
description: A student model that is easily ported to another ITS may still fail there, because student behaviour depends on domain, interface, and the system that generated training data, so ported models must be re-tested.
id: ported-models-context-sensitive-must-be-retested
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2016
sources:
  - id: valdés-aguirre-2016
    resource: "https://doi.org/10.1007/s40593-016-0113-0"
    title: "Valdés Aguirre, B., Ramírez Uresti, J. A., & du Boulay, B. (2016). An Analysis of Student Model Portability. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0113-0"
    author: "Valdés Aguirre, B., Ramírez Uresti, J. A., & du Boulay, B."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: valdés-aguirre-2016-2
    resource: "https://doi.org/10.1007/s40593-016-0113-0"
    title: "Valdés Aguirre, B., Ramírez Uresti, J. A., & du Boulay, B. (2016). An Analysis of Student Model Portability. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0113-0"
    author: "Valdés Aguirre, B., Ramírez Uresti, J. A., & du Boulay, B."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A student model that is easily ported to another ITS may still fail there, because student behaviour depends on domain, interface, and the system that generated training data, so ported models must be re-tested.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Student behaviour differs across domains: a student might behave differently on a math problem than on a physics problem, and interface differences change behaviour too. [→ Valdés Aguirre 2016](#valdes-aguirre-2016)
`q2 i?` Machine-learning based models can overfit to the system that generated their training data. [→ Valdés Aguirre 2016 (2)](#valdes-aguirre-2016-2)

## Evidence

### Valdés Aguirre 2016

Valdés Aguirre, B., Ramírez Uresti, J. A., & du Boulay, B. (2016). An Analysis of Student Model Portability. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0113-0

`q2 · i?` · `design · r2`

In its context-sensitivity analysis, the article argues that even affect, motivation, and gaming models are not exempt from context, because "a student might behave differently when addressing a math problem compared to a physics problem" and the interface constrains what the student can do.

> "This means that a student might behave differently when addressing a math problem compared to a physics problem. The interface also plays an important role in how the student will behave, since the interface dictates what a student can and cannot do."

### Valdés Aguirre 2016 (2)

Valdés Aguirre, B., Ramírez Uresti, J. A., & du Boulay, B. (2016). An Analysis of Student Model Portability. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0113-0

`q2 · i?` · `design · r2`

The article attributes the overfitting risk to Paquette et al. (2015), stating that machine-learning models "can overfit to the system that generated the training data". This is the authors' interpretive warning, not a tested result.

> "This is also true for those model involving machine learning, which can overfit to the system that generated the training data (Paquette et al. 2015)."

## Discussion


## Learner Variables
- [Domain Context](../learner-variables/domain-context.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [AI models trained on MOOC completion data risk bias toward high-performing learners, and machine-learned assessment reflects interaction rather than learning](mooc-ai-bias-toward-completers-and-interaction-not-learning.md) — related
- [Algorithmic empathy is culturally fragile: emotional inference errors in socio-emotional AI can invalidate teachers' experiences, so systems require local validation and participatory design](cultural-fragility-algorithmic-empathy.md) — related
