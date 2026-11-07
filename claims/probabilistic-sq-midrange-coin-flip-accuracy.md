---
type: claim
title: "Probabilistic surprise question accuracy collapses in the mid-range of the confidence spectrum (54.5% for 40%–60% answers) but reaches 89.9% at the extremes"
description: "Probabilistic surprise question accuracy collapses in the mid-range of the confidence spectrum (54.5% for 40%–60% answers) but reaches 89.9% at the extremes"
id: probabilistic-sq-midrange-coin-flip-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: kupf-irma-2024
    resource: "https://doi.org/10.1136/bmjopen-2023-081661"
    title: "Kupf Irma, Thanner Gabriele, Gerken Michael, Crispin Alexander, Braess Jan. (2024). How accurate is clinical prognostication by oncologists during routine practice in a general hospital and can it be improved by a specific prognosis training programme: a prospective interventional study. BMJ Open. https://doi.org/10.1136/bmjopen-2023-081661"
    author: Kupf Irma, Thanner Gabriele, Gerken Michael, Crispin Alexander, Braess Jan
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Probabilistic surprise question accuracy collapses in the mid-range of the confidence spectrum (54.5% for 40%–60% answers) but reaches 89.9% at the extremes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Mid-range probabilistic answers (40%–60%) were significantly less accurate (p<0.0001) than extreme answers (0%–30% and 70%–100%). [→ Kupf Irma 2024](#kupf-irma-2024)

## Evidence

### Kupf Irma 2024

Kupf Irma, Thanner Gabriele, Gerken Michael, Crispin Alexander, Braess Jan. (2024). How accurate is clinical prognostication by oncologists during routine practice in a general hospital and can it be improved by a specific prognosis training programme: a prospective interventional study. BMJ Open. https://doi.org/10.1136/bmjopen-2023-081661

`q3 · i?` · `causal · r1`

Analysis of 800 probabilistic surprise question answers collected in phase 3 of the prospective study; the article reports the mid-range versus extremes contrast with p<0.0001 and no effect size, and Brier scores of 0.193 (whole group), 0.191 (oncologists), 0.199 (residents).

> "These mid-range percentages (answers 40%–60%) only had a low accuracy of 54.5% which was significantly (p<0.0001) worse compared with the 'extreme' parts of the spectrum (0%–30% and 70%–100%) with a correct estimate in 89.9% of cases."

## Discussion


## Related Claims
- [Collective probabilistic estimates calibrated with real group survival: higher predicted survival likelihoods correlated with higher actual survival (p<0.0001)](collective-prognostic-estimates-track-group-survival.md) — related
- [Fine-tuned PLMs exhibit label compression toward mid-scale QoF scores, never predicting extreme labels 1 and 7](plm-label-compression-qof-extremes.md) — related
- [AI scoring shows a quality-conditioned pattern: strong agreement on fully correct and fully incorrect responses but substantial degradation on mid-range responses](ai-mid-range-scoring-degradation-u-shape.md) — a broader claim this one bears on
- [Mid-range degradation is conditioned on task-specific adaptation: it is most severe for few-shot LLMs with few examples, decreases with more task-specific data, and is mildest for the fine-tuned encoder](task-specific-adaptation-conditions-mid-range-degradation.md) — a broader claim this one bears on
