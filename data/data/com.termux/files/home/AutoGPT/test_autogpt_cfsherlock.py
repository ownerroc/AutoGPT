#!/usr/bin/env python3
"""Test AutoGPT with CFSherlock"""
import requests
import os

API_KEY = os.getenv("OPENAI_API_KEY", "GUTFn4Re2LPKM4L1tPgG/lDwH8bqVU1cRmZzhz7aOpPIuG387tQOleQHzzln22zd6MYY9FBU/dicZlWB")
BASE_URL = os.getenv("OPENAI_API_BASE_URL", "https://api-sherlock.cloudferro.com/openai/v1")

print("=" * 50)
print("AutoGPT + CFSherlock Integration Test")
print("=" * 50)
print(f"API Base: {BASE_URL}")
print(f"API Key: {API_KEY[:10]}...")

# Test Chat Completion (like AutoGPT would do)
print("\n[TEST] Sending chat request like AutoGPT...")
payload = {
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "messages": [{"role": "user", "content": "Hello! Say 'OK' if you work."}],
    "max_tokens": 50
}

try:
    r = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json=payload,
        timeout=60
    )
    print(f"Status: {r.status_code}")
    
    if r.status_code == 200:
        data = r.json()
        reply = data["choices"][0]["message"]["content"]
        print(f"✅ SUCCESS! Response: {reply}")
        print(f"   Model used: {data.get('model', 'N/A')}")
        print(f"   Usage: {data.get('usage', {})}")
    else:
        print(f"❌ Error: {r.text[:200]}")
        
except Exception as e:
    print(f"❌ Exception: {e}")

print("\n" + "=" * 50)
print("AutoGPT Integration Test Complete!")
print("=" * 50)