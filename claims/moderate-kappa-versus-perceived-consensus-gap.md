---
type: claim
title: "Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus"
description: "Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus"
id: moderate-kappa-versus-perceived-consensus-gap
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ralf-raumanns-2026
    resource: "https://arxiv.org/abs/2607.20149"
    title: "Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina. (2026). Data annotations as pedagogical hints: from subjective labels to critical thinking. https://arxiv.org/abs/2607.20149"
    author: Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ralf-raumanns-2026-2
    resource: "https://arxiv.org/abs/2607.20149"
    title: "Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina. (2026). Data annotations as pedagogical hints: from subjective labels to critical thinking. https://arxiv.org/abs/2607.20149"
    author: Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Fleiss's κ computed for 23 student groups showed a combined mean of 0.62, indicating the intended subjectivity was present in the dataset. [→ Ralf Raumanns 2026](#ralf-raumanns-2026)
`q2 i?` Students who reported group consensus despite moderate measured agreement may treat any convergence as success, and even students who computed κ themselves did not change their conceptual framework. [→ Ralf Raumanns 2026](#ralf-raumanns-2026)

## Evidence

### Ralf Raumanns 2026

Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina. (2026). Data annotations as pedagogical hints: from subjective labels to critical thinking. https://arxiv.org/abs/2607.20149

`q2 · i?` · `design · r2`

Objective agreement analysis of group annotation files: nine Fontys groups (mean κ 0.60, range 0.27–0.78) and fourteen ITU groups (mean κ 0.64, range 0.42–0.82). The article calls the gap between perceived and measured agreement noteworthy.

> "In general, the combined mean κ in all 23 groups was 0.62, indicating moderate agreement. The moderate level of agreement indi- cates that the intended degree of subjectivity is indeed present in the dataset."

### Ralf Raumanns 2026 (2)

Ralf Raumanns, Theresa Elstner, Louis Ferger-Andrews, Louise M. Carlsen, Martin Potthast, Gerard Schouten, Josien P. W. Pluim, and Veronika Cheplygina. (2026). Data annotations as pedagogical hints: from subjective labels to critical thinking. https://arxiv.org/abs/2607.20149

`q2 · i?` · `design · r2`

Authors' interpretation of the mismatch between survey-reported consensus and computed Fleiss's κ. Computing the agreement metric alone did not shift students' conceptual framing, per the authors.

> "Students who reported group consensus despite moderate agreement may treat any convergence as success, failing to recognise that the remaining disagree- ment reflects the task's subjectivity. Even when the Fontys students calculated κ themselves, the issue remained"

## Discussion


## Related Claims
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — a broader claim this one bears on
- [Making trustworthiness metrics and visualizations explicit increased inter-rater reliability among learning engineers evaluating LLM responses](trustworthiness-metrics-visualizations-increase-expert-agreement.md) — related
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md) — related
