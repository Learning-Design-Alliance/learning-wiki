---
type: claim
title: "Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy."
description: "Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy."
id: proprietary-llms-outperform-open-source-ebhs
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

# Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Proprietary systems (GPT-5 Pro, Claude Sonnet 4.5, Gemini 2.5 Pro, Grok-4, ERNIE 4.5 Turbo) showed consistently higher mean accuracy than open-source systems (DeepSeek V3.2, Qwen3 Max, Mistral Medium 3.1, Llama 3.3, Falcon H1), with GPT-5 Pro achieving 85% accuracy (95% CI 84–86%). [→ Güler Ibrahim 2026](#guler-ibrahim-2026)

## Evidence

### Güler Ibrahim 2026

Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305

`q2 · i?` · `design · r2`

Results of the multi-model EBHS evaluation (Table 1, Figure 1): GPT-5 Pro ranked first with 211 EBHS points, followed by Gemini 2.5 Pro (196) and Grok-4 (188), while the authors note "individual exceptions were observed" to the general proprietary-over-open-source pattern.

> "Proprietary systems showed consistently higher mean accuracy than open-source systems. The highest-performing LLM (GPT-5 Pro) achieved 85% accuracy with a 95% confidence interval of 84 to 86% and a mean inter-run reliability measured by Cohen’s κ of 0.739."

## Discussion


## Related Claims
- [Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.](llm-ebhs-exam-accuracy-range-72-85-percent.md) — related
- [A small subset of EBHS examination questions produced incorrect responses across most or all LLMs, concentrated in specialized domains including rare congenital anomalies, European-specific practice patterns, historical terminology and eponyms, and complex reconstructions.](llm-ebhs-persistent-subspecialty-knowledge-gaps.md) — related
- [Pairwise comparisons with Bonferroni-corrected McNemar's tests identified statistically significant differences favouring the highest-performing proprietary systems, most notably GPT-5 Pro over five lower-ranked models.](mcnemar-pairwise-llm-ebhs-significant-differences.md) — related
- [Gemini 2.5 Pro significantly outperformed GPT-5 on EDAIC questions as the only significant pairwise difference after Holm correction](gemini-outperformed-gpt5-edaic-pairwise.md) — related
- [Current-generation LLMs achieve 86% to 94% mean success rates on European anesthesiology examination questions, exceeding the EDAIC part I passing threshold](llm-success-rates-86-94-percent-anesthesiology-exams.md) — related
- [Gemini 2.5 Pro achieved the highest accuracy (92.44%) on pediatric dentistry DUS questions, significantly outperforming most other LLMs](gemini-2-5-pro-highest-accuracy-pediatric-dus.md) — related
