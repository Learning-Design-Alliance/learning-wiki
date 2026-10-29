---
type: claim
title: State-of-the-art LLMs extract effect sizes, study counts, and participant counts from educational meta-analyses with excellent agreement with adjudicated gold and silver standards
description: State-of-the-art LLMs extract effect sizes, study counts, and participant counts from educational meta-analyses with excellent agreement with adjudicated gold and silver standards
id: llm-data-extraction-icc-gold-standard
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
---

# State-of-the-art LLMs extract effect sizes, study counts, and participant counts from educational meta-analyses with excellent agreement with adjudicated gold and silver standards

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Across Gemini 2.5 Pro, GPT 4.1, and GPT o3, percentage agreement with the gold standard ranged from 77% to 81% and ICCs ranged from 0.96 to 0.97. [→ Jansen 2026](#jansen-2026)

## Evidence

### Jansen 2026

Jansen, T., Liebenow, L. W., Schaller, N.-J., Hattie, J., & Möller, J. (2026). Automated Data Extraction by Large Language Models: Assessing Accuracy in Comparison to Human Experts Using the Example of Visible Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10136-5

`q3 · i?` · `design · r3`

Evaluation of three LLMs extracting three variables from 156 educational meta-analyses randomly sampled from Visible Learning, benchmarked against adjudicated standards. The article reports "percentage agreement ranged from 77% to 81%" and ICCs "ranging from 0.96 to 0.97" against the gold standard; against the silver standard agreements were 78% to 84% with ICCs 0.94 to 0.96. No effect size is printed for this finding.

> "Across the three models, percentage agreement ranged from 77% to 81%, while the Intraclass Correlation Coefficients (ICC) were excellent, ranging from 0.96 to 0.97."

## Discussion


## Related Claims
- [Most extraction discrepancies stemmed from ambiguity within the source meta-analyses rather than coder fabrication](discrepancies-source-ambiguity.md) — related
- [Hallucinations were rare for both human and LLM coders, whereas omission errors were more frequent and varied by coder](llm-hallucinations-rare-omissions-frequent.md) — related
- [LLM-based extraction of three variables from 156 meta-analyses cost about $50 in computing fees, far less than estimated human-assistant labor costs](llm-extraction-cost-time-savings.md) — related
- [LLMs show moderate agreement with human coders when extracting explicitly stated data from education studies](llms-moderate-agreement-explicit-data-extraction-education.md) — related
- [LLMs are not ready to be used as primary data extraction tools without explicit human validation in education research synthesis](llms-not-ready-primary-data-extraction-without-human-validation.md) — reports the opposite
