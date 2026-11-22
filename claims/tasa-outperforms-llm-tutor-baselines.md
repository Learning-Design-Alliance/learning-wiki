---
type: claim
title: TASA outperforms state-of-the-art LLM tutoring baselines in normalized learning gain and response personalization across four mathematics benchmarks
description: TASA outperforms state-of-the-art LLM tutoring baselines in normalized learning gain and response personalization across four mathematics benchmarks
id: tasa-outperforms-llm-tutor-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yang-wu-2025
    resource: "https://doi.org/10.48550/arXiv.2511.15163"
    title: "Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu. (2025). Teaching According to Students’ Aptitude: Personalized Mathematics Tutoring via Persona-, Memory-, and Forgetting-Aware LLMs. arXiv. [doi:10.48550/arXiv.2511.15163](https://doi.org/10.48550/arXiv.2511.15163)"
    author: Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# TASA outperforms state-of-the-art LLM tutoring baselines in normalized learning gain and response personalization across four mathematics benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across four math benchmarks and three LLM backbones, TASA improves average normalized learning gain by 11.4% and Win Rate by 19.7% over the strongest baseline TutorLLM. [→ Yang Wu 2025](#yang-wu-2025)

## Evidence

### Yang Wu 2025

Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu. (2025). Teaching According to Students’ Aptitude: Personalized Mathematics Tutoring via Persona-, Memory-, and Forgetting-Aware LLMs. arXiv. [doi:10.48550/arXiv.2511.15163](https://doi.org/10.48550/arXiv.2511.15163)

`q2 · i?` · `design · r2`

Main results comparison (Table 1) across Assist2017, NIPS34, Algebra2005, and Bridge2006 with three LLM backbones, reporting mean over random runs. The article reports TASA "improves the average∆−NLGby 11.4%" and Win Rate by 19.7% versus TutorLLM; no standardized effect size is printed.

> "Compared with the strongest baseline TutorLLM, TASA improves the average∆−NLGby 11.4% and the Win Rate by 19.7%, showing the benefit of jointly modeling persona, memory, and forgetting dynamics."

## Discussion


## Related Claims
- [Removing any of TASA's three modules degrades performance, with the forgetting score contributing an average 6.8% drop in normalized learning gain when eliminated](tasa-ablation-module-importance.md) — related
- [Instantiating TASA with DKT as the knowledge tracing model yields the highest average learning gain among five KT variants](dkt-best-kt-backbone-for-tasa.md) — related
- [DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench](deeptutor-improves-interactive-tutoring-quality-10-76.md) — related
- [TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor](tactutor-no-degradation-external-benchmarks.md) — related
- [ToST improves guidance success rates by an average of 11% over educational LLM baselines across four math benchmarks](tost-improves-guidance-success-11-percent.md) — related
