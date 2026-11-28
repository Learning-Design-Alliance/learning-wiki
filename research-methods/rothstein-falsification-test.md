---
type: research-method
id: rothstein-falsification-test
moved_from: [element/rothstein-falsification-test-vam, theory/rothstein-falsification-test-vam-diagnostic]
title: Rothstein falsification test
description: A falsification test for teacher value-added models, introduced by Jesse Rothstein (2010) and re-assessed in this paper.
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: dan-goldhaber-2012
    resource: "https://www.mathematica.org/publications/assessing-the-rothstein-test-does-it-really-show-teacher-valueadded-models-are-biased"
    title: "Dan Goldhaber, Duncan Chaplin. (2012). Assessing the Rothstein Test: Does It Really Show Teacher Value-Added Models Are Biased? Working Paper 5. Seattle, WA: Center for Education Data & Research, University of Washington. https://www.mathematica.org/publications/assessing-the-rothstein-test-does-it-really-show-teacher-valueadded-models-are-biased"
    author: Dan Goldhaber, Duncan Chaplin
  - id: dan-goldhaber-2015
    resource: "https://www.mathematica.org/publications/assessingthe-rothstein-falsification-test-does-it-really-show-teacher-valueadded-models-are-biased"
    title: "Dan Goldhaber, Duncan Dunbar Chaplin. (2015). Assessing the \"Rothstein Falsification Test\": Does It Really Show Teacher Value-Added Models Are Biased? Journal of Research on Educational Effectiveness, vol. 8, issue 1. https://www.mathematica.org/publications/assessingthe-rothstein-falsification-test-does-it-really-show-teacher-valueadded-models-are-biased"
    author: Dan Goldhaber, Duncan Dunbar Chaplin
---

# Rothstein falsification test

> **Research Method** · [All research methods](index.md)
> **Evidence** · 12 claims (5 for, 2 mixed, 5 against) · 3 studies (2 theoretical, 1 associational), `q1`–`q2` · 1 of 3 report an effect size · 12 claims rest on one study

## Description
A falsification test for teacher value-added models, introduced by Jesse Rothstein (2010) and re-assessed in this paper. It rests on the observation that standard VAMs "suggest implausible future teacher effects on past student achievement, a finding that obviously cannot be viewed as causal", which "appears to indicate bias in VAM estimates of current teacher contributions to student learning". The present paper evaluates whether a failed test truly demonstrates bias.

## Accounts
<!-- How each source describes or uses the method -->
- **Rothstein falsification test for teacher value-added models**: A falsification test for teacher value-added models, introduced by Jesse Rothstein (2010) and re-assessed in this paper. It rests on the observation that standard VAMs "suggest implausible future teacher effects on past student achievement, a finding that obviously cannot be viewed as causal", which "appears to indicate bias in VAM estimates of current teacher contributions to student learning". The present paper evaluates whether a failed test truly demonstrates bias. (Dan Goldhaber (2012))
- **The Rothstein falsification test as a diagnostic for value-added model bias**: The Rothstein falsification test is a diagnostic procedure, proposed by Jesse Rothstein (2010), that regresses students' past achievement on future teacher assignments; implausibly large future teacher effects are taken to indicate bias in typical value-added model estimates of teacher contributions to student learning on standardized tests. This article treats the test as an inferential tool whose signal can arise without bias, since "tracking could be based on lagged student achievement, which is usually accounted for in VAMs." It is used here as the object of a methodological critique rather than as a validated measure of estimator bias. (Dan Goldhaber (2015))
- **Evaluate VAM model assumptions with pre-assignment outcomes before using value added estimates in personnel decisions**: Before value added estimates are used in hiring, firing, or compensation, the article argues the model's exclusion restrictions should be tested with pre-assignment outcomes, because non-random classroom assignment can make estimates reflect the students a teacher is assigned. The author warns that VAM-based policies "may reward and punish teachers for the students they are assigned as much as for their actual effectiveness in the classroom". (Rothstein (2008))
- **Falsification tests based on future teacher assignments to check VAM exclusion restrictions**: A specification-diagnostic framework for value added modeling that exploits the fact that "future teachers and firms cannot have causal effects on past outcomes". The article regresses lagged gains on current classroom assignments: if a 5th grade teacher assignment predicts 4th grade gains, the model's exclusion restriction fails. The author implements such tests for three widely used VAMs in North Carolina elementary data, showing each restriction is violated. (Rothstein (2008))

