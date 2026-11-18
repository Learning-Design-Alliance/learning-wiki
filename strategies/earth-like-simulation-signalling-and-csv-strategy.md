---
type: strategy
id: earth-like-simulation-signalling-and-csv-strategy
title: Signal that a live simulation is running and provide downloadable data for classroom activities
description: Based on questionnaire feedback, the Earth-Like team made design changes to increase engagement and classroom usability.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: elizabeth-j-tasker-2020
    resource: "https://arxiv.org/abs/2001.01438"
    title: "Elizabeth J. Tasker, Kana Ishimaru, Nicholas Guttenberg and Julien Foriel. (2020). Earth-Like: An education & outreach tool for exploring the diversity of planets like our own. https://arxiv.org/abs/2001.01438"
    author: Elizabeth J. Tasker, Kana Ishimaru, Nicholas Guttenberg and Julien Foriel
---

# Signal that a live simulation is running and provide downloadable data for classroom activities

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
Based on questionnaire feedback, the Earth-Like team made design changes to increase engagement and classroom usability. The form submit button was changed to read 'simulating your planet...' when pressed, and a splash animation was added, because feedback "suggested users were more engaged when they knew they were running a simulation, rather than accessing a ﬁnite set of pre-calculated options". A .csv file of the simulation data was made available for five minutes after creation so classroom activities could have students plot different planet models alongside one another.

## Design Implications

### Context
#### Requirements
- A webserver that cannot store data long-term without significant disc space, hence the five-minute availability window for the .csv file
#### Constraints
- The .csv is deleted from the server five minutes after creation; the splash bar addresses but does not eliminate the short delay from running the climate model and creating plots and images

### Target Learners
- school students in classroom settings
- general public users

### Target Learning Goals
- plotting and comparing planet model outputs
- understanding that a real simulation is being run

## Claims

- [A user survey suggests Earth-Like successfully communicates that minor changes in planetary properties can strongly impact the surface environment](../claims/earth-like-survey-communicates-planet-diversity.md) [+W]
- [Students rated the game positively, most often citing fun/interactive features, visuals, and new information learned](../claims/losing-the-lake-positive-student-feedback.md) [+W]
- [High school students did poorest on the 'Earth 2.0' comprehension question, with the majority still judging such a planet likely habitable](../claims/earth-like-high-school-earth2point0-misconception.md) [+W]

## Related Strategies

- [Embed Earth-Like in a structured lesson for school classes](earth-like-structured-lesson-for-schools.md)
- [Design outreach experiments to be easily repeatable so teachers can incorporate them into their own lessons, and keep teachers central to the activities](repeatable-experiments-teachers-central-outreach.md)

## Examples
-

## Key Sources
- Elizabeth J. Tasker, Kana Ishimaru, Nicholas Guttenberg and Julien Foriel. (2020). Earth-Like: An education & outreach tool for exploring the diversity of planets like our own. https://arxiv.org/abs/2001.01438
