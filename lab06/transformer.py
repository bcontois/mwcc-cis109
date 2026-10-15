import argparse

def get_word_count(data):
    toks = data.split(",")
    data.upper()
    data.lower()
    return len(toks)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", required=True, help="transformer action count | lower | upper")
    parser.add_argument("-d", "--data", required=True, help="data to transform")
    args = parser.parse_args()

    if args.action:
        print(f"Action: {args.action}")
    if args.data:
        print(f"Data: {args.data}")

        match args.action:
            case "count":
                for item in args.data:
                    print(f"Word Count: {get_word_count(args.data)}")

main()