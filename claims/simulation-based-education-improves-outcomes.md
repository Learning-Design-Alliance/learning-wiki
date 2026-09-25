---
type: claim
title: Simulation Based Education Improves Outcomes
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: simulation-based-education-improves-outcomes
evidence_strength: none
sources:
  - id: cook-et-al-2011
    resource: "https://doi.org/10.1001/jama.2011.1234"
    title: "Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Hamstra, S. J. (2011). Technology-Enhanced Simulation for Health Professions Education: A Systematic Review and Meta-analysis. *JAMA, 306*(9), 978–988. [doi:10.1001/jama.2011.1234](https://doi.org/10.1001/jama.2011.1234)"
    author: "Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Hamstra, S. J."
    q: 4
    i: 3
    n: 609 studies (35,226 trainees)
---

# Simulation Based Education Improves Outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i3` large · n=609 studies (35,226 trainees)

Simulation-based education — structured practice in interactive representations of real tasks (mannequins, virtual patients, flight simulators, role-play) — improves learning and performance outcomes relative to instruction without deliberate practice in the simulated environment.

## Subclaims

`q4 i3` Technology-enhanced simulation training for health professions learners produces large pooled effects on knowledge, skill and behavior outcomes, and a moderate effect on direct patient outcomes, relative to no intervention. [→ Cook et al. 2011](#cook-et-al-2011)

## Evidence

### Cook et al. 2011

Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Hamstra, S. J. (2011). Technology-Enhanced Simulation for Health Professions Education: A Systematic Review and Meta-analysis. *JAMA, 306*(9), 978–988. [doi:10.1001/jama.2011.1234](https://doi.org/10.1001/jama.2011.1234)

`q4 · systematic review and meta-analysis` · `i3 · large effect, pooled effect sizes ~1.09–1.20 for knowledge/skills/behaviors` · `n=609 studies (35,226 trainees)`

A systematic review and meta-analysis (search through May 2011 across MEDLINE, EMBASE, CINAHL, ERIC, PsycINFO, Scopus and other sources) identified 609 eligible studies of technology-enhanced simulation training (mannequins, virtual reality, part-task trainers, etc.) for physicians, nurses, dentists and other health professionals, compared against no intervention. Study designs included 137 randomized trials, 67 nonrandomized multi-group studies, and 405 single-group pretest-posttest studies. Pooled random-effects sizes versus no intervention were large for knowledge (g=1.20, 95% CI 1.04–1.35, k=118), time skills (g=1.14, k=210), process skills (g=1.09, k=426) and product skills (g=1.18, k=54), and moderate-to-large for behaviors (g≈0.79–0.81) and for direct effects on patients (g=0.50, 95% CI 0.34–0.66, k=32). Subgroup analyses found no consistent statistically significant interactions between simulation training and instructional-design features (curricular integration, distributed practice, feedback, mastery learning, repetitive practice) or study quality — heterogeneity was large (I²>50%) throughout, so this is a comparison against no intervention rather than against an equally-dosed non-simulation alternative, and it does not by itself establish which design features drive the effect.

## Discussion

**Scope and mechanism.** The claim is best understood as covering deliberate, structured practice with feedback in a simulated task environment, not passive exposure to a simulation. The plausible mechanisms are practice with immediate feedback, safe repetition of rare or high-risk scenarios, and transfer of procedural skill to real settings — consistent with [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) and [Situated Learning](../theories/situated-learning.md). Simulation is essentially a delivery vehicle for [deliberate practice](deliberate-practice-improves-performance.md) and [feedback](feedback-improves-learning.md); where those ingredients are absent, the simulation itself is unlikely to drive gains. This also places simulation within the broader evidence base for [active learning](active-learning-improves-exam-performance.md): the predicted advantage over lecture-only or demonstration-only instruction comes from learners performing the task, not from the technology.

**Moderators to establish.** The literature on simulation (especially in health professions education) suggests the effect depends heavily on design conditions: feedback quality, deliberate practice with repetition, curriculum integration, and fidelity being sufficient but not necessarily maximal. High physical fidelity without instructional alignment can waste resources; cognitive fidelity to the task's decisions often matters more than visual realism. These boundary conditions should be documented as evidence entries are added. Scenario complexity and fidelity must also be managed against working-memory limits, per [Cognitive Load Theory](../theories/cognitive-load-theory.md) — an overloaded simulation can degrade rather than support learning. Where simulation is embedded in a course rather than run as a stand-alone event, integration with assessment and [clear structure](clear-structure-improves-learning.md) around objectives is likely to moderate outcomes.

**Fidelity is not monotonic.** A recurring finding across simulation domains is that increasing physical realism beyond the point needed to support the target task yields diminishing or null returns, while mismatched fidelity can actively mislead learners by cueing irrelevant features. Designers should match fidelity to the learning objective — the decisions and cues the learner must attend to — rather than to available budget or technology. This parallels the expertise-reversal logic in [Cognitive Load Theory](../theories/cognitive-load-theory.md): more realism is not more instruction.

**Open questions.** Whether simulation outperforms well-designed non-simulated practice of equal duration, how durable the gains are over time, and how effects vary across domains (procedural vs. conceptual outcomes) all need citation-backed treatment before the claim can be rated. A further open question is cost-effectiveness: even where simulation improves outcomes, low-fidelity or paper-based alternatives may achieve comparable results at a fraction of the cost. Evidence entries should also distinguish learner-level outcomes (knowledge, skill) from patient- or system-level outcomes (e.g., safety events), since the strongest claims in the health professions literature concern the former. Comparisons with adjacent structured-practice formats — [case-based learning](case-based-learning-improves-exam-performance.md) and role-play — should record the comparison condition, since much of the apparent advantage of simulation may reduce to more practice time or more feedback rather than to the simulation per se.

**Rating withheld.** The meta-analysis recorded above compares simulation with no intervention, not with equally long non-simulation practice, so it cannot say whether simulation beats matched practice; its subgroup analyses found no significant interaction with feedback, repetition or fidelity. Further syntheses worth recording include the health-professions simulation meta-analytic literature (e.g., on simulation-based training versus non-simulation instruction) and aviation/military training-effectiveness research; each entry should record design conditions (feedback, repetition, fidelity, integration) so the moderators above can be tested rather than assumed.

## Related Claims

- [Feedback improves learning.](feedback-improves-learning.md) — feedback is the core active ingredient in most simulation designs
- [Deliberate practice improves performance.](deliberate-practice-improves-performance.md) — the practice mechanism simulation is typically built to deliver
- [Active learning improves exam performance.](active-learning-improves-exam-performance.md) — simulation is one active-learning modality
- [Case-based learning improves exam performance.](case-based-learning-improves-exam-performance.md) — adjacent structured-practice approach using realistic cases
- [Cognitive load theory](../theories/cognitive-load-theory.md) — fidelity and scenario complexity must be managed to avoid overload
- [Situated learning](../theories/situated-learning.md) — simulation works by approximating the authentic context in which skills will be used
- [Cognitive apprenticeship](../patterns/cognitive-apprenticeship.md) — simulation supports the coaching and articulation phases of the model