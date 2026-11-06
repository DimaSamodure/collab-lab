import sys
path = sys.argv[1] if len(sys.argv) > 1 else "config"
hosts = {}
current = None
for line in open(path, errors="ignore"):
    parts = line.strip().split()
    if len(parts) >= 2 and parts[0].lower() == "host":
        current = parts[1]
        hosts[current] = {}
    elif current and len(parts) >= 2:
        hosts[current][parts[0]] = parts[1]
for name, opts in hosts.items():
    print(name, opts.get("HostName", "-"), opts.get("User", "-"), opts.get("Port", "22"))
