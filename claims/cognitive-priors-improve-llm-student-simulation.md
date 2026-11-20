---
type: claim
title: Integrating cognitive prior knowledge into LLM prompts improves simulation of student gaze behaviors, cognitive states, and question answering
description: Integrating cognitive prior knowledge into LLM prompts improves simulation of student gaze behaviors, cognitive states, and question answering
id: cognitive-priors-improve-llm-student-simulation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: songlin-xu-2024
    resource: "https://doi.org/10.48550/arXiv.2404.07963"
    title: "Songlin Xu, Xinyu Zhang, Lianhui Qin. (2024). EduAgent: Generative Student Agents in Learning. Preprint. [doi:10.48550/arXiv.2404.07963](https://doi.org/10.48550/arXiv.2404.07963)"
    author: Songlin Xu, Xinyu Zhang, Lianhui Qin
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Integrating cognitive prior knowledge into LLM prompts improves simulation of student gaze behaviors, cognitive states, and question answering

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the personalized prediction experiment on EduAgent310, GPT-3.5 with cognitive priors achieved lower MAE on cognitive states and better gaze/question-answering similarity than a standard-prompt baseline, though motor AOI distance was slightly worse without priors. [→ Songlin Xu 2024](#songlin-xu-2024)

## Evidence

### Songlin Xu 2024

Songlin Xu, Xinyu Zhang, Lianhui Qin. (2024). EduAgent: Generative Student Agents in Learning. Preprint. [doi:10.48550/arXiv.2404.07963](https://doi.org/10.48550/arXiv.2404.07963)

`q2 · i?` · `causal · r1`

Simulation experiment predicting 310 real students' behaviors with GPT-3.5, comparing prompts with vs. without cognitive priors. The article reports "integrating cognitive priors improves simulation performance" on gaze, cognitive states, and question answering, while motor AOI distance was 0.340 with priors vs 0.336 without.

> "The results in Table. 2 show that integrating cognitive priors improves simulation performance including gaze behaviors, cognitive states and question answering. For motor behaviors, standard prompt is slightly better (AOI Distance = 0.336) compared with integrating cognitive priors (AOI Distance = 0.340)."

## Discussion


## Related Claims
- [GPT-4 improves gaze and question-answering simulation relative to GPT-3.5, while Gemini Pro and Llama 2 70B drop on those measures](foundation-model-comparison-student-simulation.md) — related
- [Removing past cognitive states or the whole few-shot memory from the agent degrades simulation of all behaviors](ablation-memory-components-student-simulation.md) — related
- [Simulated cognitive-state and gaze/motor behaviors correlate with question-answering accuracy in patterns aligned with cognitive-science theory](simulated-behavior-cross-correlations-consistent.md) — related
