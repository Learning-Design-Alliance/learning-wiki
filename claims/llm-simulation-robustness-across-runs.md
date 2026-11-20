---
type: claim
title: LLM student simulation is robust across repeated runs with non-deterministic temperature settings
description: LLM student simulation is robust across repeated runs with non-deterministic temperature settings
id: llm-simulation-robustness-across-runs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: songlin-xu-and-xinyu-zhang-2023
    resource: "https://doi.org/10.48550/arXiv.2310.19206"
    title: "Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)"
    author: Songlin Xu and Xinyu Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM student simulation is robust across repeated runs with non-deterministic temperature settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When temperature is set to the default value and the experiment is run four times, simulation results show significant consistency (r > 0.7) among running times in most factors. [→ Songlin Xu and Xinyu Zhang 2023](#songlin-xu-and-xinyu-zhang-2023)

## Evidence

### Songlin Xu and Xinyu Zhang 2023

Songlin Xu and Xinyu Zhang. (2023). Leveraging generative artificial intelligence to simulate student learning behavior. [doi:10.48550/arXiv.2310.19206](https://doi.org/10.48550/arXiv.2310.19206)

`q2 · i?` · `design · r2`

Robustness check within the N = 145 simulation study: temperature was set to the default value (1 instead of 0) and the experiment run four times. The authors report "significant consistency (r > 0.7) among different study running times in most factors".

> "we find significant consistency (r > 0.7) among different study running times in most factors, suggesting the robustness of LLMs' simulation."

## Discussion


## Related Claims
- [Lowering an LLM's temperature setting is one lever for improving output consistency](lowering-temperature-improves-llm-consistency.md) — related
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23](temperature-effect-negligible-gpt4o-accuracy.md) — related
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — related
