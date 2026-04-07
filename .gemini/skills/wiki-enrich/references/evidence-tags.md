# Wiki Evidence Tags

Embed inline in prose wherever a claim is made. The tag describes the **direction of effect on the page topic**:

| Tag | Meaning |
|-----|---------|
| `[+S]` | Supports — strong (meta-analytic / consistent experimental) |
| `[+M]` | Supports — moderate |
| `[+W]` | Supports — weak / emerging |
| `[~S]` `[~M]` `[~W]` | Contextual / mixed — depends on conditions |
| `[-S]` `[-M]` `[-W]` | Contradicts or reduces effectiveness |
| `[X]` | Contradicted / discredited |

**Direction rule:** Claims in a **Constraints** section MUST use `[-]` or `[~]`, never `[+]`. A constraint is a condition where the approach fails — the tag must reflect that direction.

**Wikilink + tag format.** Always use double brackets around the path. The correct format is:

```
[[claims/slug]] [+M]
```

NOT plain text like `claims/slug [+M]`. The double brackets are required — without them the link won't render.
