---
type: claim
title: The proposed framework outperforms fine-tuned BERT, Instructor-LM, GPT-4, and RAPT on TeacherEval-2023 across consistency, credibility, calibration, and fairness metrics
description: The proposed framework outperforms fine-tuned BERT, Instructor-LM, GPT-4, and RAPT on TeacherEval-2023 across consistency, credibility, calibration, and fairness metrics
id: llm-teacher-assessment-outperforms-baselines-teachereval
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: li-2025
    resource: "https://doi.org/10.3390/info16100882"
    title: "Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882"
    author: Li, Y.; Yang, H.; Fang, Q.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The proposed framework outperforms fine-tuned BERT, Instructor-LM, GPT-4, and RAPT on TeacherEval-2023 across consistency, credibility, calibration, and fairness metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On TeacherEval-2023 the framework achieves ICS of 82.4%, 12.6 points higher than BERT-base and 9.2 points higher than Instructor-LM, with ExpScore 0.78, ECE 0.032, and FG 1.8% versus 6–9% for baselines. [→ Li 2025](#li-2025)

## Evidence

### Li 2025

Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882

`q2 · i?` · `design · r2`

Quantitative comparison on TeacherEval-2023 (Table 3) against BERT-base, Instructor-LM, GPT-4, and RAPT; the framework reports "an ICS of 82.4%", ExpScore 0.78, ECE 0.032, and FG 1.8% versus a 6–9% baseline range, with paired t-tests reported significant at α = 0.05.

> "The proposed framework achieves an ICS of 82.4%, which is 12.6 absolute points higher than BERT-base and 9.2 points higher than Instructor-LM. The ExpScore reaches 0.78, representing an increase of 0.31 over BERT-base."

## Discussion


## Related Claims
- Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays — related
- GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it — related
- [The framework is robust to 15% ASR transcription noise and retains 99.6% of its ICS under zero-shot cross-domain transfer to EdNet-Math](framework-robust-asr-noise-cross-domain-transfer.md) — related
- [Expert raters rate TeachingCoach higher than a GPT-4o baseline on clarity, tone, reflection, and acknowledgment of user input](teachingcoach-outperforms-gpt4o-expert-ratings.md) — related
- [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human rating discrepancies exceeding 1.5 standard deviations in 38% of graduate-level bibliographies](gpt4-essay-score-inflation.md) — related
