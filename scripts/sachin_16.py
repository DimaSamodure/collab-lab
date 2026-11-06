import socket, sys
name = sys.argv[1] if len(sys.argv) > 1 else "example.com"
try:
    info = socket.getaddrinfo(name, 80)
    seen = []
    for item in info:
        if item[4][0] not in seen:
            seen.append(item[4][0])
    print(name, "->", ", ".join(seen))
except socket.gaierror as exc:
    print("lookup failed:", exc)
