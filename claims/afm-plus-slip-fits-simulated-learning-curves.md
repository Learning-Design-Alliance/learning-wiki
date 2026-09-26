---
type: claim
title: The AFM+S model, which explicitly models non-zero tail error, fits simulated student data better than the standard AFM
description: The AFM+S model, which explicitly models non-zero tail error, fits simulated student data better than the standard AFM
id: afm-plus-slip-fits-simulated-learning-curves
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: weak
sources:
  - id: afm-1
    title: afm-1
    q: 2
    i: 1
---

# The AFM+S model, which explicitly models non-zero tail error, fits simulated student data better than the standard AFM

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` AFM+S better fit the simulated student data from all six conditions than AFM, with three-fold cross-validated RMSE of 0.240 versus 0.257. [→ afm-1](#afm-1)

## Evidence

### afm-1

Qiao Zhang and Christopher MacLellan “Going Online: A simulated student approach for evaluating knowledge tracing in the context of mastery learning”. 2021. In: Proceedings of The 14th International Conference on Educational Data Mining (EDM21). International Educational Data Mining Society, 331-337. https://educationaldatamining.org/edm2021/

`q2 · i1`

Methodological analysis of learning-curve estimation. AFM assumes performance monotonically converges to zero error, but simulated students receive many more practice opportunities (e.g., 80 vs. 30), making the tail-error bias non-trivial; AFM+S adds slipping parameters per KC.

> "The AFM+S model better ﬁt the simulated student data from all six conditions than the AFM model (three fold cross-validated RMSE = 0.240 vs. 0.257)."

## Discussion


## Related Claims
- [The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin](em-beats-sgd-fitting-spectral-bkt.md) — related
- [OptimNN achieves lower test RMSE than EM, CGD, and SGD for fitting BKT and its variants across four tutoring datasets](optimnn-lower-rmse-than-em-cgd-sgd.md) — related
- [No single learner model was best across the six datasets, justifying a broad multi-model approach](no-single-learner-model-best-across-datasets.md) — a broader claim this one bears on
- [Simulated students (Apprentice agents) can successfully evaluate online knowledge tracing models, exposing errors before costly classroom testing](simulated-students-evaluate-online-knowledge-tracing.md) — related
