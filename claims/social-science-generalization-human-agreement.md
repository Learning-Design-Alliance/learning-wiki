---
type: claim
title: The Bloom-driven framework generalizes to social-science questions, with automated rubrics agreeing strongly with experts on usability but only modestly on Bloom level
description: The Bloom-driven framework generalizes to social-science questions, with automated rubrics agreeing strongly with experts on usability but only modestly on Bloom level
id: social-science-generalization-human-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: social-fgp
    title: social-fgp
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: human-agreement
    title: human-agreement
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The Bloom-driven framework generalizes to social-science questions, with automated rubrics agreeing strongly with experts on usability but only modestly on Bloom level

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r1`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` On the social-science subset, FGP suppresses cognitive regression to 0% for InternLM3-8B and Spark3.5-Max and raises Spark3.5-Max's CogLeap from 42.50% to 66.67%. [→ social-fgp](#social-fgp)
`q2 i?` The automatic rubric attains average agreement rates of 90.75%, 98.08%, and 95.83% with expert annotations on uniqueness, readability, and answerability, but Bloom-level agreement is only 46.58%. [→ human-agreement](#human-agreement)

## Evidence

### social-fgp

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `causal · r1`

Cognitive shift analysis on the 100-item social-science subset (RQ6, Table 8), comparing CoT and FGP across the six models. CogReg drops "to 0% for InternLM3-8B and Spark3.5-Max" under FGP.

> "with CogReg dropping to 0% for InternLM3-8B and Spark3.5-Max and CogLeap for Spark3.5-Max increasing from 42.50% to 66.67% (Table 8), indicating that higher-order cognitive alignment can likewise be promoted via prompt design in non-STEM domains."

### human-agreement

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `design · r2`

Small-scale human validation of the automated metrics against expert annotations on the social-science subset (Table 9). Usability criteria agree at 90.75-98.08%, while "Bloom-level agreement is more modest at 46.58%".

> "the automatic rubric attains average agreement rates of 90.75%, 98.08%, and 95.83% with expert annotations on uniqueness, readability, and answerability, respectively, while Bloom-level agreement is more modest at 46.58% (Table 9)"

## Discussion


## Related Claims
- [Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fine-grained prompting amplifies upward shifts while suppressing cognitive regression](cogleap-dominant-fgp-suppresses-regression.md) — related
- [Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain](fgp-improves-catcons-knowcov.md) — related
- [Fine-grained prompting substantially improves question uniqueness and usability of LLM-generated educational questions compared with Chain-of-Thought prompting](fgp-improves-question-uniqueness-usability.md) — related
- [LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-than-intended cognitive levels regardless of prompting strategy](llm-abstraction-bias-higher-order-overproduction.md) — related
- [LLMs support the shift from memorization-focused to competency-based assessment by generating rubrics, varied assessment items and authentic scenario-based tasks](llms-support-competency-based-assessment-design.md) — related
