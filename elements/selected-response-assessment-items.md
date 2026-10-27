---
type: element
id: selected-response-assessment-items
title: Selected-Response Assessment Items
description: Multiple-choice, true-false, and matching items ask students to select rather than construct a response — easy to score objectively, but hard to write well, and appropriate mainly for recognition-level rather than complex learning goals.
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# Selected-Response Assessment Items

> **Element** · [All elements](index.md)
> **Evidence** · 27 claims (4 for, 19 mixed, 4 against) · 26 studies (7 associational, 5 causal, 5 review, 5 design, 2 qualitative, 1 quant-synthesis, 1 theoretical), `q1`–`q3` · 6 of 26 report an effect size · 25 claims rest on one study

## Description
In selected-response items — multiple-choice, true-false, and matching — students select a response the teacher or test developer provides rather than constructing one in their own words, so the item measures recognition rather than recall. Because results don't depend on a scorer's judgment (and so are often machine-scored), these items are called "objective," and their elimination of scoring error increases reliability. But teachers who rely on objective items exclusively risk reducing the validity of their overall assessment, since objective items aren't appropriate for every learning goal — effective assessment depends on aligning the technique to the actual goal (if the goal is for students to conduct an experiment, they should be asked to conduct one, not asked about conducting one).

**True-false items** suit factual knowledge — vocabulary, formulae, dates, proper names, technical terms. They're efficient (simple structure, quick to complete) and easier to construct than multiple-choice or matching items, but carry a 50 percent guessing probability, which makes it hard to interpret how much a given score actually reflects knowledge. **Matching items** present two parallel columns (terms, phrases, symbols, or numbers) for the student to pair up, typically with more items in the second column than the first (so a single error doesn't force a second one); they mostly measure lower-level knowledge — people and achievements, dates and events, terms and definitions — and depend on genuinely homogeneous columns, which are harder to construct than they look. **Multiple-choice items** are the most widely used selected-response format because, unlike true-false and matching, they can be adapted to assess higher-order thinking (application) as well as factual recall; students must recognize the correct answer rather than merely reject the incorrect one, and four or five alternatives reduce guessing well below the true-false item's 50 percent.

Common item-writing errors, by format:

| Format | Error | Why it fails |
|---|---|---|
| True-false | Broad generalization stated as absolutely true or false | A statement that's "usually" true (e.g., "The president is elected to office") ignores real exceptions (succession), making the item ambiguous |
| True-false | Opinion presented as fact | A statement some people believe and others don't has no defensible true-false answer |
| True-false | Two ideas combined in one item | If one half is true and the other false, students can't tell which to mark |
| True-false / multiple-choice | Irrelevant cues | Absolute qualifiers ("always," "never," "all") tend to signal false items; qualified language ("usually," "generally") tends to signal true ones — students learn to exploit the pattern rather than the content |
| Matching | Non-homogeneous columns | Mixing categories (e.g., a mix of dates and names) in one column lets students eliminate options by category rather than by knowing the answer |
| Matching | More than ~10 items per list | Long lists (recommended range: 4-7) make the search itself the difficulty, not the content |
| Matching | Non-logical order | An alphabetized or otherwise unordered second column forces time-consuming searching unrelated to the content being tested |
| Multiple-choice | Unclear stem | A stem that doesn't clearly state the problem (e.g., a list of true/false facts about a country followed by "which statement is true") forces students to evaluate every alternative as its own true-false item |
| Multiple-choice | Implausible distractors | An alternative anyone could rule out on background knowledge alone effectively turns a four-option item into a much easier two- or three-option one |
| Multiple-choice | Irrelevant cues | A correct alternative that's noticeably longer, or grammatically mismatched incorrect alternatives, or an uneven distribution of the correct answer across positions, all let test-savvy students guess without knowing the content |
| Multiple-choice | "All of the above" | Lets a student who confirms the first two alternatives as true skip evaluating the rest, and lets one confirmed-false alternative rule out the option entirely — neither behavior tests the intended knowledge |

Other common item-writing mistakes cut across formats: unclear wording (leaving students unsure what's actually being asked), lifting sentences directly from the textbook or lecture notes (removing them from their original context can quietly change or obscure their meaning), and testing trivial facts (the exact year of a theorist's birth) rather than what's actually important to know.

## Design Implications

