---
type: strategy
id: direct_instruction-keyword_search
aliases: [reading_online_strategy-formulating_effective_search_queries]
title: "Direct Instruction: Keyword Search"
description: Explicit teaching of how to select, combine, and refine search keywords — including synonyms, operators, and Boolean logic — alongside criteria for evaluating the credibility of retrieved sources.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Direct Instruction: Keyword Search

> **Strategy** · [All strategies](index.md)
> **Evidence** · 7 claims (5 for, 2 mixed) · 17 studies (7 causal, 4 review, 3 quant-synthesis, 2 theoretical, 1 associational), `q1`–`q4` · 2 of 17 report an effect size · 2 claims rest on one study

## Description
Direct instruction of keyword search explicitly teaches learners how to translate an information need into effective search terms: generating synonyms, combining terms with Boolean operators, using field limits and phrase quotes, and iterating when results disappoint. It also teaches evaluation criteria (authority, currency, evidence) so learners can judge what retrieval returns. The instructor models each move — thinking aloud while decomposing a question into concepts, choosing terms, and revising — then guides learners through practice with feedback.

## Design Implications

Search is a procedural skill with a large novice search space: unguided, novices flounder with vague one-word queries and accept the first plausible result. Explicit, structured teaching reduces that unproductive search and working-memory burden, consistent with evidence that novices learn procedural skills better from explicit guidance than from discovery [Worked examples reduce unnecessary search for novices.](../claims/worked-example-problem-sequences.md) [+M] and with the broader finding that minimal-guidance approaches are inefficient for novices [Kirschner, Sweller, & Clark, 2006] [+S]. Because search strategy is largely invisible expert behavior, the instruction must externalize it through [Think-Aloud](../elements/think-aloud.md)-style modeling rather than merely stating rules.

### Context
#### Requirements
- A decomposable model of the search process: question → concepts → terms → query → evaluate → revise
- Worked demonstrations on authentic questions in the learners' domain, with the instructor verbalizing term choices and revision decisions
- A controlled practice environment (e.g., a library database or curated corpus) where learners apply the sequence and receive feedback on query quality, not just result counts
- Explicit evaluation criteria for judging retrieved sources
- Access to search engines and authentic research tasks that require locating information
- Time for explicit instruction and [Modeling](../elements/modeling.md) of expert query formulation
- Guided [Practice](../elements/practice.md) with [Feedback](../elements/provide-feedback.md) on query quality, not just on final results
- A reflection routine (e.g., search logs) that surfaces students' query decisions

#### Constraints
- Taught as rigid rules ("always use Boolean AND"), keyword instruction produces brittle behavior that fails when databases auto-expand, rank, or use semantic matching [~M] — modern search engines often reward natural-language queries, so operator rules must be taught as tools contingent on the system
- Direct instruction of procedures without practice in *revising* queries yields learners who can recite operators but cannot recover from a failed search [-M]
- Effectiveness drops for learners who already search fluently; redundant instruction wastes time and can reduce engagement [Worked-example guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]
- Keyword skill alone does not guarantee source evaluation; without explicit credibility criteria, learners judge by surface features such as search rank position [-M]
- Advanced operators (Boolean syntax, field limits) impose extraneous load on novices; teaching them too early can degrade performance [~M] — sequence from keyword selection to operators as fluency develops
- Search engine interfaces increasingly de-emphasize operator syntax, so taught techniques may transfer inconsistently across tools [~W]
- Skills decay without ongoing practice embedded in real content-area tasks; one-off "library lessons" show little durable effect [~M]
- Effective queries improve *retrieval*, not *evaluation* — students may still select low-quality sources without complementary evaluation instruction [-W]

#### Implementation Variability
- **Full modeling → guided practice → independent search**: a fading sequence from instructor demonstration to solo retrieval
- **Query worksheets**: learners plan concepts and synonyms on paper before touching the search box, reducing load during formulation [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]
- **Contrasting query cases**: showing a weak query beside a strong one for the same question helps learners abstract what makes terms effective [Multiple contrasting cases support abstraction.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]
- **Embedded instruction**: keyword teaching integrated into a content unit (e.g., a research essay) rather than a standalone library session, improving transfer to real tasks
- Younger learners: keyword brainstorming, quotation marks, and "try different words" routines
- Secondary/adult learners: Boolean operators, truncation, site/domain limits, and query revision cycles
- Structured tools such as Google's "Search Education" lesson plans or library database instruction can scaffold the sequence
- Search logs and think-aloud protocols can be used formatively to diagnose individual strategy gaps

