import subprocess, sys
host = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
print(result.stdout)
print("reachable" if result.returncode == 0 else "unreachable")
