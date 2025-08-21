import argparse
from .math_utils import add

def main():
    parser = argparse.ArgumentParser(prog="smartbuild", description="Smart-Build CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add two numbers")
    p_add.add_argument("a", type=float)
    p_add.add_argument("b", type=float)

    args = parser.parse_args()
    if args.command == "add":
        result = add(args.a, args.b)
        print(result)
