---
type: claim
title: "LLM accuracy on multilingual medical multiple-choice questions varies substantially by model, with Claude-Sonnet-3.7 highest (87%) and open models lowest (64%-73%)"
description: "LLM accuracy on multilingual medical multiple-choice questions varies substantially by model, with Claude-Sonnet-3.7 highest (87%) and open models lowest (64%-73%)"
id: llm-accuracy-varies-by-model-medical-mcq
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: strasser-livia-maria-2026
    resource: "https://doi.org/10.2196/81399"
    title: "Strasser Livia Maria, Anschuetz Wilma, Dennstädt Fabio, Hastings Janna. (2026). Performance Evaluation of Large Language Models in Multilingual Medical Multiple-Choice Questions: Mixed Methods Study. JMIR Medical Education. https://doi.org/10.2196/81399"
    author: Strasser Livia Maria, Anschuetz Wilma, Dennstädt Fabio, Hastings Janna
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM accuracy on multilingual medical multiple-choice questions varies substantially by model, with Claude-Sonnet-3.7 highest (87%) and open models lowest (64%-73%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 10 runs per question, Claude-Sonnet-3.7 achieved the highest mean accuracy (87%) and GPT4o 84%, while Llama3.3-70b, Llama3.1-405b, and DeepSeek V3 performed significantly less reliably (64%, 69%, 73%; P<.001). [→ Strasser Livia Maria 2026](#strasser-livia-maria-2026)

## Evidence

### Strasser Livia Maria 2026

Strasser Livia Maria, Anschuetz Wilma, Dennstädt Fabio, Hastings Janna. (2026). Performance Evaluation of Large Language Models in Multilingual Medical Multiple-Choice Questions: Mixed Methods Study. JMIR Medical Education. https://doi.org/10.2196/81399

`q2 · i?` · `causal · r2`

Quantitative analysis of five LLMs answering 114 text-only Swiss medical self-assessment questions in three languages, 10 runs per question with default settings. The article reports Claude-Sonnet-3.7 at "highest mean accuracy (87%, SD 0.34%)" and GPT4o at 84%; the three open models scored 64%-73% with P<.001 in all 3 cases.

> "Claude-Sonnet-3.7 demonstrated the highest mean accuracy (87%, SD 0.34%) and lowest variability, indicating consistent performance. GPT4o also showed strong performance (mean accuracy 84%, SD 0.36%) with slightly more variability."

## Discussion


## Related Claims
- [Claude 3.5 Sonnet achieved the highest overall performance (86.28%), accuracy (85.57%), and clarity (91.73%) in generating USMLE-style medical ethics MCQs](claude-35-sonnet-highest-ethics-mcq-performance.md) — related
- [Claude-Sonnet-3.7 shows a markedly higher frequency of reasoning errors despite factual accuracy than GPT4o in erroneous medical answers](claude-reasoning-errors-despite-factual-accuracy.md) — related
- [English prompts generally yield better LLM accuracy than language-matched prompts, but top models perform comparably with language-matched prompts](english-prompt-advantage-top-models-comparable.md) — a narrower finding that bears on this claim
- [ChatGPT-5 achieved the highest overall accuracy on ophthalmology board-style questions (92.59%), with no statistically significant differences among the four LLMs](chatgpt-5-highest-overall-accuracy-ophthalmology-board-questions.md) — related
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
- [Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement](claude-sonnet-superior-temporal-reliability-radiology-questions.md) — related
- [All four LLMs show higher accuracy on general than clinical questions, significant only for Grok-4](general-vs-clinical-accuracy-gap.md) — related
