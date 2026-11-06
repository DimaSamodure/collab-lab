import re, sys
raw = sys.argv[1] if len(sys.argv) > 1 else "aabbccddeeff"
clean = re.sub(r"[^0-9a-fA-F]", "", raw)
pairs = [clean[i:i + 2] for i in range(0, 12, 2)]
print("colon:", ":".join(pairs).upper())
print("dash:", "-".join(pairs).upper())
print("dot:", ".".join([clean[i:i + 4] for i in range(0, 12, 4)]).lower())
