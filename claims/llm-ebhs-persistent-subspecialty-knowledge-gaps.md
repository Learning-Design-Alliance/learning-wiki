---
type: claim
title: A small subset of EBHS examination questions produced incorrect responses across most or all LLMs, concentrated in specialized domains including rare congenital anomalies, European-specific practice patterns, historical terminology and eponyms, and complex reconstructions.
description: A small subset of EBHS examination questions produced incorrect responses across most or all LLMs, concentrated in specialized domains including rare congenital anomalies, European-specific practice patterns, historic...
id: llm-ebhs-persistent-subspecialty-knowledge-gaps
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

# A small subset of EBHS examination questions produced incorrect responses across most or all LLMs, concentrated in specialized domains including rare congenital anomalies, European-specific practice patterns, historical terminology and eponyms, and complex reconstructions.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A small subset of questions consistently produced incorrect responses across most or all models, suggesting persistent knowledge gaps shared among architectures; these challenging items frequently involved European-specific practice patterns differing from North American conventions, historical terminology and eponyms, or detailed numerical data from specialized surgical techniques. [→ Güler Ibrahim 2026](#guler-ibrahim-2026)

## Evidence

### Güler Ibrahim 2026

Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305

`q2 · i?` · `design · r2`

Question difficulty analysis of aggregated model performance across the 300 EBHS statements: hard items were concentrated in specialized domains including rare congenital anomalies, controversial management strategies, subtle biomechanical principles and questions requiring integration of multiple knowledge domains.

> "A small subset of questions consistently produced incorrect responses across most or all models, suggesting persistent knowledge gaps shared among architectures. These challenging items frequently involved European-specific practice patterns differing from North American conventions, historical terminology and eponyms, or detailed numerical data from specialized surgical techniques."

## Discussion


## Related Claims
- [Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.](llm-ebhs-exam-accuracy-range-72-85-percent.md) — related
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](llm-ebhs-inter-run-reliability-high-kappa-0821.md) — related
- [Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy.](proprietary-llms-outperform-open-source-ebhs.md) — related
- [Pairwise comparisons with Bonferroni-corrected McNemar's tests identified statistically significant differences favouring the highest-performing proprietary systems, most notably GPT-5 Pro over five lower-ranked models.](mcnemar-pairwise-llm-ebhs-significant-differences.md) — related
- [No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model](no-consistent-fp-fn-pattern.md) — related
