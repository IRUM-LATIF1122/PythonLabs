# A while loop in Python is a control flow statement
# that repeatedly executes a block of code as long as a specified condition remains True.
# It is useful when the number of iterations is not known in advance.

# Let's see some examples

# Example 1: Printing a pattern using a while loop
i = 1  # Initializing variable i
while i < 6:  # Loop runs while i is less than 6
    print('*' * i)  # Prints '*' multiplied by the current value of i
    i += 1  # Increments i by 1 in each iteration
print('Done')  # Prints "Done" after the loop ends

# Example 2: Guessing Number Game
# The player has 3 chances to guess the correct number

guess_number = 9  # The correct number to guess
guess_counter = 0  # Counter to track the number of attempts

while guess_counter < 3:  # Loop runs while attempts are less than 3
    num = int(input('Guess a number: '))  # Taking user input as an integer
    if num == guess_number:  # Checking if the guessed number is correct
        print('You win!')  # Display win message
        break  # Exit the loop if the guess is correct
    else:
        guess_counter += 1  # Incrementing the attempt counter if guess is incorrect

# If the user fails to guess correctly within 3 attempts, the else block executes
else:
    print('Sorry, you failed!')  # Display failure message


# Another type of loop
# for loop in python
# For loops are used for sequential traversal. For example: traversing a list or string or array etc.


for items in 'Python':
    print(items)

# example 2
for items in [1,2,3,4,5,6]:
    print(items)    # 1, 2, ..., 5
# Range function bcz we cant make list of toooo many numbers

for items in range(15):
    print(items)    # 1, 2 3 ,......,14

for items in range(5 , 10 , 2):     #range(start, end, jump)
    print(items)    #output 5  7  9

for l in ['irum' , 'meeral' , 'honey' , 'buney']:
    print(l)

# # example to calculate total cost from given list using for loop

prices = [10, 20 ,30]
total_cost = 0
for total in prices:
    total_cost = total_cost + total
print(f'Total cost is {total_cost}PKR') # output .......60

# Nested loop in python loop within the loop is called nested loop
# lets see an example

for i in range(5):
    for j in range(3):
        print(f'( {i} , {j} )')

# lets print F shape fron x using  loop

list = [5,2,5,2,2]
for y in list:
    print('x' * y)

