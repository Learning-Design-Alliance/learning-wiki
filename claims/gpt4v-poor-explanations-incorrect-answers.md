---
type: claim
title: When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations
description: When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations
id: gpt4v-poor-explanations-incorrect-answers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yang-z-2025
    resource: "https://doi.org/10.2196/65146"
    title: "Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146"
    author: Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H.
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Among 55 incorrect responses, 76.3% (42/55) demonstrated image misunderstandings, 45.5% (25/55) inference errors, and 18.2% (10/55) text hallucination; no responses contained nonmedical errors. [→ Yang Z 2025](#yang-z-2025)

## Evidence

### Yang Z 2025

Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146

`q3 · i?` · `associational · r2`

Manual error coding of GPT-4V's incorrect explanations by three health care professionals using a rating guideline; the medical student and nurse agreed with the doctor's ratings at 95% and 86%. The quote reports the category proportions for the 55 wrong answers.

> "Among GPT-4V responses with wrong answers (n=55), we found that 76.3% (n=42) of responses included misunderstanding of the image, 45.5% (n=25) of responses included logic error, 18.2% (n=10) of responses included text hallucination, and no responses included nonmedical errors."

## Discussion


## Related Claims
- [In a simulated curbside consultation, GPT-4V required multiple specific physician-guided prompts to interpret complex case data accurately](curbside-consultation-required-multiple-prompts.md) — related
- [Health care professionals rated GPT-4V's explanations nearly on par with expert explanations when answers were correct, but overwhelmingly preferred expert explanations when answers were incorrect](explanation-preference-correct-versus-incorrect.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [An exploratory LLM-judge audit labels knowledge gaps (39.1%) and reasoning errors (26.9%) as the most frequent failure modes among incorrect frontier-model responses](llm-judge-audit-failure-modes.md) — related
- [GPT-4V's accuracy was inconsistent across medical subdomains, high in some (e.g. immunology 100%) and low in others (e.g. anatomy 25%)](gpt4v-subdomain-performance-inconsistent.md) — related
- [With expert hints describing the image, 40% (22/55) of GPT-4V's incorrect responses switched to the correct answer](image-hints-corrected-40-percent-errors.md) — related
- [Expert hints raised GPT-4V's accuracy and flattened its performance across question difficulty levels, while medical students' performance declined with difficulty](expert-hints-raise-gpt4v-accuracy-plateau-difficulty.md) — related
- [Informational errors account for over 70% of incorrect answers across all models, with simple logical errors under 10%](informational-errors-dominate-incorrect-answers.md) — related
- [AI chatbots' incorrect answers on the CINECA test are predominantly logical errors rather than information or statistical errors](chatbot-incorrect-answers-predominantly-logical-errors.md) — related
