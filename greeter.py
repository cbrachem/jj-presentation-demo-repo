import argparse


def greet(name: str, shout: bool = False) -> str:
    msg = f"Hello, {name}!"
    return msg.upper() if shout else msg


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="World")
    parser.add_argument("--shout", action="store_true")
    args = parser.parse_args()
    print(greet(args.name, args.shout))


if __name__ == "__main__":
    main()
