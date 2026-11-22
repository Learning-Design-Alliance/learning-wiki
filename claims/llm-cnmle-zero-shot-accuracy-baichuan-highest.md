---
type: claim
title: "Six of seven LLMs exceeded the CNMLE passing threshold under zero-shot settings, with Chinese-corpus model Baichuan achieving the highest accuracy (86.67%)"
description: "Six of seven LLMs exceeded the CNMLE passing threshold under zero-shot settings, with Chinese-corpus model Baichuan achieving the highest accuracy (86.67%)"
id: llm-cnmle-zero-shot-accuracy-baichuan-highest
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yao-zhong-2025
    resource: "https://doi.org/10.2196/69485"
    title: "Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485"
    author: Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Six of seven LLMs exceeded the CNMLE passing threshold under zero-shot settings, with Chinese-corpus model Baichuan achieving the highest accuracy (86.67%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under zero-shot settings, 6 of 7 tested LLMs surpassed the 60% passing threshold on the 2023 CNMLE, with Baichuan highest at 86.67% and ChatGPT second at 83.83%, while Llama scored 48.00%. [→ Yao Zhong 2025](#yao-zhong-2025)

## Evidence

### Yao Zhong 2025

Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485

`q2 · i?` · `design · r2`

Benchmark test of 7 LLMs on all 600 multiple-choice questions from the 2023 CNMLE under zero-shot settings with default parameters, scored against official answers. The article reports "Baichuan (86.67%), ChatGPT (83.83%)" and Llama at 48.00%, with a passing score defined as above 60%.

> "Figure 1A illustrated the accuracy rates of 7 LLMs in the CNMLE, ranked from highest to lowest: Baichuan (86.67%), ChatGPT (83.83%), ERNIE Bot (80.83%), ChatGLM (79.33%), Kimi (76.33%), Yi-large (69.00%), and Llama (48.00%)."

## Discussion


## Related Claims
- [Few-shot prompting produced minimal change in relative model rankings, with Llama showing marked improvement](few-shot-prompting-minimal-ranking-change.md) — related
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
- [Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.](llm-ebhs-exam-accuracy-range-72-85-percent.md) — related
- [Model rankings held on 100 self-constructed uncontaminated questions, indicating performance did not rely on web retrieval or training-data contamination](self-constructed-questions-rule-out-contamination.md) — related
- [GPT-4 achieves the highest pooled accuracy among LLMs (81%), significantly outperforming GPT-3.5 (60%)](gpt4-highest-accuracy-81-outperforms-gpt35.md) — related
- [All tested LLMs exceeded the NMLE passing threshold yet stayed below 80% accuracy across all units and years](llms-pass-nmle-but-ceiling-below-80-percent.md) — related
- [GPT-4 and GPT-4o accuracy exceeds the NMLE passing threshold and the typical national pass rate](gpt4-gpt4o-exceed-nmle-passing-threshold.md) — related
- [Performance gaps between English- and Chinese-trained LLMs are attributed to training-data composition rather than language communication barriers](training-data-composition-not-language-barriers.md) — related
