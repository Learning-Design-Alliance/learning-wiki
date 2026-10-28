---
type: product
id: ai-math-personalization-tool-ampt
title: A.I. Math Personalization Tool (AMPT)
description: A generative-AI system developed by Norberg et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# A.I. Math Personalization Tool (AMPT)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 causal, 1 design), `q2`–`q3` · 1 of 2 report an effect size · 3 claims rest on one study

## Description
A generative-AI system developed by Norberg et al. that guides students in co-authoring culturally relevant mathematics word problems aligned with target pedagogical standards.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **AMPT: an AI tool that lets students co-author culturally relevant math word problems**: The A.I. Math Personalization Tool (AMPT) is a generative-AI system built "to enhance cultural relevance in math word problems by giving students agency over the content." It "leverages generative AI to directly engage students as co-authors of math word problems": through scaffolded conversations students provide the context for a problem, and the AI integrates that context with the pedagogical standards of a target learning domain. Co-authored problems have been delivered to students using MATHia for additional testing. (Norberg et al. (2025))
- **GAI-based web application for real-time context-personalized math learning material and tasks**: A self-developed, Docker-containerized Django web application through which primary students answered GAI-generated math word problems on school iPads. Student interests were captured free-form, and content was generated via the OpenAI API with a self-hosted Llama 3 fallback; Celery and Redis delegated generation to background workers so "students were not required to wait for the generation of educational content". The tool was used to run the classroom experiment and, per the authors, requires only a browser-capable device and internet connection. (Osman Tasdelen (2025))

### Claims
- [A single 30-minute session co-authoring math word problems with AMPT significantly increased students' sense of belonging in mathematics](../claims/ampt-session-increased-math-belonging.md) [+M]
- [Context-personalized AI-generated learning material increases primary students' intrinsic motivation and interest compared with standard material](../claims/gai-personalized-material-motivation-interest.md) [+M]
- [Solving context-personalized AI-generated tasks yields higher learning performance than solving standard tasks](../claims/gai-personalized-tasks-learning-performance.md) [+M]

## Related Products and Programmes

- [Waterproof](waterproof.md)

## Key Sources
- Norberg, K., Murphy, A., De Ley, L., Moltz, E.S., Almoubayyed, H., Ritter, S. (2025). Using Generative AI to Foster Student Sense of Belonging in Mathematics. In: Artificial Intelligence in Education, AIED 2025, Lecture Notes in Computer Science, vol 15882. Springer, Cham. https://doi.org/10.1007/978-3-031-98465-5_24
- Osman Tasdelen, Daniel Bodemer. (2025). Generative AI in the Classroom: Effects of Context-Personalized Learning Material and Tasks on Motivation and Performance. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00491-9
