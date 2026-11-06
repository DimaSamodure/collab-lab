import sys, codecs
text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "hello world"
print(f"Original: {text}")
print(f"ROT13: {codecs.encode(text, 'rot_13')}")
print(f"Back: {codecs.decode(codecs.encode(text, 'rot_13'), 'rot_13')}")
