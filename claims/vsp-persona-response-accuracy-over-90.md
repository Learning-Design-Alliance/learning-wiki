---
type: claim
title: "Iterative persona refinement against reference answers achieved over 90% VSP response accuracy"
description: "Iterative persona refinement against reference answers achieved over 90% VSP response accuracy"
id: vsp-persona-response-accuracy-over-90
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: li-yue-2026
    resource: "https://doi.org/10.1186/s12888-026-07896-3"
    title: "Li Yue, Wang Guodong, Huang Zhibiao, Ke Xiaoyin, Qin Jianxing, Yu Jialong, Liu Sha, Li Juan, Xu Yong. (2026). Development and preliminary evaluation of a virtual standardized patient system for psychiatric interview training. BMC Psychiatry. https://doi.org/10.1186/s12888-026-07896-3"
    author: Li Yue, Wang Guodong, Huang Zhibiao, Ke Xiaoyin, Qin Jianxing, Yu Jialong, Liu Sha, Li Juan, Xu Yong
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Iterative persona refinement against reference answers achieved over 90% VSP response accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` After iterative testing and refinement, the optimized case personas achieved over 90% response accuracy when implemented in the LLM. [→ Li Yue 2026](#li-yue-2026)

## Evidence

### Li Yue 2026

Li Yue, Wang Guodong, Huang Zhibiao, Ke Xiaoyin, Qin Jianxing, Yu Jialong, Liu Sha, Li Juan, Xu Yong. (2026). Development and preliminary evaluation of a virtual standardized patient system for psychiatric interview training. BMC Psychiatry. https://doi.org/10.1186/s12888-026-07896-3

`q1 · i?` · `design · r2`

Iterative technical evaluation: each VSP case was administered scripted questions and its responses compared with a standardized reference-answer table, with discrepancies informing persona refinement, until "the optimized personas achieved over a 90% response accuracy" in the LLM.

> "When implemented in the LLM, the optimized personas achieved over a 90% response accuracy, demonstrating both clinical validity and technical feasibility."

## Discussion


## Related Claims
- [Coherence is the weakest Dialogue Authenticity Scale dimension for LLM-based virtual patients, compromised by limited inferential reasoning and role-constraint violations](coherence-weakest-dimension-limited-inferential-reasoning.md) — related
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
