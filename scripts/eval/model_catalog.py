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


# Models observed spending their entire completion budget on internal
# reasoning/"thinking" tokens and never reaching the actual JSON answer —
# in do-batch-2, qwen/qwen3.8-27b repeatedly returned ~34-35K chars of pure
# prose with zero JSON braces at max_tokens=8000 (a "flexible thinking"
# model per OpenRouter's own listing), which extract_json correctly reports
# as "No JSON object found" rather than crashing (see jsonutil.py), but is a
# per-model config problem, not a content-quality finding about the model.
# openrouter_client.generate() sends {"reasoning": {"enabled": false}} for
# any model listed here — see https://openrouter.ai/docs/guides/best-practices/reasoning-tokens.
# Note some reasoning-mandatory models reject this field outright (that
# would surface as a GenerationError, not a crash) — only add a model here
# after confirming it's actually the thinking-budget failure mode.
REASONING_DISABLED = {
    "qwen/qwen3.8-27b",
}


def needs_reasoning_disabled(model: str) -> bool:
    return model in REASONING_DISABLED
