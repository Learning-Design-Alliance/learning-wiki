---
type: claim
title: "Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold."
description: "Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold."
id: llm-ebhs-exam-accuracy-range-72-85-percent
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

# Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Mean accuracy across the 10 evaluated LLMs ranged from 72% to 85%, corresponding to EBHS scores between 131 and 211 points, and seven of the 10 models reached or exceeded the illustrative pass threshold of 75% accuracy (150 of 300 points). [→ Güler Ibrahim 2026](#guler-ibrahim-2026)

## Evidence

### Güler Ibrahim 2026

Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305

`q2 · i?` · `design · r2`

Cross-sectional evaluation of 10 LLMs on the complete 300-item EBHS written examination, five independent runs per model via standardized zero-shot prompting through public web interfaces, yielding 15,000 answers scored against the official answer key. The abstract reports the accuracy range and pass-threshold counts verbatim.

> "Mean accuracy across the LLMs ranged from 72 to 85%, corresponding to total European Board of Hand Surgery scores between 131 and 211 points. Seven of the 10 LLMs reached or exceeded the illustrative pass threshold of 75%, equivalent to 150 of 300 points."

## Discussion


## Related Claims
- [Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy.](proprietary-llms-outperform-open-source-ebhs.md) — related
- [A small subset of EBHS examination questions produced incorrect responses across most or all LLMs, concentrated in specialized domains including rare congenital anomalies, European-specific practice patterns, historical terminology and eponyms, and complex reconstructions.](llm-ebhs-persistent-subspecialty-knowledge-gaps.md) — related
- [Pairwise comparisons with Bonferroni-corrected McNemar's tests identified statistically significant differences favouring the highest-performing proprietary systems, most notably GPT-5 Pro over five lower-ranked models.](mcnemar-pairwise-llm-ebhs-significant-differences.md) — related
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](llm-ebhs-inter-run-reliability-high-kappa-0821.md) — related
- [GPT-4 achieves the highest pooled accuracy among LLMs (81%), significantly outperforming GPT-3.5 (60%)](gpt4-highest-accuracy-81-outperforms-gpt35.md) — related
- [GPT-4 exceeds pass marks on India NEET-PG and UK PLAB 1 but falls below pass on clinical reasoning and procedural items](gpt4-neetpg-plab-pass-clinical-reasoning-below.md) — related
- [LLMs, particularly GPT-4, can match or exceed medical students' examination performance](llms-match-or-exceed-medical-students-exam-performance.md) — related
- [ChatGPT-4 achieved an overall accuracy of 81% on the Polish PES orthopedics exam, exceeding the 75% passing threshold on average](chatgpt-4-81-percent-accuracy-pes-orthopedics.md) — related
- [Current-generation LLMs achieve 86% to 94% mean success rates on European anesthesiology examination questions, exceeding the EDAIC part I passing threshold](llm-success-rates-86-94-percent-anesthesiology-exams.md) — related
