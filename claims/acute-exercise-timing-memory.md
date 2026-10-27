---
type: claim
title: The timing of acute exercise relative to learning modulates memory consolidation
status: review
generated:
  by: claude/unspecified
  at: 2026-09-25
id: acute-exercise-timing-memory
evidence_strength:
newest_evidence: 2019
sources:
  - id: loprinzi-et-al-2019
    resource: "https://doi.org/10.3390/brainsci9040087"
    title: "Loprinzi, P., Blough, J., Crawford, L., Ryu, S., Zou, L., & Li, H. (2019). The Temporal Effects of Acute Exercise on Episodic Memory Function: Systematic Review with Meta-Analysis. *Brain Sciences, 9*(4), 87. [doi:10.3390/brainsci9040087](https://doi.org/10.3390/brainsci9040087)"
    author: "Loprinzi, P., Blough, J., Crawford, L., Ryu, S., Zou, L., & Li, H."
    q: 3
    i: 2
    n: 25 studies
    kind: quant-synthesis
    rigour: "?"
  - id: van-dongen-et-al-2016
    resource: "https://doi.org/10.1016/j.cub.2016.04.071"
    title: "van Dongen, E. V., Kersten, I. H. P., Wagner, I. C., Morris, R. G. M., & Fernández, G. (2016). Physical Exercise Performed Four Hours after Learning Improves Memory Retention and Increases Hippocampal Pattern Similarity during Retrieval. *Current Biology, 26*(13), 1722–1727. [doi:10.1016/j.cub.2016.04.071](https://doi.org/10.1016/j.cub.2016.04.071)"
    author: "van Dongen, E. V., Kersten, I. H. P., Wagner, I. C., Morris, R. G. M., & Fernández, G."
    q: 3
    i: "?"
    n: "? (sample size not stated in the abstract)"
    kind: causal
    rigour: "?"
---

