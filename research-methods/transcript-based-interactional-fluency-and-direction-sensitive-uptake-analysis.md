---
type: research-method
id: transcript-based-interactional-fluency-and-direction-sensitive-uptake-analysis
title: Transcript-based interactional fluency and direction-sensitive uptake analysis
description: "A reusable analysis pipeline that operationalizes interactional fluency and direction-sensitive linguistic uptake for spoken AI practice \"using metrics extractable from diarized ASR output without manual linguistic annotation.\" The fluency component extracts seven features from word-level timestamps"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Transcript-based interactional fluency and direction-sensitive uptake analysis

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
A reusable analysis pipeline that operationalizes interactional fluency and direction-sensitive linguistic uptake for spoken AI practice "using metrics extractable from diarized ASR output without manual linguistic annotation." The fluency component extracts seven features from word-level timestamps (conversation length, turn count, mean turn duration, words per turn, response latency, floor ratio, within-turn pause ratio). The uptake component tracks lexical adoption via a global timeline with a first-use, first-source-wins rule, and syntactic uptake via four German morphosyntactic template types parsed with the Stanza UD pipeline, with correctness checked against a 91,270-noun gender lexicon. The authors provide it as "a reusable analysis pipeline for rapid, scalable evaluation of conversational AI in educational settings."

## Accounts
<!-- How each source describes or uses the method -->
- **Transcript-based pipeline for measuring interactional fluency and direction-sensitive uptake from diarized ASR output**: A reusable analysis pipeline that operationalizes interactional fluency and direction-sensitive linguistic uptake for spoken AI practice "using metrics extractable from diarized ASR output without manual linguistic annotation." The fluency component extracts seven features from word-level timestamps (conversation length, turn count, mean turn duration, words per turn, response latency, floor ratio, within-turn pause ratio). The uptake component tracks lexical adoption via a global timeline with a first-use, first-source-wins rule, and syntactic uptake via four German morphosyntactic template types parsed with the Stanza UD pipeline, with correctness checked against a 91,270-noun gender lexicon. The authors provide it as "a reusable analysis pipeline for rapid, scalable evaluation of conversational AI in educational settings." (Russell Scheinberg et al. (2026))

### Claims

- [Learners show stronger short-term syntactic priming with the AI partner, significant across all three recency-window operationalizations including one equalizing input volume](../claims/ai-syntactic-priming-advantage-survives-controls.md) [+W]
- [Lexical adoption shows no significant condition effect after controlling for input volume, but AI-first participants adopted more words at the second dialogue position](../claims/lexical-uptake-no-condition-effect-after-controls.md) [+W]

## Related Research Methods

- [Two-metric turn-level evaluation of chatbot scaffolding and student uptake](two-metric-turn-level-evaluation-of-chatbot-scaffolding-and-student-uptake.md)

## Key Sources
- Russell Scheinberg, Ameeta Agrawal, Tetyana Sydorenko, Kalab Kahsay, Nina Vyatkina, Griet Boone. (2026). What Changes When the Interlocutor Is an AI? Interactional Fluency and Linguistic Uptake in L2 Spoken Dialogue. https://arxiv.org/abs/2606.22225
