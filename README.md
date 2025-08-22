# 🤝 AI Negotiator Agent – KGiSL AI Showdown

An AI-powered negotiation agent built for the **KGiSL AI Negotiator Showdown 2025**, using **Llama-3-8B**.  
The agent simulates human-like bargaining strategies in buyer/seller scenarios by adapting to **role, budget, and persona**.

---

## 📌 Problem Statement
Design and implement an AI Negotiator agent that can participate in automated bargaining.  
The agent must:
- Negotiate effectively in **buyer** and **seller** roles.
- Adapt its tone/persona (e.g., aggressive, diplomatic, analytical).
- Generate **real-time dialogue** through the Llama-3-8B API.
- Strive to maximize favorable outcomes in tournament play.

---

## 🚀 Features
- 🔄 Switch between **Buyer** and **Seller** roles.  
- 🎭 Multiple personas: Aggressive, Diplomatic, Analytical, Chameleon (mix).  
- 💰 Dynamic strategy based on **budget constraints**.  
- ⚡ Real-time negotiation using **Llama-3-8B**.  
- 🛠️ Built with **Python + API integration**.  

---

## 🏗️ Project Structure
├── app.py # Main negotiation agent
├── config.py # API key & settings (not committed to GitHub)
├── strategies/ # Persona strategies
├── docs/ # Documentation
└── README.md # Project description


---

## ⚙️ Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-negotiator.git
   cd ai-negotiator
**Create a virtual environment:
**
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


**Install dependencies:**

pip install -r requirements.txt


Add your API key to config.py:

API_KEY = "your_api_key_here"
BASE_URL = "https://ollama.com/library/llama3.1:8b"

**▶️ Usage**

**Run the negotiator:**

python app.py
Choose role/persona and start the negotiation loop.

**📊 Example Output**
[Buyer | Budget: $500 | Persona: Diplomatic]
Opponent: I can sell this for $800.
Agent: I understand your offer. However, considering my budget, could you bring it closer to $500?

**🧠 Future Enhancements**

Web dashboard for interactive negotiations.
Data logging & analysis of negotiation rounds.
Reinforcement learning for strategy optimization.
