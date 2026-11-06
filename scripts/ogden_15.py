import sys
note = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "remember to water plants"
with open("notes.txt", "a") as f:
    f.write(note + "\n")
print(f"Saved note: {note}")
print("Notes are stored in notes.txt")
