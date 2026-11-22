---
type: claim
title: Few-shot prompting produced minimal change in relative model rankings, with Llama showing marked improvement
description: Few-shot prompting produced minimal change in relative model rankings, with Llama showing marked improvement
id: few-shot-prompting-minimal-ranking-change
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
    kind: causal
    rigour: 1
---

# Few-shot prompting produced minimal change in relative model rankings, with Llama showing marked improvement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under a few-shot protocol with 3 demonstration examples per task, relative rankings stayed largely consistent, with Baichuan (84.50%) and ChatGLM (84.50%) highest, and Llama improved significantly. [→ Yao Zhong 2025](#yao-zhong-2025)

## Evidence

### Yao Zhong 2025

Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485

`q2 · i?` · `causal · r1`

Replication of the full CNMLE test under a few-shot learning protocol with 3 demonstration examples per task, run to control for prompt-engineering confounds. The article reports the printed accuracies and concludes "the prompt engineering has minimal influence on the relative performance among models."

> "Baichuan (84.50%) demonstrated the highest accuracy rate, followed by ChatGLM (84.50%) and ChatGPT (81.83%). Notably, Llama exhibited a significant improvement in accuracy rate after prompt engineering modifications"

## Discussion


## Related Claims
- [Model rankings held on 100 self-constructed uncontaminated questions, indicating performance did not rely on web retrieval or training-data contamination](self-constructed-questions-rule-out-contamination.md) — related
- [Six of seven LLMs exceeded the CNMLE passing threshold under zero-shot settings, with Chinese-corpus model Baichuan achieving the highest accuracy (86.67%)](llm-cnmle-zero-shot-accuracy-baichuan-highest.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
