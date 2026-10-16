---
type: claim
title: Feedback Enhances Retrieval Practice
status: review
generated:
  by: claude/unspecified
  at: 2026-09-25
id: feedback-enhances-retrieval-practice
aliases: [corrective-feedback-boosts-classroom-testing-effect]
evidence_strength: pending
sources:
  - id: yang-et-al-2021
    resource: "https://doi.org/10.1037/bul0000309"
    title: "Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review. *Psychological Bulletin, 147*(4), 399–435. [doi:10.1037/bul0000309](https://doi.org/10.1037/bul0000309)"
    author: "Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R."
    q: 4
    i: 2
    n: 222 studies
    kind: quant-synthesis
    rigour: 2
  - id: pashler-et-al-2005
    resource: "https://doi.org/10.1037/0278-7393.31.1.3"
    title: "Pashler, H., Cepeda, N. J., Wixted, J. T., & Rohrer, D. (2005). When does feedback facilitate learning of words? *Journal of Experimental Psychology: Learning, Memory, and Cognition, 31*(1), 3–8. [doi:10.1037/0278-7393.31.1.3](https://doi.org/10.1037/0278-7393.31.1.3)"
    author: "Pashler, H., Cepeda, N. J., Wixted, J. T., & Rohrer, D."
    q: 3
    i: "?"
    n: 258
    kind: causal
    rigour: "?"
---

