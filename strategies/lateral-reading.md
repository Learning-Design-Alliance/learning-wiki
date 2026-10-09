---
type: strategy
id: lateral-reading
aliases: [lateral_reading]
title: Lateral Reading
description: Evaluating the trustworthiness of online information by leaving the original site and consulting other sources to see what they say about it.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Lateral Reading

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Lateral reading is a digital literacy strategy for evaluating online sources: instead of staying on a webpage and judging its content, design, or self-description (vertical reading), the reader opens new tabs and investigates what independent sources — Wikipedia, news coverage, fact-checking sites — say about the source itself. Professional fact-checkers use this technique to assess credibility in seconds, while most students and even many educators default to vertical reading [Wineburg & McGrew's studies of professional fact-checkers.](https://doi.org/10.1177/016146811912100902) [+S].

## Design Implications

Lateral reading works because it shifts evaluation from judging *content* to judging *who is behind the content* — a strategy that mirrors how experts actually verify information online [Lateral reading outperforms vertical reading for credibility judgments.](https://doi.org/10.1177/016146811912100902) [+S]. Instructionally, it is best taught through [Case-Based Learning](../patterns/case-based-learning.md): learners evaluate real, deliberately ambiguous sources and compare their judgments before and after going lateral.

### Context
#### Requirements
- Internet access and devices with multiple tabs or windows
- A curated set of authentic sources to evaluate, including deceptive or biased ones (e.g., sites mimicking news organizations)
- Guidance on which external sources to consult and what to look for (organization funding, author credentials, prior coverage)
- Instructor modeling of the strategy before independent practice
- Internet-connected devices and permission to leave the original page mid-lesson
- A short list of trusted external reference points (Wikipedia, established news outlets, dedicated fact-checkers such as Snopes or PolitiFact)
- Modeled examples: the instructor demonstrating the tab-opening process aloud, ideally with [Think-Aloud](../elements/think-aloud.md) narration
- Repeated practice with real, unfamiliar sources — the strategy is a habit, not a piece of declarative knowledge

#### Constraints
- Requires time and effort; consulting multiple sources per claim does not scale to every piece of information a learner encounters [~M]
- Overwhelming for beginners without scaffolding — novices may open tabs but not know what to look for, defaulting back to surface cues [~M]
- The reliability of the lateral sources themselves must be established; learners can lateral-read into low-quality sources (e.g., partisan "fact-checks") [~W]
- Less applicable offline or in closed platforms where source provenance is already curated
- Requires time and effort per source; learners under time pressure revert to vertical reading [~M]
- Beginners can be overwhelmed by open-ended searching without guidance on *which* queries to run and *what* counts as disconfirming evidence [-W]
- The strategy inherits the reliability of the sources consulted laterally; learners must also learn to evaluate the checkers [~M]
- Less applicable to offline or paywalled-source evaluation, where the lateral evidence base is thin

#### Implementation Variability
- **Modeled demonstration**: instructor lateral-reads aloud, making verification moves visible
- **Structured protocols**: checklists or prompts specifying which sources to consult (e.g., "search the organization name + 'funding'")
- **Simulated environments**: product developers can build sandboxed exercises where learners practice on pre-vetted deceptive sources
- **Progressive complexity**: start with obviously suspect sites, move to sources requiring finer discrimination
- Full modeling → guided practice → independent evaluation (fading the [Scaffolding](../principles/scaffolding.md))
- Structured variants: give learners a fixed protocol ("open three tabs; search the organization's name plus 'funding' or 'bias'") before open-ended reading
- Classroom variants: [Case Study](../elements/case-study.md) analysis of a viral post, or live "source triage" races comparing student vs. fact-checker methods

### Target Learners
- Secondary and higher-education students, whose credibility judgments rely heavily on surface features like design polish and domain endings [Students' civic online reasoning is weak across grade levels.](https://doi.org/10.3102/0013189X211035106) [+S]
- Adult learners in professional development focused on media and information literacy
- Learners of all ages benefit, but instruction must be scaffolded for novices; brief interventions produce measurable gains even at scale [Brief instruction in lateral reading improves students' credibility evaluations.](https://doi.org/10.3102/0013189X211035106) [+M]
- Secondary and higher-education students, who in studies overwhelmingly fail to apply lateral reading without instruction [Breakstone et al., 2021] [-S for untaught populations]
- Adult learners and professionals in media-literacy and civic-education programs
- Less necessary for learners already trained as professional fact-checkers, who use the strategy spontaneously [+S]

### Target Learning Goals
- Critical evaluation: judging source credibility and bias
- Epistemic cognition: understanding that trustworthiness is established through corroboration, not appearance
- Transferable procedural skill: a repeatable verification routine applicable across domains
- Evaluating source credibility and trustworthiness of online information
- Digital and civic online reasoning: judging claims before sharing or citing them
- Metacognitive habits of verification — treating one's own initial impressions as claims to be checked

### Instructions
1. **Model the strategy**: demonstrate lateral reading on a live source, verbalizing each move (search the organization, check Wikipedia, look for independent coverage) — a [Think-Aloud](../elements/think-aloud.md) approach
2. **Contrast with vertical reading**: have learners first evaluate a source using only on-page evidence, then repeat laterally, and compare judgments — a [Case Study](../elements/case-study.md) structure
3. **Guided practice**: learners evaluate new sources using a structured protocol, consulting at least two independent external sources (a [3-Source Rule](../strategies/3-source_rule.md) adaptation)
4. **Debrief**: discuss what the lateral sources revealed, what cues were misleading, and when lateral reading is worth the time cost
5. **Assess transfer**: present a novel source and evaluate whether learners spontaneously leave the page

## Related Strategies
- [A Finder's Guide to Facts](../strategies/a_finders_guide_to_facts.md) — a complementary framework for locating reliable factual sources
- [3-Source Rule](../strategies/3-source_rule.md) — a corroboration heuristic that operationalizes lateral verification
- [SIFT method](sift-method.md) — a four-step packaged variant (Stop; Investigate the source; Find better coverage; Trace claims) built around lateral reading
- [Case-Based Learning](case-based-learning.md) — viral misinformation cases provide authentic material for lateral-reading practice

## Examples
- **Stanford History Education Group — Civic Online Reasoning curriculum** ([cor.stanford.edu](https://cor.stanford.edu)) — free lessons and assessments in which students lateral-read real websites; the underlying research shows fact-checkers read laterally while historians and students stayed on-page and were far more often deceived [Wineburg & McGrew's studies of professional fact-checkers.](https://doi.org/10.1177/016146811912100902) [+S]
- **News Literacy Project — Checkology®** ([checkology.org](https://checkology.org)) — interactive modules where learners practice lateral reading on simulated sources in a safe environment
- **A high school civics unit**: students evaluate a polished advocacy site, first vertically, then laterally, discovering through a Wikipedia search that the organization is an industry front group
- **Stanford History Education Group's Civic Online Reasoning curriculum** — free classroom lessons and assessments built on lateral reading; field experiments show students taught these strategies outperform controls on live-source evaluations [Breakstone et al., 2021] [+S]
- **A high school civics lesson on a viral claim**: students first judge a polished advocacy site vertically, then watch the teacher open tabs to find the site's funder via Wikipedia and news coverage, then repeat the process on a new source
- **Newsroom practice**: professional fact-checkers at outlets like *The Washington Post*'s Fact Checker routinely resolve credibility questions in under a minute by leaving the source immediately — the expert behavior the strategy aims to build in students

## Key Sources
- Wineburg, S., & McGrew, S. (2019). Lateral reading and the nature of expertise: The studies of professional fact-checkers. *Teachers College Record, 121*(9), 1–24.
- Breakstone, J., Smith, M., Ortega, P., Kerr, D., & Wineburg, S. (2021). Students' civic online reasoning: A national portrait. *Educational Researcher, 50*(8), 505-515. [doi:10.3102/0013189x211017495](https://doi.org/10.3102/0013189x211017495)
- McGrew, S., Breakstone, J., Ortega, T., Kaiser, M., & Wineburg, S. (2018). Can students evaluate online sources? Learning from assessments of civic online reasoning. *Theory &amp; Research in Social Education, 46*(2), 165-193. [doi:10.1080/00933104.2017.1416320](https://doi.org/10.1080/00933104.2017.1416320)
- Wineburg, S., & McGrew, S. (2019). Lateral reading and the nature of expertise: The ability of historians to evaluate digital sources is limited. *Teachers College Record, 121*(11), 1–40.
- Breakstone, J., Smith, M., Orland, M., Barr, D., & Wineburg, S. (2021). Lateral reading on the open Internet: A district-wide field study in high school government classes. *Journal of Educational Psychology, 114*(5), 893–909. [doi:10.1037/edu0000740](https://doi.org/10.1037/edu0000740)
- McGrew, S., Ortega, T., Breakstone, J., & Wineburg, S. (2017). The challenge that's bigger than fake news: Civic reasoning in a social-media environment. *American Educator, 41*(3), 4–9.
- Wineburg, S., McGrew, S., Breakstone, J., & Ortega, T. (2016). Evaluating information: The cornerstone of civic online reasoning. *Stanford Digital Repository.*

<!-- merged 2026-10-09 from strategies/lateral_reading ("Lateral Reading"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Lateral Reading

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Lateral reading is a digital literacy strategy for evaluating online information: instead of staying on a page and scrutinizing its design, credentials, or "About Us" statement (vertical reading), the reader opens new tabs and searches what *other* sources say about the site, author, or claim. Professional fact-checkers use this technique to reach credibility judgments in seconds, relying on Wikipedia, news coverage, and fact-checking sites as external checks [Wineburg & McGrew, 2019].

## Design Implications

Lateral reading works because it shifts evaluation from analyzing a source's self-presentation to consulting independent evidence — a form of [Comparing Cases](../elements/comparing-cases.md) applied to source credibility. It must be explicitly taught: without instruction, students default to vertical reading and surface features like polish and domain endings, which are unreliable cues [~S].

### Context
#### Requirements
- Internet-connected devices and permission to leave the original page mid-lesson
- A short list of trusted external reference points (Wikipedia, established news outlets, dedicated fact-checkers such as Snopes or PolitiFact)
- Modeled examples: the instructor demonstrating the tab-opening process aloud, ideally with [Think-Aloud](../elements/think-aloud.md) narration
- Repeated practice with real, unfamiliar sources — the strategy is a habit, not a piece of declarative knowledge

#### Constraints
- Requires time and effort per source; learners under time pressure revert to vertical reading [~M]
- Beginners can be overwhelmed by open-ended searching without guidance on *which* queries to run and *what* counts as disconfirming evidence [-W]
- The strategy inherits the reliability of the sources consulted laterally; learners must also learn to evaluate the checkers [~M]
- Less applicable to offline or paywalled-source evaluation, where the lateral evidence base is thin

#### Implementation Variability
- Full modeling → guided practice → independent evaluation (fading the [Scaffolding](../principles/scaffolding.md))
- Structured variants: give learners a fixed protocol ("open three tabs; search the organization's name plus 'funding' or 'bias'") before open-ended reading
- Classroom variants: [Case Study](../elements/case-study.md) analysis of a viral post, or live "source triage" races comparing student vs. fact-checker methods

### Target Learners
- Secondary and higher-education students, who in studies overwhelmingly fail to apply lateral reading without instruction [Breakstone et al., 2021] [-S for untaught populations]
- Adult learners and professionals in media-literacy and civic-education programs
- Less necessary for learners already trained as professional fact-checkers, who use the strategy spontaneously [+S]

### Target Learning Goals
- Evaluating source credibility and trustworthiness of online information
- Digital and civic online reasoning: judging claims before sharing or citing them
- Metacognitive habits of verification — treating one's own initial impressions as claims to be checked

### Instructions
1. Present an unfamiliar source and ask learners for an initial credibility judgment (this surfaces the vertical-reading default).
2. [Model](../elements/cognitive-apprenticeship.md) lateral reading aloud: open new tabs, search the organization or author, narrate what would count as a red flag.
3. Have learners practice the same moves on new sources in pairs, using a short protocol of search queries.
4. Debrief: compare judgments before and after lateral reading, and discuss why surface features mislead.
5. Fade support: assign independent evaluation of sources embedded in a [Research](../elements/research.md) or writing task, then assess the evidence trail learners used.

## Related Strategies
- [SIFT method](sift-method.md) — a four-step packaged variant (Stop; Investigate the source; Find better coverage; Trace claims) built around lateral reading
- [A Finder's Guide to Facts](a_finders_guide_to_facts.md) — a related framework for teaching fact-verification habits
- [Case-Based Learning](case-based-learning.md) — viral misinformation cases provide authentic material for lateral-reading practice

## Related Elements
- [Case Study](../elements/case-study.md) — real misinformation cases give lateral reading authentic stakes
- [Research](../elements/research.md) — lateral reading is a form of rapid, targeted research about sources
- [Resource Evaluation](../elements/resource-evaluation.md) — the broader skill into which lateral reading feeds
- [Think-Aloud](../elements/think-aloud.md) — the modeling method that makes expert evaluation moves visible

## Tools
- Wikipedia (as a first-pass source background check)
- Snopes (https://www.snopes.com), PolitiFact (https://www.politifact.com), FactCheck.org (https://www.factcheck.org)
- Reverse image search (Google Images, TinEye) for tracing media provenance
- Stanford History Education Group's Civic Online Reasoning curriculum (https://cor.stanford.edu)

## Examples
- **Stanford History Education Group's Civic Online Reasoning curriculum** — free classroom lessons and assessments built on lateral reading; field experiments show students taught these strategies outperform controls on live-source evaluations [Breakstone et al., 2021] [+S]
- **A high school civics lesson on a viral claim**: students first judge a polished advocacy site vertically, then watch the teacher open tabs to find the site's funder via Wikipedia and news coverage, then repeat the process on a new source
- **Newsroom practice**: professional fact-checkers at outlets like *The Washington Post*'s Fact Checker routinely resolve credibility questions in under a minute by leaving the source immediately — the expert behavior the strategy aims to build in students

## Key Sources
- Wineburg, S., & McGrew, S. (2019). Lateral reading and the nature of expertise: The ability of historians to evaluate digital sources is limited. *Teachers College Record, 121*(11), 1–40.
- Breakstone, J., Smith, M., Orland, M., Barr, D., & Wineburg, S. (2021). Lateral reading on the open Internet: A district-wide field study in high school government classes. *Journal of Educational Psychology, 114*(5), 893–909. [doi:10.1037/edu0000740](https://doi.org/10.1037/edu0000740)
- McGrew, S., Ortega, T., Breakstone, J., & Wineburg, S. (2017). The challenge that's bigger than fake news: Civic reasoning in a social-media environment. *American Educator, 41*(3), 4–9.
- Wineburg, S., McGrew, S., Breakstone, J., & Ortega, T. (2016). Evaluating information: The cornerstone of civic online reasoning. *Stanford Digital Repository.*
-->
