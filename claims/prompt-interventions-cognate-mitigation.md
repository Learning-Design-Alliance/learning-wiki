---
type: claim
title: Prompt-level interventions to reduce cognates mostly failed, while lower sampling temperature and model self-checking offered partial mitigation
description: Prompt-level interventions to reduce cognates mostly failed, while lower sampling temperature and model self-checking offered partial mitigation
id: prompt-interventions-cognate-mitigation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2024
sources:
  - id: marina-sánchez-torrón-2024
    resource: "https://doi.org/10.21203/rs.3.rs-4187415/v1"
    title: "Marina Sánchez-Torrón, Egemen Ipek, Vanessa Enríquez Raído. (2024). Creating subject competence translation tests with GPT-4: A case study in English-to-Turkish translations in the engineering domain. https://doi.org/10.21203/rs.3.rs-4187415/v1"
    author: Marina Sánchez-Torrón, Egemen Ipek, Vanessa Enríquez Raído
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompt-level interventions to reduce cognates mostly failed, while lower sampling temperature and model self-checking offered partial mitigation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Appending an anti-cognate instruction increased the cognate rate to 70% (N = 10); one-shot exemplars were ineffective; adjusting temperature to 0.8 yielded a 10% reduction; and GPT-4 correctly identified cognates when asked about its own questions. [→ Marina Sánchez-Torrón 2024](#marina-sanchez-torron-2024)

## Evidence

### Marina Sánchez-Torrón 2024

Marina Sánchez-Torrón, Egemen Ipek, Vanessa Enríquez Raído. (2024). Creating subject competence translation tests with GPT-4: A case study in English-to-Turkish translations in the engineering domain. https://doi.org/10.21203/rs.3.rs-4187415/v1

`q2 · i?` · `design · r2`

Iterative prompt-engineering experiments in GPT-4 (OpenAI Playground, July 2023): the anti-cognate instruction backfired, one-shot exemplars produced bias toward example terms, and "adjusting the temperature to 0.8 yielded a 10% reduction in answers containing cognates"; lower temperatures caused incorrect Turkish suffixes.

> "We then appended to the prompt above “It is very important that the Turkish translation and the English term aren’t cognates.”, but with this new information, the percentage of questions with cognates increased to 70% (N = 10)."

## Discussion


## Related Claims
- [Test item construction, including avoidance of cognate L1 equivalents, often affects KVL difficulty scores beyond the genuine difficulty of the words](test-item-construction-affects-kvl-difficulty-scores.md) — related
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
