---
type: claim
title: Higher-adherence Student-agent prompts produced more constrained and consistent response probabilities across Patient-agent profiles
description: Higher-adherence Student-agent prompts produced more constrained and consistent response probabilities across Patient-agent profiles
id: higher-adherence-prompts-lower-response-dispersion
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kamaleddin-mohammad-amin-2026
    resource: "https://doi.org/10.2196/92964"
    title: "Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat. (2026). Multiagent Large Language Model Framework for Psychotherapy Fidelity Assessment in Motivational Interviewing and Cognitive Behavioral Therapy Training: Cross-Sectional, Simulation-Based Evaluation Study. JMIR Medical Education. https://doi.org/10.2196/92964"
    author: Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Higher-adherence Student-agent prompts produced more constrained and consistent response probabilities across Patient-agent profiles

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` For MI, the SD of session-level average token probability decreased from 4.99 percentage points (novice) to 2.46 (intermediate) to 1.74 (expert); for CBT, from 3.13 to 2.46 to 1.44. [→ Kamaleddin Mohammad Amin 2026](#kamaleddin-mohammad-amin-2026)

## Evidence

### Kamaleddin Mohammad Amin 2026

Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat. (2026). Multiagent Large Language Model Framework for Psychotherapy Fidelity Assessment in Motivational Interviewing and Cognitive Behavioral Therapy Training: Cross-Sectional, Simulation-Based Evaluation Study. JMIR Medical Education. https://doi.org/10.2196/92964

`q1 · i?` · `design · r2`

Exploratory analysis of token-level log probabilities from GPT-4.1-mini Student-agent responses, transformed to geometric mean token probability percentages. The authors state this is an indirect proxy for generative consistency and does not directly measure hallucination, clinical realism, or safety.

> "For MI, the SD decreased from 4.99 percentage points (95% CI 4.19‐5.77) for the novice profile to 2.46 (95% CI 2.19‐2.70) for the intermediate profile to 1.74 (95% CI 1.53‐1.95) for the expert profile"

## Discussion


## Related Claims
- [Evaluator-agent scores increased monotonically across prompt-defined novice, intermediate, and expert Student-agent competence levels for both MI and CBT synthetic encounters](evaluator-scores-discriminate-prompt-defined-competence-levels.md) — related
- [Appending criterion-referenced feedback text to novice Student-agent prompts shifted subsequent Evaluator-assigned scores upward in both MI and CBT](feedback-prompt-augmentation-shifts-evaluator-scores.md) — related
