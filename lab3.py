# # Question 1
# # Program to find numbers that are divisible by 7 and a multiple of 5
# # in the range 1500 to 2700 (both included)
#
# # Loop through numbers from 1500 to 2700
# for num in range(1500, 2701):
#     # Check if the number is divisible by both 7 and 5
#     if num % 7 == 0 and num % 5 == 0:
#         print(num)
#
# # -----------------------------------------------------------------------------------------------------
# ## Question 2 --> Temperature converter from Celsius to Fahrenheit and vice versa
# #
# # # Taking temperature input from the user
# # temp = float(input('Enter temperature: '))
# #
# # # Taking unit input (Celsius or Fahrenheit) and converting it to lowercase
# # unit = input('Celsius OR Fahrenheit (enter c/f): ').lower()
# #
# # # Checking if the user entered 'c' for Celsius
# # if unit == 'c':
# #     # Converting Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32
# #     converted_temp = temp * 1.8 + 32
# #     print(f'Temperature is {converted_temp}°F')
# #
# # # Checking if the user entered 'f' for Fahrenheit
# # elif unit == 'f':
# #     # Converting Fahrenheit to Celsius using the formula: C = (F - 32) * 5/9
# #     converted_temp = (temp - 32) * (5/9)
# #     print(f'Temperature is {converted_temp}°C')
# #
# # # Handling invalid unit input
# # else:
# #     print('Invalid unit. Please enter "c" for Celsius or "f" for Fahrenheit.')
# # -----------------------------------------------------------------------------------------------------
#
# # Question 3
# # program to guess a number b/t 1-9 prompt show again & again untill user enter correct guess
# # Program to guess a number between 1-9
# # Prompt will appear again & again until the user enters the correct guess
#
# correct_guess = 5  # Set the correct guess number
#
# while True:
#     try:
#         # Taking user input
#         guess_number = int(input('Guess a number: '))
#
#         # Checking if the guessed number is correct
#         if guess_number == correct_guess:
#             print('Well guessed! Good job!')
#             break  # Exit loop if correct guess
#
#     except ValueError:
#         # Handle invalid number input
#         print("Error: Please enter a valid number between 1-9.")
#
# # --------------------------------------------------------------------------------------------
#
# # Question 4 -->  print pattern using nested for loop & range function ...
#
# for i in range(0,6):  # range fron 0 to 5
#     print('*' * i)
# for i in range(4 , 0 , -1):   # range from 4 to 0 back
#     print('*' * i)
#
# # ------------------------------------------------------------------------------------------------
# # # Question 5 --> input a word from user and reverse it
#
# word = input(' Enter a word :')
# print(word[:: -1 ])
#
# # ------------------------------------------------------------------
# # Question 6
# # from series of number count no of enen and odd number
#
# numbers = (1,2,3,4,5,6,7,8,9,10)
# even_count = 0
# odd_count = 0
# for i in numbers:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f' Even count {even_count} \t Odd count {odd_count}')

# ------------------------------------------------------------------
# Question 7.
# Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in datalist:
    print ( f' {i}  -->   {type(i)}')

# ------------------------------------------------------------------
# Question 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note: Use the 'continue' statement.

for i in range(0,7):
    if i== 3 or i==6:
        continue
    else:
        print(i)

# ------------------------------------------------------------------
# Question 9. Write a Python program to get the Fibonacci series between 0 to 50.
num1 = 0
num2 = 1
print(num1 , num2 , end=" ")
while num1 + num2 < 50 :
    next_num = num1 + num2
    print(next_num , end=" ")
    num1 = num2
    num2 = next_num

# ------------------------------------------------------------------
# Question 10
# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number.
# For multiples of five print "Buzz".
# For numbers which are multiples of both three and five, print "FizzBuzz".

print('\n')
for i in range(1,51):
    if i % 3 == 0 and i % 5 ==0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print(i)

# #  ------------------------------------------------------------------
# # # Question 11
# # program that input rows and coloumn  and generate 2D array element of row coloumn should be (i*j)
# row = int(input('Enter no of rows '))
# col = int(input('Enter no of coloumn '))
# result = []
# for i in range(row):
#     new_row = []
#     for j in range(col):
#         new_row.append(i*j)
#     result.append(new_row)
#
# for i in result:
#     print(i)

# -------------------------------------------
# question 12
#  Write a Python program that accepts a sequence of lines (blank line to terminate)
# as input and prints the lines as output (all characters in lower case).

# Start an infinite loop to accept input from the user
print('Enter sequence of lines blank line to terminate ')
while True:
    line = input()  # Accept user input
    if line == "":  # Check if the input is a blank line
        break  # Exit the loop if the input is a blank line
    print(line.lower())  # Convert the line to lowercase and print it

#question 13
# input a string from user and count digits and letters in the string and display..
text = input("Enter a string: ")

letters = 0
digits = 0

for ch in text:
    if ch.isalpha():     #isalpha()  returns true if character is a letter
        letters += 1
    elif ch.isdigit():   #isdigit()  returns true if character is a digit
        digits += 1

print("Letters", letters)
print("Digits", digits)



