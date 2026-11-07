---
type: claim
title: "Health care professionals rated GPT-4V's explanations nearly on par with expert explanations when answers were correct, but overwhelmingly preferred expert explanations when answers were incorrect"
description: "Health care professionals rated GPT-4V's explanations nearly on par with expert explanations when answers were correct, but overwhelmingly preferred expert explanations when answers were incorrect"
id: explanation-preference-correct-versus-incorrect
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
    kind: design
    rigour: 2
---

# Health care professionals rated GPT-4V's explanations nearly on par with expert explanations when answers were correct, but overwhelmingly preferred expert explanations when answers were incorrect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` For correct answers, of 95 votes 19 preferred experts, 15 preferred GPT-4V, and 61 were ties; for incorrect answers, 47 preferred experts and 0 preferred GPT-4V. [→ Yang Z 2025](#yang-z-2025)

## Evidence

### Yang Z 2025

Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146

`q3 · i?` · `design · r2`

Blinded preference evaluation by three health care professionals over explanations for the 150 AMBOSS questions, without knowing correctness or source. The quote reports the vote split for correct answers and the expert preference for incorrect ones.

> "When GPT-4V answered correctly, the quality of GPT-4V-generated explanations was close to expert-generated explanations: out of 95 votes, 19 preferred experts, 15 preferred GPT-4V, and 61 preferred either. The preference for expert explanations in incorrect answers highlights key weaknesses in GPT-4V's ability to interpret clinical images accurately"

## Discussion


## Related Claims
- [Expert hints raised GPT-4V's accuracy and flattened its performance across question difficulty levels, while medical students' performance declined with difficulty](expert-hints-raise-gpt4v-accuracy-plateau-difficulty.md) — related
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](gpt4v-poor-explanations-incorrect-answers.md) — related
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — a broader claim this one bears on
- [With expert hints describing the image, 40% (22/55) of GPT-4V's incorrect responses switched to the correct answer](image-hints-corrected-40-percent-errors.md) — related
- [In a simulated curbside consultation, GPT-4V required multiple specific physician-guided prompts to interpret complex case data accurately](curbside-consultation-required-multiple-prompts.md) — related
