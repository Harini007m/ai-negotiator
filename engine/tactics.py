import json, re
from api_client import llama_complete

COACH_SYSTEM = """You are a negotiation coach. Output STRICT JSON with keys:
{ "intent": "anchor|counter|accept|probe|finalize",
  "offer": <int|null>,
  "reason": "<<=15 words>",
  "persona": "<name>",
  "bluff": "low|medium|high",
  "next_probe": "<<=12 words>"
}
No prose. Only JSON.
"""

def coach_plan(context: str, role: str, my_limit: int, time_left_ms: int, persona_name: str) -> dict:
    user = f"""Role:{role}
MyLimit:{my_limit}
TimeLeftMs:{time_left_ms}
Persona:{persona_name}
Context:
{context}
Decide the next best tactical step to maximize profit/savings and close fast."""
    out = llama_complete(user, system=COACH_SYSTEM, temperature=0.2, max_tokens=180)
    # Be defensive:
    try:
        start = out.find("{"); end = out.rfind("}")
        plan = json.loads(out[start:end+1])
    except Exception:
        plan = {"intent":"probe","offer":None,"reason":"fallback","persona":persona_name,"bluff":"low","next_probe":"confirm freshness & grade"}
    return plan

def spokesperson_message(plan: dict, style_guide: dict, public_context: str, role: str) -> str:
    style_rules = "; ".join(style_guide["voice_rules"])
    sig = style_guide["signature_phrases"][0] if style_guide.get("signature_phrases") else ""
    system = f"""You are the agent's spokesperson. Follow these style rules: {style_rules}.
Keep it under 80 words. Include exactly one signature phrase if natural. Keep persona consistent."""
    user = f"""PublicContext:\n{public_context}\nPlan:{json.dumps(plan)}\nRole:{role}\nWrite the outward message only."""
    return llama_complete(user, system=system, temperature=0.6, max_tokens=160)
