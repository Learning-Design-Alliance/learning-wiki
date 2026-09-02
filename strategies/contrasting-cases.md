---
type: strategy
id: contrasting-cases
title: Contrasting Cases
description: Learners compare two or more cases that share surface features but differ on one critical dimension, so the dimension that matters becomes perceptible.
status: review
generated:
  by: claude/unspecified
  at: 2026-08-30
sources:
  - id: schwartz-bransford-1998
    resource: "https://doi.org/10.1207/s1532690xci1604_4"
    title: "Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522"
    author: "Schwartz, D. L., & Bransford, J. D"
  - id: alfieri-2013
    resource: "https://doi.org/10.1080/00461520.2013.775712"
    title: "Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. *Educational Psychologist, 48*(2), 87–113"
    author: "Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D"
  - id: gentner-2003
    resource: "https://doi.org/10.1037/0022-0663.95.2.393"
    title: "Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology, 95*(2), 393–408"
    author: "Gentner, D., Loewenstein, J., & Thompson, L"
  - id: rittle-johnson-star-2007
    resource: "https://doi.org/10.1037/0022-0663.99.3.561"
    title: "Rittle-Johnson, B., & Star, J. R. (2007). Does comparing solution methods facilitate conceptual and procedural knowledge? An experimental study on learning to solve equations. *Journal of Educational Psychology, 99*(3), 561–574"
    author: "Rittle-Johnson, B., & Star, J. R"
---

# Contrasting Cases

> **Strategy** · [All strategies](index.md)

## Description
Contrasting cases are two or more examples deliberately built to be alike in most respects and different in exactly the respect the learner is supposed to notice. Placed side by side, the difference becomes perceptible in a way it never is when cases are met one at a time — a single case gives the learner nothing to measure it against, so its critical features and its incidental ones look alike. The strategy's defining move is the design of the contrast set, not the act of comparing: what varies across the cases is what learners will end up attending to, so the variation has to be built to point at the target feature and hold everything else still.

## Design Implications

Comparison outperforms studying the same cases sequentially, and the advantage is largest when learners are prompted to state what differs rather than left to notice on their own [Comparing Contrasting Cases Improves Learning](../claims/comparing-contrasting-cases-improves-learning.md) [+S]. The mechanism is alignment: setting two structurally similar cases against each other forces the learner to map one onto the other, and the residue of that mapping is an abstracted schema rather than a memory of two episodes [Multiple Contrasting Cases Support Abstraction](../claims/multiple-contrasting-cases-support-abstraction.md) [+S], which is also why the abstraction transfers to problems that look nothing like the originals [Analogical Reasoning Improves Transfer](../claims/analogical-reasoning-improves-transfer.md) [+M].

The strategy is most distinctive when it runs *before* instruction. Schwartz and Bransford's "time for telling" result is that learners who first analyse contrasting cases and then hear an explanation outperform learners who get the explanation first — the contrast set does not teach the concept, it manufactures the noticing that makes the subsequent explanation land [Cognitive disequilibrium motivates conceptual change](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]. Used that way it is a preparation activity, and judging it on what learners can do immediately after the comparison, before any telling, will make it look like a failure.

### Context
#### Requirements
- A set of cases engineered so that one dimension varies and the rest are held constant — off-the-shelf examples almost never satisfy this and usually have to be built
- A prompt that requires learners to *articulate* the difference; silent side-by-side presentation produces much weaker effects ([Articulation](../elements/articulation.md))
- Enough prior knowledge to interpret each individual case; a learner who cannot read one case cannot compare two [Activation Improves Learning](../claims/activation-improves-learning.md) [+M]
- Simultaneous presentation — cases visible at the same time, not on successive pages or slides
- A follow-up explanation or consolidation step when the cases are used before instruction ([Demonstration](../elements/demonstration.md))

