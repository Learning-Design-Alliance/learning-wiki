---
type: design
id: gpt3-assisted-isomorphic-problem-bank-procedure
title: A five-step generative-AI-assisted procedure for creating isomorphic problem banks using GPT-3, Inkscape and Wolfram Alpha
description: "The article describes a five-step workflow for building isomorphic problem banks: a human expert writes and reviews a seed problem; experts decide acceptable isomorphic variations at three hierarchical levels; SVG fig..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: zhongzhou-chen-2023
    resource: "https://platform.openai.com/playground"
    title: "Zhongzhou Chen, Emily Frederick, Colleen Cui, Munaimah Khan, Christopher Klatt, Mercedith Huang, Shiyang Su. (2023). Reforming Physics Exams Using Openly Accessible Large Isomorphic Problem Banks created with the assistance of Generative AI: an Explorative Study. https://platform.openai.com/playground"
    author: Zhongzhou Chen, Emily Frederick, Colleen Cui, Munaimah Khan, Christopher Klatt, Mercedith Huang, Shiyang Su
---

# A five-step generative-AI-assisted procedure for creating isomorphic problem banks using GPT-3, Inkscape and Wolfram Alpha

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article describes a five-step workflow for building isomorphic problem banks: a human expert writes and reviews a seed problem; experts decide acceptable isomorphic variations at three hierarchical levels; SVG figures are created and edited with the free open-source tool Inkscape; GPT-3 in completion mode generates problem text via one-shot and few-shot prompting; and Wolfram Alpha computes correct symbolic or numeric answers. The article reports that "The estimated cost for generating all the problem text used in this study is less than $1", and that all created problems are stored in a JSON file format and uploaded to a Github repository.

## Design Implications

### Context
#### Requirements
- Human content experts write and review the seed problem and decide which variations are acceptable as isomorphic
- Access to GPT-3, Inkscape, and Wolfram Alpha, with problems stored in a JSON file format
#### Constraints
- The procedure requires significantly more human input at every step than fully automatic generation attempts, which the authors argue reduces LLM hallucination errors and enables correction of biases

### Target Learners
- college introductory-level calculus-based physics students

### Learning Goals
- assessing problem-solving on targeted physics learning outcomes such as static friction and energy conservation

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Zhongzhou Chen, Emily Frederick, Colleen Cui, Munaimah Khan, Christopher Klatt, Mercedith Huang, Shiyang Su. (2023). Reforming Physics Exams Using Openly Accessible Large Isomorphic Problem Banks created with the assistance of Generative AI: an Explorative Study. https://platform.openai.com/playground
