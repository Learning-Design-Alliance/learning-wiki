---
type: claim
title: "Inter-model consistency declines progressively with question complexity, from substantial agreement on SBA-R (κ > 0.72) to only fair agreement on image questions (ChatGPT-o1pro κ = 0.40)"
description: "Inter-model consistency declines progressively with question complexity, from substantial agreement on SBA-R (κ > 0.72) to only fair agreement on image questions (ChatGPT-o1pro κ = 0.40)"
id: kappa-consistency-declines-question-complexity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: çamlar-mahmut-2025
    resource: "https://doi.org/10.1007/s00701-025-06628-y"
    title: "Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer. (2025). Comparative performance of neurosurgery-specific, peer-reviewed versus general AI chatbots in bilingual board examinations: evaluating accuracy, consistency, and error minimization strategies. Acta Neurochirurgica 167(1):241. https://doi.org/10.1007/s00701-025-06628-y"
    author: Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: çamlar-mahmut-2025-2
    resource: "https://doi.org/10.1007/s00701-025-06628-y"
    title: "Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer. (2025). Comparative performance of neurosurgery-specific, peer-reviewed versus general AI chatbots in bilingual board examinations: evaluating accuracy, consistency, and error minimization strategies. Acta Neurochirurgica 167(1):241. https://doi.org/10.1007/s00701-025-06628-y"
    author: Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Inter-model consistency declines progressively with question complexity, from substantial agreement on SBA-R (κ > 0.72) to only fair agreement on image questions (ChatGPT-o1pro κ = 0.40)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Overall, the top three models showed substantial agreement (ChatGPT-o1pro κ = 0.707, AtlasGPT κ = 0.728, ChatGPT-4 κ = 0.658) while other models showed only fair agreement (0.349–0.394). [→ Çamlar Mahmut 2025](#camlar-mahmut-2025)
`q2 i?` Consistency declined from SBA-R (κ > 0.72) to SBA-I (κ = 0.55–0.59) to image questions (ChatGPT-o1pro κ = 0.40, ChatGPT-4 κ = 0.331, Copilot κ = −0.04). [→ Çamlar Mahmut 2025 (2)](#camlar-mahmut-2025-2)

## Evidence

### Çamlar Mahmut 2025

Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer. (2025). Comparative performance of neurosurgery-specific, peer-reviewed versus general AI chatbots in bilingual board examinations: evaluating accuracy, consistency, and error minimization strategies. Acta Neurochirurgica 167(1):241. https://doi.org/10.1007/s00701-025-06628-y

`q2 · i?` · `design · r2`

Cohen's kappa analysis of inter-model response consistency across all 599 questions, excluding processing failures. The article reports substantial agreement among the top three models and only fair agreement among the others.

> "the top three models demonstrated substantial agreement: ChatGPT-o1pro (κ = 0.707), AtlasGPT (κ = 0.728), and ChatGPT-4 (κ = 0.658), while other models showed only fair agreement with values ranging from 0.349 to 0.394"

### Çamlar Mahmut 2025 (2)

Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer. (2025). Comparative performance of neurosurgery-specific, peer-reviewed versus general AI chatbots in bilingual board examinations: evaluating accuracy, consistency, and error minimization strategies. Acta Neurochirurgica 167(1):241. https://doi.org/10.1007/s00701-025-06628-y

`q2 · i?` · `design · r2`

Kappa analysis by question type. The article reports a progressive decline in consistency as questions became more complex: substantial agreement in SBA-R (κ > 0.72) and true–false (κ > 0.70), moderate in SBA-I (κ = 0.55–0.59), and lowest for image questions, with Copilot at κ = −0.04.

> "The most significant decline was observed in questions with images, where even the best-performing model (ChatGPT-o1pro) achieved only fair agreement (κ = 0.40), and some models showed no meaningful agreement."

## Discussion


## Related Claims
- [Accuracy on questions with images drops sharply for all models: ChatGPT-o1pro 52.6% and ChatGPT-4 45.4% versus Gemini 12.4% and Copilot 11.3%, with frequent response-generation failures](image-question-accuracy-collapse-llms.md) — related
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
- [The three LLMs showed fair inter-model agreement on the AAMC SJT, agreeing most strongly on incorrect answers](llm-fair-agreement-same-errors-aamc-sjt.md) — related
- [ChatGPT-o1pro shows higher response consistency on Turkish questions (κ = 0.836) than English questions (κ = 0.689), while AtlasGPT and ChatGPT-4 remain balanced across languages](language-specific-consistency-turkish-english.md) — related
- [On SBA-R recall-of-knowledge questions, ChatGPT-o1pro attains 81.6% accuracy, with ChatGPT-4 and AtlasGPT close behind, while Gemini, Copilot, and ChatGPT-3.5 remain below 52%](sba-r-accuracy-top-three-models-neurosurgery.md) — related
- [On true–false and SBA-I interpretative questions, ChatGPT-o1pro, ChatGPT-4, and AtlasGPT outperform Gemini, Copilot, and ChatGPT-3.5, with all models weaker on interpretative items](true-false-and-sba-i-performance-gap.md) — related
