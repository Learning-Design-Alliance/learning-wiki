---
type: claim
title: Presenting multiple cases from different perspectives supports transfer in ill-structured domains
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: cft-multiple-cases
evidence_strength: weak
---

# Presenting multiple cases from different perspectives supports transfer in ill-structured domains

Cognitive Flexibility Theory holds that ill-structured domains — where concepts vary unpredictably across situations — require learners to encounter the same content in multiple cases and from multiple conceptual perspectives, so knowledge is assembled flexibly rather than stored as a single oversimplified schema.

## Subclaims

<!-- TODO -->

## Evidence

<!-- TODO -->

## Discussion

**Scope.** The claim is deliberately restricted to ill-structured domains such as medicine, law, history, and complex management problems. In well-structured domains (e.g., introductory physics problem sets), a single well-formed schema may suffice, and the overhead of criss-crossing multiple cases may not pay off [~M]. The theory's core mechanisms — multiple knowledge representations, criss-crossing the landscape, and avoiding oversimplification — predict that single-case instruction produces knowledge that is inert when the situation changes [-M].

**Moderators and boundary conditions.** The theory was developed by Spiro and colleagues in the late 1980s partly as a critique of reductive schemas and analogies applied to complex content; it predicts that oversimplified representations actively mislead learners in ill-structured domains [-M]. The approach presupposes substantial prior knowledge to compare across cases, so it is better suited to intermediate and advanced learners than to novices, who may lack the working-memory resources to process several cases simultaneously — consistent with the broader expertise-reversal pattern described in [Expertise reversal effect](../theories/expertise-reversal-effect.md) [~M]. Case quality matters: cases must genuinely differ in how the target concept manifests, or learners extract a single rigid interpretation anyway [-M]. Superficially similar cases also impose comparison costs without flexibility gains, so case selection — not just case quantity — is the primary design lever.

**Design implications.** Practitioners implementing this claim typically sequence several [case studies](../elements/case-studies.md) that share a core concept but differ in surface features and in how the concept plays out, then prompt learners to articulate what changes and what stays constant across cases — the comparison mechanism described in [Analogical reasoning improves transfer](analogical-reasoning-improves-transfer.md). Deliberately conflicting cases can also induce the productive tension described in [Cognitive disequilibrium motivates conceptual change](cognitive-disequilibrium-motivates-conceptual-change.md). The [Cognitive Flexibility Theory](../patterns/cognitive-flexibility-theory.md) pattern operationalizes this as "criss-crossing" the case landscape: revisiting the same concept from different cases and perspectives rather than covering each case once. Hypertext and other non-linear formats were the original delivery vehicles for this criss-crossing, but the mechanism transfers to any format that lets learners revisit a concept from multiple case entry points. Because processing several cases at once taxes working memory, designers should scaffold comparisons — highlighting the shared concept and the dimension along which cases diverge — consistent with [Cognitive load management](../principles/cognitive-load-management.md).

**Open questions.** The stub currently has no evidence entries; the foundational studies (e.g., Spiro et al.'s work on knowledge representation in complex domains and the KANE hypertext experiments) still need to be added before this claim can carry evidence-strength ratings. Practitioners should treat the design guidance as theory-driven rather than meta-analytically confirmed at present [~W]. The closest classroom-level evidence is the multiple-case instruction literature summarized in [Case-based learning improves exam performance](case-based-learning-improves-exam-performance.md), but that evidence does not isolate the multiple-perspective manipulation this claim specifies. A second open question is dosage: how many cases, and how much variation between them, are needed before flexibility gains appear — the literature offers no established minimum. A third is whether the hypothesized advantage over well-structured single-case instruction shows up on delayed transfer measures rather than immediate post-tests, which is where the theory predicts its effects should be largest.

## Related Claims

- [Case-based learning improves exam performance](case-based-learning-improves-exam-performance.md) — the closest empirical sibling: multiple-case instruction in classroom settings
- [Analogical reasoning improves transfer](analogical-reasoning-improves-transfer.md) — comparison across cases is the mechanism CFT prescribes, but CFT warns against single-source analogies
- [Cognitive disequilibrium motivates conceptual change](cognitive-disequilibrium-motivates-conceptual-change.md) — conflicting cases create the productive disequilibrium CFT exploits
- [Cognitive Flexibility Theory](../patterns/cognitive-flexibility-theory.md) — the parent instructional pattern this claim underwrites
- [Cognitive flexibility](../principles/cognitive-flexibility.md) — the underlying learner capability
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — bounds the claim: novices may be harmed by multi-case complexity that benefits advanced learners
- [Case studies](../elements/case-studies.md) — the primary instructional element for implementing multiple-case sequences