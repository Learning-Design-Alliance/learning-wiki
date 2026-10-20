---
type: claim
title: Contextual noise from irrelevant textbooks broadly degrades KC planning, most in Validity and Efficiency
description: Contextual noise from irrelevant textbooks broadly degrades KC planning, most in Validity and Efficiency
id: contextual-noise-degrades-kc-planning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yu-liu-2026
    resource: "https://doi.org/10.48550/arxiv.2609.18861"
    title: "Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)"
    author: Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Contextual noise from irrelevant textbooks broadly degrades KC planning, most in Validity and Efficiency

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Adding irrelevant textbook titles costs Qwen3-30B-A3B (CoT) 54.9 percentage points in Validity and 35.7 points in Efficiency in Basic Education. [→ Yu Liu 2026](#yu-liu-2026)

## Evidence

### Yu Liu 2026

Yu Liu, Zeming Liu, Tianle Zhang, Zihao Cheng, Yuhang Guo, Kehai Chen, Min Zhang, Yunhong Wang, Haifeng Wang. (2026). PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning. arXiv. https://arxiv.org/abs/2609.18861 [doi:10.48550/arxiv.2609.18861](https://doi.org/10.48550/arxiv.2609.18861)

`q2 · i?` · `design · r2`

Controlled noise-injection experiment (Table 7) in which irrelevant textbook titles were added at varying proportions to the candidate pool for Basic Education personas. The article reports the printed percentage-point losses; no effect size is printed.

> "Contextual noise degrades performance broadly, most notably in Validity and Efficiency. Qwen3-30B-A3B (CoT) loses 54.9 percentage points in Validity and 35.7 points in Efficiency."

## Discussion


## Related Claims
- [Removing explicit mastery information from learner profiles mainly degrades Adaptivity](mastery-information-needed-for-adaptivity.md) — related
- [Retrieval augmentation raises path Validity but not the joint Final Pass rate](rag-raises-validity-not-final-pass.md) — related
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Preserving book-level document structure during mid-training improves downstream performance beyond identical content split into sections (+1.02 mean)](book-structure-preservation-improves-mid-training.md) — related
