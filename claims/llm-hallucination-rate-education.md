---
type: claim
title: "LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs"
description: "LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs"
id: llm-hallucination-rate-education
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mahamad-2025
    resource: "https://doi.org/10.3390/fi17090383"
    title: "Mahamad, S.; Chin, Y.H.; Zulmuksah, N.I.N.; Haque, M.M.; Shaheen, M.; Nisar, K. (2025). Technical Review: Architecting an AI-Driven Decision Support System for Enhanced Online Learning and Assessment. Future Internet 2025, 17, 383. https://doi.org/10.3390/fi17090383"
    author: Mahamad, S.; Chin, Y.H.; Zulmuksah, N.I.N.; Haque, M.M.; Shaheen, M.; Nisar, K.
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Hallucinations occur in 15–25% of LLM responses, undermining reliability in high-stakes assessments. [→ Mahamad 2025](#mahamad-2025)
`q2 i?` Training-data biases can undervalue non-native language inputs, with fairness metrics showing disparate impacts of 0.20–0.30 in multicultural datasets. [→ Mahamad 2025](#mahamad-2025)

## Evidence

### Mahamad 2025

Mahamad, S.; Chin, Y.H.; Zulmuksah, N.I.N.; Haque, M.M.; Shaheen, M.; Nisar, K. (2025). Technical Review: Architecting an AI-Driven Decision Support System for Enhanced Online Learning and Assessment. Future Internet 2025, 17, 383. https://doi.org/10.3390/fi17090383

`q2 · i?` · `review · r2`

The review's critique of LLM applications in education, citing prior work: "Hallucinations—fabricated or inaccurate outputs—occur in 15–25% of responses". A further sentence reports disparate impacts of 0.20–0.30 in multicultural datasets and 40–50% higher computational costs than traditional NLP.

> "Hallucinations—fabricated or inaccurate outputs—occur in 15–25% of responses, undermining reliability in high-stakes assessments [34]."

## Discussion


## Related Claims
- [Recurring risks of GenAI in STEAM education include hallucination, bias, superficial completion strategies, and compromised assessment validity](genai-steam-risks-hallucination-bias.md) — a broader claim this one bears on
- [The most reported risks of AI tools in science and chemistry education are ethical issues, including gender and racial bias, hallucinations, copyright infringement, and plagiarism](ethical-issues-most-reported-ai-risk.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [Phase VI AI-enabled systems face six documented challenges: explainability, hallucination risk, prompt sensitivity, computational cost, validation complexity, and limited large-scale evidence](phase-vi-ai-systems-six-challenges.md) — related
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — related
- [Open issues for dynamic assessment include cost-effectiveness, training, reliability and validity, and generalization](da-open-issues-cost-training-reliability-validity.md) — related
- [Source-anchored instruction pairs reduce hallucination: they achieve mean Teacher Fidelity 1.4 points higher than non-anchored pairs, and models trained on anchored subsets produce 23% fewer factual hallucinations](source-anchoring-reduces-hallucination-instruction-data.md) — related
- [Small input perturbations such as minor spelling errors can reduce state-of-the-art dialogue and assessment model accuracy by over 30%](its-dialogue-models-brittleness-perturbations.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [Current LLMs misalign instructional-strategy sensitivity with pedagogical relevance, including hallucinated relevance of irrelevant traits](llm-relevance-impact-misalignment-learner-characteristics.md) — a narrower finding that bears on this claim
