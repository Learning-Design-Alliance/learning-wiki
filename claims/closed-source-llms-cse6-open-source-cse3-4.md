---
type: claim
title: Closed-source LLMs reach CSE Level 6 while most open-source baselines cluster at CSE Levels 3–4 on CSEBench
description: Closed-source LLMs reach CSE Level 6 while most open-source baselines cluster at CSE Levels 3–4 on CSEBench
id: closed-source-llms-cse6-open-source-cse3-4
status: review
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

# Closed-source LLMs reach CSE Level 6 while most open-source baselines cluster at CSE Levels 3–4 on CSEBench

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`

## Subclaims
`q3 i?` All closed-source models evaluated reach at least CSE-6 under both zero-shot and few-shot prompting. [→ Shangchao Min 2026](#shangchao-min-2026)
`q3 i?` Most open-source baselines cluster at CSE-3 to CSE-4, with Qwen2.5-7B-Instruct reaching CSE-5 in both prompting conditions. [→ Shangchao Min 2026 (2)](#shangchao-min-2026-2)

## Evidence

### Shangchao Min 2026

Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more. (2026). Standardized Assessment of LLM English Proficiency. https://doi.org/10.21203/rs.3.rs-8820245/v1

`q3 · i?` · `design · r2`

Standard-setting study mapping model scores to CSE levels via Bookmark cut scores on two linked diagnostic forms. The results section reports that "all closed-source models in our study reach at least CSE-6" under both prompting conditions (GPT-4o, Claude4, Deepseek-R1, Gemini2.5-Pro).

> "The standard-setting results (see Table 1) indicate that all closed-source models in our study reach at least CSE-6 under both zero-shot and few-shot prompting."

### Shangchao Min 2026 (2)

Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more. (2026). Standardized Assessment of LLM English Proficiency. https://doi.org/10.21203/rs.3.rs-8820245/v1

`q3 · i?` · `design · r2`

Same standard-setting mapping applied to open-source models (RWKV-v6-7b, LLaMA-3-8B, Mistral-7B, Qwen2.5-7B). The article reports most "open-source baselines cluster at CSE-3 to CSE-4" with Qwen2.5-7B-Instruct reaching CSE-5. No effect size is printed; level assignments are the reported outcome.

> "In contrast, most open-source baselines cluster at CSE-3 to CSE-4, with Qwen2.5-7B-Instruct as a notable exception, reaching CSE-5 in both prompting conditions."

## Discussion


## Related Claims
- [Targeted enhancements (retrieval-augmented inference, multimodal training) substantially raise open-source models' phonology mastery to near-ceiling levels](targeted-enhancements-raise-phonology-mastery.md) — related
- [Few-shot prompting does not uniformly improve LLM performance and can degrade subskill mastery estimates, most notably for phonology](few-shot-prompting-degrades-phonology-mastery.md) — related
