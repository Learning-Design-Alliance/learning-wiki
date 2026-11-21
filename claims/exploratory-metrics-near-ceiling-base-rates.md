---
type: claim
title: "Exploratory quality metrics showed near-ceiling base rates: no biased language in 543 problems, only five non-grounded hallucinations, and one unrealistic-data case"
description: "Exploratory quality metrics showed near-ceiling base rates: no biased language in 543 problems, only five non-grounded hallucinations, and one unrealistic-data case"
id: exploratory-metrics-near-ceiling-base-rates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tobias-geisler-and-gerd-kortemeyer-2026
    resource: "https://doi.org/10.1103/9hh9-vt4d"
    title: "Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)"
    author: Tobias Geisler and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Exploratory quality metrics showed near-ceiling base rates: no biased language in 543 problems, only five non-grounded hallucinations, and one unrealistic-data case

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In all 543 problems there was no case of biased language or offensive content, only five problems were not grounded in the textbook (hallucinations), and only one problem used unrealistic data. [→ Tobias Geisler and Gerd Kortemeyer 2026](#tobias-geisler-and-gerd-kortemeyer-2026)

## Evidence

### Tobias Geisler and Gerd Kortemeyer 2026

Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)

`q2 · i?` · `design · r2`

Expert ground-truth rating of exploratory (class-imbalanced) metrics. The article reports "no case of biased language or offensive content", five non-grounded hallucination cases (e.g. a biology problem about mitosis), and one unrealistic-data case (a 5,000 kg freight train).

> "In all 543 problems, there was no case of biased language or offensive content."

## Discussion


## Related Claims
- [LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs](llm-hallucination-rate-education.md) — a broader claim this one bears on
- [AI systems can produce biased or inaccurate diagnostic outputs, requiring critical teacher evaluation before integration](ai-biased-inaccurate-outputs-require-critical-evaluation.md) — related
- [Source-anchored instruction pairs reduce hallucination: they achieve mean Teacher Fidelity 1.4 points higher than non-anchored pairs, and models trained on anchored subsets produce 23% fewer factual hallucinations](source-anchoring-reduces-hallucination-instruction-data.md) — related
- [The most reported risks of AI tools in science and chemistry education are ethical issues, including gender and racial bias, hallucinations, copyright infringement, and plagiarism](ethical-issues-most-reported-ai-risk.md) — related
