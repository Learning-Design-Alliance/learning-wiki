"""
page_metadata.py — show a page's frontmatter on the rendered page.

mkdocs strips YAML frontmatter out of the rendered output entirely, so on the
docs site none of it is visible: not `status`, not who generated the page or
when, not whether a human has ever checked it, and not the `id` the
design-spec pipeline resolves the page by. The page-type banner exists
precisely because of that gap, and covers exactly one field of it.

This appends a collapsed **Page metadata** block to every content page. A
mkdocs hook rather than a plugin: `hooks:` is native config (mkdocs >= 1.4), so
this adds no dependency to requirements-docs.txt and nothing to install.

Two things it surfaces that are not simply a reprint of the YAML:

  * **the trust tier.** CLAUDE.md derives three tiers from `verified` —
    unverified / machine-confirmed / human-reviewed — and until now nothing
    rendered them. A reader could not tell whether a page had ever been
    checked by a person, which is the single most useful thing to know about
    an LLM-maintained wiki and the whole reason the field exists.
  * **`sources` as a count plus ids**, not a dumped list. Some pages carry
    thirty; printing them in full would bury the fields a reader came for,
    and the citations themselves are already in `## Key Sources` right above.
"""

from __future__ import annotations

from pathlib import Path

# index.md and log.md carry no page frontmatter worth showing (index files are
# OKF-reserved and deliberately bare), and CLAUDE.md is the schema guide
# itself.
SKIP_BASENAMES = {"index.md", "log.md", "CLAUDE.md"}

# Rendered in this order when present. Anything else the page carries is shown
# afterwards in its own order, so a field added to the schema later appears
# without this list needing an edit — a panel that silently omits a new field
# is worse than one that shows it plainly.
FIELD_ORDER = ("type", "id", "aliases", "title", "description", "status",
               "grain_size", "author", "evidence_strength")

HIDE = {"generated", "verified", "sources", "template", "hide", "search", "nav_order"}


def _trust_tier(verified) -> str:
    """unverified | machine-confirmed | human-reviewed — see CLAUDE.md."""
    if not verified:
        return "unverified — no one has confirmed this page's content"
    entries = verified if isinstance(verified, list) else [verified]
    actors = [str((e or {}).get("by", "")) for e in entries if isinstance(e, dict)]
    if any(a.startswith("human:") for a in actors):
        who = ", ".join(a for a in actors if a.startswith("human:"))
        return f"human-reviewed — checked by {who}"
    return "machine-confirmed — recorded by a tool, not a person"


def _fmt(value) -> str:
    if isinstance(value, list):
        return ", ".join(f"`{v}`" for v in value) if value else "—"
    if isinstance(value, dict):
        return ", ".join(f"{k}: `{v}`" for k, v in value.items())
    text = str(value).strip()
    return f"`{text}`" if text else "—"


def _rows(meta: dict) -> list:
    rows = []
    for key in FIELD_ORDER:
        if key in meta and meta[key] not in (None, ""):
            rows.append((key, _fmt(meta[key])))
    for key, value in meta.items():
        if key in FIELD_ORDER or key in HIDE or value in (None, ""):
            continue
        rows.append((key, _fmt(value)))

    gen = meta.get("generated")
    if isinstance(gen, dict):
        rows.append(("generated", f"by `{gen.get('by', '?')}` on `{gen.get('at', '?')}`"))
    rows.append(("trust", _trust_tier(meta.get("verified"))))

    sources = meta.get("sources") or []
    if sources:
        ids = [str(s.get("id")) for s in sources if isinstance(s, dict) and s.get("id")]
        shown = ", ".join(f"`{i}`" for i in ids[:12])
        more = f" … and {len(ids) - 12} more" if len(ids) > 12 else ""
        rows.append(("sources", f"{len(sources)} — {shown}{more}" if ids else str(len(sources))))
    return rows


