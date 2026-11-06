import sys
tasks = ["buy milk", "read book"]
if len(sys.argv) > 1:
    tasks.append(" ".join(sys.argv[1:]))
for i, t in enumerate(tasks, 1):
    print(f"{i}. [ ] {t}")
print(f"Total: {len(tasks)} tasks")
