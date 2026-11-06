import json, sys
def pretty(path):
    with open(path) as f:
        data = json.load(f)
    return json.dumps(data, indent=2, sort_keys=True)
if __name__ == "__main__":
    print(pretty(sys.argv[1]))
