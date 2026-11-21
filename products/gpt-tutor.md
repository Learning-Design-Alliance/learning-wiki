---
type: product
id: gpt-tutor
title: GPT Tutor
description: GPT Tutor is a GPT-4 chat-based mathematics tutoring interface developed and studied by Bastani Hamsa et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# GPT Tutor

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 3 studies (2 causal, 1 design), `q2`–`q3` · 1 of 3 report an effect size · 5 claims rest on one study

## Description
GPT Tutor is a GPT-4 chat-based mathematics tutoring interface developed and studied by Bastani Hamsa et al. that uses teacher-provided solutions, misconceptions, and hints to support high-school students' practice without directly giving answers.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **GPTutor: an LLM-powered tutoring system integrating a structured proof-review tool and a conversational chatbot**: GPTutor is an LLM-powered tutoring system for undergraduate discrete mathematics that integrates "a structured proof-review tool and a conversational chatbot." The proof-review component provides high-level feedback and localized comments highlighting specific problematic segments, supports only structured feedback without open-ended dialogue, and requires students to produce a proof attempt before receiving feedback. The chatbot (GPT-4o) supports conversational math-focused dialogue with a system prompt instructing Socratic questioning and partial hints rather than direct answers. (Chen et al. (2026))

### Claims
- [A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performance more than a standard GPT-4 interface](../claims/gpt-tutor-improves-practice-more-than-gpt-base.md) [+M]
- [Guardrails in the GPT Tutor largely eliminate the negative exam effect, though no positive exam effect is observed](../claims/gpt-tutor-exam-effect-null.md) [+M]
- [GPT-generated tutor feedback is predominantly positive or neutral in sentiment](../claims/gpt-feedback-predominantly-positive-sentiment.md) [~W]
- [Earlier access to GPTutor was associated with higher homework scores but this benefit did not transfer to exam scores](../claims/gptutor-earlier-access-homework-not-exam.md) [+M]
- [Chatbot usage constituted a negative associative pathway to subsequent exam performance, while proof-review usage showed no detectable independent association](../claims/chatbot-usage-negative-pathway-exam.md) [~M]

## Related Products and Programmes
-

## Key Sources
- Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2422633122
- Chen, E., Judicke, S., Beigh, K., Tang, X., Wang, Y., Yuan, M., Xiao, Z., Li, C., Li, S., Luttmer, R., Singh, S., Yampolsky, M., Parikh, N., Zhao, Y., Chen, M., Huang, C., Mohanty, A., Johnson, G., Mackey, J., Lin, J., & Koedinger, K. (2026). Chat-Based Support Alone May Not Be Enough: Comparing Conversational and Embedded LLM Feedback for Mathematical Proof Learning. arXiv. https://arxiv.org/abs/2602.18807
