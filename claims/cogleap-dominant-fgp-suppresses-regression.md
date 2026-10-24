---
type: claim
title: Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fine-grained prompting amplifies upward shifts while suppressing cognitive regression
description: Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fine-grained prompting amplifies upward shifts while suppressing cognitive regression
id: cogleap-dominant-fgp-suppresses-regression
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: cogleap-prevalence
    title: cogleap-prevalence
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: fgp-shift-effects
    title: fgp-shift-effects
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fine-grained prompting amplifies upward shifts while suppressing cognitive regression

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r2`, 1 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` CogLeap is the most prevalent deviation pattern across models and prompting strategies, exceeding 44% under CoT for all models. [→ cogleap-prevalence](#cogleap-prevalence)
`q2 i?` FGP increases CogLeap proportions (e.g., +11.53 percentage points for InternLM3-8B) and reduces CogReg rates (e.g., -10.31 points for InternLM3-8B). [→ fgp-shift-effects](#fgp-shift-effects)

## Evidence

### cogleap-prevalence

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `design · r2`

Cognitive shift distribution analysis (RQ3) across six LLMs on the computer science dataset under CoT prompting, reported in Table 6 and accompanying text. The CogLeap proportion "exceeds 44% across all models".

> "Under CoT prompting, the CogLeap proportion exceeds 44% across all models, withLLaMA-3-8Breaching 54.87%,InternLM3-8Bat 53.63%, andGLM-4-9BandBaichuan2-7Bat 48.05% and 44.64%, respectively."

### fgp-shift-effects

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `causal · r2`

Comparison of cognitive shift distributions between CoT and FGP on the computer science dataset (Table 6). FGP "amplifies this upward bias", with InternLM3-8B's CogLeap increasing by 11.53 percentage points.

> "FGP further amplifies this upward bias: CogLeap increases by 11.53 percentage points forInternLM3-8B, 10.91 points forGLM-4-9B, 14.68 points forSpark Max, 5.53 points forQwen2.5-7B, and 8.32 points forBaichuan2-7B."

## Discussion


## Related Claims
- [The Bloom-driven framework generalizes to social-science questions, with automated rubrics agreeing strongly with experts on usability but only modestly on Bloom level](social-science-generalization-human-agreement.md) — related
- [LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-than-intended cognitive levels regardless of prompting strategy](llm-abstraction-bias-higher-order-overproduction.md) — related
- [LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it](llm-upward-cognitive-shift-asymmetry.md) — related
- [Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain](fgp-improves-catcons-knowcov.md) — related
- [More complex prompts tend to elicit superior results with advanced LLM versions (authors' observation)](complex-prompts-elicit-better-llm-results.md) — related
- [Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward](tza-higher-versus-lower-bloom-targets.md) — a narrower finding that bears on this claim
- [Fine-grained prompting substantially improves question uniqueness and usability of LLM-generated educational questions compared with Chain-of-Thought prompting](fgp-improves-question-uniqueness-usability.md) — related
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related
- [Cognitive architectures reproduce fine-grained educational phenomena beyond final accuracy, including reaction time distributions and qualitative error patterns](cognitive-architectures-reproduce-fine-grained-phenomena.md) — related
