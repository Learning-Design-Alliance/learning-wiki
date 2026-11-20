---
type: claim
title: Simulated final exam scores become more realistic as more past assessment history is used to instantiate virtual students
description: Simulated final exam scores become more realistic as more past assessment history is used to instantiate virtual students
id: more-assessment-history-improves-simulation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: songlin-xu-and-xinyu-zhang-2023
    resource: "https://doi.org/10.48550/arXiv.2310.19206"
    title: "Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)"
    author: Songlin Xu and Xinyu Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Simulated final exam scores become more realistic as more past assessment history is used to instantiate virtual students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Correlation between virtual and real students' final exam scores strengthens when more assessment scores are used as input, from Type iv to Type viii configurations. [→ Songlin Xu and Xinyu Zhang 2023](#songlin-xu-and-xinyu-zhang-2023)

## Evidence

### Songlin Xu and Xinyu Zhang 2023

Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)

`q2 · i?` · `design · r2`

Simulation on the Open University Learning Analytics Dataset (N = 4524 UK students with more than five assessments), each student simulated with 8 configurations yielding more than 40,716 LLM responses. The authors report the correlation "becomes stronger when we use more assessments scores as input".

> "More importantly, we find the correlation becomes stronger when we use more assessments scores as input (from Type iv to Type viii) (Fig. 2(C) and appendix Fig), suggesting that students simulation tends to be more realistic as taking more student assessment history data for instantiating virtual students."

## Discussion


## Related Claims
- [LLM-simulated virtual students show highly aligned demographic-outcome correlations with real students (r > 0.7) in most demographic factors](llm-virtual-students-demographic-outcome-correlation.md) — related
- [Simulated understanding levels align better when past understanding levels are included, and improve with slide number](past-understanding-levels-improve-slide-simulation.md) — possibly the same claim (merge candidate)
- [Adding demographics slightly worsens assessment-based simulation, and demographics-only simulation drops heavily](demographics-limited-value-with-assessment-history.md) — related
- [Non-verbal test material becomes less valid for predicting school success as grade level rises from IV to VIII](nonverbal-validity-declines-with-grade.md) — related
