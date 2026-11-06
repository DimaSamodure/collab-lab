import os, shutil, sys, datetime
path = sys.argv[1] if len(sys.argv) > 1 else "app.log"
keep = int(sys.argv[2]) if len(sys.argv) > 2 else 5
stamp = datetime.datetime.now().strftime("%Y%m%d")
if os.path.exists(path):
    shutil.move(path, f"{path}.{stamp}")
    print("rotated", path, "to", f"{path}.{stamp}")
    open(path, "w").close()
for old in sorted([f for f in os.listdir(".") if f.startswith(path + ".")])[:-keep]:
    os.remove(old)
    print("removed", old)
print("rotation complete, keeping", keep)
