---
type: claim
title: GPT-4 improves gaze and question-answering simulation relative to GPT-3.5, while Gemini Pro and Llama 2 70B drop on those measures
description: GPT-4 improves gaze and question-answering simulation relative to GPT-3.5, while Gemini Pro and Llama 2 70B drop on those measures
id: foundation-model-comparison-student-simulation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: songlin-xu-2024
    resource: "https://doi.org/10.48550/arXiv.2404.07963"
    title: "Songlin Xu, Xinyu Zhang, Lianhui Qin. (2024). EduAgent: Generative Student Agents in Learning. Preprint. [doi:10.48550/arXiv.2404.07963](https://doi.org/10.48550/arXiv.2404.07963)"
    author: Songlin Xu, Xinyu Zhang, Lianhui Qin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 improves gaze and question-answering simulation relative to GPT-3.5, while Gemini Pro and Llama 2 70B drop on those measures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across foundation models on EduAgent310, GPT-4 shows obvious improvement in gaze/motor and question-answering simulation over GPT-3.5, whereas Gemini Pro and Llama 2 70B show obvious drops in gaze and question-answering simulation. [→ Songlin Xu 2024](#songlin-xu-2024)

## Evidence

### Songlin Xu 2024

Songlin Xu, Xinyu Zhang, Lianhui Qin. (2024). EduAgent: Generative Student Agents in Learning. Preprint. [doi:10.48550/arXiv.2404.07963](https://doi.org/10.48550/arXiv.2404.07963)

`q2 · i?` · `design · r2`

Foundation-model comparison in the Experiment 1 simulation on EduAgent310 using GPT-3.5, GPT-4, Gemini Pro, and Llama 2 70B with cognitive priors. The article reports the quoted contrast and states GPT-4's "obvious improvement in gaze/motor and question answering simulation" suggests stronger correlation capture.

> "with Gemini Pro Gem and Llama 2 70B lla, we find slight improvement in motor and cognitive states simulation but obvious performance drop in gaze and question answering simulation compared with GPT-3.5"

## Discussion


## Related Claims
- [Integrating cognitive prior knowledge into LLM prompts improves simulation of student gaze behaviors, cognitive states, and question answering](cognitive-priors-improve-llm-student-simulation.md) — related
- [Pairwise comparisons showed GPT-4 significantly outperformed every other model, and Tongyi Qianwen significantly outperformed Bard and Gemini Pro, while Claude, Bard, and Gemini Pro did not differ significantly from each other](pairwise-model-comparisons-radiology-questions.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [LLaMA-2 70B performs best at adjusting readability while GPT-3.5 best preserves content and meaning](llama2-readability-vs-gpt35-meaning-preservation.md) — related
