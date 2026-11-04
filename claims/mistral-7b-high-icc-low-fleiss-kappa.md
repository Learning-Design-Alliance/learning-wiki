---
type: claim
title: Mistral 7B shows high ICCs but low Fleiss kappa when scoring summary statements
description: Mistral 7B shows high ICCs but low Fleiss kappa when scoring summary statements
id: mistral-7b-high-icc-low-fleiss-kappa
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
    kind: causal
    rigour: 2
---

# Mistral 7B shows high ICCs but low Fleiss kappa when scoring summary statements

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The small open-weights model Mistral 7B had high ICCs (≥0.88) but low Fleiss κ (0.32-0.52). [→ Stadler P 2026](#stadler-p-2026)

## Evidence

### Stadler P 2026

Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666

`q2 · i?` · `causal · r2`

Same experimental comparative study; the local Mistral 7B model was deployed via vLLM on a single NVIDIA Tesla T4 GPU. The study reports "high ICCs (≥0.88) but low Fleiss κ (0.32‐0.52)" for this model.

> "Mistral 7B, a small open-weights model, had high ICCs (≥0.88) but low Fleiss κ (0.32‐0.52)."

## Discussion


## Related Claims
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [LLM-simulated student ideas moderately overlap with teacher- and student-generated lesson ideas (mean cosine similarity 0.52), with larger LLMs slightly outperforming Mistral-7B](llm-simulated-ideas-moderate-overlap-lesson-ideas.md) — related
- [Inter-rater agreement among pre-service teachers is low regardless of grading approach or essay quality](low-inter-rater-agreement-preservice-grading.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [LLMs show moderate agreement with human coders when extracting explicitly stated data from education studies](llms-moderate-agreement-explicit-data-extraction-education.md) — related
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — related
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
- [The checklist assessment showed strong interrater reliability, contributing validation evidence](checklist-interrater-reliability-kappa-0875.md) — related
- [Student–expert agreement on bias assessment improves significantly after EBD training](student-expert-agreement-improves-post-ebd-training.md) — related
