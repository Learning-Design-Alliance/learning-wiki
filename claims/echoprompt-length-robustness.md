---
type: claim
title: "EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length"
description: "EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length"
id: echoprompt-length-robustness
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: hongrui-bao-2026
    resource: "https://arxiv.org/abs/2608.05741"
    title: "Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao. (2026). ONCE A RESPONSE, ALWAYS A RESPONSE: DETECTING LLM-GENERATED TEXT VIA LATENT PROMPT RESTORATION. arXiv preprint. https://arxiv.org/abs/2608.05741"
    author: Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Short texts are challenging for all evaluated zero-shot detectors, but EchoPrompt remains competitive in the shortest bin and its performance rises rapidly with length. [→ Hongrui Bao 2026](#hongrui-bao-2026)

## Evidence

### Hongrui Bao 2026

Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao. (2026). ONCE A RESPONSE, ALWAYS A RESPONSE: DETECTING LLM-GENERATED TEXT VIA LATENT PROMPT RESTORATION. arXiv preprint. https://arxiv.org/abs/2608.05741

`q2 · i?` · `design · r2`

Length-binned AUROC analysis (Figure 4) comparing EchoPrompt with DNA-DetectLLM, IRM, Binoculars and Fast-DetectGPT on DetectRL Length across three Llama-family proxies, showing monotonic improvement with text length.

> "Short texts are challenging for all detectors because they provide fewer tokens for estimating reliable detection signals. Even in the shortest 1-40 word bin, EchoPrompt remains competitive, with an average AUROC of 75.8% across the three Llama-family proxies. As length increases, its performance rises rapidly to 93.1% in the 81-120 bin and 98.9% in the 321-360 bin."

## Discussion


## Related Claims
- [EchoPrompt maintains cross-proxy robustness, averaging 87.06% AUROC across seven proxy models and outperforming DNA-DetectLLM by 2.70% AUROC on average](echoprompt-cross-proxy-robustness.md) — related
- [EchoPrompt remains robust across attack settings, obtaining the best AUROC and Best-F1 in four out of five attack groups and improving over IRM by 0.24% AUROC on average](echoprompt-robust-across-attacks.md) — related
- [The detection gain comes from restoring the missing prompt-response relation, not merely assigning an assistant role: the full prefix outperforms the empty prompt by 14.73% and 12.57% AUROC on Qwen2.5-3B and 5.63% and 5.33% on Llama-3.1-8B](prompt-component-ablation-context-clause.md) — related
- [Detector accuracy declined significantly as text length increased, with both detectors performing best on short texts](detector-accuracy-declines-with-text-length.md) — reports the opposite
