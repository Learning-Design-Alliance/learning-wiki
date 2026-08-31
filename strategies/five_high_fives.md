---
type: strategy
title: Five High Fives
description: A movement-based game in which students try to high-five five different classmates, then use the pattern of success and failure to discover parity (handshake) reasoning.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Five High Fives

> **Strategy** · [All strategies](index.md)

## Description
Students try to give a high-five to five different classmates; when they have collected five, they sit down. The game is partly a mystery: sometimes everyone succeeds, sometimes someone is left stranded. The hidden variable — known to the teacher but not the students — is parity. Each high-five involves two people, so the total number of high-fives given is always half the number of participants; with five high-fives each, an odd-sized group cannot complete the task, while an even-sized group can. Played repeatedly across different class sizes or groupings, the game becomes a concrete, embodied puzzle from which students can induce the underlying mathematical structure.

## Design Implications

The activity pairs whole-body movement with a genuine mathematical puzzle, so it works on two fronts: brief physical activity restores attention for subsequent instruction [Classroom physical activity improves attention.](../claims/classroom-physical-activity-improves-attention.md) [+M], and the surprising failure pattern creates cognitive conflict that motivates students to seek an explanation [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]. The teacher's role is to withhold the answer, run the game under varied conditions, and then orchestrate a discussion in which students propose and test conjectures about *why* it only sometimes works.

### Context
#### Requirements
- An open space where students can move freely and pair up quickly
- Multiple rounds with deliberately varied group sizes (odd and even) so the pattern is detectable
- A follow-up discussion structure ([Class Discussion](../elements/class-discussion.md)) where students compare results and form conjectures
- Teacher tracking of group size and outcome across rounds (e.g., a simple tally on the board)

#### Constraints
- Social dynamics can leave some students repeatedly un-paired; the "loser" of each round is publicly visible, which can be uncomfortable for socially vulnerable students [-M] — mitigate by framing the leftover person as the *clue* rather than the failure
- If the teacher reveals the parity rule too early, the puzzle collapses into recall and the conjecture work is lost [-M]
- With very small groups, the pattern may not emerge from experience alone; students may need the tally data made explicit
- The connection to the handshake lemma is not automatic — without structured discussion, students may remember the game but not the mathematics [~M]

#### Implementation Variability
- Change the target number: with four or six high-fives, everyone succeeds every time, giving students a contrasting case to reason with
- Run it as a prediction game: before each round, students vote whether everyone will succeed, then test their prediction
- Substitute elbow-bumps, beanbag exchanges, or string connections for high-fives to manage hygiene or physical contact concerns
- For older students, move from the game to graph-theory representation: each student is a vertex, each high-five an edge, and the degree sum must be even

### Target Learners
- Elementary students (K–4) encountering parity and even/odd structure for the first time; adaptable upward through middle school as an introduction to graph theory and proof
- Students who benefit from embodied, kinesthetic entry points into abstract concepts
- Less suitable as-is for students for whom unstructured peer contact is aversive; offer a role as "recorder" who tallies outcomes instead

### Target Learning Goals
- Pattern recognition and conjecture-forming: noticing *when* the game works and proposing why
- Foundational number sense: parity, even/odd structure of sums
- Early proof reasoning: explaining why an odd group must leave someone out (each high-five uses two people, so the total must be even)
- Social interaction and cooperation through a shared physical task

### Instructions
1. Explain the goal: everyone must give a high-five to five different classmates, then sit down. Do not mention parity.
2. Say "go!" and let students attempt it. Observe who completes the task and who is left standing.
3. Record the outcome (group size, how many succeeded) on a visible tally, then repeat with a different group size or grouping — mixing odd and even counts across rounds.
4. Before later rounds, have students predict the outcome and justify their prediction ([Practice](../elements/practice.md) with prediction builds engagement with the underlying rule).
5. Once the tally shows a pattern, shift to [Class Discussion](../elements/class-discussion.md): ask "Why does it only work sometimes?" and let students propose and test explanations.
6. Guide students toward the key insight — every high-five involves two people, so the total must split evenly — using [Act It Out](../elements/act-it-out.md) with a small demonstration group if needed.
7. Extend: ask what happens with four or six high-fives, and why; for older students, introduce the vertex-and-edge representation.

## Related Strategies
- [Act It Out](act_it_out.md) — the same embodied-modeling move applied to word problems and processes
- [Acting-Role-Play](acting-role-play.md) — dramatizing structure through physical movement
- [Predict–Observe–Explain](predict-observe-explain.md) — the prediction cycle this game embeds in steps 4–5

## Related Elements
- [Cognitive Conflict](../elements/cognitive-conflict.md) — the failed rounds create the disequilibrium that drives the inquiry
- [Collaboration](../elements/collaboration.md) — the game is inherently interactive; every data point is a peer interaction
- [Analogies](../elements/analogies.md) — the handshake lemma analogy (party guests shaking hands) formalizes what students experienced

## Patterns That Use This Strategy
- [Cooperative Learning](../patterns/cooperative-learning.md) — structured peer interaction with individual accountability for completing the task
- [Cognitively Guided Instruction (CGI) for Math](../patterns/cgi-for-math.md) — students' own actions and conjectures, not teacher explanation, generate the mathematical idea

## Examples
- A third-grade teacher runs the game three times with class sizes of 22, 23, and 22 (one student sitting out each time). The tally on the board shows failure only on the odd-sized day, and students use this to build the even/odd explanation themselves.
- A middle-school teacher uses the game as the launch for a graph theory unit: students draw themselves as dots and their high-fives as lines, then discover that the number of odd-degree vertices must be even.

## Key Sources
- Piaget, J. (1985). *The equilibration of cognitive structures: The central problem of intellectual development.* University of Chicago Press.
- Hillman, C. H., Erickson, K. I., & Kramer, A. F. (2008). Be smart, exercise your heart: Exercise effects on brain and cognition. *Nature Reviews Neuroscience, 9*(1), 58–65. [doi:10.1038/nrn2298](https://doi.org/10.1038/nrn2298)
- Carpenter, T. P., Fennema, E., Peterson, P. L., Chiang, C.-P., & Loef, M. (1989). Using knowledge of children's mathematics thinking in classroom teaching: An experimental study. *American Educational Research Journal, 26*(4), 499–531. [doi:10.3102/00028312026004499](https://doi.org/10.3102/00028312026004499)
- West, P., & Steiner, D. (2014). *Table Tricks: Parity games and the handshake lemma.* In classroom activity collections on discrete mathematics for elementary grades (see e.g., [Mathigon parity puzzles](https://mathigon.org)).