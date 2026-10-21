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