---
type: claim
title: Students rated documentation from a predefined few-shot prompt significantly higher than documentation from ad-hoc prompts on readability, conciseness and usefulness, and on helpfulness for one of two functions
description: Students rated documentation from a predefined few-shot prompt significantly higher than documentation from ad-hoc prompts on readability, conciseness and usefulness, and on helpfulness for one of two functions
id: students-rate-predefined-prompt-documentation-higher
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
source_checked: 2026-11-20
sources:
  - id: hans-alexander-kruse-2024
    resource: "https://doi.org/10.1109/icsme58944.2024.00058"
    title: "Hans-Alexander Kruse, Tim Puhlfürß, Walid Maalej. (2024). Can Developers Prompt? A Controlled Experiment for Code Documentation Generation. [doi:10.1109/icsme58944.2024.00058](https://doi.org/10.1109/icsme58944.2024.00058)"
    author: Hans-Alexander Kruse, Tim Puhlfürß, Walid Maalej
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Students rated documentation from a predefined few-shot prompt significantly higher than documentation from ad-hoc prompts on readability, conciseness and usefulness, and on helpfulness for one of two functions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` Among students, documentation generated via the predefined few-shot prompt was rated significantly higher than ad-hoc-prompt documentation on readability, unnecessary information and usefulness for both functions; helpfulness differed significantly, with a large effect, for function 2 only (function 1: p = .52, δ = .21). [→ Hans-Alexander Kruse 2024](#hans-alexander-kruse-2024)

## Evidence

### Hans-Alexander Kruse 2024

Hans-Alexander Kruse, Tim Puhlfürß, Walid Maalej. (2024). Can Developers Prompt? A Controlled Experiment for Code Documentation Generation. [doi:10.1109/icsme58944.2024.00058](https://doi.org/10.1109/icsme58944.2024.00058)

`q2 · i?` · `causal · r2`

Controlled between-subject lab experiment with 20 professionals and 30 computer science students using GPT-4-based VS Code extensions; MWU tests on six five-point quality dimensions. The article reports significant differences exclusively among students, e.g. Unnecessary Information for function 2 at 2.66/4.86 with δ = 1.82.

> "We observed statistically significant differences exclusively among students, who rated the readability, conciseness, usefulness, and helpfulness of comments generated via the predefined few-shot prompt higher than those created via ad-hoc prompts."

## Discussion


## Related Claims
- [Professionals showed no statistically significant rating differences between ad-hoc and predefined prompt tools, partly because some used the Docstring keyword](professionals-no-significant-prompt-format-differences.md) — reports the opposite
- [Students rated the predefined prompt tool significantly more positive than the ad-hoc prompt tool in five of six UEQ user experience categories](students-prefer-predefined-prompt-tool-ux.md) — related
- [In one study, correct answers to comprehension questions about the more complex function rose from pre-test to post-test after LLM-generated documentation within students and professionals, with the largest rises among students; answers about the other function fell slightly within both groups.](llm-documentation-helps-students-comprehend-code.md) — related
