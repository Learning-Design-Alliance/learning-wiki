---
type: claim
title: LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest
description: LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest
id: llm-within-configuration-reliability-high
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: ober-2026
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ober-2026-2
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` All eight ChatGPT4o configurations achieved Cohen's κ above 0.86 and percent agreement exceeding 88% when re-coding the same dataset on two occasions. [→ Ober 2026](#ober-2026)
`q2 i?` ChatGPT4o configurations consistently outperformed ChatGPT4o-mini configurations in within-configuration reliability (κ = 0.882–0.890 vs. 0.865–0.874). [→ Ober 2026 (2)](#ober-2026-2)

## Evidence

### Ober 2026

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Within-configuration reliability analysis comparing two independent LLM generation runs (March 30–April 2 and May 28–30, 2025) with identical parameters on the same chat log dataset. The article reports "All eight configurations achieved Cohen's κ values above 0.86" with the highest at κ = 0.890.

> "All eight configurations achieved Cohen's κ values above 0.86 and percent agreement exceeding 88%. Specifically, the configurations ranged from κ = 0.865 to κ = 0.889, with ChatGPT4o/temperature=0 showing the highest within-configuration reliability (κ = 0.890, 90.52% agreement)"

### Ober 2026 (2)

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Pairwise Cohen's κ comparisons across model types in the same reliability analysis. Regular ChatGPT4o configurations (κ = 0.882–0.890) outperformed mini configurations (κ = 0.865–0.874), supporting hypothesis H1b about model capacity.

> "Across model types, ChatGPT4o configurations consistently outperformed ChatGPT4o-mini configurations. The four ChatGPT4o configurations showed high inter-rater reliability ( κ = 0.882–0.890), though all ChatGPT4o-mini configurations tended to perform slightly lower overall (κ = 0.865–0.874) (H1b supported)"

## Discussion


## Related Claims
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers](llm-inductive-coding-risks-require-human-oversight.md) — related
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [LLM-based transcript classifications agreed highly with human judgment for explicit questions (κ = .778) and math talk (κ = .722), but only moderately for need for help (κ = .562) and confusion (κ = .531)](llm-classification-agreement-varies-by-construct.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — related
