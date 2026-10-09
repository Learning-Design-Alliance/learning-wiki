"""
two_tier.py — mkdocs builds the curated tier; the long tail is rendered beside it.

The scale test of 2026-10-09 (18,800 pages) found the Material site heading past
GitHub Pages' 1 GB limit, a 20 MB lunr index, and a 3.4 MB claims listing, all
because every page went through mkdocs with the full theme. So:

- **Curated tier (mkdocs, this hook):** principles, patterns, designs, processes,
  methods, learner variables, and the canonical elements and theories
  (`canonical: true`), with the home page, evidence.md and the guide.
- **Long tail (scripts/build_longtail.py):** claims, strategies, and every element
  and theory not marked canonical, rendered as light pages at the same URLs
  (`claims/<slug>/`), plus listings paged by first letter (`claims/all/a/`).

This hook takes the long-tail pages out of mkdocs (on_files), rewrites links to them
as directory URLs (on_page_markdown), replaces the long-tail folders' generated
index.md (the claims one is 3.4 MB) with a landing page linking the letter pages,
adds a Search page for Pagefind, and marks each page's article for Pagefind to index.
`longtail()` and `listing_groups()` are shared with build_longtail.py, so both
tiers agree on which page lives where.
"""
import os
from html import escape as html_escape
import posixpath
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
LONGTAIL_ALWAYS = ("claims", "strategies")
LONGTAIL_UNLESS_CANONICAL = ("elements", "theories")
LONGTAIL_FOLDERS = LONGTAIL_ALWAYS + LONGTAIL_UNLESS_CANONICAL
PAGE_SIZE = 400
LABELS = {"claims": "Claims", "strategies": "Strategies", "elements": "Elements", "theories": "Theories"}

_FM = re.compile(r"\A---\n(.*?)\n---", re.S)
_CANON = re.compile(r"^canonical:\s*true\s*$", re.M | re.I)
_TITLE = re.compile(r"^title:\s*(.+)$", re.M)
_DESC = re.compile(r"^description:\s*(.+)$", re.M)
_cache = {}


def _scalar(m) -> str:
    if not m:
        return ""
    v = m.group(1).strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1].replace('\\"', '"') if v[0] == '"' else v[1:-1].replace("''", "'")
    return v


def _scan(root: Path = ROOT) -> dict:
    """{folder: [(slug, title, description, canonical)]} for the long-tail folders."""
    key = str(root)
    if key not in _cache:
        out = {}
        for folder in LONGTAIL_FOLDERS:
            rows = []
            for p in sorted((root / folder).glob("*.md")):
                if p.stem == "index":
                    continue
                with open(p, encoding="utf-8") as fh:
                    head = fh.read(4000)
                m = _FM.match(head)
                fm = m.group(1) if m else ""
                rows.append((p.stem, _scalar(_TITLE.search(fm)) or p.stem,
                             _scalar(_DESC.search(fm)), bool(_CANON.search(fm))))
            out[folder] = rows
        _cache[key] = out
    return _cache[key]


def longtail(root: Path = ROOT) -> set:
    """Every "folder/slug" the long-tail renderer owns."""
    out = set()
    for folder, rows in _scan(root).items():
        for slug, _, _, canonical in rows:
            if folder in LONGTAIL_ALWAYS or not canonical:
                out.add(f"{folder}/{slug}")
    return out


def _group(title: str) -> str:
    c = (re.sub(r"[^a-z0-9]", "", title.lower()) or "#")[0]
    return c if c.isalpha() else "0-9"


def listing_groups(folder: str, root: Path = ROOT) -> list:
    """[(page_key, label, [(slug, title, description)])] for a folder's letter pages:
    one page per first letter, split into pages of PAGE_SIZE ("a", "a-2", ...)."""
    groups = {}
    for slug, title, desc, _ in _scan(root)[folder]:
        groups.setdefault(_group(title), []).append((slug, title, desc))
    out = []
    for g in sorted(groups, key=lambda g: (g == "0-9", g)):
        rows = sorted(groups[g], key=lambda r: r[1].lower())
        chunks = [rows[i:i + PAGE_SIZE] for i in range(0, len(rows), PAGE_SIZE)]
        for i, chunk in enumerate(chunks):
            key = g if i == 0 else f"{g}-{i + 1}"
            label = g.upper() if len(chunks) == 1 else f"{g.upper()} {i + 1}"
            out.append((key, label, chunk))
    return out


def dir_url(target: str) -> str:
    """The directory URL of a source path: "claims/x.md" -> "claims/x/",
    "claims/index.md" -> "claims/", "index.md" -> ""."""
    stem = target[:-3] if target.endswith(".md") else target
    if stem == "index" or stem.endswith("/index"):
        stem = stem[:-5].rstrip("/")
    return "/".join(quote(s) for s in stem.split("/")) + "/" if stem else ""


