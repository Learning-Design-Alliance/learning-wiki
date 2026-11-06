---
type: design
id: chatgpt-persona-prompt-template-clinical-cases
title: Structured prompt template with persona pattern and predefined case framework for generating clinical cases with MCQs
description: "A three-step prompting template (Table 1) for generating clinical cases with MCQs: (1) setting the role via a persona pattern — \"You are an ophthalmology teacher well-versed in undergraduate medical education\"; (2) sp..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
sources:
  - id: zhang-qi-2025
    resource: "https://doi.org/10.1186/s12909-025-08085-8"
    title: "Zhang Qi, Huang Zijing, Huang Yuqiang, Wang Geng, Zhang Riping, Yang Jianling, Cheng Yinglin, Chen Binyao, Wang Hongxi, Qiu Kunliang, Chen Haoyu. (2025). Generative AI in medical education: feasibility and educational value of LLM-generated clinical cases with MCQs. BMC Medical Education. https://doi.org/10.1186/s12909-025-08085-8"
    author: Zhang Qi, Huang Zijing, Huang Yuqiang, Wang Geng, Zhang Riping, Yang Jianling, Cheng Yinglin, Chen Binyao, Wang Hongxi, Qiu Kunliang, Chen Haoyu
---

# Structured prompt template with persona pattern and predefined case framework for generating clinical cases with MCQs

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A three-step prompting template (Table 1) for generating clinical cases with MCQs: (1) setting the role via a persona pattern — "You are an ophthalmology teacher well-versed in undergraduate medical education"; (2) specifying output as a clinical case with the selected disease and MCQs on diagnosis and differential diagnosis for undergraduates; (3) requesting supplementary imaging data if applicable. It was used to generate twelve cases spanning twelve syllabus chapters.

## Design Implications

### Context
#### Requirements
- Using the disease name directly as the keyword, which the authors report enabled more precise, syllabus-aligned generation than generic symptom keywords.
#### Constraints
- Initial symptom-based keywords (e.g., "sudden painless vision loss") produced cases with low alignment with the teaching syllabus requirements.

### Target Learners
- Undergraduate medical students
- Medical educators constructing case-based learning materials

### Learning Goals
- Diagnostic reasoning
- Knowledge application in clinical case format

### Claims
- [Chatgpt Cases Mean Quality Score 52 33](../claims/chatgpt-cases-mean-quality-score-52-33.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zhang Qi, Huang Zijing, Huang Yuqiang, Wang Geng, Zhang Riping, Yang Jianling, Cheng Yinglin, Chen Binyao, Wang Hongxi, Qiu Kunliang, Chen Haoyu. (2025). Generative AI in medical education: feasibility and educational value of LLM-generated clinical cases with MCQs. BMC Medical Education. https://doi.org/10.1186/s12909-025-08085-8
