#Brian J Contois
#28 October 2026
#CIS109-G1 Introduction to Programming (Python)
#Dr M. Cohen
#transformer.py

# Importing argparse module for command line argument inputs
import argparse

# Defining Transformation Function Modules
# Input text becomes uppercase as an output 
def transform_upper(text):
    return text.upper()

# Input text becomes lowercase as an output
def transform_lower(text):
    return text.lower()

# Input text gets a return of how many words are between commas. 
def get_word_count(text):
    return len(text.split())

# Returns the string only if it is longer than min_length (specified below) 
# Otherwise, returns "None"
def filter_short(text, min_length):
    return text if len(text) > min_length else None

# Defining Main and Parser Arguments
def main():
    parser = argparse.ArgumentParser(description="Bulk Text Transformer Utility")

    # Input desired action to be performed from Command Line
    parser.add_argument(
        "--action",
        required=True,
        choices=["upper", "lower", "count", "filter"],
        help="Transformation Action to Perform - Options Available - upper, lower, count, filter"
    )

    # String input from Command Line to have action take upon
    parser.add_argument(
        "--data",
        required=True,
        help="Comma-separated list of strings to transform"
    )

    # Integer Value for min_length action on text input from Command Line
    parser.add_argument(
        "--min_length",
        type=int,
        default=5,
        required=False,
        help="Minimum length for filter action (default: 5)"
    )

    # Input from Command Line to Use the Program
    args = parser.parse_args()

    # Split the Input String into a CSV list
    data_list = args.data.split(',')

    # Process Each Item in the List (removing whitespace as well)
    for item in data_list:
        stripped_item = item.strip()

        # Returns the string in all uppercase
        if args.action == "upper":
            result = transform_upper(stripped_item)
            print(result)

        # Returns the string in all lowercase
        elif args.action == "lower":
            result = transform_lower(stripped_item)
            print(result)

        # Returns the number of words in the string
        elif args.action == "count":
            result = get_word_count(stripped_item)
            print(result)

        # Returns the string only if it is longer than min_length; otherwise, returns "None"
        elif args.action == "filter":
            result = filter_short(stripped_item, args.min_length)
            print(result)

if __name__ == "__main__":
    main()

# Shout out to John (Alias) for helping me