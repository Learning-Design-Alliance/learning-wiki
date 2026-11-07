---
type: claim
title: Claude outperformed ChatGPT-4 and Gemini in accuracy on Polish/English medical-dental exam questions in both prompt languages
description: Claude outperformed ChatGPT-4 and Gemini in accuracy on Polish/English medical-dental exam questions in both prompt languages
id: claude-highest-accuracy-ldek-exam-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: wójcik-2025
    resource: "https://doi.org/10.1038/s41598-025-17030-0"
    title: "Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L. (2025). Comparing the performance of ChatGPT, Gemini, and Claude in English and Polish on medical examinations. Scientific Reports 15, 33083. https://doi.org/10.1038/s41598-025-17030-0"
    author: "Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: wójcik-2025-2
    resource: "https://doi.org/10.1038/s41598-025-17030-0"
    title: "Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L. (2025). Comparing the performance of ChatGPT, Gemini, and Claude in English and Polish on medical examinations. Scientific Reports 15, 33083. https://doi.org/10.1038/s41598-025-17030-0"
    author: "Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L."
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# Claude outperformed ChatGPT-4 and Gemini in accuracy on Polish/English medical-dental exam questions in both prompt languages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In Polish prompts, ChatGPT-4 and Gemini were both significantly less effective than Claude at answering exam questions; the Gemini–Claude contrast showed a medium effect size. [→ Wójcik 2025](#wojcik-2025)
`q2 i?` In English prompts, both ChatGPT-4 and Gemini were significantly less effective than Claude; most differences showed a small effect size. [→ Wójcik 2025 (2)](#wojcik-2025-2)

## Evidence

### Wójcik 2025

Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L. (2025). Comparing the performance of ChatGPT, Gemini, and Claude in English and Polish on medical examinations. Scientific Reports 15, 33083. https://doi.org/10.1038/s41598-025-17030-0

`q2 · i?` · `causal · r1`

Contrast analysis of GLMM estimated marginal means (Table 8) comparing chatbots within the Polish prompt language; the article states that with the exception of the Gemini–Claude contrast, where a medium effect size was observed, most differences showed a small effect size. Gemini/Claude OR = 0.27. No standardized effect-size value is printed, so no magnitude is coded.

> "In the case of Polish, ChatGPT-4 achieved significantly better results than Gemini (p < 0.001); however, both chatbots were less effective than Claude (p < 0.001)."

### Wójcik 2025 (2)

Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L. (2025). Comparing the performance of ChatGPT, Gemini, and Claude in English and Polish on medical examinations. Scientific Reports 15, 33083. https://doi.org/10.1038/s41598-025-17030-0

`q2 · i?` · `causal · r?`

Contrast analysis within English prompts (Table 8): ChatGPT-4/Claude OR = 0.44 and Gemini/Claude OR = 0.43, both p < 0.001; the article reports "Most differences showed a small effect size" without printing standardized values. ChatGPT-4 and Gemini did not differ significantly in English (p = 0.808).

> "The contrast analysis showed that both ChatGPT-4 and Gemini were less effective compared to Claude (p < 0.001)."

## Discussion


## Related Claims
- [Chatbot accuracy differences across dental specialties emerged mainly in Polish prompts, notably in periodontology and conservative dentistry](specialty-accuracy-differences-strongest-in-polish.md) — a narrower finding that bears on this claim
- [Only Gemini showed significantly higher accuracy in English than in Polish prompts](gemini-accuracy-lower-in-polish-prompts.md) — related
- [GPT-4 achieves the highest pooled accuracy among LLMs (81%), significantly outperforming GPT-3.5 (60%)](gpt4-highest-accuracy-81-outperforms-gpt35.md) — related
- [Accuracy rates differ significantly among ChatGPT, Claude, and Gemini on text-based endodontic examination questions](llm-accuracy-differs-endodontic-exam-questions.md) — reports the opposite
- [Chatbot answers showed only moderate cross-language agreement and imperfect consistency across repeated measurements](chatbot-response-consistency-varies-by-language-and-measurement.md) — related
- [Only Claude would have passed the LDEK/LDEW pass threshold on every attempt, while Gemini in Polish would certainly fail](only-claude-passes-ldek-threshold-every-attempt.md) — related
- [The article reports that GPT-4 outperformed GPT-3.5 on biochemistry MCQs, but contradicts a prior clinical-exam study by finding Claude, not GPT-4, was the most proficient chatbot for biochemistry](gpt-4-superior-to-gpt-35-but-not-best-in-biochemistry.md) — related
