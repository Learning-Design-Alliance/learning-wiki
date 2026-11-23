---
type: claim
title: "Distilled models use 10-60% fewer tokens than retrieval-augmented teachers while achieving higher success"
description: "Distilled models use 10-60% fewer tokens than retrieval-augmented teachers while achieving higher success"
id: distilled-models-fewer-tokens-than-rag
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: humaid-ibrahim-2025
    resource: "https://doi.org/10.48550/arXiv.2510.01375"
    title: "Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. [doi:10.48550/arXiv.2510.01375](https://doi.org/10.48550/arXiv.2510.01375)"
    author: Humaid Ibrahim, Nikolai Rozanov, Marek Rei
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Distilled models use 10-60% fewer tokens than retrieval-augmented teachers while achieving higher success

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Distilled 14B models use 10% fewer tokens in ALFWorld and 47% fewer in WebShop vs base, and 17-61% fewer vs RAG, while taking fewer steps. [→ Humaid Ibrahim 2025](#humaid-ibrahim-2025)

## Evidence

### Humaid Ibrahim 2025

Humaid Ibrahim, Nikolai Rozanov, Marek Rei. (2025). Fine-Tuning with RAG for Improving LLM Learning of New Skills. ICLR 2026. [doi:10.48550/arXiv.2510.01375](https://doi.org/10.48550/arXiv.2510.01375)

`q2 · i?` · `causal · r2`

Efficiency analysis (Table 5) with Qwen-2.5 14B Instruct, metrics averaged per episode: distilled ALFWorld 44.82k tokens/16.68 steps at 91.04% success; WebShop 4.27k tokens/4.98 steps at score 72.40. The authors attribute this to cleaner action sequences learned from hint-improved teacher demonstrations.

> "Distilled models use 10% fewer in ALFWorld and 47% fewer in WebShop vs. base, and 17–61% fewer vs. RAG, while taking fewer steps to complete tasks."

## Discussion


## Related Claims
- [Distilled students achieve the highest task success without retrieval, exceeding base, RAG and SFT agents on ALFWorld and WebShop](distilled-students-highest-success-without-retrieval.md) — related
- [Small 7B models benefit dramatically from hints in ALFWorld but struggle to use them effectively at inference in WebShop](small-models-hints-scale-dependent.md) — related
- [The OCR-based text input uses far fewer tokens than image-based multimodal input for the same slide, making it more cost-effective](ocr-input-lower-token-cost-than-image-input.md) — related
- Retrieval depth k shows diminishing returns: large hint blocks become counterproductive, with a sharp drop at k=9 in ALFWorld and reduced scores at k=6 and 9 in WebShop — related
