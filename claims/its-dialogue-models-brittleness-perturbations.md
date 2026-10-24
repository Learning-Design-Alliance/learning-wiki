---
type: claim
title: "Small input perturbations such as minor spelling errors can reduce state-of-the-art dialogue and assessment model accuracy by over 30%"
description: "Small input perturbations such as minor spelling errors can reduce state-of-the-art dialogue and assessment model accuracy by over 30%"
id: its-dialogue-models-brittleness-perturbations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: meriem-zerkouk-2025
    resource: "https://doi.org/10.48550/arxiv.2507.18882"
    title: "Meriem Zerkouk, Miloud Mihoubi and Belkacem Chikhaoui. (2025). A Comprehensive Review of AI-based Intelligent Tutoring Systems: Applications and Challenges. arXiv preprint. https://arxiv.org/abs/2507.18882 [doi:10.48550/arxiv.2507.18882](https://doi.org/10.48550/arxiv.2507.18882)"
    author: Meriem Zerkouk, Miloud Mihoubi and Belkacem Chikhaoui
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Small input perturbations such as minor spelling errors can reduce state-of-the-art dialogue and assessment model accuracy by over 30%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The review reports that small perturbations such as minor spelling errors or input phrasing can reduce response accuracy by over 30%, exposing brittleness of dialogue and assessment models outside their training distribution. [→ Meriem Zerkouk 2025](#meriem-zerkouk-2025)

## Evidence

### Meriem Zerkouk 2025

Meriem Zerkouk, Miloud Mihoubi and Belkacem Chikhaoui. (2025). A Comprehensive Review of AI-based Intelligent Tutoring Systems: Applications and Challenges. arXiv preprint. https://arxiv.org/abs/2507.18882 [doi:10.48550/arxiv.2507.18882](https://doi.org/10.48550/arxiv.2507.18882)

`q2 · i?` · `review · r2`

The review's synthesis of empirical evidence on ML/NLP-based ITS: "small perturbations such as minor spelling errors or input phrasing can reduce response accuracy by over 30%". No effect size or per-study design is printed; reported as the review's own summary claim.

> "Empirical evidence suggests that small perturbations such as minor spelling errors or input phrasing can reduce response accuracy by over 30%, exposing the brittleness of state of the art dialogue and assessment models once they stray from their training distribution."

## Discussion


## Related Claims
- [DysLexLens is moderately robust to paraphrased queries (Answer Relevancy 0.58) but sensitive to keyword-perturbed queries (0.34)](query-robustness-paraphrase-keyword-perturbation.md) — related
- Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign — related
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays](llm-overrate-short-essays-overpenalize-errors.md) — related
- [Current GenAI tools are not designed to support active learning and their apparent domain expertise is brittle](genai-tools-not-designed-for-active-learning.md) — related
- [LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs](llm-hallucination-rate-education.md) — related
