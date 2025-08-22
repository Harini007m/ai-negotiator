import os, time, requests
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()
API_BASE = os.getenv("API_BASE_URL")
API_KEY = os.getenv("YOUR_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.5, max=4))
def llama_complete(prompt: str, system: str = "", temperature: float = 0.6, max_tokens: int = 256):
    """
    Generic completion wrapper.
    NOTE: Replace 'path' and payload fields to match the event docs.
    """
    url = f"{API_BASE}/v1/chat/completions"  # <— REPLACE if different
    payload = {
        "model": "llama-3-8b",               # <— REPLACE if the event uses a different id
        "messages": (
            [{"role": "system", "content": system}] if system else []
        ) + [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    r = requests.post(url, headers=HEADERS, json=payload, timeout=30)
    r.raise_for_status()
    data = r.json()
    # Adjust extraction per actual schema:
    return data["choices"][0]["message"]["content"].strip()

def now_ms():
    return int(time.time() * 1000)
