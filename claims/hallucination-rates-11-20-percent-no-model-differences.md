---
type: claim
title: "Hallucination rates ranged from 11% to 20.1% across LLMs without significant intermodel differences"
description: "Hallucination rates ranged from 11% to 20.1% across LLMs without significant intermodel differences"
id: hallucination-rates-11-20-percent-no-model-differences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: stefan-andrei-2026
    resource: "https://doi.org/10.2196/95859"
    title: "Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie. (2026). Performance and Hallucination Analysis of Large Language Models on European Anesthesiology Examinations: Cross-Sectional Comparative Study. JMIR Formative Research. https://doi.org/10.2196/95859"
    author: Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Hallucination rates ranged from 11% to 20.1% across LLMs without significant intermodel differences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Hallucination rates ranged from 11% (11/100) to 20.1% (44/219) with no significant intermodel differences on IADE or EDAIC questions. [→ Stefan Andrei 2026](#stefan-andrei-2026)

## Evidence

### Stefan Andrei 2026

Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie. (2026). Performance and Hallucination Analysis of Large Language Models on European Anesthesiology Examinations: Cross-Sectional Comparative Study. JMIR Formative Research. https://doi.org/10.2196/95859

`q2 · i?` · `design · r2`

Cochran Q test of hallucination rates across 4 LLMs on 100 IADE questions, with dual-reviewer consensus classification. The article reports rates "did not differ significantly across models (Cochran Q3=3.38; P=.34; W=0.01)"; abstract reports the range 11% (11/100) to 20.1% (44/219).

> "For IADE questions, hallucination rates did not differ significantly across models (Cochran Q3=3.38; P=.34; W=0.01)."

## Discussion


## Related Claims
- [No significant intermodel differences in IADE overall success rates, and no significant domain-level differences after Holm adjustment](iade-no-intermodel-differences-success.md) — related
- [Current-generation LLMs achieve 86% to 94% mean success rates on European anesthesiology examination questions, exceeding the EDAIC part I passing threshold](llm-success-rates-86-94-percent-anesthesiology-exams.md) — related
- [Gemini 2.5 Pro significantly outperformed GPT-5 on EDAIC questions as the only significant pairwise difference after Holm correction](gemini-outperformed-gpt5-edaic-pairwise.md) — related
- [IADE confusion rates showed a nominally significant omnibus difference of negligible magnitude not corroborated by pairwise analysis](iade-confusion-nominal-omnibus-negligible.md) — related
- [Hallucinations were rare for both human and LLM coders, whereas omission errors were more frequent and varied by coder](llm-hallucinations-rare-omissions-frequent.md) — related
- [AI output errors are frequent: 44.5% fabricated references in drafted research proposals and 5–13% unsafe chatbot medical answers](ai-output-error-rates-fabricated-unsafe.md) — related
