---
type: claim
title: "Multilingual continue pre-training and cross-lingual training improve the dialogue LLM's translation and instruction following"
description: "Multilingual continue pre-training and cross-lingual training improve the dialogue LLM's translation and instruction following"
id: singakids-dialogue-llm-multilingual-optimization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhengyuan-liu-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-industry.86"
    title: "Zhengyuan Liu, Geyu Lin, Hui Li Tan, Huayun Zhang, Yanfeng Lu, Xiaoxue Gao, Stella Xin Yin, He Sun, Hock Huan Goh, Lung Hsiang Wong, Nancy F. Chen. (2025). SingaKids: A Multilingual Multimodal Dialogic Tutor for Language Learning. arXiv preprint. [doi:10.18653/v1/2025.acl-industry.86](https://doi.org/10.18653/v1/2025.acl-industry.86)"
    author: Zhengyuan Liu, Geyu Lin, Hui Li Tan, Huayun Zhang, Yanfeng Lu, Xiaoxue Gao, Stella Xin Yin, He Sun, Hock Huan Goh, Lung Hsiang Wong, Nancy F. Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multilingual continue pre-training and cross-lingual training improve the dialogue LLM's translation and instruction following

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A two-stage optimization (continue pre-training on 14B tokens of four-language mixed data, then multi-task and cross-lingual alignment training) improved multilingual translation and instruction following of the Qwen1.5-4B dialogue model. [→ Zhengyuan Liu 2025](#zhengyuan-liu-2025)

## Evidence

### Zhengyuan Liu 2025

Zhengyuan Liu, Geyu Lin, Hui Li Tan, Huayun Zhang, Yanfeng Lu, Xiaoxue Gao, Stella Xin Yin, He Sun, Hock Huan Goh, Lung Hsiang Wong, Nancy F. Chen. (2025). SingaKids: A Multilingual Multimodal Dialogic Tutor for Language Learning. arXiv preprint. [doi:10.18653/v1/2025.acl-industry.86](https://doi.org/10.18653/v1/2025.acl-industry.86)

`q2 · i?` · `design · r2`

Technical evaluation of the dialogue LLM's multilingual optimization, shown in Figures 6 and 7 as comparisons between the base model and the optimized model. The article reports improvement without printing numeric values in the text; no effect size is stated.

> "Experimental results shown in Figure 6 and Figure 7 show improvement on multilingual translation and instruction following."

## Discussion


## Related Claims
- [Bilingual instruction pairs transfer technique knowledge across languages, more strongly to Indo-Aryan (∆TF = +3.2) than Dravidian (∆TF = +1.8) languages](bilingual-pairs-cross-lingual-technique-transfer.md) — related
