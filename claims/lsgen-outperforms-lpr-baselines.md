---
type: claim
title: LSGEN outperforms program-repair baselines on LPR-Bench in code accuracy and bug-description F1
description: LSGEN outperforms program-repair baselines on LPR-Bench in code accuracy and bug-description F1
id: lsgen-outperforms-lpr-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhenlong-dai-2026
    resource: "https://doi.org/10.1609/aaai.v40i36.40300"
    title: "Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)"
    author: Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LSGEN outperforms program-repair baselines on LPR-Bench in code accuracy and bug-description F1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On LPR-Bench, LSGEN with iterative retrieval enhancement achieves 91.40% code accuracy on GPT-4o and 91.65% on Claude-4, exceeding the second-best baselines by 50.86% and 49.64% respectively, and achieves B-F1 of 38.46% and 38.27%. [→ Zhenlong Dai 2026](#zhenlong-dai-2026)

## Evidence

### Zhenlong Dai 2026

Zhenlong Dai, Zhuoluo Zhao, Hengning Wang, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen. (2026). Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement. [doi:10.1609/aaai.v40i36.40300](https://doi.org/10.1609/aaai.v40i36.40300)

`q2 · i?` · `design · r2`

Benchmark evaluation on LPR-Bench (Table 2) comparing LSGEN against NoRef, AdaPatcher, PAR, PyDex and PyFiXV using GPT-4o and Claude-4. LSGEN iter3 "achieves 91.40% on GPT-4o, 50.86% higher than the second-best method"; B-F1 was 38.46% on GPT-4o, 15.63% above the second-best.

> "LSGEN iter3 achieves 91.40% on GPT-4o, 50.86% higher than the second-best method, and it reaches 91.65% on Claude-4, 49.64% above the second-best method."

## Discussion


## Related Claims
- [Edit-driven solution retrieval outperforms code-similarity retrieval for program repair](edit-driven-retrieval-beats-code-retrieval.md) — related
- [Iterative Retrieval Enhancement improves repair accuracy and B-F1, with gains continuing over three iterations](iterative-retrieval-enhancement-improves-repair.md) — related
- [Each LSGEN component contributes: removing any component decreases accuracy and B-F1, with reference-inspired generation most critical for smaller models](lsgen-ablation-component-contributions.md) — related
- [GPT-4o shows a clear advantage in complex question formats, exceeding 85% accuracy on case analysis (A3/A4) and matching (B1) questions](gpt4o-advantage-complex-question-formats.md) — related
- [The automatic bug-description evaluation metric agrees strongly with human evaluators](automatic-bug-description-metric-human-agreement.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
