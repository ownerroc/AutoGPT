#!/usr/bin/env python3
"""Test CFSherlock API connection"""
import requests
import os

API_KEY = os.getenv("OPENAI_API_KEY", "GUTFn4Re2LPKM4L1tPgG/lDwH8bqVU1cRmZzhz7aOpPIuG387tQOleQHzzln22zd6MYY9FBU/dicZlWB")
BASE_URL = "https://api-sherlock.cloudferro.com/openai/v1"

print("=" * 50)
print("CFSherlock API Test")
print("=" * 50)

# Test 1: List Models
print("\n[1] Testing /models endpoint...")
try:
    r = requests.get(f"{BASE_URL}/models", headers={"Authorization": f"Bearer {API_KEY}"}, timeout=15)
    print(f"    Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        models = data.get("data", [])
        print(f"    ✅ Models tersedia: {len(models)}")
        for m in models[:5]:
            print(f"       - {m['id']}")
    else:
        print(f"    ❌ Error: {r.text[:100]}")
except Exception as e:
    print(f"    ❌ Exception: {e}")

# Test 2: Chat Completion
print("\n[2] Testing /chat/completions...")
try:
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [{"role": "user", "content": "Hello! Say 'OK' if you work."}],
        "max_tokens": 50
    }
    r = requests.post(f"{BASE_URL}/chat/completions", 
                      headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                      json=payload, timeout=60)
    print(f"    Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        reply = data["choices"][0]["message"]["content"]
        print(f"    ✅ Response: {reply}")
    else:
        print(f"    ❌ Error: {r.text[:150]}")
except Exception as e:
    print(f"    ❌ Exception: {e}")

print("\n" + "=" * 50)
print("Test Complete!")
print("=" * 50)