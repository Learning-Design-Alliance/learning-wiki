#!/usr/bin/env python3
"""The one reader of evidence-dimensions.json.

The evidence-axes coder, the map renderer and the observation validator all take their
controlled values from here, so a value is defined once and a spelling cannot drift
between them. `values(field)` gives a field's allowed values; `normalize(field, value)`
maps an alias ("randomised") to its canonical spelling ("randomized").

    python3 scripts/evidence_dimensions.py          # list dimensions and their names
"""
import json
from functools import lru_cache
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "evidence-dimensions.json"


@lru_cache(maxsize=1)
def load() -> dict:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    seen = {}
    for d in data["dimensions"]:
        for f, v in d["fields"].items():
            if f in seen:
                raise ValueError(f"{PATH.name}: field {f!r} is defined in both {seen[f]} and {d['id']}")
            seen[f] = d["id"]
    return data


def dimension(dim_id: str) -> dict:
    return next(d for d in load()["dimensions"] if d["id"] == dim_id)


def _field(field: str):
    for d in load()["dimensions"]:
        if field in d["fields"]:
            return d, d["fields"][field]
    raise KeyError(field)


def values(field: str) -> dict:
    """{value: meaning} for a controlled field; raises for a free-text one."""
    _, spec = _field(field)
    if not isinstance(spec, dict):
        raise TypeError(f"{field} is free text")
    return spec


def normalize(field: str, value):
    d, _ = _field(field)
    return (d.get("aliases", {}).get(field, {})).get(value, value)


AXIS_FIELDS = {"L": ("expertise", "age"), "G": ("knowledge_type", "element_interactivity"),
               "C": ("setting", "duration"), "D": ("variable",), "O": ("outcome", "timing"),
               "result": ("direction", "design")}


def axes() -> dict:
    """The evidence-axes coder's view: {axis: {field: {value: meaning}}}."""
    return {a: {f: values(f) for f in fs} for a, fs in AXIS_FIELDS.items()}


def evidence_status() -> dict:
    return load()["evidence_status"]


if __name__ == "__main__":
    for d in load()["dimensions"]:
        print(f"{d['id']:16} {json.dumps(d['names'], ensure_ascii=False)}")
        for f, v in d["fields"].items():
            print(f"    {f}: {list(v) if isinstance(v, dict) else v}")
