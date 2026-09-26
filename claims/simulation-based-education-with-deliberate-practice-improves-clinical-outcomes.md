---
type: claim
title: Simulation Based Education With Deliberate Practice Improves Clinical Outcomes
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: simulation-based-education-with-deliberate-practice-improves-clinical-outcomes
evidence_strength: moderate
sources:
  - id: mcgaghie-et-al-2011
    resource: "https://doi.org/10.1097/acm.0b013e318217e119"
    title: "McGaghie, W. C., Issenberg, S. B., Cohen, E. R., Barsuk, J. H., & Wayne, D. B. (2011). Does Simulation-Based Medical Education With Deliberate Practice Yield Better Results Than Traditional Clinical Education? A Meta-Analytic Comparative Review of the Evidence. *Academic Medicine, 86*(6), 706–711. [doi:10.1097/acm.0b013e318217e119](https://doi.org/10.1097/acm.0b013e318217e119)"
    author: "McGaghie, W. C., Issenberg, S. B., Cohen, E. R., Barsuk, J. H., & Wayne, D. B."
    q: 3
    i: 2
    n: 14 studies
---

# Simulation Based Education With Deliberate Practice Improves Clinical Outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment · `i2` medium · n=14 studies

Simulation-based education that incorporates deliberate practice — repeated, goal-directed rehearsal with immediate feedback and increasing difficulty — improves clinical skill performance and, in some domains, patient-level outcomes.

## Subclaims

`q3 i2` A meta-analysis of 14 studies (1990–2010) found simulation-based medical education with deliberate practice (SBME+DP) produced a medium-sized advantage in clinical skill acquisition over traditional clinical education. [→ McGaghie et al. 2011](#mcgaghie-et-al-2011)

## Evidence

### McGaghie et al. 2011

McGaghie, W. C., Issenberg, S. B., Cohen, E. R., Barsuk, J. H., & Wayne, D. B. (2011). Does Simulation-Based Medical Education With Deliberate Practice Yield Better Results Than Traditional Clinical Education? A Meta-Analytic Comparative Review of the Evidence. *Academic Medicine, 86*(6), 706–711. [doi:10.1097/acm.0b013e318217e119](https://doi.org/10.1097/acm.0b013e318217e119)

`q3 · meta-analysis (14 studies, comparative-effectiveness design, not pre-registered)` · `i2 · medium effect, d=0.71` · `n=14 studies`

Systematic review and meta-analysis of 3,742 identified articles, of which 14 met inclusion criteria comparing traditional clinical medical education against simulation-based medical education (SBME) that incorporated deliberate practice (DP) — repeated, goal-directed rehearsal with mastery standards and immediate feedback. Across the 14 studies (mostly randomized trials and pre/post comparisons of procedural and psychomotor clinical skills such as ACLS, laparoscopic and central-line procedures), the pooled effect size favoring SBME with DP was d = 0.71 (95% CI 0.65–0.76, P < .001). The authors describe the result as consistent and "without exception" across the included studies, supporting skill-acquisition outcomes; they note the number of studies is still small and call for further research to extend the finding to broader clinical and patient-level outcomes.

## Discussion

**Mechanism.** The claim rests on the deliberate practice framework: skills improve when learners perform at the edge of their ability, receive immediate diagnostic feedback, and repeat tasks until mastery criteria are met. Simulation provides a safe environment for this cycle, allowing errors without patient harm — a structural advantage over learning purely in vivo. This aligns with [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md), in which coached practice and articulation of expert reasoning are central, and with [practice](../elements/practice.md) as the active element rather than exposure or observation.

**Boundary conditions.** Simulation alone is not sufficient; the deliberate practice component — mastery standards, feedback, and repetition — appears to be the active ingredient. A single simulation exposure without structured feedback or measurable performance benchmarks is unlikely to transfer to clinical settings. Designers should treat simulation sessions as practice embedded in a feedback loop, not as demonstrations. Feedback quality matters: see [Feedback improves learning](feedback-improves-learning.md) — simulation debriefing is essentially structured feedback on authentic performance.

**Transfer and scope.** Evidence for patient-level outcomes is narrower than evidence for skill outcomes: improvements in learner performance are well documented, but demonstrating that trained skills change clinical care or patient results requires longer follow-up and larger samples, and effects attenuate when skills are not refreshed or used in practice. Simulation-based training should therefore be paired with spaced booster sessions and workplace application — consistent with [spaced practice improves retention](spaced-practice-improves-retention.md) and [testing/practice effects](retrieval-practice-improves-retention.md). Transfer is strongest when the simulation task closely matches the clinical task's cognitive demands, echoing [cognitive load management](../principles/cognitive-load-management.md): overly complex scenarios can overwhelm novices, while overly simple ones fail to push learners to the edge of their ability.

**Design implications.** Effective programs set explicit mastery benchmarks, require learners to continue until criteria are met rather than for a fixed time, use immediate expert or technology-based feedback, and increase task difficulty across repetitions. Debriefing quality is a key moderator — reflective debriefing converts a rehearsal into a learning event.

**Open questions.** The dose–response relationship between amount of deliberate practice and magnitude of clinical outcome improvement is not well characterized, and most evidence comes from procedural and psychomotor skills; transfer to complex team-based or decision-making competencies is less firmly established. Cost and faculty time for high-quality feedback loops remain practical barriers to scaling mastery-based simulation.

## Related Claims

- [Feedback improves learning](feedback-improves-learning.md) — immediate diagnostic feedback is the active ingredient linking simulation to skill gains.
- [Spaced practice improves retention](spaced-practice-improves-retention.md) — booster sessions counter skill decay after simulation training.
- [Retrieval practice improves learning](retrieval-practice-improves-retention.md) — repeated rehearsal under realistic conditions strengthens durable skill.
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — coached practice, articulation, and reflection frame simulation as authentic apprenticeship.
- [Deliberate practice improves performance](deliberate-practice-improves-performance.md) — the underlying framework: goal-directed repetition at the edge of ability.
- [Deliberate practice interventions produce higher real estate licensing exam pass rates than traditional study methods](deliberate-practice-raises-licensing-pass-rate.md) — related
- [Process-tracing measures should accompany outcome measures because process changes may not be immediately reflected in outcomes](process-tracing-measures-for-learning.md) — related
- [Simulation Based Education Improves Outcomes](simulation-based-education-improves-outcomes.md) — a broader claim this one bears on