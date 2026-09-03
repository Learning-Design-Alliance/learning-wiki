#!/usr/bin/env bash
# update.sh — bring the droplet's checkout up to date with main, safely.
#
# Run on the droplet:
#     sudo -u evalrunner bash /opt/learning-wiki/deploy/update.sh
#
# or in one hop:
#     ssh root@<droplet-ip> 'sudo -u evalrunner bash /opt/learning-wiki/deploy/update.sh'
#
# This exists because the three copies of the update command in README.md had
# each gone wrong in a different way:
#
#   * one pulled `origin claude/research-scraper-test-setup-i4bh9m` — a branch
#     CLAUDE.md lists as merged and dead, and which no longer exists on the
#     remote at all, so the command now fails outright;
#   * the other two were a bare `git pull`, which updates whatever branch
#     happens to be checked out. That is precisely the failure CLAUDE.md
#     records: a run branched off `fix/crossref-citation-corrections` instead
#     of main executed every script at its pre-#45 version, produced plausible
#     results and a clean-looking diff, and nobody could see it from the PR.
#
# So this checks out main explicitly, refuses a merge that is not a
# fast-forward, and — the part a hand-typed command always skips — refuses to
# touch a dirty tree at all. CLAUDE.md is explicit that the droplet's working
# tree routinely holds real uncommitted work; a pull that stashes or resets it
# would destroy exactly the thing worth keeping.
#
# It deliberately restarts nothing. dashboard_server.py notices a changed tree
# by fingerprint and rescans on the next page load, so the dashboard is correct
# without a restart; the systemd units that do need one are per-service and
# README.md covers them where they are relevant.

set -euo pipefail

REPO="${REPO:-/opt/learning-wiki}"
cd "$REPO"

echo "==> $REPO"
echo "    on $(git rev-parse --abbrev-ref HEAD) at $(git rev-parse --short HEAD)"

if ! git diff --quiet || ! git diff --cached --quiet; then
    echo
    echo "REFUSING: the working tree has uncommitted changes." >&2
    git status --short >&2
    echo >&2
    echo "This tree is expected to hold real work. Commit it, or move it out of" >&2
    echo "the way, and re-run — nothing here will stash or discard it for you." >&2
    exit 1
fi

before="$(git rev-parse HEAD)"

git fetch --quiet origin main
git checkout --quiet main
git merge --ff-only --quiet origin/main

after="$(git rev-parse HEAD)"

if [ "$before" = "$after" ]; then
    echo "    already up to date."
    exit 0
fi

echo
echo "==> $(git rev-list --count "$before".."$after") commit(s) pulled:"
git log --oneline "$before".."$after"

echo
echo "==> scripts/ changed in this range:"
if git diff --name-only "$before".."$after" -- scripts/ deploy/ | grep . ; then
    echo
    echo "    Tooling moved. Re-read what a script does before running it —"
    echo "    and if a service uses it, restart that unit (see deploy/README.md)."
else
    echo "    (none — content only)"
fi
