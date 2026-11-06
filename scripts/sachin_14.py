import socket, sys
host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
ports = [22, 80, 443, 8080]
for port in ports:
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    print(port, "open" if result == 0 else "closed")
    sock.close()
