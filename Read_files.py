# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file1:
#     file_content = file1.read()
#     print(file_content)
# print('file1 closed')

# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file2:
#     file_content = file2.readline()
#     print(file_content)             # it will print line 1
#     file_content = file2.readline()
#     print(file_content)             # it will print line 2
#     file_content = file2.readline()
#     print(file_content)             # it will print line 3
#

# # we can also use loop --> file2.readline() reads only the first line of the file and returns it as a string.
# # When you loop over that, you're iterating character by character instead of by line.

# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file2:
#     for line in file2.readline():
#         print(line)
#
# # correct way to read line by line using loop
# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file2:
#     for line in file2.readlines():
#         print(line, end='')


# Description
# readlines()	Loads all lines into memory as a list	❌ No (not for big files)
# readline()	Reads only one line at a time	✅ Yes (but needs a loop)


# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file2:
#     line1 = file2.readline()  # Reads the first line
#     line2 = file2.readline()  # Reads the second line
#     print(line1)  # Print the first line
#     if 'important' in line2:
#         print('This line is important!')
#     else:
#         print('line is not that important')



#
# # Looping through lines:
# # Typically,
# # you use a loop to read lines until no more lines are left.
# # t's like reading the entire book, line by line.
#
# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file2:
#     while True:
#         line = file2.readline()
#         if not line:
#             break  # Stop when there are no more lines to read
#         print(line)



# # Reading a file in reverse order (from bottom to top)

# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file:
#     lines = file.readlines()  # Read all lines into a list
#     for line in reversed(lines):  # Iterate in reverse order
#         print(line, end='')

# Reading specific characters
# First, you need to open the file you want to read.
# If you want to read characters from a specific position in the file, you can use the seek() method.
# This method moves the file pointer (like a cursor) to a particular position. The position is specified in bytes

with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file:
    file.seek(15)   # Move to the 11th byte (0-based index)
    characters = file.read(8)  # Read the next 5 characters
    print(characters)
    file.close()


with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt", "r") as file:
    i = 0
    for line in file:
        print("Iteration", str(i), ": ", line)
        i = i + 1
