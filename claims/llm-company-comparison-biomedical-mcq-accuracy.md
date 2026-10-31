---
type: claim
title: Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies
description: Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies
id: llm-company-comparison-biomedical-mcq-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-31
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: cheverko-cm-2026
    resource: "https://doi.org/10.1002/ase.70262"
    title: "Cheverko CM, Mavrych V, Bolgova O, Mohamed FRR, Westrick J, Juarez L, Rush E, Solka KA, Doubleday AF, Byram JN, Becker R, Gomez V, Ganeng BKA, Hoffman LA, Roach VA, Brown KM, DeVaul N, Garnett CN, Herriott HL, Lufler RS, Mussell JC, Balta JY, Pascoe MA, Middleton JW, Duffy S, Stephens GC, Wilson AB. (2026). The performance of ChatGPT and other large language models on multiple‐choice questions in biomedical disciplines: A meta‐analysis. Anatomical Sciences Education. https://doi.org/10.1002/ase.70262"
    author: Cheverko CM, Mavrych V, Bolgova O, Mohamed FRR, Westrick J, Juarez L, Rush E, Solka KA, Doubleday AF, Byram JN, Becker R, Gomez V, Ganeng BKA, Hoffman LA, Roach VA, Brown KM, DeVaul N, Garnett CN, Herriott HL, Lufler RS, Mussell JC, Balta JY, Pascoe MA, Middleton JW, Duffy S, Stephens GC, Wilson AB
    q: 3
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Pooled accuracy: Claude 3–3.7 = 86.2% and DeepSeek R1 = 86.0%, modestly underperforming GPT‐4o_o1; Gemini series = 75.5% and Copilot = 69.4% trailed the leading companies. [→ Cheverko CM 2026](#cheverko-cm-2026)

## Evidence

### Cheverko CM 2026

Cheverko CM, Mavrych V, Bolgova O, Mohamed FRR, Westrick J, Juarez L, Rush E, Solka KA, Doubleday AF, Byram JN, Becker R, Gomez V, Ganeng BKA, Hoffman LA, Roach VA, Brown KM, DeVaul N, Garnett CN, Herriott HL, Lufler RS, Mussell JC, Balta JY, Pascoe MA, Middleton JW, Duffy S, Stephens GC, Wilson AB. (2026). The performance of ChatGPT and other large language models on multiple‐choice questions in biomedical disciplines: A meta‐analysis. Anatomical Sciences Education. https://doi.org/10.1002/ase.70262

`q3 · i?` · `quant-synthesis · r2`

Random‐effects proportional meta‐analysis comparing newer LLM models from companies with ≥5 data points against OpenAI models. Reports Claude 3–3.7 at "86.2%, CI = 81.7%–89.7%", DeepSeek R1 at 86.0%, Gemini at 75.5%, Copilot at 69.4%. Heterogeneity was high for Gemini and Copilot (I² ≥ 76%) and low for Anthropic and DeepSeek (I² ≤ 20%).

> "Anthropic's Claude 3 through 3.7 (86.2%, CI = 81.7%–89.7%) and DeepSeek's R1 (86.0%, CI = 78.0%–90.3%) models modestly underperformed compared with OpenAI's GPT‐4o_o1 models. The performance of the Google Gemini series (75.5%, CI = 68.0%–81.7%) and Microsoft Copilot (69.4%, CI = 54.0%–81.4%) trailed that of the leading companies."

## Discussion


## Related Claims
- [GPT‐4 through o1 models achieve pooled accuracy of 87% in the anatomical sciences and ≥83% in five of six biomedical disciplines, consistently above older versions](gpt4-o1-discipline-pooled-accuracy-biomedical.md) — related
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — related
- [LLM version progression explains about half of the variance in biomedical MCQ accuracy, with GPT‐4o_o1 over six times as likely as GPT‐3/3.5 to answer correctly](llm-version-meta-regression-explains-accuracy-variance.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [The author reports that prompt phrasing and the specific foundational model had secondary impact on final material quality compared with the structure of the workflow itself.](workflow-architecture-outweighs-prompt-phrasing.md) — related
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
- [GPT‐4 through o1 models show significantly lower pooled accuracy in pathology (75%) than in other biomedical disciplines](lower-llm-accuracy-pathology-biomedical-mcq.md) — related
- [Question type, stem type, MCQ source, and web accessibility did not independently explain LLM accuracy heterogeneity in biomedical MCQ meta‐regressions](mcq-covariates-not-explaining-llm-accuracy-heterogeneity.md) — related
