---
type: claim
title: "ChatGPT's grading consistency does not improve with increased prompt specificity in essay evaluation"
description: "ChatGPT's grading consistency does not improve with increased prompt specificity in essay evaluation"
id: chatgpt-grading-consistency-not-improved-by-prompt-specificity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mrityunjay-kumar-2025
    resource: "https://doi.org/10.48550/arXiv.2510.06997"
    title: "Mrityunjay Kumar. (2025). The Limits of Goal-Setting Theory in LLM-Driven Assessment. arXiv. [doi:10.48550/arXiv.2510.06997](https://doi.org/10.48550/arXiv.2510.06997)"
    author: Mrityunjay Kumar
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# ChatGPT's grading consistency does not improve with increased prompt specificity in essay evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Mean Kappa values do not always increase when prompt specificity improves; Prompt Type 3 (rubric only) yielded the highest Mean Kappa (0.825) while Prompt Type 2 (model solution only) yielded the lowest (0.748). [→ Mrityunjay Kumar 2025](#mrityunjay-kumar-2025)

## Evidence

### Mrityunjay Kumar 2025

Mrityunjay Kumar. (2025). The Limits of Goal-Setting Theory in LLM-Driven Assessment. arXiv. [doi:10.48550/arXiv.2510.06997](https://doi.org/10.48550/arXiv.2510.06997)

`q2 · i?` · `causal · r1`

Controlled experiment in which ChatGPT evaluated 29 student submissions under four Prompt Types across six independent runs each, yielding 60 pairwise weighted Cohen's Kappa comparisons. A one-way ANOVA showed "a significant main effect of Prompt Type,F(3,56) = 5.24,p= 0.0029".

> "The results showed a significant main effect of Prompt Type,F(3,56) = 5.24,p= 0.0029"

## Discussion


## Related Claims
- [Prompt specificity does not reduce ChatGPT's performance variance in essay evaluation](prompt-specificity-does-not-reduce-chatgpt-variance.md) — related
- [LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes](llm-fast-mode-limited-thinking-mode-better-agreement.md) — related
- [Under single-pass deployment, Fs+CoT prompting yields the strongest agreement with teacher mean scores for music-analysis essay scoring (r = 0.795, ICC (2,1) = 0.657)](fscot-strongest-teacher-agreement-run1.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — reports the opposite
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — reports the opposite
