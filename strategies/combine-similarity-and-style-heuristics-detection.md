---
type: strategy
id: combine-similarity-and-style-heuristics-detection
title: Combine similarity detection using pre-generated AI answers with automatic application of instructor code-style heuristics to improve AI-code detection
description: "The article recommends improving AI-code detection by combining multiple methods rather than relying on any single detector: using similarity systems with pre-generated AI answers for comparison, plus automatic applic..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: kevin-wang-2023
    resource: "https://arxiv.org/abs/2311.16292"
    title: "Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. https://arxiv.org/abs/2311.16292"
    author: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
---

# Combine similarity detection using pre-generated AI answers with automatic application of instructor code-style heuristics to improve AI-code detection

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends improving AI-code detection by combining multiple methods rather than relying on any single detector: using similarity systems with pre-generated AI answers for comparison, plus automatic application of the style heuristics instructors use. It states "there may be opportunities to increase performance by combining multiple methods of similarity detection utilizing pre-generated AI answers for comparison and automatic application of code style heuristics utilized by instructors." Future work also suggests examining a student's submission history for submissions beyond their skill level.

## Design Implications

### Context
#### Requirements
- Requires a labeled set of pre-generated AI answers for each question, which the article notes may not always be practical to provide
#### Constraints
- Detection accuracy is expected to be lower if students use ChatGPT 4 or other systems, vary prompts, or modify/obfuscate output, and the problem will continually evolve given rapid improvement of generative AI

### Target Learners
- post-secondary computer science course instructors and teaching assistants

### Target Learning Goals
- detecting AI-generated assessment submissions to protect academic integrity

## Claims

- [Similarity-based detection of AI-generated code (MOSS, JPlag) is weak when few submissions are AI-generated and significantly more accurate when AI submissions reach 50%](../claims/similarity-detection-depends-on-ai-submission-rate.md) [+W]
- [GPTZero, an AI detector built for writing, fails to detect AI-generated code, assigning AI solutions lower suspicion scores than human solutions](../claims/gptzero-fails-ai-generated-code.md) [+W]
- [Instructors and teaching assistants detect AI-generated code with only 69% accuracy and a 22% false positive rate, with large variability between raters](../claims/instructor-ai-detection-insufficient.md) [+W]

## Related Strategies

- [Protect AI-mediated assessment through isolated environments, clear guidelines, resilience assessments, and teaching prompt-processing awareness](protect-ai-grading-from-prompt-injection-strategies.md)
- [Provisional assessment-defence strategies: question styles AI struggles with, pre-approval open-book exams, and routine AI-capability monitoring](provisional-ai-assessment-defence-strategies.md)

## Examples
-

## Key Sources
- Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. https://arxiv.org/abs/2311.16292
