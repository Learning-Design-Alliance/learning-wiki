---
type: claim
title: Experts iterated extensively on prompts, averaging 30 executions and 10 library commits, with most reaching their final textbook-level prompt in 3 to 6 iterations
description: Experts iterated extensively on prompts, averaging 30 executions and 10 library commits, with most reaching their final textbook-level prompt in 3 to 6 iterations
id: prompthive-prompt-iteration-behavior
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: mohi-reza-2025
    resource: "https://doi.org/10.1145/3706598.3714051"
    title: "Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos. (2025). PromptHive: Bringing Subject Matter Experts Back to the Forefront with Collaborative Prompt Engineering for Educational Content Creation. arXiv preprint. Originally published 2024. [doi:10.1145/3706598.3714051](https://doi.org/10.1145/3706598.3714051)"
    author: Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: mohi-reza-2025-2
    resource: "https://doi.org/10.1145/3706598.3714051"
    title: "Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos. (2025). PromptHive: Bringing Subject Matter Experts Back to the Forefront with Collaborative Prompt Engineering for Educational Content Creation. arXiv preprint. Originally published 2024. [doi:10.1145/3706598.3714051](https://doi.org/10.1145/3706598.3714051)"
    author: Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Experts iterated extensively on prompts, averaging 30 executions and 10 library commits, with most reaching their final textbook-level prompt in 3 to 6 iterations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Logging data showed participants made on average 30 executions (SD = 12.57) and 10 commits (SD = 5.02) to author 10 textbook-level and 59 lesson-level prompts. [→ Mohi Reza 2025](#mohi-reza-2025)
`q2 i?` Participants took between 1 and 17 iterations to arrive at their final textbook-level prompt, with most taking between 3 and 6. [→ Mohi Reza 2025 (2)](#mohi-reza-2025-2)

## Evidence

### Mohi Reza 2025

Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos. (2025). PromptHive: Bringing Subject Matter Experts Back to the Forefront with Collaborative Prompt Engineering for Educational Content Creation. arXiv preprint. Originally published 2024. [doi:10.1145/3706598.3714051](https://doi.org/10.1145/3706598.3714051)

`q2 · i?` · `design · r2`

Log analysis of the PromptHive backend logging engine during 1.5-hour collaborative prompt-writing sessions with ten experts. The logs show "30 executions" and "10 commits each" on average; these are descriptive statistics with no effect size.

> "indicating that on average, they made 30 executions (𝑆𝐷 = 12.57) and 10 commits each (𝑆𝐷 = 5.02) to author the 10 textbook-level prompts and 59 lesson-level prompts covering hints for the entirety of a textbook"

### Mohi Reza 2025 (2)

Mohi Reza, Ioannis Anastasopoulos, Shreya Bhandari, Zachary A Pardos. (2025). PromptHive: Bringing Subject Matter Experts Back to the Forefront with Collaborative Prompt Engineering for Educational Content Creation. arXiv preprint. Originally published 2024. [doi:10.1145/3706598.3714051](https://doi.org/10.1145/3706598.3714051)

`q2 · i?` · `design · r2`

The same log analysis traced execution chains per participant; iteration counts ranged from 1 (P2) to 17 (P3 and P8), with "most taking between 3 to 6 iterations". Descriptive only.

> "participants did between 1 (P2) and 17 (P3 and P8) iterations based on executions to arrive at their final textbook-level prompt, with most taking between 3 to 6 iterations"

## Discussion


## Related Claims
- [Most lesson-level prompts needed tailoring: only 8 of 59 were verbatim textbook-level clones](lesson-level-prompts-needed-tailoring.md) — related
- [Iterative prompt refinement and expert pilot-testing may partly explain favorable LLM virtual patient output quality](iterative-prompt-refinement-expert-testing-improves-output.md) — related
- [Hints generated with PromptHive produced learning gains on par with hints manually authored by subject matter experts without generative AI](prompthive-hints-learning-gains-on-par-with-human.md) — related
- [All subjects iterated while designing a training simulator specification, with iteration counts ranging from 10 to 30](all-subjects-iterated-log-evidence.md) — related
- [Upvotes on shared prompts did not correlate with a prompt's influence on other experts' lesson-level prompts](upvotes-did-not-correlate-with-prompt-influence.md) — related
