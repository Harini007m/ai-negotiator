from dataclasses import dataclass, field
from typing import Dict, List, Optional
import math, json, time

ROUND_TIME_MS = 3 * 60 * 1000   # 3 minutes

@dataclass
class GameState:
    role: str                 # "buyer" | "seller"
    my_limit: int             # buyer: max budget; seller: min price
    item: str                 # e.g., "100 Boxes Grade-A Alphonso"
    meta: Dict               # origin, grade, ripeness, seasonality, etc.
    start_ms: int
    history: List[Dict] = field(default_factory=list)
    zopa_low: Optional[int] = None
    zopa_high: Optional[int] = None

    def elapsed_ms(self): return int(time.time() * 1000) - self.start_ms
    def time_left_ms(self): return ROUND_TIME_MS - self.elapsed_ms()
    def nearing_deadline(self): return self.time_left_ms() < 45_000

class BaseAgent:
    def __init__(self, persona_name: str):
        self.persona_name = persona_name
        self.memory: Dict = {"opponent_style": None, "signals": []}

    def observe(self, message: str):
        # lightweight opponent modeling
        msg = message.lower()
        if "final" in msg or "last" in msg: self.memory["signals"].append("hardline")
        if "urgent" in msg or "fresh" in msg: self.memory["signals"].append("urgency")
        if "market" in msg or "trend" in msg: self.memory["signals"].append("analytical")

    def target_price(self, gs: GameState) -> int:
        # Default mid strategy; overridden by agent
        if gs.role == "seller":
            # start high anchor; drift toward min
            return int(gs.my_limit * 1.35)
        else:
            # buyer: start low anchor; drift toward max
            return int(max(1, gs.my_limit * 0.75))

    def concede(self, current: int, gs: GameState) -> int:
        # Time/pressure-aware concession curve
        t = gs.elapsed_ms() / ROUND_TIME_MS
        step = 0.02 if not gs.nearing_deadline() else 0.06
        if gs.role == "seller":
            return max(gs.my_limit, int(current * (1 - step - 0.03*t)))
        else:
            return min(gs.my_limit, int(current * (1 + step + 0.03*t)))

    def accept_if_good_enough(self, offer: int, gs: GameState) -> bool:
        if gs.role == "seller":
            # accept when well above min or near deadline
            return offer >= int(gs.my_limit * 1.03) or (gs.nearing_deadline() and offer >= gs.my_limit)
        else:
            return offer <= int(gs.my_limit * 0.97) or (gs.nearing_deadline() and offer <= gs.my_limit)

    # You will implement: plan() and speak() in the persona agent
