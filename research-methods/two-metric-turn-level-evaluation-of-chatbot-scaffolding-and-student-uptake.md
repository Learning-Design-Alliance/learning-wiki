---
type: research-method
id: two-metric-turn-level-evaluation-of-chatbot-scaffolding-and-student-uptake
title: Two-metric turn-level evaluation of chatbot scaffolding and student uptake
description: An evaluation pipeline that scores both sides of student-chatbot interactions at the turn level.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Two-metric turn-level evaluation of chatbot scaffolding and student uptake

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An evaluation pipeline that scores both sides of student-chatbot interactions at the turn level. As the article defines them, "We define two turn-levels metrics:Chatbot Scaffoldingas how much scaffolding the chatbot provides andStudent Uptakeas how much the student takes up the scaffolding". GPT-5-mini acts as an ordinal classifier on a 1-5 scale per turn, with turn-level scores aggregated to per-chat means; uptake is mapped onto a signed -1 to +1 scale showing who drives the chat flow. It was applied across nine datasets totalling 9,490 valid chats.

## Accounts
<!-- How each source describes or uses the method -->
- **Two-metric turn-level evaluation pipeline: Chatbot Scaffolding and Student Uptake**: An evaluation pipeline that scores both sides of student-chatbot interactions at the turn level. As the article defines them, "We define two turn-levels metrics:Chatbot Scaffoldingas how much scaffolding the chatbot provides andStudent Uptakeas how much the student takes up the scaffolding". GPT-5-mini acts as an ordinal classifier on a 1-5 scale per turn, with turn-level scores aggregated to per-chat means; uptake is mapped onto a signed -1 to +1 scale showing who drives the chat flow. It was applied across nine datasets totalling 9,490 valid chats. (Neagu et al. (2026))

### Claims
- [The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters](../claims/llm-judge-pipeline-validated-against-human-raters.md) [+M]

## Related Research Methods
-

## Key Sources
- Neagu, A., Wong, J. T. H., Messer, M., Nelson, R., & Johnson, P. B. (2026). Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments. Pluralistic Alignment Workshop @ ICML 2026. https://arxiv.org/abs/2606.15766
