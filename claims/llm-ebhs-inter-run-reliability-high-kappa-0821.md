---
type: claim
title: "Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement."
description: "Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement."
id: llm-ebhs-inter-run-reliability-high-kappa-0821
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-05
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

# Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-11-05 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across five independent runs per model, inter-run reliability measured by Cohen's κ was consistently high: six of ten models were rated almost perfect (0.81–1.00), three substantial (0.61–0.80), one moderate (0.41–0.60), and the overall mean κ was 0.821 (SD 0.127; range 0.585–0.979). [→ Güler Ibrahim 2026](#guler-ibrahim-2026)

## Evidence

### Güler Ibrahim 2026

Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305

`q2 · i?` · `design · r2`

Reliability analysis of five independent runs per model (Table 2, Figures 2 and 3): for each model, all pairwise κ values across the five runs were calculated (10 combinations per model, 100 coefficients in total), with the mean κ per model summarizing overall inter-run reliability; the printed mean κ (SD; range) was 0.821 (0.127; 0.585–0.979).

> "Inter-run reliability was consistently high across the evaluated systems. Most models demonstrated agreement levels consistent with the upper interpretive categories, indicating that repeated evaluations under identical conditions produced stable, reproducible outputs."

## Discussion


## Related Claims
- [Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.](llm-ebhs-exam-accuracy-range-72-85-percent.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- [A small subset of EBHS examination questions produced incorrect responses across most or all LLMs, concentrated in specialized domains including rare congenital anomalies, European-specific practice patterns, historical terminology and eponyms, and complex reconstructions.](llm-ebhs-persistent-subspecialty-knowledge-gaps.md) — related
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
- [Current-generation LLMs achieve 86% to 94% mean success rates on European anesthesiology examination questions, exceeding the EDAIC part I passing threshold](llm-success-rates-86-94-percent-anesthesiology-exams.md) — related
- [Multiagent framework demonstrated stable cross-specialty scalability with lower variability than single-LLM baseline](multiagent-stable-cross-specialty-scalability.md) — related
- [Substantial within-model output instability was identified, most notably GPT-5.2 in female urology (SD ±22.8%) and anatomy (SD ±14.2%)](llm-output-instability-female-urology-anatomy.md) — reports the opposite
