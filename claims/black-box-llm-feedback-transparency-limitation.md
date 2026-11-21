---
type: claim
title: Using a black-box LLM for feedback generation limits transparency and explainability
description: Using a black-box LLM for feedback generation limits transparency and explainability
id: black-box-llm-feedback-transparency-limitation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: jieun-han-2024
    resource: "https://doi.org/10.18653/v1/2024.customnlp4u-1.21"
    title: "Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. (2024). LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction. arXiv. Originally published 2023. [doi:10.18653/v1/2024.customnlp4u-1.21](https://doi.org/10.18653/v1/2024.customnlp4u-1.21)"
    author: Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# Using a black-box LLM for feedback generation limits transparency and explainability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The authors state that using ChatGPT, a black-box language model, for feedback generation results in a lack of transparency because it provides no explicit justifications or rationales for the generated feedback. [→ Jieun Han 2024](#jieun-han-2024)

## Evidence

### Jieun Han 2024

Jieun Han, Haneul Yoo, Junho Myung, Minsun Kim, Hyunseung Lim, Yoonsu Kim, Tak Yeon Lee, Hwajung Hong, Juho Kim, So-Yeon Ahn, Alice Oh. (2024). LLM-as-a-tutor in EFL Writing Education: Focusing on Evaluation of Student-LLM Interaction. arXiv. Originally published 2023. [doi:10.18653/v1/2024.customnlp4u-1.21](https://doi.org/10.18653/v1/2024.customnlp4u-1.21)

`q1 · i?` · `causal · r1`

This is the authors' own stated limitation, not a tested result: they report that "a black-box language model" produces feedback without "explicit justifications or rationales", and call for continued research on more explainable feedback models.

> "We utilize ChatGPT, a black-box language model, for feedback generation. This results in a lack of transparency in our system, as it does not provide explicit justifications or rationales for the gener- ated feedback."

## Discussion


## Related Claims
- [The most frequent limitation of AI in instructional design is content reliability and transparency (16 of 28 studies, 57.14%)](ai-id-limitation-content-reliability-transparency.md) — a broader claim this one bears on
- [GPT-4's chain-of-thought reasoning, captured via structured output, was consistently reliable and appeared to provide logical, context-grounded justification usable for prompt tuning and end-user insight](gpt4-cot-reasoning-reliable-transparent.md) — reports the opposite
- [Students report negative experiences with ChatGPT including inaccurate outputs, lack of emotional connection, and risk of overreliance, which constrain competence](chatgpt-negative-experiences-inaccuracy-overreliance.md) — related
- [Large language models can produce fluent but factually inaccurate or fabricated outputs (AI hallucination), posing risks for uncritical users in science education](llm-hallucination-risk-science-education.md) — related
- [GenAI feedback limitations require students to exercise evaluative judgement](genai-limitations-require-evaluative-judgement.md) — related
- [Gen-AI hallucinates sources and values and produces convincing but incorrect explanations, risking student misinformation](genai-hallucination-convincing-incorrect-explanations.md) — related
- [ChatGPT-generated text shows inaccuracy, weak logical flow, lack of critical elaboration and non-originality in an author's first-hand test](chatgpt-output-inaccuracy-nonoriginality.md) — related
- [LLMs support HCXAI in education through natural-language explanations, interactive dialogues, and explained content generation](llms-provide-natural-language-explanations-dialogues-content.md) — reports the opposite
