# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text2.txt" , "w") as file2:
#     file2.write('Hlo its text file no 2 \n')
#     file2.write('its been created by "w" mode ')
# print('sucessfully written')


# # we can copy content from 1 file and paste on another
# with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text1.txt" , "r") as readFile:
#     with open(r"C:\Users\Lenovo\PycharmProjects\PythonLabs\text2.txt" , "w") as writeFile:
#         copied_content = readFile.readlines()
#         for line in copied_content:
#             writeFile.write(line)
#


# Lines = ["This is line 1", "This is line 2", "This is line 3"]
# # Create a new file Example3.txt for writing
# with open('Example3.txt', 'w') as file2:
#     for line in Lines:
#         file2.write(line + "\n")
#     # file2 is automatically closed when the 'with' block exits



# # Data to append to the existing file
# new_data = "This is new line "
# # Open an existing file Example2.txt for appending
# with open('Example3.txt', 'a') as file1:
#     file1.write(new_data + "\n")
#     # file1 is automatically closed when the 'with' block exits


# ADDITIONAL MODES
# It's fairly ineffecient to open the file in "a" or "w" and then reopening it in "r" to read any lines.
# Luckily we can access the file in the following modes:
# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists.

# Let's try out the a+ mode:
# with open('Example3.txt', 'a+') as testwritefile:
#     testwritefile.write("This is line E\n")
#     testwritefile.seek(0)  # Move pointer to beginning of the file
#     print(testwritefile.read())
# as there is issue that after appending when we try to read cursor was at the end of file and we could not read anything

# # lets reVisit a+
# # Initially, a+ puts the file pointer at the end.
# # So the first read will give you nothing unless you do seek(0).
# # After seek(0, 0), you can read the whole file again.
#
# with open('Example3.txt', 'a+') as testwritefile:
#     print("Initial Location: {}".format(testwritefile.tell()))
#
#     data = testwritefile.read()
#     if (not data):  # empty strings return false in python
#         print('Read nothing')
#     else:
#         print(data)
#
#     testwritefile.seek(0, 0)  # move 0 bytes from beginning.
#
#     print("\nNew Location : {}".format(testwritefile.tell()))
#     data = testwritefile.read()
#     if (not data):
#         print('Read nothing')
#     else:
#         print(data)
#
#     print("Location after read: {}".format(testwritefile.tell()))




# # it overwrite existing data in file bus doesnot delete old data
# with open('Example3.txt', 'r+') as testwritefile:
#     testwritefile.seek(0,0) #write at beginning of file
#     testwritefile.write("Line 1" + "\n")
#     testwritefile.write("Line 2" + "\n")
#     testwritefile.write("Line 3" + "\n")
#     testwritefile.write("Line 4" + "\n")
#     testwritefile.write("finished\n")
#     testwritefile.seek(0,0)
#     print(testwritefile.read())



# What truncate() does:
# It removes everything after the current file pointer.
# Since you just finished writing and the pointer is at the end of the new content,
# it deletes any leftover content that was originally in the file.
with open('Example3.txt', 'r+') as testwritefile:
    testwritefile.seek(0, 0)  # write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    # Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0, 0)
    print(testwritefile.read())





