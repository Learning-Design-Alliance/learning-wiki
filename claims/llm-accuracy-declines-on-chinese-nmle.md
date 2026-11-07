---
type: claim
title: "All four LLMs showed a decline in accuracy on the Chinese-language NMLE, with GPT-4, GPT-3.5 and Bard failing to reach the 70% accuracy threshold"
description: "All four LLMs showed a decline in accuracy on the Chinese-language NMLE, with GPT-4, GPT-3.5 and Bard failing to reach the 70% accuracy threshold"
id: llm-accuracy-declines-on-chinese-nmle
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: chen-yikai-2024
    resource: "https://doi.org/10.1186/s12909-024-06309-x"
    title: "Chen Yikai, Huang Xiujie, Yang Fangjie, Lin Haiming, Lin Haoyu, Zheng Zhuoqun, Liang Qifeng, Zhang Jinhai, Li Xinxin. (2024). Performance of ChatGPT and Bard on the medical licensing examinations varies across different cultures: a comparison study. BMC Medical Education. https://doi.org/10.1186/s12909-024-06309-x"
    author: Chen Yikai, Huang Xiujie, Yang Fangjie, Lin Haiming, Lin Haoyu, Zheng Zhuoqun, Liang Qifeng, Zhang Jinhai, Li Xinxin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# All four LLMs showed a decline in accuracy on the Chinese-language NMLE, with GPT-4, GPT-3.5 and Bard failing to reach the 70% accuracy threshold

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Performance dropped on the NMLE: GPT-4, GPT-3.5 and Bard scored below 70% (69.8%, 60.4%, 61.3%), and even GPT-4o scored lower (84.9%) than on the three English-based examinations. [→ Chen Yikai 2024](#chen-yikai-2024)

## Evidence

### Chen Yikai 2024

Chen Yikai, Huang Xiujie, Yang Fangjie, Lin Haiming, Lin Haoyu, Zheng Zhuoqun, Liang Qifeng, Zhang Jinhai, Li Xinxin. (2024). Performance of ChatGPT and Bard on the medical licensing examinations varies across different cultures: a comparison study. BMC Medical Education. https://doi.org/10.1186/s12909-024-06309-x

`q2 · i?` · `design · r2`

Benchmarking evaluation of the same four LLMs on 139 Chinese-language NMLE sample questions drawn from the official 2023 sample question book, scored against standard answers. Table 1 prints GPT-4o at 118/139 (84.9%), GPT-4 at 97/139 (69.8%), GPT-3.5 at 84/139 (60.4%) and Bard at 84/137 (61.3%).

> "Our research indicates that all four LLMs showed a decline in accuracy on the NMLE, with GPT-4, GPT-3.5, and Bard all failing to reach the 70% accuracy threshold."

## Discussion


## Related Claims
- [GPT-4 performed comparably to average human NMLE examinees, DeepSeek slightly exceeded them, and no tested LLM reached the top-10% human threshold](llm-nmle-performance-versus-human-examinees.md) — related
- [GPT-4 and GPT-4o accuracy exceeds the NMLE passing threshold and the typical national pass rate](gpt4-gpt4o-exceed-nmle-passing-threshold.md) — related
- [All tested LLMs exceeded the NMLE passing threshold yet stayed below 80% accuracy across all units and years](llms-pass-nmle-but-ceiling-below-80-percent.md) — related
- [GPT-4o and GPT-4 significantly outperform GPT-3.5 and Google Bard on overall accuracy across four medical licensing examinations](gpt4o-gpt4-outperform-gpt35-bard-medical-licensing-exams.md) — related
