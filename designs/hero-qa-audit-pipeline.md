---
type: design
id: hero-qa-audit-pipeline
title: "HERO-QA pipeline: hierarchical retrieval, answer generation with abstention, and a structured-output LLM judge"
description: HERO-QA is the audit pipeline the article uses to generate and compare answers grounded in different institutional handbooks.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: yubo-li-2026
    resource: "https://arxiv.org/abs/2607.22606"
    title: "Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606"
    author: Yubo Li, Rema Padman, Ramayya Krishnan
---

# HERO-QA pipeline: hierarchical retrieval, answer generation with abstention, and a structured-output LLM judge

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
HERO-QA is the audit pipeline the article uses to generate and compare answers grounded in different institutional handbooks. The article states it "uses hierarchical BM25 (Robertson & Zaragoza, 2009) and dense retrieval (Xiao et al., 2024) with reranking, or the full extracted text for short handbooks (≤80,000 characters)." Qwen3-32B generates answers at temperature 0.1 and can return NOT ADDRESSED when evidence is insufficient; a Qwen3-32B judge with structured JSON output assigns a relationship label (ABSENT, CONSISTENT, COMPLEMENTARY, DIVERGENT, CONTRADICTORY), a divergence topic, and a low/medium/high significance rating.

## Design Implications

### Context
#### Requirements
- Retrieval quality and sufficient handbook text; the judge supplies labels, divergence topics, and significance ratings for disagreements
#### Constraints
- The article states these ratings describe potential consequences inferred by the model, not observed patient harm, and do not establish clinical correctness; generation and judging use the same model family

### Target Learners
- health-IT teams auditing patient-facing generative AI systems

### Learning Goals
- measuring coverage and disagreement across institutional patient-education corpora before AI deployment

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606
