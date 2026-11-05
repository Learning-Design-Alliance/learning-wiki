---
type: claim
title: Segmenting domain content into moderate token chunks significantly improves GPT-4.1 accuracy on specialised medical board questions compared with no prior content input
description: Segmenting domain content into moderate token chunks significantly improves GPT-4.1 accuracy on specialised medical board questions compared with no prior content input
id: token-splitting-improves-gpt41-specialised-exam-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: lei-yung-hsu-2025
    resource: "https://doi.org/10.1080/10872981.2025.2602788"
    title: "Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju. (2025). Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. Medical Education Online. https://doi.org/10.1080/10872981.2025.2602788"
    author: Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Segmenting domain content into moderate token chunks significantly improves GPT-4.1 accuracy on specialised medical board questions compared with no prior content input

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All segmented-input conditions achieved statistically significant accuracy improvements over the no-prior-input baseline on textbook-derived practice items. [→ Lei Yung-Hsu 2025](#lei-yung-hsu-2025)

## Evidence

### Lei Yung-Hsu 2025

Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju. (2025). Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. Medical Education Online. https://doi.org/10.1080/10872981.2025.2602788

`q2 · i?` · `causal · r2`

Phase 2 evaluation using the standard GPT-4.1 web interface on 481 textbook-derived single-choice items across six input strategies; pairwise McNemar tests with Bonferroni correction showed "statistically significant improvements in accuracy for all segmented-input conditions compared to the baseline".

> "The analysis reveals statistically significant improvements in accuracy for all segmented-input conditions compared to the baseline (p < 0.001)."

## Discussion


## Related Claims
- [Under 6,000-token segmentation, GPT-4.1 accuracy did not differ significantly across Bloom's taxonomy cognitive levels](no-bloom-level-accuracy-differences-under-token-splitting.md) — related
- [6,000-token segmentation outperformed both larger 20,000-token segments and unsegmented full-chapter input on specialised exam accuracy](six-thousand-token-segments-outperform-large-and-full-chapter-inputs.md) — a narrower finding that bears on this claim
- [Segmenting Improves Multimedia Learning](segmenting-improves-multimedia-learning.md) — a broader claim this one bears on
- [Segmentation Benefits Shrink With Expertise](segmentation-benefits-shrink-with-expertise.md) — related
- [GPT-4.1 achieved the highest accuracy among GPT-4.1, GPT-4o and GPT-4 on Taiwan plastic surgery board questions, but no model reached accuracy sufficient for independent clinical education use](gpt41-highest-accuracy-but-below-clinical-education-threshold.md) — related
- [LLMs, particularly GPT-4, can match or exceed medical students' examination performance](llms-match-or-exceed-medical-students-exam-performance.md) — related
