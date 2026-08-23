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
    return json.loads(text[start:end + 1])
