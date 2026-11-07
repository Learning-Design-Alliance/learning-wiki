---
type: strategy
id: llm-wellbeing-recommendation-improvement-strategy
title: Iterate on the recommendation pipeline through prompt refinement, hallucination safeguards, intervention studies, and larger cohorts
description: "The authors recommend a staged improvement path for LLM-based personalized student recommendations: refine prompts and explore more advanced models to address alignment variability, add safeguards against harmful outp..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
sources:
  - id: ahmed-arfan-2025
    resource: "https://doi.org/10.1038/s41598-025-89386-2"
    title: "Ahmed Arfan, Aziz Sarah, Abd-alrazaq Alaa, AlSaad Rawan, Sheikh Javaid (2025). Leveraging LLMs and wearables to provide personalized recommendations for enhancing student well-being and academic performance through a proof of concept. Scientific Reports 15, 4591. https://doi.org/10.1038/s41598-025-89386-2"
    author: Ahmed Arfan, Aziz Sarah, Abd-alrazaq Alaa, AlSaad Rawan, Sheikh Javaid
---

# Iterate on the recommendation pipeline through prompt refinement, hallucination safeguards, intervention studies, and larger cohorts

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The authors recommend a staged improvement path for LLM-based personalized student recommendations: refine prompts and explore more advanced models to address alignment variability, add safeguards against harmful outputs, incorporate advanced data analytics and continuous feedback loops, and validate impact through intervention designs. They state that "intervention groups are crucial and would validate the recommendations' effectiveness in improving student well-being and academic performance", with a randomized controlled trial as a possible next step, and note the small sample of 12 limits statistical power.

## Design Implications

### Context
#### Requirements
- Larger cohorts, stakeholder (student and/or parent) feedback, proper anonymization, and ethical approvals for future studies.
#### Constraints
- The risk of model hallucinations poses a challenge; excessive feedback may lead to anxiety rather than improvement in well-being; Fitbit-derived HRV has limited validation in adolescents.

### Target Learners
- high school students aged 13 to 17

### Target Learning Goals
- enhancing student well-being and academic performance through personalized recommendations

## Claims

- [Alignment of LLM recommendations with individual student data showed more variability than clarity or actionability ratings](../claims/llm-recommendation-alignment-variable.md) [+W]
- [Validators rated LLM-generated personalized recommendations as generally clear and actionable for most of the eight evaluated students](../claims/llm-recommendations-rated-clear-actionable.md) [+W]

## Related Strategies

- [Refine LLM feedback prompts and adopt RAG to reduce verbosity and align feedback with course content](refine-llm-prompts-rag-reduce-verbosity.md)
- [Practise prompt engineering through simulations, prompt-a-thons and scenario exercises to obtain accurate LLM outputs](prompt-engineering-practice-simulations-prompt-a-thons.md)
- [Co-create micro-intervention repertoires with generative AI through a seed-request-refine prompt sequence, with the instructor curating output](ai-co-creation-of-emotional-micro-interventions.md)

## Examples
-

## Key Sources
- Ahmed Arfan, Aziz Sarah, Abd-alrazaq Alaa, AlSaad Rawan, Sheikh Javaid (2025). Leveraging LLMs and wearables to provide personalized recommendations for enhancing student well-being and academic performance through a proof of concept. Scientific Reports 15, 4591. https://doi.org/10.1038/s41598-025-89386-2
