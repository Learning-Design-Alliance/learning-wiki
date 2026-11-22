---
type: design
id: rag-textbook-slackbot-astro17
title: "RAG-encoded textbook Slackbot for course Q&A"
description: A Slack channel bot deployed in the Fall 2025 Astro 17 course to answer student questions using a retrieval-augmented cosmology textbook rather than model training data.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: stubbs-2025
    resource: "https://github.com/astrostubbs/harvard-astro17-labs"
    title: "Stubbs, C. W., Huang, D., Koh, J., Woods, M., & Plazas Malagón, A. A. (2025). Lessons Learned from Integrating Generative AI into an Introductory Undergraduate Astronomy Course at Harvard. https://github.com/astrostubbs/harvard-astro17-labs"
    author: "Stubbs, C. W., Huang, D., Koh, J., Woods, M., & Plazas Malagón, A. A"
---

# RAG-encoded textbook Slackbot for course Q&A

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A Slack channel bot deployed in the Fall 2025 Astro 17 course to answer student questions using a retrieval-augmented cosmology textbook rather than model training data. It was built with API calls to OpenAI's Assistants API using the gpt-4.1 model with File Search enabled, as a Node.js application. "The bot consists of three primary modules: (1) a Textbook Bot that handles Q&A using the OpenAI Assistants API with the cosmology textbook uploaded as a searchable knowledge base", plus a Vision Bot for image-extracted questions and a Summary Bot for activity summaries. Its prompt enforced textbook citation, suppressed chatbot affect, and aimed at "obsolescence by mastery".

## Design Implications

### Context
#### Requirements
- Upload of authoritative course materials (the textbook PDF) as persistent context so responses draw on the textbook rather than training data
#### Constraints
- Students did not make extensive use of this tool; the authors speculate reluctance to ask questions in a shared public space rather than privately

### Target Learners
- introductory undergraduate astrophysics students

### Learning Goals
- supporting active reading of the textbook and answering course content questions

### Claims
- [Gai Utility Ranked Task Focused Work Highest](../claims/gai-utility-ranked-task-focused-work-highest.md) [~M]

## Related Designs

- [Markdown textbook with Wiki RAG and custom structural tags](nupad-markdown-textbook-wiki-rag.md)

## Examples
-

## Key Sources
- Stubbs, C. W., Huang, D., Koh, J., Woods, M., & Plazas Malagón, A. A. (2025). Lessons Learned from Integrating Generative AI into an Introductory Undergraduate Astronomy Course at Harvard. https://github.com/astrostubbs/harvard-astro17-labs
