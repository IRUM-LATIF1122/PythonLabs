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

# SPECIAL CHARACTERS IN STRINGS
print('\nHere are some special characters used in strings:')

# \n for a new line
print("This is\nnew line command")

# \t for a horizontal tab
print("This is\t tab key command")

# \\ for a backslash
print("This is \\ back slash")

# \" for double quotes
print("This is \"double quote\"")

# \' for single quotes
print('This is \'single quote\'')

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

#   String indices and accessing string elements
#   Strings are arrays of characters and elements of an array can be accessed using indexing.
#   Indices start with 0 from left side and -1 when starting from right side.

string1 ="PYTHON TUTORIAL"
print("length of string is : ", len(string1))
string1 ="PYTHON TUTORIAL"
print(string1[0])   # output:    P    (print 1st character)

string1 ="PYTHON TUTORIAL"
print(string1[13])   # output:    A

string1 ="PYTHON TUTORIAL"
print(string1[-1])   # output:    L   (print last character)

string1 ="PYTHON TUTORIAL"
print(string1[14])   # output:    L   (print last character)

string1 ="PYTHON TUTORIAL"
print(string1[-15])   # output:    P   (print 1st character)

#   string1 ="PYTHON TUTORIAL"
#   print(string1[18])   # output:    IndexError string index out of range

#   STRING SLICING
#   In Python, string slicing is a way to extract a portion (substring) of a string using the syntax: string[start:end]
#   Key Points About String Slicing:
#   starting index (INclusive)
#   ending index  (Exclusive)

print("\n From here string slicing concept starts: ")

text = "PythonProgramming"
print(text[3:7])  # Output: "honP"

#   we can also use negative indices for slicing
text = "PythonProgramming"
print(text[-7:-1])   # Output: "rammin"

#   Omitting Indices:
#   Start omitted: Starts from the beginning.
#   End omitted: Goes to the end of the string.

text = "PythonProgramming"
print(text[:6])  # Output: "Python"
print(text[6:])  # Output: "Programming"

# STRING CONCATINATING ( COMBINING AND DISPLAYING 2 STRINGS)

name = input(' What\'s your name? ')
color = input(" What\'s your fav colour? ")
print(name + ' likes ' + color)

#Multi Line string we use tripple qoutes , ('''   ''') or ("""   """)

print('''Hi Irum
hope you are doing well
hows is your journey going ? ''')

# STRING FORMATING Lets we are concatinating some strings
# we want to display (  Irum [Noor] is a coder  )

first_name = input('enter first name ')
last_name = input('enter last name ')
msg = (first_name + ' [' + last_name + '] is a coder ')
print(msg)  # although it will display correct but its not good approach

# Approach 2  formatted string  its syntax = f'---'

formated_msg  = f'{first_name} [{last_name}] is a coder'
print(formated_msg)

