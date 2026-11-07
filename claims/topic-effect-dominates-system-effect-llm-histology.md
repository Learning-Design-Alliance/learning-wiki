---
type: claim
title: Histology topic, not LLM platform, was the primary factor in performance variance (η2 = 0.452 vs 0.006), with a significant system-by-topic interaction
description: Histology topic, not LLM platform, was the primary factor in performance variance (η2 = 0.452 vs 0.006), with a significant system-by-topic interaction
id: topic-effect-dominates-system-effect-llm-histology
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: mavrych-volodymyr-2025
    resource: "https://doi.org/10.1080/10872981.2025.2534065"
    title: "Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065"
    author: Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena
    q: 2
    i: 0
    kind: design
    rigour: 2
  - id: mavrych-volodymyr-2025-2
    resource: "https://doi.org/10.1080/10872981.2025.2534065"
    title: "Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065"
    author: Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Histology topic, not LLM platform, was the primary factor in performance variance (η2 = 0.452 vs 0.006), with a significant system-by-topic interaction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i0`–`i3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i0` In the two-way mixed ANOVA, the system main effect was negligible (η2 = 0.006) while the topic main effect (η2 = 0.452) was large, with topic difficulty accounting for approximately 45.2% of performance variance. [→ Mavrych Volodymyr 2025](#mavrych-volodymyr-2025)
`q2 i3` The system-by-topic interaction was significant (F(76,1520) = 8.94, p < 0.001, η2 = 0.147), indicating differential performance patterns across topics. [→ Mavrych Volodymyr 2025 (2)](#mavrych-volodymyr-2025-2)

## Evidence

### Mavrych Volodymyr 2025

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i0` · `design · r2`

Two-way mixed ANOVA of accuracy across LLM systems and histology topics. The article reports "significant main effects for both LLM systems (F(4,95) = 138.42, p < 0.001, η2 = 0.006) and topic (F(19,380) = 42.86, p < 0.001, η2 = 0.452)"; the system-level η2 = 0.006 is a negligible effect (i = 0), while topic difficulty accounted for approximately 45.2% of total variance.

> "significant main effects for both LLM systems (F(4,95) = 138.42, p < 0.001, η2 = 0.006) and topic (F(19,380) = 42.86, p < 0.001, η2 = 0.452)"

### Mavrych Volodymyr 2025 (2)

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i3` · `design · r2`

The same two-way mixed ANOVA of LLM accuracy across systems and topics found "a significant interaction between system and topic (F(76,1520) = 8.94, p < 0.001, η2 = 0.147)".

> "as well as a significant interaction between system and topic (F(76,1520) = 8.94, p < 0.001, η2 = 0.147)"

## Discussion


## Related Claims
- [LLM accuracy varied sharply by histology topic: perfect in foundational areas and lowest in Muscle (76.0%)](histology-topic-difficulty-llm-performance.md) — a narrower finding that bears on this claim
- [Five LLMs showed comparable, exceptionally high accuracy (collective mean 91.1%) on text-based medical histology MCQs](llm-mean-accuracy-91-1-histology-mcqs.md) — related
- [Across all questions, final performance showed a main effect of learning condition and a large main effect of question type, with only a trend toward an interaction](omnibus-anova-condition-question-type-latimier.md) — related
- [Question type significantly affects LLM accuracy on Chinese medical licensing exam questions, with Type A basic-knowledge items answered better than Type B and Type C items](question-type-effect-llm-chinese-medical-licensing.md) — related
- [LLM accuracy varied significantly across oncology topics, with the lowest performance in colorectal tumors (mean 48.3%) and genitourinary tumors (mean 50.8%)](llm-accuracy-varies-across-oncology-topics.md) — related
