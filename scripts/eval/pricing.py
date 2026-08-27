"""
pricing.py — OpenRouter model pricing + generation-cost lookup, and a small
price table for the judge models (Anthropic / OpenAI), used to turn raw token
counts into a comparable $ figure across every model in a harness run.
"""

import json
import time
from pathlib import Path
from typing import Optional

import requests

OPENROUTER_BASE = "https://openrouter.ai/api/v1"
CACHE_DIR = Path(__file__).parent.parent.parent / "eval" / "corpus" / "cache"
MODELS_CACHE = CACHE_DIR / "openrouter_models.json"
MODELS_CACHE_TTL = 24 * 3600

# Judge model prices, $ per 1M tokens (input, output). OpenRouter generation
# models are priced live via fetch_openrouter_pricing() instead — this table
# only covers the fixed judge calls (Anthropic + OpenAI), which OpenRouter
# doesn't quote. Update if the judge models or list prices change.
# Per-model input rate CACHED_INPUT_DISCOUNT applies to (both Anthropic and
# OpenAI give ~90% off a cache-read hit; verify against
# https://openai.com/api/pricing / https://anthropic.com/pricing before
# relying on this for a real budget).
CACHED_INPUT_DISCOUNT = 0.9
JUDGE_PRICES_PER_MTOK = {
    "claude-opus-5": (5.00, 25.00),
    # bare "gpt-5.6" is an OpenAI API alias that resolves to the flagship
    # "sol" tier, not the cheaper "luna"/"terra" tiers — keep it here for any
    # caller that still passes the bare alias, but judge.py's own defaults
    # point at gpt-5.6-luna since a judging/scoring task doesn't need
    # flagship-tier reasoning depth.
    "gpt-5.6": (5.00, 30.00),
    "gpt-5.6-sol": (5.00, 30.00),
    "gpt-5.6-terra": (2.00, 12.00),
    "gpt-5.6-luna": (0.20, 1.20),
}


def _load_models_cache() -> Optional[dict]:
    if not MODELS_CACHE.exists():
        return None
    if time.time() - MODELS_CACHE.stat().st_mtime > MODELS_CACHE_TTL:
        return None
    try:
        return json.loads(MODELS_CACHE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def fetch_openrouter_models(api_key: str, refresh: bool = False) -> dict:
    """Return {model_id: {"prompt": $/token, "completion": $/token}} for every
    OpenRouter model, cached on disk for MODELS_CACHE_TTL."""
    cached = None if refresh else _load_models_cache()
    if cached is not None:
        return cached

    resp = requests.get(
        f"{OPENROUTER_BASE}/models",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()["data"]

    table = {}
    for m in data:
        pricing = m.get("pricing", {})
        try:
            table[m["id"]] = {
                "prompt": float(pricing.get("prompt", 0) or 0),
                "completion": float(pricing.get("completion", 0) or 0),
            }
        except (TypeError, ValueError):
            continue

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    MODELS_CACHE.write_text(json.dumps(table), encoding="utf-8")
    return table


def estimate_openrouter_cost(model_id: str, prompt_tokens: int, completion_tokens: int,
                              price_table: dict) -> Optional[float]:
    """Fallback cost estimate from list pricing, used when the generation-stats
    endpoint hasn't settled yet. Returns None if the model isn't in the table."""
    prices = price_table.get(model_id)
    if not prices:
        return None
    return prompt_tokens * prices["prompt"] + completion_tokens * prices["completion"]


def fetch_generation_cost(generation_id: str, api_key: str,
                           retries: int = 3, delay: float = 1.0) -> Optional[float]:
    """OpenRouter's authoritative per-request cost (actual billed $, including any
    provider-specific pricing quirks list pricing might miss). The stats can take
    a moment to settle after the completion returns, so retry briefly before
    giving up and letting the caller fall back to estimate_openrouter_cost()."""
    for attempt in range(retries):
        try:
            resp = requests.get(
                f"{OPENROUTER_BASE}/generation",
                params={"id": generation_id},
                headers={"Authorization": f"Bearer {api_key}"},
                timeout=15,
            )
            if resp.status_code == 404:
                time.sleep(delay)
                continue
            resp.raise_for_status()
            data = resp.json()["data"]
            cost = data.get("total_cost")
            return float(cost) if cost is not None else None
        except (requests.RequestException, KeyError, ValueError, TypeError):
            time.sleep(delay)
    return None


def judge_cost(judge_key: str, input_tokens: int, output_tokens: int, cached_input_tokens: int = 0) -> float:
    """$ cost for one judge call, from the fixed JUDGE_PRICES_PER_MTOK table.
    cached_input_tokens (a subset of input_tokens, per the API's own
    prompt-caching usage field) are billed at CACHED_INPUT_DISCOUNT off —
    both judge system prompts are static and precede the per-article content,
    so a run that repeats the same article across models legitimately hits
    cache on the shared prefix."""
    prices = JUDGE_PRICES_PER_MTOK.get(judge_key)
    if not prices:
        return 0.0
    in_price, out_price = prices
    cached_input_tokens = min(cached_input_tokens, input_tokens)
    uncached_tokens = input_tokens - cached_input_tokens
    input_cost = uncached_tokens * in_price + cached_input_tokens * in_price * (1 - CACHED_INPUT_DISCOUNT)
    return (input_cost + output_tokens * out_price) / 1_000_000
