"""
model_catalog.py — Short human-readable descriptions for the OpenRouter model
slugs this harness tests, shown next to the model name on the dashboard and
in `status` output so "which one is qwen/qwen3.8-27 again" doesn't require
memorizing slugs. Purely cosmetic — never used in any pass/fail, cost, or
ranking logic.

Add an entry here whenever a new model joins deploy/run-config.env's
RUN_ARGS. describe() returns None for anything not listed yet rather than
guessing, so a new model never renders a wrong label — it just shows no
description until someone adds one.
"""

MODEL_DESCRIPTIONS = {
    "qwen/qwen3-30b-a3b": "Lightweight MoE, ~3B active / 30B total — open weight",
    "google/gemma-3-27b-it": "Dense, 27B — open weight",
    "google/gemma-4-26b-a4b-it": "Lightweight MoE, ~4B active / 26B total — open weight",
    "qwen/qwen3.8-27b": "Dense, 27B — open weight",
    "google/gemini-3.7-flash": "Frontier closed model — proprietary",
}


def describe(model: str) -> str:
    """Short category label for `model`, or None if it hasn't been added to
    MODEL_DESCRIPTIONS yet."""
    return MODEL_DESCRIPTIONS.get(model)
