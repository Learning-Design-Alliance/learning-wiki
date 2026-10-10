---
type: strategy
id: avp-content-gating-strategy
title: Gate sensitive simulated-patient content behind an accumulated-skill threshold with constraint-first prompting
description: "The article's implementation strategy is to release sensitive disclosure topics only as the trainee's accumulated skill crosses fixed thresholds."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: angela-chen-2026
    resource: "https://arxiv.org/abs/2606.10051"
    title: "Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051"
    author: Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu
---

# Gate sensitive simulated-patient content behind an accumulated-skill threshold with constraint-first prompting

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's implementation strategy is to release sensitive disclosure topics only as the trainee's accumulated skill crosses fixed thresholds. The prompt is built constraint-first: a disclosure-constraint instruction marked absolute, then level-matched topics, then memory, then dialogue history. Long-term memory is "seeded only from G-level content at session start, so memory retrieval cannot surface sensitive material before the level allows it." At G, H-level facts are not in the prompt so the LLM cannot produce them.

## Design Implications

### Context
#### Requirements
- Requires per-level disclosure topic sets and constraint instructions authored for each persona
- Requires a validated disclosure-labeling mechanism to resolve the current level each turn
#### Constraints
- The threshold values (M at 4.5, H at 10.0) and the 3:1 weight ratio are design choices; the article states the optimal ratio likely exceeds 3:1

### Target Learners
- clinicians and clinical trainees practicing psychotherapy micro-skills

### Target Learning Goals
- practicing elicitation of progressively deeper patient disclosure

### Affordances
- [Avp State Generation Separation Framework](../designs/avp-state-generation-separation-framework.md)

## Related Strategies

- [Mastery Based Progression](mastery-based-progression.md)

## Examples
-

## Key Sources
- Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills. https://arxiv.org/abs/2606.10051
