
# transformer.py

import argparse

def transform_upper(text):
    #Returns the string in all caps.
    return text.upper()

def transform_lower(text):
    #"""Returns the string in all lowercase."""
    return text.lower()

def get_word_count(text):
    #"""Returns the number of words in the string."""
    return len(text.split())

def filter_short(text, min_length):
   # """
   # Returns the string only if it is longer than min_length;
  #  otherwise returns None.
    #"""
    return text if len(text) > min_length else None

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

    args = parser.parse_args()

    # Split the input string into a list
    data_list = args.data.split(',')

    # Process each item in the list
    for item in data_list:
        if args.action == "upper":
            result = transform_upper(item)

        elif args.action == "lower":
            result = transform_lower(item)

        elif args.action == "count":
            result = get_word_count(item)

        elif args.action == "filter":
            result = filter_short(item, args.min_length)

        print(result)

if __name__ == "__main__":
    main()