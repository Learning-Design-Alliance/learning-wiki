---
type: claim
title: Multiple Contrasting Cases Support Abstraction
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: multiple-contrasting-cases-support-abstraction
evidence_strength: unverified
sources:
  - id: alfieri-et-al-2013
    resource: "https://doi.org/10.1080/00461520.2013.775712"
    title: "Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. *Educational Psychologist, 48*(2), 87–113. [doi:10.1080/00461520.2013.775712](https://doi.org/10.1080/00461520.2013.775712)"
    author: "Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D."
    q: 4
    i: 2
    n: 57 experiments (336 tests)
  - id: gentner-et-al-2003
    resource: "https://doi.org/10.1037/0022-0663.95.2.393"
    title: "Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology, 95*(2), 393–408. [doi:10.1037/0022-0663.95.2.393](https://doi.org/10.1037/0022-0663.95.2.393)"
    author: "Gentner, D., Loewenstein, J., & Thompson, L."
    q: 3
    i: "?"
    n: 128 undergraduates (Experiment 2)
---

# Multiple Contrasting Cases Support Abstraction

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i2` medium

Comparing multiple cases that differ on key dimensions helps learners abstract the underlying principles, rather than learning each case as an isolated instance. The claim concerns comparison of *minimally contrasting* cases — cases aligned enough to compare, differing on the dimension to be abstracted.

## Subclaims

`q4 i2` Across 57 experiments (336 tests), case-comparison activities produced greater learning than sequential, single-case or nonanalogous case study, traditional instruction and controls (d = .50); benefits were larger when learners were asked to find similarities, when the principle was given after the comparison, for perceptual content, and on immediate tests. [→ Alfieri et al. 2013](#alfieri-et-al-2013)

`q3 i?` Undergraduates who compared two negotiation cases side by side were more than twice as likely to transfer the underlying principle to a new negotiation as those who studied the same two cases separately (48% vs 19%), showing that comparison, not exposure to multiple cases, drives schema abstraction. [→ Gentner et al. 2003](#gentner-et-al-2003)

## Evidence

### Alfieri et al. 2013

Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. *Educational Psychologist, 48*(2), 87–113. [doi:10.1080/00461520.2013.775712](https://doi.org/10.1080/00461520.2013.775712)

`q4 · meta-analysis (random effects)` · `i2 · medium effect, d=0.50, 95% CI [.44, .56]` · `n=57 experiments (336 tests)`

A random-effects meta-analysis of 57 experiments, in laboratory and classroom settings, comparing case-comparison activities against other ways of studying cases (sequential, single case, nonanalogous) and against traditional instruction and controls. Comparison led to greater learning overall (d = .50). Of 15 candidate moderators, four reliably moderated the effect: asking learners to find similarities, presenting the principle after the comparison, using perceptual content, and testing immediately were each associated with larger gains. The review pools comparison of cases in general; it does not isolate *minimally contrasting* cases, so the page's narrower framing is a subset of what it tests.

### Gentner et al. 2003

Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology, 95*(2), 393–408. [doi:10.1037/0022-0663.95.2.393](https://doi.org/10.1037/0022-0663.95.2.393)

`q3 · peer-reviewed randomised experiments (3 studies)` · `i? · no standardised effect size reported; 48% vs 19% transfer, χ²(1, N=128)=11.85, p<.01` · `n=128 undergraduates (Experiment 2)`

Three experiments taught novices negotiation strategies (trade-offs, contingent contracts) from short cases. In Experiment 2, 128 undergraduates were randomly assigned to read two cases on one page and describe their similarities, or to read and describe each case separately; they then negotiated a new lease case. Comparers were more than twice as likely to use the principle in the new negotiation (48% vs 19%), and the benefit held for both strategy types. Experiment 1 found a benefit of comparison over no case study, and Experiment 3 found that more comparison support raised transfer in a face-to-face negotiation. The compared cases were analogous, sharing a principle across different surface stories, rather than contrasting on one dimension.

## Discussion

**Mechanism.** Contrasting cases make the deep structure of a domain visible by highlighting what varies and what stays constant across examples. When learners compare cases that differ on surface features but share a principle, they are pushed to explain the differences, which supports abstraction and transfer. This is the core rationale of [Cognitive Flexibility Theory](../patterns/cognitive-flexibility-theory.md), which argues for multiple representations and cases in ill-structured domains — see [Cognitive flexibility theory: multiple cases support flexible transfer.](../claims/cognitive-flexibility-theory-multiple-cases.md).

**Comparison as the active ingredient.** The benefit is generally attributed to comparison itself, not mere exposure to multiple cases. Learners need prompts to align the cases and articulate similarities and differences; simply presenting several examples side by side without comparison support is unlikely to produce the same abstraction. This connects closely to [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md), where structured comparison of analogs drives schema formation. Structured comparison prompts — asking learners to identify what is the same, what differs, and why — function as a form of [self-explanation](../claims/self-explanation-improves-learning.md) applied across cases rather than within one.

**Case selection matters.** Cases should be minimally contrasting — similar enough to align, but differing on the dimension the learner is meant to abstract. Overly dissimilar cases are hard to align; overly similar cases highlight nothing. This mirrors the use of contrasting examples and non-examples in [Concept Attainment](../patterns/concept-attainment.md), where the boundary between instances and non-instances carries the definitional information.

**Sequencing and load.** Whether to present cases simultaneously (side by side) or successively is an open design question, and the optimal arrangement may depend on learner expertise and working-memory demands — see [Cognitive Load Theory](../theories/cognitive-load-theory.md) and [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md). Simultaneous display requires holding two cases in mind at once, which can overload novices even when the comparison itself would be valuable; successive presentation reduces load but makes alignment harder because the first case must be retrieved from memory.

**Single-case limitation and expertise reversal.** A single well-chosen case can sometimes suffice for novices, and multiple cases impose additional processing demands that may not pay off when the target concept is simple or the learner is very inexperienced. As with worked examples, an expertise-reversal dynamic is plausible: see [Expertise Reversal Effect](../theories/expertise-reversal-effect.md). More advanced learners, who already possess a schema, may extract little from additional cases and may benefit more from varied practice than from further comparison.

**Open questions.** The claim currently lacks a populated evidence base. Key studies on contrasting cases in mathematics and physics instruction, and on simultaneous versus sequential comparison formats, still need to be added before an evidence strength can be assigned. Until then, designers should treat the claim as theoretically well-motivated but empirically unverified on this page, and weight design decisions toward the comparison-support and case-selection conditions described above, which are the moderators most likely to determine whether multiple cases help or merely add load.

## Related Claims

- [Cognitive flexibility theory: multiple cases support flexible transfer.](../claims/cognitive-flexibility-theory-multiple-cases.md) — the theoretical framework behind multiple-case instruction in ill-structured domains
- [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md) — structured comparison of analogs drives schema abstraction
- [Self-explanation improves learning.](../claims/self-explanation-improves-learning.md) — the prompts that make case comparison productive operate through self-explanation
- [Case-based learning improves exam performance.](../claims/case-based-learning-improves-exam-performance.md) — cases as the unit of instruction in professional education
- [Concept attainment](../patterns/concept-attainment.md) — pattern in which learners induce a concept from contrasting examples and non-examples
- [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) — worked examples are a single-case alternative whose multi-case extensions raise the same design questions
- [Comparing Contrasting Cases Improves Learning](comparing-contrasting-cases-improves-learning.md) — possibly the same claim (merge candidate)
- [Encoding variability across varied example contexts produces decontextualization supporting transfer (review reports DiVesta and Peverly)](encoding-variability-decontextualization-transfer.md) — related
- [PAIR-C scaffolding shows mixed evidence for deep understanding and reduced misconceptions in emergent-phenomena instruction](pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) — related