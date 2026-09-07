---
type: method
id: stakeholder-mapping
title: Stakeholder Mapping
description: A design method that enumerates the parties who participate in, govern, fund, or are affected by a learning activity, gives each a stable identity, and records only the relationships that change a design decision.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-07
---

# Stakeholder Mapping

> **Design Method** · [All design methods](index.md)

## Description
Stakeholder Mapping enumerates the parties with a stake in a learning activity — learners, instructors, the institution, an employer, a funder, a regulator, a community — and gives each one a durable identity the rest of the design can refer to. It then records the relationships that matter: who mandates the activity, who funds it, who evaluates it, who is affected by it without holding any say over it. Its output is a short registry rather than an organisation chart, and the discipline is in what it leaves out.

The method is the entry point to a family that runs from description to redistribution. Where the question is *who is in the room*, this is enough. Where the question is *who decides, and should they*, the harder sibling is [Make the Invisible Visible (Power Dynamics)](make-the-invisible-visible-power-dynamics.md).

## Design Implications

Most learning designs already carry their stakeholders implicitly — in a policy nobody can relax, a schedule nobody set, a certificate somebody else requires. Naming them converts those facts from constraints of unknown origin into constraints with an owner, which is the precondition for asking whether the owner would relax them. Stakeholder theory's founding move was exactly this: treating an organisation as accountable to a set of identified parties rather than to one, and identification is the step that makes the rest tractable.

The salience literature supplies the test that keeps the list short. Mitchell, Agle and Wood argue that a party's claim on attention comes from some combination of **power** (can it impose its will), **legitimacy** (is its claim proper) and **urgency** (does it require attention now), and that parties holding only one of the three are latent rather than definitive. A map that records every party equally is a map that says nothing about where design effort should go.

### Context
#### Requirements
- Somebody who has actually met the parties — a map assembled from an org chart records reporting lines rather than stakes
- A rule for what earns a place: each party must change a design decision, and the reason recorded beside it
- A convention for identity that the rest of the design already uses, so a party named here and a party named on an approval are recognisably the same entity

#### Constraints
- Analyst-led mapping produces the parties the analyst already knows; who is *missing* from a map is systematically harder to see than who is on it, and the party nobody invited is often the one whose interests the design overrides [~M]
- Stakeholder analysis conducted without any intention to act on it consumes the goodwill of the people consulted; participation with no visible consequence depresses willingness to participate again [-M]
- The technique is descriptive by construction. It surfaces who holds authority and is silent on whether they should, which is a limitation rather than a neutrality — see [Make the Invisible Visible (Power Dynamics)](make-the-invisible-visible-power-dynamics.md)
- Categories imposed by the analyst ("primary/secondary", "internal/external") can pre-decide the answer; the typology literature treats the choice of method as itself a design decision with consequences for who ends up counted [~M]

#### Implementation Variability
- **Registry only:** a list of parties with a one-line reason each — half an hour, and enough for most single-course designs
- **Registry plus relationships:** adds the directed edges that decide something (X mandates the learner, Y evaluates the deliverable) — the form a machine-readable design can act on
- **Interest/influence grid:** parties plotted on two axes to triage attention; fast, and prone to hardening a snap judgement into a diagram
- **Salience assessment:** power, legitimacy and urgency assessed per party, distinguishing definitive stakeholders from latent ones
- **Participatory mapping:** the parties build the map themselves, which surfaces relationships an analyst cannot see and changes the exercise into an intervention

### Target Learners
- Not a learner-facing method. Its subject is the design, and learners appear in it as one party among several
- Its indirect beneficiaries are learners whose constraints turn out to belong to a party who can relax them — an assessment policy, a device restriction, a scheduling rule
- Learners subject to a mandated activity, where naming the mandating party is what distinguishes a design for people who chose to be there from one for people who did not; motivation and its supports differ sharply between the two [Autonomy supports intrinsic motivation.](../claims/autonomy-supports-intrinsic-motivation.md) [+S]

### Target Learning Goals
- None directly. The method produces a design artifact, not instruction
- It bears on goals indirectly wherever a party other than the learner has a say in what counts as achievement — an accreditor, an employer, a professional body

### Instructions
1. **List the parties.** Everyone who participates in, governs, funds, evaluates, or is materially affected by the activity. Include the parties who are absent from every meeting.
2. **Give each a durable id.** Not a person's name — a role. The id is what the rest of the design refers to, so it has to survive staff turnover.
3. **Write the reason, not the description.** "The employer pays for the seat" is a fact; "the employer requires the certificate, so the assessment cannot be formative-only" is a design consequence. Only the second earns the line.
4. **Draw only the edges that decide something.** Who mandates, who funds, who constrains, who evaluates, who benefits. An edge that changes no decision is noise.
5. **Write down who is *not* here.** The absences are frequently the most consequential entry — a self-paced design with no facilitator, a course with no employer at the table, a programme whose regulator is invisible from inside it.
6. **Test the list against the salience question.** For each party: what power, what legitimacy, what urgency? A party with none of the three does not belong on the map.

## Related Methods
- [Make the Invisible Visible (Power Dynamics)](make-the-invisible-visible-power-dynamics.md) — the heavier sibling, which asks who *should* decide rather than who does, and treats the answer as changeable
- [Needs Analysis](needs-analysis.md) — establishes what the activity is for; this establishes who is asking
- [Learner and Context Analysis](learner-and-context-analysis.md) — the learner-side counterpart, which goes deep on one party rather than wide across several

## Examples
- **Public-sector strategy work** — Bryson's technique set (stakeholder identification, power-versus-interest grids, participation planning) is the most widely used operationalisation in government and non-profit planning, and is explicit that different techniques serve different purposes
- **Natural resource management** — Reed and colleagues catalogued the methods actually in use across environmental projects and found the choice of technique changes who ends up represented, which is the strongest available warning against treating any one grid as neutral
- **Instructional design intake** — the ordinary case: a designer's first conversation with a client establishes the sponsor, the subject-matter expert, the approving body and the learner's manager, and almost never writes any of them down

## Key Sources
- Freeman, R. E. (1984). *Strategic Management: A Stakeholder Approach*. Pitman.
- Mitchell, R. K., Agle, B. R., & Wood, D. J. (1997). Toward a theory of stakeholder identification and salience: Defining the principle of who and what really counts. *Academy of Management Review, 22*(4), 853–886. [doi:10.2307/259247](https://doi.org/10.2307/259247)
- Bryson, J. M. (2004). What to do when stakeholders matter: Stakeholder identification and analysis techniques. *Public Management Review, 6*(1), 21–53. [doi:10.1080/14719030410001675722](https://doi.org/10.1080/14719030410001675722)
- Reed, M. S., Graves, A., Dandy, N., Posthumus, H., Hubacek, K., Morris, J., Prell, C., Quinn, C. H., & Stringer, L. C. (2009). Who's in and why? A typology of stakeholder analysis methods for natural resource management. *Journal of Environmental Management, 90*(5), 1933–1949. [doi:10.1016/j.jenvman.2009.01.001](https://doi.org/10.1016/j.jenvman.2009.01.001)
