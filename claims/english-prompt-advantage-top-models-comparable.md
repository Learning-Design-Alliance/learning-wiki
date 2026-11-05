---
type: claim
title: English prompts generally yield better LLM accuracy than language-matched prompts, but top models perform comparably with language-matched prompts
description: English prompts generally yield better LLM accuracy than language-matched prompts, but top models perform comparably with language-matched prompts
id: english-prompt-advantage-top-models-comparable
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

# English prompts generally yield better LLM accuracy than language-matched prompts, but top models perform comparably with language-matched prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all models, English prompts led to better or comparable performance relative to language-matched prompts (OR 1.81, 95% CI 1.60-2.05; P<.001). [→ Strasser Livia Maria 2026](#strasser-livia-maria-2026)
`q2 i?` The top-performing models GPT4o and Claude-Sonnet-3.7 showed comparable results for language-matched prompts, with slightly lower accuracy for Claude-Sonnet-3.7 particularly in German. [→ Strasser Livia Maria 2026](#strasser-livia-maria-2026)

## Evidence

### Strasser Livia Maria 2026

Strasser Livia Maria, Anschuetz Wilma, Dennstädt Fabio, Hastings Janna. (2026). Performance Evaluation of Large Language Models in Multilingual Medical Multiple-Choice Questions: Mixed Methods Study. JMIR Medical Education. https://doi.org/10.2196/81399

`q2 · i?` · `causal · r2`

GEE comparison of the two prompt scenarios (English vs language-matched system and user instructions) across five LLMs and three question languages. The article reports OR 1.81 (95% CI 1.60-2.05; P<.001) favoring English prompts, while noting Claude-Sonnet-3.7 and GPT4o showed the highest and most consistent accuracy across all prompt types.

> "Across all models, comparing model performance across the 2 prompt scenarios, English prompts generally led to better or comparable performance relative to language-matched prompts (OR 1.81, 95% CI 1.60-2.05; P<.001)."

## Discussion


## Related Claims
- [Students rated Claude-generated Turkish clinical scenarios highest across clarity, realism, and clinical reasoning support](claude-highest-student-ratings-clinical-scenarios.md) — related
- [Claude-Sonnet-3.7 shows a markedly higher frequency of reasoning errors despite factual accuracy than GPT4o in erroneous medical answers](claude-reasoning-errors-despite-factual-accuracy.md) — related
- [LLMs answer diagnosis questions significantly better than treatment questions in medical multiple-choice items](treatment-questions-solved-worse-than-diagnosis.md) — related
- [Any type of prompt significantly improved performance for both GPT-3.5 (68% vs 54%, P=.03) and GPT-4 (85% vs 79%, P<.01)](prompts-improve-chatgpt-exam-accuracy.md) — related
- [LLM accuracy on multilingual medical multiple-choice questions varies substantially by model, with Claude-Sonnet-3.7 highest (87%) and open models lowest (64%-73%)](llm-accuracy-varies-by-model-medical-mcq.md) — a broader claim this one bears on
- [LLM accuracy on medical multiple-choice questions is significantly lower for Italian than German questions, with no significant German-French difference](question-language-effect-german-best-italian-lower.md) — related
