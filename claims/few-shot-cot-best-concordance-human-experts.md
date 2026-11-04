---
type: claim
title: Few-shot with chain-of-thought prompting achieves the best concordance with human expert ratings for all tested LLMs
description: Few-shot with chain-of-thought prompting achieves the best concordance with human expert ratings for all tested LLMs
id: few-shot-cot-best-concordance-human-experts
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-03
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: stadler-p-2026
    resource: "https://doi.org/10.2196/94666"
    title: "Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666"
    author: Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Few-shot with chain-of-thought prompting achieves the best concordance with human expert ratings for all tested LLMs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Few-shot+CoT prompting achieved the best concordance with human ratings for all models, peaking for Mistral Large (accuracy 77%; Gwet AC1 and AC2 0.85). [→ Stadler P 2026](#stadler-p-2026)

## Evidence

### Stadler P 2026

Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666

`q2 · i?` · `design · r2`

Concordance with human expert ratings measured with accuracy and Gwet AC1/AC2 across 16 experimental conditions (4 models × 4 prompting strategies), each run 5 times. The study reports "peaking for Mistral Large (accuracy 77%; Gwet AC1 and AC2 0.85, 95% CI 0.83‐0.87)".

> "Few-shot+CoT prompting achieved the best concordance with human ratings for all the models (means across runs and rubric components), peaking for Mistral Large (accuracy 77%; Gwet AC1 and AC2 0.85, 95% CI 0.83‐0.87)."

## Discussion


## Related Claims
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Prompting with category information or few-shot examples yields limited improvement in distribution alignment, with zero-shot closest for most models](prompting-strategies-limited-alignment-gain.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
- [Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation](reasoning-variants-no-alignment-improvement.md) — reports the opposite
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related
- [Concordance between LLM and human ratings is higher for binary rubric components than for ternary components](higher-concordance-binary-than-ternary-components.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
