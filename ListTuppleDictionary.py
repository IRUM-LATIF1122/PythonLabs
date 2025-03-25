#  Lists and tuples are both used to store multiple items in a single variable.
# allows you to store a collection of items, which can be of any data type (integers, strings, floats,other lists).
# mutuable, allow duplicates, ordered

# A list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])   # access zero index which is 1
print(numbers[-1])  # last index which is 5


# find maximum nuumber from given list ......................
list = [4,6,8,90,43,1,2,56]
max = list[0]
for item in list:
    if item > max:
        max = item
print(f'maximum from list is {max}')

# 2D list # A 2D list in Python is a list where each element is also a list.
#  It is used to represent matrices, grids, or tabular data.

# Creating a 2D list (Matrix representation)

matrix = [
    [1, 2, 3],   # Row 0
    [4, 5, 6],   # Row 1
    [7, 8, 9]    # Row 2
]

# Accessing elements in a 2D list
print(matrix[0][1])  # Output: 2 (Row 0, Column 1)
print(matrix[2][2])  # Output: 9 (Row 2, Column 2)

# Modifying elements in a 2D list
matrix[1][1] = 10  # Changes the element at Row 1, Column 1 to 10
print(matrix)  # Updated matrix: [[1, 2, 3], [4, 10, 6], [7, 8, 9]]

# Some predefine methods about lists
# append() is used to insert an element it inserts in end of list
list1 = [1, 2 ,3 ,4, 5, 5 , 5 , 6, 7]
list1.append(10)     #output  [1, 2 ,3 ,4, 5, 6, 7, 10]
print(list1)

# insert(_index, _object)  it inserts element on specific index in list
list1.insert(0, -1)  # [-1 , 1, 2 ,3 ,4, 5, 5 ,5 , 6, 7, 10]
print(list1)

# remove(object) it removes element from list
list1.remove(1) # [-1, 2 ,3 ,4, 5, 5, 5, 6, 7, 10]
print(list1)

# pop() it removes last item from list
list1.pop() # [-1, 2 ,3 ,4, 5, 5, 5, 6, 7]
print(list1)

# list1. count(_) it tell number of times object occur in list
print(list1.count(5))   # 3

# clear() it removes all items from string
list1.clear()   # []
print(list1)

# program to remove duplicates from the given list
numbers = [1, 2 ,3, 2, 4, 4, 5, 5, 6, 7, 7, 8 ,9 ,9 ,10]
new_list = []
for items in numbers:
    if items not in new_list:
        new_list.append(items)
print(new_list)


# ---- TUPLES ----
# Tuples are ordered, immutable (cannot be changed), and allow duplicates.
fruits_tuple = ("apple", "banana", "cherry")

# Accessing elements (indexing starts from 0)
print(fruits_tuple[1])  # Output: banana

# Tuples are immutable (cannot be changed after creation)
# fruits_tuple[1] = "mango"  # ❌ This will give an error

# A tuple with one element needs a comma (otherwise, it's just a string/int)
single_element_tuple = ("apple",)  # ✅ Correct
not_a_tuple = ("apple")  # ❌ Incorrect, this is a string

# Unpacking in Python means extracting values from a collection (like a list, tuple, or dictionary)
# and assigning them to variables in a single step.

# Define a tuple
fruits = ("apple", "banana", "cherry")

# Unpacking the tuple
fruit1, fruit2, fruit3 = fruits

print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry

# unpacking the  list
numbers = [10, 20, 30]

a, b, c = numbers
print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30

# Using * to Collect Remaining Values

numbers = [1, 2, 3, 4, 5]

a, b, *rest = numbers
print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]  (remaining values go into a list)

#  Unpacking in Loops
# You can use unpacking in loops when iterating over lists of tuples:

students = [("Alice", 20), ("Bob", 22), ("Charlie", 21)]

for name, age in students:
    print(f"{name} is {age} years old.")

# A dictionary in Python is a collection that stores data in key-value pairs. It is:
# Mutable (modifiable)
# Indexed by unique keys
# Efficient for data retrieval

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics"]
}
print(student["name"])  #accessing via []

print(student.get("age"))   # can also access via get() function

student["dateOfBirth"] =   "21,march 2004" # can add new key value pair
print(student.get("dateOfBirth"))

print(student)  # Output: {'name': 'Alice', 'age': 20, 'grade': 'A', 'subjects': ['Math', 'Physics']}

# an example program that input phone number and display it in english counting

ph_number = input('Enter phone no > ')
number_mapping = {
    "1" : "one ",
    "2" : "two ",
    "3" : "three ",
    "4" : "four ",
    "5" : "five ",
    "6" : "six ",
    "7" : "seven ",
    "8" : "eight ",
    "9" : "nine "

}
output = ""
for ch in ph_number:
    output += number_mapping.get(ch , "!")
print(output)

