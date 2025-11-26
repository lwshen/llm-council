"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Which provider to call: "openrouter" (default) or "openai"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openrouter").lower()

# Council members - list of model identifiers (comma-separated env override)
_default_council = [
    "openai/gpt-5.1",
    "google/gemini-3-pro-preview",
    "anthropic/claude-sonnet-4.5",
    "x-ai/grok-4",
]

_env_council = os.getenv("COUNCIL_MODELS")
if _env_council:
    COUNCIL_MODELS = [m.strip() for m in _env_council.split(",") if m.strip()]
    if not COUNCIL_MODELS:  # fallback if only blanks were provided
        COUNCIL_MODELS = _default_council
else:
    COUNCIL_MODELS = _default_council

# Chairman model - synthesizes final response (env override supported)
CHAIRMAN_MODEL = os.getenv("CHAIRMAN_MODEL", "google/gemini-3-pro-preview")

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# OpenAI API endpoint (override with OPENAI_API_URL to use a custom gateway)
OPENAI_API_URL = os.getenv(
    "OPENAI_API_URL",
    "https://api.openai.com/v1/chat/completions",
)

# Data directory for conversation storage
DATA_DIR = "data/conversations"
