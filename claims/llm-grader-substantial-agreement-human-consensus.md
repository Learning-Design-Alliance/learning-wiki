---
type: claim
title: An LLM grader using a four-level explanation-quality rubric achieved substantial agreement with human consensus scores (quadratic-weighted κ=0.78).
description: An LLM grader using a four-level explanation-quality rubric achieved substantial agreement with human consensus scores (quadratic-weighted κ=0.78).
id: llm-grader-substantial-agreement-human-consensus
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: eason-chen-2026
    resource: "https://doi.org/10.1007/978-3-032-29763-1_42"
    title: "Eason Chen, Xinyi Tang, Yvonne Zhao, Meiyi Chen, Meryam Elmir, Elizabeth McLaughlin, Mingyu Yuan, Yumo Wang, Shyam Agarwal, Jared Cochrane, Jionghao Lin, Tongshuang Wu, and Ken Koedinger. (2026). Practice Less, Explain More: LLM-Supported Self-Explanation Improves Explanation Quality on Transfer Problems in Calculus. arXiv preprint. [doi:10.1007/978-3-032-29763-1_42](https://doi.org/10.1007/978-3-032-29763-1_42)"
    author: Eason Chen, Xinyi Tang, Yvonne Zhao, Meiyi Chen, Meryam Elmir, Elizabeth McLaughlin, Mingyu Yuan, Yumo Wang, Shyam Agarwal, Jared Cochrane, Jionghao Lin, Tongshuang Wu, and Ken Koedinger
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: eason-chen-2026-2
    resource: "https://doi.org/10.1007/978-3-032-29763-1_42"
    title: "Eason Chen, Xinyi Tang, Yvonne Zhao, Meiyi Chen, Meryam Elmir, Elizabeth McLaughlin, Mingyu Yuan, Yumo Wang, Shyam Agarwal, Jared Cochrane, Jionghao Lin, Tongshuang Wu, and Ken Koedinger. (2026). Practice Less, Explain More: LLM-Supported Self-Explanation Improves Explanation Quality on Transfer Problems in Calculus. arXiv preprint. [doi:10.1007/978-3-032-29763-1_42](https://doi.org/10.1007/978-3-032-29763-1_42)"
    author: Eason Chen, Xinyi Tang, Yvonne Zhao, Meiyi Chen, Meryam Elmir, Elizabeth McLaughlin, Mingyu Yuan, Yumo Wang, Shyam Agarwal, Jared Cochrane, Jionghao Lin, Tongshuang Wu, and Ken Koedinger
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# An LLM grader using a four-level explanation-quality rubric achieved substantial agreement with human consensus scores (quadratic-weighted κ=0.78).

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-5.1, using the same rubric and grading prompt as human graders, achieved quadratic-weighted κ=0.78 against the human consensus score. [→ Eason Chen 2026](#eason-chen-2026)

## Evidence

### Eason Chen 2026

Eason Chen, Xinyi Tang, Yvonne Zhao, Meiyi Chen, Meryam Elmir, Elizabeth McLaughlin, Mingyu Yuan, Yumo Wang, Shyam Agarwal, Jared Cochrane, Jionghao Lin, Tongshuang Wu, and Ken Koedinger. (2026). Practice Less, Explain More: LLM-Supported Self-Explanation Improves Explanation Quality on Transfer Problems in Calculus. arXiv preprint. [doi:10.1007/978-3-032-29763-1_42](https://doi.org/10.1007/978-3-032-29763-1_42)

`q2 · i?` · `causal · r2`

LLM grading validation study: two human graders evaluated "a sample of 160 explanations from a prior pilot study, reaching substantial agreement" (quadratic-weighted Cohen's κ=0.70) to form the human consensus score against which the LLM grader was evaluated.

> "Two human graders evaluated a sample of 160 explanations from a prior pilot study, reaching substantial agreement (quadratic- weighted Cohen’sκ=0.70); disagreements were resolved by the first author to formthehumanconsensusscore."

### Eason Chen 2026 (2)

Eason Chen, Xinyi Tang, Yvonne Zhao, Meiyi Chen, Meryam Elmir, Elizabeth McLaughlin, Mingyu Yuan, Yumo Wang, Shyam Agarwal, Jared Cochrane, Jionghao Lin, Tongshuang Wu, and Ken Koedinger. (2026). Practice Less, Explain More: LLM-Supported Self-Explanation Improves Explanation Quality on Transfer Problems in Calculus. arXiv preprint. [doi:10.1007/978-3-032-29763-1_42](https://doi.org/10.1007/978-3-032-29763-1_42)

`q2 · i?` · `causal · r2`

The LLM (GPT-5.1), using the same rubric and grading prompt, achieved quadratic-weighted "κ=0.78 with human consensus score", with κ=0.68 against Grader 1 and κ=0.66 against Grader 2.

> "The model achieved quadratic-weightedκ=0.68 against Grader 1,κ=0.66 against Grader 2, andκ=0.78 with human consensus score."

## Discussion


## Related Claims
- [Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters](scaffolded-cot-human-level-agreement-gpt35-grading.md) — related
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](gpt4o-self-consistency-human-level-grading-agreement.md) — related
- [GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)](gpt4o-grades-written-physics-explanations-comparable-to-human-graders.md) — related
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — a broader claim this one bears on
- [Open-ended self-explanation with LLM feedback produces significantly higher-quality explanations than control on NEI transfer problems in calculus (β=+11.9 percentage points, p=.030, d=0.44).](llm-open-ended-self-explanation-nei-transfer-explanation-quality.md) — related
- [The GPT-4o mini event classifier agrees with domain experts at almost-perfect pairwise levels (κ = 0.841–0.855), reducing multi-rater Fleiss κ only marginally (0.682 to 0.624)](llm-event-classifier-expert-agreement.md) — related
- [GPT-4o achieved substantial agreement with human raters for the Physics Concepts theme (Cohen's κ = 0.7) after optimization](gpt4o-substantial-agreement-physics-concepts-coding.md) — related