# Feedback Enhances Retrieval Practice

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r?`, 1 quant-synthesis `r2` · `q3`–`q4` · `i2` medium

Retrieval practice strengthens long-term retention, and providing feedback after retrieval attempts further improves learning by correcting errors and confirming correct responses. This page treats the *interaction* — whether feedback adds incremental value beyond retrieval alone — as a distinct claim requiring its own evidence.

## Subclaims

`q4 i2` In classroom studies, quizzing followed by corrective feedback produced a larger testing effect than quizzing without feedback (g = 0.537 vs g = 0.374). This is a between-study moderator comparison, and an earlier meta-analysis (Adesope et al., 2017) found no such moderation. [→ Yang et al. 2021](#yang-et-al-2021)

`q3 i?` In a laboratory word-pair study, giving the correct answer after an incorrect retrieval greatly increased retention one week later. Feedback after correct responses made little difference, even when learners had low confidence in them. [→ Pashler et al. 2005](#pashler-et-al-2005)

`q4 i2` Across classroom studies, testing effects were significantly larger where class quizzes were followed by corrective feedback than where they were not (a between-study moderator comparison, so feedback may be confounded with other study features). [→ Yang et al. 2021](#yang-et-al-2021)

## Evidence

### Yang et al. 2021

Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review. *Psychological Bulletin, 147*(4), 399–435. [doi:10.1037/bul0000309](https://doi.org/10.1037/bul0000309)

`q4 · systematic review and multilevel meta-analysis` · `i2 · medium effect, g=0.537 with corrective feedback vs g=0.374 without` · `n=222 studies` · `quant-synthesis · r2`

This review pooled classroom studies that compared quizzing with restudying and other control activities. The published abstract gives 222 independent studies and 48,478 students; the accepted manuscript gives 223 studies, 574 effects and 48,582 students. The overall testing effect was g = 0.499. Whether [corrective feedback](../elements/feedback.md) was given significantly moderated that effect (Q(2) = 11.197, p = .004). Quizzes followed by feedback (335 effects) produced g = 0.537 [0.469, 0.604], and quizzes without feedback (142 effects) produced g = 0.374 [0.278, 0.471]. Two cautions: the comparison is made across studies rather than within them, so feedback may be confounded with other study features, and the authors note that Adesope et al. (2017) found no moderation (g = 0.63 with feedback, g = 0.60 without), whereas Rowland (2014) reported g = 0.73 with feedback and g = 0.39 without.

<!-- merged 2026-10-13 from corrective-feedback-boosts-classroom-testing-effect: that page's entry for this study, which differed from the one above, kept verbatim.
### Yang 2020

Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2020). Testing (Quizzing) Boosts Classroom Learning: A Systematic and Meta-Analytic Review. Psychological Bulletin. https://doi.org/10.1037/bul0000309

`q4 · i2` · `quant-synthesis · r?`

Meta-analytic moderator analysis of corrective feedback in classroom studies; the review reports feedback "significantly increases learning gains over not providing feedback", with printed effect sizes g = 0.537 with feedback versus g = 0.374 without.

> "Offering corrective feedback following class quizzes ( g = 0.537) significantly increases learning gains over not providing feedback ( g = 0.374)."
-->

### Pashler et al. 2005

Pashler, H., Cepeda, N. J., Wixted, J. T., & Rohrer, D. (2005). When does feedback facilitate learning of words? *Journal of Experimental Psychology: Learning, Memory, and Cognition, 31*(1), 3–8. [doi:10.1037/0278-7393.31.1.3](https://doi.org/10.1037/0278-7393.31.1.3)

`q3 · peer-reviewed experiment, between-subjects` · `i? · no standardized effect size in the abstract; reported as a 494% increase in final retention` · `n=258` · `causal · r?`

258 participants studied Luganda–English word pairs twice. They were then tested on each item several times, and the presence and type of feedback varied between participants. A final test followed one week later. Supplying the correct answer after an incorrect response improved performance during learning and raised final retention by 494%. Feedback after correct responses made little difference, either immediately or after a week, even when the learner was not confident in the response. This supports the page's boundary condition that feedback matters most after failed retrievals. (Coded from the abstract only; the full text could not be retrieved.)

## Studies bearing on this claim

<!-- synthesis:start -->
*Does feedback after retrieval add to the benefit?* This table gathers the studies behind this claim and the 7 narrower claims that bear on it: **9 distinct studies** (3 quant-synthesis, 3 causal, 2 review, 1 theoretical), `q2`–`q4`, 1 of 9 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Yang et al. 2021](https://doi.org/10.1037/bul0000309) | q4 · quant-synthesis · r2 | i2 · medium effect, g=0.537 with corrective feedback vs g=0.374 without | this claim |
| [Pashler et al. 2005](https://doi.org/10.1037/0278-7393.31.1.3) | q3 · causal · r? | i? | this claim |
| [Adesope 2017](https://doi.org/10.3102/0034654316689306) | q4 · quant-synthesis · r3 | i? | [Providing corrective feedback on practice tests does not significantly change the testing ](feedback-no-significant-moderation.md) (qualifies) |
| [Karpicke 2017](https://doi.org/10.1016/b978-0-12-809324-5.21055-9) | q2 · review · r3 | i? | [Initial short-answer tests outperform initial multiple-choice tests mainly when feedback f](feedback-determines-whether-short-answer-retrieval-outperforms-multiple-choice.md) (supports); [Taking initial multiple-choice tests without feedback can lead students to later produce t](multiple-choice-lures-can-be-learned-as-false-knowledge.md) (supports) |
| [Metcalfe 2017](https://doi.org/10.1146/annurev-psych-010416-044022) | q2 · review · r? | i? | [High-confidence errors lead to better retention after correction than low-confidence error](high-confidence-errors-improve-retention.md) (supports) |
| [Fazio & Marsh 2009](https://doi.org/10.3758/pbr.16.1.88) | q3 · causal · r? | i? | [High-confidence errors lead to better retention after correction than low-confidence error](high-confidence-errors-improve-retention.md) (supports) |
| [Kluger 1996](https://doi.org/10.1037/0033-2909.119.2.254) | q2 · quant-synthesis · r2 | i? | [Outcome feedback (mere knowledge of results) impedes learning of complex tasks in the mult](outcome-feedback-impedes-complex-task-learning-mcpl.md) (qualifies) |
| Weiss 1980 | q2 · causal · r? | i? | [Immediate knowledge of results during computerized achievement testing produces essentiall](knowledge-of-results-no-effect-achievement-test-dimensionality.md) (qualifies) |
| Glaser 1966 | q2 · theoretical · r3 | i? | [Overt correction of errors speeds young children's learning compared with knowledge of cor](overt-error-correction-speeds-young-children-learning.md) (supports) |
<!-- synthesis:end -->

## Discussion

**Why feedback should help.** Retrieval attempts can produce errors or partial answers; without corrective information, learners may re-encode mistaken responses. Feedback after a retrieval attempt allows learners to confirm correct retrievals and repair incorrect ones, and the act of first attempting retrieval is thought to make subsequent feedback more deeply processed than feedback delivered without an attempt — the same "generation then correction" logic that underlies [Pretesting enhances learning from subsequent instruction.](pretesting-enhances-learning.md)

**Boundary conditions to investigate.** The benefit of feedback likely depends on retrieval success: for items learners retrieve correctly and confidently, feedback may add little, while for failed or low-confidence retrievals it should matter most. Timing (immediate vs. delayed), format (correct-answer-only vs. elaborated explanation), and learner expertise are plausible moderators that the evidence base must establish before this claim can be rated. The general feedback literature suggests effects are heterogeneous across these conditions, so this claim should not be treated as uniformly positive until moderators are pinned down.

**Relation to the base effect.** This claim augments, and should be evaluated against, [Retrieval practice improves long-term retention.](retrieval-practice-improves-retention.md) — the question is whether feedback adds incremental value beyond retrieval alone, not whether retrieval works. It also sits within the broader claim that [Feedback improves learning outcomes.](feedback-improves-learning.md), which this page specializes to retrieval contexts.

**Design implications while evidence is pending.** Practitioners combining retrieval with feedback should prioritize feedback on failed or low-confidence retrievals, where the corrective value is greatest, and avoid interrupting successful retrievals with redundant confirmation that adds time without benefit. Feedback format should follow the same principles as elsewhere: answer feedback is efficient for factual items, while elaborated explanation is more appropriate where learners must understand why an answer is correct — consistent with the guidance in [Feedback improves learning outcomes.](feedback-improves-learning.md). Because retrieval practice itself is well supported, adding feedback should not displace retrieval opportunities; the combination is best treated as retrieval practice with a corrective layer, not as a replacement for it.

**Open questions.** Whether feedback benefits persist on delayed tests, whether elaborate feedback outperforms simple answer feedback after retrieval, and whether feedback changes the metacognitive monitoring that retrieval practice supports are all unresolved pending addition of primary studies. Until then, designers combining retrieval with feedback should treat the combination as promising but unverified as an interaction.

## Related Claims

- [Retrieval practice improves long-term retention.](retrieval-practice-improves-retention.md) — the base effect that feedback is hypothesized to augment
- [Feedback improves learning outcomes.](feedback-improves-learning.md) — the general feedback effect this claim situates within retrieval contexts
- [Pretesting enhances learning from subsequent instruction.](pretesting-enhances-learning.md) — related "errorful generation then correction" mechanism
- [Spacing improves retention.](spaced-practice-improves-retention.md) — often combined with retrieval and feedback in durable learning designs
- [Retrieval practice and spaced retrieval improve achievement and retention by medium amounts, while interleaving helps category learning only for some materials and blocking beats it for words](desirable-difficulties-enhance-learning.md) — related
- [High-confidence errors lead to better retention after correction than low-confidence errors.](high-confidence-errors-improve-retention.md) — related
- [Overt correction of errors speeds young children's learning compared with knowledge of correctness alone](overt-error-correction-speeds-young-children-learning.md) — related
- [Guiding analytics for learners can improve mathematics achievement, retention, learning strategies, and reduce math anxiety](guiding-analytics-improves-achievement-and-strategies.md) — related
- Retrieval practice strengthens memory and produces stronger, more enduring learning — a broader claim this one bears on
- [Timely feedback on homework increases learning, and computer platforms providing immediate feedback help teachers adapt](timely-feedback-improves-homework-learning.md) — related
- [Struggling to encode, retrieve, and reorganize information produces deeper comprehension and retention, and AI-supplied ready-made solutions short-circuit these processes](ai-removing-struggle-short-circuits-desirable-difficulties.md) — related
- [Classroom testing (quizzing) significantly boosts student academic achievement to a medium extent (g = 0.499).](classroom-quizzing-medium-effect-achievement.md) — related
- [Providing corrective feedback on practice tests does not significantly change the testing effect (g = 0.63 with feedback vs. g = 0.60 without)](feedback-no-significant-moderation.md) — reports the opposite
- [Both preclass (g = 0.186) and postclass (g = 0.536) quizzes enhance learning, with postclass quizzes more effective; benefits increase with treatment duration.](postclass-quizzes-and-longer-duration-larger-gains.md) — related
- [The classroom testing effect increases with the number of test repetitions on the same content.](test-repetitions-positive-relationship-classroom.md) — related
- [AI chatbots provide students detailed feedback, step-by-step homework solutions, and self-quizzing support](chatbot-homework-study-assistance.md) — related
- [Immediate-feedback tutors allow learning from errors but deny learning from their downstream consequences](immediate-feedback-limits-downstream-error-learning.md) — related
