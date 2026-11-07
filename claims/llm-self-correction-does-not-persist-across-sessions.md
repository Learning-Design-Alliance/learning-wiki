---
type: claim
title: LLMs can self-correct errors within a single session but revert to the original incorrect responses when the same questions are re-entered in a new session
description: LLMs can self-correct errors within a single session but revert to the original incorrect responses when the same questions are re-entered in a new session
id: llm-self-correction-does-not-persist-across-sessions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: chen-yikai-2024
    resource: "https://doi.org/10.1186/s12909-024-06309-x"
    title: "Chen Yikai, Huang Xiujie, Yang Fangjie, Lin Haiming, Lin Haoyu, Zheng Zhuoqun, Liang Qifeng, Zhang Jinhai, Li Xinxin. (2024). Performance of ChatGPT and Bard on the medical licensing examinations varies across different cultures: a comparison study. BMC Medical Education. https://doi.org/10.1186/s12909-024-06309-x"
    author: Chen Yikai, Huang Xiujie, Yang Fangjie, Lin Haiming, Lin Haoyu, Zheng Zhuoqun, Liang Qifeng, Zhang Jinhai, Li Xinxin
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# LLMs can self-correct errors within a single session but revert to the original incorrect responses when the same questions are re-entered in a new session

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` When researchers corrected incorrect responses within a session, models changed their answers, but re-entering the same questions in a new session produced the original incorrect responses again. [→ Chen Yikai 2024](#chen-yikai-2024)

## Evidence

### Chen Yikai 2024

Chen Yikai, Huang Xiujie, Yang Fangjie, Lin Haiming, Lin Haoyu, Zheng Zhuoqun, Liang Qifeng, Zhang Jinhai, Li Xinxin. (2024). Performance of ChatGPT and Bard on the medical licensing examinations varies across different cultures: a comparison study. BMC Medical Education. https://doi.org/10.1186/s12909-024-06309-x

`q1 · i?` · `design · r2`

An exploratory experiment in which the researchers corrected three LLMs' incorrect responses, observed within-session changes, and then re-tested the same questions in new sessions. No sample size or effect size is printed; the article reports that models "still reverted to the original incorrect responses".

> "However, when we initiated a new session and re-entered the same questions, these models still reverted to the original incorrect responses."

## Discussion


## Related Claims
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
