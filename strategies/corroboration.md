---
type: strategy
title: Corroboration
description: Learners verify a claim by checking it against multiple independent sources before accepting or sharing it.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Corroboration

> **Strategy** · [All strategies](index.md)

## Description
Corroboration is a source-verification strategy in which learners treat a single source's claim as provisional until it is confirmed by at least one other independent source. Learners identify the claim, locate additional sources on the same question, and compare the accounts — attending to agreement, disagreement, and each source's evidence and incentives. It is one of the three core heuristics of civic online reasoning, alongside [lateral reading](../strategies/lateral_reading.md) and source evaluation.

## Design Implications

Corroboration shifts learners from evaluating a source in isolation to evaluating a claim across a network of sources, which is how professional fact-checkers actually work [Explicit instruction in civic online reasoning improves learners' evaluation of online information.](../claims/civic-online-reasoning-instruction-improves-evaluation.md) [+S]. The key design move is requiring *independence*: two sites repeating the same wire story do not corroborate each other, and learners need practice distinguishing independent confirmation from echo. Corroboration works best when paired with a low threshold for action — learners decide whether a claim is confirmed, disputed, or unverifiable — so the comparison produces a judgment rather than open-ended browsing.

### Context
#### Requirements
- A specific, checkable claim (not a vague topic) to corroborate
- Access to multiple, genuinely independent sources (different outlets, primary documents, datasets)
- A protocol or graphic organizer for recording what each source says and on what evidence
- A decision rule: what counts as "confirmed," "disputed," or "unverifiable"

#### Constraints
- Fails when learners consult sources that share an upstream origin (syndicated content, press releases) — apparent agreement is not corroboration [-M]
- Weak for claims that are matters of interpretation or values, where "independent sources agree" does not establish truth [~M]
- Can degrade into confirmation bias if learners search only for sources that agree with the first account; prompts to actively seek *disconfirming* sources are needed [-M]
- Time-intensive; without a decision rule and time limit, learners stall in open-ended searching [-W]

#### Implementation Variability
- **Two-source minimum vs. triangulation:** a quick second-source check for everyday claims vs. three-plus sources for consequential ones (see [3-Source Rule](../strategies/3-source_rule.md))
- **Reverse corroboration:** start with a fact-check or primary document and ask which secondary sources got it right
- **Corroborating images/video:** reverse image search to find the original context of a viral photo
- **Structured disagreement:** deliberately assign sources known to conflict so learners must adjudicate

### Target Learners
- Middle school through adult learners; the largest documented gains are in secondary and postsecondary settings [Explicit instruction in civic online reasoning improves learners' evaluation of online information.](../claims/civic-online-reasoning-instruction-improves-evaluation.md) [+S]
- Learners who already read fluently but treat search results and polished websites as self-authenticating
- Less effective for beginning readers, who lack the fluency to compare accounts efficiently; simplify to pre-selected source sets first

### Target Learning Goals
- Information literacy: judging the reliability of claims and sources
- Civic reasoning: making evidence-based judgments about public claims before acting or sharing
- Epistemic cognition: understanding that single-source claims are provisional

### Instructions
1. **Identify the claim.** Restate it as a specific, checkable proposition (who, what, when).
2. **Read laterally first.** Before corroborating, establish what the original source is using [Lateral Reading](../strategies/lateral_reading.md) — corroboration with an unreliable first source is wasted effort.
3. **Find independent sources.** Search for the claim separately; require sources with different origins (see [A Finder's Guide to Facts](../strategies/a_finders_guide_to_facts.md)).
4. **Compare accounts.** Record what each source claims, its evidence, and its incentives, using [Comparing Cases](../elements/comparing-cases.md) or a simple matrix.
5. **Seek disconfirmation.** Prompt learners to search for reasons the claim might be false, not just confirmation.
6. **Decide and justify.** Classify the claim as confirmed / disputed / unverifiable and state the evidential basis — a form of [Argument Construction](../elements/argument-construction.md).

## Related Strategies
- [Lateral Reading](../strategies/lateral_reading.md) — the companion heuristic; establish what a source is before weighing its claim
- [3-Source Rule](../strategies/3-source_rule.md) — a concrete corroboration threshold learners can apply habitually
- [A Finder's Guide to Facts](../strategies/a_finders_guide_to_facts.md) — teaches the source-incentive analysis that makes corroboration discriminating

## Examples
- **Stanford History Education Group — Civic Online Reasoning curriculum** ([https://cor.stanford.edu](https://cor.stanford.edu)): free classroom tasks in which students corroborate breaking-news claims across outlets; field-tested in dozens of districts.
- **News Literacy Project — Checkology®** ([https://checkology.org](https://checkology.org)): includes a "contradicting the claim" lesson sequence where students hunt for independent confirmation and disconfirmation.
- **Fact-checker modeling:** showing videos of professional fact-checkers (e.g., from Snopes or PolitiFact) corroborating a viral claim, then having students replicate the process on a new claim.

## Key Sources
- Wineburg, S., & McGrew, S. (2019). Lateral reading and the nature of expertise: Reading less and learning more when evaluating digital information. *Teachers College Record, 121*(11), 1–40.
- Breakstone, J., Smith, M., Wineburg, S., Lester, A., Ortega, T., & Collins, S. (2021). Students' civic online reasoning: A national portrait. *Educational Researcher, 50*(8), 505–515. [doi:10.3102/0013189x211017495](https://doi.org/10.3102/0013189x211017495)
- McGrew, S., Ortega, T., Breakstone, J., & Wineburg, S. (2017). The challenge that's bigger than fake news: Civic reasoning in a social media environment. *American Educator, 41*(3), 4–9.
- Wineburg, S., Martin, D., & Monte-Sano, C. (2013). *Reading like a historian: Teaching literacy in middle and high school history classrooms* (2nd ed.). Teachers College Press.