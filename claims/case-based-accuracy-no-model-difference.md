---
type: claim
title: Case-based question accuracy does not differ significantly across the four LLMs under either querying method
description: Case-based question accuracy does not differ significantly across the four LLMs under either querying method
id: case-based-accuracy-no-model-difference
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: erdal-selda-gökçe-2026
    resource: "https://doi.org/10.1186/s12909-026-08808-5"
    title: "Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül. (2026). The effectiveness of large language models in dental specialty questions: a comparative study in the field of prosthodontics. BMC Medical Education. https://doi.org/10.1186/s12909-026-08808-5"
    author: Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Case-based question accuracy does not differ significantly across the four LLMs under either querying method

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the 22 case-based questions, chi-square tests found no significant between-model difference under independent querying (χ²(3) = 5.11, p = 0.164) or sequential querying (χ²(3) = 5.09, p = 0.165). [→ Erdal Selda Gökçe 2026](#erdal-selda-gokce-2026)

## Evidence

### Erdal Selda Gökçe 2026

Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül. (2026). The effectiveness of large language models in dental specialty questions: a comparative study in the field of prosthodontics. BMC Medical Education. https://doi.org/10.1186/s12909-026-08808-5

`q2 · i?` · `causal · r1`

Chi-square test on observed correct/incorrect frequencies for the 22 case-based items. Table 1 reports independent-query case accuracies of 64%, 68%, 45%, and 77% (χ²(3) = 5.11, p = 0.164) and sequential-query accuracies of 77%, 68%, 64%, and 91% (χ²(3) = 5.09, p = 0.165); equivalence was not tested.

> "Regarding case-based questions, however, no statistically significant difference was found between the models under independent querying (p > 0.05) (Table 1)."

## Discussion


## Related Claims
- [The four LLMs differ significantly in overall and knowledge-question accuracy on DUS prosthodontics questions under independent querying, driven by DeepSeek's lower performance](llm-accuracy-differs-independent-query-dus-prosthodontics.md) — related
- [The evaluated LLMs show higher accuracy on knowledge-based than case-based DUS questions, indicating a limitation in clinically oriented reasoning](llm-knowledge-beats-case-based-prosthodontics.md) — related
- [Gemini 2.5 Pro achieved the highest case-based accuracy (91%) under sequential querying](gemini-highest-case-accuracy-sequential.md) — related
- [No significant differences in LLM accuracy across medical specialties or between acute and chronic questions](no-accuracy-differences-specialty-urgency.md) — related
