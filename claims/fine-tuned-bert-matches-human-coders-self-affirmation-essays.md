---
type: claim
title: A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability
description: A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability
id: fine-tuned-bert-matches-human-coders-self-affirmation-essays
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: ye-2026
    resource: "https://github.com/visortown/bert-self-affirm"
    title: "Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm"
    author: "Ye, C., Borman, T. H., & Borman, G. D."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Evidence quality** · No study behind this claim is a peer-reviewed article with a DOI: it rests on a source with no registered publication record (a web page, book or unpublished report). It is kept because a design page cites it; treat it as a lead to check, not an established finding.

## Subclaims
`q3 i?` The fine-tuned BERT model reached Cohen's Kappa of 0.85 with both original and double human coders, compared to 0.83 between human coders. [→ Ye 2026](#ye-2026)

## Evidence

### Ye 2026

Ye, C., Borman, T. H., & Borman, G. D. (2026). Automating Self-Affirmation Essay Coding: Fine-Tuned BERT Performance Comparable to Human Coders and Comparison with GPT-4. Journal of Educational Data Mining, Volume 18, No 1. https://github.com/visortown/bert-self-affirm

`q3 · i?` · `design · r2`

Interrater reliability analysis on an out-of-sample comparison dataset of 134 double-coded essays from a randomized trial of 7th graders. The article reports "Cohen ’s Kappa values of 0.85" for BERT versus both coder sets, against 0.83 human-human agreement; Naive Bayes reached 0.76 and 0.69.

> "the BERT model achieved almost perfect agreement with human coders, with Cohen ’s Kappa values of 0.85 when compared to both the original coders and the double coders."

## Discussion


## Related Claims

- [The fine-tuned BERT model's classification performance is consistent across stereotype-threatened and non-threatened students and other demographic subgroups](bert-consistent-performance-across-student-subgroups.md) — related
- The BERT model's errors are predominantly false positives, and in most disagreements with the original coder its predictions aligned with second-round human coding — related
- [The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders](bert-generalizes-external-self-affirmation-dataset.md) — related
- Fine-tuned BERT outperforms a Naive Bayes baseline and zero-shot GPT-4 in classifying self-affirmation essays — related
- GPT-4 classifies self-affirmation essays reasonably in zero-shot mode but below fine-tuned BERT, and few-shot prompting does not appreciably improve it — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — related
- The interview coding achieved high inter-rater reliability, with Cohen's Kappa of 0.82 between independent coders — related
- [Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models](backtranslation-outperforms-llm-judge-diagram-agreement.md) — related
- An independent human second coder reached moderate agreement (kappa = 0.395) with the AI-assisted primary coding on the five-category outcome — related
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — a narrower finding that bears on this claim
- [Transformer-based NLP models achieve automated essay scoring with correlations to human grading exceeding 0.85](bert-essay-scoring-correlation-085.md) — related
- The review's coding framework showed very good inter-coder agreement (κ = 0.89, p < 0.001) on a random sample of six papers — related
- [Rubric-based assessment showed substantial to almost-perfect inter-rater reliability across all three time points](rubric-interrater-reliability-visualization-assessment.md) — related
- Scaled qualitative coding of preservice teachers' video-analysis responses reached very good interrater agreement — related
- [Five judges classifying 63 test units reached average inter-judge correlation of 0.542 ± 0.019 on the two scales](judge-agreement-classifying-test-units-scales.md) — related
- [A GPT-4-based coding scheme achieved over 90% inter-coder agreement, surpassing results reported for specialised pre-2017 AI (~80%)](gpt4-surpasses-specialised-intelligence-agreement.md) — related