### Target Learners
- Novices — secondary and early undergraduate students — encountering library databases or academic search for the first time [+M]
- Learners with low domain vocabulary, who need explicit support generating synonyms and discipline-specific terms; vocabulary breadth directly constrains query quality
- Less beneficial for experienced searchers, who benefit more from advanced technique refreshers than from basic operator instruction [~M]
- Middle school, high school, and adult learners developing digital and information literacy
- Novices who default to typing full questions and rarely revise unproductive queries [~M]
- Less necessary for experienced searchers with strong domain knowledge, who already generate effective terminology [~W]

### Target Learning Goals
- Procedural skill: formulating, executing, and revising search queries
- Strategic knowledge: knowing *when* to broaden, narrow, or re-conceptualize a search
- Critical evaluation: judging the credibility and relevance of retrieved sources
- Metacognitive monitoring: recognizing when results indicate the query, not the literature, is the problem
- Procedural skill: constructing, testing, and revising search queries
- Strategic learning: planning and monitoring an information-seeking process
- Metacognitive development: reflecting on one's own search behavior and strategy gaps [Self-monitoring improves self-regulation.](../claims/self-monitoring-improves-self-regulation.md) [+M]

### Instructions
1. **Activate the need.** Pose an authentic research question and elicit learners' initial search attempts; surface the gap between their results and the available literature.
2. **Model decomposition.** Think aloud while breaking the question into 2–3 core concepts, generating synonyms for each — an [Advance Organizer](../elements/advance-organizers.md) for the query-planning sequence.
3. **Demonstrate query construction.** Show concept combination with Boolean operators, phrase quotes, and truncation, verbalizing each decision; keep the demonstration chunked so learners hold only one move in mind at a time.
4. **Demonstrate evaluation and revision.** Model judging a result's credibility and diagnosing a weak query ("too many results → add a limiting concept").
5. **Guide practice.** Learners execute parallel searches on a new question with a planning worksheet, then compare queries and results in pairs; prompt them to explain why one query outperformed another [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M].
6. **Fade support.** Move learners to independent searching on their own questions, with feedback shifting from query mechanics to strategy and source evaluation.

### Claims
- [ChatGPT users began information seeking with narrow, specified queries far more often than Google users](../claims/chatgpt-narrow-starting-queries.md) [~W]

## Related Strategies

- Direct instruction of keyword search is a specific application of explicit teaching of procedural skills; it pairs naturally with worked-example and modeling approaches for any invisible expert process.
- [Use the Mentefacto Map to define keywords and inclusion/exclusion criteria in systematic reviews](mentefacto-map-review-criteria.md)
- [Evaluating Online Sources](evaluating_online_sources.md) — the necessary complement; good queries retrieve candidates, evaluation filters them
- [Think-Aloud Modeling](think-aloud-modeling.md) — the instructional method for making expert search reasoning visible
- [Metacognitive Reflection Prompts](metacognitive_reflection_prompts.md) — structures the reflection component of this strategy

