---
type: claim
title: Human–GPT coding agreement varied sharply by code, with near-chance or negative Kappa for co-ordination codes despite near-perfect agreement on others
description: Human–GPT coding agreement varied sharply by code, with near-chance or negative Kappa for co-ordination codes despite near-perfect agreement on others
id: gpt4-kappa-varies-by-dialogue-code
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: mixed
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: long-2024
    resource: "https://doi.org/10.1038/s41539-024-00273-3"
    title: "Long, Y., Luo, H. & Zhang, Y. (2024). Evaluating large language models in analysing classroom dialogue. npj Science of Learning 9:60. https://doi.org/10.1038/s41539-024-00273-3"
    author: "Long, Y., Luo, H. & Zhang, Y."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human–GPT coding agreement varied sharply by code, with near-chance or negative Kappa for co-ordination codes despite near-perfect agreement on others

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Kappa was near-perfect for ELI (0.973 Chinese, 0.995 math) and EL (0.961 Chinese, 0.977 math), but near zero or negative for CI, SC, RC, RW and SU in at least one subject. [→ Long 2024](#long-2024)

## Evidence

### Long 2024

Long, Y., Luo, H. & Zhang, Y. (2024). Evaluating large language models in analysing classroom dialogue. npj Science of Learning 9:60. https://doi.org/10.1038/s41539-024-00273-3

`q2 · i?` · `design · r2`

Cohen's Kappa analysis between human coder and ChatGPT by code and subject (Table 3). The article reports "lower Kappa scores, such as CI" and negative values, noting negative Kappa in RC "suggest no agreement beyond chance".

> "High Kappa values, as seen in codes such as ELI (0.973 for Chinese, 0.995 for Math) and EL (0.961 for Chinese, 0.977 for Math), indicate near-perfect agreement, underscoring the potential of ChatGPT to accurately follow the coding scheme. Conversely, lower Kappa scores, such as CI (0.497 for Chinese, −0.005 for Math) and SC (0.216 for Chinese, 0.004 for Math), point to a divergence in understanding or application of the coding manual"

## Discussion


## Related Claims
- [GPT-4's coding consistency differed between math and Chinese lessons for codes such as CI, SC, RW and SU](gpt4-coding-consistency-subject-differences.md) — possibly the same claim (merge candidate)
- [A customised GPT-4 agreed with a human coder on over 90% of coded dialogue turns in both math and Chinese lessons](gpt4-human-coder-agreement-over-90-percent.md) — related
- [In classroom video labeling, high raw agreement (often exceeding 90%) co-occurred with low chance-corrected κ due to temporal misalignment](raw-agreement-kappa-paradox-classroom-video.md) — related
- [Prior non-LLM automated coding approaches yielded variable and often lower agreement with human coders on teacher knowledge measures, especially PCK](prior-automated-coding-variable-lower-agreement-pck.md) — related
- [All automated models, including GradeOpt, were most challenged by knowledge of teaching mathematics items (GradeOpt κ = .59) and least challenged by knowledge of students' mathematical thinking (κ = .79)](pck-subdomain-variation-ktm-hardest.md) — related
