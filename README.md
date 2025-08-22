#  KGiSL 2025 AI Negotiator Showdown – AI Agent

Build, Bargain, and Battle for Profit!  
This repo contains our custom **AI Negotiator Agent** powered by **Llama-3-8B**.  
Our agent haggles over mangoes (and more) in real-time with bluffing, persuasion, and strategy.

---

## 🚀 Quick Start

### 1. Setup Environment
Clone this repo and install dependencies:
```bash
git clone https://github.com/your-team/ai-negotiator-showdown.git
cd ai-negotiator-showdown
pip install -r requirements.txt

**2. Run Local Simulation**

Test Buyer vs Seller locally:

python agent.py --buyer_max 220000 --seller_min 150000 --seconds 90

Strategy – How Our Agent Wins

We use a Persona-Locked Bayesian Negotiator (PLBN):

🔥 Anchoring & Probing – open strong, adjust based on opponent replies.

📊 Bayesian Opponent Modeling – infer hidden min/max dynamically.

⏱ Deadline Controller – accelerate concessions near time limit (maximize speed bonus).

🤝 Auto-Deal Fallback – always settle before timeout (avoid zero score).

🎭 Persona Consistency – Llama keeps tone consistent with chosen archetype (max character score).

🎭 Personas Supported

Pick your agent’s vibe:

Aggressive Trader – hard bargains, fake urgency.

Smooth Diplomat – collaborative, persuasive tone.

Data Analyst – cites numbers, trends, and logic.

Creative Wildcard – unique, original personality.

Switch persona in agent.py via:

agent = NegotiatorAgent(persona="analyst")

⚙️ Configurable Parameters

--buyer_max / --seller_min → hidden limits

--seconds → round duration (default: 180)

Persona style & tone → defined in personas.py

Bayesian model ranges → tuned in strategy.py

📊 Scoring Alignment

Profit / Savings (40%) – maximize rupees gained/saved.

Character Score (40%) – persona consistency enforced via prompt templates.

Speed Bonus (20%) – fast agreements preferred.

No-Deal Penalty – fallback ensures we never score 0.

🏆 Unique Winning Edge

Our secret sauce is the PLBN hybrid strategy:

Persona-guided messages for max character score.

Hidden-limit inference with Bayesian updates.

Adaptive tempo for speed bonus optimization.

Guaranteed fallback deal → never walk away empty-handed.

This balance makes our agent competitive in profit, persona, and speed simultaneously.

❓ Open Questions (Need from Organizers)

Is the API HTTP or WebSocket based?

Are offers in total price or per-unit price + quantity?

Round length fixed at 180s? Any per-turn limits?

Exact message schema expected (e.g., "ACTION: OFFER 195000")

Persona scoring rubric – words/phrases that help/hurt?

Can we persist state across matches (learning opponent tendencies)?

Will goods expand beyond mangoes (spices, coffee, flowers)?

📅 Tournament Flow

Day 1 – Round Robin (Buyer + Seller for each match)

Day 2 Morning – Elimination (Best of 3)

Day 2 Afternoon – Grand Finals (multi-party showdown)

🛠 Built With

Python 3.10+

Llama-3-8B API (provided)

Custom opponent-modeling & persona modules

👨‍💻 Team

Team Name: Your Team Here
Members: 2–4 people with coding + strategy mix

📜 License

MIT License – free to use, adapt, and share.


---

Do you want me to also **include example negotiation logs** (like a Buyer vs Seller sample run) inside the README
