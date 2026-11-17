---
type: product
id: the-tutor-web
title: the tutor-web
description: An open-source, freely accessible AIWBES platform developed for modular university mathematics and statistics instruction through adaptive multiple-choice drilling.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-29
---

# the tutor-web

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 3 studies (1 causal, 1 associational, 1 design), `q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
An open-source, freely accessible AIWBES platform developed for modular university mathematics and statistics instruction through adaptive multiple-choice drilling.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Mobile tutor-web: an adaptive, off-line-capable mobile drilling system for mathematics and statistics**: A freely available mobile website providing educational material and drilling on mathematics and statistics topics, emphasising tablets and mobile phones. The drill interface runs entirely on the student's device using HTML and JavaScript and uses AppCache and LocalStorage so it "can even work without any Internet connection". Questions are selected based on the student's current grade, answers are timed with a countdown timer, and step-by-step explanations follow each answer. The server is based on the Plone CMS and MySQL, and the system adapts to student performance based on statistical models of data from prior testing. (Jamie Lentin et al. (2014))
- **Grading scheme combining an inverse-dome timeout with a lengthening taper of recent answers to reflect expertise rather than guessing**: The mobile tutor-web's grading mechanism addresses two failure modes of earlier versions: students guessing their way to an adequate grade, and students quitting after a single error following a run of correct answers. A timeout in the shape of an inverse dome curve is set so that "beginning or struggling students do not get affected by the timeout", while students cannot reach a high grade without passing through the timeout set at intermediate-level grades. The grade is an average of recent responses whose tail gets longer (n/2) as responses n increase above 16, up to a maximum of 30 questions in the grade, so that extended guessing produces a longer tail. The behaviour is controlled by parameters whose effects can be estimated statistically. (Jamie Lentin et al. (2014))
- **The tutor-web open educational system**: The tutor-web (http://tutor-web.net) is a free, open-source web-based educational system built in Plone on the Zope Application Server, with teaching material licensed under the Creative Commons Attribution-ShareAlike License. Material is organized into a tree of departments, courses, tutorials, lectures, and slides, with quiz questions linked to every lecture. Its quizzes have "the primary purpose of increasing learning rather than mere evaluation," and grading uses only the last eight questions answered per lecture. It was used for computer-assisted education in statistics and mathematics, including the 2011 experiment reported here. (Anna Helga Jonsdottir (2013))

### Claims
- [Classical IRT models without learning terms do not fit tutor-web drill data; a logistic model with numseen and attempt terms is needed](../claims/irt-models-fail-learning-environment-fitted-logistic-model.md) [+W]
- [Revised mobile-web grading (timeout plus longer variable taper) shows a clearer relationship between tutor-web grade and final exam grade than the earlier fixed-taper system in the grade range 6-9](../claims/timeout-taper-grading-better-predicts-exam.md) [+M]
- [Students reported positive experience with the tutor-web: 92% said they learned from it, but 82% preferred a mixture of tutor-web and written homework](../claims/tutor-web-student-survey-positive-mixed-preference.md) [+M]

## Related Products and Programmes

- [Open-source modular AI math tutoring platform](open-source-modular-ai-math-tutoring-platform.md)

## Key Sources
- Anna Helga Jonsdottir, Gunnar Stefansson. (2014). From evaluation to learning: Some aspects of designing a cyber-university. https://arxiv.org/abs/1310.5552
- Jamie Lentin, Anna H. Jonsdottir, David Stern, Victoria Mokua, Eva Dogg Steingrimsdottir, Magnea Run Vignisdottir and Gunnar Stefansson. (2014). A MOBILE WEB FOR ENHANCING STATISTICS AND MATHEMATICS EDUCATION. http://mobile.tutor-web.net
- Anna Helga Jonsdottir, Gunnar Stefansson. (2013). Enhanced Learning with Web-Assisted Education. https://arxiv.org/abs/1310.4667
