---
type: claim
title: "Zero-shot MeNSP scored science written responses without training data at Cohen's Kappa 0.30–0.57, improvable to 0.38 at the lower end with few-shot samples"
description: "Zero-shot MeNSP scored science written responses without training data at Cohen's Kappa 0.30–0.57, improvable to 0.38 at the lower end with few-shot samples"
id: mensp-zero-shot-scoring-kappa-range
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: zhai-2024
    resource: "https://doi.org/10.1108/979-8-88730-606-320251011"
    title: "Zhai, X. (2024). AI and Machine Learning for Next Generation Science Assessments. Jiao, H., & Lissitz, R. W. (Eds.). Machine learning, natural language processing and psychometrics. Charlotte, NC: Information Age Publisher. [doi:10.1108/979-8-88730-606-320251011](https://doi.org/10.1108/979-8-88730-606-320251011)"
    author: Zhai, X.
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Zero-shot MeNSP scored science written responses without training data at Cohen's Kappa 0.30–0.57, improvable to 0.38 at the lower end with few-shot samples

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The MeNSP zero-shot approach, using pre-trained models without training data, scored student written responses with Cohen's Kappa between 0.30 and 0.57; a few training samples raised the lower end to 0.38. [→ Zhai 2024](#zhai-2024)

## Evidence

### Zhai 2024

Zhai, X. (2024). AI and Machine Learning for Next Generation Science Assessments. Jiao, H., & Lissitz, R. W. (Eds.). Machine learning, natural language processing and psychometrics. Charlotte, NC: Information Age Publisher. [doi:10.1108/979-8-88730-606-320251011](https://doi.org/10.1108/979-8-88730-606-320251011)

`q2 · i?` · `review · r2`

The chapter reports Wu et al.'s MeNSP approach, which matches exemplars as next sentence prediction using pre-trained models. The printed Kappa range is 0.30 to 0.57; the chapter adds that few-shot samples "can increase the lower end of scoring accuracy of Cohen's Kappa from 0.30 to 0.38."

> "Without training data, MeNSP was able to score student written responses with Cohen's Kappa ranges between 0.30 to 0.57."

## Discussion


## Related Claims
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85](gpt4-few-shot-classifies-trainee-responses.md) — related
- [ML scoring models for scientific argumentation items achieved good to almost perfect agreement with human consensus scores (mean Cohen's kappa = 0.60)](ml-scoring-argumentation-mean-kappa-060.md) — related
