---
type: product
id: ethel
title: Ethel
description: Ethel is an ETH Zurich virtual teaching assistant system combining a course-grounded chatbot, handwritten-homework feedback, and handwritten-exam grading support for university courses.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# Ethel

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Ethel is an ETH Zurich virtual teaching assistant system combining a course-grounded chatbot, handwritten-homework feedback, and handwritten-exam grading support for university courses.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Ethel virtual teaching assistant system (RAG chatbot, homework feedback, exam grading)**: Ethel is a virtual teaching assistant developed at ETH Zurich with three components: a course-specific chatbot, handwritten homework feedback, and exam grading support. Its chatbot "utilizes course-specific materials (typically PDFs) through Retrieval Augmented Generation (RAG)," built with LangChain and OpenAI's ada embeddings, and "this can be implemented in about 400 lines of code." It was deployed across six courses in Spring 2024. (Kortemeyer (2024))
- **Ethel chatbot with on-demand exercise generation and validation pipeline**: Ethel is "a virtual teaching-assistant ecosystem developed at ETH Zurich" that served as the study platform. A mini LLM performs intent detection on user prompts; exercise requests trigger a specialized prompt using RAG over course materials and chat history, generating multiple candidate problems as structured JSON. Client-side JavaScript renders interactive problems and evaluates submitted answers. The study adds a problem-validation step (LLM-as-a-judge) between generation and delivery, which is the focus of the research. (Tobias Geisler et al. (2026))

### Claims
- [Ethel's course-specific chatbot was deployed to over 1500 students across six courses, and a survey found the majority of students found it helpful or very helpful](../claims/ethel-chatbot-deployment-helpfulness.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Kortemeyer, G. (2024). Ethel: A Virtual Teaching Assistant. arXiv. https://arxiv.org/abs/2407.19452. [doi:10.1119/5.0231187](https://doi.org/10.1119/5.0231187)
- Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. https://arxiv.org/abs/2508.03085