# The timing of acute exercise relative to learning modulates memory consolidation

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r?`, 1 quant-synthesis `r?` · `q3` · `i2` medium
> **Currency** · newest study 2019 · 1 of 2 entries checked against their sources (automated) · not reviewed by a person

A single bout of cardiovascular exercise can enhance memory for recently learned material, but the effect depends on *when* the exercise occurs relative to encoding and consolidation — before learning, shortly after learning, or much later.

## Subclaims

`q3 i2` Across 25 experiments, the effect of a single bout of exercise on episodic memory depended on its timing: slightly negative during encoding (d=−0.12), small and non-significant before encoding (d=0.11), medium during early consolidation (d=0.47), and large but imprecise during late consolidation (d=1.05, from only two studies). [→ Loprinzi et al. 2019](#loprinzi-et-al-2019)

`q3 i?` In a three-group randomised experiment, exercise performed 4 hours after learning improved 48-hour retention of picture-location associations compared with no exercise, while exercise performed immediately after learning did not. [→ van Dongen et al. 2016](#van-dongen-et-al-2016)

## Evidence

### Loprinzi et al. 2019

Loprinzi, P., Blough, J., Crawford, L., Ryu, S., Zou, L., & Li, H. (2019). The Temporal Effects of Acute Exercise on Episodic Memory Function: Systematic Review with Meta-Analysis. *Brain Sciences, 9*(4), 87. [doi:10.3390/brainsci9040087](https://doi.org/10.3390/brainsci9040087)

`q3 · systematic review with meta-analysis (not pre-registered)` · `i2 · medium effect, d=0.47 during early consolidation` · `n=25 studies` · `quant-synthesis · r?`

This review pooled 25 experimental studies of healthy adults aged 18 to 84, comparing one bout of exercise with a control condition. It sorted them by when the exercise happened: before learning, during learning, within 4 hours after learning (early consolidation), or 4 or more hours after (late consolidation). Exercise during learning slightly hurt memory (d=−0.12). Exercise before learning had a small effect that did not reach significance (d=0.11), though it helped young adults (d=0.18) and hurt older adults (d=−0.53). Exercise after learning helped: d=0.47 in the early window and d=1.05 in the late window. The late-window estimate comes from only two studies and has a wide interval (95% CI 0.32 to 1.78). No study blinded its outcome assessors.

### van Dongen et al. 2016

van Dongen, E. V., Kersten, I. H. P., Wagner, I. C., Morris, R. G. M., & Fernández, G. (2016). Physical Exercise Performed Four Hours after Learning Improves Memory Retention and Increases Hippocampal Pattern Similarity during Retrieval. *Current Biology, 26*(13), 1722–1727. [doi:10.1016/j.cub.2016.04.071](https://doi.org/10.1016/j.cub.2016.04.071)

`q3 · randomised three-group experiment` · `i? · no effect size in the abstract` · `n=? (sample size not stated in the abstract)` · `causal · r?`

Participants were randomly assigned to one of three groups, and all of them learned a set of picture-location pairs. One group exercised immediately afterwards, one exercised 4 hours later, and one did not exercise. The procedures were otherwise the same. Memory was tested 48 hours later, with cued recall in an MRI scanner. Only the group that exercised 4 hours later remembered better than the no-exercise group. That group also showed more hippocampal pattern similarity when recalling correctly. The finding runs against the idea that exercise immediately after learning is the best time and that delayed exercise does little.

## Studies bearing on this claim

<!-- synthesis:start -->
*Does what happens in the hours after learning, such as a bout of exercise, change how much is remembered later?* This table gathers the studies behind this claim and the 0 narrower claims that bear on it: **2 distinct studies** (1 quant-synthesis, 1 causal), `q3`, 1 of 2 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Loprinzi et al. 2019](https://doi.org/10.3390/brainsci9040087) | q3 · quant-synthesis · r? | i2 · medium effect, d=0.47 during early consolidation | this claim |
| [van Dongen et al. 2016](https://doi.org/10.1016/j.cub.2016.04.071) | q3 · causal · r? | i? | this claim |
<!-- synthesis:end -->

## Discussion

**Timing windows.** The literature on acute exercise and memory distinguishes several timing protocols: exercise before encoding (which may raise arousal and catecholamine levels during learning), exercise immediately after encoding (during the early consolidation window, when exercise-induced noradrenaline and BDNF are hypothesized to strengthen newly formed memory traces), and exercise delayed by hours. The evidence below reverses the usual expectation for the last of these: in Loprinzi et al. (2019), exercise four or more hours after learning had the largest effect (d = 1.05, though from only two studies, 95% CI 0.32–1.78), and van Dongen et al. (2016) found a benefit only for exercise four hours after learning, not immediately after. The post-encoding window is the most theoretically interesting because it isolates effects on consolidation rather than on encoding itself, but results across studies are mixed, with effect sizes varying by exercise intensity, duration, and memory type (e.g., motor vs. verbal vs. spatial memory). Exercise during learning slightly impaired memory (d = −0.12) and exercise before learning had a small, non-significant effect (d = 0.11).

**Moderators and boundary conditions.** Key moderators remain unresolved: the dose (intensity × duration) that reliably elevates consolidation-relevant physiology without degrading encoding; whether effects generalize from laboratory word-list and motor tasks to classroom learning; and how long any memory benefit persists beyond immediate or short-delay tests. Very intense exercise immediately before learning can impair encoding through fatigue and resource competition (unsourced on this page), so the same bout that helps consolidation can hurt acquisition — timing and dose must be considered jointly rather than as independent levers. The two studies recorded below (Loprinzi et al. 2019; van Dongen et al. 2016) speak to the timing of exercise after learning; neither settles the dose question or classroom generalisation.

**Practical framing.** If the timing effect is confirmed, it suggests scheduling physical activity after demanding learning episodes, with the current evidence favouring a delay of some hours over immediately afterwards, rather than treating exercise as a generic, time-independent learning enhancer. This connects to broader claims that [Classroom physical activity increases children's on-task behaviour, with no consistent gain on attention or other cognitive tests](classroom-physical-activity-improves-attention.md), which concerns effects during learning rather than consolidation after it. Designers should also weigh any consolidation benefit against the risk that a strenuous break adds load or fatigue that competes with subsequent lessons [-M] — see [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md)

**Open questions.** Whether the effect is driven by arousal (inverted-U), by molecular signaling (BDNF, noradrenaline), or both; whether the optimal window differs for declarative versus motor skill learning; and whether chronic exercise training changes the acute-response profile are all unresolved and should temper strong instructional prescriptions.

## Learner Variables
- [Long-Term Memory](../learner-variables/long-term-memory.md) — outcome: instruction changes it
- [Physical Well-Being](../learner-variables/physical-wellbeing.md) — moderator: an instructional effect differs with it

## Related Claims

- [Classroom physical activity increases children's on-task behaviour, with no consistent gain on attention or other cognitive tests](classroom-physical-activity-improves-attention.md) — exercise during instruction affects attention and engagement in the moment, complementing post-encoding consolidation effects
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — any exercise benefit must be weighed against added load or fatigue competing with encoding
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — encoding quality sets the ceiling on what consolidation can strengthen, so exercise timing interacts with how material is structured
- [Exercise Increases Hippocampal Volume](exercise-increases-hippocampal-volume.md) — related
- [Physical Experience Enhances Science Learning](physical-experience-enhances-science-learning.md) — related
- [Whether timing, intensity, and duration of class size reduction moderate its effect remains an open question in the literature the review synthesises](timing-intensity-duration-moderators-open-question.md) — related
- [Physical well-being — exercise, sleep, and nutrition — impacts learning](physical-wellbeing-impacts-learning.md) — a broader claim this one bears on
- [A combined model of demographics, aerobic fitness, and the two critical activity windows accounts for over 30% of variance in long-term memory retention](combined-model-memory-retention-variance.md) — related
- [A single bout of open-skill exercise improves short-term memory performance in primary-school children of both age groups (7–8 and 9–10 years).](open-skill-exercise-improves-stm-both-ages.md) — related
- [Spending more time sedentary 1 to 2 hours after encoding is associated with better long-term memory retention, implying physical activity in that window is detrimental](post-encoding-activity-detrimental-to-memory.md) — related
- [Physical activity in the hour before memory retrieval is associated with superior memory retention, while sedentary time in that window is negatively associated](pre-retrieval-activity-benefits-memory.md) — a narrower finding that bears on this claim
- [Acute exercise produces an overall small positive effect on cognition, with executive functions benefiting most and effects lasting up to two hours post-exercise](acute-exercise-small-positive-executive-cognition-effect.md) — related
- [Short-duration anaerobic sprint exercise speeds vocabulary-type associative learning by 20% with increased serum BDNF that correlates with learning success](anaerobic-sprint-bdnf-associative-learning.md) — related
- [Exercise performed four hours, but not immediately, after encoding enhances 48-hour retention of picture-location associations and hippocampal pattern similarity](delayed-post-learning-exercise-enhances-retention.md) — a narrower finding that bears on this claim
- [Greater aerobic fitness is associated with more stable long-term memory retention over 12 hours in young adults](aerobic-fitness-predicts-memory-retention.md) — related
- [Total percentage of time spent sedentary or in moderate-to-vigorous physical activity during the day is unrelated to long-term memory retention in young adults](total-daily-activity-unrelated-to-long-term-memory.md) — related
- [Motor activities combined with high integration and high relevance produce the largest positive effects on memory, per a meta-analysis cited by the review](high-integration-relevance-motor-activity-memory-effects.md) — related
- [Contrary to predictions, post-practice cardiovascular exercise produced no detectable effect on between-session offline change scores](cve-no-effect-between-session-offline-learning-pd.md) — a narrower finding that bears on this claim
- [Even a substantially increased declarative-load intervening task placed late in training does not impair the post-rest gain (Experiment 2)](increased-declarative-load-late-no-impairment-experiment-2.md) — related
- [A preceding bout of HIIT exercise produced no detectable difference in micro-consolidation of an implicit motor sequence learned in close temporal proximity to exercise](hiit-does-not-modify-micro-consolidation.md) — related
- [Force error increased at retention for the rest group but not the exercise group](force-error-retention-group-by-time.md) — a narrower finding that bears on this claim
- [Exercise eliminated the offline skill decline seen after rest: the rest group lost skill over the 6-hour delay while the exercise group did not](hiit-preserves-skill-over-six-hour-retention.md) — a narrower finding that bears on this claim
- [High-intensity exercise prior to practice reduced skill acquisition in older adults, with the detriment specific to the oldest participants](hiit-reduces-motor-acquisition-oldest-older-adults.md) — related
- [Cognitive control strategies enhanced young children's coding skills, with attention during learning related to coding outcomes](cognitive-control-strategies-improve-coding-skills-attention-linked.md) — a narrower finding that bears on this claim