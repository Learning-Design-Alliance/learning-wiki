---
type: strategy
title: Direct Instruction: Keyword Search
description: Explicit teaching of how to select, combine, and refine search keywords — including synonyms, operators, and Boolean logic — alongside criteria for evaluating the credibility of retrieved sources.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Direct Instruction: Keyword Search

> **Strategy** · [All strategies](index.md)

## Description
Direct instruction of keyword search explicitly teaches learners how to translate an information need into effective search terms: generating synonyms, combining terms with Boolean operators, using field limits and phrase quotes, and iterating when results disappoint. It also teaches evaluation criteria (authority, currency, evidence) so learners can judge what retrieval returns. The instructor models each move — thinking aloud while decomposing a question into concepts, choosing terms, and revising — then guides learners through practice with feedback.

## Design Implications

Search is a procedural skill with a large novice search space: unguided, novices flounder with vague one-word queries and accept the first plausible result. Explicit, structured teaching reduces that unproductive search and working-memory burden, consistent with evidence that novices learn procedural skills better from explicit guidance than from discovery [Worked examples reduce unnecessary search for novices.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M] and with the broader finding that minimal-guidance approaches are inefficient for novices [Kirschner, Sweller, & Clark, 2006] [+S]. Because search strategy is largely invisible expert behavior, the instruction must externalize it through [Think-Aloud](../elements/think-aloud.md)-style modeling rather than merely stating rules.

### Context
#### Requirements
- A decomposable model of the search process: question → concepts → terms → query → evaluate → revise
- Worked demonstrations on authentic questions in the learners' domain, with the instructor verbalizing term choices and revision decisions
- A controlled practice environment (e.g., a library database or curated corpus) where learners apply the sequence and receive feedback on query quality, not just result counts
- Explicit evaluation criteria for judging retrieved sources

#### Constraints
- Taught as rigid rules ("always use Boolean AND"), keyword instruction produces brittle behavior that fails when databases auto-expand, rank, or use semantic matching [~M] — modern search engines often reward natural-language queries, so operator rules must be taught as tools contingent on the system
- Direct instruction of procedures without practice in *revising* queries yields learners who can recite operators but cannot recover from a failed search [-M]
- Effectiveness drops for learners who already search fluently; redundant instruction wastes time and can reduce engagement [Worked-example guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]
- Keyword skill alone does not guarantee source evaluation; without explicit credibility criteria, learners judge by surface features such as search rank position [-M]

#### Implementation Variability
- **Full modeling → guided practice → independent search**: a fading sequence from instructor demonstration to solo retrieval
- **Query worksheets**: learners plan concepts and synonyms on paper before touching the search box, reducing load during formulation [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]
- **Contrasting query cases**: showing a weak query beside a strong one for the same question helps learners abstract what makes terms effective [Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md) [+M]
- **Embedded instruction**: keyword teaching integrated into a content unit (e.g., a research essay) rather than a standalone library session, improving transfer to real tasks

### Target Learners
- Novices — secondary and early undergraduate students — encountering library databases or academic search for the first time [+M]
- Learners with low domain vocabulary, who need explicit support generating synonyms and discipline-specific terms; vocabulary breadth directly constrains query quality
- Less beneficial for experienced searchers, who benefit more from advanced technique refreshers than from basic operator instruction [~M]

### Target Learning Goals
- Procedural skill: formulating, executing, and revising search queries
- Strategic knowledge: knowing *when* to broaden, narrow, or re-conceptualize a search
- Critical evaluation: judging the credibility and relevance of retrieved sources
- Metacognitive monitoring: recognizing when results indicate the query, not the literature, is the problem

### Instructions
1. **Activate the need.** Pose an authentic research question and elicit learners' initial search attempts; surface the gap between their results and the available literature.
2. **Model decomposition.** Think aloud while breaking the question into 2–3 core concepts, generating synonyms for each — an [Advance Organizer](../elements/advance-organizers.md) for the query-planning sequence.
3. **Demonstrate query construction.** Show concept combination with Boolean operators, phrase quotes, and truncation, verbalizing each decision; keep the demonstration chunked so learners hold only one move in mind at a time.
4. **Demonstrate evaluation and revision.** Model judging a result's credibility and diagnosing a weak query ("too many results → add a limiting concept").
5. **Guide practice.** Learners execute parallel searches on a new question with a planning worksheet, then compare queries and results in pairs; prompt them to explain why one query outperformed another [Self-explanation improves conceptual understanding.](../claims/self-explanation-improves-conceptual-understanding.md) [+M].
6. **Fade support.** Move learners to independent searching on their own questions, with feedback shifting from query mechanics to strategy and source evaluation.

## Related Strategies
- Direct instruction of keyword search is a specific application of explicit teaching of procedural skills; it pairs naturally with worked-example and modeling approaches for any invisible expert process.

## Examples
- **The Big6 information literacy framework** (Eisenberg & Berkowitz) — a widely adopted K–12 curriculum that explicitly teaches task definition, information-seeking strategies, and source evaluation as sequenced steps ([https://thebig6.org](https://thebig6.org)).
- **ACRL Framework for Information Literacy** — academic librarians' one-shot and credit-bearing instruction sessions routinely use modeled keyword demonstrations on databases such as EBSCOhost and JSTOR ([https://www.ala.org/acrl/standards/ilframework](https://www.ala.org/acrl/standards/ilframework)).
- **Google Search Education** — Google's "A Google A Day" challenges and Search Education lesson plans taught operators and query refinement through modeled, then practiced, searches.

## Key Sources
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Brand-Gruwel, S., Wopereis, I., & Vermetten, Y. (2005). Information problem solving by experts and novices: Analysis of a complex cognitive skill. *Computers in Human Behavior, 21*(3), 487–508. [doi:10.1016/j.chb.2004.10.005](https://doi.org/10.1016/j.chb.2004.10.005)
- Walraven, A., Brand-Gruwel, S., & Boshuizen, H. P. A. (2008). Information-problem solving: A review of problems students encounter and instructional solutions. *Computers in Human Behavior, 24*(3), 1023–1038. [doi:10.1016/j.chb.2007.01.030](https://doi.org/10.1016/j.chb.2007.01.030)
- Eisenberg, M. B., & Berkowitz, R. E. (1990). *Information problem-solving: The Big Six skills approach to library and information skills instruction.* Ablex.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285. [doi:10.1207/s15516709cog1202_4](https://doi.org/10.1207/s15516709cog1202_4)