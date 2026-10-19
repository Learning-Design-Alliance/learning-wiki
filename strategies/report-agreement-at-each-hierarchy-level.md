---
type: strategy
id: report-agreement-at-each-hierarchy-level
title: Report intercoder agreement at each level of a hierarchical codebook using set-valued measures such as Jaccard similarity
description: For multi-label coding with large hierarchical codebooks, the article recommends abandoning single chance-corrected coefficients, which penalize partial overlap as full disagreement, and instead reporting Jaccard simi...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: liu-2026
    resource: "https://osf.io/ju59q/overview?view_only=96afb71945044b8794e113f9763cc74a"
    title: "Liu, A., Sun, M., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., & He, K. (2026). Human-LLM Collaborative Inductive Coding for Conceptualizing K-12 Educator AI Use. https://osf.io/ju59q/overview?view_only=96afb71945044b8794e113f9763cc74a"
    author: "Liu, A., Sun, M., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., & He, K"
---

# Report intercoder agreement at each level of a hierarchical codebook using set-valued measures such as Jaccard similarity

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For multi-label coding with large hierarchical codebooks, the article recommends abandoning single chance-corrected coefficients, which penalize partial overlap as full disagreement, and instead reporting Jaccard similarity over code sets at multiple hierarchy levels. The authors state: "We suggest that researchers validating large hierarchical codebooks report agreement at each level of the hierarchy", since a single fine-grained coefficient understates structural reliability while a coarse one overstates item reliability.

## Design Implications

### Context
#### Requirements
- Multi-label annotation over a large codebook, pairwise computation across coders on an overlap set, and iterative calibration rounds before independent coding
#### Constraints
- The reported agreement, while adequate for multi-label coding at this codebook size, leaves room for improvement per the authors' limitations

### Target Learners
- Qualitative research teams validating hierarchical codebooks

### Target Learning Goals
- Establishing truthful, granularity-sensitive intercoder reliability evidence for multi-label coding instruments

## Related Strategies

- [Use two researchers as independent instruments for interpretation instead of one researcher confirming the other's reliability](two-researchers-independent-interpretive-instruments.md)

## Examples
-

## Key Sources
- Liu, A., Sun, M., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., & He, K. (2026). Human-LLM Collaborative Inductive Coding for Conceptualizing K-12 Educator AI Use. https://osf.io/ju59q/overview?view_only=96afb71945044b8794e113f9763cc74a