### Claims
- [Rothstein (2010) found that standard VAMs imply implausible future-teacher effects on past student achievement](../claims/rothstein-implausible-future-teacher-effects.md) [+W]
- [The Rothstein falsification test is not definitive in showing bias in VAM teacher effect estimates](../claims/rothstein-test-not-definitive-evidence-of-bias.md) [-W]
- [The Rothstein test can reject VAMs even when students are randomly assigned conditional on the covariates in the model](../claims/rothstein-test-rejects-vams-random-assignment.md) [-W]
- [The Rothstein falsification test can reject value-added models even when estimated teacher effects are unbiased](../claims/rothstein-test-rejects-vams-without-bias.md) [-W]
- [The Rothstein falsification test generates large and implausible future teacher effects even when students are randomly assigned to classrooms](../claims/rothstein-falsification-test-implausible-effects-random-assignment.md) [-W] — (also cited [+M])
- [Theoretically and in simulations, the Rothstein test often falsifies unbiased VAMs and fails to falsify biased VAMs](../claims/falsification-test-falsifies-unbiased-vams.md) [-W] — (also cited [+M])
- [Tracking based on lagged student achievement is usually accounted for in value-added models, which is why the falsification test can mislead](../claims/lagged-achievement-tracking-accounted-for-in-vams.md) [~W] — (also cited [-W])
- [Detecting that students are tracked to teachers does not necessarily imply bias in teacher effectiveness estimates](../claims/tracking-detection-does-not-imply-vam-bias.md) [~W] — (also cited [-W])
- [Bias from non-random classroom assignments is large relative to estimated teacher effects in VAM1 and somewhat smaller in VAM2](../claims/vam-bias-nonrandom-assignment-magnitude.md) [+M]
- [In North Carolina elementary data, 5th grade classroom assignments significantly predict students' 4th grade test score gains, violating the VAM1 exclusion restriction](../claims/vam1-future-teacher-assignment-predicts-past-gains.md) [+M]
- [VAM2's exclusion restriction is violated in North Carolina data: residuals are correlated across grades and 5th grade teachers predict 4th grade gains controlling for 4th grade scores](../claims/vam2-exclusion-restriction-violated-north-carolina.md) [+M]
- [VAM3's conditional strict exogeneity assumption is rejected: 5th grade teacher coefficients for 3rd and 4th grade gains are near-zero correlated, and the restricted model fails the overidentification test](../claims/vam3-strict-exogeneity-rejected-north-carolina.md) [+M]

## Related Research Methods
-

## Key Sources
- Dan Goldhaber, Duncan Chaplin. (2012). Assessing the Rothstein Test: Does It Really Show Teacher Value-Added Models Are Biased? Working Paper 5. Seattle, WA: Center for Education Data & Research, University of Washington. https://www.mathematica.org/publications/assessing-the-rothstein-test-does-it-really-show-teacher-valueadded-models-are-biased
- Dan Goldhaber, Duncan Dunbar Chaplin. (2015). Assessing the "Rothstein Falsification Test": Does It Really Show Teacher Value-Added Models Are Biased? Journal of Research on Educational Effectiveness, vol. 8, issue 1. https://www.mathematica.org/publications/assessingthe-rothstein-falsification-test-does-it-really-show-teacher-valueadded-models-are-biased
<!-- merged 2026-10-10 from elements/rothstein-falsification-test-vam ("Rothstein falsification test for teacher value-added models"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Dan Goldhaber, Duncan Dunbar Chaplin. (2015). Assessing the "Rothstein Falsification Test": Does It Really Show Teacher Value-Added Models Are Biased? Journal of Research on Educational Effectiveness, vol. 8, issue 1. https://www.mathematica.org/publications/assessingthe-rothstein-falsification-test-does-it-really-show-teacher-valueadded-models-are-biased
- Rothstein, Jesse. (2008). Teacher Quality in Educational Production: Tracking, Decay, and Student Achievement. NBER Working Paper No. 14442. http://www.nber.org/papers/w14442

# Rothstein falsification test for teacher value-added models

> **Element** · [All elements](index.md)
> **Evidence** · 8 claims (1 for, 2 mixed, 5 against) · 2 studies (2 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 8 claims rest on one study

## Description
A falsification test for teacher value-added models, introduced by Jesse Rothstein (2010) and re-assessed in this paper. It rests on the observation that standard VAMs "suggest implausible future teacher effects on past student achievement, a finding that obviously cannot be viewed as causal", which "appears to indicate bias in VAM estimates of current teacher contributions to student learning". The present paper evaluates whether a failed test truly demonstrates bias.

## Design Implications

### Context
#### Requirements
- Requires VAM teacher effect estimates and the test's implausible future-teacher-effect diagnostic as described by Rothstein (2010)
#### Constraints
- The paper shows the test can reject VAMs even when estimates are unbiased and students are randomly assigned conditional on model covariates, so a rejection is not definitive evidence of bias

### Target Learners
- K-12 students whose teachers are evaluated with value-added models

### Target Learning Goals
- Fair and accurate estimation of teacher contributions to student achievement for personnel policy

## Claims

- [Rothstein (2010) found that standard VAMs imply implausible future-teacher effects on past student achievement](../claims/rothstein-implausible-future-teacher-effects.md) [+W]
- [The Rothstein falsification test is not definitive in showing bias in VAM teacher effect estimates](../claims/rothstein-test-not-definitive-evidence-of-bias.md) [-W]
- [The Rothstein test can reject VAMs even when students are randomly assigned conditional on the covariates in the model](../claims/rothstein-test-rejects-vams-random-assignment.md) [-W]
- [The Rothstein falsification test can reject value-added models even when estimated teacher effects are unbiased](../claims/rothstein-test-rejects-vams-without-bias.md) [-W]
- [The Rothstein falsification test generates large and implausible future teacher effects even when students are randomly assigned to classrooms](../claims/rothstein-falsification-test-implausible-effects-random-assignment.md) [-W]
- [Theoretically and in simulations, the Rothstein test often falsifies unbiased VAMs and fails to falsify biased VAMs](../claims/falsification-test-falsifies-unbiased-vams.md) [-W]
- [Tracking based on lagged student achievement is usually accounted for in value-added models, which is why the falsification test can mislead](../claims/lagged-achievement-tracking-accounted-for-in-vams.md) [~W]
- [Detecting that students are tracked to teachers does not necessarily imply bias in teacher effectiveness estimates](../claims/tracking-detection-does-not-imply-vam-bias.md) [~W]

## Related Elements
- 

## Examples
-

## Key Sources
- Dan Goldhaber, Duncan Chaplin. (2012). Assessing the Rothstein Test: Does It Really Show Teacher Value-Added Models Are Biased? Working Paper 5. Seattle, WA: Center for Education Data & Research, University of Washington. https://www.mathematica.org/publications/assessing-the-rothstein-test-does-it-really-show-teacher-valueadded-models-are-biased
-->

<!-- merged 2026-10-10 from theories/rothstein-falsification-test-vam-diagnostic ("The Rothstein falsification test as a diagnostic for value-added model bias"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# The Rothstein falsification test as a diagnostic for value-added model bias

> **Theory** · [All theories](index.md)
> **Evidence** · 4 claims (2 for, 2 against) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The Rothstein falsification test is a diagnostic procedure, proposed by Jesse Rothstein (2010), that regresses students' past achievement on future teacher assignments; implausibly large future teacher effects are taken to indicate bias in typical value-added model estimates of teacher contributions to student learning on standardized tests. This article treats the test as an inferential tool whose signal can arise without bias, since "tracking could be based on lagged student achievement, which is usually accounted for in VAMs." It is used here as the object of a methodological critique rather than as a validated measure of estimator bias.

## Design Implications

### Context
#### Requirements
- Interpretation requires distinguishing tracking-on-lagged-achievement, which VAMs typically control, from tracking that induces genuine bias in teacher effect estimates.
#### Constraints
- The article reports that the test "will often falsify VAMs that are unbiased and fail to falsify VAMs that are biased," limiting its use as a bias diagnostic.

### Target Learners
- K-12 students in classrooms assigned to teachers

### Target Learning Objectives
- Accurate estimation of teacher contributions to student achievement on standardized tests

### Claims

- [Rothstein Falsification Test Implausible Effects Random Assignment](../claims/rothstein-falsification-test-implausible-effects-random-assignment.md) [+M]
- [Falsification Test Falsifies Unbiased Vams](../claims/falsification-test-falsifies-unbiased-vams.md) [+M]
- [Tracking based on lagged student achievement is usually accounted for in value-added models, which is why the falsification test can mislead](../claims/lagged-achievement-tracking-accounted-for-in-vams.md) [-W]
- [Detecting that students are tracked to teachers does not necessarily imply bias in teacher effectiveness estimates](../claims/tracking-detection-does-not-imply-vam-bias.md) [-W]

## Related Theories

- [Untestable-assumptions account for bias in nonexperimental estimation](../theories/untestable-assumptions-nonexperimental-estimators.md)

## Examples
-

## Key Sources
- Dan Goldhaber, Duncan Dunbar Chaplin. (2015). Assessing the "Rothstein Falsification Test": Does It Really Show Teacher Value-Added Models Are Biased? Journal of Research on Educational Effectiveness, vol. 8, issue 1. https://www.mathematica.org/publications/assessingthe-rothstein-falsification-test-does-it-really-show-teacher-valueadded-models-are-biased
-->
