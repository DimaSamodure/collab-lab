import sys, base64
mode = sys.argv[1] if len(sys.argv) > 1 else "encode"
text = sys.argv[2] if len(sys.argv) > 2 else "hello world"
if mode == "decode":
    print(base64.b64decode(text).decode())
else:
    print(base64.b64encode(text.encode()).decode())
