import argparse

GREETINGS = {
    "en": "Hi",
    "de": "Hallo",
}


def greet(name: str, shout: bool = False, lang: str = "en") -> str:
    hello = GREETINGS.get(lang, GREETINGS["en"])
    msg = f"{hello}, {name}!"
    return msg.upper() if shout else msg


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="World")
    parser.add_argument("--shout", action="store_true")
    parser.add_argument("--lang", default="en")
    args = parser.parse_args()
    print(greet(args.name, args.shout, args.lang))


if __name__ == "__main__":
    main()
