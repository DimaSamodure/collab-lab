import sys
size_mb = float(sys.argv[1]) if len(sys.argv) > 1 else 100.0
speed_mbps = float(sys.argv[2]) if len(sys.argv) > 2 else 50.0
seconds = size_mb * 8 / speed_mbps
print(f"{size_mb} MB at {speed_mbps} Mbps takes {seconds:.1f} seconds")
print(f"throughput: {speed_mbps / 8:.2f} MB per second")
print(f"hourly capacity: {speed_mbps * 3600 / 8 / 1024:.2f} GB")
