#!/bin/bash
# build_site.sh — build the docs site: the curated tier with mkdocs, the long tail with
# build_longtail.py, then a Pagefind index over both (docs_hooks/two_tier.py says why).
# One script, so the deploy, preview and validate workflows cannot drift apart.
#   scripts/build_site.sh [--strict]        SKIP_SEARCH=1 leaves out the Pagefind index (validate.yml)
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf docs && mkdir -p docs
for dir in $(python3 -c "import sys; sys.path.insert(0, 'scripts'); import okf_lib; print(' '.join(okf_lib.CONTENT_FOLDERS))") branding; do
  ln -s ../$dir docs/$dir
done
ln -s ../index.md docs/index.md
ln -s ../CLAUDE.md docs/CLAUDE.md
ln -s ../evidence.md docs/evidence.md
mkdocs build ${1:-}
python3 scripts/build_longtail.py --site site
[ -n "${SKIP_SEARCH:-}" ] && exit 0
# Permalink glyphs and the collapsed metadata and evidence-code panels are not content.
python3 -m pagefind --site site --output-subdir pagefind --exclude-selectors ".headerlink" --exclude-selectors "details.info"
