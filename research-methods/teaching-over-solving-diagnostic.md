---
type: research-method
id: teaching-over-solving-diagnostic
title: Teaching-over-solving diagnostic
description: "The article proposes a lightweight diagnostic that reaggregates public tutoring benchmark scores into two composites: a solving composite (problem solving, solution correctness, mistake location, mistake correction) and a pedagogy composite (socratic questioning, scaffolding win rate, pedagogy instr"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Teaching-over-solving diagnostic

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a lightweight diagnostic that reaggregates public tutoring benchmark scores into two composites: a solving composite (problem solving, solution correctness, mistake location, mistake correction) and a pedagogy composite (socratic questioning, scaffolding win rate, pedagogy instruction-following win rate, hard scaffolding, hard pedagogy instruction-following). For each model it defines "Gap(m) = Teach(m)−Solve(m)", where positive values indicate models relatively stronger on pedagogy than on solving. It is intended for education-oriented NLP work that lacks private classroom data.

## Accounts
<!-- How each source describes or uses the method -->
- **Teaching-over-solving diagnostic: separating answer-production ability from learning-support behavior via solving and pedagogy composites and their gap**: The article proposes a lightweight diagnostic that reaggregates public tutoring benchmark scores into two composites: a solving composite (problem solving, solution correctness, mistake location, mistake correction) and a pedagogy composite (socratic questioning, scaffolding win rate, pedagogy instruction-following win rate, hard scaffolding, hard pedagogy instruction-following). For each model it defines "Gap(m) = Teach(m)−Solve(m)", where positive values indicate models relatively stronger on pedagogy than on solving. It is intended for education-oriented NLP work that lacks private classroom data. (Junyi Yao et al. (2026))
- **Report solving-oriented and pedagogy-oriented tutoring scores separately, with a disclosure-sensitive dimension penalizing full-solution giveaways**: The article recommends that tutoring benchmark leaderboards stop collapsing task success and learning support into a single helpfulness score. It argues "benchmark reporting should preserve the distinction between solving strength and teaching strength instead of collapsing them into a single notion of helpfulness", and that benchmarks should include a disclosure-sensitive dimension penalizing giving away full solutions when the learner context calls for scaffolding. (Junyi Yao et al. (2026))

### Claims
- [Solving-oriented and pedagogy-oriented composite scores on the public MathTutorBench leaderboard are only moderately correlated (Pearson 0.421, Spearman 0.690)](../claims/solving-pedagogy-composites-moderately-correlated-mathtutorbench.md) [+M]
- [In the public TutorBench sample, agency-oriented rubric criteria are most concentrated in the active-learning use case (agency-dimension density 0.720, agency-skill density 0.411)](../claims/tutorbench-rubrics-encode-agency-active-learning-highest.md) [+M]

## Related Research Methods
-

## Key Sources
- Junyi Yao, Zihao Zheng, and Baichuan Li. (2026). Beyond Helpfulness: A Teaching-over-Solving Diagnostic for Measuring Educational Impact in LLM Tutors. arXiv preprint. https://arxiv.org/abs/2606.16206
