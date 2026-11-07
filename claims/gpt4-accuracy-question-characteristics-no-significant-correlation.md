---
type: claim
title: GPT-4 accuracy did not significantly correlate with most question characteristics, though TCM internal medicine, dermatology, and acupuncture showed significantly better performance
description: GPT-4 accuracy did not significantly correlate with most question characteristics, though TCM internal medicine, dermatology, and acupuncture showed significantly better performance
id: gpt4-accuracy-question-characteristics-no-significant-correlation
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

# GPT-4 accuracy did not significantly correlate with most question characteristics, though TCM internal medicine, dermatology, and acupuncture showed significantly better performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Logistic regression found no significant correlation between GPT-4 accuracy and question characteristics overall, but three subjects (internal medicine aOR 3.07, dermatology aOR 5.11, acupuncture aOR 2.14) showed statistically significant better performance. [→ Tseng Liang-Wei 2025](#tseng-liang-wei-2025)

## Evidence

### Tseng Liang-Wei 2025

Tseng Liang-Wei, Lu Yi-Chin, Tseng Liang-Chi, Chen Yu-Chun, Chen Hsing-Yu. (2025). Performance of ChatGPT-4 on Taiwanese Traditional Chinese Medicine Licensing Examinations: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/58897

`q3 · i?` · `design · r2`

Univariable and multivariable logistic regression on 476 questions used cognitive level, DOK, question type, vignette style, polarity, and subject as covariates. The Results section reports the printed adjusted odds ratios and CIs for the three significant subjects; accuracy "ranging from 31.3% in TCM pediatrics to 73.7% in TCM dermatology."

> "only TCM internal medicine (adjusted odds ratio [aOR] 3.07, 95% CI 1.41‐6.68; P=.005), TCM dermatology (aOR 5.11, 95% CI 1.65‐15.85; P=.005), and TCM acupuncture (aOR 2.14, 95% CI 1.12‐4.11; P=.02) showed statistically significant better performance"

## Discussion


## Related Claims
- [GPT-4 achieved 43.9% accuracy on the 2022 Taiwanese TCM licensing examination, below two human TCM resident doctors (70% and 78.4%) and below the 60% pass threshold](gpt4-43-9-accuracy-tcm-licensing-below-humans.md) — related
- [Most GPT-4 errors on TCM examination questions stemmed from misunderstanding of TCM concepts (55.3%), not misreading questions](gpt4-tcm-errors-concept-misunderstanding-55-3.md) — related
- [The 2022 Taiwanese TCM licensing examination questions were predominantly HOTS (55.3%), SAMC format (92.2%), and negatively framed (62.2%)](tcm-2022-exam-question-characteristics-hots-samc-negative.md) — related
- [Human review of GPT-4's explanations reduced overall accuracy from 43.9% to 40.3% and 39.1%, driven mainly by LOTS and recall questions](human-curation-lowered-gpt4-accuracy-lots-recall.md) — related
