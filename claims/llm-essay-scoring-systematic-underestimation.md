---
type: claim
title: In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range
description: In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range
id: llm-essay-scoring-systematic-underestimation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-29
recheck_by: 2029
sources:
  - id: tongxi-liu-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100565"
    title: "Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565"
    author: Tongxi Liu, Luyao Ye, Wei Yan
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-29 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Of the five LLMs tested on 60 undergraduate essays scored against the IELTS Task 2 rubric, most systematically assigned lower scores than human raters, a consistent negative bias the article interprets as a calibration offset rather than random fluctuation. [→ Tongxi Liu 2026](#tongxi-liu-2026)

## Evidence

### Tongxi Liu 2026

Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565

`q2 · i?` · `associational · r1`

Bland-Altman bias analysis across five LLMs (GPT-4.1, Llama 4 Maverick, Gemini 2.5 Flash, Claude Sonnet 4, DeepSeek R1) scoring 60 essays written by non-native English-speaking students for an undergraduate course, on the four IELTS Task 2 rubric dimensions, reported in Results §4.3 with Fig. 4. The article describes the negative bias as a "general calibration offset rather than random fluctuation" with magnitude varying by model and criterion.

> "Specifically, underestimation emerged as the dominant trend, indi - cating that most models systematically assigned lower scores than human raters (Fig. 4)."

## Discussion


## Related Claims

- [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human rating discrepancies exceeding 1.5 standard deviations in 38% of graduate-level bibliographies](gpt4-essay-score-inflation.md) — reports the opposite
- [Under the initial rubric with direct evaluation, machine raters systematically underestimate openness while relevance and clarity align near-perfectly](initial-rubric-openness-systematic-underestimation.md) — related
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — reports the opposite
- ML-based scoring approaches more often overestimated expert-assigned scores, whereas LLM-based approaches more often underestimated them — possibly the same claim (merge candidate)
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
- [Under LLM evaluators, structured rubrics produced larger negative deviations from the human baseline than free-form rubrics, the opposite direction of the human-evaluator pattern](structured-free-form-llm-deviation-contrast.md)
- [AI scoring shows a systematic conservative bias, under-grading writing so 15.3% (2024) and 16.5% (2025) of human-passing tests would fail under AI scoring](ai-scoring-systematic-under-grading-bias-pass-fail.md) — a narrower finding that bears on this claim
- [Lower linguistic quality of physics explanations is associated with higher odds that AI-based scoring underestimates conceptual understanding, across all eleven examined AI-based scoring approaches](ai-scoring-underestimates-linguistically-weak-physics-explanations.md) — related
- [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays](llm-overrate-short-essays-overpenalize-errors.md) — reports the opposite
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [RAG prompting shows systematic leniency, over-scoring relative to teacher mean scores in all four rubric dimensions (total bias = 1.787)](rag-systematic-leniency-overscoring.md) — reports the opposite
- [ChatGPT 3.5 grading with the best prompt was significantly lower than official IELTS examiner grades, indicating systematic bias in absolute grading](llm-grades-significantly-lower-than-examiners.md) — a narrower finding that bears on this claim
