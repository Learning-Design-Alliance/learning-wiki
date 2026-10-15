---
type: claim
title: LLM feedback for students marked by race, language, disability, gender, or motivation shows positive feedback bias and feedback withholding bias — more praise and less substantive critique than for unmarked counterparts
description: LLM feedback for students marked by race, language, disability, gender, or motivation shows positive feedback bias and feedback withholding bias — more praise and less substantive critique than for unmarked counterparts
id: marked-students-praise-withholding-bias
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

# LLM feedback for students marked by race, language, disability, gender, or motivation shows positive feedback bias and feedback withholding bias — more praise and less substantive critique than for unmarked counterparts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Students identified as Black, Hispanic, Asian, female, unmotivated, and learning-disabled received less constructive criticism and more praise than their counterparts, reflecting feedback withholding and positive feedback biases. [→ Tan et al. 2026](#tan-et-al-2026)

## Evidence

### Tan et al. 2026

Mei Tan, Lena Phalen, and Dorottya Demszky. 2026. Marked Pedagogies: Examining Linguistic Biases in Personalized Automated Writing Feedback. In LAK 2026: 16th International Learning Analytics and Knowledge Conference (LAK 2026). ACM, New York, NY, USA. [doi:10.1145/3785022.3785113](https://doi.org/10.1145/3785022.3785113)

`q2 · i?` · `causal · r2`

Cross-condition lexical comparison of feedback generated for the same 600 essays under marked versus comparative prompts; the article reports the praise asymmetry as a qualitative pattern across conditions with no printed effect size. In some cases praise took stereotyped forms, with "love" used disproportionately with female students and "powerful" appearing only for Black students.

> "students identified as Black, Hispanic, Asian, female, unmotivated, and learning-disabled received less constructive criticism and more praise, reflecting both feedback withholding [ 11] and positive feedback biases [ 20]."

## Studies bearing on this claim

<!-- synthesis:start -->
*Does automated feedback on student work substitute praise for critique, and for whom?* This table gathers the studies behind this claim and the 4 narrower claims that bear on it: **3 distinct studies** (2 associational, 1 causal), `q2`, 0 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Tan et al. 2026](https://doi.org/10.1145/3785022.3785113) | q2 · causal · r2 | i? | this claim; [Motivation prompts shift feedback tone: unmotivated students receive enthusiastic, collabo](motivation-prompt-enthusiasm-pedagogy.md) (supports); [Gender prompts shift feedback stance: female students receive affective, first-person, emp](gender-prompt-emotional-connection-pedagogy.md) (qualifies) |
| [Jerin George Mathew 2026](https://doi.org/10.48550/arxiv.2603.23714) | q2 · associational · r2 | i? | [LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high s](llm-feedback-sentiment-tracks-scores.md) (qualifies) |
| [validation-content](https://doi.org/10.48550/arxiv.2609.19635) | q2 · associational · r2 | i? | [The agent's praise was indiscriminate affirmation: validation followed about half of parti](indiscriminate-affirmation-reflection-agent.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Gender prompts shift feedback stance: female students receive affective, first-person, empathy-oriented feedback while male students receive objective, task-oriented critique](gender-prompt-emotional-connection-pedagogy.md) — related
- [Race prompts elicit culturally stereotyped feedback: Black, Hispanic, and Asian students are positioned through cultural or linguistic stereotypes while White students receive argument-structure feedback](race-prompts-cultural-stereotype-feedback.md) — related
- [Motivation prompts shift feedback tone: unmotivated students receive enthusiastic, collaborative encouragement while motivated students receive direct, higher-level critique](motivation-prompt-enthusiasm-pedagogy.md) — a narrower finding that bears on this claim
- [Names alone elicit weaker, less consistent identity-marked feedback language than explicit attribute prompts](names-alone-elicit-weaker-marked-language.md) — related
- [Explicitly prompting a student attribute produces large, systematic increases in the concentration of stereotype-aligned marked words in LLM-generated writing feedback](prompted-attributes-increase-marked-pedagogy-concentration.md) — related
- [LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise](llm-feedback-sentiment-tracks-scores.md) — related
