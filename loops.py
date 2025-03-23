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
