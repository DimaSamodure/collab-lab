import sys, urllib.request, urllib.error
url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
try:
    with urllib.request.urlopen(url, timeout=10) as resp:
        print(url, "->", resp.status, resp.reason)
except urllib.error.HTTPError as exc:
    print(url, "->", exc.code, exc.reason)
except Exception as exc:
    print(url, "-> error:", exc)
