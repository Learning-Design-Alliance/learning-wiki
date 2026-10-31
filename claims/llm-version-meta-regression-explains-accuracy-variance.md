---
type: claim
title: LLM version progression explains about half of the variance in biomedical MCQ accuracy, with GPT‐4o_o1 over six times as likely as GPT‐3/3.5 to answer correctly
description: LLM version progression explains about half of the variance in biomedical MCQ accuracy, with GPT‐4o_o1 over six times as likely as GPT‐3/3.5 to answer correctly
id: llm-version-meta-regression-explains-accuracy-variance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-31
evidence_strength: strong
newest_evidence: 2026
sources:
  - id: cheverko-cm-2026
    resource: "https://doi.org/10.1002/ase.70262"
    title: "Cheverko CM, Mavrych V, Bolgova O, Mohamed FRR, Westrick J, Juarez L, Rush E, Solka KA, Doubleday AF, Byram JN, Becker R, Gomez V, Ganeng BKA, Hoffman LA, Roach VA, Brown KM, DeVaul N, Garnett CN, Herriott HL, Lufler RS, Mussell JC, Balta JY, Pascoe MA, Middleton JW, Duffy S, Stephens GC, Wilson AB. (2026). The performance of ChatGPT and other large language models on multiple‐choice questions in biomedical disciplines: A meta‐analysis. Anatomical Sciences Education. https://doi.org/10.1002/ase.70262"
    author: Cheverko CM, Mavrych V, Bolgova O, Mohamed FRR, Westrick J, Juarez L, Rush E, Solka KA, Doubleday AF, Byram JN, Becker R, Gomez V, Ganeng BKA, Hoffman LA, Roach VA, Brown KM, DeVaul N, Garnett CN, Herriott HL, Lufler RS, Mussell JC, Balta JY, Pascoe MA, Middleton JW, Duffy S, Stephens GC, Wilson AB
    q: 4
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# LLM version progression explains about half of the variance in biomedical MCQ accuracy, with GPT‐4o_o1 over six times as likely as GPT‐3/3.5 to answer correctly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q4`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q4 i?` Meta‐regression of OpenAI versions found version progression explained 54.9% of observed variance in accuracy (p < 0.001), with GPT‐4 OR = 3.13 and GPT‐4o_o1 OR = 6.36 versus GPT‐3/3.5. [→ Cheverko CM 2026](#cheverko-cm-2026)

## Evidence

### Cheverko CM 2026

Cheverko CM, Mavrych V, Bolgova O, Mohamed FRR, Westrick J, Juarez L, Rush E, Solka KA, Doubleday AF, Byram JN, Becker R, Gomez V, Ganeng BKA, Hoffman LA, Roach VA, Brown KM, DeVaul N, Garnett CN, Herriott HL, Lufler RS, Mussell JC, Balta JY, Pascoe MA, Middleton JW, Duffy S, Stephens GC, Wilson AB. (2026). The performance of ChatGPT and other large language models on multiple‐choice questions in biomedical disciplines: A meta‐analysis. Anatomical Sciences Education. https://doi.org/10.1002/ase.70262

`q4 · i?` · `quant-synthesis · r2`

Meta‐regression (maximum‐likelihood, random effects) on the pooled all‐discipline OpenAI dataset. Version progression "explained 54.9% of the observed variance in performance (p < 0.001)"; the article also reports β = 1.14 (OR = 3.13) for GPT‐4 and β = 1.85 (OR = 6.36) for GPT‐4o_o1 versus GPT‐3/3.5. Odds ratios are not standardised effect sizes, so i is null.

> "A meta‐regression analysis of OpenAI's GPT versions indicated that version progression explained 54.9% of the observed variance in performance (p < 0.001)."

## Discussion


## Related Claims
- [GPT‐4 through o1 models achieve pooled accuracy of 87% in the anatomical sciences and ≥83% in five of six biomedical disciplines, consistently above older versions](gpt4-o1-discipline-pooled-accuracy-biomedical.md) — related
- [Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies](llm-company-comparison-biomedical-mcq-accuracy.md) — related
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — related
- [Question type, stem type, MCQ source, and web accessibility did not independently explain LLM accuracy heterogeneity in biomedical MCQ meta‐regressions](mcq-covariates-not-explaining-llm-accuracy-heterogeneity.md) — related
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
