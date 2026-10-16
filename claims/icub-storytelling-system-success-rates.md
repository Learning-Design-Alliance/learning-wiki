---
type: claim
title: "The iCub storytelling system achieved 88% trial success and 86% VLM sticker-description agreement, with the LLM adding to human contributions in 8% of trials and never correcting them"
description: "The iCub storytelling system achieved 88% trial success and 86% VLM sticker-description agreement, with the LLM adding to human contributions in 8% of trials and never correcting them"
id: icub-storytelling-system-success-rates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: maria-lombardi-2025
    resource: "https://doi.org/10.48550/arxiv.2508.02505"
    title: "Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska. (2025). Would you let a humanoid play storytelling with your child? A usability study on LLM-powered narrative Human-Robot Interaction. https://arxiv.org/abs/2508.02505 [doi:10.48550/arxiv.2508.02505](https://doi.org/10.48550/arxiv.2508.02505)"
    author: Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: maria-lombardi-2025-2
    resource: "https://arxiv.org/abs/2508.02505"
    title: "Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska. (2025). Would you let a humanoid play storytelling with your child? A usability study on LLM-powered narrative Human-Robot Interaction. https://arxiv.org/abs/2508.02505"
    author: Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# The iCub storytelling system achieved 88% trial success and 86% VLM sticker-description agreement, with the LLM adding to human contributions in 8% of trials and never correcting them

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`

## Subclaims
`q3 i?` Across the validation trials the system was robust with an 88% success rate despite failures such as wrong sticker detection, microphone issues and LLM crashes. [→ Maria Lombardi 2025](#maria-lombardi-2025)
`q3 i?` Zero-shot VLM sticker descriptions agreed with the participant's chosen image in 86% of cases, and the LLM added a small contribution to the human's story piece in 8% of trials while never correcting or polishing it. [→ Maria Lombardi 2025 (2)](#maria-lombardi-2025-2)

## Evidence

### Maria Lombardi 2025

Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska. (2025). Would you let a humanoid play storytelling with your child? A usability study on LLM-powered narrative Human-Robot Interaction. https://arxiv.org/abs/2508.02505 [doi:10.48550/arxiv.2508.02505](https://doi.org/10.48550/arxiv.2508.02505)

`q3 · i?` · `design · r2`

Quantitative failure analysis of the validation experiment, logging FSM transitions and trial success across the many interacting modules. The article reports an overall 88% success rate; the 12% failed tests are analysed in the Limitations section.

> "Our system was pretty robust with 88% success rate."

### Maria Lombardi 2025 (2)

Maria Lombardi, Carmela Calabrese, Davide Ghiglino, Caterina Foglino, Davide De Tommaso, Giulia Da Lisca, Lorenzo Natale, Agnieszka Wykowska. (2025). Would you let a humanoid play storytelling with your child? A usability study on LLM-powered narrative Human-Robot Interaction. https://arxiv.org/abs/2508.02505

`q3 · i?` · `design · r2`

VLM detection evaluation computed as agreement between the LLM's sticker description and the image chosen by the participant, yielding 86% overall agreement. A separate LLM-generation analysis found additions in 8% of trials and no corrections of the human's contribution.

> "The overall agreement was 86%."

## Discussion


## Related Claims
- [Adults rated the LLM-powered iCub storytelling system as usable, with a total SUS score of 76.70 indicating good product usability](icub-storytelling-sus-76-good-usability.md) — related
- [Participants liked the co-created stories (mean likability 8.61) and perceived them as coherent (mean coherence 8.28) on a 1-10 scale](icub-stories-liked-and-coherent-ratings.md) — related
