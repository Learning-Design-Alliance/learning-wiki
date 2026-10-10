---
type: claim
title: "EchoPrompt remains robust across attack settings, obtaining the best AUROC and Best-F1 in four out of five attack groups and improving over IRM by 0.24% AUROC on average"
description: "EchoPrompt remains robust across attack settings, obtaining the best AUROC and Best-F1 in four out of five attack groups and improving over IRM by 0.24% AUROC on average"
id: echoprompt-robust-across-attacks
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
  - id: hongrui-bao-2026-2
    resource: "https://arxiv.org/abs/2608.05741"
    title: "Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao. (2026). ONCE A RESPONSE, ALWAYS A RESPONSE: DETECTING LLM-GENERATED TEXT VIA LATENT PROMPT RESTORATION. arXiv preprint. https://arxiv.org/abs/2608.05741"
    author: Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# EchoPrompt remains robust across attack settings, obtaining the best AUROC and Best-F1 in four out of five attack groups and improving over IRM by 0.24% AUROC on average

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` EchoPrompt sustains detection performance under direct prompting, prompt attacks, paraphrase, perturbation and data-mixing attacks. [→ Hongrui Bao 2026](#hongrui-bao-2026)
`q2 i?` Under stronger generation-task and human-style attacks, detection remains strong, but on non-chat/completion RAID outputs AUROC drops to 82.50%, consistent with weaker latent dependency. [→ Hongrui Bao 2026 (2)](#hongrui-bao-2026-2)

## Evidence

### Hongrui Bao 2026

Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao. (2026). ONCE A RESPONSE, ALWAYS A RESPONSE: DETECTING LLM-GENERATED TEXT VIA LATENT PROMPT RESTORATION. arXiv preprint. https://arxiv.org/abs/2608.05741

`q2 · i?` · `design · r2`

Per-attack comparison (Table 2) with the Llama-3-8B proxy family across five attack groups; under paraphrasing EchoPrompt ranks second, trailing IRM by only 0.87% AUROC and 1.10% Best-F1 while still achieving a Best-F1 of 94.53%.

> "It obtains the best AUROC and Best-F1 in four out of five attack groups and achieves the strongest average attack performance, improving over IRM by 0.24% AUROC and 1.37% Best-F1 on average."

### Hongrui Bao 2026 (2)

Hongrui Bao, Yubing Ren, Jinhan You, Fang Fang, Shi Wang, Yanan Cao. (2026). ONCE A RESPONSE, ALWAYS A RESPONSE: DETECTING LLM-GENERATED TEXT VIA LATENT PROMPT RESTORATION. arXiv preprint. https://arxiv.org/abs/2608.05741

`q2 · i?` · `design · r2`

Evaluation on RAID non-chat/completion outputs shows a performance drop the authors attribute to generation that "does not rely on instruction-tuned assistant behavior". On DetectRL attacks that alter the task or encourage human-like writing, AUROCs remain high (99.98%, 96.96%, 99.60%; 98.46% after back-translation).

> "We also evaluate non-chat/completion outputs from RAID (Dugan et al., 2024), including GPT-2, GPT-3, Cohere, MPT, and Mistral, where EchoPrompt obtains an AUROC of 82.50%. The expected performance drop in this setting is consistent with our hypothesis"

## Discussion


## Related Claims
- [EchoPrompt maintains cross-proxy robustness, averaging 87.06% AUROC across seven proxy models and outperforming DNA-DetectLLM by 2.70% AUROC on average](echoprompt-cross-proxy-robustness.md) — related
- [EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length](echoprompt-length-robustness.md) — related
- [The detection gain comes from restoring the missing prompt-response relation, not merely assigning an assistant role: the full prefix outperforms the empty prompt by 14.73% and 12.57% AUROC on Qwen2.5-3B and 5.63% and 5.33% on Llama-3.1-8B](prompt-component-ablation-context-clause.md) — related
