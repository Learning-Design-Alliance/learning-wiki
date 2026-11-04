---
type: claim
title: "Pairwise comparisons with Bonferroni-corrected McNemar's tests identified statistically significant differences favouring the highest-performing proprietary systems, most notably GPT-5 Pro over five lower-ranked models."
description: "Pairwise comparisons with Bonferroni-corrected McNemar's tests identified statistically significant differences favouring the highest-performing proprietary systems, most notably GPT-5 Pro over five lower-ranked models."
id: mcnemar-pairwise-llm-ebhs-significant-differences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: güler-ibrahim-2026
    resource: "https://doi.org/10.1177/17531934261436305"
    title: "Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305"
    author: Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Pairwise comparisons with Bonferroni-corrected McNemar's tests identified statistically significant differences favouring the highest-performing proprietary systems, most notably GPT-5 Pro over five lower-ranked models.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Of the 45 pairwise model comparisons (α = 0.0011 after Bonferroni correction), a limited number were statistically significant, most favouring the highest-performing proprietary systems: GPT-5 Pro significantly outperformed Qwen3 Max (OR 3.82), Mistral Medium 3.1 (OR 2.89), Falcon H1 (OR 3.85), Llama 3.3 (OR 4.4) and ERNIE 4.5 Turbo (OR 4.08), and Gemini 2.5 Pro significantly outperformed Falcon H1 (OR 2.71), Llama 3.3 (OR 2.62) and ERNIE 4.5 Turbo (OR 2.53). [→ Güler Ibrahim 2026](#guler-ibrahim-2026)

## Evidence

### Güler Ibrahim 2026

Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305

`q2 · i?` · `design · r2`

McNemar's test compared paired responses across the 300 items for each model pair, with a significance threshold of α = 0.0011 controlling the family-wise error rate after Bonferroni correction for the 45 pairwise comparisons; effect sizes were reported as odds ratios with 95% confidence intervals (Table 3).

> "Pairwise comparisons identified a limited number of statistically significant differences, most of which favoured the highest-performing proprietary systems. Overall, these comparisons reflect a stable ranking structure among models, even though the absolute gaps between systems were moderate and do not limit the potential educational use of several mid-tier architectures."

## Discussion


## Related Claims
- [Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.](llm-ebhs-exam-accuracy-range-72-85-percent.md) — related
- [A small subset of EBHS examination questions produced incorrect responses across most or all LLMs, concentrated in specialized domains including rare congenital anomalies, European-specific practice patterns, historical terminology and eponyms, and complex reconstructions.](llm-ebhs-persistent-subspecialty-knowledge-gaps.md) — related
- [Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy.](proprietary-llms-outperform-open-source-ebhs.md) — related
