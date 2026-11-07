---
type: claim
title: DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o on both question-level and case-level accuracy
description: DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o on both question-level and case-level accuracy
id: deepseek-qwen32b-outperform-gpt4o-clinical-cases
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: cha-j-2026
    resource: "https://doi.org/10.2196/95342"
    title: "Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342"
    author: Cha J, Zhao Y, Zong H.
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o on both question-level and case-level accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` DeepSeek-R1 achieved the highest case pass rate of 79.9% (151/189), significantly higher than GPT-4o (65.6%; P<.001) and Gemini-2.5-Flash (71.4%; P=.02). [→ Cha J 2026](#cha-j-2026)
`q3 i?` Qwen2.5-32B (76.2% CPR) also significantly outperformed GPT-4o (65.6%; P=.03) at the case level. [→ Cha J 2026](#cha-j-2026)

## Evidence

### Cha J 2026

Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342

`q3 · i?` · `design · r2`

Pairwise McNemar tests with Bonferroni correction compared the four main models across 189 paired cases. DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o in both QPR and CPR; differences between DeepSeek-R1 and Qwen2.5-32B were not significant.

> "At the case level, DeepSeek-R1 achieved the highest CPR of 79.9% (151/189), significantly higher than GPT-4o (124/189, 65.6%; P<.001) and Gemini-2.5-Flash (135/189, 71.4%; P=.02)."

## Discussion


## Related Claims
- [Observed case pass rates closely align with expected case pass rates computed under question independence](observed-cpr-matches-expected-independence-benchmark.md) — related
- [LLMs with high question-level accuracy on medical licensing exam cases show substantially lower case-level accuracy, with consistency gaps of 10% to 17.9%](llm-consistency-gap-question-vs-case-level.md) — related
- [The consistency gap increases with case complexity, though the 4-question subgroup contained only 7 cases](case-complexity-increases-consistency-gap.md) — related
- [Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies](llm-company-comparison-biomedical-mcq-accuracy.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [Complex Type C integrative questions distinguish models most: the Deepseek-R1 vs. ChatGPT-4o accuracy gap on Type C was nearly 25%](type-c-questions-distinguish-models.md) — related
- [GPT-4.1 achieved the highest accuracy among GPT-4.1, GPT-4o and GPT-4 on Taiwan plastic surgery board questions, but no model reached accuracy sufficient for independent clinical education use](gpt41-highest-accuracy-but-below-clinical-education-threshold.md) — related
- [Post-hoc comparisons show ChatGPT o1 performed significantly better than most other models across both question types (p < 0.0031)](chatgpt-o1-posthoc-significantly-better.md) — related
