---
type: claim
title: LLM-based transcript classifications agreed highly with human judgment for explicit questions (κ = .778) and math talk (κ = .722), but only moderately for need for help (κ = .562) and confusion (κ = .531)
description: LLM-based transcript classifications agreed highly with human judgment for explicit questions (κ = .778) and math talk (κ = .722), but only moderately for need for help (κ = .562) and confusion (κ = .531)
id: llm-classification-agreement-varies-by-construct
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: hur-2026
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    title: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030"
    author: "Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-based transcript classifications agreed highly with human judgment for explicit questions (κ = .778) and math talk (κ = .722), but only moderately for need for help (κ = .562) and confusion (κ = .531)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Human–LLM agreement on 200 randomly coded instances was high for the more objective constructs (explicit question κ = .778; discussing math κ = .722) and more moderate for need help (κ = .562) and might be confused (κ = .531). [→ Hur 2026](#hur-2026)

## Evidence

### Hur 2026

Hur, P., Palaguachi, C., Machaka, N., Krist, C., Dyer, E. B., D'Angelo, C., & Bosch, N. (2026). A Framework for Considering Exploration, Interpretation, and Confirmation During Data Analysis: Computationally Assisted Analysis of Teacher–Group Interactions. Journal of Educational Data Mining, 18(1). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1030

`q2 · i?` · `design · r2`

Reliability assessment of the on-premises Mistral LLM classifications against human judgment on 200 randomly selected instances, with sample size set by simulation-based power analysis (10,000 iterations) targeting a Cohen's κ confidence interval width below 0.2. The article reports "high agreement between humans and LLM" for explicit question and discussing math, and more moderate agreement for need help (κ = .562) and might be confused (κ = .531).

> "Inter - rater reliability showed high agreement between humans and LLM for the more objective con- structs “explicit question” (κ = .778) and “discussing math” ( κ = .722)."

## Discussion


## Related Claims
- [LLM-detected confusion in student dialogue decreased after teacher–group interactions (β = −0.061, p = .049)](confusion-decreased-after-interactions.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — reports the opposite
- [Constructs with higher operational clarity show higher overall coder agreement, and low clarity harms human coder agreement more than LLM agreement](construct-clarity-predicts-coding-agreement.md) — a broader claim this one bears on
- [LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers](llm-inductive-coding-risks-require-human-oversight.md) — related
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- [The interview coding achieved high inter-rater reliability, with Cohen's Kappa of 0.82 between independent coders](chatgpt-study-coding-kappa-082.md) — related
