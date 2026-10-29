---
type: claim
title: Hallucinations were rare for both human and LLM coders, whereas omission errors were more frequent and varied by coder
description: Hallucinations were rare for both human and LLM coders, whereas omission errors were more frequent and varied by coder
id: llm-hallucinations-rare-omissions-frequent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-22
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: jansen-2026
    resource: "https://doi.org/10.1007/s10648-026-10136-5"
    title: "Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J. (2026). Automated Data Extraction by Large Language Models: Assessing Accuracy in Comparison to Human Experts Using the Example of Visible Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10136-5"
    author: "Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J."
    q: 3
    i: "?"
    kind: design
    rigour: 3
  - id: jansen-2026-2
    resource: "https://doi.org/10.1007/s10648-026-10136-5"
    title: "Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J. (2026). Automated Data Extraction by Large Language Models: Assessing Accuracy in Comparison to Human Experts Using the Example of Visible Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10136-5"
    author: "Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J."
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Hallucinations were rare for both human and LLM coders, whereas omission errors were more frequent and varied by coder

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Hallucinations ranged from 3 to 4 cases among the 55 meta-analyses lacking the information in the full text, for all coder sources. [→ Jansen 2026](#jansen-2026)
`q3 i?` Omission rates differed by coder: author coding had 12 omissions, Gemini 2.5 Pro 21, GPT 4.1 22, Visible Learning 31, and GPT o3 36, all in the number of included students. [→ Jansen 2026 (2)](#jansen-2026-2)

## Evidence

### Jansen 2026

Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J. (2026). Automated Data Extraction by Large Language Models: Assessing Accuracy in Comparison to Human Experts Using the Example of Visible Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10136-5

`q3 · i?` · `design · r3`

Error-type analysis of the extraction evaluation, defining hallucinations as reporting a value absent from the source text. The article reports "the number of hallucinations ranging from 3 to 4 cases" among the 55 meta-analyses missing that information; no effect size is printed.

> "Both expert human coders and LLMs produced very few fabricated data points, with the number of hallucinations ranging from 3 to 4 cases among the 55 meta-analyses for which that information was missing in the full text."

### Jansen 2026 (2)

Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J. (2026). Automated Data Extraction by Large Language Models: Assessing Accuracy in Comparison to Human Experts Using the Example of Visible Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10136-5

`q3 · i?` · `design · r2`

Omission analysis in the same evaluation: coding present information as missing. The article reports Gemini 2.5 Pro and GPT 4.1 at "21 and 22 errors, respectively", better than Visible Learning's 31 omissions; author coding had the lowest rate (12) and GPT o3 the highest (36), all in student counts.

> "The state-of-the-art LLMs (Gemini 2.5 Pro and GPT 4.1) showed moderate omission rates, with 21 and 22 errors, respectively, performing better on this metric than the Visible Learning data, which had 31 omissions."

## Discussion


## Related Claims
- [Most extraction discrepancies stemmed from ambiguity within the source meta-analyses rather than coder fabrication](discrepancies-source-ambiguity.md) — related
- [State-of-the-art LLMs extract effect sizes, study counts, and participant counts from educational meta-analyses with excellent agreement with adjudicated gold and silver standards](llm-data-extraction-icc-gold-standard.md) — related
- [Across 468 data points, human coders, LLMs, and both standards agreed on the same value in 280 cases (59.8%)](coder-agreement-patterns-upset-468.md) — related
- [Neither LLM nor human coders showed systematic over- or under-estimation in extracting data from educational meta-analyses](no-systematic-bias-llm-extraction.md) — related
- [LLMs are not ready to be used as primary data extraction tools without explicit human validation in education research synthesis](llms-not-ready-primary-data-extraction-without-human-validation.md) — reports the opposite
