---
type: claim
title: Retrieval Practice Improves Transfer
status: review
generated:
  by: claude/unspecified
  at: 2026-09-25
id: retrieval-practice-improves-transfer
evidence_strength: provisional
sources:
  - id: pan-rickard-2018
    resource: "https://doi.org/10.1037/bul0000151"
    title: "Pan, S. C., & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. *Psychological Bulletin, 144*(7), 710–756. [doi:10.1037/bul0000151](https://doi.org/10.1037/bul0000151)"
    author: "Pan, S. C., & Rickard, T. C."
    q: 4
    i: 2
    n: 122 experiments (192 effect sizes, N=10,382)
    kind: quant-synthesis
    rigour: 2
  - id: butler-2010
    resource: "https://doi.org/10.1037/a0019902"
    title: "Butler, A. C. (2010). Repeated testing produces superior transfer of learning relative to repeated studying. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 36*(5), 1118–1133. [doi:10.1037/a0019902](https://doi.org/10.1037/a0019902)"
    author: Butler, A. C.
    q: 3
    i: "?"
    n: 4 experiments
    kind: causal
    rigour: "?"
---

# Retrieval Practice Improves Transfer

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r?`, 1 quant-synthesis `r2` · `q3`–`q4` · `i2` medium

Practicing retrieval of learned material (rather than rereading or restudying) improves learners' ability to apply that knowledge to new problems and contexts, not just to recall it verbatim.

## Subclaims

`q4 i2` Across 192 transfer effect sizes, practice testing produced transfer relative to non-testing re-exposure (d = 0.40), but the benefit is greatest for application/inference questions and changed test formats, weakest for rearranged items and untested material, and bias-corrected estimates often show no positive transfer when favourable moderators are absent. [→ Pan & Rickard 2018](#pan-rickard-2018)

`q3 i?` In four experiments with prose passages, repeated testing produced better one-week performance than repeated restudying on new inferential questions, both within the same knowledge domain and across different domains. [→ Butler 2010](#butler-2010)

## Evidence

### Pan & Rickard 2018

Pan, S. C., & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. *Psychological Bulletin, 144*(7), 710–756. [doi:10.1037/bul0000151](https://doi.org/10.1037/bul0000151)

`q4 · meta-analysis` · `i2 · medium effect, d=0.40` · `n=122 experiments (192 effect sizes, N=10,382)` · `quant-synthesis · r2`

A random-effects meta-analysis of 67 published and unpublished articles spanning more than 40 years, comparing practice testing with a non-testing re-exposure control on transfer tests. Testing yielded transferable learning overall (d = 0.40, 95% CI [0.31, 0.50]), strongest across test formats, to application and inference questions, and to medical-diagnosis problems, and weakest to rearranged stimulus-response items, to untested material seen during study, and to worked-example problems. Response congruency, elaborated retrieval practice and initial test performance strongly moderated transfer. Publication-bias corrections (PET-PEESE and selection methods) left moderator effects largely intact but substantially reduced the intercept, often indicating no positive transfer when none of those moderators is present — a significant qualification of the unconditional claim.

### Butler 2010

Butler, A. C. (2010). Repeated testing produces superior transfer of learning relative to repeated studying. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 36*(5), 1118–1133. [doi:10.1037/a0019902](https://doi.org/10.1037/a0019902)

`q3 · peer-reviewed experiment` · `i? · no effect size in the abstract read` · `n=4 experiments` · `causal · r?`

Participants studied prose passages and then either repeatedly restudied them or took repeated tests on them. A week later the final test used the same questions (Experiment 1a), new inferential questions from the same knowledge domain (Experiments 1b and 2), or new inferential questions from different knowledge domains (Experiment 3). Repeated testing produced better retention and transfer than repeated studying in every case, indicating the benefit is not limited to the specific response practised.

## Studies bearing on this claim

<!-- synthesis:start -->
*Does the benefit carry to new questions, inferences and applications, or only to the items practised?* This table gathers the studies behind this claim and the 11 narrower claims that bear on it: **6 distinct studies** (3 quant-synthesis, 2 causal, 1 review), `q2`–`q4`, 4 of 6 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Pan & Rickard 2018](https://doi.org/10.1037/bul0000151) | q4 · quant-synthesis · r2 | i2 · medium effect, d=0.40; i2; i? | this claim; [Practice testing yields transferrable learning relative to a nontesting reexposure control](testing-yields-transfer-versus-reexposure-control-d-040.md) (supports); [Transfer of test-enhanced learning is greatest across test formats, to application and inf](transfer-greatest-test-formats-application-inference-medical-mediator-cues.md) (supports); [Transfer of test-enhanced learning is weakest to rearranged stimulus-response items, to un](transfer-weakest-rearranged-untested-materials-worked-examples.md) (qualifies); [Response congruency, elaborated retrieval practice, and initial test performance strongly ](moderators-congruency-elaborated-retrieval-initial-test-performance.md) (qualifies) |
| [Butler 2010](https://doi.org/10.1037/a0019902) | q3 · causal · r? | i? | this claim |
| [Adesope 2017](https://doi.org/10.3102/0034654316689306) | q4 · quant-synthesis · r3 | i2 | [Practice tests benefit retention (g = 0.63) and transfer (g = 0.53) outcomes without a sig](practice-tests-aid-retention-and-transfer.md) (supports) |
| [Karpicke 2017](https://doi.org/10.1016/b978-0-12-809324-5.21055-9) | q2 · review · r3 | i?; i0 | [Retrieval practice enhances performance on final inference and transfer questions relative](retrieval-practice-improves-final-inference-and-transfer-questions.md) (supports); [Practicing retrieval of some portions of an educational text can enhance retention of rela](retrieval-induced-facilitation-of-nontested-text-material-requires-relational-encoding.md) (qualifies); [Retrieval practice effects on mediator-cued final tests have been positive, but Coppens et](mediator-cued-final-test-effects-of-retrieval-practice-may-be-small.md) (qualifies) |
| [Nero 2021](https://doi.org/10.24191/ajue.v17i4.16222) | q3 · causal · r2 | i? | [After retrieval practice, undergraduates score significantly higher on lower-order thinkin](retrieval-practice-lower-order-questions-outscore-higher-order-questions.md) (qualifies); [The effect of retrieval practice format on reading comprehension does not differ significa](retrieval-format-by-levels-of-thinking-interaction-not-significant.md) (qualifies) |
| [Donoghue & Hattie 2021](https://doi.org/10.3389/feduc.2021.581216) | q3 · quant-synthesis · r? | i1 · small effect on deep outcomes, d = 0.26 (0.60 surface); far transfer d = 0.39 | [Learning techniques have much smaller effects on deep learning and far transfer than on su](learning-techniques-smaller-effects-on-deep-learning-and-far-transfer.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

**Scope of the claim.** The retrieval-practice literature distinguishes near transfer (applying knowledge to reworded or slightly varied problems) from far transfer (applying it to novel problem types or domains). The strongest documented benefits are for retention and near transfer; evidence for far transfer is thinner and more contested. Designers should treat "retrieval improves transfer" as most defensible when the transfer task shares structural features with the practiced material.

**Mechanism.** Retrieval is hypothesized to improve transfer because it forces learners to reconstruct knowledge and make it accessible under varied cues, rather than merely re-encountering it. Successful retrieval also consolidates memories and can reveal gaps that restudy conceals. This connects to [Spaced practice improves long-term retention](spaced-practice-improves-retention.md) — retrieval and spacing interact multiplicatively, with spaced retrieval producing the largest durable gains.

**Moderators and boundary conditions.** Retrieval practice benefits depend on successful retrieval: if learners fail to retrieve and receive no corrective feedback, the attempt can reinforce errors. Feedback after retrieval, and retrieval tasks that require some reconstruction (short answer, generation) rather than pure recognition, are generally associated with better outcomes — see [Feedback improves learning outcomes](feedback-improves-learning.md). As with [worked examples](../elements/demonstration.md), an expertise dimension likely applies — highly fluent learners may gain little from low-difficulty retrieval, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md).

**Design implications.** To bias retrieval toward transfer rather than verbatim recall, vary the surface features of retrieval questions so learners must extract the underlying structure, and interleave retrieval across related topics rather than blocking by type. Pure recognition formats (multiple choice) are efficient for retention but provide weaker reconstruction demands than short-answer or generation formats. Successful retrieval also depends on material being within working-memory limits — see [Chunking reduces working memory load](chunking-reduces-working-memory-load.md).

**Open questions.** How retrieval practice supports transfer to genuinely novel problem structures, and how much task variability during retrieval is needed to produce flexible knowledge, remain active research questions. Two entries are recorded: a meta-analysis of 122 experiments (Pan & Rickard 2018, d = 0.40, but bias-corrected estimates often show no positive transfer when its favourable moderators are absent) and four laboratory experiments with prose passages (Butler 2010). Neither tests far transfer to new problem structures in classroom settings, so the claim is best read as conditional on those moderators. <!-- deprecated (2026-10-05, stale beside two recorded entries): Until evidence entries are added, the strength of this specific transfer claim should be treated as provisional. -->

## Related Claims

- [Spaced practice improves long-term retention](spaced-practice-improves-retention.md) — spacing and retrieval interact; spaced retrieval is the strongest durable-learning combination
- [Testing improves retention of learned material](retrieval-practice-improves-retention.md) — the core testing effect on retention, of which transfer is an extension
- [Feedback improves learning outcomes](feedback-improves-learning.md) — feedback after retrieval attempts is a key moderator of retrieval benefits
- [Desirable difficulties enhance learning](desirable-difficulties-enhance-learning.md) — retrieval practice is the canonical desirable difficulty
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — successful retrieval depends on material being within working-memory limits
- [The benefits of retrieval practice do not depend on an exact match between initial retrieval practice conditions and the final test format](retrieval-practice-benefits-do-not-require-matching-initial-and-final-test-formats.md) — related
- [Retrieval practice enhances performance on final inference and transfer questions relative to restudying, although a single-word fill-in-the-blank task did not](retrieval-practice-improves-final-inference-and-transfer-questions.md) — a narrower finding that bears on this claim
- [Students given retrieval practice instructions spontaneously used a repeated retrieval strategy on new materials one week later without further instructions](spontaneous-strategy-transfer-one-week-delay.md) — related
- [The authors attribute the spaced-practice knowledge benefit to deeper learning or transfer, because quiz and final-test items were never repeated](spaced-practice-benefit-reflects-transfer-not-item-memorization.md) — related
- [The review reports that simulation games support near transfer of knowledge but evidence for long-term or far transfer is less robust](simulation-near-transfer-robust-far-transfer-weak.md) — related
- [The classroom testing effect transfers to mismatched test formats, but consistent quiz–exam formats yield a significantly larger effect (g = 0.531 vs. g = 0.399).](format-consistency-moderates-classroom-testing-effect.md) — a narrower finding that bears on this claim
- [Effects of pre-instruction testing on untested but studied materials are highly inconsistent across experiments and materials](pretesting-untested-materials-inconsistent.md) — related
- [Testing benefits retention over a conservative restudy control, establishing the testing effect as robust](testing-effect-robust-versus-restudy-control.md) — related
- [Practice testing yields transferrable learning relative to a nontesting reexposure control condition (d = 0.40)](testing-yields-transfer-versus-reexposure-control-d-040.md) — possibly the same claim (merge candidate)
- [Transfer of test-enhanced learning is greatest across test formats, to application and inference questions, to medical diagnosis problems, and to mediator and related word cues](transfer-greatest-test-formats-application-inference-medical-mediator-cues.md) — possibly the same claim (merge candidate)
- [Transfer of test-enhanced learning is weakest to rearranged stimulus-response items, to untested materials seen during initial study, and to problems involving worked examples](transfer-weakest-rearranged-untested-materials-worked-examples.md) — possibly the same claim (merge candidate)
- [Testing effects are stronger when practice and final test formats are identical (g = 0.63) than dissimilar (g = 0.53), supporting transfer-appropriate processing](tap-identical-formats-stronger-effect.md) — related
- [Effects of implicit strategies (higher-order questioning, concept mapping, discussion) on CT are inconclusive, with domain-specific gains that fail to transfer](implicit-strategies-inconclusive-domain-specific-only.md) — related
- [Intervention types (cue-generation encoding-based, retrieval-based, cue-attention, cue-selection) do not substantially differ in effectiveness](intervention-types-no-substantial-difference.md) — related