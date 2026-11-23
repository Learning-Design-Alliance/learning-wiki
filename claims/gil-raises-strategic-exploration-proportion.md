---
type: claim
title: LLM agents rarely explore strategically without guidance; GIL scaffolding raises the proportion of strategic exploration steps
description: LLM agents rarely explore strategically without guidance; GIL scaffolding raises the proportion of strategic exploration steps
id: gil-raises-strategic-exploration-proportion
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: marta-knežević-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.1861"
    title: "Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)"
    author: Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: marta-knežević-2026-2
    resource: "https://doi.org/10.18653/2026.findings-emnlp.1861"
    title: "Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)"
    author: Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM agents rarely explore strategically without guidance; GIL scaffolding raises the proportion of strategic exploration steps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the IL 0-shot condition, strategic exploration accounted for only 21.63% of exploration steps across models, while under GIL it averaged 91.64% (0-shot) and 85.21% (3-shot). [→ Marta Knežević 2026](#marta-knezevic-2026)
`q2 i?` Under the GIL approach the proportion of strategic exploration rose substantially relative to IL. [→ Marta Knežević 2026 (2)](#marta-knezevic-2026-2)

## Evidence

### Marta Knežević 2026

Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)

`q2 · i?` · `causal · r2`

Trajectory annotation study in Results §5.3: two researchers annotated agent trajectories using the control-of-variables rubric (Cohen's Kappa 0.94; 10926 steps annotated in total). The quote reports the IL 0-shot strategic-exploration proportion of "only 21.63%".

> "In the IL setting, strategic exploration accounted for only 21.63% of exploration steps across models in the 0-shot condition."

### Marta Knežević 2026 (2)

Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)

`q2 · i?` · `causal · r2`

Same trajectory-annotation analysis in Results §5.3, reporting the GIL condition of the same measure: strategic exploration "averaging 91.64% in the 0-shot setting and85.21%in the 3-shot setting", with examples also increasing strategic data collection across models.

> "Under the GIL approach, the proportion of strategic exploration rose substantially, averaging 91.64% in the 0-shot setting and85.21%in the 3-shot setting."

## Discussion


## Related Claims
- [GIL reasoning guidance increases explicit cause–effect relationships in agent reasoning, with cause–effect ratios reaching 1.00 in all GIL conditions](gil-increases-explicit-cause-effect-reasoning.md) — related
- [Guided Inquiry Learning scaffolding improves LLM agents' equation-discovery success over unguided IL for most models](gil-scaffolding-improves-llm-equation-discovery.md) — related
- [LLM agents repeat prior hypotheses and refine them in model-specific ways, suggesting a confirmation-bias-like tendency](llm-hypothesis-repetition-confirmation-bias.md) — related
- [LLM-based agents show limited inherent inquiry capabilities, with low rates of correctly discovered equations that improve with in-context examples](llm-agents-limited-inherent-inquiry-capabilities.md) — related
