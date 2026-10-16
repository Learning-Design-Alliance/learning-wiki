---
type: claim
title: Interaction patterns of benchmark datasets and real-world deployment categories are statistically distinct in the scaffolding-uptake space
description: Interaction patterns of benchmark datasets and real-world deployment categories are statistically distinct in the scaffolding-uptake space
id: benchmark-and-realworld-interaction-categories-statistically-distinct
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: neagu-2026
    resource: "https://doi.org/10.48550/arxiv.2606.15766"
    title: "Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B. (2026). Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments. Pluralistic Alignment Workshop @ ICML 2026. https://arxiv.org/abs/2606.15766 [doi:10.48550/arxiv.2606.15766](https://doi.org/10.48550/arxiv.2606.15766)"
    author: "Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Interaction patterns of benchmark datasets and real-world deployment categories are statistically distinct in the scaffolding-uptake space

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Pairwise PERMANOVA and PERMDISP tests found significant separation in centroid and dispersion among the three dataset categories. [→ Neagu 2026](#neagu-2026)

## Evidence

### Neagu 2026

Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B. (2026). Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments. Pluralistic Alignment Workshop @ ICML 2026. https://arxiv.org/abs/2606.15766 [doi:10.48550/arxiv.2606.15766](https://doi.org/10.48550/arxiv.2606.15766)

`q2 · i?` · `associational · r2`

Statistical validation in Section 4.1 over the combined nine-dataset corpus of 9,490 valid chats. The paper reports pairwise PERMANOVA at p<0.0001 and pairwise PERMDISP tests (p<0.001), finding "significant separation between the three categories".

> "We applied pairwise PERMANOV A (Anderson, 2001) tests (p<0.0001 ) onto the combined datasets of the three categories to evaluate the centroid and dispersion differences."

## Discussion


## Related Claims
- [Students in real-world chatbot deployments exhibit lower scaffolding uptake than benchmarks assume, frequently bypassing the chatbot's pedagogical framing](real-world-students-bypass-chatbot-scaffolding.md) — possibly the same claim (merge candidate)
- [Student uptake is only weakly and inconsistently correlated with chatbot scaffolding in real-world deployments](weak-inconsistent-scaffolding-uptake-correlation-real-world.md) — related
- [AI tutor benchmark datasets show essentially no correlation between chatbot scaffolding and student uptake](no-scaffolding-uptake-correlation-in-benchmarks.md) — related
