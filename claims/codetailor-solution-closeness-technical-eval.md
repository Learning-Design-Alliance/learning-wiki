---
type: claim
title: "CodeTailor generates correct solutions closer to a student's incorrect code than a most common student solution"
description: "CodeTailor generates correct solutions closer to a student's incorrect code than a most common student solution"
id: codetailor-solution-closeness-technical-eval
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: xinying-hou-2024
    title: Xinying Hou 2024
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: xinying-hou-2024-2
    title: Xinying Hou 2024 (2)
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CodeTailor generates correct solutions closer to a student's incorrect code than a most common student solution

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The personalized solution's similarity to the student's incorrect code was significantly higher than the baseline common solution's similarity. [→ Xinying Hou 2024](#xinying-hou-2024)
`q2 i?` The LLM-generated code achieved an average accuracy rate of 0.98 across inputs, and final solutions were always correct after fallback. [→ Xinying Hou 2024 (2)](#xinying-hou-2024-2)

## Evidence

### Xinying Hou 2024

Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson. 2024. CodeTailor: LLM-Powered Personalized Parsons Puzzles for Engaging Support While Learning Programming. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3662032

`q2 · i?` · `design · r2`

Technical evaluation on 500 incorrect code submissions (50 per problem, each from a unique student) from an intermediate Python course; a Wilcoxon signed-rank test compared token-sequence similarity of personalized vs common solutions to each student's code. "W = 369.0, p < .001, CLES = 0.75".

> "the incorrect-personalized similarity, M (SD) = 0.6 (0.2), Median = 0.7, is significantly higher than the incorrect-baseline similarity, M (SD) = 0.5 (0.1), Median = 0.5, across student incorrect code inputs, W = 369.0, p < .001, CLES = 0.75."

### Xinying Hou 2024 (2)

Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson. 2024. CodeTailor: LLM-Powered Personalized Parsons Puzzles for Engaging Support While Learning Programming. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3662032

`q2 · i?` · `design · r2`

Same technical evaluation; correctness was measured by unit tests integrated in CodeTailor. The article reports "The average accuracy rate of the LLM-generated code for all incorrect student code inputs across questions was 0.98 (SD = 0.13)" and that fallback made final solutions always correct; no standardized effect size is printed.

> "The average accuracy rate of the LLM-generated code for all incorrect student code inputs across questions was 0.98 (SD = 0.13)."

## Discussion


## Related Claims
- [CodeTailor's personalized Parsons puzzles contain significantly fewer movable blocks than fully movable puzzles built from the same solution](codetailor-puzzles-more-concise.md) — related
- [Novice programmers perceive CodeTailor's personalized Parsons puzzles as more engaging support than receiving a direct LLM-generated code solution](codetailor-more-engaging-than-ai-solution.md) — related
- [Students applied more scaffolded practice elements independently on the posttest after using CodeTailor than after receiving an AI-generated solution](codetailor-higher-scaffolding-apply-rate.md) — related
- [Posttest programming scores did not differ significantly between CodeTailor support and receiving an AI-generated solution](codetailor-posttest-performance-null.md) — related
- [Most novice programmers (88%) preferred CodeTailor over receiving a direct AI-generated solution for learning](codetailor-preference-88-percent.md) — related
