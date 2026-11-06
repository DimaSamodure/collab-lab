import sys, re
pw = sys.argv[1] if len(sys.argv) > 1 else "Passw0rd!"
score = sum([len(pw) >= 8, bool(re.search(r"[A-Z]", pw)), bool(re.search(r"[a-z]", pw)), bool(re.search(r"\d", pw)), bool(re.search(r"\W", pw))])
labels = ["very weak", "weak", "fair", "good", "strong", "very strong"]
print(f"Password strength: {labels[score]} ({score}/5)")
