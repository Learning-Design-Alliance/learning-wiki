---
name: defining-learning-principles
description: Identifies and selects learning design principles for a project by searching the ld-wiki principles library. Accepts user-provided principles or context; searches and reads wiki pages; evaluates coverage across motivation, cognition, social, and assessment dimensions; presents candidates for user approval; and writes the result to projects/[name]/learning-principles.md.
---

# Defining Learning Principles

Produces **`projects/[project-name]/learning-principles.md`** — the set of named, cited learning science commitments for this project. The user approves what goes in. This file is consumed by `building-learning-patterns`.

---

## Step 0 — Gather project context

Ask the user for:
- **Project name** (used for the output path)
- **Learner profile**: who are the learners? (age, background, prior knowledge, special factors)
- **Domain and topic**: what is being learned?
- **Delivery format**: self-paced / blended / live; sync or async; device
- **Learning goals** (if known): what should learners be able to do?

If `projects/[name]/learning-goals.md` exists, read it.

---

## Step 1 — Accept user-provided principles

Ask: *"Do you have any principles, research papers, or design commitments you'd like to start with? Paste them in or share the files."*

Accept any form: named principles with or without citations, research abstracts, "we believe" statements, or nothing (proceed to Step 2).

---

## Step 2 — Search the wiki

Read `index.md` to get the full list of principle pages. Then:

1. Identify 6–10 keywords from the project context (domain, learner profile, delivery format, learning goals).
2. Grep `principles/` for pages matching those keywords — search page titles, descriptions, and Target Learners sections.
3. Read the 10–15 most relevant principle pages. For each, focus on:
   - `## Description` — what the principle recommends
   - `### Target Learners` — who it applies to
   - `### Target Learning Objectives` — what goals it supports
   - `### Context > Constraints` — when it fails or doesn't apply
   - `### Claims` — linked claims with evidence tags (use these for the Evidence field)
   - `## Key Sources` — citations to carry forward

Organize candidates by dimension:

| Dimension | Covers |
|---|---|
| Motivation | Relevance, autonomy, value, belonging, engagement |
| Cognition | Load, practice, retrieval, schema, transfer, feedback |
| Social | Collaboration, peer learning, discussion, community |
| Assessment | Formative feedback, self-monitoring, mastery evidence |

Note which dimensions the user's submitted material already covers and which are thin.

---

## Step 3 — Select and normalize candidates

For each candidate (user-submitted + wiki finds), normalize to this schema:

```
Name: [principle name — use wiki page title or user's name]
Wiki: [Title](/principles/slug.md)  ← omit if not from wiki
Category: [motivation | cognition | social | assessment]
Evidence: [strong | moderate | emerging — infer from claim tags: [+S]/[+M] → strong/moderate; [+W] → emerging]
Claim: [one sentence — what this principle asserts about learning]
Justification: [why this principle matters for THIS project's specific learner profile and domain]
Application: [one concrete instructional implication]
Citation: [from the page's ## Key Sources, or user-provided; flag as "not provided" if absent]
```

Apply selection filters before presenting:
- Match `### Target Learners` to the project's learner profile — exclude poor fits
- Match `### Target Learning Objectives` to the project's goals — exclude off-topic principles
- Check `### Context > Constraints` — exclude principles that contradict the delivery format or learner level
- Aim for 5–8 principles total, spanning all four dimensions

---

## Step 4 — Present candidates for approval

Present all candidates as a numbered list:

> "Here are the principles I've identified. Which would you like to include? You can say 'all', list numbers, or ask me to adjust any of them."

Show each with: name, category, one-sentence claim, and citation.

Wait for the user's selection before writing output. If a selection leaves a dimension uncovered, note the gap and ask whether to replace it.

---

## Step 5 — Write output

Write approved principles to `projects/[project-name]/learning-principles.md`:

```markdown
# Learning Principles — [Project Name]

*[Date]. Approved by user.*

## Coverage
| Dimension | Principles |
|---|---|
| Motivation | [names] |
| Cognition | [names] |
| Social | [names] |
| Assessment | [names] |

---

## [Principle Name]

**Category:** [motivation | cognition | social | assessment]
**Evidence:** [strong | moderate | emerging]
**Wiki:** [Title](/principles/slug.md)

**Claim:** [one sentence]

**Justification:** [why it matters for this project]

**Application:** [one concrete instructional implication]

**Citation:** [APA citation]

---
```

Repeat the entry block for each approved principle.

Confirm: *"Saved [N] principles to projects/[name]/learning-principles.md. Ready to run building-learning-patterns when you are."*
