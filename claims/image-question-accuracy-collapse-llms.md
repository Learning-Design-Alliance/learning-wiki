---
type: claim
title: "Accuracy on questions with images drops sharply for all models: ChatGPT-o1pro 52.6% and ChatGPT-4 45.4% versus Gemini 12.4% and Copilot 11.3%, with frequent response-generation failures"
description: "Accuracy on questions with images drops sharply for all models: ChatGPT-o1pro 52.6% and ChatGPT-4 45.4% versus Gemini 12.4% and Copilot 11.3%, with frequent response-generation failures"
id: image-question-accuracy-collapse-llms
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

# Accuracy on questions with images drops sharply for all models: ChatGPT-o1pro 52.6% and ChatGPT-4 45.4% versus Gemini 12.4% and Copilot 11.3%, with frequent response-generation failures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For 97 questions with images, ChatGPT-o1pro (52.6%) and ChatGPT-4 (45.4%) significantly exceeded Gemini (12.4%) and Copilot (11.3%) (p < 0.001), and ChatGPT-o1pro declined from 81.1% on non-image questions. [→ Çamlar Mahmut 2025](#camlar-mahmut-2025)
`q2 i?` Response-generation failures concentrated on image questions: Copilot failed on 68 of 97 items and Gemini on 30, while ChatGPT-o1pro processed all questions. [→ Çamlar Mahmut 2025 (2)](#camlar-mahmut-2025-2)

## Evidence

### Çamlar Mahmut 2025

Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer. (2025). Comparative performance of neurosurgery-specific, peer-reviewed versus general AI chatbots in bilingual board examinations: evaluating accuracy, consistency, and error minimization strategies. Acta Neurochirurgica 167(1):241. https://doi.org/10.1007/s00701-025-06628-y

`q2 · i?` · `design · r2`

Analysis of 97 image-based questions in the six-model benchmark (Table 1). The article reports ChatGPT-o1pro declined substantially from 81.1% on non-image questions to 52.6% on image questions, and that AtlasGPT and ChatGPT-3.5 were excluded because they lack image-evaluation capabilities.

> "For questions with images, ChatGPT-o1pro had 52.6% and ChatGPT-4 had 45.4% accurasies. These rates differed significantly from those for Gemini (12.4%) and Copilot (11.3%) (p < 0.001)."

### Çamlar Mahmut 2025 (2)

Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer. (2025). Comparative performance of neurosurgery-specific, peer-reviewed versus general AI chatbots in bilingual board examinations: evaluating accuracy, consistency, and error minimization strategies. Acta Neurochirurgica 167(1):241. https://doi.org/10.1007/s00701-025-06628-y

`q2 · i?` · `design · r2`

Response-failure analysis for image questions. The article reports Copilot failed on 68 of 97 items, Gemini on 30, ChatGPT-4 on three, and ChatGPT-o1pro processed all questions; the authors suggest the high non-response rate markedly affected accuracy.

> "For questions with images, Copilot failed to generate responses for 68 of the 97 items owing to technical limitations, whereas Gemini encountered processing errors in 30 cases."

## Discussion


## Related Claims
- [ChatGPT-o1pro, ChatGPT-4, and AtlasGPT achieve significantly higher overall accuracy than Gemini, Copilot, and ChatGPT-3.5 on 599 bilingual neurosurgery multiple-choice questions](gpt-o1pro-chatgpt4-atlasgpt-outperform-general-chatbots-neurosurgery-mcq.md) — a broader claim this one bears on
- [Inter-model consistency declines progressively with question complexity, from substantial agreement on SBA-R (κ > 0.72) to only fair agreement on image questions (ChatGPT-o1pro κ = 0.40)](kappa-consistency-declines-question-complexity.md) — related
- [All seven LLMs showed markedly lower accuracy on image-based than text-based DUS questions, with significant text-image gaps for five models but not Gemini or Claude](llms-lower-accuracy-image-based-dus-questions.md) — related
- [A sensitivity analysis excluding not-applicable answers (e.g., image-based items) yielded results similar to the main accuracy comparison](cineca-accuracy-sensitivity-analysis-similar-results.md) — related
