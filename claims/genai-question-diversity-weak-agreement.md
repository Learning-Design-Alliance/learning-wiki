---
type: claim
title: Model-expert agreement on question diversity is very weak, with the model systematically overestimating diversity relative to experts
description: Model-expert agreement on question diversity is very weak, with the model systematically overestimating diversity relative to experts
id: genai-question-diversity-weak-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: riya-gill-2025
    resource: "https://doi.org/10.1108/aiie-05-2025-0088"
    title: "Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita. (2025). Generative AI-Enabled Adaptive Learning Platform: How I Can Help You Pass Your Driving Test?. [doi:10.1108/aiie-05-2025-0088](https://doi.org/10.1108/aiie-05-2025-0088)"
    author: Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita
    q: 2
    i: 1
    kind: design
    rigour: 2
---

# Model-expert agreement on question diversity is very weak, with the model systematically overestimating diversity relative to experts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i1` small
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i1` Diversity ratings by model and expert show very weak alignment (r = 0.12, κ = 0.10), and the model overestimates diversity compared to the expert. [→ Riya Gill 2025](#riya-gill-2025)

## Evidence

### Riya Gill 2025

Riya Gill, Ievgeniia Kuzminykh, Maher Salem, Bogdan Ghita. (2025). Generative AI-Enabled Adaptive Learning Platform: How I Can Help You Pass Your Driving Test?. [doi:10.1108/aiie-05-2025-0088](https://doi.org/10.1108/aiie-05-2025-0088)

`q2 · i1` · `design · r2`

Diversity evaluation comparing 50 model-generated questions against authentic questions from the Theory 4 in 1 app, rated by both the evaluation model and experts on a 1-5 scale. The article reports "r = 0.12 (p-value = 0.230)" and κ = 0.10, indicating slight agreement.

> "The Pearson coefficient for diversity is r = 0.12 (p-value = 0.230), which indicates very weak alignment between the model and the expert, and the model systematically overestimates diversity compared to the expert."

## Discussion


## Related Claims
- [GenAI-generated driving theory questions show strong model-expert agreement on accuracy and relevancy, with the model slightly outperforming the expert on weighted average](genai-question-accuracy-relevancy-strong-agreement.md) — related
- [LLM alignment with expert teaching ratings does not predict, and is often negatively associated with, alignment with student learning gains](proxy-alignment-not-impact-alignment-llm-classroom.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
