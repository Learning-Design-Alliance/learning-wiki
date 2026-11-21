---
type: claim
title: Markov transition analysis of tutor logs showed Buggy examples produced error-loop struggle patterns while Guided examples redirected errors toward hint-seeking
description: Markov transition analysis of tutor logs showed Buggy examples produced error-loop struggle patterns while Guided examples redirected errors toward hint-seeking
id: markov-behavior-patterns-logic-tutor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: sutapa-dey-tithi-2026
    resource: "https://doi.org/10.1145/3772318.3791631"
    title: Sutapa Dey Tithi 2026
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
  - id: sutapa-dey-tithi-2026-2
    resource: "https://doi.org/10.1145/3772318.3791631"
    title: Sutapa Dey Tithi 2026 (2)
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
  - id: sutapa-dey-tithi-2026-3
    resource: "https://doi.org/10.1145/3772318.3791631"
    title: Sutapa Dey Tithi 2026 (3)
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# Markov transition analysis of tutor logs showed Buggy examples produced error-loop struggle patterns while Guided examples redirected errors toward hint-seeking

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2` · `i3` large
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In Buggy examples students tended to remain stuck on incorrect attempts (51% of transitions) with tight loops on incorrect attempts and rule reading. [→ Sutapa Dey Tithi 2026](#sutapa-dey-tithi-2026)
`q2 i?` In Guided examples incorrect attempts rarely led to extended error cycles; students typically requested hints (44% of the time). [→ Sutapa Dey Tithi 2026 (2)](#sutapa-dey-tithi-2026-2)
`q2 i3` In PS problems, low prior knowledge students transitioned from hints to incorrect steps three times more often than high prior knowledge students (probability-based effect size A = .91, exploratory). [→ Sutapa Dey Tithi 2026 (3)](#sutapa-dey-tithi-2026-3)

## Evidence

### Sutapa Dey Tithi 2026

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q2 · i?` · `causal · r?`

First-order Markov models built from student action sequences across problem types (visualized with Graphviz in Figure 5): in Buggy problems students "tend to remain stuck on incorrect attempts 51% of the time", transitioning to correct attempts 27% of the time. Descriptive transition probabilities; no effect size printed.

> "Buggy examples demonstrate a distinctive "struggle pattern" characterized by tight loops on incorrect attempts and reading rule descriptions. Students frequently start with both correct attempts and incorrect attempts to fix any solution element, but they tend to remain stuck on incorrect attempts 51% of the time"

### Sutapa Dey Tithi 2026 (2)

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q2 · i?` · `causal · r?`

Same Markov transition analysis of tutor logs: in Guided problems, "students who make mistakes typically request hints (44% of the time)". The authors note strong transitions to hints from all actions raise the question of over-reliance on hints. Descriptive probabilities; no effect size printed.

> "Incorrect attempts in Guided examples rarely lead to extended error cycles; students who make mistakes typically request hints (44% of the time) rather than persist with more incorrect attempts."

### Sutapa Dey Tithi 2026 (3)

Sutapa Dey Tithi, Xiaoyi Tian, Ally Limke, Min Chi, and Tiffany Barnes. 2026. Exploring the Design and Impact of Interactive Worked Examples for Learners with Varying Prior Knowledge. Proceedings of The ACM CHI conference on Human Factors in Computing Systems (CHI'26). [doi:10.1145/3772318.3791631](https://doi.org/10.1145/3772318.3791631)

`q2 · i3` · `causal · r2`

Exploratory Mann-Whitney U comparison of per-student transition probabilities between low and high prior knowledge groups in PS problems, without Bonferroni adjustment: "30.4% vs. 10.1%,𝑝= 0.009" with printed probability-based effect size A = .91.

> "low prior knowledge students were three times more likely to transition from hints to incorrect steps than high prior knowledge students (30.4% vs. 10.1%,𝑝= 0.009,𝐴=. 91, 95% CI [.73, 1.0])"

## Discussion


## Related Claims
- [Buggy and Guided interactive worked examples produced significantly higher posttest problem scores than passive worked examples in logic tutoring](buggy-guided-higher-posttest-scores.md) — related
- [Guided examples improved posttest rule application accuracy over Control while Buggy accuracy did not differ significantly after correction](guided-rule-accuracy-gain-buggy-null.md) — related
- [Markov transition analysis shows the three clusters differ in workflow dynamics: iterative optimization loops, rapid prototyping flows, and browsing-anchored exploration](markov-workflow-dynamics-three-clusters.md) — related
- [Students rarely request on-demand hints in this tutor, with no significant differences between conditions or proficiency groups](on-demand-hint-requests-rare-and-equivalent.md) — related
- [Error rates per completed problem-solving step did not significantly differ between conditions](no-difference-error-rate-log.md) — related
- [Mindful-condition students completed fewer problem-solving steps and requested fewer hints per step than Cognitive-condition students](mindful-condition-fewer-steps-hints.md) — related
- [A warning message about potential AI mistakes increases seventh-graders' hint requests in a math intelligent tutoring system](ai-fallibility-warning-increases-help-seeking.md) — related
- [Platform logs show behavioral shifts toward goal-oriented optimization between workshop Days 4 and 5](behavioral-shift-goal-oriented-optimization.md) — related
- [Within problems, students' strongest transitions reflect persistence in ongoing states and immediate replay after successful solutions](within-problem-persistence-and-immediate-replay-transitions.md) — related
