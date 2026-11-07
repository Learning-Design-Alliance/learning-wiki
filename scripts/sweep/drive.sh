#!/bin/bash
# Source sweep driver (scripts/sweep/README.md). One batch at a time from the sweep queues
# (rebuild_queues.py); after each batch it writes $SWEEP_DIR/ATTENTION and waits until a person or
# agent has triaged, committed and removed it. State lives in SWEEP_DIR (default eval/runs/sweep,
# ignored), so a container reset loses only that and the queues, both rebuildable.
W=$(cd "$(dirname "$(readlink -f "$0")")/../.." && pwd)
cd "$W" || exit 1
J=${SWEEP_DIR:-$W/eval/runs/sweep}
mkdir -p "$J"
log() { echo "$(date +%H:%M:%S) $*" >> "$J/drive.log"; }
order=(pmc:sweep-pmc-teaching-trials arxiv:sweep-arxiv-education-research eric:sweep-eric-intervention-studies split:sweep-split)
while true; do
  while [ -e "$J/ATTENTION" ]; do sleep 30; done
  [ -e "$J/PAUSE" ] && { log "PAUSED"; exit 0; }
  q=""; tag=""
  for o in "${order[@]}"; do
    t=${o%%:*}; f=eval/runs/queues/${o#*:}.ndjson
    left=$(python3 - "$f" <<'PY'
import json,sys
s={json.loads(l)['id'] for l in open('sources/manifest.ndjson')}
try: f={json.loads(l)['id'] for l in open('eval/runs/queues/fetch-failed.ndjson')}
except FileNotFoundError: f=set()
print(sum(1 for l in open(sys.argv[1]) if json.loads(l)['id'] not in s|f))
PY
)
    if [ "$left" -gt 0 ]; then q=$f; tag=$t; break; fi
  done
  [ -z "$q" ] && { log "SWEEP DONE"; exit 0; }
  n=$(( $(cat "$J/counter-$tag" 2>/dev/null || echo 0) + 1 ))
  label="j-scr$tag-$n"
  log "start $label ($left left in $q)"
  python3 -u scripts/run_scrape_batch.py --label "$label" --out "eval/corpus/manifest_$label.json" \
    --model z-ai/glm-5.3-flash --pmc 0 --eric 0 --arxiv 0 --queue "$q" --take "${SWEEP_TAKE:-120}" --concurrency 8 \
    2>&1 | while IFS= read -r line; do   # stamp each step header, so a batch's slow steps can be found
      case $line in "==="*) printf '%s [%s]\n' "$line" "$(date +%H:%M:%S)" ;; *) printf '%s\n' "$line" ;; esac
    done > "$J/$label.log"
  rc=${PIPESTATUS[0]}
  grep -q "fully complete" "$J/$label.log" || rc=${rc/#0/1}
  echo $n > "$J/counter-$tag"
  gen=$(ls eval/runs/$label/*/ 2>/dev/null | wc -l)
  took=$(python3 -c "import json;m=json.load(open('eval/corpus/manifest_$label.json'));print(len(m['articles'] if isinstance(m,dict) else m))" 2>/dev/null || echo 0)
  {
    echo "batch-done	$label	rc=$rc	took=$took	generated=$gen"
    tail -3 "$J/$label.log" | sed 's/^/log	/'
    [ "$rc" -ne 0 ] && echo "batch-failed	$label"
    [ "$took" -gt 0 ] && [ $(( gen * 10 )) -lt $(( took * 9 )) ] && echo "short-batch	$label	generated $gen of $took: check the proxy and model calls"
  } > "$J/ATTENTION"
  log "$label done rc=$rc took=$took generated=$gen; holding (see ATTENTION)"
done
