---
type: design
id: gpt3-chatbot-tutor-pedagogical-preprompt
title: GPT-3-based chatbot tutor with instructor-designed pedagogical pre-prompt
description: A GPT-3-based chat interface serving as a chatbot tutor in both studies.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: harsh-kumar-2024
    resource: "https://doi.org/10.1145/3687038"
    title: "Harsh Kumar, Ilya Musabirov, Mohi Reza, Jiakai Shi, Xinyuan Wang, Joseph Jay Williams, Anastasia Kuzminykh, and Michael Liut. 2024. Impact of Guidance and Interaction Strategies for LLM Use on Learner Performance and Perception. Proc. ACM Hum.-Comput. Interact. 8, CSCW2, Article 499 (November 2024). https://doi.org/10.1145/3687038"
    author: Harsh Kumar, Ilya Musabirov, Mohi Reza, Jiakai Shi, Xinyuan Wang, Joseph Jay Williams, Anastasia Kuzminykh, and Michael Liut
---

# GPT-3-based chatbot tutor with instructor-designed pedagogical pre-prompt

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A GPT-3-based chat interface serving as a chatbot tutor in both studies. In the classroom deployment, the model prompt, designed with the instructor and teaching assistant, instructed that "The instructor never explicitly gives the solution" and "never writes the SQL query," providing only brainstorms. In Study 2, a pre-prompted variant framed the model as "a professional K12 math teacher helping students answer math questions," instructed to give explanations, examples, and analogies and to reflect on whether answers support learning, confidence, and trust. An unprompted variant served as the control.

## Design Implications

### Context
#### Requirements
- A carefully iterated system prompt designed with instructors to steer response style
#### Constraints
- The prompted vs. unprompted contrast was only possible in the online controlled setting; the classroom used only the prompted tutor

### Target Learners
- undergraduate computer science students
- adult crowdworkers

### Learning Goals
- solving database assignment problems
- solving elementary and high-school math problems

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Harsh Kumar, Ilya Musabirov, Mohi Reza, Jiakai Shi, Xinyuan Wang, Joseph Jay Williams, Anastasia Kuzminykh, and Michael Liut. 2024. Impact of Guidance and Interaction Strategies for LLM Use on Learner Performance and Perception. Proc. ACM Hum.-Comput. Interact. 8, CSCW2, Article 499 (November 2024). https://doi.org/10.1145/3687038
