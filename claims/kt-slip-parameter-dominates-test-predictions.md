---
type: claim
title: After nominal mastery, variability in knowledge-tracing test predictions reflects persistent differences in the slip parameter rather than knowledge state
description: After nominal mastery, variability in knowledge-tracing test predictions reflects persistent differences in the slip parameter rather than knowledge state
id: kt-slip-parameter-dominates-test-predictions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-25
evidence_strength: moderate
newest_evidence: 1995
recheck_by: 1998
sources:
  - id: corbett-1995
    resource: "https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    title: "Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf"
    author: Albert T. Corbett and John R. Anderson
    q: 2
    i: 3
    kind: design
    rigour: 3
---

# After nominal mastery, variability in knowledge-tracing test predictions reflects persistent differences in the slip parameter rather than knowledge state

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2` · `i3` large
> **Currency** · newest study 1995 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 1998**: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Predicting test accuracy from knowledge probabilities alone greatly overestimates accuracy (predicted 0.99 vs actual 0.86 on test 3), and the correlation of ln(slip weight) with test accuracy is r=-0.72. [→ Corbett 1995](#corbett-1995)

## Evidence

### Corbett 1995

Albert T. Corbett and John R. Anderson. (1995). Knowledge tracing: Modeling the acquisition of procedural knowledge. CMU-CS-95-129, School of Computer Science, Carnegie Mellon University. https://reports-archive.adm.cs.cmu.edu/anon/1995/CMU-CS-95-129.pdf

`q2 · i3` · `design · r3`

Analysis in the Future Directions section of Experiment 4 data: predictions using only knowledge state probabilities (0.95-1.00 after mastery) overestimated third-test accuracy, and the article reports the correlation of ln(slip weight) and test accuracy as r = -0.72.

> "If test predictions are based solely on these knowledge probabilities without considering the performance parameters the model greatly overestimates average accuracy. The predicted accuracy for the third test under this model is 0.99 compared to an average actual accuracy of 0.86"

## Discussion


## Related Claims
- [Knowledge tracing predicts test performance well at intermediate learning levels but is insensitive to individual differences among students who have nominally reached mastery](kt-external-validity-test-prediction.md) — related
- [Incorporating individualized learning and performance parameter weights makes knowledge tracing sensitive to residual individual differences after nominal mastery](kt-individualized-parameter-weights.md) — related
- [BKT's interpretable latent estimates may not be as useful as thought, though BKT retains uses where model structure must be explained](bkt-latent-estimates-less-useful-than-thought.md) — related
- [Standard knowledge tracing models in use do not allow individual learning rates or individualized initial knowledge](standard-knowledge-tracing-lacks-individualization.md) — related
