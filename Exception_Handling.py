# Exception handling in Python is a mechanism that allows a program to deal with unexpected errors gracefully instead of crashing.
# It Prevents program crashes due to runtime errors.
# Provides custom error messages for better debugging.
# Allows controlled execution even when errors occur.

try:
    # Code that may cause an error
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ZeroDivisionError:
    # Handles division by zero error
    print("Error: You can't divide by zero!")

except ValueError:
    # Handles invalid number input
    print("Error: Please enter a valid number!")

except Exception as e:
    # Catches any other exception
    print(f"An unexpected error occurred: {e}")

finally:
    # The finally block executes no matter what, whether an exception occurs or not.
    print("Execution completed.")

# How It Works
# The try block contains code that might cause an exception.
# If an error occurs, the corresponding except block catches the exception and executes custom error-handling code.
# The program does not crash and continues execution.


# using Try- except
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")


