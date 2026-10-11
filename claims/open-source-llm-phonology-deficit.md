---
type: claim
title: Open-source LLMs show persistent phonology deficits despite adequate mastery of other subskills
description: Open-source LLMs show persistent phonology deficits despite adequate mastery of other subskills
id: open-source-llm-phonology-deficit
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: shangchao-min-2026
    resource: "https://doi.org/10.21203/rs.3.rs-8820245/v1"
    title: "Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more. (2026). Standardized Assessment of LLM English Proficiency. https://doi.org/10.21203/rs.3.rs-8820245/v1"
    author: Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more
    q: 3
    i: "?"
    kind: design
    rigour: 2
  - id: shangchao-min-2026-2
    resource: "https://doi.org/10.21203/rs.3.rs-8820245/v1"
    title: "Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more. (2026). Standardized Assessment of LLM English Proficiency. https://doi.org/10.21203/rs.3.rs-8820245/v1"
    author: Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Open-source LLMs show persistent phonology deficits despite adequate mastery of other subskills

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`

## Subclaims
`q3 i?` Qwen2.5-7B-Instruct exceeds the mastery threshold for cohesion, vocabulary, and syntax but remains markedly weak on phonology (mastery probability 0.0352 in both prompting settings). [→ Shangchao Min 2026](#shangchao-min-2026)
`q2 i?` The remaining open-source baselines do not reach mastery on any attribute. [→ Shangchao Min 2026 (2)](#shangchao-min-2026-2)

## Evidence

### Shangchao Min 2026

Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more. (2026). Standardized Assessment of LLM English Proficiency. https://doi.org/10.21203/rs.3.rs-8820245/v1

`q3 · i?` · `design · r2`

Cognitive diagnostic analysis using the HO-GDINA model (selected by fit) with an expert-defined Q-matrix over four attributes. The results report Qwen2.5-7B-Instruct "remains markedly weak on phonology (0.0352 in both prompting settings)" while mastering the other three subskills.

> "Among open-source baselines, Qwen2.5-7B-Instruct is the strongest overall: it exceeds the mastery threshold (probability > 0.5) for cohesion, vocabulary, and syntax, but remains markedly weak on phonology (0.0352 in both prompting settings)."

### Shangchao Min 2026 (2)

Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more. (2026). Standardized Assessment of LLM English Proficiency. https://doi.org/10.21203/rs.3.rs-8820245/v1

`q3 · i?` · `design · r2`

Same HO-GDINA mastery analysis: the article states the remaining open-source baselines (RWKV-v6-7b, Meta-Llama-3-8B-Instruct, Mistral-7B-Instruct-v0.3) do not reach mastery on any attribute. No effect size is printed.

> "The remaining open-source baselines do not reach mastery on any attribute."

## Discussion


## Related Claims
- [Few-shot prompting does not uniformly improve LLM performance and can degrade subskill mastery estimates, most notably for phonology](few-shot-prompting-degrades-phonology-mastery.md) — related
- [Targeted enhancements (retrieval-augmented inference, multimodal training) substantially raise open-source models' phonology mastery to near-ceiling levels](targeted-enhancements-raise-phonology-mastery.md) — reports the opposite
