---
type: claim
title: LLMs use fewer extreme grades than human examiners, with grade-dependent opposing biases compressing grades toward the middle
description: LLMs use fewer extreme grades than human examiners, with grade-dependent opposing biases compressing grades toward the middle
id: llm-central-tendency-grade-compression
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: brevik-a-2026
    resource: "https://doi.org/10.3389/feduc.2026.1904452"
    title: "Brevik A, Jerpseth H and Lafontan SR (2026). Large language models as grading assistants in public health education: a method-comparison study of essay-style exam assessment. Front. Educ. 11:1904452. https://doi.org/10.3389/feduc.2026.1904452"
    author: Brevik A, Jerpseth H and Lafontan SR
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# LLMs use fewer extreme grades than human examiners, with grade-dependent opposing biases compressing grades toward the middle

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` LLM grading showed central tendency: fewer A and F grades than humans, upward adjustment of lower grades and downward adjustment of higher grades. [→ Brevik A 2026](#brevik-a-2026)

## Evidence

### Brevik A 2026

Brevik A, Jerpseth H and Lafontan SR (2026). Large language models as grading assistants in public health education: a method-comparison study of essay-style exam assessment. Front. Educ. 11:1904452. https://doi.org/10.3389/feduc.2026.1904452

`q3 · i?` · `design · r2`

Bland-Altman analysis (Figure 3) comparing the average of five ChatGPT sessions with human assessment. The plot showed "opposing biases across the grading scale"; the average numeric grade was 3.63 for humans versus 3.73 for the five ChatGPT parallels, a non-significant difference.

> "Thus, the small overall mean difference concealed opposing biases across the grading scale: upward adjustmen t of lower grades and downward adjustmen t of higher grades. This pattern is consistent with a central tendency or grade-compression effect, whereby ChatGPT concentra ted assessments toward the middle of the grading scale."

## Discussion


## Related Claims
- LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses — related
- [LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes](llm-fast-mode-limited-thinking-mode-better-agreement.md) — related
- [ChatGPT in thinking mode shows the strongest agreement with human examiners on essay-style exam grading (weighted kappa 0.718)](chatgpt-thinking-mode-strongest-human-grading-agreement.md) — related
- [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human rating discrepancies exceeding 1.5 standard deviations in 38% of graduate-level bibliographies](gpt4-essay-score-inflation.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