### Context
#### Requirements
- Careful, deliberate item construction — selected-response items are easy to *score* but hard to *write* well, and most common problems stem from teachers not investing enough time in construction
- A learning goal genuinely suited to recognition-level assessment, since aligning item type to the actual instructional goal is what makes the assessment valid in the first place
#### Constraints
- True-false items carry a 50 percent guessing floor that limits how confidently a score can be interpreted
- Selected-response formats as a whole are poorly suited to complex learning outcomes like integration, application-in-context, or written expression — see [Constructed-Response Assessment Items](constructed-response-assessment-items.md) for formats built for those goals
- Deliberately including some negative-phrased items to give students practice with a format standardized tests use is a defensible tradeoff, but should be a deliberate choice, not an accident

### Target Learners
- All students in a K-12 or classroom-assessment context; true-false's guessing floor makes it a weaker choice specifically when a precise estimate of individual knowledge matters

### Target Learning Goals
- Recognition-level factual, definitional, and lower-order conceptual knowledge (true-false, matching); recognition-level knowledge extending to application (multiple-choice)

### Affordances
- [Validity, Reliability, and Bias in Classroom Assessment](../principles/validity-reliability-and-bias-in-classroom-assessment.md) — selected-response items trade some validity (format constrains what can be assessed) for reliability (no scorer judgment involved)

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Taking initial multiple-choice tests without feedback can lead students to later produce the incorrect lure answers they selected, even when an overall retrieval practice benefit occurs](../claims/multiple-choice-lures-can-be-learned-as-false-knowledge.md) [-W]
- [Initial short-answer tests outperform initial multiple-choice tests mainly when feedback follows them; without feedback, the higher initial success of multiple-choice tests can favor multiple-choice](../claims/feedback-determines-whether-short-answer-retrieval-outperforms-multiple-choice.md) [~W]
- [Having more multiple-choice alternatives benefits later retention when initial retrieval success is high but hurts learning when it is low](../claims/effect-of-more-multiple-choice-alternatives-depends-on-initial-retrieval-success.md) [~W]
- [Evidence on whether initial short-answer questions produce more learning than initial multiple-choice questions is mixed, with recent studies finding little or no difference](../claims/short-answer-versus-multiple-choice-retrieval-practice-evidence-is-mixed.md) [~W]
- [MCQs generated by the generate-then-validate SLM pipeline are generally answerable and unambiguous, as judged by seven human experts](../claims/slm-generated-mcqs-answerable-unambiguous-human-judges.md) [+W] — attached 2026-10-11 from Generate-Then-Validate: Question Generation for Education, which proposed "Generate-Then-Validate: a Phi-2-based question generation pipeline with expansive generation and selective validation".
- [Candidate selection is a second bottleneck: an oracle ranker over proposed candidates substantially raises proportional match, and plausibility checks reject some valid distractors](../claims/candidate-selection-loss-oracle-ranker.md) [~W]
- [The multiple-choice component of the revised ELA placement test strongly measured overall ELA performance, but few items strongly measured the three specific ELA domains](../claims/cmi-ela-test-strong-overall-weak-domain-measurement.md) [~W]
- [Teachers' dyslexia knowledge differs depending on whether an item presents a term or an explanation of the term](../claims/dyslexia-knowledge-term-versus-explanation-items.md) [~W]
- [LLM-generated retrieval practice was practical to deploy and well received, but high correctness rates (about 70% of items at p=1.0) restricted score variance](../claims/llm-generated-retrieval-practice-deployable-but-high-accuracy-limits-variance.md) [~W]
- [Lesson designers report LLM-generated lessons save substantial time drafting scenarios and multiple-choice questions](../claims/llm-lessons-time-saving-scenario-drafting.md) [~W]
- [Distractor distribution did not differ across ChatGPT, Google Gemini and NLE MCQs](../claims/distractor-distribution-does-not-differ-across-sources.md) [~W]
- [Judging learning-objective alignment of generated MCQs is more subjective than answering them, with only moderate human agreement](../claims/lo-alignment-judgment-more-subjective-than-answering.md) [~M]
- [MCQ accuracy was high (above 87%) across all conditions with no significant difference between diverse and generic explanations](../claims/mcq-accuracy-no-significant-condition-difference.md) [~W]
- [Children are considerably more overconfident about incorrect answers to true-false questions than about incorrect answers to open-ended questions](../claims/overconfidence-incorrect-answers-higher-true-false.md) [-W]
- [Multiple-choice single-select items are less difficult than open-ended response questions, and delayed perceived task difficulty ratings relate more strongly to relative item difficulty for open-ended items](../claims/answer-format-availability-affects-difficulty-and-ratings.md) [+W]
- [AI pilots found models not yet capable of high-quality math output generation, including multiple choice problems, coherent word problems, and math visuals](../claims/ai-not-capable-math-output-generation.md) [~W]
- [Model and student error patterns on IVDA MCQs show limited question-level consistency but comparable difficulty distributions for easiest and hardest questions](../claims/limited-model-student-question-level-alignment.md) [~W]
- [Multiple-choice testing increases the later production of multiple-choice lures as answers on cued recall tests, even under warning against guessing](../claims/mc-testing-increases-lure-production.md) [-W]
- [PeerWise student ratings of multiple-choice questions correlate well with instructor ratings (0.5 and 0.58)](../claims/peerwise-student-ratings-correlate-instructor-ratings.md) [~W]
- [The true-versus-false statement accuracy difference is larger for misconception than control trials, and significant for science but not maths](../claims/trial-statement-interaction-science-not-maths.md) [~W]
- [Competitive true-false questions can produce benefits similar to competitive multiple-choice questions for previously asked and related questions](../claims/competitive-true-false-similar-benefits.md) [~W]
- [Open response format is associated with higher Alpha than multiple choice in knowledge tests](../claims/knowledge-test-alpha-response-format.md) [-W]
- [Word-picture matching task accuracy was predicted by post-test scores but not pre-test scores, supporting it as a concurrent measure of learning](../claims/matching-task-post-scores-concurrent-learning.md) [~W]
- [Case-based (vignette) MCQs are classified as testing higher-order thinking and discriminate better between low- and high-information students](../claims/case-based-questions-higher-order-value.md) [~W]
- [Expert evaluation found the hybrid system's generated MCQ stems promising in usefulness and grammatical correctness](../claims/expert-evaluation-mcq-stems-promising.md) [~W]

## The evidence by question
- *Which practice format: short answer, multiple choice, or matching the final test?* [Evidence on whether initial short-answer questions produce more learning than initial multiple-choice questions is mixed, with recent studies finding little or no difference](../claims/short-answer-versus-multiple-choice-retrieval-practice-evidence-is-mixed.md) [~M]
- *Can taking a multiple-choice test teach learners the wrong answers it shows them, and does feedback prevent that?* [Taking initial multiple-choice tests without feedback can lead students to later produce the incorrect lure answers they selected, even when an overall retrieval practice benefit occurs](../claims/multiple-choice-lures-can-be-learned-as-false-knowledge.md) [~M]
- *Can selected-response items measure higher-order skills and specific domains, or mainly overall recognition-level knowledge?* [Multiple-choice state tests are prone to ceiling and floor effects and do not measure higher-order skills well](../claims/multiple-choice-state-tests-limits-high-low-performers.md) [+M]
- *Can a language model write usable multiple-choice items and distractors, or do its drafts need human review?* [AI-generated assessment items frequently need faculty correction, supporting AI as a draft generator within quality assurance](../claims/genai-assessment-items-draft-generator-quality-assurance.md) [+M]

## Related Elements

- [Constructed-Response Assessment Items](constructed-response-assessment-items.md) — the complementary item family for goals selected-response can't reach
- [Developmental checklists for one-to-one correspondence, classification, and seriation as teacher assessment and curriculum-planning tools](preschool-math-development-checklists.md)
- [Traditional multiple-choice test item structure: stem, alternatives, and plausible distractors](traditional-mc-item-stem-alternatives-distractors.md)
- [Sound unit test outcome measure for the TEEMSS evaluation](../products/teemss-sound-unit-test.md)

## Examples

- A true-false item testing whether "the U.S. Civil War Battle of Fort Sumter" occurred before or after a listed date, versus a poorly-worded version bundling two separate historical claims into one statement
- A multiple-choice item testing application of the "law of diminishing returns" concept via a novel scenario, versus one merely testing recall of the definition
- [Sequence retrieval practice from less effortful item types (multiple choice, factual) to more effortful ones (short answer, applied) as learners reach mastery](../strategies/sequence-practice-easy-to-difficult-item-types.md)
- [Use true-false examinations with immediate self-correction and public display of scores as a time-saving teaching and assessment routine](../strategies/true-false-immediate-correction-display-strategy.md)

## Key Sources
- Linn, R. L., & Miller, M. D. (2005). *Measurement and assessment in teaching* (9th ed.). Pearson.
- Arduini-Van Hoose, N. (2020). Teacher-made assessments. In *Educational psychology*. Retrieved from https://edpsych.pressbooks.sunycreate.cloud. CC BY-NC-SA 4.0.
