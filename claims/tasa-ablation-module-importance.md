---
type: claim
title: "Removing any of TASA's three modules degrades performance, with the forgetting score contributing an average 6.8% drop in normalized learning gain when eliminated"
description: "Removing any of TASA's three modules degrades performance, with the forgetting score contributing an average 6.8% drop in normalized learning gain when eliminated"
id: tasa-ablation-module-importance
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
    kind: causal
    rigour: 1
---

# Removing any of TASA's three modules degrades performance, with the forgetting score contributing an average 6.8% drop in normalized learning gain when eliminated

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Ablating the forgetting score, persona, or memory each substantially lowers Δ-NLG and Win Rate, with average drops of 6.8%, 11.5%, and 4.9% respectively. [→ Yang Wu 2025](#yang-wu-2025)

## Evidence

### Yang Wu 2025

Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu. (2025). Teaching According to Students’ Aptitude: Personalized Mathematics Tutoring via Persona-, Memory-, and Forgetting-Aware LLMs. arXiv. [doi:10.48550/arXiv.2511.15163](https://doi.org/10.48550/arXiv.2511.15163)

`q2 · i?` · `causal · r1`

Ablation study (Table 2) on the Assist2017 dataset with the Llama3.1-8B-Instruct backbone, removing one component at a time. The article reports the forgetting-score ablation causes "an average drop of 6.8% in∆-NLG"; persona and memory removals decrease performance by 11.5% and 4.9% on average. No standardized effect size is printed.

> "Specifically, eliminating the forgetting score re- sults in an average drop of 6.8% in∆-NLG, confirm- ing that temporal retention modeling is crucial for adap- tive instruction."

## Discussion


## Related Claims
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Removing real-time adjustment or personalized recommendations lowers engagement and retention in ablations](ablation-realtime-personalization-components.md) — related
- [TASA outperforms state-of-the-art LLM tutoring baselines in normalized learning gain and response personalization across four mathematics benchmarks](tasa-outperforms-llm-tutor-baselines.md) — related
