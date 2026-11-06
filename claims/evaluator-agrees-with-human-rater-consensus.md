---
type: claim
title: Evaluator-agent scores agreed closely with a 16-rater human consensus benchmark for both MI (ICC(2,1)=0.959) and CBT (ICC(2,1)=0.934)
description: Evaluator-agent scores agreed closely with a 16-rater human consensus benchmark for both MI (ICC(2,1)=0.959) and CBT (ICC(2,1)=0.934)
id: evaluator-agrees-with-human-rater-consensus
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kamaleddin-mohammad-amin-2026
    resource: "https://doi.org/10.2196/92964"
    title: "Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat. (2026). Multiagent Large Language Model Framework for Psychotherapy Fidelity Assessment in Motivational Interviewing and Cognitive Behavioral Therapy Training: Cross-Sectional, Simulation-Based Evaluation Study. JMIR Medical Education. https://doi.org/10.2196/92964"
    author: Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Evaluator-agent scores agreed closely with a 16-rater human consensus benchmark for both MI (ICC(2,1)=0.959) and CBT (ICC(2,1)=0.934)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Evaluator-vs-human-consensus agreement was ICC(2,1) of 0.959 for MI and 0.934 for CBT, with Pearson r of 0.969 and 0.948 respectively. [→ Kamaleddin Mohammad Amin 2026](#kamaleddin-mohammad-amin-2026)
`q2 i?` Human interrater reliability was ICC(2,1) of 0.866 for MI and 0.769 for CBT across the same session × criterion observations. [→ Kamaleddin Mohammad Amin 2026](#kamaleddin-mohammad-amin-2026)

## Evidence

### Kamaleddin Mohammad Amin 2026

Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat. (2026). Multiagent Large Language Model Framework for Psychotherapy Fidelity Assessment in Motivational Interviewing and Cognitive Behavioral Therapy Training: Cross-Sectional, Simulation-Based Evaluation Study. JMIR Medical Education. https://doi.org/10.2196/92964

`q2 · i?` · `design · r2`

Agreement analysis comparing Evaluator-agent scores with ratings from a pragmatic 16-rater human benchmark (3 physicians and 13 Prolific raters) across 90 MI and 110 CBT session × criterion observations using ICC(2,1) with percentile-bootstrap 95% CIs.

> "Evaluator-vs-human-consensus agreement was high for MI, with ICC(2,1) of 0.959 (95% CI 0.940‐0.973), Pearson r of 0.969, Spearman ρ of 0.878, mean absolute error (MAE) of 0.366, and root mean square error (RMSE) of 0.490."

## Discussion


## Related Claims
- [An automated LLM assessor rates 3E clinical communication skills with agreement comparable to individual human raters](llm-assessor-agrees-with-human-raters-3e.md) — related
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](llm-high-consensus-agreement-circularity-risk.md) — related
- [Evaluator-agent MI scores aligned with AnnoMI metadata-derived session-level quality labels, achieving 91.7% classification accuracy at a threshold of 2](evaluator-scores-align-annomi-session-labels.md) — related
- [Appending criterion-referenced feedback text to novice Student-agent prompts shifted subsequent Evaluator-assigned scores upward in both MI and CBT](feedback-prompt-augmentation-shifts-evaluator-scores.md) — related
- [The custom-made anatomical recognition score agrees strongly with the reference TTE quality score](reference-custom-tte-score-agreement.md) — related
