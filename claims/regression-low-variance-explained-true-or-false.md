---
type: claim
title: Linear regression of midterm and final exam scores on paper-test scores explained little variance, corroborating the SRD finding, with variance inflation factors close to 1.
description: Linear regression of midterm and final exam scores on paper-test scores explained little variance, corroborating the SRD finding, with variance inflation factors close to 1.
id: regression-low-variance-explained-true-or-false
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: márton-benedek-and-balázs-r-sziklai-2025
    resource: "https://doi.org/10.48550/arXiv.2510.16019"
    title: "Márton Benedek and Balázs R. Sziklai. (2025). Impact of AI Tools on Learning Outcomes: Decreasing Knowledge and Over-Reliance. arXiv preprint. [doi:10.48550/arXiv.2510.16019](https://doi.org/10.48550/arXiv.2510.16019)"
    author: Márton Benedek and Balázs R. Sziklai
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Linear regression of midterm and final exam scores on paper-test scores explained little variance, corroborating the SRD finding, with variance inflation factors close to 1.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Final exam and midterm results explained very little of the variance in true-or-false test scores, with the offline group somewhat better in this regard. [→ Márton Benedek and Balázs R. Sziklai 2025](#marton-benedek-and-balazs-r-sziklai-2025)

## Evidence

### Márton Benedek and Balázs R. Sziklai 2025

Márton Benedek and Balázs R. Sziklai. (2025). Impact of AI Tools on Learning Outcomes: Decreasing Knowledge and Over-Reliance. arXiv preprint. [doi:10.48550/arXiv.2510.16019](https://doi.org/10.48550/arXiv.2510.16019)

`q2 · i?` · `causal · r1`

Linear regression analysis (Table 2, Figure 3) in the randomized course experiment, with true-or-false scores as dependent variable. The article states "If knowledge were the driving force behind the test scores we would expect to see much higherR2 values" and that VIF values close to 1 rule out multicollinearity.

> "The final exam and midterm results explain very little of the variance in the true-or-false test scores, although the offline group is somewhat better in this regard (see also Figure 3)."

## Discussion


## Related Claims
- [In a randomized course experiment with merged final-exam groups, the AI-permitted group scored slightly but significantly higher than the offline group on the offline true-or-false paper test, so Hypothesis 1 was not supported.](paper-test-significant-advantage-ai-group.md) — related
- [Sum of Ranking Differences analysis supported Hypothesis 2: paper-test rankings aligned with other test scores for the offline group, but for the AI group only the first midterm aligned and the second midterm ranked students nearly in the opposite way.](srd-alignment-offline-group-genuine-learning.md) — related
- [The AI-permitted group outperformed the offline group on both midterms, but on the final exam the offline group outperformed the AI group with no statistically significant difference.](ai-group-midterm-outperformance-final-null.md) — related
