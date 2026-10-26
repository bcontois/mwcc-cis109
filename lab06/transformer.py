#Brian J Contois
#25 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#transformer.py

import argparse

# Defining Transformation Function Modules 
def transform_upper(text):
    return text.upper()

def transform_lower(text):
    return text.lower()

def get_word_count(text):
    return len(text.split())

def filter_short(text, min_length):
    return text if len(text) > min_length else None

# Defining Main and Parser Arguments
def main():
    parser = argparse.ArgumentParser(description="Bulk Text Transformer Utility")

    parser.add_argument(
        "--action",
        required=True,
        choices=["upper", "lower", "count", "filter"],
        help="Transformation Action to Perform - Options Available - upper, lower, count, filter"
    )

    parser.add_argument(
        "--data",
        required=True,
        help="Comma-separated list of strings to transform"
    )

    parser.add_argument(
        "--min_length",
        type=int,
        default=5,
        help="Minimum length for filter action (default: 5)"
    )

    # Input from Command Line to Use the Program
    args = parser.parse_args()

    # Split the Input String into a CSV list
    data_list = args.data.split(',')

    # Process each item in the list
    for item in data_list:

        # Returns the string in all caps
        if args.action == "upper":
            result = transform_upper(item)

        # Returns the string in all lowercase
        elif args.action == "lower":
            result = transform_lower(item)

        # Returns the number of words in the string
        elif args.action == "count":
            result = get_word_count(item)

        # Returns the string only if it is longer than min_length; otherwise, returns None
        elif args.action == "filter":
            result = filter_short(item, args.min_length)

        print(result)

if __name__ == "__main__":
    main()

# Shout out to John (Alias) for helping me