---
type: claim
title: LLMs struggled to generate complex functional code and could not autonomously retrieve astronomical datasets from online archives or query data tables
description: LLMs struggled to generate complex functional code and could not autonomously retrieve astronomical datasets from online archives or query data tables
id: llm-code-and-archive-access-failures
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zabludoff-2026
    resource: "https://doi.org/10.48550/arXiv.2603.25984"
    title: "Zabludoff, A., Chuang, C., Johnson, P. T., Liu, Y., Martinez, B. B., Shah, N., Steffes, L., & Weible, G. G. (2026). Can LLMs Produce Original Astronomy Research in a Semester? A Graduate Class Experiment. Originally published 2025. [doi:10.48550/arXiv.2603.25984](https://doi.org/10.48550/arXiv.2603.25984)"
    author: "Zabludoff, A., Chuang, C., Johnson, P. T., Liu, Y., Martinez, B. B., Shah, N., Steffes, L., & Weible, G. G."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs struggled to generate complex functional code and could not autonomously retrieve astronomical datasets from online archives or query data tables

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Students found LLMs struggled with generating complex functional code for data analysis and physically accurate simulation code, and could point to data-table URLs but could not successfully query the tables or retrieve datasets from archives such as VizieR. [→ Zabludoff 2026](#zabludoff-2026)

## Evidence

### Zabludoff 2026

Zabludoff, A., Chuang, C., Johnson, P. T., Liu, Y., Martinez, B. B., Shah, N., Steffes, L., & Weible, G. G. (2026). Can LLMs Produce Original Astronomy Research in a Semester? A Graduate Class Experiment. Originally published 2025. [doi:10.48550/arXiv.2603.25984](https://doi.org/10.48550/arXiv.2603.25984)

`q2 · i?` · `design · r2`

Failure analysis from the Fall 2025 course experiment. The article reports the models had difficulties autonomously accessing datasets from archives like VizieR, running packages such as STARBURST99, and generated code incompatible with the MaNGA dataset format. No statistics reported.

> "Despite agentic advances, this apparent inability to directly search the internet or to interact with APIs, e.g., for querying data tables and downloading data from them, is a significant impediment to research."

## Discussion


## Related Claims
- [Optional IBM Quantum hardware execution supplied extra evidence but did not remove substantial AI assistance, as ChatGPT generated the code and could interpret returned noisy data](hardware-execution-did-not-eliminate-llm-assistance.md) — related
- [Higher-struggling-level problems elicit more diverse but less student-like LLM-generated errors](higher-struggling-problems-elicit-more-diverse-less-student-like-errors.md) — related
