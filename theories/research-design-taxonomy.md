---
type: theory
title: Research Design Taxonomy — Quantitative/Qualitative and Descriptive/Correlational/Experimental
description: Two overlapping ways of classifying a research study — quantitative vs. qualitative (or mixed) by data type, and descriptive vs. correlational vs. experimental by what conclusion the design can actually support — determine what a study can and can't tell you, independent of how well it was executed.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# Research Design Taxonomy — Quantitative/Qualitative and Descriptive/Correlational/Experimental

## Description
**Quantitative research** typically starts with a focused research question or hypothesis, collects a small amount of data from each of a large number of individuals, describes the resulting data with statistical techniques, and draws general conclusions about a population. It is comparatively weak at generating novel, interesting research questions or providing rich description of behavior in particular situations. **Qualitative research** does the reverse: it can generate new questions and hypotheses, collects large amounts of relatively unfiltered data from a relatively small number of individuals, describes that data with non-statistical techniques, and can produce rich, detailed description of behavior in the real-world contexts where it occurs — what qualitative researchers call the "lived experience" of participants. Because the two approaches have complementary strengths, some researchers combine them into **mixed-methods research**, either by using qualitative work to generate hypotheses that quantitative work then tests, or through **triangulation** — using both approaches simultaneously on the same question and comparing results. Convergent results reinforce and enrich each other; divergent results raise a genuinely useful further question: why do they diverge, and how can that be reconciled?

A separate dimension classifies research by what kind of conclusion the design can support, regardless of whether the underlying data is quantitative or qualitative. **Descriptive research** measures and reports a variable without testing any relationship between variables — it can answer interesting and important questions, but not questions about relationships. **Correlational research** goes a step further and formally tests whether a relationship exists between two or more variables, expressed as a correlation coefficient (*r*) from −1 to +1: the closer to 1 in either direction, the stronger and more predictable the relationship. Correlations have genuine predictive value — a university admissions committee, for instance, can use the correlation between current students' standardized test scores and their college GPA to help predict applicants' likely success. But correlation is limited in a specific way: establishing that a relationship exists tells us little about cause and effect. A correlation between two variables can arise because one variable is a **confounding variable** driving both — the classic textbook case is ice cream sales correlating with crime rates, where temperature drives both rather than either causing the other — or because people accept a causal story (do healthier people eat cereal, or does eating cereal make you healthier?) without checking for a confound.

People also perceive relationships between variables that don't actually exist at all — **illusory correlations**. The persistent belief that a full moon affects human behavior is a textbook case: a meta-analysis of nearly 40 studies found no such relationship (Rotton & Kelly, 1985), yet the belief persists because people notice and remember odd behavior during a full moon while failing to notice that odd behavior occurs at a constant rate throughout the lunar cycle — the same confirmation-bias mechanism (see [Evidence-Based Teaching and Scientific Reasoning](../principles/evidence-based-teaching-and-scientific-reasoning.md)) that makes personal inquiry generally unreliable. Illusory correlations are not merely a curiosity: research suggests they are involved in forming the prejudicial attitudes toward particular groups that can escalate into discriminatory behavior (Fiedler, 2004).

**Experimental research** goes further still, randomly assigning participants to conditions so that hypothesis testing can support inferences about causal relationships — see [Designing a Valid Experiment](../principles/designing-a-valid-experiment.md) for the mechanics. Descriptive, correlational, and experimental research form a genuine hierarchy of what a design can conclude, not a hierarchy of rigor or value: a descriptive study of what a phenomenon even looks like is often the necessary first step before a correlational study is worth running, which in turn can motivate a specific causal hypothesis worth testing experimentally.

## Implications

### Context
#### Requirements
- Matching the research question actually being asked to a design that can support the kind of conclusion it needs — a descriptive or correlational question does not need (and cannot be answered by mis-reading) an experimental design, and vice versa
#### Constraints
- A strong correlation, however large *r* is, never by itself establishes which variable (if either) causes the other, or whether a third variable causes both
- Readers as well as researchers are vulnerable to illusory correlations — noticing confirming instances and failing to notice the (much larger) set of disconfirming ones

### Target Learners
- Anyone reading, citing, or designing educational research — including this wiki's own claim pages, whose evidence-quality (`q`) ratings track exactly this design hierarchy (see `CLAUDE.md`'s evidence-quality tiers)

### Target Learning Objectives
- Reading a correlational finding (in a study, a news article, or a claim page) without silently upgrading it to a causal one

## Claims
- [Illusory correlations, like the belief that a full moon affects behavior, persist through confirmation bias despite having no basis in evidence](../claims/illusory-correlations-persist-through-confirmation-bias.md) [X]

## Related Theories
- [Designing a Valid Experiment](../principles/designing-a-valid-experiment.md) — the design that actually supports causal conclusions, and the mechanics of running one properly
- [Developmental Research Designs](developmental-research-designs.md) — a further, orthogonal set of design choices specific to studying change over time

## Examples
- A study reporting that students who use a particular study app have higher grades (correlational) is a different, weaker claim than a study that randomly assigns students to use the app or not and then compares outcomes (experimental)

## Key Sources
- Rotton, J., & Kelly, I. W. (1985). Much ado about the full moon: A meta-analysis of lunar-lunacy research. *Psychological Bulletin, 97*(2), 286-306.
- Fiedler, K. (2004). Illusory correlation. In R. F. Pohl (Ed.), *Cognitive illusions: A handbook on fallacies and biases in thinking, judgement and memory* (pp. 97-114). Psychology Press.
- Arduini-Van Hoose, N. (2020). Quantitative and qualitative approaches to research; Descriptive research; Correlational research. In *Educational psychology*. Retrieved from https://edpsych.pressbooks.sunycreate.cloud. CC BY-NC-SA 4.0.
