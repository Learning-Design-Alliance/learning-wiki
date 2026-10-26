---
type: strategy
id: kindergarten-screening-early-md-support
title: Use kindergarten-age screening information to identify children at potential risk of math difficulties and provide access to early support
description: "The article recommends transferring prediction models of the kind it validated into school practice: kindergarten measures across arithmetic, cognitive, home-environment, parental, motivational, behavioral, and gender..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-25
sources:
  - id: psyridou-2024
    resource: "https://doi.org/10.1037/edu0000835"
    title: "Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M. (2024). Early prediction of math difficulties with the use of a neural networks model. Journal of Educational Psychology, 116(2), 212-232. https://doi.org/10.1037/edu0000835"
    author: "Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M"
---

# Use kindergarten-age screening information to identify children at potential risk of math difficulties and provide access to early support

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (4 for, 2 mixed) · 2 studies (1 quant-synthesis, 1 associational), `q3` · 1 of 2 report an effect size · 6 claims rest on one study

## Description
The article recommends transferring prediction models of the kind it validated into school practice: kindergarten measures across arithmetic, cognitive, home-environment, parental, motivational, behavioral, and gender domains are entered into a trained model whose output flags children at potential risk, enabling timely support before difficulties consolidate in later grades. The authors state that in a school setting, early prediction results could be used to identify children at potential risk of developing MD and to provide access to early support. A reduced six-predictor model eases everyday use because assessing all possible predictors for every child is quite challenging in practice.

## Design Implications

### Context
#### Requirements
- Kindergarten-age assessment of the model's predictor measures (a minimal set of six top-ranked features suffices per the reduced model)
- A trained and evaluated prediction model before deployment
#### Constraints
- The model's positive predictive value was low (.245–.252) due to low MD prevalence, so flagged children include many false positives
- Prediction identifies risk without explaining underlying mechanisms; inference models remain needed for intervention design

### Target Learners
- kindergarten-age children (age 6)

### Target Learning Goals
- early identification of and support for children at risk of math difficulties

### Affordances
- [Neural Networks Prediction Learning Difficulties](../research-methods/prediction-versus-explanation-as-two-cultures-of-statistical-modelling-in-educational-psyc.md)

## Claims

- [Kindergarten counting, arithmetic, and letter-knowledge measures correlate with Grade 6 arithmetic fluency (r up to .45)](../claims/kindergarten-measures-correlate-grade6-math.md) [+M]
- [At a sensitivity of .672 the MD prediction model showed specificity of .754–.762 but a low positive predictive value (.245–.252)](../claims/md-model-sensitivity-specificity-ppv.md) [~M]
- [A multilayer perceptron trained on 49 kindergarten-age measures predicts Grade 6 math difficulties with an AUC of .818](../claims/mlp-kindergarten-predictors-md-grade6-auc-818.md) [+M]
- [A reduced model using only the six top-ranked predictors maintains relatively similar MD prediction performance (AUC .776)](../claims/six-predictor-md-model-auc-776.md) [+M]
- [The most important kindergarten predictors of Grade 6 MD are RAN, spatial relations, arithmetic skills, number concepts, attention-orientation, and counting](../claims/top-predictors-md-ran-spatial-attention.md) [+M]
- [Only four screeners demonstrated acceptable diagnostic accuracy for distinguishing children with or at-risk of mathematical learning difficulties](../claims/four-screeners-acceptable-diagnostic-accuracy.md) [~W]

## Related Strategies

- [Use the SYMP Test as a quick screening measure to identify children at risk for mathematical difficulties or dyscalculia](symp-screening-at-risk-children-strategy.md)
- [Assess Arabic numeral identification and symbolic magnitude estimation to identify children likely to struggle with math](assess-symbolic-number-skills-for-early-identification.md)
- [Early identification battery for children at risk for long-term mathematics difficulties](early-math-risk-identification-battery.md)
- [Response To Intervention](response-to-intervention.md)
- [Provide early, effective, targeted intensive intervention to disrupt persistent trajectories of reading difficulty](early-intensive-intervention-disrupt-reading-difficulty-trajectories.md)
- [Identify children with weak inhibition skills in kindergarten and provide intervention or training programs to support later monitoring accuracy](early-inhibition-screening-and-training-for-monitoring.md)
- [Use broader baseline cognitive predictors beyond conventional phonological measures to detect at-risk learners and personalize literacy intervention](broad-predictors-personalized-dyslexia-intervention.md)

## Examples
-

## Key Sources
- Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M. (2024). Early prediction of math difficulties with the use of a neural networks model. Journal of Educational Psychology, 116(2), 212-232. https://doi.org/10.1037/edu0000835
