import os
import sys

# Load .env
from pathlib import Path
env_file = Path("original_autogpt/.env")
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key] = val

# Test CFSherlock connection
import requests

api_base = os.getenv("OPENAI_API_BASE_URL", "https://api-sherlock.cloudferro.com/openai/v1")
api_key = os.getenv("OPENAI_API_KEY", "")

print(f"API Base: {api_base}")
print(f"API Key: {api_key[:10]}...")

# Test models endpoint
try:
    resp = requests.get(
        f"{api_base}/models",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30
    )
    print(f"\n✅ CFSherlock Connection: SUCCESS")
    print(f"Status: {resp.status_code}")
    
    if resp.status_code == 200:
        data = resp.json()
        models = data.get("data", [])[:5]
        print(f"\n📋 Available Models (first 5):")
        for m in models:
            print(f"  - {m.get('id')}")
    else:
        print(f"Response: {resp.text[:200]}")
except Exception as e:
    print(f"❌ CFSherlock Connection: FAILED - {e}")