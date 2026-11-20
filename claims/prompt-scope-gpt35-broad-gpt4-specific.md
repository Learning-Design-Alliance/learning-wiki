---
type: claim
title: "Prompt scope affects models differently: GPT-3.5 benefits from broad all-domain prompts while GPT-4 benefits from domain-specific prompts"
description: "Prompt scope affects models differently: GPT-3.5 benefits from broad all-domain prompts while GPT-4 benefits from domain-specific prompts"
id: prompt-scope-gpt35-broad-gpt4-specific
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: jie-tian-2024
    resource: "https://doi.org/10.31219/osf.io/d3nc6"
    title: "Jie Tian, Jixin Hou, Zihao Wu, Peng Shu, Ning Liu, Zhengliang Liu, Yujie Xiang, Beikang Gu, Nicholas Filla, Yiwei Li, Xianyan Chen, Keke Tang, Tianming Liu, and Xianqiao Wang. (2024). Assessing Large Language Models in Mechanical Engineering Education: A Study on Mechanics-Focused Conceptual Understanding. [doi:10.31219/osf.io/d3nc6](https://doi.org/10.31219/osf.io/d3nc6)"
    author: Jie Tian, Jixin Hou, Zihao Wu, Peng Shu, Ning Liu, Zhengliang Liu, Yujie Xiang, Beikang Gu, Nicholas Filla, Yiwei Li, Xianyan Chen, Keke Tang, Tianming Liu, and Xianqiao Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Prompt scope affects models differently: GPT-3.5 benefits from broad all-domain prompts while GPT-4 benefits from domain-specific prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-3.5 achieves better results with prompts covering all domains, whereas GPT-4 tends to do better with domain-specific prompts. [→ Jie Tian 2024](#jie-tian-2024)

## Evidence

### Jie Tian 2024

Jie Tian, Jixin Hou, Zihao Wu, Peng Shu, Ning Liu, Zhengliang Liu, Yujie Xiang, Beikang Gu, Nicholas Filla, Yiwei Li, Xianyan Chen, Keke Tang, Tianming Liu, and Xianqiao Wang. (2024). Assessing Large Language Models in Mechanical Engineering Education: A Study on Mechanics-Focused Conceptual Understanding. [doi:10.31219/osf.io/d3nc6](https://doi.org/10.31219/osf.io/d3nc6)

`q2 · i?` · `causal · r1`

Prompt-engineering analysis (Figure 6) comparing simple, mechanics-specific, and domain-specific system prompts across trials; the article concludes "the prompt covering all domains has a higher likelihood of yielding optimal results" for GPT-3.5 while GPT-4 prefers specific domains. No effect size printed.

> "For GPT -3.5, we can conclude that the prompt covering all domains has a higher likelihood of yielding optimal results. Regarding GPT -4, a more specific domain typically leads to  a higher accuracy, but the improvement is not as substantial as with GPT-3.5."

## Discussion


## Related Claims
- [More complex prompts tend to elicit superior results with advanced LLM versions (authors' observation)](complex-prompts-elicit-better-llm-results.md) — related
- [Domain-specific knowledge, rather than model complexity or general abilities, limits the precision of LLM criterion-based grading](domain-specific-knowledge-limits-llm-grading-precision.md) — related
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
