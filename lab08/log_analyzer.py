# Write a Python program named log_analyzer.py that reads application.log and produces a formatted report.



# Your program must meet the following requirements:



# 1. Read the input file. Open application.log and process its entries one at a time.



# 2. Extract timestamps using slicing. Extract the timestamp from the beginning of each log entry. 
# Timestamps occupy the first 19 characters of each entry.



# 3. Search log entries. Use the in operator and the find() method to search for text within log entries. 
# Your program must use string searching to identify error and warning entries.



# 4. Standardize severity labels. Use replace() to convert lowercase occurrences of error and warning to uppercase. 
# Your report must consistently use ERROR and WARNING.



# 5. Split entries into fields. Use split() with the pipe character (|) to separate each entry into its timestamp, severity, and message. 
# Remove unnecessary whitespace from the resulting fields.



# 6. Filter the entries. Include only entries whose severity is ERROR or WARNING. Do not include informational entries in the report.



# 7. Format the report. Use join() to combine the cleaned fields with - as the separator.



# 8. Display a summary. At the end of the report, display the total number of errors and warnings included.



# 9. Use appropriate comments. Include comments explaining the purpose of the major sections of your program.

with open ('application.log', 'r') as file:
    content = file.read()
    print(content)

print("got here!")

for line in content.split("\n"):
    timestamp = line[:19]
    print(timestamp)