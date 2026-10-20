---
type: claim
title: Access to AI advice roughly doubled reported confidence in answers in one experiment
description: Access to AI advice roughly doubled reported confidence in answers in one experiment
id: ai-access-inflates-confidence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: chiara-marcoccia-2026
    resource: "https://doi.org/10.31234/osf.io/5y6m4_v1"
    title: "Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro. (2026). AI advice suppresses people's willingness to say \"I don't know\", even when the advice is wrong and accuracy is incentivized. https://osf.io/nwx6r/overview?view_only=a03ae0ca587c4c84a442c44d55ab97b6 [doi:10.31234/osf.io/5y6m4_v1](https://doi.org/10.31234/osf.io/5y6m4_v1)"
    author: Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro
    q: 3
    i: "?"
    kind: causal
    rigour: 3
  - id: chiara-marcoccia-2026-2
    resource: "https://osf.io/nwx6r/overview?view_only=a03ae0ca587c4c84a442c44d55ab97b6"
    title: "Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro. (2026). AI advice suppresses people's willingness to say \"I don't know\", even when the advice is wrong and accuracy is incentivized. https://osf.io/nwx6r/overview?view_only=a03ae0ca587c4c84a442c44d55ab97b6"
    author: Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro
    q: 3
    i: "?"
    kind: causal
    rigour: 3
---

# Access to AI advice roughly doubled reported confidence in answers in one experiment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r3` · `q3`

