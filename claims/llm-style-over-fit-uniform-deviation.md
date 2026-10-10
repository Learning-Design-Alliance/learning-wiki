---
type: claim
title: On structured pedagogical-judgment items, all evaluated models share a systematic style-over-fit deviation, converging on the same non-reference option
description: On structured pedagogical-judgment items, all evaluated models share a systematic style-over-fit deviation, converging on the same non-reference option
id: llm-style-over-fit-uniform-deviation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: yilin-jiang-2026
    resource: "https://arxiv.org/abs/2608.09548"
    title: "Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548"
    author: Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: yilin-jiang-2026-2
    resource: "https://arxiv.org/abs/2608.09548"
    title: "Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548"
    author: Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# On structured pedagogical-judgment items, all evaluated models share a systematic style-over-fit deviation, converging on the same non-reference option

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r3` · `q2`

## Subclaims
`q2 i?` Models substitute pedagogical style for pedagogical fit, favoring gentler, more Socratic, more elaborate options over the goal-optimal reference. [→ Yilin Jiang 2026](#yilin-jiang-2026)
`q2 i?` On 105 of the 500 judgment items, at least eight of ten models select a single common non-reference option; 140 items are answered correctly by all ten and 87 by none. [→ Yilin Jiang 2026 (2)](#yilin-jiang-2026-2)

## Evidence

### Yilin Jiang 2026

Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548

`q2 · i?` · `design · r3`

Uniform-deviation analysis of the 500-item structured judgment task, scored by exact match with no LLM judge. The authors identify the shared error as "substitutionofpedagogical style for pedagogical fit"; on some items the rationale identifies the reference answer then declines it as too direct, an explicit override by style preference.

> "The sharederrorisasubstitutionofpedagogical style for pedagogical fit. Models favor the option that is more gentle, more Socratic, more elaborate, or phrased in a morestudent-centeredregisterovertheoptionthatbestserves the specific developmental goal an item names."

### Yilin Jiang 2026 (2)

Yilin Jiang, Xiaorong Zhu, Fei Tan, Zicheng Zhang, Kaiyi Huang, Yang Yu, Zexuan Fei, Yiming Luo, Keqian Li, Hao Hao, Guangtao Zhai, Aimin Zhou. (2026). ELBench: A Multi-Dimensional Benchmark for Education-Facing Large Language Models. https://arxiv.org/abs/2608.09548

`q2 · i?` · `design · r3`

Item-level analysis across ten evaluated models on the structured judgment task. Printed counts: 140 items correct by all ten, 87 by none, 105 items with at least eight models on the common non-reference option (mean share 0.97), giving median item discrimination index D = 0; grading alignment verified on 4,999 of 5,000 responses.

> "On105itemsatleast eightofthetenmodelsselectasinglecommonnon-reference option, on 84 items at least nine do, and on 53 items all ten do; the mean share of models on the common non-reference optionis0.97."

## Discussion


## Related Claims
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md) — related
