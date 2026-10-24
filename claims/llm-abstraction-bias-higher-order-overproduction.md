---
type: claim
title: LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-than-intended cognitive levels regardless of prompting strategy
description: LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-than-intended cognitive levels regardless of prompting strategy
id: llm-abstraction-bias-higher-order-overproduction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: abstraction-bias
    title: abstraction-bias
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-than-intended cognitive levels regardless of prompting strategy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` LLMs consistently prefer generating semantically rich and abstract questions, reflecting an inherent tendency toward higher cognitive levels under both CoT and FGP. [→ abstraction-bias](#abstraction-bias)

## Evidence

### abstraction-bias

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `causal · r1`

Authors' interpretation of the cognitive shift results (RQ3/RQ4) across six LLMs and both prompting strategies, offered as an explanation of the persistent upward drift in generated Bloom levels. The paper states LLMs show "an inherent tendency toward higher cognitive levels".

> "Regardless of whether CoT or FGP is used, LLMs consistently prefer generating semantically rich and abstract questions, reflecting an inherent tendency toward higher cognitive levels."

## Discussion

## Related Claims

- [LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it](llm-upward-cognitive-shift-asymmetry.md) — the general claim this finding bears on, with the studies behind it
- [Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fine-grained prompting amplifies upward shifts while suppressing cognitive regression](cogleap-dominant-fgp-suppresses-regression.md) — related
- [Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain](fgp-improves-catcons-knowcov.md) — related
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related
- [The Bloom-driven framework generalizes to social-science questions, with automated rubrics agreeing strongly with experts on usability but only modestly on Bloom level](social-science-generalization-human-agreement.md) — related
