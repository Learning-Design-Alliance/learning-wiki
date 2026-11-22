---
type: claim
title: Model rankings held on 100 self-constructed uncontaminated questions, indicating performance did not rely on web retrieval or training-data contamination
description: Model rankings held on 100 self-constructed uncontaminated questions, indicating performance did not rely on web retrieval or training-data contamination
id: self-constructed-questions-rule-out-contamination
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

# Model rankings held on 100 self-constructed uncontaminated questions, indicating performance did not rely on web retrieval or training-data contamination

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On 100 novel physician-constructed questions not retrievable online, all 7 models exceeded the passing threshold and Baichuan remained highest (87.00%), with Llama improving from 48% to 74%. [→ Yao Zhong 2025](#yao-zhong-2025)

## Evidence

### Yao Zhong 2025

Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485

`q2 · i?` · `design · r2`

Contamination-control test using 100 novel questions built by three experienced physicians to mirror CNMLE format, presented under the same prompts. The article reports Llama "rising from 48% to 74%" while other models stayed consistent, with Baichuan at 87.00% and ChatGPT at 84.00%.

> "In a set of 100 self-constructed questions, Llama's accuracy rate saw a significant improvement, rising from 48% to 74%, whereas the other models' performance remained largely consistent with their results in the CNMLE."

## Discussion


## Related Claims
- [Few-shot prompting produced minimal change in relative model rankings, with Llama showing marked improvement](few-shot-prompting-minimal-ranking-change.md) — related
- [Six of seven LLMs exceeded the CNMLE passing threshold under zero-shot settings, with Chinese-corpus model Baichuan achieving the highest accuracy (86.67%)](llm-cnmle-zero-shot-accuracy-baichuan-highest.md) — related
- [ChatGPT answered unsupervised web-based MCQ assessments with a mean accuracy of 70% (range 35–100%)](chatgpt-wba-mcq-mean-70-percent.md) — related