def rel_url(from_url: str, to_url: str) -> str:
    """A relative href from a page's directory URL to another directory URL."""
    base = posixpath.dirname(from_url.rstrip("/") + "/x") if from_url else "."
    r = posixpath.relpath(to_url or ".", base or ".")
    return (r + "/") if not r.endswith("/") and to_url.endswith("/") else r


_LINK = re.compile(r"(\]\()(<[^>]+>|[^)\s]+(?:\([^)\s]*\)[^)\s]*)*)(\))")


def rewrite_links(markdown: str, src_path: str, page_url: str, owned: set) -> str:
    """Links to pages in `owned` ("folder/slug") become relative directory URLs."""
    src_dir = posixpath.dirname(src_path)

    def fix(m):
        dest = m.group(2)
        bare = dest[1:-1] if dest.startswith("<") else dest
        if "://" in bare or bare.startswith(("#", "mailto:")):
            return m.group(0)
        path, _, frag = bare.partition("#")
        if not path.endswith(".md"):
            return m.group(0)
        from urllib.parse import unquote
        target = posixpath.normpath(posixpath.join(src_dir, unquote(path)))
        if target[:-3] not in owned:
            return m.group(0)
        href = rel_url(page_url, dir_url(target)) + (f"#{frag}" if frag else "")
        return f"{m.group(1)}{href}{m.group(3)}"
    return _LINK.sub(fix, markdown)


def landing_markdown(folder: str, page_url: str, root: Path = ROOT) -> str:
    """The site's page for a long-tail folder, in place of its generated index.md."""
    rows = _scan(root)[folder]
    label = LABELS[folder]
    lines = [f"# {label}", "",
             f"{len(rows):,} {label.lower()}. Browse them by first letter, or use [Search](../search/).", ""]
    lines.append(" · ".join(f"[{lab}](all/{key}/)" for key, lab, _ in listing_groups(folder, root)))
    canon = [(s, t, d) for s, t, d, c in rows if c and folder in LONGTAIL_UNLESS_CANONICAL]
    if canon:
        lines += ["", f"## Canonical {label.lower()}", "",
                  f"The {len(canon)} pages other {label.lower()} attach to.", ""]
        lines += [f"* [{t}]({quote(s)}/)" + (f" - {d[:160]}" if d else "") for s, t, d in sorted(canon, key=lambda r: r[1].lower())]
    lines += ["", "The full machine-readable listing is this folder's "
              f"[`index.md` on GitHub](https://github.com/Learning-Design-Alliance/learning-wiki/blob/main/{folder}/index.md)."]
    return "\n".join(lines) + "\n"


SEARCH_PAGE = """# Search

<link href="../pagefind/pagefind-ui.css" rel="stylesheet">
<div id="main-pages" hidden>
<p><strong>Main pages</strong></p>
<ol id="main-pages-list"></ol>
<p><strong>All results</strong></p>
</div>
<div id="wiki-search"></div>
<script src="../pagefind/pagefind-ui.js"></script>
<script type="module">
  // Long pages are not penalised and repeated words count for less, so a topic's
  // main page is not buried under claims that repeat its words more densely.
  const ranking = { pageLength: 0, termFrequency: 0.3 };
  const pf = await import("../pagefind/pagefind.js");
  await pf.options({ ranking });
  const box = document.getElementById("main-pages");
  const list = document.getElementById("main-pages-list");
  const esc = s => String(s).replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"})[c]);
  let seq = 0;
  // The canonical pages first, then the rest of the curated tier (principles, patterns,
  // designs, products, methods, canonical elements and theories), above the full results.
  async function mainPages(term) {
    const n = ++seq;
    if (!term || term.trim().length < 2) { box.hidden = true; return; }
    const canon = await pf.search(term, { filters: { tier: "canonical" } });
    const rest = await pf.search(term, { filters: { tier: "curated" } });
    const pool = [...(canon ? canon.results.slice(0, 12).map(x => [x, 0]) : []),
                  ...(rest ? rest.results.slice(0, 12).map(x => [x, 1]) : [])];
    const rows = await Promise.all(pool.map(async ([x, tier], i) => ({ d: await x.data(), tier, i })));
    // A page named by the query is the main page for it: rank by how many query words
    // the title carries (by their first five letters, so "practice" finds "practise"),
    // then the shorter title, then canonical over curated, then Pagefind's own order.
    const words = term.toLowerCase().match(/[a-z0-9]+/g) || [];
    for (const r of rows) {
      const t = ((r.d.meta.title || "") + " " + (r.d.meta.aliases || "")).toLowerCase();
      r.cover = words.filter(w => t.includes(w.slice(0, 5))).length;
      r.len = ((r.d.meta.title || "").toLowerCase().match(/[a-z0-9]+/g) || []).length;
    }
    rows.sort((a, b) => b.cover - a.cover || a.len - b.len || a.tier - b.tier || a.i - b.i);
    const seen = new Set();
    const top = rows.filter(r => !seen.has(r.d.url) && seen.add(r.d.url)).slice(0, 5).map(r => r.d);
    if (n !== seq) return;
    list.innerHTML = top.map(d => `<li><a href="${esc(d.url)}">${esc(d.meta.title)}</a>`
      + ` <small>${esc(((d.filters || {}).kind || [""])[0])}</small></li>`).join("");
    box.hidden = !top.length;
  }
  const ui = new PagefindUI({ element: "#wiki-search", showSubResults: false, showImages: false,
                              openFilters: ["kind"], ranking,
                              processTerm: t => { mainPages(t); return t; } });
  // `tier` is the Main pages list's own filter, not one for readers: hide its block.
  new MutationObserver(() => {
    // Main pages sits between the search box and the full results.
    const drawer = document.querySelector("#wiki-search .pagefind-ui__drawer");
    if (drawer && box.nextElementSibling !== drawer) { drawer.before(box); }
    for (const el of document.querySelectorAll("#wiki-search .pagefind-ui__filter-name")) {
      if (el.textContent.trim().toLowerCase() === "tier") {
        const block = el.closest(".pagefind-ui__filter-block") || el.closest("details");
        if (block) block.style.display = "none";
      }
    }
  }).observe(document.getElementById("wiki-search"), { childList: true, subtree: true });
  const q = new URLSearchParams(window.location.search).get("q");
  if (q) { ui.triggerSearch(q); }
</script>

Search covers every page in the wiki, both the curated pages and the claims,
strategies and other long-tail pages. Agents should use the MCP server's
`search` tool (`scripts/mcp_server.py`) instead.
"""

