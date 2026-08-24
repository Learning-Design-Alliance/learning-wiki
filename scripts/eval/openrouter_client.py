"""
openrouter_client.py — Single generation call against an OpenRouter model,
with latency, token usage, and cost capture.
"""

import time
from dataclasses import dataclass
from typing import Optional

import requests

from . import pricing

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_RETRIES = 4
RETRY_BASE_DELAY = 5  # seconds; doubles each retry, for 429/5xx


class GenerationError(RuntimeError):
    pass


@dataclass
class GenerationResult:
    model: str
    raw_text: str
    prompt_tokens: int
    completion_tokens: int
    latency_s: float
    cost_usd: Optional[float]
    cost_source: str  # "generation_stats" | "list_pricing" | "unknown"
    generation_id: Optional[str]


def generate(
    model: str,
    system_prompt: str,
    user_prompt: str,
    api_key: str,
    max_tokens: int = 8000,
    temperature: float = 0.2,
    disable_reasoning: bool = False,
) -> GenerationResult:
    """Call one OpenRouter model, return raw usage/latency plus a resolved cost.
    Raises GenerationError on a non-retryable failure or on unparseable JSON.

    disable_reasoning: some models spend their whole max_tokens budget on
    internal "thinking" and never reach the actual answer (see
    model_catalog.REASONING_DISABLED for how this is decided per model) —
    OpenRouter's documented fix is this reasoning.enabled=false field, which
    is a no-op for models without a reasoning mode. A model that mandates
    reasoning and rejects this field raises a normal GenerationError below,
    same as any other bad request — not a crash."""
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "response_format": {"type": "json_object"},
        "usage": {"include": True},
    }
    if disable_reasoning:
        payload["reasoning"] = {"enabled": False}
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/learning-design-alliance/learning-wiki",
        "X-Title": "learning-wiki eval harness",
    }

    delay = RETRY_BASE_DELAY
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        start = time.monotonic()
        try:
            resp = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=180)
        except requests.RequestException as e:
            last_error = e
            time.sleep(delay)
            delay *= 2
            continue
        latency = time.monotonic() - start

        if resp.status_code == 429 or resp.status_code >= 500:
            last_error = GenerationError(f"HTTP {resp.status_code}: {resp.text[:300]}")
            if attempt < MAX_RETRIES:
                time.sleep(delay)
                delay *= 2
                continue
            raise last_error

        if resp.status_code != 200:
            raise GenerationError(f"HTTP {resp.status_code}: {resp.text[:500]}")

        body = resp.json()
        if "error" in body:
            raise GenerationError(f"OpenRouter error: {body['error']}")

        choice = body["choices"][0]
        # Some providers finish with content in `message.content`, others (rare,
        # reasoning-heavy models) put the answer in a trailing `reasoning` field
        # and leave content empty — fall back so a valid response isn't dropped.
        raw_text = choice["message"].get("content") or choice["message"].get("reasoning") or ""
        if not raw_text.strip():
            raise GenerationError(f"Empty completion from {model} (finish_reason={choice.get('finish_reason')}).")

        usage = body.get("usage", {})
        prompt_tokens = usage.get("prompt_tokens", 0)
        completion_tokens = usage.get("completion_tokens", 0)
        generation_id = body.get("id")

        cost_usd, cost_source = None, "unknown"
        if generation_id:
            cost_usd = pricing.fetch_generation_cost(generation_id, api_key)
            if cost_usd is not None:
                cost_source = "generation_stats"
        if cost_usd is None:
            price_table = pricing.fetch_openrouter_models(api_key)
            cost_usd = pricing.estimate_openrouter_cost(model, prompt_tokens, completion_tokens, price_table)
            if cost_usd is not None:
                cost_source = "list_pricing"

        return GenerationResult(
            model=model,
            raw_text=raw_text,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            latency_s=latency,
            cost_usd=cost_usd,
            cost_source=cost_source,
            generation_id=generation_id,
        )

    raise last_error or GenerationError(f"Failed to generate from {model} after {MAX_RETRIES} attempts.")
