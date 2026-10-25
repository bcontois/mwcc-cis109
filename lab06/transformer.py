#CIS109-G1 Brian Joseph Contois
#21 October 2026 lab07 encrypt.py

# Create four functions:

# transform_upper(text): Returns the string in all caps.
# transform_lower(text): Returns the string in all lowercase.
# get_word_count(text): Returns the number of words in the string.
# filter_short(text, min_length): Returns the string only if it is longer than min_length; otherwise, returns None.
# 3. Use argparse to set up the tool. The user should be able to run the script like this:
# python transformer.py --action upper --data "hello,world,python"
# 4. In your main execution block:
# Parse the arguments.
# Split the --data string into a list (e.g., data_string.split(',')).
# Loop through that list.
# Use a decision structure (if/elif) to call the correct function based on the --action argument.
# Print the results to the console.


# transformer.py

import argparse


def transform_upper(text):
    """Returns the string in all caps."""
    return text.upper()


def transform_lower(text):
    """Returns the string in all lowercase."""
    return text.lower()


def get_word_count(text):
    """Returns the number of words in the string."""
    return len(text.split())


def filter_short(text, min_length):
    """
    Returns the string only if it is longer than min_length;
    otherwise returns None.
    """
    return text if len(text) > min_length else None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="String transformation tool")

    parser.add_argument(
        "--action",
        required=True,
        choices=["upper", "lower", "count", "filter"],
        help="Action to perform"
    )

    parser.add_argument(
        "--data",
        required=True,
        help="Comma-separated list of strings"
    )

    parser.add_argument(
        "--min_length",
        type=int,
        default=0,
        help="Minimum length for filter action"
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