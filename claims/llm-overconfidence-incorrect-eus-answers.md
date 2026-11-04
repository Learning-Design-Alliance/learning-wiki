---
type: claim
title: LLMs frequently assign maximum self-reported confidence to incorrect EUS answers
description: LLMs frequently assign maximum self-reported confidence to incorrect EUS answers
id: llm-overconfidence-incorrect-eus-answers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: balaban-ugur-2026
    resource: "https://doi.org/10.1038/s41598-026-57001-7"
    title: "Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay. (2026). Performance of large language models on the Turkish Pharmacy Specialty Examination: a comparative analysis of accuracy, confidence, and readability. Scientific Reports. https://doi.org/10.1038/s41598-026-57001-7"
    author: Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs frequently assign maximum self-reported confidence to incorrect EUS answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ChatGPT-5.1 assigned maximum confidence to 7 of 8 incorrect responses (87.5%), DeepSeek-R1 to 5 of 9 (55.6%), and Gemini 2.5 Flash to 4 of 6 (66.7%). [→ Balaban Ugur 2026](#balaban-ugur-2026)

## Evidence

### Balaban Ugur 2026

Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay. (2026). Performance of large language models on the Turkish Pharmacy Specialty Examination: a comparative analysis of accuracy, confidence, and readability. Scientific Reports. https://doi.org/10.1038/s41598-026-57001-7

`q2 · i?` · `design · r2`

Confidence analysis of incorrect responses across the 84-question EUS benchmark (Fig. 2). ChatGPT-5.1 assigned maximum confidence to 7 out of 8 incorrect responses (87.5%), DeepSeek-R1 to 5 out of 9 (55.6%), and Gemini 2.5 Flash to 4 out of 6 (66.7%).

> "ChatGPT-5.1 assigned maximum confidence to 7 out of 8 incorrect responses (87.5%), while DeepSeek-R1 assigned maximum confidence to 5 out of 9 incorrect responses (55.6%). Gemini 2.5 Flash assigned maximum confidence to 4 out of 6 incorrect responses (66.7%)."

## Discussion


## Related Claims
- [ChatGPT-5.1 generates EUS answers with significantly lower linguistic complexity (GFI, SMOG) than DeepSeek-R1 and Gemini 2.5 Flash](chatgpt-lower-gfi-smog-readability.md) — related
- [ChatGPT-5.1, DeepSeek-R1, and Gemini 2.5 Flash show high, statistically comparable accuracy on Turkish Pharmacy Specialty Examination questions](llms-high-comparable-accuracy-eus.md) — related
- [LLM accuracy on the EUS varies by subject area, with pharmacy legislation/ethics lowest (DeepSeek-R1 at 20%)](eus-subject-area-accuracy-variation.md) — related
