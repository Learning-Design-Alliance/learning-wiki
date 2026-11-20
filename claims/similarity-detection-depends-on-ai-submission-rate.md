---
type: claim
title: "Similarity-based detection of AI-generated code (MOSS, JPlag) is weak when few submissions are AI-generated and significantly more accurate when AI submissions reach 50%"
description: "Similarity-based detection of AI-generated code (MOSS, JPlag) is weak when few submissions are AI-generated and significantly more accurate when AI submissions reach 50%"
id: similarity-detection-depends-on-ai-submission-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: kevin-wang-2023
    resource: "https://doi.org/10.1109/csci62032.2023.00268"
    title: "Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)"
    author: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: kevin-wang-2023-2
    resource: "https://doi.org/10.1109/csci62032.2023.00268"
    title: "Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)"
    author: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Similarity-based detection of AI-generated code (MOSS, JPlag) is weak when few submissions are AI-generated and significantly more accurate when AI submissions reach 50%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MOSS and JPlag showed weak recall with a small proportion of AI submissions, and detection accuracy was significantly higher when 50% of solutions were AI. [→ Kevin Wang 2023](#kevin-wang-2023)
`q2 i?` Question complexity moderates detection: simpler questions produce more uniform solutions that are easier to detect, while complex questions make detection more challenging. [→ Kevin Wang 2023 (2)](#kevin-wang-2023-2)

## Evidence

### Kevin Wang 2023

Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)

`q2 · i?` · `design · r2`

Automated similarity-detection experiment on 100 submissions across four CS1/CS2 questions, with AI proportion varying from 5% to 50% and cutoffs of 90% for JPlag and 70% for MOSS. Figures 6-9 report precision, recall, and F1; the study reports accuracy "significantly higher" at 50% AI than the weak detection at 5%.

> "When the percentage of AI solutions is 50% (shown in Figures 8 and 9), the detection accuracy is significantly higher."

### Kevin Wang 2023 (2)

Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)

`q2 · i?` · `associational · r1`

The authors' analysis of factors affecting similarity detection in the same experiment, listing question complexity alongside student modification of solutions, varied prompting methods, and multiple generative AI systems as factors influencing detection difficulty.

> "Simpler questions lead to more uniform solutions, making it easier to detect AI generated content. More complex questions, with a wider range of responses, make detection more challenging."

## Discussion


## Related Claims
- [MOSS detected far fewer suspicious cases in Spring 2026 than in prior offerings, as LLM-assisted submissions lack similarity signals](moss-detection-declined-spring-2026.md) — related
- [Solutions from different LLM providers converged broadly on most CS1 labs, with cross-LLM MOSS match rates of about 88% pooled across labs but only 13.18–22.11% on Lab 10](cross-llm-convergence-task-dependent.md) — related
- [Popular plagiarism detection tools detect plagiarism in AI-assisted essays in less than 15% of cases](plagiarism-detectors-below-15-percent-ai-essays.md) — related
- [AI-assisted web programming submissions were more complex, employed uncommon syntax and libraries, and were less readable due to generic identifier names](ai-assisted-submissions-complex-less-readable.md) — related
- [Instructors and teaching assistants detect AI-generated code with only 69% accuracy and a 22% false positive rate, with large variability between raters](instructor-ai-detection-insufficient.md) — related
- [Plagiarized web programming submissions kept the original program semantic and were disguised mainly by color changes and identifier renaming](plagiarism-disguises-web-programming.md) — related
