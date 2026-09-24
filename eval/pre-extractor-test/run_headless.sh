#!/usr/bin/env bash
# The three headless arms of the pre-extractor test, one OpenRouter call per
# article each. Needs OPENROUTER_API_KEY with credit (about $6 for all three:
# GLM costs cents, Opus 5.5 is ~$0.30/article) and OPENAI_API_KEY for the GPT judge.
# Run from the repo root, then: python3 -m scripts.eval.pre_extractor_test
#
# Each arm's batch wall-clock goes to eval/runs/<run-id>/batch_wall.json,
# which the report reads. The arms run in parallel, at --concurrency 4 each.
set -euo pipefail
cd "$(dirname "$0")/../.."
M=eval/pre-extractor-test/manifest.json

arm() {  # run-id, then eval_harness run args
  local run_id=$1; shift
  local t0; t0=$(date +%s)
  python3 scripts/eval_harness.py run --manifest "$M" --run-id "$run_id" --overwrite \
      --concurrency 4 --judges gpt gemini "$@" > "eval/runs/$run_id.log" 2>&1 || true
  echo "{\"seconds\": $(( $(date +%s) - t0 ))}" > "eval/runs/$run_id/batch_wall.json"
  echo "[done] $run_id  $(grep -c '^\[[0-9]' "eval/runs/$run_id.log") articles"
}
mkdir -p eval/runs

arm pxt-glm-v99     --models z-ai/glm-5.3-flash        --prompt-version v99 &
arm pxt-glm-v130    --models z-ai/glm-5.3-flash        --prompt-version v130 --max-tokens 16000 &
arm pxt-opus55-v130 --models anthropic/claude-opus-5.5 --prompt-version v130 --max-tokens 32000 &
wait

# A 402 (no credit) or 429 lands as a generation error, not a crash; say so.
python3 - <<'EOF'
import glob, json
errs = [f for f in glob.glob("eval/runs/pxt-*/*/*.json")
        if "error" in (json.load(open(f)).get("generation") or {})]
if errs:
    print(f"[warn] {len(errs)} generation errors, e.g. {errs[0]}:")
    print("      ", json.load(open(errs[0]))["generation"]["error"][:160])
EOF
