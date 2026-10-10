---
type: claim
title: "The investigate–solve–write scaffold, with personalization disabled, improves all five backbone model families on general agentic benchmarks, with average relative gains of 25.69%–32.03%"
description: "The investigate–solve–write scaffold, with personalization disabled, improves all five backbone model families on general agentic benchmarks, with average relative gains of 25.69%–32.03%"
id: solver-scaffold-transfers-general-agentic-problem-solving
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: bingxi-zhao-2026
    resource: "https://arxiv.org/abs/2604.26962"
    title: "Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962"
    author: Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The investigate–solve–write scaffold, with personalization disabled, improves all five backbone model families on general agentic benchmarks, with average relative gains of 25.69%–32.03%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` With the Hybrid Personalization Engine disabled, the solver-only pipeline improves all five backbone families across HLE, GPQA-Diamond, LiveBench, GAIA, and AA-LCR, with average relative gains ranging from 25.69% to 32.03%. [→ Bingxi Zhao 2026](#bingxi-zhao-2026)

## Evidence

### Bingxi Zhao 2026

Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962

`q2 · i?` · `design · r2`

Extended generalization evaluation on five public benchmarks (HLE, GPQA-Diamond, LiveBench, GAIA, AA-LCR) with personalization disabled, per backbone (Gemini-3-Flash, Sonnet-4.5, Qwen-3.5-Plus, GPT-5-Mini, Minimax-M2.5). Printed gains are relative percentages, not standardized effect sizes.

> "As shown in Table 3, the solver-only pipeline improves all five backbone families, with average relative gains ranging from 25.69% to 32.03%. Because personalization, SKG, and DPM are disabled in this setting, the gains point to the general value of the investigate–solve–write scaffold"

## Discussion


## Related Claims
- [In a preliminary 2×3 controlled lesson study across five backbone LLMs, structured student agents produce more differentiated mastery and misconception traces than a baseline simulator](structured-student-agents-differentiated-mastery-traces.md) — related
- [Expert evaluation finds larger, more capable LLM backbones produce higher-quality multi-domain graphs, with GPT-5 pro rated best](llm-backbone-graph-quality-expert-evaluation.md) — related
