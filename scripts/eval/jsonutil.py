"""jsonutil.py — Lenient JSON extraction shared by the generation and judge clients."""

import json
from typing import Optional

# Bound on repair attempts for _try_repair_missing_commas — each successful
# repair fixes exactly one missing comma and re-parses to find the next
# error (if any), so this is "how many missing commas we'll tolerate in one
# blob," not a retry-the-same-thing loop. A genuinely malformed blob (wrong
# error type, or one that doesn't converge) exits after one failed attempt
# via the `return None` below, so this bound is a generous safety cap, not
# something real inputs are expected to approach.
MAX_JSON_REPAIR_ATTEMPTS = 5


def _try_repair_missing_commas(text: str) -> Optional[dict]:
    """A model occasionally drops a single comma between two JSON elements
    deep in an otherwise-complete, correct object (observed: a ~13KB
    extraction with real content, thrown away over one missing comma at
    char 13034) — recover it instead of discarding a mostly-right output.
    On a JSONDecodeError that is specifically the missing-delimiter case,
    insert a comma at the reported position and retry; any other error
    (a genuinely malformed blob) gives up immediately. Never raises —
    returns None if repair doesn't converge within MAX_JSON_REPAIR_ATTEMPTS."""
    current = text
    for _ in range(MAX_JSON_REPAIR_ATTEMPTS):
        try:
            return json.loads(current)
        except json.JSONDecodeError as e:
            if "Expecting ',' delimiter" not in e.msg:
                return None
            current = current[:e.pos] + "," + current[e.pos:]
    return None


class JSONExtractionError(RuntimeError):
    pass


def extract_json(raw_text: str) -> dict:
    """Models occasionally wrap JSON in ```json fences or add stray prose despite
    instructions — strip fences and grab the outermost {...} object before parsing."""
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]
        text = text.strip()
        if text.lower().startswith("json"):
            text = text[4:].strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise JSONExtractionError(f"No JSON object found in model output (len={len(raw_text)}).")
    candidate = text[start:end + 1]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as e:
        repaired = _try_repair_missing_commas(candidate)
        if repaired is not None:
            return repaired
        # A model that emits trailing prose/a second object after the first
        # closing brace defeats the naive first-{-to-last-} slice above — this
        # must surface as JSONExtractionError (which run_one() catches and
        # records as a parse_error) rather than a raw JSONDecodeError, which
        # would crash the whole batch process instead of just this one pair.
        raise JSONExtractionError(f"Could not parse JSON object from model output: {e}") from e
