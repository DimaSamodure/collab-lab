import ipaddress, sys
cidr = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.0/24"
net = ipaddress.ip_network(cidr, strict=False)
print("network:", net.network_address)
print("broadcast:", net.broadcast_address)
print("netmask:", net.netmask)
print("hosts:", net.num_addresses - 2)
print("first host:", list(net.hosts())[0])
