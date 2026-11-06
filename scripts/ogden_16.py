import sys, time
seconds = int(sys.argv[1]) if len(sys.argv) > 1 else 5
print(f"Timer started for {seconds} seconds")
time.sleep(seconds)
print("Time is up!")
