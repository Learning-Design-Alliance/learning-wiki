---
type: product
id: facet-framework-for-agent-based-classroom-enhancement-for-teachers
title: FACET (Framework for Agent-based Classroom Enhancement for Teachers)
description: FACET is a teacher-facing LLM-based multi-agent framework developed by Jana Gonnermann-Müller et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# FACET (Framework for Agent-based Classroom Enhancement for Teachers)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
FACET is a teacher-facing LLM-based multi-agent framework developed by Jana Gonnermann-Müller et al. that simulates learner profiles and generates and evaluates personalized classroom worksheets.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **FACET: a teacher-facing LLM-based multi-agent framework for generating personalized classroom worksheets**: FACET (Framework for Agent-based Classroom Enhancement for Teachers) is a modular, teacher-oriented system that simulates learner behavior to personalize outputs such as worksheets. It instantiates three LLM-backed agents: learner agents embodying cognitive and motivational profiles, a teacher agent applying didactical directives, and an evaluator agent providing quality assurance. The pipeline runs sequentially (learner→teacher→evaluator) via a custom web interface, using GPT-4.1 for reasoning-heavy agents and GPT-4o for evaluation, with reusable prompt templates and slot-filling for grade, topic, and profile parameters. The article states it "is designed to simulate and analyze learner behavior, with the objective of personalizing output, such as worksheets." (Jana Gonnermann-Müller et al. (2025))
- **Differentiation beyond performance: teacher-specifiable learner profiles spanning cognitive, motivational, and neurodiversity dimensions**: The article operationalizes differentiated instruction as adaptation that goes beyond performance metrics alone. FACET's learner profiles integrate "prior knowledge levels, motivational aspects, reading and writing difficulties, attention-related needs, and other cognitive and affective factors," grounded in the argument that effective differentiation must address motivation and neurodiversity (dyslexia, ADHD) as well as cognitive proficiency. Profiles are defined in terms of observable, learning-relevant needs rather than diagnostic labels to mitigate stereotyping risks. (Gonnermann-Müller et al. (2026))

### Claims
- [Agent-based evaluation of FACET-generated worksheets returns consistently high, stable ratings across four learner profiles and ten iterations](../claims/facet-agent-evaluation-high-stable-ratings.md) [+M]
- [K-12 in-service teachers rated FACET-generated personalized worksheets highly, especially didactical structure and suitability for learners](../claims/facet-teacher-expert-evaluation-ratings.md) [+M]
- [Dyslexia-adapted worksheet shows partial alignment with accessibility guidelines but weak font readability](../claims/dyslexia-worksheet-mixed-accessibility-ratings.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Jana Gonnermann-Müller, Jennifer Haase, Konstantin Fackeldey, Sebastian Pokutta. (2025). FACET: Teacher-Centred LLM-Based Multi-Agent Systems—Towards Personalized Educational Worksheets. https://arxiv.org/abs/2508.11401
- Gonnermann-Müller, J., Haase, J., Leins, N., Igel, M., Fackeldey, K., & Pokutta, S. (2026). FACET: Multi-Agent AI Supporting Teachers in Scaling Differentiated Learning for Diverse Students. arXiv preprint. https://arxiv.org/abs/2601.22788
