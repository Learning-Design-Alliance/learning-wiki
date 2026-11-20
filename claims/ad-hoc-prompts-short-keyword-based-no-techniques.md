---
type: claim
title: "Developers' successful ad-hoc prompts were short, keyword-based, and never included prompt engineering techniques such as examples or templates"
description: "Developers' successful ad-hoc prompts were short, keyword-based, and never included prompt engineering techniques such as examples or templates"
id: ad-hoc-prompts-short-keyword-based-no-techniques
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
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

# Developers' successful ad-hoc prompts were short, keyword-based, and never included prompt engineering techniques such as examples or templates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Hans-Alexander Kruse 2024: no comparison group (read from the study by two models, 2026-11-20)

## Subclaims
`q2 i?` Successful ad-hoc prompts fell into five patterns dominated by documentation keywords, with mean lengths of about seven words, and no participant added examples or templates. [→ Hans-Alexander Kruse 2024](#hans-alexander-kruse-2024)

## Evidence

### Hans-Alexander Kruse 2024

Hans-Alexander Kruse, Tim Puhlfürß, Walid Maalej. (2024). Can Developers Prompt? A Controlled Experiment for Code Documentation Generation. [doi:10.1109/icsme58944.2024.00058](https://doi.org/10.1109/icsme58944.2024.00058)

`q2 · i?` · `causal · r2`

Categorization of the ad-hoc prompts collected during the controlled experiment (Table I): comment (34x), Docstring (12), explain (2), summarize (1), Python-conform description (1). Successful prompts were short, with a mean length of 7.1 (2.09) words among professionals and 6.7 (2.62) among students, and none enhanced prompts with examples or templates.

> "We categorized the 50 prompts that led to a successful generation of code comments for both code functions into five prompt patterns"

## Discussion


## Related Claims
- [Professionals showed no statistically significant rating differences between ad-hoc and predefined prompt tools, partly because some used the Docstring keyword](professionals-no-significant-prompt-format-differences.md) — related
- [Students rated the predefined prompt tool significantly more positive than the ad-hoc prompt tool in five of six UEQ user experience categories](students-prefer-predefined-prompt-tool-ux.md) — related
