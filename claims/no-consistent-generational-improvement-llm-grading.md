---
type: claim
title: Newer LLM generations do not consistently agree better with human essay graders
description: Newer LLM generations do not consistently agree better with human essay graders
id: no-consistent-generational-improvement-llm-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: jerin-george-mathew-2026
    resource: "https://doi.org/10.48550/arxiv.2603.23714"
    title: "Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)"
    author: Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Newer LLM generations do not consistently agree better with human essay graders

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Improvements in general language modeling capability do not necessarily translate into better agreement with human essay grading across datasets; GPT-4 achieved the lowest MAE on DREsS while GPT-5 performed better on ASAP. [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)

`q2 · i?` · `associational · r2`

Comparison of successive GPT and Llama versions across the three datasets: the GPT family showed an overall MAE reduction from GPT-3.5 to GPT-5, but intermediate versions did not follow the trend, and Llama 4 showed lower agreement than earlier versions on ASAP but higher on DREsS.

> "Improvements in general language modeling capability do not necessarily translate into better agreement with human essay grading across different datasets."

## Discussion


## Related Claims
- [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](claude3-palm2-substantial-agreement-failing-grades.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [Few-shot prompting modestly improves LLM-human score agreement, inconsistently across datasets and models](few-shot-prompting-inconsistent-grading-gains.md) — related
- [LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes](llm-fast-mode-limited-thinking-mode-better-agreement.md) — related
- [Newer LLM generations such as GPT-4 generally outperform GPT-3.5 in short-answer grading accuracy, but this advantage is not consistent across all tasks and domains](gpt4-advantage-uneven-across-tasks.md) — reports the opposite
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
