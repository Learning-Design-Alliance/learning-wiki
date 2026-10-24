---
type: claim
title: "SFT with simulated children's reading errors yields higher LM-PPL than other experiments, driven by brevity and post-story irrelevant content"
description: "SFT with simulated children's reading errors yields higher LM-PPL than other experiments, driven by brevity and post-story irrelevant content"
id: simulated-errors-experiment-higher-lm-ppl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: qian-shen-2026
    resource: "https://doi.org/10.48550/arxiv.2605.13709"
    title: "Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite. (2026). Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety. https://arxiv.org/abs/2605.13709 [doi:10.48550/arxiv.2605.13709](https://doi.org/10.48550/arxiv.2605.13709)"
    author: Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SFT with simulated children's reading errors yields higher LM-PPL than other experiments, driven by brevity and post-story irrelevant content

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Mean LM-PPL values for stories from SFT with simulated children's reading errors were higher than those of other experiments, attributed to story brevity and appended irrelevant content causing genre shifts. [→ Qian Shen 2026](#qian-shen-2026)

## Evidence

### Qian Shen 2026

Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite. (2026). Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety. https://arxiv.org/abs/2605.13709 [doi:10.48550/arxiv.2605.13709](https://doi.org/10.48550/arxiv.2605.13709)

`q2 · i?` · `design · r2`

Qualitative outlier analysis in the Results section: stories from the simulated-errors experiment had higher mean LM-PPL than other experiments, explained by brevity-driven uncertainty and appended narrative-irrelevant content causing abrupt genre shifts.

> "Primarily, the mean LM-PPL values for stories from SFT with simulated children's reading errors were higher than those of other experiments. Observation of these stories revealed that their higher LM-PPL values were either due to their brevity, which led to increased uncertainty and higher cross-entropy per word, or because the LLMs appended content irrelevant to the narrative after generating a short story."

## Discussion


## Related Claims
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
- [Rewarded SFT produces the most stable outputs among the SFT designs, nearly free of hallucinations and story-irrelevant material](rewarded-sft-most-stable-outputs.md) — related
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
