---
type: strategy
title: Four Moves and a Habit
description: "A framework for fact-checking that includes four key moves: Check for previous work, go upstream to find the source, read laterally, and circle back."
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Four Moves and a Habit

## Description
The Four Moves and a Habit (also known as SIFT) is a fact-checking framework developed by Mike Caulfield for evaluating online information. The four moves are: **Stop** and check your emotional reaction (the habit), **Investigate the source** before engaging with its content, **Find better coverage** of the claim from more reliable outlets, and **Trace claims, quotes, and media to their original context**. Unlike traditional checklist approaches (e.g., CRAAP), it treats the web as the fact-checker's tool rather than the object of suspicion — learners open new tabs and consult external sources about a source instead of scrutinizing the source page itself.

## Design Implications

The framework works because it replaces exhaustive, page-internal evaluation with the fast, external verification strategies used by professional fact-checkers. Research shows that expert fact-checkers evaluate sources by leaving the page and reading laterally — checking what other sites say about the source — while historians and undergraduates tend to read vertically, staying on the page and being routinely deceived by professional design [Lateral reading outperforms vertical reading for source evaluation.](https://doi.org/10.3102/0034654319839149) [+S]. The "stop" habit leverages the fact that strong emotional reactions (outrage, vindication) reliably predict susceptibility to misinformation, so interrupting the reaction creates space for deliberate evaluation [~M].

### Context
#### Requirements
- Access to online information and the ability to open parallel tabs and searches
- Basic search skills: querying a source's name plus "wikipedia," using reverse image search, finding original publication dates
- Willingness to abandon a source quickly when it fails investigation — the framework explicitly optimizes for *not* reading dubious material deeply
- Minimal prior knowledge of specific sources; the moves themselves supply the evaluative leverage [Prior knowledge of individual sources is not required for lateral reading to improve evaluation.](../claims/prior-knowledge-not-related-to-performance.md) [~W]

#### Constraints
- Ineffective when learners remain on the source page and apply the moves as an internal checklist — the benefit comes from external corroboration, not from re-reading [Lateral reading outperforms vertical reading for source evaluation.](https://doi.org/10.3102/0034654319839149) [-S]
- Requires reliable third-party infrastructure (Wikipedia, established news outlets, fact-checking sites); in information environments lacking such anchors, "find better coverage" degrades into circular sourcing
- The "stop" habit is the least trained and most easily dropped move; without it, learners fact-check only claims they already doubt, confirming rather than correcting bias [~W]
- Time-pressured learners default to shallow heuristics (design quality, domain suffix) when the moves are not practiced to automaticity [-M]

#### Implementation Variability
- Taught as full lessons (Caulfield's open textbook), as short video micro-lessons (Stanford History Education Group's Civic Online Reasoning curriculum), or as embedded prompts in a research assignment
- Can be compressed to "SIFT" as a memorable acronym for quick application, or expanded with domain-specific moves (e.g., tracing scientific claims to journal articles)
- Works as a whole-class [Case-Based Learning](../elements/case-based-learning.md) activity using live, real-world claims rather than sanitized examples

### Target Learners
- Undergraduate and secondary students conducting online research, who default to vertical reading and design-based judgments [Lateral reading outperforms vertical reading for source evaluation.](https://doi.org/10.3102/0034654319839149) [+S]
- Novices with little background knowledge of sources — the moves substitute external verification for expertise [Prior knowledge of individual sources is not required for lateral reading to improve evaluation.](../claims/prior-knowledge-not-related-to-performance.md) [~W]
- Less effective for learners who already habitually read laterally; instruction adds little for professional fact-checkers [~W]

### Target Learning Goals
- Source evaluation: judging the credibility of websites, authors, and media
- Claim tracing: locating original context for quotes, statistics, and images
- Metacognitive self-monitoring: recognizing when emotional arousal is driving acceptance of a claim [Self-monitoring improves self-regulation.](../claims/self-monitoring-improves-self-regulation.md) [+M]

### Instructions
1. **Stop.** Notice your emotional reaction to the claim; if it is strong, slow down before sharing or accepting it. This habit precedes and frames every other move.
2. **Investigate the source.** Open a new tab and search for what known references say about the source or author — not what the source says about itself. Compare coverage of the same source across outlets to sharpen discrimination between reliable and unreliable publishers [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]
3. **Find better coverage.** Look for the claim in more authoritative outlets; the goal is the *claim's* credibility, not the original page's.
4. **Trace to the original.** Follow quotes, figures, and media upstream to their original context — via citation-chasing, reverse image search, or archival links — and check whether the original supports the framing. Verbalizing why a source passed or failed each move strengthens the evaluative schema [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M]

## Related Strategies
- [A Finder's Guide to Facts](a_finder's_guide_to_facts.md) — complementary framework emphasizing how to locate authoritative sources rather than vet a given one
- [3-Source Rule](3-source_rule.md) — a corroboration heuristic that operationalizes the "find better coverage" move

## Examples
- **[Web Literacy for Student Fact-Checkers](https://webliteracy.pressbooks.com/)** — Caulfield's open textbook, the canonical statement of the four moves, with worked demonstrations of each technique
- **[Civic Online Reasoning](https://cor.stanford.edu/)** — Stanford History Education Group curriculum built on lateral-reading research; includes classroom-ready assessments showing large gains in students' source evaluation after brief instruction
- **First-year composition courses** using SIFT as a pre-research routine: students apply the moves to sources found via Google before admitting them into an annotated bibliography

## Key Sources
- Caulfield, M. (2017). *Web literacy for student fact-checkers... and other people who care about facts.* Pressbooks. [https://webliteracy.pressbooks.com/](https://webliteracy.pressbooks.com/)
- Wineburg, S., & McGrew, S. (2019). Lateral reading and the nature of expertise: Reading college and professional fact-checkers. *The Reading Teacher, 72*(5), 585–595. [doi:10.37016/mr-2020-56](https://doi.org/10.37016/mr-2020-56)
- Breakstone, J., Smith, M., Wineburg, S., Lester, A., Ortega, T., & Dreier, S. (2021). Civic online reasoning: Curriculum evaluation with large-scale field trials. *Teachers College Record, 123*(5), 1–48. [doi:10.1177/01614681211018744](https://doi.org/10.1177/01614681211018744)
- McGrew, S., Ortega, T., Breakstone, J., & Wineburg, S. (2017). The challenge that's bigger than fake news: Civic reasoning in a social-media environment. *American Educator, 41*(3), 4–9.