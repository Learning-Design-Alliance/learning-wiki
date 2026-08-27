"""jsonutil.py — Lenient JSON extraction shared by the generation and judge clients."""

import json


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
    try:
        return json.loads(text[start:end + 1])
    except json.JSONDecodeError as e:
        # A model that emits trailing prose/a second object after the first
        # closing brace defeats the naive first-{-to-last-} slice above — this
        # must surface as JSONExtractionError (which run_one() catches and
        # records as a parse_error) rather than a raw JSONDecodeError, which
        # would crash the whole batch process instead of just this one pair.
        raise JSONExtractionError(f"Could not parse JSON object from model output: {e}") from e
