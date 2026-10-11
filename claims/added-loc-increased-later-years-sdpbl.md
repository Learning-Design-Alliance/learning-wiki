---
type: claim
title: "Students' implementation throughput (added LOC per lecture) increased in 2024–2025 cohorts relative to 2022–2023, temporally corresponding with LLM proliferation"
description: "Students' implementation throughput (added LOC per lecture) increased in 2024–2025 cohorts relative to 2022–2023, temporally corresponding with LLM proliferation"
id: added-loc-increased-later-years-sdpbl
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hidetake-tanaka-2026
    resource: "https://arxiv.org/abs/2608.30572"
    title: "Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu. (2026). Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL. https://arxiv.org/abs/2608.30572"
    author: Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: hidetake-tanaka-2026-2
    resource: "https://arxiv.org/abs/2608.30572"
    title: "Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu. (2026). Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL. https://arxiv.org/abs/2608.30572"
    author: Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Students' implementation throughput (added LOC per lecture) increased in 2024–2025 cohorts relative to 2022–2023, temporally corresponding with LLM proliferation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`

## Subclaims
`q2 i?` Steel-Dwass tests revealed statistically significant year differences in added LOC in seven of eight lectures, with earlier years (2022, 2023) having fewer added LOC than later years (2024, 2025). [→ Hidetake Tanaka 2026](#hidetake-tanaka-2026)

## Evidence

### Hidetake Tanaka 2026

Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu. (2026). Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL. https://arxiv.org/abs/2608.30572

`q2 · i?` · `associational · r1`

Retrospective observational analysis of Git commit added LOC per student per lecture for 38 (2022), 28 (2023), 25 (2024), and 14 (2025) students, with Steel-Dwass tests summarized in Table 1; lec11 was not significant (p = 0.1608).

> "The Steel- Dwass tests revealed statistically signiﬁcant diﬀerences among academic years in seven of the eight lectures: lec06, lec07, lec08, lec09, l ec10, lec12, and lec13. Only lec11 showed no signiﬁcant diﬀerences."

### Hidetake Tanaka 2026 (2)

Hidetake Tanaka, Hiroshi Igaki, Kazumasa Shimari, Kiyoshi Honda, and Naoki Fukuyasu. (2026). Practical Implementation Report on Introducing Spec-Driven Development Using AI Agents in Software Development PBL. https://arxiv.org/abs/2608.30572

`q2 · i?` · `design · r2`

The same observational LOC analysis reports the direction of the significant pairwise contrasts: "earlier years (2022, 2023) have f ewer added LOC than later years (2024, 2025)", e.g., Year 2022 significantly lower than Year 2024 in lec06, lec07, lec08, lec10, and lec12.

> "A consistent pattern is that earlier years (2022, 2023) have f ewer added LOC than later years (2024, 2025)."

## Discussion


## Related Claims
- [Publication counts in the selected sample increased in 2023 and 2024, coinciding with growing attention to large language models and generative AI](ai-math-publications-growth-2023-2024-llm-shift.md) — related
- [Discourse on AI in education peaked sharply in 2023 with the rise of generative AI tools such as ChatGPT before declining in 2024](aied-topic-peaked-2023-declined-2024.md) — related
- [Research on AI applications in science and chemistry education increased between 2021 and 2024, with 11 of 18 reviewed studies published in 2024](ai-science-chemistry-studies-increase-2021-2024.md) — related
- [Research on LLM-based family education increased sharply after 2023, following ChatGPT's release](llm-family-education-publication-growth-post-2023.md) — related
- [Research on AI and GAI in education surged after ChatGPT's late-2022 release, with 54% of reviewed articles published in 2023](gai-research-surge-2023-chatgpt.md) — related
- [Publication of review-automation papers grew at an estimated 4.7% monthly rate from January 2020 through June 2025](review-automation-publication-growth-4-7-monthly.md) — related
- [In SDPBL with SDD introduced, AI usage varies greatly by team and phase, with all teams using AI in Implementation and Debugging but large team differences in Investigation and Planning](ai-usage-varies-by-team-and-phase-sdpbl-sdd.md) — related
