---
type: claim
title: "Domain-matched experts judged 87% of Bespoke-generated lecture videos at or above the rubric midpoint corresponding to a standard MOOC lecture's quality (mean G = 3.42 of 5)"
description: "Domain-matched experts judged 87% of Bespoke-generated lecture videos at or above the rubric midpoint corresponding to a standard MOOC lecture's quality (mean G = 3.42 of 5)"
id: bespoke-87-percent-mooc-comparable-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: romain-puech-2026
    resource: "https://arxiv.org/abs/2609.26540"
    title: "Romain Puech, Dewang Kumar Agarwal, Antonio Santamaría Escobar, Dimitris Bertsimas. (2026). Bespoke: Generating MOOC-Quality Industry-Personalized Lecture Videos at Scale. arXiv preprint. https://arxiv.org/abs/2609.26540"
    author: Romain Puech, Dewang Kumar Agarwal, Antonio Santamaría Escobar, Dimitris Bertsimas
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Domain-matched experts judged 87% of Bespoke-generated lecture videos at or above the rubric midpoint corresponding to a standard MOOC lecture's quality (mean G = 3.42 of 5)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In an expert evaluation of 92 generated videos, 87% scored at or above G = 3, the anchor described as comparable to a standard MOOC lecture, with mean overall quality G = 3.42 (SD = 0.85). [→ Romain Puech 2026](#romain-puech-2026)

## Evidence

### Romain Puech 2026

Romain Puech, Dewang Kumar Agarwal, Antonio Santamaría Escobar, Dimitris Bertsimas. (2026). Bespoke: Generating MOOC-Quality Industry-Personalized Lecture Videos at Scale. arXiv preprint. https://arxiv.org/abs/2609.26540

`q2 · i?` · `design · r2`

Expert rating study of the Bespoke corpus: 25 domain-matched reviewers each scored one 92-video sample on a five-point rubric whose midpoint anchor is a standard MOOC lecture. The article reports "87% of videos at or above" the midpoint, mean G = 3.42 (SD = 0.85), and 48% at G ≥ 4.

> "Reviewers judged 87% of videos at or above “comparable to a standard MOOC lecture” ( 𝐺≥ 3; reviewer-clustered bootstrap 95% CI[76%, 96%]). Mean global quality is 𝐺= 3.42out of5(SD = 0.85); 48% scored𝐺≥ 4"

## Discussion


## Related Claims
- [Across rubric dimensions, content scored highest (A = 4.03) while production scored lowest (D = 3.41), driven by synthetic voice quality (D1 = 3.16)](bespoke-content-strongest-production-weakest-voice.md) — related
- [Reviewer free-text comments identified synthetic voice, slide–narration reveal timing, and slide layout as the main remaining quality issues](bespoke-free-text-voice-reveal-layout-issues.md) — related
- [Pedagogy and production dimensions associated most strongly with global quality (Spearman ρ = 0.68 and 0.66), while content was relatively independent (ρ = 0.46)](bespoke-pedagogy-production-correlate-with-global-quality.md) — related
- [Overall quality was similar across durations and across the 21-lecture held-out set unused during system development](bespoke-quality-stable-across-durations-and-held-out-lectures.md) — related
- [Industry-targeted videos scored only slightly higher on personalization depth than generic-audience videos (0.32 points; modeled increment 0.25, p = 0.11), an effect not resolved under reviewer clustering](bespoke-industry-personalization-increment-small-nonsignificant.md) — related
- [A deterministic slide-image override converts a 0/9 corpus-grounding failure into 9/10 successful slide matches on the same topic](slide-image-override-corpus-grounding-recovery.md) — related
