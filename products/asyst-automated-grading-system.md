---
type: product
id: asyst-automated-grading-system
title: ASYST (Automated Grading System)
description: ASYST is a graphical interface developed by Ulrike Padó and colleagues that lets teachers locally generate and review automated short-answer grading suggestions from Excel files using German or English Transformer models.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# ASYST (Automated Grading System)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (5 for) · 3 studies (2 design, 1 causal), `q2`–`q3` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
ASYST is a graphical interface developed by Ulrike Padó and colleagues that lets teachers locally generate and review automated short-answer grading suggestions from Excel files using German or English Transformer models.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ASYST: an easy-to-use automated grading system with local processing and Excel-based workflow**: ASYST (Automated Grading System) is a graphical user interface wrapping the German Transformer SAG model (and an English model) so that teachers without programming skills can generate automated grade suggestions. It "takes as input an Excel sheet containing student answers and correct reference answers", optionally accepts existing manual grades for reliability analysis, and runs grading locally: "Automated grading is fully local, which precludes data protection issues because the student answers never leave the teacher's computer." Results are saved as an Excel sheet for teacher review. It is released as a compiled Windows 11 executable with open-source Python code. (Ulrike Padó et al. (2024))
- **AI-based automated grading system for R assignments with NLP comment classification**: A tool that automatically grades assignments consisting of R commands and Italian-language comments. It performs static code analysis to extract commands, outputs, and comments, then uses a Python NLP server (fastText embeddings, 300 dimensions) and an R classification engine (CARET/E1071 SVM) to judge comment correctness. The distance calculator module combines missing commands, differing outputs, and comment correctness into a final grade converted to the Italian 0–31 scale. (Pierpaolo Vittorini et al. (2021))
- **Automated grading system for first-order logic knowledge representation exercises using the Prover9 theorem prover**: An online tool in which students translate English sentences into first-order logic given an explicit list of allowed predicates, functions, and constant symbols. Because "there are usually multiple correct solutions to exercises of this kind," submissions are not string-compared; instead, Prover9 checks whether the formula A ⇔ B is valid, where A is the instructor's model answer and B the student's submission. Students receive instant "Correct/Incorrect" judgments with unlimited resubmissions, and a per-exercise server time limit (5 seconds by default) handles the undecidability of first-order logic. (Angelo Kyrilov et al. (2015))

### Claims
- [Six expert teachers completed grading tasks in ASYST with 100% effectiveness, median 2:15 minutes, and an average SUS score of 88.8](../claims/asyst-usability-study-high-sus.md) [+M]
- [Automated grading achieves excellent agreement with human grading (ICC = 0.893)](../claims/automated-grading-excellent-agreement-icc-0893.md) [+M]
- [SVM classifier on sentence embeddings classifies comment correctness with F1 = 0.914 and Cohen's K = 0.764](../claims/svm-embeddings-classify-comments-f1-0914.md) [+M]
- [Automated tool reduces correction time by 43% (raw) and 33% (normalised)](../claims/automated-tool-reduces-correction-time-43-percent.md) [+M]
- [Use of an automated grading system for first-order logic translation exercises was associated with marginally significantly higher aggregate scores on knowledge representation final-examination questions](../claims/automated-grading-system-higher-aggregate-exam-scores.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner. (2024). Short-Answer Grading for German: Addressing the Challenges. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00383-w
- Pierpaolo Vittorini, Stefano Menini, Sara Tonelli. (2021). An AI-Based System for Formative and Summative Assessment in Data Science Courses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00230-2
- Angelo Kyrilov and David C. Noelle. (2015). Using Automated Theorem Provers to Teach Knowledge Representation in First-Order Logic. 4th International Conference on Tools for Teaching Logic. https://arxiv.org/abs/1507.03670
