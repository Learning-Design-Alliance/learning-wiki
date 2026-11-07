---
type: claim
title: "Human review of GPT-4's explanations reduced overall accuracy from 43.9% to 40.3% and 39.1%, driven mainly by LOTS and recall questions"
description: "Human review of GPT-4's explanations reduced overall accuracy from 43.9% to 40.3% and 39.1%, driven mainly by LOTS and recall questions"
id: human-curation-lowered-gpt4-accuracy-lots-recall
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
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

# Human review of GPT-4's explanations reduced overall accuracy from 43.9% to 40.3% and 39.1%, driven mainly by LOTS and recall questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` After human revision of AI-provided explanations, accuracy decreased to 40.3% (human 1) and 39.1% (human 2), with the decrease concentrated in LOTS and recall-level questions. [→ Tseng Liang-Wei 2025](#tseng-liang-wei-2025)

## Evidence

### Tseng Liang-Wei 2025

Tseng Liang-Wei, Lu Yi-Chin, Tseng Liang-Chi, Chen Yu-Chun, Chen Hsing-Yu. (2025). Performance of ChatGPT-4 on Taiwanese Traditional Chinese Medicine Licensing Examinations: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/58897

`q3 · i?` · `design · r2`

Discussion section reporting the effect of human-curated answers on measured accuracy. The article states the decrease "was primarily driven by a reduction in accuracy for LOTS questions" and in recall-level DOK, while HOTS accuracy remained stable or increased.

> "GPT-4 failed the exam with an overall accuracy of 43.9%; following human revision of AI-provided explanations, the accuracy further decreased to 40.3% (human 1) and 39.1% (human 2)."

## Discussion


## Related Claims
- [Agreement between GPT-4's answers and human-curated answers based on its explanations was low (κ=0.504), with frequent answer-explanation mismatches](gpt4-answer-explanation-consistency-low-kappa.md) — related
- [Providing LLM pre-labels can decrease human annotation accuracy when the model is incorrect, due to automation bias](llm-prelabels-decrease-human-accuracy.md) — a broader claim this one bears on
- [The 2022 Taiwanese TCM licensing examination questions were predominantly HOTS (55.3%), SAMC format (92.2%), and negatively framed (62.2%)](tcm-2022-exam-question-characteristics-hots-samc-negative.md) — related
- [GPT-4 accuracy did not significantly correlate with most question characteristics, though TCM internal medicine, dermatology, and acupuncture showed significantly better performance](gpt4-accuracy-question-characteristics-no-significant-correlation.md) — related
- [Most GPT-4 errors on TCM examination questions stemmed from misunderstanding of TCM concepts (55.3%), not misreading questions](gpt4-tcm-errors-concept-misunderstanding-55-3.md) — related
