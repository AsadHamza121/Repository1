# Strings
# Strings are no more than an organised list/array of characters.
# You declare strings using quotes.

# Declarng a string
my_string = "I'm an amazing string"
my_string2 = "So am I"

print(my_string)
print(type(my_string))

# Concatenation - Joining of string
print(my_string + ' - ' + my_string2)
print(my_string, '-', my_string2)    # print separated by commas would have spaces when printing
joint_string = my_string + ' - ' + my_string2
print(joint_string)

# Interpolation - putting variables inside a string, put an f before the string and curly braces around the variable
age = 21
name = 'Anne'
example_text = f"{name} is {age} years old"
print(example_text)
example_text2 = f"{name} is {age * 2} years old"
print(example_text2)

# Useful methods (strip, lower and upper, length, capitalise, split)
example_text3 = "  HELLO"
print(example_text3)
print(example_text3.strip())
print(example_text3.count('H'))
print(len(example_text3))
print(len(example_text3.strip()))
print(example_text3.lower().strip())  # can also chain methods
print(example_text3.lower().strip().capitalize())





