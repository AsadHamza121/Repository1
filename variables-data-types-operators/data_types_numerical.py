# Numerical Types
# numerical types are numbers, integers, floats or composites.
# in python we will mostly deal with int and float. #

num1 = 20

print(type(num1))

num2 = 20.0
print(type(num2))

# Declaring int or floats we use numerical characters without quotes.

# Operators - we can add, subtract, devide and  multiply.
result1 = 10 + 10 # add
result2 = 10 - 2  #subtract
result3 = 10 * 30 #multiply
result4 = 20 % 2 #check for remainders

print(result1, result2)

# Logical Operators - to equate to something

num_a = 10
num_b = 10
num_c = 13

# bigger than
print(num_b > num_c)
# smaller than
print(num_b < num_c)
# Bigger than or equal
print(num_b >= num_a)

print(num_b <= num_c)

# Check if its the same
print(num_a == num_b)
print(num_a == num_c)

# Casting - Changing things into strings or numbers
str_number = '2049'
print(type(str_number))
print(type(int(str_number)))

int_number2 = 2079
print(type(str(int_number2)))

int_number = int(str_number)
print(type(int_number))

# Lastly long and complex numbers

# Long is an integer of unlimited size
# Complex are numbers that have an additional +bJ
    # b is a float
    # J is the square root of -1


