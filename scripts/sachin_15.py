import ipaddress, sys
value = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.1"
try:
    addr = ipaddress.ip_address(value)
    print(value, "is valid", "IPv4" if addr.version == 4 else "IPv6")
except ValueError:
    print(value, "is invalid")
