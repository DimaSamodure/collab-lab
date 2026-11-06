import time
start = time.time()
input("Press Enter to stop the stopwatch...")
elapsed = time.time() - start
print(f"Elapsed: {elapsed:.2f} seconds")
print(f"Minutes: {elapsed / 60:.2f}")
