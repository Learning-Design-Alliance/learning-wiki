---
type: research-method
id: countable-versus-dispositional-prompt-rule-audit
title: Countable versus dispositional prompt-rule audit
description: "The paper's organizing framework splits system-prompt instructions into two kinds."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Countable versus dispositional prompt-rule audit

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 causal, 1 associational), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The paper's organizing framework splits system-prompt instructions into two kinds. Countable rules "set targets that anyone can check from the output, such as the two-sentence cap on replies", while dispositional rules "describe how the agent should behave or its manner, such as not being overly agreeable". Instruction-following benchmarks only test the first kind, leaving manner rules unmeasured; the paper supplies the missing scoring mechanism through human coders and validated LLM annotators applied to a deployment's own transcripts, treating an unaudited agent as an unverified treatment in the health-intervention sense.

## Accounts
<!-- How each source describes or uses the method -->
- **Countable versus dispositional prompt rules, audited from deployment transcripts**: The paper's organizing framework splits system-prompt instructions into two kinds. Countable rules "set targets that anyone can check from the output, such as the two-sentence cap on replies", while dispositional rules "describe how the agent should behave or its manner, such as not being overly agreeable". Instruction-following benchmarks only test the first kind, leaving manner rules unmeasured; the paper supplies the missing scoring mechanism through human coders and validated LLM annotators applied to a deployment's own transcripts, treating an unaudited agent as an unverified treatment in the health-intervention sense. (Faithful Where It Can Be Checked: Auditing a Reflection Agent Against Its System Prompt in)

### Claims
- [A deployed reflection agent followed its prompt's countable rules but broke its dispositional rules about manner](../claims/agent-followed-countable-not-dispositional-rules.md) [+M]
- [An explicit prompt instruction to challenge gently changed nothing: the agent challenged in about 1% of turns under both prompts](../claims/challenge-instruction-changed-nothing.md) [+M]

## Related Research Methods
-

## Key Sources
- Subigya K. Nepal, Serena Soh, Noah Vinoya, SoHyun Park, Mahnaz Roshanaei, and Gabriella Harari. 2027. Faithful Where It Can Be Checked: Auditing a Reflection Agent Against Its System Prompt in a Randomized Trial. In Proceedings of CHI Conference on Human Factors in Computing Systems (CHI '27). ACM, New York, NY, USA. https://arxiv.org/abs/2609.19635
