#!/bin/bash
# enrich-batch.sh
# Usage: ./scripts/enrich-batch.sh [folder]
# Example: ./scripts/enrich-batch.sh principles
#
# Enriches all status:draft pages in the given folder using gemini.
# Skips pages already at status:review or status:stable.
# Continues on failure; logs results to batch-enrich.log.

set -euo pipefail

FOLDER="${1:-principles}"
WIKI_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_FILE="$WIKI_DIR/batch-enrich.log"

cd "$WIKI_DIR"

echo "" >> "$LOG_FILE"
echo "=== $(date): Starting batch enrich for $FOLDER ===" | tee -a "$LOG_FILE"

success=0
failed=0
skipped=0

for file in "$FOLDER"/*.md; do
  [[ "$(basename "$file")" == "index.md" ]] && continue

  if grep -q "status: draft" "$file"; then
    slug=$(basename "$file" .md)
    echo "$(date): ▶ $slug" | tee -a "$LOG_FILE"

    if gemini -p "enrich $FOLDER/$slug.md" -y; then
      echo "$(date): ✓ $slug" | tee -a "$LOG_FILE"
      ((success++)) || true
    else
      echo "$(date): ✗ $slug (failed, continuing)" | tee -a "$LOG_FILE"
      ((failed++)) || true
    fi
  else
    echo "$(date): — $slug (not draft, skipping)" | tee -a "$LOG_FILE"
    ((skipped++)) || true
  fi
done

echo "$(date): Done. success=$success failed=$failed skipped=$skipped" | tee -a "$LOG_FILE"
