---
type: element
title: Open Educational Resources (The 5Rs)
description: Open Educational Resources are teaching materials licensed to grant free, perpetual permission to retain, reuse, revise, remix, and redistribute them — the "5Rs" test that distinguishes genuine open licensing from merely free-to-enroll access.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# Open Educational Resources (The 5Rs)

> **Element** · [All elements](index.md)

## Description
Wiley (2014) argues that "open" in education should be defined by open **licensing**, not open **entry** — a distinction he draws to correct what he saw as damage MOOCs did to the term. The Open University's original 1971 sense of "open" meant anyone could enroll regardless of prior achievement; MIT's 2001 OpenCourseWare initiative added a different meaning — course materials released under a license anyone could freely use. Wiley proposes a concrete test, the **5Rs**, for whether a copyrightable work is genuinely open: it must grant free, perpetual permission to **Retain** (make and keep copies), **Reuse** (use the work as-is in varied contexts), **Revise** (adapt or modify it, e.g. translate it), **Remix** (combine it with other open works), and **Redistribute** (share the original, revisions, or remixes with others). Creative Commons licenses are the most common mechanism for granting all five permissions at once — a Khan Academy video, MIT OpenCourseWare notes, an OpenStax textbook, or a Wikipedia article under CC licensing all pass the 5R test; a MOOC that is free to enroll in but forbids copying, requires registration deadlines, and charges for a credential does not, no matter how many people can access it.

Wiley frames the value of true 5R openness as "permissionless innovation" (Thierer, 2014): when materials can be freely forked, translated, and recombined without seeking permission or paying a fee, the cost of instructional experimentation drops sharply — designers do not need to negotiate rights before trying something new. He extends the same logic beyond content alone into a proposed four-part **open education infrastructure**: **open resources** (the historically dominant case — OER itself), **open credentials** (advanced by Mozilla's Open Badges work), and two areas Wiley identifies as still underdeveloped — **open competencies** (institutions tend to treat their competency frameworks as proprietary even while promoting OER to students, which stalls collaborative development of competency-based education) and **open assessments**. Weller (2018) offers a complementary practical observation: OER succeeded where the earlier "learning objects" movement largely failed because it mapped onto an existing practice teachers already did (adapting a text) rather than requiring new technical packaging standards and metadata schemes — the lesson being that content-reuse innovations succeed when they need minimal new infrastructure, not when they depend on an unfamiliar standard.

## Design Implications

### Context
#### Requirements
- A license that explicitly grants all five permissions (retain, reuse, revise, remix, redistribute) — anything less (e.g., "free to view but not to copy or modify") does not meet the 5R bar even if access itself is free
- For adoption at scale: content reuse succeeds fastest when it maps onto a practice instructors already engage in (adapting an existing text) rather than requiring new infrastructure or metadata standards to be learned first
#### Constraints
- Free enrollment (open access) is a different property from open licensing (the 5Rs) — conflating the two, as Wiley argues MOOCs did, can actually set back the broader cause of genuinely open, remixable materials
- Competencies and assessments remain far less commonly openly licensed than content itself, even at institutions that promote OER use among their own students — this asymmetry limits collaborative innovation in competency-based education specifically

### Target Learners
- Any learner or instructor wanting to adapt, translate, remix, or redistribute existing materials rather than only consume them as originally packaged

### Target Learning Goals
- Not learner-facing directly — a resource property that enables instructional designers and instructors to adapt, combine, and iterate on materials at low cost

### Affordances
- [Massive Open Online Course (MOOC)](../patterns/massive-open-online-course.md)

## Related Elements
- [Digital Open Badges](digital-open-badges.md)

## Examples
- Khan Academy videos, MIT OpenCourseWare, and OpenStax textbooks under Creative Commons licenses, all passing the 5R test
- Mozilla's Open Badges as an early instance of open credentialing infrastructure (see [Digital Open Badges](digital-open-badges.md))

## Key Sources
- Wiley, D. (2014). The MOOC misstep and the open education infrastructure. Republished in R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/open_educational_resources](https://edtechbooks.org/lidtfoundations/open_educational_resources)
- Weller, M. (2018). Twenty years of EdTech. *EDUCAUSE Review, 53*(4). Republished in R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/twenty_years_of_edtech](https://edtechbooks.org/lidtfoundations/twenty_years_of_edtech)
- Thierer, A. (2014). *Permissionless innovation: The continuing case for comprehensive technological freedom*. Mercatus Center.
