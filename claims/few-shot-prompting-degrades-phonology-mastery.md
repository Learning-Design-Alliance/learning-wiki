---
type: claim
title: Few-shot prompting does not uniformly improve LLM performance and can degrade subskill mastery estimates, most notably for phonology
description: Few-shot prompting does not uniformly improve LLM performance and can degrade subskill mastery estimates, most notably for phonology
id: few-shot-prompting-degrades-phonology-mastery
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: shangchao-min-2026
    resource: "https://doi.org/10.21203/rs.3.rs-8820245/v1"
    title: "Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more. (2026). Standardized Assessment of LLM English Proficiency. https://doi.org/10.21203/rs.3.rs-8820245/v1"
    author: Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Few-shot prompting does not uniformly improve LLM performance and can degrade subskill mastery estimates, most notably for phonology

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Few-shot prompting can slightly degrade subskill mastery, particularly for phonology, in enhanced models such as Qwen2.5-VL CrossAttn. [→ Shangchao Min 2026](#shangchao-min-2026)

## Evidence

### Shangchao Min 2026

Shangchao Min, Shaonan Wang, Xinyu Gao, Hui Wang, Zhiling Jin, and 2 more. (2026). Standardized Assessment of LLM English Proficiency. https://doi.org/10.21203/rs.3.rs-8820245/v1

`q2 · i?` · `causal · r1`

Authors' discussion of prompting-condition comparisons across the model suite on CSEBench. The article states few-shot prompting "slightly degrades subskill mastery, most notably for phonology", visible in enhanced models such as Qwen2.5-VL CrossAttn. No effect size is printed.

> "Few-shot prompting does not uniformly improve performance and, in some cases, slightly degrades subskill mastery, most notably for phonology."

## Discussion


## Related Claims
- [Closed-source LLMs reach CSE Level 6 while most open-source baselines cluster at CSE Levels 3–4 on CSEBench](closed-source-llms-cse6-open-source-cse3-4.md) — related
- [Targeted enhancements (retrieval-augmented inference, multimodal training) substantially raise open-source models' phonology mastery to near-ceiling levels](targeted-enhancements-raise-phonology-mastery.md) — related
- [Open-source LLMs show persistent phonology deficits despite adequate mastery of other subskills](open-source-llm-phonology-deficit.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — a broader claim this one bears on
- [Few-shot prompting modestly improves LLM-human score agreement, inconsistently across datasets and models](few-shot-prompting-inconsistent-grading-gains.md) — related
