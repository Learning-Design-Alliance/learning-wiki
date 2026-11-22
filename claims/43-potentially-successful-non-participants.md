---
type: claim
title: "Applying the model at a high-confidence threshold identifies 43 non-participants (3.9%) as potentially successful in the Physics Olympiad"
description: "Applying the model at a high-confidence threshold identifies 43 non-participants (3.9%) as potentially successful in the Physics Olympiad"
id: 43-potentially-successful-non-participants
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tschisgale-2026
    resource: "https://doi.org/10.48550/arXiv.2609.35151"
    title: "Tschisgale, P., & Neumann, K. (2026). “What If I Had Participated?”—A Machine Learning-Based Counterfactual Analysis of Non-Participants’ Success Potential in STEM Competitions: The Case of the German Physics Olympiad. Leibniz Institute for Science and Mathematics Education (IPN), Kiel, Germany. [doi:10.48550/arXiv.2609.35151](https://doi.org/10.48550/arXiv.2609.35151)"
    author: "Tschisgale, P., & Neumann, K."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Applying the model at a high-confidence threshold identifies 43 non-participants (3.9%) as potentially successful in the Physics Olympiad

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A precision-targeting threshold of p = .58 (precision proxy 78.9%) identified 43 of 1,103 non-participants as potentially successful. [→ Tschisgale 2026](#tschisgale-2026)

## Evidence

### Tschisgale 2026

Tschisgale, P., & Neumann, K. (2026). “What If I Had Participated?”—A Machine Learning-Based Counterfactual Analysis of Non-Participants’ Success Potential in STEM Competitions: The Case of the German Physics Olympiad. Leibniz Institute for Science and Mathematics Education (IPN), Kiel, Germany. [doi:10.48550/arXiv.2609.35151](https://doi.org/10.48550/arXiv.2609.35151)

`q2 · i?` · `associational · r2`

The final elastic net model was applied to 1,103 non-participants, assigning each a predicted probability of first-round success. Precision was prioritized over recall, targeting a precision proxy of ≈ 80%; the selected threshold "p = .58" yielded a precision proxy of 78.9% and identified 43 students (3.9%).

> "The precision-targeting procedure (≈ 80% target) selected a threshold of p = .58, at which the precision proxy reached 78.9% (see Figure 4). At this threshold, 43 non-participants (3.9% of the sample) were identified as potentially successful"

## Discussion


## Related Claims
- [74.4% of potentially successful non-participants had previously entered at least one selective STEM competition, leaving 11 students unreached](74-percent-reached-through-other-competitions.md) — related
- [Elastic net logistic regression performs comparably to random forest and gradient boosting in predicting first-round Physics Olympiad success and is selected as the final model](elastic-net-comparable-performance-olympiad-success.md) — related
