---
type: claim
title: Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades
description: Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades
id: claude3-palm2-substantial-agreement-failing-grades
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
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

# Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Claude3 and PaLM2 demonstrated substantial agreement with human graders, performing better on higher-grade assessments than on identifying failing grades. [→ Pecuchova 2025](#pecuchova-2025)

## Evidence

### Pecuchova 2025

Pecuchova, J., Benko, Ľ., & Drlik, M. (2025). Automated Grading of Open-Ended Questions in Higher Education Using GenAI Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00517-2

`q2 · i?` · `design · r2`

Findings summary of the model-comparison evaluation in the software engineering grading study, as stated by the authors: the models were "excelling in higher-grade assessments but falling short in identifying failing grades".

> "Models such as Claude3 and PaLM2 dem onstrated substantial agreement, excelling in higher-grade assessments but falling short in identifying failing grades."

## Discussion

## Related Claims

- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — the general claim this finding bears on, with the studies behind it
- [GenAI models' grades differ significantly across models, with GPTo1 grading more leniently than Llama2, Mistral7B and Cohere](genai-grade-differences-wilcoxon.md) — related
- [Newer LLM generations do not consistently agree better with human essay graders](no-consistent-generational-improvement-llm-grading.md) — related
- [ChatGPT's exam scores were within 10% of human grades 70% of the time in a study of AI-based grading](chatgpt-grading-within-10-percent-human.md) — related
- [LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes](llm-fast-mode-limited-thinking-mode-better-agreement.md) — related
