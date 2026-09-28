# Design decisions on a pattern, element or principle page — task for an in-session agent

Usage scenarios showed that the wiki's claims give precise, checkable advice, but that the design
pages do not turn them into decisions: `elements/practice` (915 inbound links) cited 6 claims and
`elements/feedback` 4, while the wiki holds dozens of claims on each, including meta-analyses. A course
designer reading the page learns what the component is, not how to set it up. This section is that
missing step.

## What to add

A `## Design Decisions` section, placed immediately before the page's first `## Related …`,
`## Examples` or `## Key Sources` heading (whichever comes first), in this shape:

```markdown
## Design Decisions
<!-- Decision section (2026-09-30 pilot): drafted from the linked claim pages only; every choice
     cites the claims that settle it, with markers capped by each claim's recorded evidence. -->

### <The decision, as the question a designer asks: "When should feedback come?">
- **Default:** <the choice the evidence favours, with any parameter it gives> — [claim title](../claims/<slug>.md) [+M]
- **Changes when:** <condition> → <different choice> — [claim](../claims/<slug>.md) [~W]
- **Tested with:** <the populations and settings behind these claims, in a few words>
- **Not settled:** <what the evidence here does not decide, or "no wiki evidence on X">
```

- **3–7 decisions per page**, each one a choice a designer actually makes with this component:
  timing, dose and schedule, form or type, who delivers it, sequence and fading, what it is combined
  with, and when not to use it. Pick the decisions the evidence can speak to; name the important ones it
  cannot under **Not settled** rather than dropping them.
- **Every Default and Changes-when line cites at least one wiki claim page.** No studies from memory, no
  citation that is not a claim page, no advice the cited claims do not state. If no claim speaks to a
  choice, say so under Not settled.
- **Read every claim page before citing it**, including its Evidence and Discussion: a claim's title can
  overstate, and its Discussion often says where it stops applying. Quote numbers (d, g, k, days) only as
  the claim page gives them.
- **Markers**: polarity is how the claim bears on this choice (`+` supports it, `~` depends on
  conditions, `-` against). Strength is capped by the claim's header line
  (`grep -m1 '^> \*\*Evidence' claims/<slug>.md`): **S** only if it shows 2 or more studies and a `q3`
  or higher; **M** if at least 1 study and a `q2` or higher; otherwise **W**.
- **Find claims** with `python3 scripts/mcp_server.py --call search '{"query": "...", "kind": "claim", "limit": 15}'`
  (several phrasings), `--call backlinks '{"id": "<kind>/<slug>"}'` on the page and on its neighbours,
  and `grep -il` over `claims/`. Prefer claims resting on syntheses (`quant-synthesis`, q3–q4) and say
  when a choice rests on one small study.
- Then add every claim you cited to the page's existing `### Claims` (or `## Claims`) list if it is not
  already there, as `- [title](../claims/<slug>.md) [marker]`, creating the list under the
  Implications/Design Implications section if the page has none.

## Rules

- Edit only the pages you are given. Change nothing else on them except the two additions above.
  Never edit a claim page, an index file, or git; never add `verified:`.
- Other agents are editing other design pages at the same time.
- Run `python3 scripts/lint.py` at the end (0 on your pages).
- Report per page: the decisions written, the claims cited (slug, marker, and what capped it), the
  important decisions you could not ground, and any claim whose page contradicted its own title.
