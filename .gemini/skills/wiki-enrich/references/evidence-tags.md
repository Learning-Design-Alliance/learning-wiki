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

**Cross-link + tag format.** Always use a standard markdown link to the bundle-relative path. The correct format is:

```
[Claim statement](/claims/slug.md) [+M]
```

NOT plain text like `claims/slug [+M]`. The markdown link is required — without it the reference won't resolve.
