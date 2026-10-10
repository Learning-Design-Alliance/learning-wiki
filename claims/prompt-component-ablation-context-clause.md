---
type: claim
title: "The detection gain comes from restoring the missing prompt-response relation, not merely assigning an assistant role: the full prefix outperforms the empty prompt by 14.73% and 12.57% AUROC on Qwen2.5-3B and 5.63% and 5.33% on Llama-3.1-8B"
description: "The detection gain comes from restoring the missing prompt-response relation, not merely assigning an assistant role: the full prefix outperforms the empty prompt by 14.73% and 12.57% AUROC on Qwen2.5-3B and 5.63% and..."
id: prompt-component-ablation-context-clause
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
    kind: causal
    rigour: 2
---

# The detection gain comes from restoring the missing prompt-response relation, not merely assigning an assistant role: the full prefix outperforms the empty prompt by 14.73% and 12.57% AUROC on Qwen2.5-3B and 5.63% and 5.33% on Llama-3.1-8B

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` The full generic prefix consistently outperforms an empty prompt, and the context clause framing the passage as content generated in response to a user's request provides the strongest individual component contribution. [→ Hongrui Bao 2026](#hongrui-bao-2026)

## Evidence

### Hongrui Bao 2026

Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao. (2026). ONCE A RESPONSE, ALWAYS A RESPONSE: DETECTING LLM-GENERATED TEXT VIA LATENT PROMPT RESTORATION. arXiv preprint. https://arxiv.org/abs/2608.05741

`q2 · i?` · `causal · r2`

Prompt-component ablation (Figure 3) under Qwen2.5-3B and Llama-3.1-8B on DetectRL Multi-Domain and Multi-LLM. Context clause A improves AUROC by 12.63%, 9.28%, 3.84%, and 3.41% across the four settings; leave-one-out results lead to the same conclusion.

> "The component-level results further show that the gain does not simply come from assigning an assistant identity to the proxy model. The role sentence alone brings only limited gains, especially on Llama-3.1-8B, where the improvements are about 1.60% and 1.44%."

## Discussion


## Related Claims
- [EchoPrompt maintains cross-proxy robustness, averaging 87.06% AUROC across seven proxy models and outperforming DNA-DetectLLM by 2.70% AUROC on average](echoprompt-cross-proxy-robustness.md) — related
- [EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length](echoprompt-length-robustness.md) — related
- [EchoPrompt remains robust across attack settings, obtaining the best AUROC and Best-F1 in four out of five attack groups and improving over IRM by 0.24% AUROC on average](echoprompt-robust-across-attacks.md) — related
