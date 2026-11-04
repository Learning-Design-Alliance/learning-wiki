---
type: claim
title: Angoff estimates correlated with observed item difficulty more strongly for LLMs than for faculty judges
description: Angoff estimates correlated with observed item difficulty more strongly for LLMs than for faculty judges
id: llm-angoff-item-difficulty-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: salah-eldin-kassab-shadan-mariam-ziganshina-arina-khanday-shifan-hamdy-hossam-2026
    resource: "https://doi.org/10.2196/98766"
    title: "Salah Eldin Kassab; Shadan Mariam; Ziganshina Arina; Khanday Shifan; Hamdy Hossam. (2026). AI-Assisted Angoff Standard Setting for Multiple-Choice Examinations in Medical Education: Comparative Study. JMIR Medical Education. https://doi.org/10.2196/98766"
    author: Salah Eldin Kassab; Shadan Mariam; Ziganshina Arina; Khanday Shifan; Hamdy Hossam
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Angoff estimates correlated with observed item difficulty more strongly for LLMs than for faculty judges

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Pearson correlation between Angoff estimates and item P values was r=0.552 for LLMs versus r=0.437 for faculty judges. [→ Salah Eldin Kassab; Shadan Mariam; Ziganshina Arina; Khanday Shifan; Hamdy Hossam 2026](#salah-eldin-kassab-shadan-mariam-ziganshina-arina-khanday-shifan-hamdy-hossam-2026)

## Evidence

### Salah Eldin Kassab; Shadan Mariam; Ziganshina Arina; Khanday Shifan; Hamdy Hossam 2026

Salah Eldin Kassab; Shadan Mariam; Ziganshina Arina; Khanday Shifan; Hamdy Hossam. (2026). AI-Assisted Angoff Standard Setting for Multiple-Choice Examinations in Medical Education: Comparative Study. JMIR Medical Education. https://doi.org/10.2196/98766

`q2 · i3` · `design · r2`

Pearson correlation analysis relating mean Angoff estimates to observed item difficulty (item P values) from the same examination administration; the LLM correlation was r=0.552 and the faculty correlation r=0.437, both statistically significant and positive.

> "The correlation was moderate for LLMs (r=0.552; P<.001) and weaker for faculty judges (r=0.437; P<.001). Because the difference between these dependent correlations was not formally tested, these coefficients are presented descriptively rather than as evidence that one correlation was statistically greater than the other."

## Discussion


## Related Claims
- [LLM-generated modified Angoff cutoff estimates are comparable to faculty-generated estimates for a medical MCQ examination](llm-angoff-estimates-comparable-to-faculty.md) — related
- [A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines](llm-simulated-respondents-predict-item-difficulty-above-regression-baselines.md) — related
- [Zero-shot GPT-4o difficulty ratings, rescaled and entered in grade-specific regressions, beat a grade-level dummy regressor and correlate strongly with true Rasch difficulties overall, for K-5 math and reading items](direct-llm-estimation-beats-dummy-regressor-k5-items.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
