---
type: claim
title: Explicitly prompting a student attribute produces large, systematic increases in the concentration of stereotype-aligned marked words in LLM-generated writing feedback
description: Explicitly prompting a student attribute produces large, systematic increases in the concentration of stereotype-aligned marked words in LLM-generated writing feedback
id: prompted-attributes-increase-marked-pedagogy-concentration
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: tan-et-al-2026
    resource: "https://doi.org/10.1145/3785022.3785113"
    title: Tan et al. 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Explicitly prompting a student attribute produces large, systematic increases in the concentration of stereotype-aligned marked words in LLM-generated writing feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across all marked attributes, using the marked prompt produces large, systematic increases in the concentration of associated Marked Pedagogy words relative to baseline, e.g., +3.829 percentage points for ELL and +4.260 for unmotivated (both p < 0.001). [→ Tan et al. 2026](#tan-et-al-2026)

## Evidence

### Tan et al. 2026

Mei Tan, Lena Phalen, and Dorottya Demszky. 2026. Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback. In LAK 2026: 16th International Learning Analytics and Knowledge Conference (LAK 2026). ACM, New York, NY, USA. [doi:10.1145/3785022.3785113](https://doi.org/10.1145/3785022.3785113)

`q2 · i?` · `causal · r2`

Regression analysis of feedback generated for 600 PERSUADE essays across prompt conditions, controlling for true student characteristics, holistic essay score, and writing-assignment and source-LLM fixed effects. The article reports "3.829 percentage points (+78%,𝑝< 0.001)" for ELL and "4.260 percentage points (+74%,𝑝< 0.001)" for unmotivated; no standardized effect size is printed.

> "specifying that a student is an English Language Learner increases the concentration of 𝑀𝐸𝐿𝐿 words by 3.829 percentage points (+78%,𝑝< 0.001) on average, and prompting that a student is unmotivated increases the concentration of𝑀𝑈𝑛𝑚𝑜𝑡𝑖𝑣𝑎𝑡𝑒𝑑 words by 4.260 percentage points (+74%,𝑝< 0.001), relative to baseline."

## Discussion


## Related Claims
- [Names alone elicit weaker, less consistent identity-marked feedback language than explicit attribute prompts](names-alone-elicit-weaker-marked-language.md) — reports the opposite
- [Race prompts elicit culturally stereotyped feedback: Black, Hispanic, and Asian students are positioned through cultural or linguistic stereotypes while White students receive argument-structure feedback](race-prompts-cultural-stereotype-feedback.md) — related
- [LLM feedback for students marked by race, language, disability, gender, or motivation shows positive feedback bias and feedback withholding bias — more praise and less substantive critique than for unmarked counterparts](marked-students-praise-withholding-bias.md) — related
- [LLMs exhibit demographic sensitivity: systematic output differences attributable solely to demographic context when task inputs are held constant](llm-demographic-sensitivity-educational-tasks.md) — a broader claim this one bears on
- [Motivation prompts shift feedback tone: unmotivated students receive enthusiastic, collaborative encouragement while motivated students receive direct, higher-level critique](motivation-prompt-enthusiasm-pedagogy.md) — related
- [Feedback prompted with ELL status narrows to surface-level grammar and mechanics corrections, assuming limited language competency rather than addressing argument and reasoning](ell-feedback-language-inadequacy-pedagogy.md) — related
- [Identical student essays attributed to a \"White\" versus \"Black\" student receive different scores and feedback from ChatGPT, with the \"White\" student scored higher](chatgpt-racial-bias-autoscoring-example.md) — related
