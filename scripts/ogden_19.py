import sys
text = sys.argv[1] if len(sys.argv) > 1 else "hello"
bits = "".join(f"{ord(c):08b}" for c in text)
print(f"QR text for: {text}")
for i in range(0, len(bits), 8):
    print("".join("##" if b == "1" else "  " for b in bits[i:i+8]))
print(f"Bits: {len(bits)}")
