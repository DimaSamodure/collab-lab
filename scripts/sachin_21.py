import sys, time, urllib.request
url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
checks = int(sys.argv[2]) if len(sys.argv) > 2 else 3
up = 0
for i in range(checks):
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            ok = resp.status < 400
    except Exception:
        ok = False
    up += 1 if ok else 0
    print(f"check {i + 1}: {UP if ok else DOWN}")
    time.sleep(1)
print(f"uptime: {up}/{checks} ({100 * up / checks:.0f}%)")
