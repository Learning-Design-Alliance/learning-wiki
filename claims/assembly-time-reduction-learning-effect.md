---
type: claim
title: The v4.1 redesign reduced mean developer assembly time from 21.4 to 13.7 minutes, but the first-attempt-only mean was 20.4 minutes, with the further reduction reflecting a junior learning effect
description: The v4.1 redesign reduced mean developer assembly time from 21.4 to 13.7 minutes, but the first-attempt-only mean was 20.4 minutes, with the further reduction reflecting a junior learning effect
id: assembly-time-reduction-learning-effect
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: farnaz-baksh-2026
    resource: "https://doi.org/10.48550/arxiv.2606.15239"
    title: "Farnaz Baksh, Matevž B. Zorec, Feiazie Baksh, and Karl Kruusamäe. (2026). Co-Creating Buildable and Open Social Robot Study Companions with University Students. https://arxiv.org/abs/2606.15239 [doi:10.48550/arxiv.2606.15239](https://doi.org/10.48550/arxiv.2606.15239)"
    author: Farnaz Baksh, Matevž B. Zorec, Feiazie Baksh, and Karl Kruusamäe
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: farnaz-baksh-2026-2
    resource: "https://arxiv.org/abs/2606.15239"
    title: "Farnaz Baksh, Matevž B. Zorec, Feiazie Baksh, and Karl Kruusamäe. (2026). Co-Creating Buildable and Open Social Robot Study Companions with University Students. https://arxiv.org/abs/2606.15239"
    author: Farnaz Baksh, Matevž B. Zorec, Feiazie Baksh, and Karl Kruusamäe
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The v4.1 redesign reduced mean developer assembly time from 21.4 to 13.7 minutes, but the first-attempt-only mean was 20.4 minutes, with the further reduction reflecting a junior learning effect

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r1`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` Assembly times trended downward from 21.4 to 13.7 minutes across versions, compressing the assembly-to-disassembly ratio from 4.3x to 2.9x. [→ Farnaz Baksh 2026](#farnaz-baksh-2026)
`q2 i?` On a first-attempt-only basis the v4.1 mean was 20.4 minutes against v4's 21.4, and the article attributes the further reduction to a substantial junior learning effect of about 43%, suggesting the redesign primes learning rather than driving first-build speedup. [→ Farnaz Baksh 2026 (2)](#farnaz-baksh-2026-2)

## Evidence

### Farnaz Baksh 2026

Farnaz Baksh, Matevž B. Zorec, Feiazie Baksh, and Karl Kruusamäe. (2026). Co-Creating Buildable and Open Social Robot Study Companions with University Students. https://arxiv.org/abs/2606.15239 [doi:10.48550/arxiv.2606.15239](https://doi.org/10.48550/arxiv.2606.15239)

`q2 · i?` · `causal · r1`

Study 1 within-subjects timing data from four developers performing full assembly and disassembly of both versions. The article reports times "trended downward (21.4→ 13.7 minutes)"; only descriptive means are printed, so impact is null.

> "Assembly times trended downward (21.4→ 13.7 minutes; see Fig. 3), compressing the assembly-to-disassembly ratio from 4.3×to 2.9×."

### Farnaz Baksh 2026 (2)

Farnaz Baksh, Matevž B. Zorec, Feiazie Baksh, and Karl Kruusamäe. (2026). Co-Creating Buildable and Open Social Robot Study Companions with University Students. https://arxiv.org/abs/2606.15239

`q2 · i?` · `design · r2`

Study 1 secondary analysis of junior developers' second v4.1 assembly attempts, conducted a day or two after the first. The article prints the ≈43% learning effect and the 20.4 vs 21.4 first-attempt means as descriptive values only.

> "On a first-attempt-only basis, v4.1’s mean is 20.4 minutes against v4’s 21.4; the fur-ther reduction to the 13.7 minutes in Table 3 reflects a substantial junior learning effect (≈43%, with one junior reaching 14.1 minutes on second attempt, Fig. 3)"

## Discussion


## Related Claims
- [First-time builders completed the v4.1 build in a mean of 39.1 minutes with SUS 74.6 (Good), but showed higher assembly Mental Demand than developers and tactile fragility concerns around snap-fit components](first-time-builder-v41-validation.md) — related
- [DfA/DfD-informed mechanical redesign of the RSC chassis raised developers' perceived usability from Poor (SUS 59.4) to Excellent (SUS 89.4)](dfa-dfd-redesign-raises-sus-developers.md) — related
- [The v4.1 redesign achieved tool-free serviceability, with disassembly workload reduction consistent across all measures and disassembly rated near-perfectly easy](tool-free-serviceability-disassembly-ease.md) — related
