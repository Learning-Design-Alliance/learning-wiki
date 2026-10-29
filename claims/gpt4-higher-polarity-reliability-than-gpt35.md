---
type: claim
title: GPT-4 demonstrated higher reliability of feedback than GPT-3.5, with higher F1 agreement with instructors on most assessment aspects
description: GPT-4 demonstrated higher reliability of feedback than GPT-3.5, with higher F1 agreement with instructors on most assessment aspects
id: gpt4-higher-polarity-reliability-than-gpt35
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-15
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: dai-2024
    resource: "https://doi.org/10.1016/j.caeai.2024.100299"
    title: "Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen. (2024). Assessing the Proficiency of Large Language Models in Automatic Feedback Generation: An Evaluation Study. Computers and Education: Artificial Intelligence, 7, 100299. Preprint submitted to Elsevier. https://doi.org/10.1016/j.caeai.2024.100299"
    author: Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 demonstrated higher reliability of feedback than GPT-3.5, with higher F1 agreement with instructors on most assessment aspects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4's F1 agreement with instructor polarity exceeded GPT-3.5's on all aspect-polarity pairs except negative polarity for Clarity. [→ Dai 2024](#dai-2024)

## Evidence

### Dai 2024

Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen. (2024). Assessing the Proficiency of Large Language Models in Automatic Feedback Generation: An Evaluation Study. Computers and Education: Artificial Intelligence, 7, 100299. Preprint submitted to Elsevier. https://doi.org/10.1016/j.caeai.2024.100299

`q2 · i?` · `design · r2`

Reliability analysis treating instructor polarity labels as ground truth and computing precision, recall and F1 per aspect (Table 8). The article reports "an increase of F1 for GPT-4 compared to GPT-3.5 except for negative polarity for the aspect of Clarity".

> "Although GPT models did not achieve high agreement with instructors on the other four assessment aspects, we can observe an increase of F1 for GPT-4 compared to GPT-3.5 except for negative polarity for the aspect of Clarity."

## Discussion


## Related Claims
- [GPT models achieved high polarity agreement with instructors only for positive feedback on the Topic aspect, and could not reliably assess the other rubric aspects](gpt-polarity-agreement-low-except-topic.md) — related
- [A human assessor agreed with the majority of GPT-generated feedback comments on assessment aspects that instructors had not commented on](human-assessor-agrees-with-gpt-feedback-on-uncommented-aspects.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [AI assessors show emerging reliability: acceptable AI-human rater agreement (Cohen's 0.78) in a 12-educator case study and human-comparable feedback helpfulness ratings with 45 learners](agentic-assessment-rater-agreement-and-helpfulness.md) — related
- [GenAI feedback aligned more reliably with LA-based ground-truth SRL data than tutor feedback](genai-feedback-reliability-vs-la-ground-truth.md) — related
