---
type: principle
title: Designing a Valid Experiment
description: A scientific experiment isolates one manipulated variable between an experimental and control group, guards against experimenter and participant-expectancy bias through blinding, and uses random sampling for generalizability and random assignment for causal inference — two distinct uses of randomness that are often conflated.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# Designing a Valid Experiment

## Description
An experiment, in the scientific sense, has precise requirements that everyday use of the word "experiment" doesn't imply. The most basic design involves an **experimental group** and a **control group**, built to be identical except for one deliberate difference — the **experimental manipulation** (the treatment or variable being tested). Because that manipulation is the only planned difference between the groups, any resulting difference in outcome can be attributed to it rather than to chance. Manipulated variables need an **operational definition** — a precise description of how the variable is actually measured — so that other researchers can understand exactly what was measured and can repeat the study if they choose to.

Researchers distinguish the **independent variable** (manipulated or controlled by the experimenter — the only important planned difference between groups) from the **dependent variable** (what the researcher measures to see how much effect the independent variable had). The dependent variable is expected to change as a function of the independent variable — the central experimental question is simply what effect the independent variable has on the dependent variable.

Two forms of bias threaten an otherwise well-designed experiment. **Experimenter bias** is the risk that a researcher's own expectations skew how they record or interpret results — guarded against with a **single-blind study** (participants don't know which group they're in, but the researcher does) or, more strongly, a **double-blind study** (neither participants nor the researchers interacting with them know group assignment). Blinding also guards against the **placebo effect** — the tendency for a person's own expectations to change their experience regardless of any actual treatment effect — which is why a credible drug trial gives the control group an inert placebo rather than nothing at all, so that any difference in outcome can be attributed to the drug itself rather than to the mere expectation of receiving treatment.

Randomness serves two genuinely distinct purposes that are easy to conflate. **Random sampling** — giving every member of a population an equal chance of being included in the study's sample — supports **generalizability**: a large-enough random sample is likely to be representative of the larger population on the characteristics (sex, ethnicity, socioeconomic status, and others) that might affect the results. **Random assignment** — giving every sampled participant an equal chance of landing in the experimental versus the control group — supports **causal inference**: it makes it improbable that the two groups differ systematically before the study even begins, so that any measured difference afterward can be attributed to the manipulation rather than to a pre-existing difference between groups. A study can have one without the other — a convenience sample of volunteers can still be randomly assigned to conditions, which supports causal claims about that sample without supporting generalization beyond it.

Not every causal question can be answered this way. When the variable of interest can't actually be manipulated by the experimenter (for instance, a participant's sex, in a study asking what effect sex has on some outcome), the approach is called **quasi-experimental**, and it cannot support the same strength of cause-and-effect claim a true experiment can, since a systematic pre-existing difference between groups can never be ruled out by design alone. Ethical constraints impose a further limit: some causal questions (does experiencing childhood abuse cause lower adult self-esteem?) could only be answered by an experiment that randomly assigned some participants to be harmed, which is not permissible research.

Once data is collected, a statistical analysis determines how likely it is that an observed difference between groups occurred by chance rather than reflecting a real effect. In psychology, a difference is conventionally treated as meaningful, or **statistically significant**, when the odds of it occurring by chance alone are 5 percent or less (p < .05) — equivalently, if the study were repeated 100 times, the same result would be expected at least 95 times.

## Implications

### Context
#### Requirements
- A precise operational definition for every manipulated and measured variable, stated clearly enough that another researcher could replicate the procedure
- Random assignment to conditions whenever a causal claim is the goal, independent of whether the sample itself was randomly drawn
#### Constraints
- Without blinding, a researcher's own hopes for the outcome can distort how ambiguous behavior gets recorded or scored, even without any intent to bias the result
- Some variables of real interest (a person's sex, native language, prior achievement level) cannot be experimentally manipulated at all, capping the design at quasi-experimental and the causal claim at a correspondingly weaker one
- Ethical limits rule out manipulating some variables regardless of what a true experiment would require

### Target Learners
- Anyone designing, reviewing, or citing an experimental claim, including this wiki's own claim pages, where the `q` evidence-quality tier for an RCT versus a quasi-experiment tracks exactly this distinction (see `CLAUDE.md`)

### Target Learning Objectives
- Distinguishing a genuinely random, causally-informative assignment from a merely random-seeming sample, and recognizing when a study's design (quasi-experimental, unblinded, unrandomized) caps how strong a causal conclusion it can support

## Related Principles
- [Research Design Taxonomy — Quantitative/Qualitative and Descriptive/Correlational/Experimental](../theories/research-design-taxonomy.md) — where experimental design sits in the larger hierarchy of what a study design can conclude
- [Evidence-Based Teaching and Scientific Reasoning](evidence-based-teaching-and-scientific-reasoning.md)

## Examples
- A double-blind, placebo-controlled drug trial where neither the participant nor the administering researcher knows who received the active medication
- A quasi-experimental comparison of male and female students' spatial-memory scores, which can describe a difference but cannot establish that sex itself causes it

## Key Sources
- Arduini-Van Hoose, N. (2020). Experimental research. In *Educational psychology*. Retrieved from https://edpsych.pressbooks.sunycreate.cloud. CC BY-NC-SA 4.0.
