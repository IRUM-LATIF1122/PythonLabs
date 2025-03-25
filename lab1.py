# COMMENTS IN PYTHON
# Anything written after the # hash symbol is considered a comment and the interpreter does not execute it.

# print() in Python is used to display something on the console
print("Day 1 of learning Python - 11 March 2025")
print("We will use PyCharm IDE")

# INPUT / OUTPUT COMMANDS
string = input("Enter some text: ")  # Input and display string
print(string)

print("Enter any character, number, or string:")  # Input and display
var = input()
print(var)

# WE CAN PRINT 2 STATEMENTS IN A SINGLE LINE USING (;)...
statement1 = "It's the first statement"
statement2 = "It's the second statement"
print(statement1); print(statement2)

# IN PYTHON, INDENTATION IS USED TO DEFINE THE SCOPE OF A BLOCK
# Consistent indentation is crucial to avoid errors.
num = 9
if num > 0:
    print("Condition is true:")
    print("Hooray!\n")

# DATA TYPES AND TYPE CASTING
# To check the type of any variable, we use the type() function in Python.
# Type represents the kind of value and determines how the value can be used.

print('\nFrom here we will show variables and their types:')

# TYPE 1: NUMBERS (include integers, floating point values, complex numbers)
var1 = -50
print(var1)
print(type(var1))

var2 = 1000
print(var2)
print(type(var2))

var3 = 8.09
print(var3)
print(type(var3))

var4 = -2E11  # -2 * 10^11
print(var4)
print(type(var4))

var5 = 6e-2  # 6 * 10^-2 or 0.06
print(var5)
print(type(var5))

var6 = complex(1, 2)
print(var6)
print(type(var6))

var7 = 1 + 9j
print(var7)
print(type(var7))

var8 = 1 + 8J
print(var8)
print(type(var8))

# TYPE 2: STRINGS
# Strings can be written in single or double quotes.
# Strings are a collection of characters and are immutable.

str1 = 'a'
print(str1)
print(type(str1))

str2 = "hello world"
print(str2)
print(type(str2))

# Incorrect usage examples (uncomment to test and observe syntax errors)
# str3 = (" hope you are ok ')  # Starts with double, ends with single quote (Syntax Error)
# str4 = ("'hello '")  # Single quote within double quotes (Correct)

# TYPE 3: BOOLEAN
# The simplest built-in type in Python is bool, representing True or False.

print('\nHere are more type variables and their types:')
x = True
print(x)
print(type(x))

y = False
print(y)
print(type(y))

#  Example of boolean in condition
years_of_experience = 2
is_eligible = years_of_experience > 1
print("Is the candidate eligible?", is_eligible)
print(type(is_eligible))

#   Lists
# allows you to store a collection of items, which can be of any data type (integers, strings, floats,other lists).
# mutuable, allow duplicates, ordered

print (" \n From here Lists concept started :")
# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A mixed data type list
mixed = [1, "hello", 3.14, True]

# A nested list (list within a list)
nested = [1, [2, 3], [4, 5]]

# Empty list
empty_list = []


print(numbers)
print(fruits)
print(mixed)
print(nested)
print(empty_list)


#   LIST Slicing  (is same as string slicing)

print('List Slicing Concept: ')
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[0:3])  # Output: [10, 20, 30]
print(numbers[2:6])  # Output: [30, 40, 50, 60]
print(numbers[:4])   # Output: [10, 20, 30, 40]
print(numbers[4:])   # Output: [50, 60, 70, 80]
print(numbers[-4:-1])  # Output: [50, 60, 70]

# Reverse the List with Step -1
print("Reverse list: ",numbers[::-1])   # Output: [80, 70, 60, 50, 40, 30, 20, 10]

# Sorting a list .sort() method sorts orignal list
fruits = ['banana' , 'cherry' , 'apple', 'strawbery' , 'plum']
fruits.sort()  # Sorts in ascending order
# fruits.sort(reverse=True)
print(fruits)