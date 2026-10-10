---
type: claim
title: "EchoPrompt maintains cross-proxy robustness, averaging 87.06% AUROC across seven proxy models and outperforming DNA-DetectLLM by 2.70% AUROC on average"
description: "EchoPrompt maintains cross-proxy robustness, averaging 87.06% AUROC across seven proxy models and outperforming DNA-DetectLLM by 2.70% AUROC on average"
id: echoprompt-cross-proxy-robustness
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

# EchoPrompt maintains cross-proxy robustness, averaging 87.06% AUROC across seven proxy models and outperforming DNA-DetectLLM by 2.70% AUROC on average

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` EchoPrompt remains strong across proxy model families and scales, though its performance is still influenced by the specific proxy family selected. [→ Hongrui Bao 2026](#hongrui-bao-2026)

## Evidence

### Hongrui Bao 2026

Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao. (2026). ONCE A RESPONSE, ALWAYS A RESPONSE: DETECTING LLM-GENERATED TEXT VIA LATENT PROMPT RESTORATION. arXiv preprint. https://arxiv.org/abs/2608.05741

`q2 · i?` · `design · r2`

Proxy-model analysis (Figure 5) across Qwen2.5-1.5B/3B, Llama-3.2-1B/3B, Falcon-7B, Llama-3.1-8B and Llama-3-8B. On Llama-family proxies EchoPrompt reaches 93.50% AUROC, exceeding IRM by 1.80% AUROC and 2.63% Best-F1.

> "Figure 5 shows that EchoPrompt remains strong across different proxy model families and scales. Averaged over all proxy settings, EchoPrompt achieves 87.06% AUROC and 83.03% Best-F1, outperforming the strongest competing average baseline, DNA-DetectLLM, by 2.70% AUROC and 3.23% Best-F1."

## Discussion


## Related Claims
- [EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length](echoprompt-length-robustness.md) — related
- [EchoPrompt remains robust across attack settings, obtaining the best AUROC and Best-F1 in four out of five attack groups and improving over IRM by 0.24% AUROC on average](echoprompt-robust-across-attacks.md) — related
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — related
- [The detection gain comes from restoring the missing prompt-response relation, not merely assigning an assistant role: the full prefix outperforms the empty prompt by 14.73% and 12.57% AUROC on Qwen2.5-3B and 5.63% and 5.33% on Llama-3.1-8B](prompt-component-ablation-context-clause.md) — related
