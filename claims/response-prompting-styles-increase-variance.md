---
type: claim
title: Demographic and psychometric response prompting produces higher-variance, heavier-tailed originality distributions than a no-context baseline, though still less variable than humans
description: Demographic and psychometric response prompting produces higher-variance, heavier-tailed originality distributions than a no-context baseline, though still less variable than humans
id: response-prompting-styles-increase-variance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: antonio-laverghetta-jr-2024
    resource: "https://doi.org/10.48550/arxiv.2409.00202"
    title: "Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202 [doi:10.48550/arxiv.2409.00202](https://doi.org/10.48550/arxiv.2409.00202)"
    author: Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# Demographic and psychometric response prompting produces higher-variance, heavier-tailed originality distributions than a no-context baseline, though still less variable than humans

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`

## Subclaims
`q2 i?` Compared to the no-context baseline, demographic and psychometric prompting strategies exhibit higher variance and heavier tails in the originality distribution, better reflecting human trends, but both curves still have lower variance than humans. [→ Antonio Laverghetta Jr. 2024](#antonio-laverghetta-jr-2024)

## Evidence

### Antonio Laverghetta Jr. 2024

Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202 [doi:10.48550/arxiv.2409.00202](https://doi.org/10.48550/arxiv.2409.00202)

`q2 · i?` · `design · r?`

Distributional comparison of originality scores by item response prompting strategy (Results §4.3, Fig. 5a), with human participant scores from the scoring model's training data plotted as a non-equivalent comparison since humans were not given the CPIG items. Descriptive only; no test statistic or effect size is printed.

> "Compared to the no-context baseline — where the item response generator LLMs are simply instructed to answer the item —both demographic and psychometric prompting strategies exhibit higher variance and heavier tails in the originality distribution, better reflecting the trends from human participants."

## Discussion


## Related Claims
- [CPIG's iterative exemplar selection consistently improves the originality of LLM responses to generated CPS items by the last round of item generation](cpig-improves-response-originality-over-iterations.md) — related
- [Human-shadow prompting generates broad psychometric variance while AI-assistant responses are uniform](human-shadow-prompting-generates-psychometric-variance.md) — related
- Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts — related
- LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses — related
- [LLMs simulating survey respondents under AI-assistant instructions report higher mathematics self-efficacy and lower anxiety than under human-shadow conditioning](ai-assistant-mode-inflates-math-self-efficacy.md) — related
