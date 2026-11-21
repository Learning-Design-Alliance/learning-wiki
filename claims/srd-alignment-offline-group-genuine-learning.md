---
type: claim
title: "Sum of Ranking Differences analysis supported Hypothesis 2: paper-test rankings aligned with other test scores for the offline group, but for the AI group only the first midterm aligned and the second midterm ranked students nearly in the opposite way."
description: "Sum of Ranking Differences analysis supported Hypothesis 2: paper-test rankings aligned with other test scores for the offline group, but for the AI group only the first midterm aligned and the second midterm ranked s..."
id: srd-alignment-offline-group-genuine-learning
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
    rigour: 2
  - id: márton-benedek-and-balázs-r-sziklai-2025-2
    resource: "https://doi.org/10.48550/arXiv.2510.16019"
    title: "Márton Benedek and Balázs R. Sziklai. (2025). Impact of AI Tools on Learning Outcomes: Decreasing Knowledge and Over-Reliance. arXiv preprint. [doi:10.48550/arXiv.2510.16019](https://doi.org/10.48550/arXiv.2510.16019)"
    author: Márton Benedek and Balázs R. Sziklai
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Sum of Ranking Differences analysis supported Hypothesis 2: paper-test rankings aligned with other test scores for the offline group, but for the AI group only the first midterm aligned and the second midterm ranked students nearly in the opposite way.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the AI group only the first midterm fell left of the 0.05 significance threshold; the second midterm was close to the 0.95 threshold, meaning it ranked students in almost the exact opposite way. [→ Márton Benedek and Balázs R. Sziklai 2025](#marton-benedek-and-balazs-r-sziklai-2025)
`q2 i?` The offline group's SRD values clustered on the left side, and Hypothesis 2 was supported despite the weakened treatment effect. [→ Márton Benedek and Balázs R. Sziklai 2025 (2)](#marton-benedek-and-balazs-r-sziklai-2025-2)

## Evidence

### Márton Benedek and Balázs R. Sziklai 2025

Márton Benedek and Balázs R. Sziklai. (2025). Impact of AI Tools on Learning Outcomes: Decreasing Knowledge and Over-Reliance. arXiv preprint. [doi:10.48550/arXiv.2510.16019](https://doi.org/10.48550/arXiv.2510.16019)

`q2 · i?` · `causal · r2`

SRD analysis (Figure 2) comparing paper-test rankings of students to rankings from other test scores in the randomized course experiment. The article adds that the second midterm results are "close to the 0.95 threshold (XX19), meaning it ranks the students in almost the exact opposite way."

> "In case of the AI group, only the first midterm falls to the left of the 0.05 significance threshold (XX1). The other two measurements are indistinguishable from random rankings."

### Márton Benedek and Balázs R. Sziklai 2025 (2)

Márton Benedek and Balázs R. Sziklai. (2025). Impact of AI Tools on Learning Outcomes: Decreasing Knowledge and Over-Reliance. arXiv preprint. [doi:10.48550/arXiv.2510.16019](https://doi.org/10.48550/arXiv.2510.16019)

`q2 · i?` · `causal · r2`

SRD analysis in the Results section shows for the offline group the values "cluster on the left side of the distribution", so students who achieved good scores on the true-or-false test were the ones who excelled on other tests as well.

> "In particular, the final test score for the AI group falls right the 0.05 threshold, while that of the offline group fall left. Hence, Hypothesis 2 is supported by our data, despite the weakened treatment effect."

## Discussion


## Related Claims
- [In a randomized course experiment with merged final-exam groups, the AI-permitted group scored slightly but significantly higher than the offline group on the offline true-or-false paper test, so Hypothesis 1 was not supported.](paper-test-significant-advantage-ai-group.md) — related
- [Linear regression of midterm and final exam scores on paper-test scores explained little variance, corroborating the SRD finding, with variance inflation factors close to 1.](regression-low-variance-explained-true-or-false.md) — related
- [The AI-permitted group outperformed the offline group on both midterms, but on the final exam the offline group outperformed the AI group with no statistically significant difference.](ai-group-midterm-outperformance-final-null.md) — related
