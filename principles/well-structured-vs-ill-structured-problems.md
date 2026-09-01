---
type: principle
id: well-structured-vs-ill-structured-problems
title: Well-Structured vs. Ill-Structured Problems
description: Problems vary in how much information and how clear a solution procedure they provide; well-structured problems support algorithms with guaranteed correct solutions, while ill-structured problems require heuristics that work often but not always.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# Well-Structured vs. Ill-Structured Problems

> **Principle** · [All principles](index.md)

## Description
Problems vary along two related dimensions: how much of the information needed for a solution is actually given, and how many (and how clear) the rules or procedures for reaching a solution are. A **well-structured problem** provides most of the needed information and can, in principle, be solved with relatively few clearly understood rules — the word problems common in math classes are a classic example, since everything needed is contained in the stated problem and the solution procedure is relatively clear and precise. An **ill-structured problem** has the opposite qualities: the needed information is not necessarily contained in the problem itself, many different procedures are potentially applicable, and multiple different solutions are plausible (Voss, 2006) — extreme examples include "How can the world achieve lasting peace?" or "How can teachers ensure that students learn?"

A well-defined, guaranteed-correct procedure for a well-structured problem is called an **algorithm** (e.g., the procedure for long division, or the instructions for a computer routine) (Leiserson et al., 2001). Algorithms only work when a problem is genuinely well-structured and there is no ambiguity about whether the algorithm even applies; carried to an ill-structured problem, where there is real ambiguity about how to proceed or even what the problem is actually asking, algorithms fail. For ill-structured problems, a **heuristic** — a general strategy or "rule of thumb" that often works but is not guaranteed to — is more appropriate (e.g., scanning a library catalog for relevant-looking titles when starting research for a term paper offers no guarantee of finding the best sources, but succeeds often enough to be worth trying).

Many real problems are not purely one or the other. A nine-dot puzzle ("connect all nine dots using only four straight lines") looks well-structured — nine dots, four lines, a seemingly precise task — but is not completely so, since the puzzle's real solution requires information (that lines may extend beyond the dots) that was never explicitly stated. Learners applying the simple algorithm "draw one line, then another, then another" fail; solving it requires recognizing that a heuristic-like reframing (questioning what "draw a line" was actually taken to mean) is needed instead.

## Implications

### Context
#### Requirements
- Accurate diagnosis of whether a task is genuinely well-structured (an algorithm will work) or actually ill-structured behind a well-structured-looking surface (a heuristic or reframing is needed)
#### Constraints
- Applying an algorithm to an ill-structured problem, or expecting a single guaranteed procedure where none exists, produces persistent failure that looks like a reasoning deficit but is really a mismatched strategy
- [Functional fixedness](../claims/functional-fixedness-limits-problem-solving.md) [-M] is especially likely to trap solvers on problems that look well-structured but actually depend on an unstated assumption

### Target Learning Objectives
- Correctly classifying a problem as well- or ill-structured before choosing a solution approach, rather than defaulting to algorithmic procedure regardless of fit

### Strategies for Solving Ill-Structured Problems
Beyond recognizing structure, several general strategies help regardless of a problem's specific content (Thagard, 2005): **problem analysis** — identifying a problem's component parts and working on each separately, especially useful for ill-structured problems (e.g., "devise a plan to improve bicycle transportation in the city" decomposes into installing bike lanes, educating cyclists and motorists, fixing potholes, and revising relevant traffic laws); [working backward](../strategies/direct_instruction-problem-solving_strategies.md) — starting from the target solution and reasoning back to the given problem, useful when a well-structured problem contains distracting or misleading elements; and [analogical thinking](analogical-reasoning.md) — using a structurally similar prior problem or experience to guide a new one (e.g., applying lessons from improving conditions for cars to the bicycle-transportation problem, since both involve roadway and driver-education measures).

## Related Principles
- [Analogical Reasoning](analogical-reasoning.md) — one of the general strategies useful across both well- and ill-structured problems
- [Problem-based Learning](problem-based-learning.md) — deliberately poses ill-structured problems as a design choice

## Examples
- A "word lily" problem ("lilies double their lake coverage every day; it takes 100 days to cover the whole lake — how many days to cover half?") is well-structured and solvable by working backward from Day 100, but a solver who treats the stated lily size as relevant has misrepresented the problem and will be misled by irrelevant information.

## Key Sources
- Voss, J. F. (2006). Toulmin's model and the solving of ill-structured problems. In D. Hitchcock & B. Verheij (Eds.), *Arguing on the Toulmin model* (pp. 303-311). Springer.
- Leiserson, C. E., Rivest, R. L., Stein, C., & Cormen, T. H. (2001). *Introduction to algorithms* (2nd ed.). MIT Press.
- Thagard, P. (2005). *Mind: Introduction to cognitive science* (2nd ed.). MIT Press.
- Arduini-Van Hoose, N. (2020). Problem-solving. In *Educational psychology*. Retrieved from https://edpsych.pressbooks.sunycreate.cloud. CC BY-NC-SA 4.0.
