---
type: claim
title: "Instructors and teaching assistants detect AI-generated code with only 69% accuracy and a 22% false positive rate, with large variability between raters"
description: "Instructors and teaching assistants detect AI-generated code with only 69% accuracy and a 22% false positive rate, with large variability between raters"
id: instructor-ai-detection-insufficient
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: kevin-wang-2023
    resource: "https://doi.org/10.1109/csci62032.2023.00268"
    title: "Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)"
    author: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: kevin-wang-2023-2
    resource: "https://doi.org/10.1109/csci62032.2023.00268"
    title: "Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)"
    author: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Instructors and teaching assistants detect AI-generated code with only 69% accuracy and a 22% false positive rate, with large variability between raters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 10 survey respondents, average recall was 69.29%, precision 74.51%, F1 71.42%, overall accuracy 69%, and false positive rate 22%. [→ Kevin Wang 2023](#kevin-wang-2023)
`q2 i?` Detection performance varied substantially between instructors, with F1 scores ranging from 40% to 100%, and was higher for more experienced instructors and teaching assistants. [→ Kevin Wang 2023 (2)](#kevin-wang-2023-2)

## Evidence

### Kevin Wang 2023

Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)

`q2 · i?` · `associational · r1`

Human-detection survey experiment: course instructors and teaching assistants classified 32 randomized mixed student and ChatGPT solutions from 4 CS1/CS2 assignments. The study reports average recall of 69.29%, precision of 74.51%, F1 of 71.42%, accuracy of 69%, and a false positive rate of 22%.

> "The average recall across all participants was 69.29%. The average precision was 74.51%, and the average F1 score was 71.42%. Overall the detection accuracy rate is 69%, and the false positive rate is 22%."

### Kevin Wang 2023 (2)

Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)

`q2 · i?` · `associational · r1`

The same survey experiment's participant-level results: the study reports substantial variability between instructors, with the lowest F1 score at 40% and the highest at 100%, and notes there was higher performance for participants with more experience. 70% of participants reported the task very time consuming.

> "there is substantial variability between instructors in detecting AI. The lowest F1 score was 40% with the highest at 100%."

## Discussion


## Related Claims
- [The stylometric detector misclassified 4 of 18 independently authored documents as GPT-assisted (FPR 22.2%) and 2 of 18 GPT-assisted documents (FNR 11.1%), with wide confidence intervals](stylometric-detector-fpr-22-fnr-11.md) — related
- [Independent evaluation found commercial AI-text detectors neither sufficiently accurate nor sufficiently reliable for high-stakes use](detectors-insufficient-accuracy-high-stakes.md) — a broader claim this one bears on
- [The AI text classifier flagged more ChatGPT-group essays as likely AI-generated, but also produced false positives in the control group](ai-classifier-flags-more-gpt-essays-false-positives.md) — related
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](aggregate-accuracy-group-fairness-detectors.md) — related
- [Similarity-based detection of AI-generated code (MOSS, JPlag) is weak when few submissions are AI-generated and significantly more accurate when AI submissions reach 50%](similarity-detection-depends-on-ai-submission-rate.md) — related
