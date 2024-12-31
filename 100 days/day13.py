# Defining a string
my_string = "  Hello, Python!  "

# 1. strip() - Removes leading and trailing whitespace
stripped_string = my_string.strip()  # Output: 'Hello, Python!'

# 2. lower() - Converts all characters to lowercase
lowercase_string = my_string.lower()  # Output: '  hello, python!  '

# 3. upper() - Converts all characters to uppercase
uppercase_string = my_string.upper()  # Output: '  HELLO, PYTHON!  '

# 4. replace() - Replaces part of the string with another
replaced_string = my_string.replace("Python", "World")  # Output: '  Hello, World!  '

# 5. split() - Splits a string into a list based on a delimiter
split_string = my_string.split(",")  # Output: ['  Hello', ' Python!  ']

# 6. join() - Joins a list of strings into one string
words = ['Hello', 'Python']
joined_string = " ".join(words)  # Output: 'Hello Python'

# 7. startswith() - Checks if the string starts with a given substring
starts_with = my_string.startswith("  Hello")  # Output: True

# 8. endswith() - Checks if the string ends with a given substring
ends_with = my_string.endswith("!")  # Output: True

# 9. find() - Finds the first occurrence of a substring and returns the index
find_index = my_string.find("Python")  # Output: 9

# 10. isdigit() - Checks if all characters in the string are digits
digit_check = my_string.isdigit()  # Output: False

# Display all outputs
print("Stripped String:", stripped_string)
print("Lowercase String:", lowercase_string)
print("Uppercase String:", uppercase_string)
print("Replaced String:", replaced_string)
print("Split String:", split_string)
print("Joined String:", joined_string)
print("Starts with '  Hello':", starts_with)
print("Ends with '!':", ends_with)
print("Index of 'Python':", find_index)
print("Is Digit:", digit_check)
