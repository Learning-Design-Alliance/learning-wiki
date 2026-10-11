---
type: claim
title: Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B
description: Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B
id: finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: qian-shen-2026
    resource: "https://arxiv.org/abs/2605.13709"
    title: "Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite. (2026). Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety. https://arxiv.org/abs/2605.13709"
    author: Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite
    q: 2
    i: 3
    kind: causal
    rigour: 1
  - id: qian-shen-2026-2
    resource: "https://arxiv.org/abs/2605.13709"
    title: "Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite. (2026). Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety. https://arxiv.org/abs/2605.13709"
    author: Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2` · `i3` large

## Subclaims
`q2 i3` Welch's T-tests comparing best-performing fine-tuned 8B stories against GPT-4o and Llama 3.3 70B stories show all p-values below 0.001 and all Cohen's d greater than 0.8 for coherence, syntactic complexity, Spache readability, and LM-PPL. [→ Qian Shen 2026](#qian-shen-2026)
`q2 i?` Fine-tuned 8B LLMs generate stories with difficulty levels more suitable for K-2 children than zero-shot GPT-4o and Llama 3.3 70B, with almost no discernible safety issues. [→ Qian Shen 2026 (2)](#qian-shen-2026-2)

## Evidence

### Qian Shen 2026

Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite. (2026). Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety. https://arxiv.org/abs/2605.13709

`q2 · i3` · `causal · r1`

Significance testing (Welch's T-test) in the Results section compared best-mean fine-tuned 8B stories against GPT-4o and Llama 3.3 70B stories on four metrics; "all p-values are less than 0.001" and all Cohen's d greater than 0.8.

> "In the results of Welch's T-test, all p-values are less than 0.001, and all Cohen's d are greater than 0.8, which shows that the differences in the mean scores for coherence, syntactic complexity, Spache readability and LM-PPL between the stories of fine-tuned LLMs and those of GPT-4o and Llama 3.3 70B are statistically significant."

### Qian Shen 2026 (2)

Qian Shen, Fanghua Cao, Min Yao, Shlok Gilda, Bonnie J. Dorr, Walter L. Leite. (2026). Children's English Reading Story Generation via Supervised Fine-Tuning of Compact LLMs with Controllable Difficulty and Safety. https://arxiv.org/abs/2605.13709

`q2 · i?` · `design · r2`

Authors' summary of the quantitative evaluation of stories generated across the SFT experiments versus the two zero-shot large models, stating "difficulty levels more suitable for K-2 children" and near-absent safety issues.

> "In summary, quantitative evaluation shows that our SFT experiments, particularly Rewarded SFT, enable fine-tuned 8B LLMs to generate stories with difficulty levels more suitable for K-2 children than those from GPT-4o and Llama 3.3 70B, while presenting almost no discernible safety issues."

## Discussion


## Related Claims
- [Epi2Diff achieves the best performance across all four item-difficulty test sets and all reported metrics, outperforming SLM fine-tuning, LLM prompting, and supervised LLM adaptation baselines](epi2diff-best-across-four-difficulty-benchmarks.md) — related
- [Rewarded SFT produces the most stable outputs among the SFT designs, nearly free of hallucinations and story-irrelevant material](rewarded-sft-most-stable-outputs.md) — related
- [SFT with simulated children's reading errors yields higher LM-PPL than other experiments, driven by brevity and post-story irrelevant content](simulated-errors-experiment-higher-lm-ppl.md) — related
- [The adapted 4B model outperforms zero-shot cloud baselines on lexical and semantic measures despite lower raw accuracy](adapted-4b-outpaces-cloud-baselines-on-lexical-semantic-measures.md) — related
- [Self-hosted open-weight LLMs offer privacy, reproducibility, and environmental advantages over commercial LLM interfaces in educational ITSs](self-hosted-llm-advantages-education.md) — related
