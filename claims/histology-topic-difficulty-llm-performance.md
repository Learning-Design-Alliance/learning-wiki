---
type: claim
title: "LLM accuracy varied sharply by histology topic: perfect in foundational areas and lowest in Muscle (76.0%)"
description: "LLM accuracy varied sharply by histology topic: perfect in foundational areas and lowest in Muscle (76.0%)"
id: histology-topic-difficulty-llm-performance
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
    kind: associational
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
    i: 3
    kind: associational
    rigour: 2
---

# LLM accuracy varied sharply by histology topic: perfect in foundational areas and lowest in Muscle (76.0%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All systems achieved perfect performance (100%) in Histological Methods, Blood and Hemopoiesis, and Circulatory System. [→ Mavrych Volodymyr 2025](#mavrych-volodymyr-2025)
`q2 i?` The lowest-performing topics were Muscle (76.0%), Lymphoid System (84.7%), and Urinary System (84.7%). [→ Mavrych Volodymyr 2025 (2)](#mavrych-volodymyr-2025-2)
`q2 i3` Performance across the challenging topics differed significantly (F(2,8) = 12.34, p < 0.001, η2 = 0.327), with muscle tissue significantly lower than lymphoid and urinary topics. [→ Mavrych Volodymyr 2025 (3)](#mavrych-volodymyr-2025-3)

## Evidence

### Mavrych Volodymyr 2025

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i?` · `associational · r2`

Topic-specific analysis of pooled accuracy across the five LLMs and twenty topics. The article reports "perfect performance (100%) across all systems in three fundamental areas: Histological Methods, Blood and Hemopoiesis, and Circulatory System."

> "The analysis revealed perfect performance (100%) across all systems in three fundamental areas: Histological Methods, Blood and Hemopoiesis, and Circulatory System."

### Mavrych Volodymyr 2025 (2)

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i?` · `design · r2`

Topic-specific analysis of LLM accuracy; the article reports that "Lower performance was noted in specialized topics such as the Lymphoid System (84.7%, SD = 7.2), Urinary System (84.7%, SD = 6.2), and Muscle (76.0%, SD = 6.1)." These are descriptive means without printed effect sizes.

> "Lower performance was noted in specialized topics such as the Lymphoid System (84.7%, SD = 7.2), Urinary System (84.7%, SD = 6.2), and Muscle (76.0%, SD = 6.1)."

### Mavrych Volodymyr 2025 (3)

Mavrych Volodymyr, Yousef Einas M., Yaqinuddin Ahmed, Bolgova Olena. (2025). Large language models in medical education: a comparative cross-platform evaluation in answering histological questions. Medical Education Online. https://doi.org/10.1080/10872981.2025.2534065

`q2 · i3` · `associational · r2`

One-way repeated measures ANOVA across the challenging topics, with Bonferroni-corrected post-hoc tests showing muscle tissue significantly lower than both lymphoid and urinary topics (mean difference = −8.7%, p = 0.003 for each). The article reports "η2 = 0.327".

> "A one-way repeated measures ANOVA comparing performance across these challenging topics revealed significant differences (F(2,8) = 12.34, p < 0.001, η2 = 0.327)"

## Discussion


## Related Claims
- [Histology topic, not LLM platform, was the primary factor in performance variance (η2 = 0.452 vs 0.006), with a significant system-by-topic interaction](topic-effect-dominates-system-effect-llm-histology.md) — a broader claim this one bears on
- [Five LLMs showed comparable, exceptionally high accuracy (collective mean 91.1%) on text-based medical histology MCQs](llm-mean-accuracy-91-1-histology-mcqs.md) — related
- [LLM accuracy on the EUS varies by subject area, with pharmacy legislation/ethics lowest (DeepSeek-R1 at 20%)](eus-subject-area-accuracy-variation.md) — related
- [LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference](subject-area-accuracy-variation-dus-llms.md) — related
- [Chatbot accuracy varied substantially across biochemistry topics: highest for eicosanoids (100%), bioenergetics and electron transport chain (96.4%), ketone bodies (93.8%), and the hexose monophosphate pathway (91.7%), lowest for globular proteins and hemoglobin (58.4%)](topic-level-chatbot-accuracy-variation-biochemistry.md) — a narrower finding that bears on this claim
- [LLM accuracy varied significantly across oncology topics, with the lowest performance in colorectal tumors (mean 48.3%) and genitourinary tumors (mean 50.8%)](llm-accuracy-varies-across-oncology-topics.md) — related
