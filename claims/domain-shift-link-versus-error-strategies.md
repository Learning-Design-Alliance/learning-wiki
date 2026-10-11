---
type: claim
title: "LLM distractor-generation strategies differ by domain: error description and simulation dominate on math while conceptual linking and discriminability checks dominate on science"
description: "LLM distractor-generation strategies differ by domain: error description and simulation dominate on math while conceptual linking and discriminability checks dominate on science"
id: domain-shift-link-versus-error-strategies
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yanick-zengaffinen-2026
    resource: "https://arxiv.org/abs/2603.15547"
    title: "Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547"
    author: Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM distractor-generation strategies differ by domain: error description and simulation dominate on math while conceptual linking and discriminability checks dominate on science

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` LINK is prevalent on SciQ but nearly absent on Eedi, whereas ERR_DESC and ERR_SIM dominate on Eedi but appear only sporadically on SciQ. [→ Yanick Zengaffinen 2026](#yanick-zengaffinen-2026)

## Evidence

### Yanick Zengaffinen 2026

Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation for Multiple-Choice Questions. https://arxiv.org/abs/2603.15547

`q2 · i?` · `causal · r2`

Annotation of 885 DEEPSEEK-V3.2 and GLM-4.7 reasoning traces with the ten-strategy taxonomy; Table 3 reports e.g. Error Description 22.83±2.70 occurrences on Eedi versus 0.78±0.31 on SciQ, and Conceptual Link 0.04±0.05 on Eedi versus 5.36±0.87 on SciQ.

> "LINK is prevalent on SciQ but nearly absent on Eedi, whereas ERR_DESC and ERR_SIM dominate on Eedi but appear only sporadically on SciQ."

## Discussion


## Related Claims
- [On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design](llms-solve-first-error-injection-edi.md) — related
- [LLM error simulation rarely fails, but the model is less likely to reproduce a targeted distractor on problems with longer correct solutions](error-simulation-accurate-but-longer-solutions-harder.md) — related
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
