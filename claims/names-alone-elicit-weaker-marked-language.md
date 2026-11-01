---
type: claim
title: Names alone elicit weaker, less consistent identity-marked feedback language than explicit attribute prompts
description: Names alone elicit weaker, less consistent identity-marked feedback language than explicit attribute prompts
id: names-alone-elicit-weaker-marked-language
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: tan-et-al-2026
    resource: "https://doi.org/10.1145/3785022.3785113"
    title: Tan et al. 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Names alone elicit weaker, less consistent identity-marked feedback language than explicit attribute prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Feedback generated using racially and gendered names showed some identity-marked language — Black names were associated with higher concentrations of MBlack — but effects were smaller, less consistent, and often noisy relative to explicit prompts. [→ Tan et al. 2026](#tan-et-al-2026)

## Evidence

### Tan et al. 2026

Mei Tan, Lena Phalen, and Dorottya Demszky. 2026. Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback. In LAK 2026: 16th International Learning Analytics and Knowledge Conference (LAK 2026). ACM, New York, NY, USA. [doi:10.1145/3785022.3785113](https://doi.org/10.1145/3785022.3785113)

`q2 · i?` · `causal · r2`

Robustness experiment generating feedback for each essay using names drawn from U.S. naming distributions, then regressing the concentration metric on the race and gender categories encoded in the names. Full regression tables are in supplemental materials; no effect size is printed in the main text.

> "Some identity-marked language appeared in response to names—e.g., Black names were associated with higher concen- trations of 𝑀𝐵𝑙𝑎𝑐𝑘 , and non-male and non-White names showed modest increases in𝑀𝐿𝑒𝑎𝑟𝑛𝑖𝑛𝑔𝐷𝑖𝑠𝑎𝑏𝑖𝑙𝑖𝑡𝑦 and𝑀𝑈𝑛𝑚𝑜𝑡𝑖𝑣𝑎𝑡𝑒𝑑 —but the effects were smaller, less consistent, and often noisy relative to explicit prompts."

## Discussion


## Related Claims
- [Explicitly prompting a student attribute produces large, systematic increases in the concentration of stereotype-aligned marked words in LLM-generated writing feedback](prompted-attributes-increase-marked-pedagogy-concentration.md) — reports the opposite
- [LLM feedback for students marked by race, language, disability, gender, or motivation shows positive feedback bias and feedback withholding bias — more praise and less substantive critique than for unmarked counterparts](marked-students-praise-withholding-bias.md) — related
- [Race prompts elicit culturally stereotyped feedback: Black, Hispanic, and Asian students are positioned through cultural or linguistic stereotypes while White students receive argument-structure feedback](race-prompts-cultural-stereotype-feedback.md) — related
- [LLMs exhibit demographic sensitivity: systematic output differences attributable solely to demographic context when task inputs are held constant](llm-demographic-sensitivity-educational-tasks.md) — a broader claim this one bears on
- [Identical student essays attributed to a \"White\" versus \"Black\" student receive different scores and feedback from ChatGPT, with the \"White\" student scored higher](chatgpt-racial-bias-autoscoring-example.md) — related
