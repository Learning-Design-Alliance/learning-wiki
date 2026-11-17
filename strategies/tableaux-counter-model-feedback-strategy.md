---
type: strategy
id: tableaux-counter-model-feedback-strategy
title: Use tableaux-based theorem provers to generate counter-model feedback on incorrect logic exercise submissions
description: "The authors propose replacing the resolution theorem prover with a tableaux-based prover so that, when a submission is not logically equivalent to the model answer, the tableau procedure's counter model can be shown t..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
sources:
  - id: angelo-kyrilov-and-david-c-noelle-2015
    resource: "https://arxiv.org/abs/1507.03670"
    title: "Angelo Kyrilov and David C. Noelle. (2015). Using Automated Theorem Provers to Teach Knowledge Representation in First-Order Logic. 4th International Conference on Tools for Teaching Logic. https://arxiv.org/abs/1507.03670"
    author: Angelo Kyrilov and David C. Noelle
---

# Use tableaux-based theorem provers to generate counter-model feedback on incorrect logic exercise submissions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The authors propose replacing the resolution theorem prover with a tableaux-based prover so that, when a submission is not logically equivalent to the model answer, the tableau procedure's counter model can be shown to the student. They illustrate with the ProofTools prover: for a typical incorrect solution to "Joe does not have a lawyer," the counter model shows a lawyer the student is not a customer of plus another lawyer Joe retained, information they say "should help a struggling student discover the error that had been made."

## Design Implications

### Context
#### Requirements
- A tableaux-based prover that produces a counter model when the provided sentence is not valid
#### Constraints
- Presented as future work under investigation; the article reports only initial explorations showing promise, not a deployed or evaluated implementation

### Target Learners
- undergraduate students learning first-order logic knowledge representation

### Target Learning Goals
- identifying and correcting errors in one's own logical formalizations of English sentences

## Claims

- [The authors report that instant binary Correct/Incorrect feedback on programming exercises can demotivate beginners and promote cheating](../claims/binary-feedback-demotivation-cheating-concern.md) [+W]
- [Students struggle with constructing axiomatic proofs substantially more than with semantic tableaux in the same logic course](../claims/axiomatic-proofs-harder-than-semantic-tableaux-homework.md) [+W]

## Related Strategies
- Prover9 Automated Grading System Fol

## Examples
-

## Key Sources
- Angelo Kyrilov and David C. Noelle. (2015). Using Automated Theorem Provers to Teach Knowledge Representation in First-Order Logic. 4th International Conference on Tools for Teaching Logic. https://arxiv.org/abs/1507.03670
