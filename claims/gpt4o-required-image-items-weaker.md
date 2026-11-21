---
type: claim
title: "GPT-4o performs far worse on items requiring image interpretation (49%) than on text-only items (81%)"
description: "GPT-4o performs far worse on items requiring image interpretation (49%) than on text-only items (81%)"
id: gpt4o-required-image-items-weaker
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: gerd-kortemeyer-2025
    resource: "https://doi.org/10.1103/98hg-rkrf"
    title: "Gerd Kortemeyer, Marina Babayeva, Giulia Polverini, Ralf Widenhorn, Bor Gregorcic. (2025). Multilingual Performance of a Multimodal Artificial Intelligence System on Multisubject Physics Concept Inventories. [doi:10.1103/98hg-rkrf](https://doi.org/10.1103/98hg-rkrf)"
    author: Gerd Kortemeyer, Marina Babayeva, Giulia Polverini, Ralf Widenhorn, Bor Gregorcic
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# GPT-4o performs far worse on items requiring image interpretation (49%) than on text-only items (81%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Performance was 81% on text-only tasks, 79% on tasks with unneeded images, and 49% on tasks with required images; the gap is especially large in Relativity, Optics, Mechanics, Mathematics, and Astronomy. [→ Gerd Kortemeyer 2025](#gerd-kortemeyer-2025)

## Evidence

### Gerd Kortemeyer 2025

Gerd Kortemeyer, Marina Babayeva, Giulia Polverini, Ralf Widenhorn, Bor Gregorcic. (2025). Multilingual Performance of a Multimodal Artificial Intelligence System on Multisubject Physics Concept Inventories. [doi:10.1103/98hg-rkrf](https://doi.org/10.1103/98hg-rkrf)

`q2 · i?` · `associational · r2`

Item-level analysis across all languages, with each item coded as text-only, unneeded-image, or required-image; percentages are correct responses divided by submissions per category as shown in Figure 6. No effect size is reported.

> "Overall, we found that the performance on text-only tasks was 81% , compared to 79% on tasks containing unneeded images, and just 49% on tasks with required images (see Figure 6)."

## Discussion


## Related Claims
- [GPT-4o and Claude 3.5 Sonnet are significantly more accurate on text-only than image-based KMLE questions, while Gemini 1.5 Pro performs comparably across formats](text-only-beats-image-based-kmle-accuracy.md) — related
- [ChatGPT performs poorly on image-based data interpretation across DNA footprinting and BLI questions regardless of image detail](chatgpt-poor-image-inference-scientific-graphs.md) — related
- [Studies using both text- and image-based questions show higher pooled LLM accuracy (78%) than text-only studies (71%)](multimodal-questions-higher-llm-accuracy.md) — related
- [GPT-4o's performance is weaker in Laboratory skills (35.0%), which include strategies for data collection and analysis](gpt4o-subject-category-variation-lab-weakest.md) — related