# The scales are loaded from evidence-scales.json — the same file an agent
# reads to interpret the `q`/`i` now mirrored into each claim's frontmatter.
# One definition, two audiences: if the tiers change, the page and the agent
# change together, which a second copy here could not guarantee.
def _load_scales():
    """Read the whole of evidence-scales.json, not only its tier tables.

    The file already says what each letter stands for — quality, impact,
    sample — and what `?` means, in its `means` fields. The first version of
    this panel took the tiers and paraphrased the rest inline, which put a
    second wording of the same fact one directory away from the first. The
    letters are exactly the part a reader does not know, so they are the part
    that must not drift."""
    import json
    path = Path(__file__).resolve().parent.parent / "evidence-scales.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    quality = [(f"q{t['code']}", t["definition"]) for t in data["quality"]["tiers"]]
    # `i0` is labelled "negligible" and defined "negligible or unclear", so
    # the naive label + definition join reads "Negligible — Negligible or
    # unclear". Drop the label where the definition already opens with it.
    impact = []
    for tier in data["impact"]["tiers"]:
        label, definition = tier["label"], tier["definition"]
        meaning = (definition if definition.lower().startswith(label.lower())
                   else f"{label.capitalize()} — {definition}")
        impact.append((f"i{tier['code']}", meaning[0].upper() + meaning[1:]))
    return quality, impact, data


QUALITY_TIERS, IMPACT_TIERS, SCALES = _load_scales()


def _first_sentence(text: str) -> str:
    """The `means` fields carry a definition and then a qualification. The
    panel wants the definition; the qualification is in the Schema & Guide."""
    head = str(text).split(". ")[0].strip()
    return head if head.endswith(".") else head + "."


def _evidence_legend() -> str:
    """A collapsed key to `q3 i2`, placed where the bare codes appear.

    An evidence entry spells its own codes out — `q3 · quasi-experimental
    study · i2 · large effect · n=large` — so it needs no help. A subclaim
    prefix does not: it is bare, it is the first thing a reader meets under
    ## Subclaims, and across the claims corpus there are 465 quality codes and
    443 impact codes with nothing next to them saying what the numbers mean.

    The tables have always existed in CLAUDE.md, which is in the nav as
    Schema & Guide, so this is a proximity problem rather than a missing-docs
    one — hence a collapsed panel at the point of use rather than a fifth copy
    of the schema.

    Not tooltips: the codes sit inside code spans, and neither `abbr` nor
    Material's tooltips reach inside a `<code>` element."""
    q_rows = [f"    | `{code}` | {meaning} |" for code, meaning in QUALITY_TIERS]
    i_rows = [f"    | `{code}` | {meaning} |" for code, meaning in IMPACT_TIERS]
    q_means = _first_sentence(SCALES["quality"]["means"])
    i_means = _first_sentence(SCALES["impact"]["means"])
    n_means = _first_sentence(SCALES["sample"]["means"])
    unknown = SCALES["unknown"]["means"]
    return "\n".join([
        "", '??? info "Reading the evidence codes"', "",
        "    The letters are abbreviations:", "",
        f"    * **`q` — quality.** {q_means}",
        f"    * **`i` — impact.** {i_means}",
        f"    * **`n` — sample.** {n_means}", "",
        "    A subclaim is prefixed with the first two, bare: `q3 i2` means a q3 study",
        "    with an i2 effect. An evidence entry spells them out in words beside the",
        "    code and adds `n=`.", "",
        "    **`q` — evidence quality**", "",
        "    | Code | Criteria |", "    |---|---|", *q_rows, "",
        "    **`i` — impact magnitude**", "",
        "    | Code | Rough effect size |", "    |---|---|", *i_rows, "",
        f"    A `?` in place of a digit — `q?`, `i?` — {unknown[0].lower()}{unknown[1:]}", "",
        "    Strength here describes the *research*. Whether anyone has checked that this",
        "    page reports it faithfully is a separate axis — see `trust` in the page",
        "    metadata below, and the [Schema & Guide](../CLAUDE.md).", "",
    ])


def on_page_markdown(markdown: str, page, config, files) -> str:
    if page.file.src_path.split("/")[-1] in SKIP_BASENAMES:
        return markdown
    meta = page.meta or {}
    if not meta.get("type"):
        return markdown          # not a content page

    # Claim pages get the q/i key inserted right under ## Subclaims, which is
    # where the bare codes are read. Appending it at the bottom would put the
    # explanation after every use of the thing it explains.
    if meta.get("type") == "claim" and "## Subclaims" in markdown:
        head, sep, tail = markdown.partition("## Subclaims")
        markdown = head + sep + "\n" + _evidence_legend() + tail

    rows = _rows(meta)
    lines = ["", "", '??? info "Page metadata"', "", "    | Field | Value |",
             "    |---|---|"]
    lines += [f"    | `{k}` | {v} |" for k, v in rows]
    lines += ["",
              "    Frontmatter is the page's machine-readable record — see the "
              "[Schema & Guide](../CLAUDE.md).", ""]
    return markdown + "\n".join(lines)
