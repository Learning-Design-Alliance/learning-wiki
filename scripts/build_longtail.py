#!/usr/bin/env python3
"""
build_longtail.py — render the wiki's long tail into a built mkdocs site.

mkdocs renders the curated tier only (docs_hooks/two_tier.py says which pages are
which and why). This renders the rest, claims, strategies and the elements and
theories not marked canonical, at the URLs mkdocs would have given them
(`site/claims/<slug>/index.html`), with the same markdown extensions and the same
metadata panel (docs_hooks/page_metadata.py), but a light page: Material's
stylesheet and a one-line header instead of the full theme and its navigation,
which was most of every page's weight. It also writes each long-tail folder's
letter pages (`site/claims/all/a/`), which the folder's landing page links.

Run after `mkdocs build`, before Pagefind:

    python3 scripts/build_longtail.py [--site site] [--workers 8]
"""
import argparse
import html
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "docs_hooks"))
sys.path.insert(0, str(ROOT / "scripts"))
import two_tier  # noqa: E402

EXTENSIONS = ["admonition", "attr_list", "md_in_html", "footnotes", "pymdownx.details",
              "pymdownx.superfences", "pymdownx.highlight", "pymdownx.tasklist", "tables", "toc"]
EXT_CONFIG = {"pymdownx.tasklist": {"custom_checkbox": True}, "toc": {"permalink": True}}

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} - Learning Design Wiki</title>
<link rel="icon" href="{rel}branding/lazuli-favicon.svg">
{css}
<style>
.lt-header{{background:var(--md-primary-fg-color);color:var(--md-primary-bg-color);padding:.6rem 1rem;font-size:.8rem}}
.lt-header a{{color:inherit;text-decoration:none;margin-right:.6rem}}
.lt-header a:hover{{text-decoration:underline}}
.lt-header form{{display:inline;float:right}}
.lt-header input{{font:inherit;padding:.1rem .4rem;border-radius:.2rem;border:0}}
.lt-main{{max-width:52rem;margin:0 auto;padding:1rem 1.2rem 3rem}}
</style>
</head>
<body dir="ltr" data-md-color-scheme="default" data-md-color-primary="custom" data-md-color-accent="custom">
<header class="lt-header">
<a href="{rel}"><strong>Learning Design Wiki</strong></a>
<a href="{rel}{folder}/">{label}</a>
<form action="{rel}search/"><input name="q" placeholder="Search" aria-label="Search"></form>
</header>
<main class="lt-main"><article class="md-typeset"{pagefind}>
{body}
</article></main>
</body>
</html>
"""

_state = {}


def _init(site: str, css_paths: list, owned: set) -> None:
    import markdown
    import yaml
    import page_metadata
    page_metadata.LEGEND_URL = "../evidence-codes/"
    _state.update(site=Path(site), css=css_paths, owned=owned, yaml=yaml, pm=page_metadata,
                  md=markdown.Markdown(extensions=EXTENSIONS, extension_configs=EXT_CONFIG))


def _css(rel: str) -> str:
    return "\n".join(f'<link rel="stylesheet" href="{rel}{c}">' for c in _state["css"])


def _write(url: str, title: str, folder: str, body_html: str, index: bool, kind: str = "") -> None:
    rel = "../" * url.rstrip("/").count("/") + "../" if url else ""
    out = _state["site"] / url / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEMPLATE.format(title=html.escape(title), rel=rel, css=_css(rel), folder=folder,
                                   label=two_tier.LABELS.get(folder, folder.title()), body=body_html,
                                   pagefind=two_tier.pagefind_attrs(kind) if index else ""), encoding="utf-8")


class _Page:
    def __init__(self, src, meta):
        self.file = type("F", (), {"src_path": src, "src_uri": src})()
        self.meta = meta


def render_page(key: str) -> None:
    from urllib.parse import unquote
    folder, slug = key.split("/", 1)
    text = (ROOT / f"{key}.md").read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end > 0:
            try:
                meta = _state["yaml"].safe_load(text[4:end]) or {}
            except Exception:
                meta = {}
            body = text[end + 4:].lstrip("\n")
    src = f"{key}.md"
    url = unquote(two_tier.dir_url(src))
    body = _state["pm"].on_page_markdown(body, _Page(src, meta), None, None)
    # Every .md link becomes a directory URL: the long tail's own pages and the
    # curated pages mkdocs wrote are both at folder/slug/.
    body = two_tier.rewrite_links(body, src, two_tier.dir_url(src), _AnyPage())
    md = _state["md"]
    md.reset()
    title = str(meta.get("title") or slug)
    _write(url, title, folder, md.convert(body), True, str(meta.get("type") or ""))


class _AnyPage:
    """A set that contains every page: rewrite_links then rewrites every .md link."""
    def __contains__(self, item):
        return True


def render_listings(folder: str) -> int:
    groups = two_tier.listing_groups(folder)
    nav = " · ".join(f'<a href="../{k}/">{html.escape(lab)}</a>' for k, lab, _ in groups)
    for key, label, rows in groups:
        items = "\n".join(
            f'<li><a href="../../{two_tier.quote(s)}/">{html.escape(t)}</a>'
            + (f" - {html.escape(d[:200])}" if d else "") + "</li>" for s, t, d in rows)
        body = (f"<h1>{two_tier.LABELS[folder]}: {html.escape(label)}</h1>\n<p>{nav}</p>\n"
                f"<ul>\n{items}\n</ul>")
        _write(f"{folder}/all/{key}/", f"{two_tier.LABELS[folder]}: {label}", folder, body, False)
    return len(groups)


def render_legend() -> None:
    """The one shared copy of the claim pages' evidence-code legend, open."""
    import textwrap
    pm = _state["pm"]
    saved, pm.LEGEND_URL = pm.LEGEND_URL, None
    text = pm._evidence_legend(None)
    pm.LEGEND_URL = saved
    body = textwrap.dedent(text.split('"Reading the evidence codes"', 1)[1])
    body = "# Reading the evidence codes\n" + body.replace("    **This claim:** no standardized effect", "")
    body = "\n".join(l for l in body.split("\n") if not l.startswith("**This claim:**"))
    body = two_tier.rewrite_links(body, "claims/evidence-codes.md", "claims/evidence-codes/", _AnyPage())
    md = _state["md"]
    md.reset()
    _write("claims/evidence-codes/", "Reading the evidence codes", "claims", md.convert(body), False)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", default=str(ROOT / "site"))
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 4)
    args = ap.parse_args()
    site = Path(args.site)
    css = sorted(str(p.relative_to(site)) for p in (site / "assets" / "stylesheets").glob("main.*.min.css"))
    css += sorted(str(p.relative_to(site)) for p in (site / "assets" / "stylesheets").glob("palette.*.min.css"))
    css += ["branding/lazuli-theme.css"]
    if not css[0].startswith("assets/"):
        sys.exit(f"no Material stylesheet in {site}/assets: run mkdocs build first")
    owned = sorted(two_tier.longtail(ROOT))
    _init(str(site), css, set(owned))
    assert "claims/evidence-codes" not in owned, "a claim's slug collides with the legend page"
    render_legend()
    for folder in two_tier.LONGTAIL_FOLDERS:
        print(f"{folder}: {render_listings(folder)} listing page(s)")
    with ProcessPoolExecutor(args.workers, initializer=_init, initargs=(str(site), css, set(owned))) as ex:
        list(ex.map(render_page, owned, chunksize=200))
    print(f"rendered {len(owned)} long-tail page(s) into {site}")


if __name__ == "__main__":
    main()
