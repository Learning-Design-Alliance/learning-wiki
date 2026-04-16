---
name: building-learning-patterns
description: Selects instructional patterns for a project by searching the ld-wiki patterns library. Accepts user-provided patterns or context; searches and reads wiki pages; evaluates arc coverage (activation → instruction → practice → reflection); presents candidates for user approval; resolves each pattern into a phase sequence with design guidance; and writes the result to projects/[name]/learning-patterns.md. Run after defining-learning-principles.
---

# Building Learning Patterns

Produces **`projects/[project-name]/learning-patterns.md`** — the selected and fully described pattern set for this project. The user approves what goes in.

---

## Step 0 — Gather inputs

Read `projects/[name]/learning-principles.md` — required. If missing, run `defining-learning-principles` first.

From learning-principles.md and any prior context, identify:
- **Design level**: course / unit / lesson (sets grain_size filter)
- **Objective types**: procedural, conceptual, problem-solving, dispositional
- **Delivery format**: self-paced / blended / live; sync or async; device
- **Learner profile**: novice/advanced, age range, special factors
- **Principles in scope** — patterns must connect to at least one

---

## Step 1 — Accept user-provided patterns

Ask: *"Do you have any instructional patterns, frameworks, or structural approaches you'd like to start with? These could be named patterns (e.g. 'Problem-Based Learning'), frameworks from your research, or how you usually structure your courses."*

Accept any form: named patterns with or without phase sequences, described structures, research frameworks, or nothing (proceed to Step 2).

---

## Step 2 — Search the wiki

Read `index.md` to get the full list of pattern pages. Then:

1. Filter by `grain_size` matching the design level — read the frontmatter of candidate pages and exclude mismatches.
2. Grep `patterns/` for pages matching objective types, delivery format, and learner profile keywords.
3. Read the 8–12 most relevant pattern pages. For each, focus on:
   - `## Description` — what the pattern is and what problem it solves
   - `### Grain Size` — course / unit / lesson
   - `### Target Goals` — what objective types it serves
   - `### Target Learners` — who it fits
   - `### Context > Requirements` — what must be in place to use it
   - `### Context > Constraints` — when it fails or causes harm
   - `### Theory > Supporting / Contradicting` — theoretical grounding
   - `### Claims` — linked claims with evidence tags
   - `## Design > Sequence` — the phase sequence (if present)

Evaluate arc coverage across candidates:

| Arc phase | Covers |
|---|---|
| Activation | Prior knowledge, motivation, hook |
| Instruction | Concept delivery, modeling, worked examples |
| Practice | Application, guided and independent |
| Reflection/Transfer | Assessment, consolidation, real-world connection |

Note which arc phases the user's submitted patterns already cover and which are missing.

---

## Step 3 — Select and normalize candidates

For each candidate (user-submitted + wiki finds), normalize to this schema:

```
Name: [pattern name — use wiki page title or user's name]
Wiki: [[patterns/slug]]  ← omit if not from wiki
Grain size: [course | unit | lesson]
Best for: [objective type and learner context — from Target Goals and Target Learners sections]
Arc phases covered: [list which arc phases this pattern addresses]
Phases: [ordered phase names — verbatim from wiki Design > Sequence, or derived from user submission]
Rationale: [why this pattern fits THIS project — trace to a specific principle in learning-principles.md]
Constraints to flag: [any constraints from the wiki page that apply to this project]
```

Apply selection rules before presenting:
1. **Grain size must match** the design level — do not select a course-level pattern for lesson design
2. **Check Constraints** — exclude patterns that contradict the delivery format or learner level
3. **Cover the arc** — selected patterns together must span activation → instruction → practice → reflection
4. **No duplicates** — patterns must complement, not repeat, each other
5. **Trace to principles** — each pattern must connect to at least one principle in learning-principles.md
6. **Audience patience filter** — if learners are time-constrained or task-oriented, reject patterns with more than 5 mandatory sequential phases unless phases can be collapsed

Aim for 3–5 patterns total.

---

## Step 4 — Present candidates for approval

Present all candidates as a numbered list:

> "Here are the patterns I've gathered. Which would you like to include? You can say 'all', list numbers, or ask me to adjust any of them."

For each candidate show: name, grain size, arc phases covered, and which principle it connects to.

Wait for the user's selection before writing output.

---

## Step 5 — Resolve and write output

For each approved pattern, re-read its wiki page and extract the full design detail:

- Phase sequence (from `## Design > Sequence` — verbatim names)
- Design guidance (from `## Design > Affordances` and `### Personalization` if present)
- Claims and evidence tags (from `### Claims`)
- Constraints to flag for the designer

Write approved patterns to `projects/[project-name]/learning-patterns.md`:

```markdown
# Learning Patterns — [Project Name]

*[Date]. Approved by user.*

## Arc Coverage
| Arc phase | Pattern(s) |
|---|---|
| Activation | [names] |
| Instruction | [names] |
| Practice | [names] |
| Reflection/Transfer | [names] |

---

## [Pattern Name]

**Grain size:** [course | unit | lesson]
**Best for:** [objective type and learner context]
**Wiki:** [[patterns/slug]]
**Connects to principle:** [principle name from learning-principles.md]

**Rationale:** [why this pattern fits this project — cite the specific principle and any claims]

**Phases:**
1. [Phase name] — [brief purpose]
2. [Phase name] — [brief purpose]
...

**Design notes:**
- [Key requirement or affordance from the wiki page]
- [Key constraint to watch for in this project]

**Evidence:** [1–2 claims with tags, e.g. [[claims/slug]] [+M]]

---
```

Repeat for each approved pattern. Keep each entry under 200 words.

Confirm: *"Saved [N] patterns to projects/[name]/learning-patterns.md. Ready to run building-lessons when you are."*
