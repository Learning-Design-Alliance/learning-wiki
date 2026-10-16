---
type: claim
title: Validator agent reliability is highest for realism and lowest for authenticity in human evaluation
description: Validator agent reliability is highest for realism and lowest for authenticity in human evaluation
id: validator-reliability-highest-realism-lowest-authenticity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: fareya-ikram-2026
    resource: "https://doi.org/10.48550/arxiv.2604.05160"
    title: "Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160 [doi:10.48550/arxiv.2604.05160](https://doi.org/10.48550/arxiv.2604.05160)"
    author: Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Validator agent reliability is highest for realism and lowest for authenticity in human evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The realism validator agent matches human majority judgments with fair agreement (κ=0.322, acc=0.667), while the authenticity validator shows only slight agreement (κ=0.133, acc=0.511). [→ Fareya Ikram 2026](#fareya-ikram-2026)

## Evidence

### Fareya Ikram 2026

Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160 [doi:10.48550/arxiv.2604.05160](https://doi.org/10.48550/arxiv.2604.05160)

`q2 · i?` · `design · r2`

Human evaluation in which three annotators with college-level mathematics background labeled 45 problems sampled from the Zero-Shot baseline outputs for authenticity, realism, and readability using the same rubric as the validator agents; solvability was excluded due to highly skewed labels. Cohen's κ and accuracy against the human majority label are reported in Table 3.

> "For realism (κ=0.322, acc=0.667) and readability (κ=0.281, acc=0.800), there isfairagreement between validator agents and human annotators. For authenticity (κ=0.133, acc=0.511), there is onlyslightagreement."

## Discussion


## Related Claims
- [Validator failure patterns vary by interest topic and math curriculum unit](failure-patterns-vary-by-topic-and-curriculum-unit.md) — related
- [Authenticity and realism are the most frequent failure modes in initial LLM-personalized math problems, and a single refinement iteration substantially reduces failures](single-refinement-iteration-reduces-personalization-failures.md) — related
- [Realism issues were detected by agents during generation but were rare in final versions](realism-issues-rare-final-versions.md) — related
