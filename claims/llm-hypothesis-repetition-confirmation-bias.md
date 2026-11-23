---
type: claim
title: LLM agents repeat prior hypotheses and refine them in model-specific ways, suggesting a confirmation-bias-like tendency
description: LLM agents repeat prior hypotheses and refine them in model-specific ways, suggesting a confirmation-bias-like tendency
id: llm-hypothesis-repetition-confirmation-bias
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: marta-knežević-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.1861"
    title: "Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)"
    author: Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM agents repeat prior hypotheses and refine them in model-specific ways, suggesting a confirmation-bias-like tendency

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models explicitly repeated the same hypotheses in a high ratio of trajectories, reaching up to 44% in the 0-shot IL setup with Qwen-32B. [→ Marta Knežević 2026](#marta-knezevic-2026)

## Evidence

### Marta Knežević 2026

Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)

`q2 · i?` · `causal · r2`

Hypothesis-behavior annotation in Results §5.3 (Table 3, Mean ± SEM) covering support, repeated hypotheses, numerical modification, and term modification. The quote reports repeated hypotheses "reaching up to 44%" for Qwen-32B; Qwen models added numerical factors while Llama-70B added variable terms.

> "We found that models explicitly repeated the same hypotheses in a relatively high ratio of trajectories reaching up to 44% in the 0-shot IL setup using the Qwen-32B model."

## Discussion


## Related Claims
- [LLM agents rarely explore strategically without guidance; GIL scaffolding raises the proportion of strategic exploration steps](gil-raises-strategic-exploration-proportion.md) — related
- [Re-sampling the same question against a fixed interaction history produces diverging LLM answers, revealing stochastic flips and trajectory bifurcation](llm-resampling-reveals-stochastic-flips.md) — related
- [GIL reasoning guidance increases explicit cause–effect relationships in agent reasoning, with cause–effect ratios reaching 1.00 in all GIL conditions](gil-increases-explicit-cause-effect-reasoning.md) — related
- [GPT-2 generates different text for the same prompt across repeated runs, demonstrating its stochastic output](gpt2-stochastic-output-varies-across-runs.md) — related
