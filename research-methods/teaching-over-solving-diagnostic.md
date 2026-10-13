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
> **Evidence** · 4 claims (3 for, 1 mixed) · 3 studies (2 causal, 1 associational), `q2`–`q3` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
The article proposes a lightweight diagnostic that reaggregates public tutoring benchmark scores into two composites: a solving composite (problem solving, solution correctness, mistake location, mistake correction) and a pedagogy composite (socratic questioning, scaffolding win rate, pedagogy instruction-following win rate, hard scaffolding, hard pedagogy instruction-following). For each model it defines "Gap(m) = Teach(m)−Solve(m)", where positive values indicate models relatively stronger on pedagogy than on solving. It is intended for education-oriented NLP work that lacks private classroom data.

## Accounts
<!-- How each source describes or uses the method -->
- **Teaching-over-solving diagnostic: separating answer-production ability from learning-support behavior via solving and pedagogy composites and their gap**: The article proposes a lightweight diagnostic that reaggregates public tutoring benchmark scores into two composites: a solving composite (problem solving, solution correctness, mistake location, mistake correction) and a pedagogy composite (socratic questioning, scaffolding win rate, pedagogy instruction-following win rate, hard scaffolding, hard pedagogy instruction-following). For each model it defines "Gap(m) = Teach(m)−Solve(m)", where positive values indicate models relatively stronger on pedagogy than on solving. It is intended for education-oriented NLP work that lacks private classroom data. (Junyi Yao et al. (2026))
- **Report solving-oriented and pedagogy-oriented tutoring scores separately, with a disclosure-sensitive dimension penalizing full-solution giveaways**: The article recommends that tutoring benchmark leaderboards stop collapsing task success and learning support into a single helpfulness score. It argues "benchmark reporting should preserve the distinction between solving strength and teaching strength instead of collapsing them into a single notion of helpfulness", and that benchmarks should include a disclosure-sensitive dimension penalizing giving away full solutions when the learner context calls for scaffolding. (Junyi Yao et al. (2026))
- **Taxonomy of high-quality strategies that foster understanding versus low-quality strategies that lead students to the solution**: The article defines a two-category taxonomy of tutor moves in mathematics tutoring, drawing on prior work. High-quality strategies "foster students' understanding": prompting the student to explain, asking questions to guide thinking, and affirming the student's correct attempt. Low-quality strategies "lead students directly to the solution or passively engage students": asking the student to retry, giving away the answer/explanation, giving away the solution strategy, and encouraging the student in a generic way. Binary RoBERTa classifiers identified these strategies at scale with F1-scores between 0.65 and 0.90. (Rose E. Wang et al. (2025))

### Claims

- [Solving-oriented and pedagogy-oriented composite scores on the public MathTutorBench leaderboard are only moderately correlated (Pearson 0.421, Spearman 0.690)](../claims/solving-pedagogy-composites-moderately-correlated-mathtutorbench.md) [+M]
- [In the public TutorBench sample, agency-oriented rubric criteria are most concentrated in the active-learning use case (agency-dimension density 0.720, agency-skill density 0.411)](../claims/tutorbench-rubrics-encode-agency-active-learning-highest.md) [+M]
- [Tutors with Tutor CoPilot access use more understanding-fostering strategies (e.g., prompting students to explain) and rely less on giving away answers than control tutors](../claims/tutor-copilot-shifts-tutors-toward-understanding-fostering-strategies.md) [+M]
- [Model scale alone does not induce Socratic behavior: unaligned Qwen-72B achieves 0% scaffolding effectiveness and 96.7% keyword leakage](../claims/scale-alone-does-not-induce-socratic-behavior.md) [~W]

## Related Research Methods
-

## Key Sources
- Junyi Yao, Zihao Zheng, and Baichuan Li. (2026). Beyond Helpfulness: A Teaching-over-Solving Diagnostic for Measuring Educational Impact in LLM Tutors. arXiv preprint. https://arxiv.org/abs/2606.16206
- Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky. (2025). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017v2. https://arxiv.org/abs/2410.03017v2
