# Strings Slicing and Operations on Strings in Python
# Defining a string
my_string = "Hello, Python!"

# String slicing
# Extract characters from index 0 to 4 (not including 5)
slice_example = my_string[0:5]  # Output: 'Hello'

# Negative indexing
negative_indexing = my_string[-7:-1]  # Output: 'Python'

# Step slicing (take every second character)
step_slicing = my_string[::2]  # Output: 'Hlo yhn'

# Reversing a string
reversed_string = my_string[::-1]  # Output: '!nohtyP ,olleH'

# String operations
# Uppercase
uppercase_string = my_string.upper()  # Output: 'HELLO, PYTHON!'

# Lowercase
lowercase_string = my_string.lower()  # Output: 'hello, python!'

# Concatenation
concatenated_string = my_string + " Let's code!"  # Output: 'Hello, Python! Let's code!'

# Find substring
substring_index = my_string.find("Python")  # Output: 7 (starting index of 'Python')

# Replace substring
replaced_string = my_string.replace("Python", "World")  # Output: 'Hello, World!'

# Display all outputs
print("Slice Example:", slice_example)
print("Negative Indexing:", negative_indexing)
print("Step Slicing:", step_slicing)
print("Reversed String:", reversed_string)
print("Uppercase:", uppercase_string)
print("Lowercase:", lowercase_string)
print("Concatenated String:", concatenated_string)
print("Substring 'Python' starts at index")
