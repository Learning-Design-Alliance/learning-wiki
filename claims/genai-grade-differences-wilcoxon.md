---
type: claim
title: "GenAI models' grades differ significantly across models, with GPTo1 grading more leniently than Llama2, Mistral7B and Cohere"
description: "GenAI models' grades differ significantly across models, with GPTo1 grading more leniently than Llama2, Mistral7B and Cohere"
id: genai-grade-differences-wilcoxon
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
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

# GenAI models' grades differ significantly across models, with GPTo1 grading more leniently than Llama2, Mistral7B and Cohere

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The Friedman test showed statistically significant differences among models' scores, and Wilcoxon tests with Bonferroni correction found GPTo1 grades better than Llama2, Mistral7B and Cohere but comparable to PaLM2 and Claude3. [→ Pecuchova 2025](#pecuchova-2025)
`q2 i?` Llama2, Mistral7B and Cohere showed no significant grade differences with near-zero RBC values, indicating practical equivalence at grade level. [→ Pecuchova 2025](#pecuchova-2025)

## Evidence

### Pecuchova 2025

Pecuchova, J., Benko, Ľ., & Drlik, M. (2025). Automated Grading of Open-Ended Questions in Higher Education Using GenAI Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00517-2

`q2 · i?` · `design · r2`

Non-parametric comparisons in the evaluation phase (Friedman ANOVA N = 1885, df = 10, p < 0.01; Wilcoxon with Bonferroni correction); a negative RBC of -0.2791 suggested "GPTo1 grades with better marks than Cohere", while it "performs comparably to PaLM2 and Claude3".

> "On the other hand, GPTo1 performs comparably to PaLM2 and Claude3 ( p > 0.05)."

## Discussion


## Related Claims
- [Claude3 and PaLM2 show substantial agreement but fall short on identifying failing grades](claude3-palm2-substantial-agreement-failing-grades.md) — related
- [Statistical tests show significant grading differences among nearly all pairs of LLMs, with only 7 of 153 pairs statistically indistinguishable](friedman-posthoc-llm-grading-pairs-differ.md) — possibly the same claim (merge candidate)
- [The omnibus ANOVA on total QM score did not reach conventional significance, though a Friedman test suggested an overall difference with no significant pairwise Wilcoxon comparisons](total-qm-score-omnibus-nonsignificant-friedman-significant.md) — related
