#!/usr/bin/env python3
"""
mint_release_doi.py — a DOI for an LDA research release, reserved before the
release is frozen and published after.

A release version is an immutable file, and a DOI is normally minted once a
work is published, which would mean editing a frozen file to add it. So the
order is reversed: RESERVE a DOI (Zenodo pre-reserves one per deposition),
write it into the release file as `release.doi` / `release.doi_registrar`,
merge, and only then PUBLISH the deposit, which is when the DOI starts to
resolve. The string never changes; only its state at the registrar does, and
that is looked up rather than stored.

    python3 scripts/mint_release_doi.py --release <id> --version <v> --metadata
        # what would be deposited, offline — read this first

    python3 scripts/mint_release_doi.py --release <id> --version <v> --reserve [--sandbox]
        # creates an unpublished Zenodo deposition with a reserved DOI and prints
        # the two lines to add to the release file. Reversible: an unpublished
        # deposition can be deleted.

    python3 scripts/mint_release_doi.py --release <id> --version <v> --publish \\
        --deposition <n> --by human:<id> --yes [--sandbox]
        # uploads the release file and publishes. IRREVERSIBLE: a published
        # Zenodo record cannot be deleted, and the DOI resolves from then on.

Token: ZENODO_TOKEN (or ZENODO_SANDBOX_TOKEN with --sandbox), scopes
deposit:write and deposit:actions. Try the whole flow on the sandbox first:
sandbox DOIs are 10.5072-style test DOIs that never resolve.

What it refuses, each for a reason:
- a release that fails any research-layer check. The layer's publication gate
  (the protocol must permit research-publication) is the check that matters
  most here, and it is not re-implemented: the layer's own validator runs.
- a release whose provenance.source_type is not `research`. A DOI is the badge
  that makes a record read as real.
- anything carrying the embargo marker (see check_embargo.py).
- publishing without a `human:` actor and --yes. An agent may reserve a DOI and
  prepare a deposit; making a work public under a permanent identifier is a
  person's decision, the same rule that keeps an agent from writing a
  verified: entry or a citation authority.

Nothing is published today, on purpose. See research/PUBLISHING.md.
"""

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_embargo
import research_lib as rl

ZENODO = "https://zenodo.org/api"
ZENODO_SANDBOX = "https://sandbox.zenodo.org/api"


class Refusal(Exception):
    pass


def load_release(rid: str, version: str) -> tuple[Path, dict]:
    path = rl.RELEASE_DIR / rid / f"{version}.yaml"
    if not path.is_file():
        raise Refusal(f"no release file at {path.relative_to(rl.WIKI_ROOT)}")
    import yaml
    return path, yaml.safe_load(path.read_text(encoding="utf-8"))


def gate(path: Path, rec: dict, rid: str, version: str, *, allow_doi: bool) -> None:
    """Everything that must hold before any call leaves this machine."""
    text = path.read_text(encoding="utf-8")
    if check_embargo.MARKER in text:
        raise Refusal("the release file carries the embargo marker; it stays in the private "
                      "research repo until the embargo lifts")
    source_type = (rec.get("provenance") or {}).get("source_type")
    if source_type != "research":
        raise Refusal(f"provenance.source_type is {source_type!r}; only a research release "
                      f"gets a DOI")
    prefix = f"releases/{rid}/{version}"
    problems = [i for i in rl.validate_all() if i.startswith(prefix)]
    if problems:
        raise Refusal("the release fails the research layer's own checks:\n  "
                      + "\n  ".join(problems[:10]))
    doi = (rec.get("release") or {}).get("doi")
    if doi and not allow_doi:
        raise Refusal(f"release.doi is already {doi!r}; one version, one DOI")
    if not doi and allow_doi:
        raise Refusal("release.doi is not set: reserve one with --reserve, write it into the "
                      "release file, and merge that before publishing")


def deposit_metadata(rec: dict, rid: str, version: str) -> dict:
    """Zenodo deposition metadata, built only from what the release states."""
    r = rec.get("release") or {}
    authors = (rec.get("provenance") or {}).get("authors") or []
    creators = []
    for a in authors:
        if not isinstance(a, dict):
            continue
        if not a.get("name"):
            raise Refusal(f"provenance.authors entry {a.get('id')!r} has no `name`; a DOI "
                          f"record names its creators, and an id is not a name")
        c = {"name": a["name"]}
        if a.get("affiliation"):
            c["affiliation"] = a["affiliation"]
        if a.get("orcid"):
            c["orcid"] = a["orcid"]
        creators.append(c)
    if not creators:
        raise Refusal("the release names no authors")

    def para(s):
        return " ".join(str(s or "").split())

    description = (f"<p><b>Question.</b> {para(r.get('question'))}</p>"
                   f"<p><b>Interpretation.</b> {para(rec.get('interpretation'))}</p>"
                   "<p><b>Limitations.</b></p><ul>"
                   + "".join(f"<li>{para(x)}</li>" for x in rec.get("limitations") or [])
                   + f"</ul><p>Learning Design Alliance research release {rid} {version}.</p>")
    related = []
    for d in rec.get("datasets") or []:
        loc = (d or {}).get("location") or {}
        if loc.get("kind") == "doi" and loc.get("ref"):
            related.append({"identifier": loc["ref"], "relation": "references",
                            "scheme": "doi"})
    if r.get("supersedes"):
        related.append({"identifier": f"{rid}@{r['supersedes']}", "relation": "isNewVersionOf",
                        "scheme": "other"})
    meta = {
        "title": para(r.get("title")),
        "upload_type": "publication",
        "publication_type": "report",
        "description": description,
        "creators": creators,
        "publication_date": str(r.get("released_at")),
        "version": version,
        "notes": f"Funding: {para(rec.get('funding'))} Conflicts: {para(rec.get('conflicts'))}",
    }
    if related:
        meta["related_identifiers"] = related
    return meta


