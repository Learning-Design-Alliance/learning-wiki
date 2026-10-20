---
type: claim
title: Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading
description: Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading
id: embedding-models-moderate-agreement-need-supervision
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: pecuchova-2025
    resource: "https://doi.org/10.1007/s40593-025-00517-2"
    title: "Pecuchova, J., Benko, Ľ., & Drlik, M. (2025). Automated Grading of Open-Ended Questions in Higher Education Using GenAI Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00517-2"
    author: "Pecuchova, J., Benko, Ľ., & Drlik, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Sentence embedding models reach only moderate agreement and need human supervision for open-ended grading

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Sentence embedding models achieved mostly moderate agreement with human graders and are not appropriate for open-ended assessment without further human supervision. [→ Pecuchova 2025](#pecuchova-2025)

## Evidence

### Pecuchova 2025

Pecuchova, J., Benko, Ľ., & Drlik, M. (2025). Automated Grading of Open-Ended Questions in Higher Education Using GenAI Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00517-2

`q2 · i?` · `design · r2`

Evaluation of SBERT, USE, T5, BERT and RoBERTa using cosine similarity against reference answers in the same 1,885-response dataset; "Most of the sentence embedding models' agreement is at moderate level" with human graders.

> "Most of the sentence embedding models’ agreement is at moderate level and would be not appropriate to use these models for open-ended questions assessment without further human supervision."

## Discussion


## Related Claims
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — related
- Two human graders reached almost perfect agreement (QWK = 0.95), though one waterfall-model question showed only substantial agreement — related
- [Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones](plm-performance-depends-on-pedagogical-expertise-required.md) — related
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — related
- [The most challenging holistic-rubric question reached only moderate inter-rater reliability (kw=0.54) after three iterations](holistic-hardest-question-moderate-reliability.md) — related
- [Most faculty–GPT-4 scoring discrepancies were only one-point differences, shrinking across iterations](oeq-scoring-discrepancies-mostly-one-point.md) — related
- [Comparison models (RoBERTa, SBERT, naïve GPT-4o prompting) failed to reach acceptable agreement on PCK items, with Cohen's κ at or below .55](baseline-models-unacceptable-pck-agreement.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — a broader claim this one bears on
