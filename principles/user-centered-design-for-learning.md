---
type: principle
title: User-Centered Design for Learning
description: User-centered design applies human-computer-interaction methods — personas, prototyping, and usability evaluation — to reduce the extraneous cognitive load a learning interface imposes, alongside pedagogical design.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# User-Centered Design for Learning

> **Principle** · [All principles](index.md)

## Description
Learning technologies fail not only when the pedagogy is wrong, but when the interface itself creates barriers — a learner who cannot find an assignment or navigate a confusing menu is paying a cognitive cost that has nothing to do with the content being taught (Earnshaw, Tawfik, & Schmidt, 2018). **Usability** describes how easily an interface can be used as intended; **user experience (UX)** is the broader "person's perceptions and responses that result from the use... of a product, system, or service" (ISO, 2010). **User-centered design (UCD)** is the practice of centering users' needs and mental models throughout the design process rather than treating the interface as an afterthought to the pedagogy.

The connection to instructional design runs directly through [Cognitive Load Theory](../theories/cognitive-load-theory.md): a poorly designed interface — confusing navigation, unfamiliar terminology, inconsistent layout — increases **extraneous cognitive load**, which competes with the working-memory resources a learner needs for germane, schema-building processing. Distributed cognition and activity theory extend the picture to collaborative and tool-mediated settings, treating knowledge as distributed across people and artifacts rather than held only in an individual mind.

UCD proceeds iteratively: identifying user needs (often via **personas** — detailed fictional users built from real interview/observation data), gathering requirements, and building prototypes of increasing fidelity — from **paper prototypes** (fast, cheap, focused on navigation and workflow, not visuals) to **wireframes** (layout, no visual polish) to **functional prototypes** (interactive, close to final). At each stage, evaluation methods appropriate to that fidelity level are used: ethnography and focus groups early (front-end analysis), card sorting to align navigation with users' mental models, heuristic evaluation (e.g., against Nielsen's 10 usability heuristics) and cognitive walkthroughs during prototyping, and think-aloud studies, A/B testing, or eye-tracking once a functional prototype exists.

## Implications

### Context
#### Requirements
- Access to real (or representative) users for needs identification, persona-building, and evaluation — UCD's evidence base comes from data about actual users, not designer assumptions
- An iterative process budget: UCD assumes multiple rounds of prototyping and revision rather than a single build-then-ship cycle
#### Constraints
- Adds design and evaluation overhead relative to skipping usability work entirely; the investment pays off mainly when the interface is complex, novel, or used repeatedly by many learners
- Usability improvements reduce *extraneous* load but do not by themselves improve the pedagogical design of the content — the two are complementary, not substitutes

### Target Learners
- Any learner using a digital interface to access instruction, but the payoff is largest for novices unfamiliar with the interface's conventions, and for accessibility-dependent learners (e.g., users with autism, as in eye-tracking studies of facial-expression-identification interfaces)

### Target Learning Objectives
- Not a content objective — a precondition for reliably measuring content learning at all: if learners cannot navigate the interface, learning-outcome data is confounded by usability failures

### Theory
#### Supporting
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) [+M] — extraneous cognitive load from a poorly designed interface directly competes with the working-memory resources needed for germane processing
- Distributed cognition and activity theory — extend the picture from an individual user's cognitive load to knowledge distributed across people, tools, and artifacts in collaborative or workplace learning contexts

## Claims

## Related Principles
- [Scaffolding and Fading](scaffolding-and-fading.md) — both concern how much support structure a learner needs and when it should be reduced, though scaffolding targets content mastery while UCD targets interface usability
- [Cone of Experience (Concrete-to-Abstract Media Selection)](cone-of-experience.md) — both concern deliberate media/interface choice, though UCD addresses usability rather than concreteness/abstraction

## Examples
- Building a persona from user interviews before designing a course's navigation structure
- Paper prototyping a course's menu structure and running an open card sort to check it against learners' own mental categories
- A heuristic evaluation of an LMS course page against Nielsen's 10 usability heuristics before launch

## Key Sources
- Earnshaw, Y., Tawfik, A. A., & Schmidt, M. (2018). User experience design. In R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/user_experience_design](https://edtechbooks.org/lidtfoundations/user_experience_design)
- Nielsen, J. (1994). Heuristic evaluation. In J. Nielsen & R. L. Mack (Eds.), *Usability inspection methods* (pp. 25–62). Wiley.
- International Organization for Standardization. (2010). *Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems* (ISO 9241).