## Subclaims
`q3 i?` AI advice nearly doubled reported confidence on a 0–100 scale (29.6 vs. 75.9 without stakes; 37.7 vs. 73.5 with stakes). [→ Chiara Marcoccia 2026](#chiara-marcoccia-2026)
`q3 i?` Stakes raised confidence only when AI advice was unavailable; the confidence increase disappeared when AI advice was available (significant interaction). [→ Chiara Marcoccia 2026 (2)](#chiara-marcoccia-2026-2)

## Evidence

### Chiara Marcoccia 2026

Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro. (2026). AI advice suppresses people's willingness to say "I don't know", even when the advice is wrong and accuracy is incentivized. https://osf.io/nwx6r/overview?view_only=a03ae0ca587c4c84a442c44d55ab97b6 [doi:10.31234/osf.io/5y6m4_v1](https://doi.org/10.31234/osf.io/5y6m4_v1)

`q3 · i?` · `causal · r3`

Study 2 secondary measure: after each question participants rated confidence on a continuous 0–100 scale. The article reports a "large main effect of AI advice, which nearly doubled reported confidence"; no standardized effect size printed.

> "Confidence judgments revealed a large main effect of AI advice, which nearly doubled reported confidence (29.6 vs. 75.9 without stakes; 37.7 vs. 73.5 with stakes)"

### Chiara Marcoccia 2026 (2)

Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro. (2026). AI advice suppresses people's willingness to say "I don't know", even when the advice is wrong and accuracy is incentivized. https://osf.io/nwx6r/overview?view_only=a03ae0ca587c4c84a442c44d55ab97b6

`q3 · i?` · `causal · r3`

Study 2 simple slopes for the significant stakes × AI interaction on confidence (b = −10.509, p = .006): stakes raised confidence only "when participants could not seek AI advice". No standardized effect size printed.

> "Monetary stakes increased confidence when participants could not seek AI advice (29.6 vs. 37.7; b = 8.083, SE = 3.163, t = 2.556, p = .011), but this effect disappeared when AI advice was available (75.9 vs. 73.5; b = −2.426, SE = 2.216, t = −1.095, p = .274; see Figure 2b)."

## Studies bearing on this claim

<!-- synthesis:start -->
*Does working with AI make learners' judgments of their own knowledge, effort and performance less accurate, and what restores them?* This table gathers the studies behind this claim and the 13 narrower claims that bear on it: **8 distinct studies** (6 causal, 1 theoretical, 1 review), `q2`–`q4`, 2 of 8 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Chiara Marcoccia 2026](https://doi.org/10.31234/osf.io/5y6m4_v1) | q3 · causal · r3 | i? | this claim |
| [Bastani Hamsa 2025](https://doi.org/10.1073/pnas.2422633122) | q2 · causal · r3 | i? | [Students do not perceive the learning harm from copying GPT solutions and overestimate the](students-unaware-of-ai-learning-harm.md) (supports) |
| [Fernandes 2026](https://doi.org/10.48550/arxiv.2605.25856) | q3 · causal · r2 | i3; i1; i2 | [Participants substantially overestimated their performance in all trace conditions, with t](overestimation-largest-under-full-traces.md) (supports); [Full reasoning traces worsened calibration bias and Brier scores relative to both other co](full-traces-worsen-calibration-and-brier-scores.md) (supports) |
| [Sunny Yu 2026](https://doi.org/10.48550/arxiv.2605.22687) | q3 · causal · r3 | i? | [People overestimate how much time AI assistance saves (speedup illusion), driven by miscal](speedup-illusion-ai-assisted-time-underestimation.md) (supports); [People significantly underestimate AI-assisted completion times even though actual AI-assi](speedup-illusion-ai-assisted-time-underestimation.md) (supports); [People overestimate how much mental effort AI assistance alleviates (offloading illusion),](offloading-illusion-ai-effort-savings.md) (supports); [People are well-calibrated about their own independent completion times](accurate-independent-completion-time-predictions.md) (qualifies); [Participants more averse to thinking are more susceptible to the speedup illusion; AI fami](thinking-aversion-predicts-speedup-illusion.md) (qualifies) |
| [Dongming Mei 2026](https://doi.org/10.48550/arxiv.2605.09624) | q2 · theoretical · r2 | i? | [AI assistance can inflate confidence even after errors and reduce accuracy when AI is faul](cognitive-surrender-inflates-confidence-after-errors.md) (supports) |
| [Qusay H. Mahmoud 2026](https://doi.org/10.48550/arxiv.2609.29473) | q2 · review · r3 | i? | [Task completion with GenAI is a weak proxy for durable competence, with struggling learner](task-completion-weak-proxy-competence.md) (supports) |
| [Benjamin Lira 2025](https://doi.org/10.48550/arxiv.2502.02880) | q4 · causal · r3 | i? | [Practicing with AI did not create an illusion of mastery: participants reported learning a](no-illusion-of-mastery-from-ai-practice.md) (counts against) |
| [Ren S 2026](https://doi.org/10.3389/fpsyg.2026.1926110) | q2 / q3 · causal · r2 | i3; i1; i? | [Reflection improves correspondence between perceived and behavioral reliance on ChatGPT](reflection-improves-awareness-calibration.md) (qualifies); [Better awareness calibration co-occurs with lower incorrect-advice acceptance and lower at](calibration-negatively-associated-overreliance.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

## Learner Variables
- [Metacognition](../learner-variables/metacognition.md) — outcome: instruction changes it

## Related Claims

- [Self-efficacy judgments correspond less well to behavior in learning settings than in performance settings](self-efficacy-accuracy-lower-in-learning-settings.md) — the general claim this finding bears on, with the studies behind it
- [Merely having access to AI advice nearly eliminates people's willingness to suspend judgment under uncertainty, even when the advice is wrong](ai-access-nearly-eliminates-judgment-suspension.md) — related
- [Monetary incentives for accuracy improve answer correctness specifically when AI advice is available, by reducing reliance on that advice](stakes-improve-accuracy-specifically-with-ai.md) — related
- [Monetary stakes for accuracy act independently of AI availability on judgment suspension, with no significant AI × stakes interaction](stakes-independent-of-ai-on-suspension.md) — related
- [AI advice dramatically reduces judgment suspension even when it is displayed automatically rather than actively requested](unsolicited-ai-advice-still-suppresses-suspension.md) — related
- [Participants seek AI advice less frequently when accuracy carries monetary stakes](stakes-reduce-ai-advice-seeking.md) — related
- [AI assistance can inflate confidence even after errors and reduce accuracy when AI is faulty (cognitive surrender)](cognitive-surrender-inflates-confidence-after-errors.md) — related
- [88% of AI-assisted students reported increased self-efficacy and confidence during independent practicals](ai-feedback-88-percent-self-efficacy-increase.md) — related
- [Practicing with AI did not create an illusion of mastery: participants reported learning and skill levels similar to other conditions](no-illusion-of-mastery-from-ai-practice.md) — related
