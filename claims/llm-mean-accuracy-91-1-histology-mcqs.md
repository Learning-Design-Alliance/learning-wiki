---
type: claim
title: "Five LLMs showed comparable, exceptionally high accuracy (collective mean 91.1%) on text-based medical histology MCQs"
description: "Five LLMs showed comparable, exceptionally high accuracy (collective mean 91.1%) on text-based medical histology MCQs"
id: llm-mean-accuracy-91-1-histology-mcqs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mavrych-volodymyr-2025
    resource: "https://doi.org/10.1080/10872981.2025.2534065"
    title: "Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065"
    author: Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: mavrych-volodymyr-2025-2
    resource: "https://doi.org/10.1080/10872981.2025.2534065"
    title: "Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065"
    author: Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: mavrych-volodymyr-2025-3
    resource: "https://doi.org/10.1080/10872981.2025.2534065"
    title: "Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065"
    author: Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena
    q: 2
    i: 0
    kind: design
    rigour: 2
---

# Five LLMs showed comparable, exceptionally high accuracy (collective mean 91.1%) on text-based medical histology MCQs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2` · `i0` negligible
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across three testing attempts, the five LLMs achieved a collective mean accuracy of 91.1% (SD = 7.2) on 200 text-based histology MCQs. [→ Mavrych Volodymyr 2025](#mavrych-volodymyr-2025)
`q2 i?` Differences in accuracy between the five systems were not statistically significant, indicating comparable capabilities. [→ Mavrych Volodymyr 2025 (2)](#mavrych-volodymyr-2025-2)
`q2 i0` Only 0.6% of the total variance in performance was attributable to differences between LLM systems (Cohen's f = 0.079, η2 = 0.006). [→ Mavrych Volodymyr 2025 (3)](#mavrych-volodymyr-2025-3)

## Evidence

### Mavrych Volodymyr 2025

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i?` · `design · r2`

Performance analysis of the cross-sectional comparative evaluation, in which five LLMs answered the same 200 MCQs in three sessions. The article reports "a collective mean accuracy of 91.1% (SD = 7.2)" across GPT-4.1, Claude 3.7 Sonnet, Gemini 2.0 Flash, Copilot, and DeepSeek R1.

> "The selected LLMs demonstrated remarkably high proficiency levels in answering medical histology questions, with a collective mean accuracy of 91.1% (SD = 7.2)."

### Mavrych Volodymyr 2025 (2)

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i?` · `design · r2`

One-way ANOVA with post-hoc Tukey's HSD tests compared accuracy across the five systems in the performance analysis. The article reports the differences were "not statistically significant (p > 0.05)"; equivalence was not formally tested.

> "The differences in performance between these systems were not statistically significant (p > 0.05), indicating comparable capabilities across all the tested LLMs in histology knowledge."

### Mavrych Volodymyr 2025 (3)

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i0` · `design · r2`

Post-hoc power analysis of the between-system comparison. The article reports "a Cohen's f of 0.079 and eta-squared (η2) of 0.006", a negligible system-level effect (η2 = 0.006, below the d = 0.2 equivalent range), with achieved power of 95.0%.

> "The effect size analysis indicated a Cohen's f of 0.079 and eta-squared (η2) of 0.006, suggesting that only 0.6% of the total variance in performance was attributable to differences between LLM systems."

## Discussion


## Related Claims
- [LLM accuracy varied sharply by histology topic: perfect in foundational areas and lowest in Muscle (76.0%)](histology-topic-difficulty-llm-performance.md) — related
- [The authors report LLM histology accuracy (91.1% average) exceeded averages reported for other basic medical sciences (neuroscience 67.2%, anatomy 41.5%, embryology 78.7%, biochemistry 81.1%)](llm-histology-accuracy-exceeds-other-basic-sciences.md) — related
- [Test-retest reliability of LLM answers to histology MCQs ranged from moderate (Gemini, DeepSeek) to excellent (Claude)](llm-test-retest-reliability-varies-histology.md) — related
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — related
- [ChatGPT-4 achieved the highest accuracy of the five tested AI models on standardised dental MCQs, at 91.3% in both testing sessions](chatgpt-4-highest-accuracy-dental-mcqs-91-3.md) — related
- [LLM accuracy on multilingual medical multiple-choice questions varies substantially by model, with Claude-Sonnet-3.7 highest (87%) and open models lowest (64%-73%)](llm-accuracy-varies-by-model-medical-mcq.md) — related
- [Histology topic, not LLM platform, was the primary factor in performance variance (η2 = 0.452 vs 0.006), with a significant system-by-topic interaction](topic-effect-dominates-system-effect-llm-histology.md) — related
