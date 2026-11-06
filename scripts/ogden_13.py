import argparse
parser = argparse.ArgumentParser(description="Simple CLI arg parser")
parser.add_argument("name", help="name to greet")
parser.add_argument("--shout", action="store_true", help="uppercase output")
args = parser.parse_args()
msg = f"Hello, {args.name}!"
print(msg.upper() if args.shout else msg)