## Examples
- **The Big6 information literacy framework** (Eisenberg & Berkowitz) — a widely adopted K–12 curriculum that explicitly teaches task definition, information-seeking strategies, and source evaluation as sequenced steps ([https://thebig6.org](https://thebig6.org)).
- **ACRL Framework for Information Literacy** — academic librarians' one-shot and credit-bearing instruction sessions routinely use modeled keyword demonstrations on databases such as EBSCOhost and JSTOR ([https://www.ala.org/acrl/standards/ilframework](https://www.ala.org/acrl/standards/ilframework)).
- **Google Search Education** — Google's "A Google A Day" challenges and Search Education lesson plans taught operators and query refinement through modeled, then practiced, searches.
- **Google Search Education** (https://www.google.com/insidesearch/searcheducation/) — published lesson plans and "A Google A Day" challenges that sequence keyword selection, operators, and query evaluation.
- **School library information-literacy curricula** (e.g., the Big6 framework, https://thebig6.org) — embed query formulation as the "information-seeking strategies" stage of a full research process.
- **Middle school science research project** — students search a question three ways (full question, keywords, keywords with quotation marks), compare the relevance of top results, and record which formulation worked in a search log.

## Key Sources
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Brand-Gruwel, S., Wopereis, I., & Vermetten, Y. (2005). Information problem solving by experts and novices: Analysis of a complex cognitive skill. *Computers in Human Behavior, 21*(3), 487–508. [doi:10.1016/j.chb.2004.10.005](https://doi.org/10.1016/j.chb.2004.10.005)
- Walraven, A., Brand-Gruwel, S., & Boshuizen, H. P. A. (2008). Information-problem solving: A review of problems students encounter and instructional solutions. *Computers in Human Behavior, 24*(3), 623-648. [doi:10.1016/j.chb.2007.01.030](https://doi.org/10.1016/j.chb.2007.01.030)
- Eisenberg, M. B., & Berkowitz, R. E. (1990). *Information problem-solving: The Big Six skills approach to library and information skills instruction.* Ablex.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)
- Brand-Gruwel, S., Wopereis, I., & Vermetten, Y. (2005). Information problem solving by experts and novices: Analysis of a complex cognitive skill. *Computers in Human Behavior, 21*(3), 487-508. [doi:10.1016/j.chb.2004.10.005](https://doi.org/10.1016/j.chb.2004.10.005)
- Walraven, A., Brand-Gruwel, B., & Boshuizen, H. P. A. (2008). Information-problem solving: A review of problems students encounter and instructional solutions. *Computers in Human Behavior, 24*(3), 623-648. [doi:10.1016/j.chb.2007.01.030](https://doi.org/10.1016/j.chb.2007.01.030)
- Kuiper, E., Volman, M., & Terwel, J. (2005). The Web as an information resource in K–12 education: Knowledge-building and classroom integration. *Computers & Education, 45*(1), 361–371.
- Leu, D. J., Kinzer, C. K., Coiro, J., Castek, J., & Henry, L. A. (2013). New literacies: A dual-level theory of the changing nature of literacy, instruction, and assessment. In D. E. Alvermann, N. J. Unrau, & R. B. Ruddell (Eds.), *Theoretical models and processes of reading* (6th ed., pp. 1150–1181). International Reading Association.

<!-- merged 2026-10-14 from strategies/reading_online_strategy-formulating_effective_search_queries ("Reading Online Strategy: Formulating Effective Search Queries"), a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Reading Online Strategy: Formulating Effective Search Queries

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 3 studies (1 causal, 1 review, 1 theoretical), `q2`–`q3` · 0 of 3 report an effect size · 1 claim rests on one study

## Description
This strategy teaches students to translate an information need into search terms that a search engine can act on effectively. For younger students, this means selecting keywords and using quotation marks rather than typing full questions; for older students, it extends to Boolean operators (AND, OR, NOT, NEAR), parentheses, and truncation (asterisk). Because search behavior is largely invisible and habitual, instruction pairs explicit modeling with metacognitive reflection on students' own information-seeking, so they can evaluate and revise their query strategies rather than repeating unproductive habits.

## Design Implications

Query formulation is a procedural skill that novices perform poorly without explicit instruction — most students default to typing natural-language questions and rarely revise failed queries [~M]. Instruction works best when the teacher makes expert search reasoning visible through a [Think-Aloud](../elements/think-aloud.md) and then fades support as students practice independently, consistent with [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) [+M]. Metacognitive reflection on search behavior supports self-regulation of the broader information problem-solving process [Self-monitoring improves self-regulation.](../claims/self-monitoring-improves-self-regulation.md) [+M].

### Context
#### Requirements
- Access to search engines and authentic research tasks that require locating information
- Time for explicit instruction and [Modeling](../elements/modeling.md) of expert query formulation
- Guided [Practice](../elements/practice.md) with [Feedback](../elements/provide-feedback.md) on query quality, not just on final results
- A reflection routine (e.g., search logs) that surfaces students' query decisions

#### Constraints
- Advanced operators (Boolean syntax, field limits) impose extraneous load on novices; teaching them too early can degrade performance [~M] — sequence from keyword selection to operators as fluency develops
- Search engine interfaces increasingly de-emphasize operator syntax, so taught techniques may transfer inconsistently across tools [~W]
- Skills decay without ongoing practice embedded in real content-area tasks; one-off "library lessons" show little durable effect [~M]
- Effective queries improve *retrieval*, not *evaluation* — students may still select low-quality sources without complementary evaluation instruction [-W]

#### Implementation Variability
- Younger learners: keyword brainstorming, quotation marks, and "try different words" routines
- Secondary/adult learners: Boolean operators, truncation, site/domain limits, and query revision cycles
- Structured tools such as Google's "Search Education" lesson plans or library database instruction can scaffold the sequence
- Search logs and think-aloud protocols can be used formatively to diagnose individual strategy gaps

### Target Learners
- Middle school, high school, and adult learners developing digital and information literacy
- Novices who default to typing full questions and rarely revise unproductive queries [~M]
- Less necessary for experienced searchers with strong domain knowledge, who already generate effective terminology [~W]

### Target Learning Goals
- Procedural skill: constructing, testing, and revising search queries
- Strategic learning: planning and monitoring an information-seeking process
- Metacognitive development: reflecting on one's own search behavior and strategy gaps [Self-monitoring improves self-regulation.](../claims/self-monitoring-improves-self-regulation.md) [+M]

### Instructions
1. Present an authentic information need and elicit students' current search habits to activate prior knowledge ([Activation](../elements/activation.md)).
2. Model query formulation with a [Think-Aloud](../elements/think-aloud.md): identify key concepts, generate synonyms, choose keywords, and demonstrate quotation marks and operators while verbalizing each decision.
3. Provide guided [Practice](../elements/practice.md): students formulate queries for parallel tasks, compare results across query versions, and revise based on [Feedback](../elements/provide-feedback.md) on relevance and reliability of retrieved sources.
4. Have students keep a search log and reflect on which formulations worked, why, and what they will try next — building metacognitive monitoring of the process.
5. Fade support by moving students to independent research tasks in content areas, with periodic check-ins on query quality.

## Claims

- [ChatGPT users began information seeking with narrow, specified queries far more often than Google users](../claims/chatgpt-narrow-starting-queries.md) [~W]

## Related Strategies
- [Evaluating Online Sources](evaluating_online_sources.md) — the necessary complement; good queries retrieve candidates, evaluation filters them
- [Think-Aloud Modeling](think-aloud-modeling.md) — the instructional method for making expert search reasoning visible
- [Metacognitive Reflection Prompts](metacognitive_reflection_prompts.md) — structures the reflection component of this strategy

## Examples
- **Google Search Education** (https://www.google.com/insidesearch/searcheducation/) — published lesson plans and "A Google A Day" challenges that sequence keyword selection, operators, and query evaluation.
- **School library information-literacy curricula** (e.g., the Big6 framework, https://thebig6.org) — embed query formulation as the "information-seeking strategies" stage of a full research process.
- **Middle school science research project** — students search a question three ways (full question, keywords, keywords with quotation marks), compare the relevance of top results, and record which formulation worked in a search log.

## Key Sources
- Brand-Gruwel, S., Wopereis, I., & Vermetten, Y. (2005). Information problem solving by experts and novices: Analysis of a complex cognitive skill. *Computers in Human Behavior, 21*(3), 487-508. [doi:10.1016/j.chb.2004.10.005](https://doi.org/10.1016/j.chb.2004.10.005)
- Walraven, A., Brand-Gruwel, B., & Boshuizen, H. P. A. (2008). Information-problem solving: A review of problems students encounter and instructional solutions. *Computers in Human Behavior, 24*(3), 623-648. [doi:10.1016/j.chb.2007.01.030](https://doi.org/10.1016/j.chb.2007.01.030)
- Kuiper, E., Volman, M., & Terwel, J. (2005). The Web as an information resource in K–12 education: Knowledge-building and classroom integration. *Computers & Education, 45*(1), 361–371.
- Leu, D. J., Kinzer, C. K., Coiro, J., Castek, J., & Henry, L. A. (2013). New literacies: A dual-level theory of the changing nature of literacy, instruction, and assessment. In D. E. Alvermann, N. J. Unrau, & R. B. Ruddell (Eds.), *Theoretical models and processes of reading* (6th ed., pp. 1150–1181). International Reading Association.
-->
