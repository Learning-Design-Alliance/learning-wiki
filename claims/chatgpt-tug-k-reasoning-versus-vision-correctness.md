---
type: claim
title: "ChatGPT's TUG-K responses show correct reasoning in 69.7% but correct visual interpretation in only 30.9%, with no significant association between the two"
description: "ChatGPT's TUG-K responses show correct reasoning in 69.7% but correct visual interpretation in only 30.9%, with no significant association between the two"
id: chatgpt-tug-k-reasoning-versus-vision-correctness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: giulia-polverini-and-bor-gregorcic-2024
    resource: "https://doi.org/10.1103/physrevphyseducres.20.010109"
    title: "Giulia Polverini and Bor Gregorcic. (2024). Performance of ChatGPT on the Test of Understanding Graphs in Kinematics. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010109](https://doi.org/10.1103/physrevphyseducres.20.010109)"
    author: Giulia Polverini and Bor Gregorcic
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT's TUG-K responses show correct reasoning in 69.7% but correct visual interpretation in only 30.9%, with no significant association between the two

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Correct reasoning appears in 69.7% of coded responses while correct vision appears in only 30.9%; reasoning and vision correctness are statistically independent. [→ Giulia Polverini and Bor Gregorcic 2024](#giulia-polverini-and-bor-gregorcic-2024)

## Evidence

### Giulia Polverini and Bor Gregorcic 2024

Giulia Polverini and Bor Gregorcic. (2024). Performance of ChatGPT on the Test of Understanding Graphs in Kinematics. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010109](https://doi.org/10.1103/physrevphyseducres.20.010109)

`q2 · i?` · `design · r2`

Qualitative binary coding of 780 ChatGPT responses (first 30 of 60 surveys) by both authors; Cohen's kappa was 0.809 for reasoning and 0.967 for vision. A Chi-square test found no significant association between reasoning and vision (χ²(1)=2.016, p=0.156).

> "correct reasoning is present in 69.7% of all responses, while a correct visual interpretation can be found in only 30.9% of responses"

## Discussion


## Learner Variables
- [Statistical Reasoning](../learner-variables/statistical-reasoning.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Transcribing one TUG-K graph item into text raised ChatGPT's correctness from 10% to 100%](graph-transcription-bypasses-vision-failure.md) — related
- [ChatGPT can be unreliable even on basic conceptual physics tasks when vision is correct, as on item 17 (5% correct vs 70% for students)](chatgpt-uncanny-reasoning-failures.md) — related
- [Incorrect vision is a stronger predictor of incorrect TUG-K answers than incorrect reasoning in a logistic regression](incorrect-vision-predicts-incorrect-answers.md) — related
- [ChatGPT-4's performance on the Japanese National Nursing Examination differs by attached file format, with JPG (26% median) far below text-based formats (87%-94% medians)](file-format-affects-chatgpt-nursing-exam-performance.md) — a broader claim this one bears on
- [Generative AI excels at processing digital text but struggles with interpreting text from images](genai-visual-comprehension-gap-images.md) — a broader claim this one bears on
- [All four multimodal LLMs show a marked decrease in correct response rates on visually-based versus text-only JNEOT questions](llm-visual-question-decline-jneot.md) — a broader claim this one bears on
- [ChatGPT performed 34.4 percentage points lower than students on objective 1 (determining velocity from a position graph)](chatgpt-tug-k-objective-1-gap.md) — related
- [LLM accuracy drops from 96% on text-only to 74% on multimodal physics problems, with significant differences emerging among models](multimodal-physics-accuracy-drops-to-74-percent.md) — a broader claim this one bears on
- [TUG-K performance among Bogotá Physics I students fits a two-group model with proportions 0.6 and 0.4](tug-k-two-group-fit-bogota.md) — related
