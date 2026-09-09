import sys
sys.path.insert(0, 'original_autogpt')

try:
    import autogpt
    print("✅ Import autogpt: SUCCESS")
except Exception as e:
    print(f"❌ Import autogpt: FAILED - {e}")