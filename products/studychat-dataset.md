---
type: product
id: studychat-dataset
title: StudyChat dataset
description: StudyChat is a publicly available dataset released by Menggian Wu and collaborators containing naturalistic undergraduate student–LLM programming dialogues linked to assignment submissions.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# StudyChat dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
StudyChat is a publicly available dataset released by Menggian Wu and collaborators containing naturalistic undergraduate student–LLM programming dialogues linked to assignment submissions.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **StudyChat dataset of student–LLM conversations in AI and computer science coursework**: StudyChat records student interactions with an LLM-based chatbot during Fall 2024 and Spring 2025, with each record containing a student prompt, the LLM response, and conversation, student, assignment, and interaction-order identifiers. The article reports that "The corpus contains 2,214 conversations from 203 students completing 7 course assignments in artificial intelligence and computer science", comprising 16,851 student utterances with a mean of 7.6 student turns per conversation (median = 4). The conversation is the sampling unit and released normalized assignment grades serve as measures of assessed performance. (Jorge Fábrega (2026))
- **StudyChat and SWE-Chat human-AI collaboration conversation datasets**: The paper evaluates PTA on two real-world conversation corpora. StudyChat is "a collection of conversations between students and an LLM tutor in a university programming-based artificial intelligence course," with 1,540 sessions by 171 students across two semesters and exam scores as outcomes. SWE-Chat is "a collection of conversations between professional developers and AI-powered coding agents working on real software repositories," with 2,774 sessions from developers with at least two sessions and a per-session success signal as outcome. The two settings let the authors compare shared and setting-specific structure in effective LLM use. (Hunter McNichols et al. (2026))

### Claims
- [78.8% of student-GenAI turns lack mastery-oriented aims and reliable epistemic strategies](../claims/low-epistemic-engagement-788-percent-non-mastery.md) [+M]
- [Direction is observable in nearly all AI-mediated conversations, while Integration and Evaluation become progressively more observable as conversation length increases](../claims/direction-nearly-universal-integration-evaluation-rise-with-length.md) [+M]
- [Assignment scores do not distinguish conversations in which all three observable dimensions appear from those in which at least one is not observed](../claims/no-stable-score-difference-by-die-coverage.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Menggian Wu. (2026). Constructing Epistemic AI Literacy: Detecting Epistemic Aims and Processes in Student-AI Co-Programming. 2nd International Workshop on AI Literacy Education For All (ALIT4ALL 2026), co-located with AIED 2026, Seoul, Republic of Korea.
- Jorge Fábrega. (2026). Same Performance, Different Process: Epistemic Ownership in AI-Mediated Education. Preprint. https://arxiv.org/abs/2610.02731
- Hunter McNichols, Kai Du, Andrew Lan. (2026). PRINCIPAL TRAIT ANALYSIS: TOWARDS DERIVING "SKILLS" IN HUMAN-AI COLLABORATION. A preprint - August 13, 2026. https://arxiv.org/abs/2608.11460
