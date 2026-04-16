#!/bin/bash
# serve.sh — Sync wiki content into Quartz and start the local dev server.
#
# Usage:
#   bash scripts/serve.sh         # full sync + serve with incremental auto-sync
#   bash scripts/serve.sh --sync  # one-shot full sync only, no server
#
# Requires:
#   - /Users/davidporcaro/ld-wiki-site (Quartz install)
#   - Node 22+, npm
#   - fswatch (brew install fswatch) for instant sync; falls back to 3s polling

set -e

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh"
nvm use 22 --silent 2>/dev/null || true

WIKI_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
QUARTZ_ROOT="/Users/davidporcaro/ld-wiki-site"
CONTENT_DIR="$QUARTZ_ROOT/content"

# ── Initial full sync ──────────────────────────────────────────────────────────

echo "Syncing wiki → $CONTENT_DIR ..."
find "$CONTENT_DIR" -mindepth 1 -delete 2>/dev/null || true
mkdir -p "$CONTENT_DIR"
rsync -a --include="*/" --include="*.md" --exclude="*" "$WIKI_ROOT/" "$CONTENT_DIR/"
rm -rf "$CONTENT_DIR/scripts"
echo "  [$(date +%H:%M:%S)] Synced $(find "$CONTENT_DIR" -name '*.md' | wc -l | tr -d ' ') pages"

if [[ "$1" == "--sync" ]]; then
  echo "Sync complete. Run 'bash scripts/serve.sh' to start the server."
  exit 0
fi

# ── Incremental background watcher ────────────────────────────────────────────
# Copies only the changed file — Quartz rebuilds just that page (~1s vs ~60s)

WATCHER_PID=""

cleanup() {
  echo ""
  echo "Stopping..."
  [[ -n "$WATCHER_PID" ]] && kill "$WATCHER_PID" 2>/dev/null
  exit 0
}
trap cleanup INT TERM

sync_one() {
  local changed_file="$1"
  local rel="${changed_file#$WIKI_ROOT/}"
  [[ "$rel" == scripts/* ]] && return
  local dest="$CONTENT_DIR/$rel"
  mkdir -p "$(dirname "$dest")"
  cp "$changed_file" "$dest"
  echo "  [$(date +%H:%M:%S)] Updated: $rel"
}

if command -v fswatch &>/dev/null; then
  echo "Watching for changes (fswatch — instant sync)..."
  fswatch -0 --include="\.md$" --recursive "$WIKI_ROOT" | \
    while IFS= read -r -d "" changed_file; do
      sync_one "$changed_file"
    done &
  WATCHER_PID=$!
else
  echo "fswatch not found — polling every 3s (brew install fswatch for instant sync)"
  (
    sentinel="$CONTENT_DIR/.last_sync"
    touch "$sentinel"
    while true; do
      sleep 3
      while IFS= read -r -d "" changed_file; do
        sync_one "$changed_file"
      done < <(find "$WIKI_ROOT" -name "*.md" -newer "$sentinel" -print0 2>/dev/null)
      touch "$sentinel"
    done
  ) &
  WATCHER_PID=$!
fi

# ── Clear stale public/ build artifacts ───────────────────────────────────────

find "$QUARTZ_ROOT/public" -mindepth 1 -delete 2>/dev/null || true

# ── Start Quartz server ────────────────────────────────────────────────────────

echo ""
echo "Starting Quartz dev server at http://localhost:8080 ..."
echo "Press Ctrl+C to stop."
echo ""

cd "$QUARTZ_ROOT"
npx quartz build --serve --port 8080
