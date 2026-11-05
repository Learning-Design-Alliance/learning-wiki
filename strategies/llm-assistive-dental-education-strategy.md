---
type: strategy
id: llm-assistive-dental-education-strategy
title: Use advanced LLMs as assistive tools in dental education and practice, with comprehensive validation, strict regulation, and human supervision before deployment
description: "The article recommends integrating advanced LLMs into dentistry: in education, they \"could serve as personalized intelligent tutors\" tailored to students' interests and needs and could simulate clinical scenarios to c..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: zhang-jiarui-2025
    resource: "https://doi.org/10.1186/s12903-025-07540-8"
    title: "Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting. (2025). From accuracy to robustness: a comparative study of five advanced large language models on the Chinese dental licensing examination. BMC Oral Health. https://doi.org/10.1186/s12903-025-07540-8"
    author: Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting
---

# Use advanced LLMs as assistive tools in dental education and practice, with comprehensive validation, strict regulation, and human supervision before deployment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The article recommends integrating advanced LLMs into dentistry: in education, they "could serve as personalized intelligent tutors" tailored to students' interests and needs and could simulate clinical scenarios to cultivate clinical reasoning; in practice, they may relieve physician workload and serve as consultants for patients in remote areas. The recommendation rests on the study's benchmark accuracy and robustness findings.

## Design Implications

### Context
#### Requirements
- Models must be validated comprehensively, strictly regulated, and operated under human supervision before real-world deployment, as the article's conclusion states these are mandatory.
#### Constraints
- The assessment was restricted to structured MCQs and excluded image-based questions, so it does not capture dynamic decision-making, patient-physician communication, or procedural contexts; findings reflect only current model versions.

### Target Learners
- Dental students and CDLE candidates
- Dental practitioners
- Patients in remote areas lacking sufficient medical resources

### Target Learning Goals
- Strengthening grasp of basic medical knowledge and skills
- Cultivating clinical reasoning

## Claims

- [GPT-4o significantly lags the other four LLMs on dentistry questions, while in clinical medicine no significant pairwise differences were detected](../claims/cdle-dentistry-gpt4o-lags-subjects.md) [+W]
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](../claims/cdle-four-llms-outperform-gpt4o-overall.md) [+W]
- [New-generation LLMs significantly outperform GPT-4o on knowledge-based question types (A1, B1) but not on case-analysis types (A2, A3/A4)](../claims/cdle-knowledge-vs-case-analysis-question-types.md) [+W]
- [Mainstream non-Chinese LLMs performed comparably to DeepSeek-R1 on the Chinese-language CDLE, suggesting prior linguistic-basis disadvantages have been mitigated](../claims/cdle-language-bias-mitigated-new-generation.md) [~W]
- [All five LLMs show only slight, non-significant accuracy declines under semantic-equivalence and irrelevant-information perturbations, indicating strong robustness](../claims/cdle-llm-robustness-adversarial-perturbations.md) [+W]
- [Across the ten dentistry sub-disciplines, significant model differences appear only in prosthodontics and oral anatomy, where GPT-4o is lowest](../claims/cdle-subdiscipline-prosthodontics-oral-anatomy.md) [+W]

## Related Strategies

- [Integrate AI chatbots into dental education as supervised supplementary tools for exam preparation and formative self-assessment](supervised-chatbot-supplementary-dental-education.md)
- [Integrate AI literacy and critical appraisal skills into dental curricula alongside discipline-specific AI validation](ai-literacy-critical-appraisal-dental-curricula-strategy.md)
- [Frame LLM use in biomedical education around low‐stakes formative tasks with expert‐guided verification and rationale requests](llm-low-stakes-formative-use-expert-verification-strategy.md)

## Examples
-

## Key Sources
- Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting. (2025). From accuracy to robustness: a comparative study of five advanced large language models on the Chinese dental licensing examination. BMC Oral Health. https://doi.org/10.1186/s12903-025-07540-8
