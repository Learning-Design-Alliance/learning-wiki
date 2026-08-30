---
type: strategy
title: Elaborative Interrogation
description: Learners generate explanations for why a stated fact or concept is true, prompting integration of new material with prior knowledge.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Elaborative Interrogation

## Description
Elaborative interrogation asks learners to answer "why is this true?" or "why does this make sense?" prompts about facts they are studying, rather than passively rereading them. The generated explanations connect new material to existing knowledge, producing richer, more retrievable memory traces. It is typically applied to factual claims embedded in text or lists, one item at a time.

## Design Implications

Elaborative interrogation is one of the most consistently supported learning techniques in the strategy literature [Dunlosky et al. rated elaborative interrogation as a moderately effective technique with broad utility.](../claims/elaborative-interrogation-improves-learning.md) [+M]. Its benefit comes from forcing integration: answering "why" requires retrieving relevant prior knowledge and linking it to the new fact, which improves both comprehension and later recall [Generating explanations during learning improves retention and transfer.](../claims/self-explanation-improves-learning.md) [+S]. Prompts should be specific to the material ("Why would this make the population grow?") rather than generic, and learners must actually attempt an answer — reading the prompt without generating a response eliminates the effect.

### Context
#### Requirements
- Factual or conceptual content stated as claims that can plausibly be explained
- Prompts that direct learners to connect the fact to prior knowledge, not just restate it
- Sufficient prior knowledge to generate a meaningful answer; a fallback (answer key, feedback) when learners cannot
- Time — generating explanations is slower than rereading, and this cost must be budgeted

#### Constraints
- Effectiveness drops sharply for learners with low prior knowledge, who cannot generate accurate explanations and may entrench misconceptions [Elaborative interrogation benefits depend on learners having sufficient prior knowledge to generate correct explanations.](../claims/elaborative-interrogation-improves-learning.md) [~M]
- Works best for discrete factual claims; less suited to complex, multi-step procedures or ill-structured problems
- Learners with high prior knowledge may gain little because the connections are already automatic [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]
- If learners cannot answer, they may simply read the provided explanation — which converts the activity into passive exposure [-W]

#### Implementation Variability
- **Prompted self-study:** "why" questions embedded in text margins or study guides
- **Peer questioning:** partners alternate asking and answering why-questions about assigned material
- **Combined with [Self-Explanation](../elements/self-explanation.md):** interrogation of one's own solution steps rather than stated facts
- **Adaptive prompts:** instructor- or system-generated why-questions targeting known misconceptions

### Target Learners
- Intermediate learners with moderate prior knowledge who can generate plausible explanations [Elaborative interrogation benefits depend on learners having sufficient prior knowledge.](../claims/elaborative-interrogation-improves-learning.md) [+M]
- Learners prone to passive rereading and illusions of fluency
- Less appropriate for complete novices, who should first build foundational knowledge through [Advance Organizers](../elements/advance-organizers.md) or worked examples

### Target Learning Goals
- Factual retention: remembering discrete claims and their justifications
- Conceptual integration: connecting new facts to existing knowledge structures
- Not well suited to procedural skill or transfer to novel problem types [Generating explanations improves retention more than far transfer.](../claims/self-explanation-improves-learning.md) [~M]

### Instructions
1. Present the material as a set of discrete factual claims ([Chunking](../principles/chunking.md) helps keep each unit answerable).
2. For each claim, pose a specific why-prompt ("Why would X lead to Y?").
3. Have learners generate an answer in their own words before any explanation is shown ([Generation](../elements/generation.md)).
4. Provide the correct explanation as feedback, especially when learner answers are incomplete or wrong.
5. Follow with retrieval practice — [Practice Testing](../elements/practice-testing.md) — to consolidate the elaborated connections.

## Related Strategies
- [Self-Explanation](../elements/self-explanation.md) — the sibling technique applied to one's own reasoning steps rather than stated facts
- [Retrieval Practice](retrieval-practice.md) — complementary; interrogation elaborates at encoding, retrieval strengthens later
- [Rereading](rereading.md) — the low-yield technique elaborative interrogation typically replaces

## Examples
- **Biology study guide:** after reading "capillaries have thin walls," students answer "Why would thin walls be useful for capillaries' function?" before checking the provided rationale.
- **History margin prompts:** a textbook embeds "Why did the treaty fail?" questions at each key claim, with brief model answers at chapter end.
- **Anki-style flashcards:** cards phrased as why-questions ("Why does exercise lower resting heart rate?") rather than simple definition pairs.

## Key Sources
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Pressley, M., McDaniel, M. A., Turnure, J. E., Wood, E., & Ahmad, M. (1987). Generation and precision of elaboration: Effects on intentional and incidental learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 13*(2), 291–300. [doi:10.1037/0278-7393.13.2.291](https://doi.org/10.1037/0278-7393.13.2.291)
- Pressley, M., Wood, E., Woloshyn, V. E., Martin, V., King, A., & Menke, D. (1992). Encouraging mindful use of prior knowledge: Attempting to construct explanatory answers facilitates learning. *Educational Psychologist, 27*(1), 91–109. [doi:10.1207/s15326985ep2701_7](https://doi.org/10.1207/s15326985ep2701_7)
- Ozgungor, S., & Guthrie, J. T. (2004). Interactions between elaborative knowledge and modeling elaborations on text comprehension. *Journal of Educational Psychology, 96*(2), 351–363. [doi:10.1037/0022-0663.96.2.351](https://doi.org/10.1037/0022-0663.96.2.351)