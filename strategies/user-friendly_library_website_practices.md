---
type: strategy
title: User-Friendly Library Website Practices
description: Designing library websites so students can efficiently find and use resources through clear navigation, plain language, accessibility, and usability testing.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# User-Friendly Library Website Practices

## Description
This strategy applies usability and accessibility principles to academic library websites so that students can locate and use library resources with minimal friction. Core practices include a clear vision for the site, prominent search access, simplified navigation, a homepage that functions as a gateway, elimination of library jargon, conformance with accessibility standards, and iterative usability testing with real users.

## Design Implications

Library websites are learning interfaces: every search box, label, and menu either supports or taxes the cognitive work of research. Simplified navigation and plain-language labeling reduce extraneous processing, freeing working memory for the actual research task [Chunking and simplifying displayed information reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]; cluttered, jargon-heavy interfaces contribute to the overload that degrades learning and task completion [Cognitive overload degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [+S]. Usability testing with representative users is the mechanism that converts design assumptions into evidence-based decisions.

### Context
#### Requirements
- A stated design vision tied to user tasks (find, access, ask), not to organizational structure
- Prominent, single-point search entry (discovery layer or federated search) on the homepage
- Plain-language labels; jargon such as "serials," "ILL," or "databases A–Z" replaced or glossed
- Conformance with WCAG 2.1 AA: keyboard navigation, alt text, sufficient contrast, screen-reader compatibility
- A recurring usability testing cycle (e.g., five-user tests, card sorting, analytics review) feeding design revisions

#### Constraints
- Usability gains decay without maintenance; new databases, guides, and vendor tools reintroduce inconsistency [-W]
- Heuristic expert review alone misses real user failures; evaluator-based inspection finds only a minority of usability problems compared with testing actual users [~S]
- Accessibility retrofits applied after launch consistently underperform accessibility built in from the start; many academic library sites remain partially non-compliant despite stated policy [-M]
- Discovery layers can hide the distinction between catalog, database, and full-text holdings, leaving novices unable to judge source quality or scope [~W]

#### Implementation Variability
- Small libraries may use lightweight testing (hallway tests, first-click tests) instead of formal lab studies
- Jargon elimination can be phased: rename high-traffic labels first, provide tooltips/glossaries for specialist terms
- Accessibility work can be driven by automated audits (WAVE, axe) supplemented by manual screen-reader testing (NVDA, JAWS)

### Target Learners
- First-year and novice researchers who lack mental models of library systems and abandon sites that require insider vocabulary
- Students with disabilities, for whom accessible design is a prerequisite rather than an enhancement
- Distance and online learners who interact with the library exclusively through the website
- Less critical for advanced researchers with established search habits, who may even prefer direct database links over simplified gateways [~W]

### Target Learning Goals
- Information literacy: locating, evaluating, and retrieving sources independently
- Self-efficacy in research: reducing the frustration that deters students from using library resources at all
- Transferable search behavior: interface habits that generalize to other discovery systems

### Instructions
1. Define the site's user tasks and success metrics before redesigning (find an article, renew a loan, contact a librarian).
2. Simplify the information architecture: group content by user task, [chunking](../principles/chunking.md) menus into a small number of scannable categories [Chunking and simplifying displayed information reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M].
3. Place a single prominent search box on the homepage as the primary gateway.
4. Rewrite labels in plain language; apply [accessible vocabulary and syntax](../principles/accessible-vocabulary-syntax.md) throughout.
5. Build to WCAG 2.1 AA from the outset and verify with [accommodations](../elements/accommodations.md)-compatible assistive technologies.
6. Run iterative usability tests with 5–8 representative students; observe task completion, not opinions.
7. [Assess performance](../elements/assess-performance.md) continuously via analytics (search usage, page depth, abandonment) and revise.

## Related Strategies
- Plain-language labeling of research tools — reduces the vocabulary barrier that most strongly predicts novice failure
- Embedded librarian instruction — pairs the simplified interface with guided practice in using it
- Discovery service optimization — the search layer is the highest-traffic component of most library sites

## Related Elements
- [Chunking](../principles/chunking.md) — limits menu and page complexity to what working memory can hold
- [Advance organizers](../elements/advance-organizers.md) — orientation pages and guides that frame where to start research
- [Accommodations](../elements/accommodations.md) — accessibility features that make the site usable for learners with disabilities
- [Assess performance](../elements/assess-performance.md) — analytics and testing that close the design loop

## Examples
- **NCSU Libraries** (https://www.lib.ncsu.edu) — long-running usability program; its search-first homepage and plain-language navigation are widely cited models in the library UX literature.
- **University of Michigan Library** (https://www.lib.umich.edu) — iterative redesigns grounded in published usability studies with student participants.
- **Five-user discount testing** (Nielsen & Landauer's model) — many academic libraries run small quarterly tests on high-traffic tasks (e.g., "find a peer-reviewed article on X") rather than large annual studies.

## Key Sources
- Nielsen, J., & Molich, R. (1990). Heuristic evaluation of user interfaces. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 249–256. [doi:10.1145/97243.97281](https://doi.org/10.1145/97243.97281)
- Krug, S. (2014). *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability* (3rd ed.). New Riders.
- Comeaux, D., & Schmetzke, A. (2013). Accessibility of academic library web sites in North America: Current status and trends (2002–2012). *Library Hi Tech, 31*(2), 271–288.
- Georgas, H. (2013). Google vs. the library (Part II): Student search patterns and behaviors when using Google and a federated search tool. *portal: Libraries and the Academy, 13*(4), 343–366.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)