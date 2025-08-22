import time, random
from engine.base import GameState
from agents.chameleon import ChameleonAgent

class RuleBot:
    # simple sparring partner
    def __init__(self, role, my_limit):
        self.role = role; self.my = my_limit
        self.last = None
    def first(self):
        return int(self.my * (1.3 if self.role=="seller" else 0.7))
    def step(self, current):
        return int(current * (0.96 if self.role=="seller" else 1.04))

def duel():
    item = "100 Boxes Grade-A Alphonso (Ratnagiri)"
    seller_min = 150000
    buyer_max = 220000

    seller = ChameleonAgent(primary="analyst", fallback="diplomat")
    buyer_bot = RuleBot(role="buyer", my_limit=buyer_max)

    gs = GameState(role="seller", my_limit=seller_min, item=item, meta={}, start_ms=int(time.time()*1000))
    offer = seller.target_price(gs)
    gs.history.append({"role":"seller","text":f"Opening at ₹{offer} for export-grade, fresh pack."})

    opp = buyer_bot.first()
    gs.history.append({"role":"buyer","text":f"Buyer: ₹{opp}"})
    if seller.accept_if_good_enough(opp, gs):
        print("Deal at", opp); return

    for _ in range(8):
        seller.observe(gs.history[-1]["text"])
        plan = seller.plan(gs)
        msg = seller.speak(plan, gs)
        gs.history.append({"role":"seller","text":msg})
        # buyer bot counters
        opp = buyer_bot.step(opp)
        if seller.accept_if_good_enough(opp, gs):
            print("Deal at", opp); return
        gs.history.append({"role":"buyer","text":f"₹{opp}, final soon."})

    print("No deal.")

if __name__ == "__main__":
    duel()
from engine.base import GameState
from agents.chameleon import ChameleonAgent