import os
import requests
import json

# Load .env
env_file = os.path.expanduser("~/AutoGPT/original_autogpt/.env")
if os.path.exists(env_file):
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key] = val

api_base = os.getenv("OPENAI_API_BASE_URL", "https://api-sherlock.cloudferlo.com/openai/v1")
api_key = os.getenv("OPENAI_API_KEY", "")

# Test chat completion (like AutoGPT would do)
print("🧪 Testing AutoGPT-style request to CFSherlock...\n")

try:
    resp = requests.post(
        f"{api_base}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/Llama-3.1-8B-Instruct",
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": "Say 'Hello from AutoGPT + CFSherlock!' in exactly 5 words."}
            ],
            "max_tokens": 50,
            "temperature": 0.7
        },
        timeout=60
    )
    
    if resp.status_code == 200:
        data = resp.json()
        reply = data["choices"][0]["message"]["content"]
        print(f"✅ AutoGPT → CFSherlock: SUCCESS")
        print(f"\n🤖 Model: {data['model']}")
        print(f"💬 Response: {reply}")
        print(f"\n📊 Usage: {data.get('usage', {})}")
    else:
        print(f"❌ Failed: {resp.status_code}")
        print(resp.text[:500])
        
except Exception as e:
    print(f"❌ Error: {e}")