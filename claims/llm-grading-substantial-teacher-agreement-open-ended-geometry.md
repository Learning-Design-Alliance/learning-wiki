---
type: claim
title: "LLM-based grading of open-ended geometry explanations shows substantial agreement with teacher judgments (overall agreement 0.866, Cohen's κ = 0.737)"
description: "LLM-based grading of open-ended geometry explanations shows substantial agreement with teacher judgments (overall agreement 0.866, Cohen's κ = 0.737)"
id: llm-grading-substantial-teacher-agreement-open-ended-geometry
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yong-oh-lee-2026
    resource: "https://doi.org/10.1109/access.2026.3657726"
    title: "Yong Oh Lee, Byeonghun Bang, Joohyun Lee, Sejun Oh. (2026). Personalized Auto-Grading and Feedback System for Constructive Geometry Tasks Using Large Language Models on an Online Math Platform. Preprint. Originally published 2025. [doi:10.1109/access.2026.3657726](https://doi.org/10.1109/access.2026.3657726)"
    author: Yong Oh Lee, Byeonghun Bang, Joohyun Lee, Sejun Oh
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-based grading of open-ended geometry explanations shows substantial agreement with teacher judgments (overall agreement 0.866, Cohen's κ = 0.737)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across seven open-ended explanatory items in the field study, automated LLM grading agreed with teacher grading at an overall rate of 0.866 with Cohen's κ = 0.737. [→ Yong Oh Lee 2026](#yong-oh-lee-2026)

## Evidence

### Yong Oh Lee 2026

Yong Oh Lee, Byeonghun Bang, Joohyun Lee, Sejun Oh. (2026). Personalized Auto-Grading and Feedback System for Constructive Geometry Tasks Using Large Language Models on an Online Math Platform. Preprint. Originally published 2025. [doi:10.1109/access.2026.3657726](https://doi.org/10.1109/access.2026.3657726)

`q2 · i?` · `design · r2`

Field study with 79 middle-school students; LLM grades on the seven open-ended explanation items were benchmarked against teacher judgments, with per-item agreement from 71.3% (Q15) to 96.5% (Q13). The article reports "the overall agreement rate reached 0.866" with κ = 0.737.

> "When aggregated across all explanatory tasks, the overall agreement rate reached 0.866 and the corresponding Cohen's κ was 0.737, indicating substantial consistency between automated and teacher grading."

## Discussion


## Related Claims
- [Teacher agreement with LLM grading is higher when the system judges answers correct (95.3%) than when it judges them incorrect (77.2%)](grading-agreement-asymmetry-correct-incorrect-judgments.md) — related
- [The multi-agent LLM GradeOpt achieved substantial agreement with human coders on overall PCK items (κ = .68, QWK = .79) and outperformed RoBERTa, SBERT, and naïve GPT-4o prompting](gradeopt-substantial-agreement-pck-outperforms-baselines.md) — related
- [Expert-rated quality of LLM feedback averages 3.98 on a five-point guidance rubric but varies substantially by item (Q9: 4.55; Q15: 3.33)](feedback-guidance-quality-varies-by-item.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Machine learning detects five of eight reflective-writing categories with substantial or almost perfect reliability and three with moderate reliability (Cohen's κ .53–.85)](ml-detects-reflection-categories-kappa-053-085.md) — related
- [Comparison models (RoBERTa, SBERT, naïve GPT-4o prompting) failed to reach acceptable agreement on PCK items, with Cohen's κ at or below .55](baseline-models-unacceptable-pck-agreement.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
