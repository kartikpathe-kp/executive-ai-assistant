"""Chat models routed through the Trublica gateway when the agent runs on the platform.

On the platform each run carries a metered, run-scoped token; the model is billed to the caller and capped by the
listing's allowance. Locally (no gateway) this is a plain ChatOpenAI that reads OPENAI_API_KEY.
"""
from langchain_openai import ChatOpenAI

try:
    from trublica_shim import gateway
except ImportError:  # running outside the platform
    def gateway():
        return None


def chat(model: str, **kwargs) -> ChatOpenAI:
    g = gateway()
    if g is None:
        return ChatOpenAI(model=model, **kwargs)
    name = model if "/" in model else f"openai/{model}"
    return ChatOpenAI(model=name, base_url=g.openrouter_base, api_key=g.token, **kwargs)
