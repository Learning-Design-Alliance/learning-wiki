---
type: research-method
id: uptake-formalized-as-pointwise-jensen-shannon-divergence-estimated-via-next-utterance-clas
title: Uptake formalized as pointwise Jensen-Shannon Divergence estimated via next utterance classification
description: "The article's central framework defines uptake as the dependence of a teacher reply T on a student utterance S, quantified by pointwise Jensen-Shannon Divergence: \"the extent to which we can tell whetherT is a response toS or is it a random response\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# Uptake formalized as pointwise Jensen-Shannon Divergence estimated via next utterance classification

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article's central framework defines uptake as the dependence of a teacher reply T on a student utterance S, quantified by pointwise Jensen-Shannon Divergence: "the extent to which we can tell whetherT is a response toS or is it a random response". If the true reply cannot be distinguished from a random one, the authors argue there can be no uptake, as the reply fails the functions of coherence, grounding and collaboration. PJSD is estimated by fine-tuning BERT-base via next utterance classification on 777k mixed student-teacher and Switchboard pairs, and the framework is positioned as unsupervised to support domain transferability where labeled data is unavailable.

## Accounts
<!-- How each source describes or uses the method -->
- **Uptake formalized as pointwise Jensen-Shannon Divergence estimated via next utterance classification**: The article's central framework defines uptake as the dependence of a teacher reply T on a student utterance S, quantified by pointwise Jensen-Shannon Divergence: "the extent to which we can tell whetherT is a response toS or is it a random response". If the true reply cannot be distinguished from a random one, the authors argue there can be no uptake, as the reply fails the functions of coherence, grounding and collaboration. PJSD is estimated by fine-tuning BERT-base via next utterance classification on 777k mixed student-teacher and Switchboard pairs, and the framework is positioned as unsupervised to support domain transferability where labeled data is unavailable. (Dorottya Demszky et al. (2021))

### Claims
- [PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations](../claims/pjsd-outperforms-repetition-baseline-uptake.md) [+M]
- [PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T](../claims/pjsd-captures-uptake-phenomena-switchboard.md) [+M]

## Related Research Methods
-

## Key Sources
- Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. https://arxiv.org/abs/2106.03873
