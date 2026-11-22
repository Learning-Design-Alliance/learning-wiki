---
type: product
id: studychat-dataset
title: StudyChat dataset
description: StudyChat is a publicly available dataset released by Menggian Wu and collaborators containing naturalistic undergraduate student–LLM programming dialogues linked to assignment submissions.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# StudyChat dataset

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 3 studies (3 associational), `q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
StudyChat is a publicly available dataset released by Menggian Wu and collaborators containing naturalistic undergraduate student–LLM programming dialogues linked to assignment submissions.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **StudyChat dataset of student–LLM conversations in AI and computer science coursework**: StudyChat records student interactions with an LLM-based chatbot during Fall 2024 and Spring 2025, with each record containing a student prompt, the LLM response, and conversation, student, assignment, and interaction-order identifiers. The article reports that "The corpus contains 2,214 conversations from 203 students completing 7 course assignments in artificial intelligence and computer science", comprising 16,851 student utterances with a mean of 7.6 student turns per conversation (median = 4). The conversation is the sampling unit and released normalized assignment grades serve as measures of assessed performance. (Jorge Fábrega (2026))
- **StudyChat and SWE-Chat human-AI collaboration conversation datasets**: The paper evaluates PTA on two real-world conversation corpora. StudyChat is "a collection of conversations between students and an LLM tutor in a university programming-based artificial intelligence course," with 1,540 sessions by 171 students across two semesters and exam scores as outcomes. SWE-Chat is "a collection of conversations between professional developers and AI-powered coding agents working on real software repositories," with 2,774 sessions from developers with at least two sessions and a per-session success signal as outcome. The two settings let the authors compare shared and setting-specific structure in effective LLM use. (Hunter McNichols et al. (2026))
- **StudyChat: a public dataset of annotated student–LLM tutoring dialogues from a university AI course**: StudyChat is a publicly available dataset capturing real-world student interactions with an LLM-powered tutoring chatbot deployed in a semester-long, university-level artificial intelligence course. The authors deployed a web application replicating ChatGPT's core functionalities and logged interactions while students worked on Python programming assignments. It contains 2,214 conversations from 203 students totaling 16,851 utterances, plus 924 graded assignment submissions, all annotated with dialogue act labels and filtered for PII. (The StudyChat Dataset: Analyzing Student Dialogues With ChatGPT in an Artificial Intellige)
- **StudyChat dataset of naturalistic LLM tutoring conversations with LLM-annotated confusion windows**: StudyChat is a publicly available HuggingFace dataset of conversation logs from a GPT-4o mini tutoring assistant deployed in COMPSCI 383, an undergraduate AI course at the University of Massachusetts Amherst. The article states "The final dataset contained 16,851 user -AI interactions from 203 unique users across 2,214 conversations." The authors annotated each interaction with a locally hosted Gemma 4 model across six binary labels and constructed 1,718 confusion windows pairing an AI response with the student's next turn. (Shayla Sharmin et al. (2026))
- **StudyChat dataset of student-ChatGPT programming tutoring conversations**: StudyChat is "a public dataset of real student dialogues with ChatGPT in a university-level artificial intelligence course", collected longitudinally across Fall 2024 and Spring 2025 over 15 weeks of seven Python-based programming assignments. It includes interactions from 203 consenting students across 2,214 conversations, which this study transformed into 16,851 assistant-response interaction rows. LLM-assisted annotation with Gemma 4 achieved "82% agreement with the LLM-assisted labels, and Cohen's kappa was 0.74" against two human authors. (Mohammad Fahim Abrar et al. (2026))

### Claims

- [78.8% of student-GenAI turns lack mastery-oriented aims and reliable epistemic strategies](../claims/low-epistemic-engagement-788-percent-non-mastery.md) [+M]
- [Direction is observable in nearly all AI-mediated conversations, while Integration and Evaluation become progressively more observable as conversation length increases](../claims/direction-nearly-universal-integration-evaluation-rise-with-length.md) [+M]
- [Assignment scores do not distinguish conversations in which all three observable dimensions appear from those in which at least one is not observed](../claims/no-stable-score-difference-by-die-coverage.md) [+M]
- [PTA traits show stronger statistical explanatory power than dialogue-act and Bloom's taxonomy coded baselines on StudyChat](../claims/pta-traits-beat-dialogue-act-bloom-baselines.md) [~W]
- [Trait-score trajectories over time are inconclusive as learning-curve evidence: one StudyChat trait increases while the significant SWE-Chat traits stay flat](../claims/trait-temporal-trends-inconclusive-learning-curves.md) [~W]

## Related Products and Programmes

- [Open dataset of student-chatbot interaction logs, code snapshots, and knowledge and self-regulation measures](open-dataset-of-student-chatbot-interaction-logs-code-snapshots-and-knowledge-and-self-reg.md)
- [NCTE Transcript dataset](ncte-transcript-dataset.md)
- [Released dataset of lesson logs, tutor responses, human annotation rubrics, and generative AI prompts](released-dataset-of-lesson-logs-tutor-responses-human-annotation-rubrics-and-generative-ai.md)

## Key Sources
- Menggian Wu. (2026). Constructing Epistemic AI Literacy: Detecting Epistemic Aims and Processes in Student-AI Co-Programming. 2nd International Workshop on AI Literacy Education For All (ALIT4ALL 2026), co-located with AIED 2026, Seoul, Republic of Korea.
- Jorge Fábrega. (2026). Same Performance, Different Process: Epistemic Ownership in AI-Mediated Education. Preprint. https://arxiv.org/abs/2610.02731
- Hunter McNichols, Kai Du, Andrew Lan. (2026). PRINCIPAL TRAIT ANALYSIS: TOWARDS DERIVING "SKILLS" IN HUMAN-AI COLLABORATION. A preprint - August 13, 2026. https://arxiv.org/abs/2608.11460
- Hunter McNichols, Fareya Ikram, and Andrew Lan. 2026. The StudyChat Dataset: Analyzing Student Dialogues With ChatGPT in an Artificial Intelligence Course. In LAK26: 16th International Learning Analytics and Knowledge Conference (LAK 2026). https://doi.org/10.1145/3785022.3785029
- Shayla Sharmin, Mohammad Fahim Abrar, Roghayeh Leila Barmaki. (2026). Micro-level AI Feedback Features and Student Responses in Consecutive LLM Tutoring Interactions. https://huggingface.co/datasets/wmcnicho/StudyChat
- Mohammad Fahim Abrar, Shyala Sharmin, and Roghayeh Leila Barmaki. (2026). When LLM Tutoring Responses Work: Evidence from Student Programming Conversations. arXiv preprint. https://arxiv.org/abs/2607.09919
