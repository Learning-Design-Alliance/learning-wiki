---
type: element
id: selected-response-assessment-items
title: Selected-Response Assessment Items
description: Multiple-choice, true-false, and matching items ask students to select rather than construct a response — easy to score objectively, but hard to write well, and appropriate mainly for recognition-level rather than complex learning goals.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# Selected-Response Assessment Items

> **Element** · [All elements](index.md)

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

## Related Elements
- [Constructed-Response Assessment Items](constructed-response-assessment-items.md) — the complementary item family for goals selected-response can't reach

## Examples
- A true-false item testing whether "the U.S. Civil War Battle of Fort Sumter" occurred before or after a listed date, versus a poorly-worded version bundling two separate historical claims into one statement
- A multiple-choice item testing application of the "law of diminishing returns" concept via a novel scenario, versus one merely testing recall of the definition

## Key Sources
- Linn, R. L., & Miller, M. D. (2005). *Measurement and assessment in teaching* (9th ed.). Pearson.
- Arduini-Van Hoose, N. (2020). Teacher-made assessments. In *Educational psychology*. Retrieved from https://edpsych.pressbooks.sunycreate.cloud. CC BY-NC-SA 4.0.