# --------------------------------------------------------------------- hooks

_owned = set()


def on_files(files, config):
    global _owned
    _owned = longtail(ROOT)
    for f in list(files):
        if f.src_uri.endswith(".md") and f.src_uri[:-3] in _owned:
            files.remove(f)
    from mkdocs.structure.files import File
    files.append(File.generated(config, "search.md", content=SEARCH_PAGE))
    return files


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    folder = src.split("/")[0]
    if folder in LONGTAIL_FOLDERS and src == f"{folder}/index.md":
        return landing_markdown(folder, page.url)
    return rewrite_links(markdown, src, page.url, _owned)


def pagefind_attrs(kind: str) -> str:
    """The article's Pagefind attributes: index it, and file it under its kind so a
    search can be narrowed to principles, claims, ... A curated-tier content page also
    carries TIER_MARK, which the search page's Main pages list searches on its own."""
    label = KIND_LABELS.get(kind, "")
    return " data-pagefind-body" + (f' data-pagefind-filter="kind:{label}"' if label else "")


# Pagefind reads one filter per attribute ("kind:Principle, tier:curated" became one kind
# value), so the tier rides on an empty element of its own inside the article.
# `canonical` for the pages the ledger settles against (canonical: true), `curated` for the
# rest of the curated tier; the Main pages list searches the canonical ones first.
TIER_MARK = '<span data-pagefind-filter="tier:{tier}"></span>'



KIND_LABELS = {"principle": "Principle", "element": "Element", "pattern": "Pattern", "design": "Design",
               "product": "Product or programme", "research-method": "Research method",
               "strategy": "Strategy", "process": "Design process", "method": "Design method",
               "theory": "Theory", "learner-variable": "Learner variable", "claim": "Claim"}


HEADER_SEARCH = ('<form class="lt-header-search" action="{rel}search/" role="search" '
                 'style="margin:0 .6rem;align-self:center">'
                 '<input name="q" type="search" placeholder="Search" aria-label="Search the wiki" '
                 'style="font:inherit;font-size:.7rem;padding:.25rem .5rem;border-radius:.2rem;border:0;'
                 'width:11rem;max-width:30vw;background:var(--md-default-bg-color);'
                 'color:var(--md-default-fg-color)"></form>')


def on_post_page(output, page, config):
    kind = str((page.meta or {}).get("type") or "")
    meta = page.meta or {}
    canonical = str(meta.get("canonical", "")).lower() == "true"
    mark = TIER_MARK.format(tier="canonical" if canonical else "curated") if kind in KIND_LABELS else ""
    # A page's former slugs name it too ("spaced-practice" is Spaced Learning), so the
    # search page's Main pages ranking reads them beside the title.
    aliases = meta.get("aliases") or []
    if mark and isinstance(aliases, list) and aliases:
        words = " ".join(str(a).replace("-", " ").replace("_", " ") for a in aliases)
        mark += f'<span data-pagefind-meta="aliases:{html_escape(words)}"></span>'
    if page.file.src_uri != "search.md":       # the search page itself is not a result
        output = output.replace('<article class="md-content__inner md-typeset">',
                                f'<article class="md-content__inner md-typeset"{pagefind_attrs(kind)}>{mark}', 1)
    # A search box in the header, sending the reader to the search page (?q=), since
    # the theme's own box went with its lunr search.
    rel = "../" * page.url.count("/")
    return output.replace('<div class="md-header__source">',
                          HEADER_SEARCH.format(rel=rel) + '<div class="md-header__source">', 1)