class Zenodo:
    """The two write calls and one read, behind one small surface."""

    def __init__(self, sandbox: bool, token: str | None = None, session=None):
        self.base = ZENODO_SANDBOX if sandbox else ZENODO
        var = "ZENODO_SANDBOX_TOKEN" if sandbox else "ZENODO_TOKEN"
        self.token = token or os.environ.get(var)
        if not self.token:
            raise Refusal(f"{var} is not set")
        if session is None:
            import requests
            session = requests.Session()
        self.s = session

    def _call(self, method, url, **kw):
        kw.setdefault("headers", {})["Authorization"] = f"Bearer {self.token}"
        resp = self.s.request(method, url, timeout=60, **kw)
        if resp.status_code >= 400:
            raise Refusal(f"Zenodo {method} {url} -> {resp.status_code}: {resp.text[:300]}")
        return resp.json() if resp.content else {}

    def reserve(self, meta: dict) -> tuple[int, str]:
        body = {"metadata": {**meta, "prereserve_doi": True}}
        dep = self._call("POST", f"{self.base}/deposit/depositions", json=body)
        doi = ((dep.get("metadata") or {}).get("prereserve_doi") or {}).get("doi")
        if not doi:
            raise Refusal(f"Zenodo created deposition {dep.get('id')} but reserved no DOI")
        return dep["id"], doi

    def get(self, dep_id: int) -> dict:
        return self._call("GET", f"{self.base}/deposit/depositions/{dep_id}")

    def upload(self, dep: dict, path: Path, name: str) -> None:
        bucket = (dep.get("links") or {}).get("bucket")
        if not bucket:
            raise Refusal("the deposition has no file bucket")
        with path.open("rb") as fh:
            self._call("PUT", f"{bucket}/{name}", data=fh)

    def publish(self, dep_id: int) -> dict:
        return self._call("POST", f"{self.base}/deposit/depositions/{dep_id}/actions/publish")


def main(argv=None, client=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--release", required=True)
    ap.add_argument("--version", required=True)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--metadata", action="store_true", help="print the deposit metadata, offline")
    mode.add_argument("--reserve", action="store_true", help="create a deposition and reserve a DOI")
    mode.add_argument("--publish", action="store_true", help="upload and publish (irreversible)")
    ap.add_argument("--deposition", type=int, help="the deposition --reserve created")
    ap.add_argument("--by", help="human:<id> — required to publish")
    ap.add_argument("--yes", action="store_true", help="confirm publishing")
    ap.add_argument("--sandbox", action="store_true", help="use sandbox.zenodo.org")
    args = ap.parse_args(argv)

    try:
        path, rec = load_release(args.release, args.version)
        if args.metadata:
            print(json.dumps(deposit_metadata(rec, args.release, args.version), indent=2,
                             ensure_ascii=False))
            return 0
        if args.reserve:
            gate(path, rec, args.release, args.version, allow_doi=False)
            meta = deposit_metadata(rec, args.release, args.version)
            z = client or Zenodo(args.sandbox)
            dep_id, doi = z.reserve(meta)
            print(f"Reserved {doi} on deposition {dep_id} (unpublished, so still deletable).\n"
                  f"Add to the `release:` block of {path.relative_to(rl.WIKI_ROOT)}, then merge:\n\n"
                  f"  doi: {doi}\n  doi_registrar: zenodo\n\n"
                  f"Publish afterwards with --publish --deposition {dep_id} --by human:<id> --yes")
            return 0
        # publish
        if not (args.by or "").startswith("human:"):
            raise Refusal("publishing needs --by human:<id>: making a work public under a "
                          "permanent identifier is a person's decision, not an agent's")
        if not args.yes:
            raise Refusal("publishing is irreversible (a published Zenodo record cannot be "
                          "deleted); pass --yes to confirm")
        if args.deposition is None:
            raise Refusal("--publish needs --deposition <id>")
        gate(path, rec, args.release, args.version, allow_doi=True)
        doi = rec["release"]["doi"]
        if rec["release"].get("doi_registrar") != "zenodo":
            raise Refusal("release.doi_registrar is not zenodo; this script publishes to Zenodo only")
        z = client or Zenodo(args.sandbox)
        dep = z.get(args.deposition)
        reserved = ((dep.get("metadata") or {}).get("prereserve_doi") or {}).get("doi")
        if reserved != doi:
            raise Refusal(f"deposition {args.deposition} reserved {reserved!r}, but the release "
                          f"file says {doi!r}; refusing to publish the wrong record")
        z.upload(dep, path, f"{args.release}-{args.version}.yaml")
        out = z.publish(args.deposition)
        print(f"Published {out.get('doi') or doi} ({args.by}): "
              f"{(out.get('links') or {}).get('record_html') or ''}")
        return 0
    except Refusal as exc:
        print(f"refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