#### Constraints
- Cases that differ on several dimensions at once teach nothing in particular: learners cannot tell which difference matters, and comparison degrades into listing [-M]
- Comparison imposes real working memory cost — two cases must be held and aligned at once — so contrast sets that are long, dense, or split across pages overload novices and the benefit disappears [Cognitive Overload Degrades Learning](../claims/cognitive-overload-degrades-learning.md) [-S]
- Superficially similar cases invite surface mapping: learners align the matching cover stories and miss the structural difference entirely [-M]
- Guidance that supports novice comparison becomes redundant for learners who already hold the schema, and can slow them down [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]
- Where the goal is a procedure to be executed fluently rather than a concept to be discriminated, studying and practising a single worked example is the more efficient route [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [~M]

#### Implementation Variability
- **Before instruction (preparation for future learning)** — learners analyse the contrast set, attempt to invent an account of the difference, and only then receive the canonical explanation
- **After instruction** — the contrast set is used to sharpen a concept learners already hold, testing the boundary between cases that do and do not fall under it
- **Correct versus erroneous** — one case is right and one contains a targeted error, so the comparison isolates the misconception [Erroneous examples improve conceptual understanding by forcing comparison with correct models.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+M]
- **Multiple solution methods** — the cases are different valid routes to the same answer, so what varies is method rather than content ([Comparing Multiple Solution Methods](comparing_multiple_solution_methods.md))
- **Progressive narrowing** — an initial wide contrast establishes the dimension, then successive pairs narrow the gap until learners discriminate fine differences

### Target Learners
- Novices who cannot yet tell which features of a case matter — the population for whom a single example is genuinely ambiguous
- Learners holding a robust intuitive misconception, where a contrast that the misconception predicts wrongly is more persuasive than an explanation
- Learners moving from recognition to discrimination in a domain with confusable categories: clinical signs, chemical structures, genre conventions, code smells
- Weaker fit for learners who already discriminate reliably, for whom the comparison adds load without adding information [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Perceptual discrimination: reliably telling apart categories that look alike to a novice
- Conceptual understanding of what a principle actually ranges over, including the cases it excludes
- Transfer to structurally similar problems with different surface features [Analogical Reasoning Improves Transfer](../claims/analogical-reasoning-improves-transfer.md) [+M]
- Readiness to learn from a subsequent lecture, text, or demonstration
- Flexible knowledge in ill-structured domains where no single case is representative [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]

### Instructions
1. **Name the discrimination.** State the single feature learners should end up able to detect. If you cannot state it in one sentence, the contrast set cannot be designed yet.
2. **Build the cases around that one difference.** Construct two to four cases that vary on the target feature and match on everything else — same context, same length, same surface story. Resist making the cases interesting in ways that vary.
3. **Present them together.** Put the cases on one page or one screen so alignment is a matter of looking rather than remembering ([Cognitive Load Management](../principles/cognitive-load-management.md)).
4. **Prompt the comparison explicitly.** Ask what differs and what stays the same, and require a written or spoken answer — the articulation is the learning event, not the display ([Articulation](../elements/articulation.md), [Self-Explanation](../elements/self-explanation.md)).
5. **Let learners attempt an account.** Before supplying the answer, have them propose why the difference matters. Wrong proposals are useful: they expose the feature learners were actually tracking.
6. **Then tell.** Deliver the explanation, definition, or formalism, referring back to the specific cases learners just argued over ([Demonstration](../elements/demonstration.md)).
7. **Test the discrimination on new cases.** Give unseen examples, including a near-miss, and ask learners to classify and justify ([Practice](../elements/practice.md), [Feedback](../elements/feedback.md)).

## Related Strategies
- [Comparing Contrasting Cases](comparing-contrasting-cases.md) — the same move framed around the comparison activity rather than the design of the case set
- [Comparing Cases](comparing_cases.md) — comparison of cases that are not necessarily engineered to isolate a single dimension
- [Analogical Encoding](analogical-encoding.md) — comparison of structurally parallel cases to abstract a shared relational schema, rather than to detect a difference
- [Comparing Multiple Solution Methods](comparing_multiple_solution_methods.md) — contrasting cases applied to procedures instead of concepts
- [Worked Examples](worked-examples.md) — the alternative when the goal is fluent execution rather than discrimination; example–problem pairs and contrast sets often alternate [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-examples-example-problem-sequences.md) [+S]
- [Case-Based Learning](case-based_learning.md) — extended authentic cases, where the contrast is across a sequence rather than within one activity [Case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [+M]

## Examples

**Schwartz and Bransford's density and variability cases:** Undergraduates analysed contrasting data sets before reading a text on the underlying concept, and outperformed peers who read the text first — the canonical demonstration that comparison prepares learners to learn.

**Equation-solving with paired solution methods:** Rittle-Johnson and Star presented algebra students with two solutions to the same equation side by side and asked which was better and why; comparing methods produced greater procedural flexibility than studying the methods sequentially.

**Analogical encoding in negotiation training:** Gentner, Loewenstein, and Thompson had learners compare two negotiation scenarios sharing a deep structure; those who compared were far more likely to use the strategy later in an unrelated negotiation than those who studied the cases separately.

**Clinical image pairs:** Radiology and dermatology teaching sets pair a positive and a near-miss negative image differing only in the diagnostic feature, so trainees learn what the feature looks like rather than what a positive case looks like.

## Key Sources
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522. [doi:10.1207/s1532690xci1604_4](https://doi.org/10.1207/s1532690xci1604_4)
- Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. *Educational Psychologist, 48*(2), 87–113. [doi:10.1080/00461520.2013.775712](https://doi.org/10.1080/00461520.2013.775712)
- Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology, 95*(2), 393–408. [doi:10.1037/0022-0663.95.2.393](https://doi.org/10.1037/0022-0663.95.2.393)
- Rittle-Johnson, B., & Star, J. R. (2007). Does comparing solution methods facilitate conceptual and procedural knowledge? An experimental study on learning to solve equations. *Journal of Educational Psychology, 99*(3), 561–574. [doi:10.1037/0022-0663.99.3.561](https://doi.org/10.1037/0022-0663.99.3.561)
