---
type: claim
title: "Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)"
description: "Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)"
id: five-error-types-llm-diagnosis-vague-evidence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yoonsu-kim-2026
    resource: "https://doi.org/10.48550/arxiv.2504.00843"
    title: "Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843 [doi:10.48550/arxiv.2504.00843](https://doi.org/10.48550/arxiv.2504.00843)"
    author: Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim
    q: 2
    i: "?"
    kind: qualitative
    rigour: 3
  - id: yoonsu-kim-2026-2
    resource: "https://arxiv.org/abs/2504.00843"
    title: "Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843"
    author: Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Three authors coded 372 sampled error cases (13.2% of 2,816) into five error types with substantial inter-rater reliability (Fleiss' κ= 0.74). [→ Yoonsu Kim 2026](#yoonsu-kim-2026)
`q2 i?` Smaller models showed a higher proportion of hallucination errors (48.78%), while reasoning-oriented models committed over-inference more frequently (46.61%). [→ Yoonsu Kim 2026 (2)](#yoonsu-kim-2026-2)

## Evidence

### Yoonsu Kim 2026

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843 [doi:10.48550/arxiv.2504.00843](https://doi.org/10.48550/arxiv.2504.00843)

`q2 · i?` · `qualitative · r3`

Qualitative error analysis of model outputs on incorrectly diagnosed vague-evidence cases. Three authors coded 372 of 2,816 error instances into five types (evidence misidentification, rubric misinterpretation, over-inference, consistency issues, hallucination) with Fleiss' κ= 0.74.

> "Three authors collaboratively ana-lyzed 372 cases (13.2%) sampled from a total of 2,816 error instances, covering 18 model responses, and iteratively derived five recurring error types with sub-stantial inter-rater reliability (Fleiss'κ= 0.74)."

### Yoonsu Kim 2026 (2)

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843

`q2 · i?` · `design · r2`

Distribution of the five error types across model categories (Table 4, Figure 5). The article reports over-inference at 33.5%, evidence misidentification at 23.4%, and hallucination at 19.8%, with systematic differences by model type.

> "Errors related toover-inferencewere most prevalent (33.5%), followed byevi-dence misidentification(23.4%) andhallucination(19.8%)."

## Discussion


## Related Claims
- [LLMs frequently over-attribute evidential strength and assert Evident evidence even for incorrect diagnoses, and the two tendencies are strongly correlated](evidence-over-attribution-false-attribution.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers — related
- [Three recurring AI failure modes arose in this project-based learning context: plausible-but-incorrect code, missing specialized knowledge, and limited long-term context](three-ai-failure-modes-project-based-learning.md) — related
- [Recurring risks of GenAI in STEAM education include hallucination, bias, superficial completion strategies, and compromised assessment validity](genai-steam-risks-hallucination-bias.md) — related
- [Phase VI AI-enabled systems face six documented challenges: explainability, hallucination risk, prompt sensitivity, computational cost, validation complexity, and limited large-scale evidence](phase-vi-ai-systems-six-challenges.md) — related
- [The most reported risks of AI tools in science and chemistry education are ethical issues, including gender and racial bias, hallucinations, copyright infringement, and plagiarism](ethical-issues-most-reported-ai-risk.md) — related
- Among 828 manually coded matched references, the most common issue was ACM metadata mismatch (229 cases), followed by author-field errors (225 cases) — related
- [All 18 evaluated LLMs score macro F1 below 0.5 in diagnosing students' cognitive skills from handwritten math work](llms-f1-below-05-cognitive-skill-diagnosis.md) — related
- [MathCog: a benchmark of 3,036 teacher-annotated diagnostic verdicts over 639 handwritten student responses to 110 math problems with Evident/Vague evidence labels](mathcog-benchmark-dataset.md) — related
- [Thematic coding of sentence misinterpretations yields three categories: lexical confusion, structure misinterpretation, and partial recognition with wrong sequencing](thematic-categories-sentence-misinterpretation.md) — related
- [Vision-assisted extraction identified chart type in all sampled images but showed ±5–10% numeric estimation error and two failure modes correctable via mandatory review](llm-chart-extraction-accuracy-failure-modes.md) — related
- [LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs](llm-hallucination-rate-education.md) — related
