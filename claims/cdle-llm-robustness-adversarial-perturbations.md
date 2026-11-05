---
type: claim
title: All five LLMs show only slight, non-significant accuracy declines under semantic-equivalence and irrelevant-information perturbations, indicating strong robustness
description: All five LLMs show only slight, non-significant accuracy declines under semantic-equivalence and irrelevant-information perturbations, indicating strong robustness
id: cdle-llm-robustness-adversarial-perturbations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhang-jiarui-2025
    resource: "https://doi.org/10.1186/s12903-025-07540-8"
    title: "Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting. (2025). From accuracy to robustness: a comparative study of five advanced large language models on the Chinese dental licensing examination. BMC Oral Health. https://doi.org/10.1186/s12903-025-07540-8"
    author: Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# All five LLMs show only slight, non-significant accuracy declines under semantic-equivalence and irrelevant-information perturbations, indicating strong robustness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Accuracy declined by 2.5%–5% in the semantic equivalence test and by 1.66%–5.84% when irrelevant redundant information was injected, with no significant drop under either perturbation (p > 0.05, McNemar's test). [→ Zhang Jiarui 2025](#zhang-jiarui-2025)

## Evidence

### Zhang Jiarui 2025

Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting. (2025). From accuracy to robustness: a comparative study of five advanced large language models on the Chinese dental licensing examination. BMC Oral Health. https://doi.org/10.1186/s12903-025-07540-8

`q3 · i?` · `causal · r2`

Adversarial testing of 120 of the 600 questions, rewritten by Claude Sonnet 4 under two perturbation strategies (synonym/colloquial substitution; injection of unrelated distracting information), compared against original-item accuracy with McNemar's test. The article reports "an accuracy drop ranging from 1.66% to 5.84%" and no significant drop (p > 0.05).

> "When irrelevant and redundant information was injected, the five LLMs showed an accuracy drop ranging from 1.66% to 5.84%. No significant accuracy drop was observed among the five LLMs under either perturbation relative to the original items (p > 0.05)."

## Discussion


## Related Claims
- [On MedQA, GPT-5.4-mini's accuracy increases monotonically with prompt sophistication across semantically equivalent questions, with generated Low Literacy prompt variants scoring significantly below Prompt Engineer variants](prompt-privilege-monotonic-accuracy-gap-medqa.md) — reports the opposite
- [DysLexLens is moderately robust to paraphrased queries (Answer Relevancy 0.58) but sensitive to keyword-perturbed queries (0.34)](query-robustness-paraphrase-keyword-perturbation.md) — related
