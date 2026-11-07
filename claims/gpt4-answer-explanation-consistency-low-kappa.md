---
type: claim
title: "Agreement between GPT-4's answers and human-curated answers based on its explanations was low (κ=0.504), with frequent answer-explanation mismatches"
description: "Agreement between GPT-4's answers and human-curated answers based on its explanations was low (κ=0.504), with frequent answer-explanation mismatches"
id: gpt4-answer-explanation-consistency-low-kappa
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: tseng-liang-wei-2025
    resource: "https://doi.org/10.2196/58897"
    title: "Tseng Liang-Wei, Lu Yi-Chin, Tseng Liang-Chi, Chen Yu-Chun, Chen Hsing-Yu. (2025). Performance of ChatGPT-4 on Taiwanese Traditional Chinese Medicine Licensing Examinations: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/58897"
    author: Tseng Liang-Wei, Lu Yi-Chin, Tseng Liang-Chi, Chen Yu-Chun, Chen Hsing-Yu
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Agreement between GPT-4's answers and human-curated answers based on its explanations was low (κ=0.504), with frequent answer-explanation mismatches

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The κ statistic between AI-generated and human-curated answers was 0.504; for 33% of correctly answered questions the AI gave an incorrect explanation, and for 17% of incorrectly answered questions it gave a correct explanation. [→ Tseng Liang-Wei 2025](#tseng-liang-wei-2025)

## Evidence

### Tseng Liang-Wei 2025

Tseng Liang-Wei, Lu Yi-Chin, Tseng Liang-Chi, Chen Yu-Chun, Chen Hsing-Yu. (2025). Performance of ChatGPT-4 on Taiwanese Traditional Chinese Medicine Licensing Examinations: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/58897

`q3 · i?` · `design · r2`

Human reviewers curated answers from GPT-4's item-by-item explanations without amending them, and agreement was assessed with the κ statistic. The Results section reports consistency "was low (κ=0.504)"; after human review accuracy decreased to 40.3% and 39.1%.

> "The consistency between AI-generated and human-curated results was low (κ=0.504; Figure 5)."

## Discussion


## Related Claims
- [Human review of GPT-4's explanations reduced overall accuracy from 43.9% to 40.3% and 39.1%, driven mainly by LOTS and recall questions](human-curation-lowered-gpt4-accuracy-lots-recall.md) — related
- [Validator false-negative cases reveal structural reasoning weaknesses, including answer-schema misinterpretation and internal inconsistency](code-gen-validator-fn-reasoning-weaknesses.md) — related
- [Chatbot explanations achieved acceptable content validity (average CVI ≥0.92) despite occasional hallucinated or fabricated references](chatbot-explanations-acceptable-cvi-despite-hallucinated-references.md) — related
- [GPT-4o was the most inconsistent chatbot, with 19 questions answered correctly in the first round answered incorrectly in the second](gpt-4o-most-inconsistent-across-rounds.md) — related
- [Qualitative analysis of LLM answer explanations identified 3 ambiguous examination questions, supporting LLM use for question quality assurance](llm-explanations-flag-ambiguous-questions.md) — related
