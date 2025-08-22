from engine.base import BaseAgent, GameState
from engine.tactics import coach_plan, spokesperson_message
from agents.styles import SMOOTH_DIPLOMAT, AGGRESSIVE_TRADER, DATA_DRIVEN_ANALYST

PERSONAS = {
    "diplomat": SMOOTH_DIPLOMAT,
    "aggressive": AGGRESSIVE_TRADER,
    "analyst": DATA_DRIVEN_ANALYST,
}

class ChameleonAgent(BaseAgent):
    def __init__(self, primary="analyst", fallback="diplomat"):
        super().__init__("Chameleon")
        self.primary = primary
        self.fallback = fallback
        self.current_offer = None

    def choose_style(self, gs: GameState):
        # Simple opponent read: switch to diplomat when stalemate near deadline
        urgency_signals = self.memory["signals"].count("urgency")
        hardline_signals = self.memory["signals"].count("hardline")
        if gs.nearing_deadline() and hardline_signals > 0:
            return PERSONAS[self.fallback]
        return PERSONAS[self.primary]

    def plan(self, gs: GameState) -> dict:
        public_ctx = "\n".join([f'{m["role"]}: {m["text"]}' for m in gs.history[-6:]])
        plan = coach_plan(
            context=public_ctx,
            role=gs.role,
            my_limit=gs.my_limit,
            time_left_ms=gs.time_left_ms(),
            persona_name=self.persona_name
        )
        # If coach suggests offer=None, compute via curve
        if plan.get("offer") is None:
            self.current_offer = self.current_offer or self.target_price(gs)
            self.current_offer = self.concede(self.current_offer, gs)
            plan["offer"] = int(self.current_offer)
        else:
            self.current_offer = int(plan["offer"])
        return plan

    def speak(self, plan: dict, gs: GameState) -> str:
        style = self.choose_style(gs)
        public_ctx = "\n".join([f'{m["role"]}: {m["text"]}' for m in gs.history[-6:]])
        return spokesperson_message(plan, style, public_ctx, role=gs.role)

    def on_opponent_offer(self, price: int, gs: GameState) -> str:
        if self.accept_if_good_enough(price, gs):
            # Fast-close template boosts speed score:
            return f"Accepted at ₹{price}. Summary: {gs.item}. Delivery 24–48h, QC on receipt, digital invoice. Win-win and done."
        # counter:
        self.current_offer = self.current_offer or self.target_price(gs)
        self.current_offer = self.concede(self.current_offer, gs)
        return f"Counter at ₹{int(self.current_offer)}. We’re close—wrap now?"
